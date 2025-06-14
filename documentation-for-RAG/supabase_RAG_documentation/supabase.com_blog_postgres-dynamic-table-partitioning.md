---
url: "https://supabase.com/blog/postgres-dynamic-table-partitioning"
title: "Dynamic Table Partitioning in Postgres"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Dynamic Table Partitioning in Postgres

03 Oct 2023

•

25 minute read

[![Michel Pelletier avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmichelp.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Michel PelletierEngineering](https://github.com/michelp)

![Dynamic Table Partitioning in Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpartitions%2Fdynamic-table-partitioning-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We helped a customer recently who was storing 500 million chat messages in a single Postgres table. As the table was growing, their queries were slowing down.

The simple solution we offered was table partitioning. The difficulty was creating the partitions and migrating the data without blocking queries and downtime. This post explores the method we used to solve this - Dynamic Table Partitioning.

## Why Partition Data? The Large Table Problem [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#why-partition-data-the-large-table-problem)

When small projects get big, millions of rows can quickly grow to billions of rows. This presents several challenges when storing data in a single table:

- **SELECTs get slower as an index grows.** The most common index type in Postgres is a btree, which is a tree like structure. To find a row, that tree must be "walked" from the root to the appropriate leaf node where the new values exist. The larger the index, the more nodes need to be traversed.
- **INSERTs get slower as an index grows.** For many of the same reasons that SELECTs get slower, indexes must again be "walked" to find leaf nodes where a value needs to be inserted. If the leaf node is fully occupied, new nodes must be added. The larger a table gets, the longer this process takes.
- **Data can become less relevant.** The utility of real-world data often decreases with time. For example, chat messages are most useful when they sent, but over time the frequency that you a user will read them decreases. Old chat messages take up space in your table, and querying new chat messages suffers as a result.
- **Large tables mix unrelated data.** Often unrelated data is stored together, and so a select statement needs to scan through many irrelevant rows. Using our chat example: maybe it's unusual for users from one organization to be chatting with a different organization. It would be better if each organizations data was split into separate blocks of storage.
- **Large tables prevent vacuum operations from completing.** Vacuuming is one of the most mysterious aspects of Postgres. Due to the concurrency model of Postgres (MVCC) updated or deleted rows are not immediately removed from storage, but instead are marked deleted. In the background, Postgres will occasionally remove these "dead" rows and reclaim their storage for newly updated or inserted rows. The bigger a table gets, the longer this vacuuming process can take. If your table is being updated frequently it can block this process from completing successfully.
- **Large tables mean more data to move around.** Usually to test new features you don't need _all_ of your production data, just a small subset of it. Perhaps you only need a month of analytics data, or a day of chats. By partitioning your data into smaller chunks, you can choose to load just enough that you need to run the test you have in mind. This pattern is called Incremental Data Loading.
- **Archiving older data is easier done in well defined partitions.** The flip side of the incremental data loading problem is incremental archiving. Old data often become so irrelevant that it cost prohibitive to keep it in live database tables. By using dynamic partitioning older partitions can be detached and archived into a cheaper “cold storage” and then loaded again and re-attached only as needed.

## Starting small but getting big [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#starting-small-but-getting-big)

A common growing pain for small startups is that they start their database model in a very simple and straightforward way, but then their popularity explodes and so does the amount of data they need to store. Postgres is good at handling millions of rows in a single table, but often there is that one table in a system, the “Large Table”, that grows at a daily rate into hundreds of millions of rows.

Partitioning is a simple solution, but for Postgres this usually requires setting up the partitions at the same time that you create your tables. The challenge is figuring out how to create the partitions _after_ you have millions of rows in your database, and how to migrate those existing rows into your new partitioning scheme with minimal downtime.

Let’s explore a working example showing how to escape this situation using dynamic table partitioning. We’ll setup a simulated “chat app” that has to store possibly millions of chat messages per day. The first step is to set up a fake “Large Table” problem to simulate a data set that has grown past where Postgres can handle it all in one table. So first, we’ll add a couple of new tables for our example chat app:

`
create table chats (
id bigserial,
created_at timestamptz not null default now(),
primary key (id)
);
create table chat_messages (
id bigserial,
created_at timestamptz not null,
chat_id bigint not null,
chat_created_at timestamptz not null,
message text not null,
primary key (id),
foreign key (chat_id) references chats (id)
);
`

The first table holds `chats` which are conversations between parties in the app, and the second table holds `chat_messages` which are the individual messages sent back-and-forth in the chat. Notice that in this example, we don’t include any columns to describe the sender or receivers of these chats for simplicity’s sake, that problem is left up to you to solve, but would likely involve some kind of foreign key references from the `chats` table to your user tables in an application. Here we are only interested in the structure of the message storage itself.

Next we have to synthesize some fake data. We’ll `INSERT` some chat rows over a span of time, and then `INSERT` some chat messages into those chats. You can tweak how much data is created by adjusting the “beginning” and “end” timestamps below. We’re only setting up one month of data but you can increase the timespan or decreasing the one hour interval between chats for more rows.

`
INSERT INTO chats (created_at)
SELECT generate_series(
'2022-01-01'::timestamptz,
'2022-01-30 23:00:00'::timestamptz,
interval '1 hour'
);
INSERT INTO chat_messages (
	created_at,
	chat_id,
	chat_created_at,
	message
)
SELECT
mca,
chats.id,
chats.created_at,
(SELECT ($$[0:2]={'hello','goodbye','I would like a sandwich please'}$$::text[])[trunc(random() * 3)::int])
FROM chats
CROSS JOIN LATERAL (
    SELECT generate_series(
        chats.created_at,
        chats.created_at + interval '1 day',
        interval '1 minute'
		) AS mca
) b;
CREATE INDEX ON chats (created_at);
CREATE INDEX ON chat_messages (created_at);
`

## Dynamic partitioning with pl/pgSQL [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#dynamic-partitioning-with-plpgsql)

Next we’ll show a simple partitioning strategy that provides a starting point for your own partitioning tooling using the above “Large Table” fake data, using some of the partitioning patterns described in the Intro above.

First, we should explain Postgres table partitioning a bit more. A Partitioned table can be thought of as a “parent” table with a bunch of “children” tables that are “attached” to it. By breaking one large table into many smaller tables, there are many performance and administrative benefits. When you query a partitioned table, you query the **parent** table just like you would any other Postgres table, but internally, Postgres knows how to delegate those queries down to the **children** in the most optimal way.

Child tables are partitioned by some key column in the rows of data that they store. In our “chat” example, this key will be the `created_at` timestamp. We’ll partition the day into “daily” partitions, so that each child table holds one day’s worth of chat messages. When you create a new child partition table, you must tell Postgres what the range of dates are that the table will hold, this is how Postgres knows where to store and find chat messages in partitions. You’ll see how in our examples below, our child partition table names contain the date of the day that the partition holds, so `chats_2023-08-03` is a child partition table for August 3rd, 2023.

If you query the parent tables but do not provide a `WHERE` clause value for the creation date or range of dates you are looking for, then Postgres must look in **_all_** the child tables, this can take some time for lots of data, so make sure you’re always trying to constrain your queries by small range of time so that Postgres can optimize finding that data by looking in the minimum number of child partitions necessary.

In our example below, we will be copying lots of existing chat messages out of one big table into new partitions that we will be creating “on the fly” so to speak, so we must make sure that the rows we insert into each new child partition fall into the right day’s time range. This per-child range of time is called the **partitioning constraint**. When we copy data into the new tables, we will use a trick by first creating a **check constraint** that will force Postgres to make sure that the constraint **_holds_** for every row, it will throw an error if you try to put a row outside of a child’s partition constraint range.

After we have pre-loaded a new child table with copied rows and verified that the rows are valid with a check constraint, then we can **attach** the partition to the parent table with `ATTACH PARTITION ...` command. This will make the new range of child data available for queries on the parent table.

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpartitions%2Fdynamic-table-partitioning-diagram-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Postgres partitioning became significantly easier in recent versions. Postgres added the new syntax for [Declarative Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html#DDL-PARTITIONING-DECLARATIVE) that makes it easy to create new partitions by adding additional details to your `CREATE TABLE` statements:

`
CREATE TABLE measurement (
city_id int not null,
logdate date not null,
peaktemp int,
unitsales int
) PARTITION BY RANGE (logdate);
`

But in many cases like those discussed above, there are some wrinkles to simple partitioning that can end up blocking queries if you want to first pre-load data into a partition before attaching it to a parent. So there are in general two approaches, a new child can be declared when the table is created, but it must be empty.

The approach described in this post is that a standalone table is created, filed with data, and then “attached” to the parent table, but this option has a downside if it is not done carefully: if the newly filled table is not setup properly, Postgres will lock the parent table with an `EXCLUSIVE ACCESS` lock that prevents queries while Postgres ensure that the new partition only contains data that falls within the partitions data range, called a **partition constraint**. In order to avoid this locking, this constraint must first be added to the standalone table so that Postgres does not need to scan it first.

For example if you partition your data per-day, then Postgres must ensure that there are no rows in the new table that fall outside the boundaries of a given date range that you intend to attach the table with. This blog post provide a simple approach to address this problem with some plpgsql functions that you can quickly and easily adapt to your needs.

There is no one size fits all solution for Partitioning so you will likely have to modify this example to suit your needs. Read the official [Table Partitioning Docs](https://www.postgresql.org/docs/current/ddl-partitioning.html) so that you understand all the issue involved. Partitioning can be a complex subject, but hopefully this code will get you started down the road to high scalability with very large data sets!

## Creating Parent Tables [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#creating-parent-tables)

The example model shown here is a "chat" app, where there is a table of "chats" that act as a container for a bunch of chat messages.

Since user representation is a highly application specific concept, I leave it as an exercise to you how you want to associated these messages with any kind of user system. A likely approach would be to add foreign key references to the `chats` table that contain the ids of the parties of the chat. For simple person to person chats, this could be as simple as two columns, for multi-party chats, you’ll have to come up with a many-to-many join table that relates chats to participants.

`
BEGIN;
CREATE SCHEMA app;
CREATE TABLE app.chats(
    id bigserial,
    created_at timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (id, created_at)  -- the partition column must be part of pk
    ) PARTITION BY RANGE (created_at);
CREATE INDEX "chats_created_at" ON app.chats (created_at);
CREATE TABLE app.chat_messages(
    id bigserial,
    created_at timestamptz NOT NULL,
    chat_id bigint NOT NULL,
    chat_created_at timestamptz NOT NULL,
    message text NOT NULL,
    PRIMARY KEY (id, created_at),
    FOREIGN KEY (chat_id, chat_created_at)   -- multicolumn fk to ensure
        REFERENCES app.chats(id, created_at)
    ) PARTITION BY RANGE (created_at);
CREATE INDEX "chat_messages_created_at" ON app.chat_messages (created_at);
--
-- need this index on the fk source to lookup messages by parent
--
CREATE INDEX "chat_messages_chat_id_chat_created_at"
    ON app.chat_messages (chat_id, chat_created_at);
`

In this model, chats are partitioned by their creation data, this can be seen with the `PARTITION BY RANGE` clause. We will be creating a new partition for every day, this means that every day a new table will be created for "today's" chat messages. Without partitioning, every day queries to the table would get slower and slower, but with partitioning, the query times remain consistent. Both the `chats` and `chat_messages` tables will be partitioned by day. This makes the model fairly simple, but there is a wrinkle, chats can span _multiple days_, so that's something to keep in mind if you want to keep your data consistent.

Another detail is that the primary key for the `chats` and `chat_messages` tables have _two_ columns. This is called a "composite" primary key. This is important because the job of a primary key is to uniquely identify the row, and in the case of a partitioned table it must also _uniquely identity the partition_. So the partitioned column `created_at` must be part of the primary key. This is an important structural requirement for partitioning, and it allows Postgres to quickly work with partitioned data, since Postgres always knows which partition table any given primary key will be stored it, it does not have to check all partitions on every operation, which would be prohibitively slow.

Note that this composite primary keys mean that any foreign keys that reference it must also be composite. This can be seen in the `FOREIGN KEY` clause in the `CREATE TABLE` statement for `chat_messages`. This can be tricky because even though it is a totally normal and common SQL pattern that has existed in Postgres and other databases for decades, many ORM like tools in various languages still do not understand or support the notion of composite keys. If this is the case for you, you may want to reconsider using a tool that does not understand standard SQL patterns like this. Powerful ORMs like [sqlalchemy](https://www.sqlalchemy.org/) have no problem with composite keys, but even popular tools like Django do not support them, in fact in Django, there is [an 18 year old ticket on the issue](https://code.djangoproject.com/ticket/373) of supporting composite keys.

Finally note there is a `CREATE INDEX` statement that creates an index on the foreign key relationship in the `chat_messages` table. This is to ensure that looking up a `chat_messages` row from a `chats` row is fast, otherwise, the `chat_messages` table would have to be scanned, which is definitely something to avoid!

## Creating Dynamic Child Tables [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#creating-dynamic-child-tables)

Now that we have our parent tables created, it's time to make some partitions! There are two steps to this process, so I have broken them into two `PROCEDURE` objects for each table. Postgres procedures are like functions, but they cannot be used in many contexts that function can be used such as RLS policies, computed indexes, default expressions, etc. They can only be called with the `CALL procedure_name(args)` syntax, to avoid accidental misuse. Procedures can also take part in transaction control which we’ll get into a little later in this post.

A complete code example is shown below for both the `chats` and `chat_messages` tables, so I’ll only be explaining the partitioning code for the `chats` table, they are both very similar so you should have no problem adapting this pattern to one or more tables in your database.

In order to create new partitions, we need to know the day to create the table for, this is the only argument to the procedure `partition_day`. Also we will be creating new tables with the day as part of the child partition table name, so we need to execute "dynamic" SQL. This is done with the `EXECUTE` keyword that will execute of string of SQL code. Because we have to format that string, we use the `format()` function to render the SQL string that is executed, this is meta-programming in Postgres! It's not pretty but it works great, and in this case it exactly accomplishes our goal.

Note how the child partitions are created using the `LIKE` clause so they get the exact schema of the parent table, and the clauses `INCLUDING DEFAULTS INCLUDING CONSTRAINTS` means the child tables get their own copies of the parent table's default values and constraints like foreign keys.

`
--
-- Function creates a chats partition for the given day argument
--
CREATE OR REPLACE PROCEDURE app.create_chats_partition(partition_day date)
    LANGUAGE plpgsql AS
$$
BEGIN
    EXECUTE format(
    $i$
        CREATE TABLE IF NOT EXISTS app."chats_%1$s"
        (LIKE app.chats INCLUDING DEFAULTS INCLUDING CONSTRAINTS);
    $i$, partition_day);
END;
$$;
`

In the full code listing, there is a similar function `create_chat_messages_partition()` that does the same thing for the `chat_messages` tables.

Once we have created our child partition tables using the `create_chats_partition()` procedure, it's time to index and attach those child tables to the parent.

Some important details below, primary keys are added after the data is loaded, this is so the index creation for those keys happens as quickly as possible. Also as noted above, a `CHECK` constraint is added to the child tables to ensure they do not violate the parent tables `PARTITION BY RANGE` constraint, this avoid any unnecessary `EXCLUSIVE ACCESS` locking on the parent tables when they are attached. This type of lock causes downtime because it blocks all access to a table, including `SELECT` queries. For hundreds of millions of rows of data which could take several hours to copy, you can’t afford to have that long of a downtime of your application.

Avoiding this locking time is an important optimization to make sure you can do the migration from the large table without causing downtime by blocking queries on the parent table. Since the _check constraint_ exactly matches the _partition constraint_ Postgres knows that it can attach the table without having to lock it and scan it for validity. The check constraint already proves the validity of the data in the new child partition, so Postgres doesn’t have to re-prove it at attachment time and can attach the new child partition without blocking any other queries.

After loading the data, you may also create any other indexes needed for the application, like the foreign key index on `chat_messages` we discussed previously. It’s always faster to create indexes after bulk loading data into a table, than to create the indexes first before loading the data, since the indexes slow down each insert more than the total time it takes to scan the table and create an index. This is another important optimization that speeds up the copying process.

Finally the magic happens, `ATTACH PARTITION ... FOR VALUES FROM <low> TO <high>` is used to attach the new child partition table to the parent. Since all constraints are known to be verified with the primary key and `CHECK` constraints, this will happen without locking. Next, the newly created indexes are also attached with `ALTER INDEX ... ATTACH PARTITION`. Finally, the `CHECK` constraints that were so helpful to avoid table locking are now no longer necessary, so they can be dropped with `ALTER TABLE ... DROP CONSTRAINT`.

`
CREATE OR REPLACE PROCEDURE app.index_and_attach_chats_partition(partition_day date)
    LANGUAGE plpgsql AS
$$
BEGIN
    EXECUTE format(
    $i$
        -- now that any bulk data is loaded, setup the new partition table's pks
        ALTER TABLE app."chats_%1$s" ADD PRIMARY KEY (id, created_at);
        -- adding these check constraints means postgres can
        -- attach partitions without locking and having to scan them.
        ALTER TABLE app."chats_%1$s" ADD CONSTRAINT
               "chats_partition_by_range_check_%1$s"
           CHECK ( created_at >= DATE %1$L AND created_at < DATE %2$L );
        -- add more partition indexes here if necessary
        CREATE INDEX "chats_%1$s_created_at"
            ON app."chats_%1$s"
            USING btree(created_at)
            WITH (fillfactor=100);
        -- by "attaching" the new tables and indexes *after* the pk,
        -- indexing and check constraints verify all rows,
        -- no scan checks or locks are necessary, attachment is very fast,
        -- and queries to parent are not blocked.
        ALTER TABLE app.chats
            ATTACH PARTITION app."chats_%1$s"
        FOR VALUES FROM (%1$L) TO (%2$L);
        -- You now also "attach" any indexes you made at this point
        ALTER INDEX app."chats_created_at"
            ATTACH PARTITION app."chats_%1$s_created_at";
        -- Dropping the now unnecessary check constraint they were just needed
        -- to prevent the attachment from forcing a scan to do the same check
        ALTER TABLE app."chats_%1$s" DROP CONSTRAINT
            "chats_partition_by_range_check_%1$s";
    $i$,
    partition_day, (partition_day + interval '1 day')::date);
END;
$$;
`

Again, there is a full code listing below that shows a similar procedure for `index_and_attach_chat_messages_partition`.

## Progressively Copying Data from the Large Tables [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#progressively-copying-data-from-the-large-tables)

Now that the partition creation and attachment code is in place, it’s time to create one last set of procedures for copying the data over from the old “Large Table” to the new partitioning scheme. This is a procedure that pretty much just does a simple `INSERT` of the new data that is `SELECT` ed from the old data.

Something worth noting is that the selected data is `ORDER BY` the `created_at` column. This means that all the rows that are inserted into the new partition are naturally ordered by their creation date, this tends to improve cache efficiency by keeping recent messages close together in the same database block files:

`
--
-- Function copies one day's worth of chats rows from old "large"
-- table new partition.  Note that the copied data is ordered by
-- created_at, this improves block cache density.
--
CREATE OR REPLACE PROCEDURE app.copy_chats_partition(partition_day date)
    LANGUAGE plpgsql AS
$$
DECLARE
    num_copied bigint = 0;
BEGIN
    EXECUTE format(
    $i$
        INSERT INTO app."chats_%1$s" (id, created_at)
        SELECT id, created_at FROM chats
        WHERE created_at::date >= %1$L::date AND created_at::date < (%1$L::date + interval '1 day')
        ORDER BY created_at
    $i$, partition_day);
    GET DIAGNOSTICS num_copied = ROW_COUNT;
    RAISE NOTICE 'Copied % rows to %', num_copied, format('app."chats_%1$s"', partition_day);
END;
$$;
`

## Putting it all together: Creating, Copying, Indexing, Attaching [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#putting-it-all-together-creating-copying-indexing-attaching)

Now the final procedure we need is a wrapper that puts it all together, creating a partition, copying the old data into the new table, indexing the new table, and then attaching it to the parent.

The way this is going to work is that a procedure will create partitions for a whole range of days, and copy over each day one by one, calling `COMMIT` between each day so that the new table grows incrementally without blocking or locking other database sessions. Note that this procedure _works backwards_ from the newest chats to the oldest (this is the `interval '-1 day'` argument to `generate_series()`). So that the new tables can be immediately useful even as you are still loading old data. As above, we’ll just show the example procedure for `load_chats_partitions()`.

`
--
-- Wrapper function to create, copy, index and attach a given day.
--
CREATE OR REPLACE PROCEDURE app.load_chats_partition(i date)
    LANGUAGE plpgsql AS
$$
BEGIN
    CALL app.create_chats_partition(i);
    CALL app.copy_chats_partition(i);
    CALL app.index_and_attach_chats_partition(i);
END;
$$;
--
-- This procedure loops over all days in the old table, copying each day
-- and then committing the transaction.
--
CREATE OR REPLACE PROCEDURE app.load_chats_partitions()
    LANGUAGE plpgsql AS
$$
DECLARE
    start_date date;
    end_date date;
    i date;
BEGIN
    SELECT min(created_at)::date INTO start_date FROM chats;
    SELECT max(created_at)::date INTO end_date FROM chats;
    FOR i IN SELECT * FROM generate_series(end_date, start_date, interval '-1 day') LOOP
        CALL app.load_chats_partition(i);
        COMMIT;
    END LOOP;
END;
$$;
`

Notice how that the `COMMIT` statement happens inside the loop after every create, copy, and attach procedure. This allows other sessions to see the new data as it’s being committed so that the new tables are usable even as the old data is being loaded.

And finally, it’s time to kick off the whole process by calling the `load_` procedures:

`
CALL app.load_chats_partitions();
CALL app.load_chat_messages_partitions();
`

## Setting up a Daily Cron Job to Create Partitions [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#setting-up-a-daily-cron-job-to-create-partitions)

This old school but simple tool will run a scheduled "job" every night at 23:00, one hour before midnight to create the partition for the next day. I'll leave it as an exercise to you if want to try and elaborate this a bit and ensure a whole weeks worth of partitions are created in advance, this would give you a bit more leeway to avoid downtime if the cron job happened to fail, giving you several days to solve the problem instead of one hour.

`
--
-- This procedure will be used by pg_cron to create both new
-- partitions for "today".
--
CREATE OR REPLACE PROCEDURE app.create_daily_partition(today date)
    LANGUAGE plpgsql AS
$$
BEGIN
    CALL app.create_chats_partition(today);
    CALL app.create_chat_messages_partition(today);
END;
$$;
SELECT cron.schedule('new-chat-partition', '0 23 * * *', 'CALL app.create_daily_partition(now()::date + "interval 1 day")');
COMMIT;
`

## Complete Example Code [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#complete-example-code)

And that's it! While there is some complexity, I hope this example has given you some ideas on how you too can partition your data for optimal query performance. There are many ways to slice this problem depending on your needs, while I showed one simple common approach to partition time series data by date range, there are a lot of other approaches and I suggest you go over the official Postgres Table Partitioning documentation to see how other patterns may apply to your situation.

[See the full code example on GitHub](https://github.com/supabase/supabase/tree/master/examples/enterprise-patterns/supachat)

## More Postgres Resources [\#](https://supabase.com/blog/postgres-dynamic-table-partitioning\#more-postgres-resources)

- [Table Partitioning Docs](https://www.postgresql.org/docs/current/ddl-partitioning.html)
- [pgvector v0.5.0: Faster semantic search with HNSW indexes](https://supabase.com/blog/increase-performance-pgvector-hnsw)
- [Choosing a Postgres Primary Key](https://supabase.com/blog/choosing-a-postgres-primary-key)
- [pg\_jsonschema: JSON Schema support for Postgres](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation)
- [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-dynamic-table-partitioning&text=Dynamic%20Table%20Partitioning%20in%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-dynamic-table-partitioning&text=Dynamic%20Table%20Partitioning%20in%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-dynamic-table-partitioning&t=Dynamic%20Table%20Partitioning%20in%20Postgres)

[Last post\\
\\
**Supabase Beta September 2023** \\
\\
4 October 2023](https://supabase.com/blog/beta-update-september-2023)

[Next post\\
\\
**Supabase Beta August 2023** \\
\\
8 September 2023](https://supabase.com/blog/beta-update-august-2023)

[postgres](https://supabase.com/blog/tags/postgres)

On this page

- [Why Partition Data? The Large Table Problem](https://supabase.com/blog/postgres-dynamic-table-partitioning#why-partition-data-the-large-table-problem)
- [Starting small but getting big](https://supabase.com/blog/postgres-dynamic-table-partitioning#starting-small-but-getting-big)
- [Dynamic partitioning with pl/pgSQL](https://supabase.com/blog/postgres-dynamic-table-partitioning#dynamic-partitioning-with-plpgsql)
- [Creating Parent Tables](https://supabase.com/blog/postgres-dynamic-table-partitioning#creating-parent-tables)
- [Creating Dynamic Child Tables](https://supabase.com/blog/postgres-dynamic-table-partitioning#creating-dynamic-child-tables)
- [Progressively Copying Data from the Large Tables](https://supabase.com/blog/postgres-dynamic-table-partitioning#progressively-copying-data-from-the-large-tables)
- [Putting it all together: Creating, Copying, Indexing, Attaching](https://supabase.com/blog/postgres-dynamic-table-partitioning#putting-it-all-together-creating-copying-indexing-attaching)
- [Setting up a Daily Cron Job to Create Partitions](https://supabase.com/blog/postgres-dynamic-table-partitioning#setting-up-a-daily-cron-job-to-create-partitions)
- [Complete Example Code](https://supabase.com/blog/postgres-dynamic-table-partitioning#complete-example-code)
- [More Postgres Resources](https://supabase.com/blog/postgres-dynamic-table-partitioning#more-postgres-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-dynamic-table-partitioning&text=Dynamic%20Table%20Partitioning%20in%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-dynamic-table-partitioning&text=Dynamic%20Table%20Partitioning%20in%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-dynamic-table-partitioning&t=Dynamic%20Table%20Partitioning%20in%20Postgres)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpartitions%2Fdynamic-table-partitioning-diagram-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)