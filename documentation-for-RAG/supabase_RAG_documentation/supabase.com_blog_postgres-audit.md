---
url: "https://supabase.com/blog/postgres-audit"
title: "Postgres Auditing in 150 lines of SQL"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Postgres Auditing in 150 lines of SQL

08 Mar 2022

•

13 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![Postgres Auditing in 150 lines of SQL](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupa-audit%2Fpostgres_auditing_in_150_lines_of_SQL.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Data auditing is a system that tracks changes to tables' contents over time.
PostgreSQL has a robust set of features which we can leverage to create a generic auditing solution in 150 lines of SQL.

Auditing is particularly useful for historical analysis. To demonstrate, imagine you have a `users` table that tracks when a user is online.
You might add a `status` column which can have one of two values: `online` and `offline`. How would you track how long a user is online for throughout an entire month?
An auditing system would track every change with timestamps, and so you can measure the difference between each timestamp and sum them up for the entire month.

The goals of our auditing solution are:

- low maintenance
- easy to use
- fast to query

To demonstrate what we're working towards, the following example shows what we'll have at the end of the blog post:

`
-- create a table
create table public.members (
id int primary key,
name text not null
);
-- Enable auditing on the new table
select audit.enable_tracking('public.members');
`

Produce some records to audit

`
-- create a new record
insert into public.members
(id, name)
values
(1, 'foo');
-- edit the record
update public.members
set name = 'bar'
where id = 1;
-- delete the record
delete from public.members;
`

Review the audit log

`
select * from audit.record_history;
`

`
id | record_id | old_record_id | op | ts | table_oid | table_schema | table_name | record | old_record
----+--------------------------------------+--------------------------------------+--------+-------------------------------------+-----------+--------------+------------+--------------------------+--------------------------
2 | 1ecd5ff0-1b6b-5bc2-ad80-1cb19769c081 | | INSERT | Mon Feb 28 18:13:52.698511 2022 PST | 16452 | public | members | {"id": 1, "name": "foo"} |
3 | 1ecd5ff0-1b6b-5bc2-ad80-1cb19769c081 | 1ecd5ff0-1b6b-5bc2-ad80-1cb19769c081 | UPDATE | Mon Feb 28 18:13:52.698511 2022 PST | 16452 | public | members | {"id": 1, "name": "bar"} | {"id": 1, "name": "foo"}
4 | | 1ecd5ff0-1b6b-5bc2-ad80-1cb19769c081 | DELETE | Mon Feb 28 18:13:52.698511 2022 PST | 16452 | public | members | | {"id": 1, "name": "bar"}
(3 rows)
`

Notice that our `record_id` and `old_record_id` stayed constant as we updated the row so we can easily query for a single row's history over time!

## Lets get building [\#](https://supabase.com/blog/postgres-audit\#lets-get-building)

### Namespace [\#](https://supabase.com/blog/postgres-audit\#namespace)

To quote a tenet from [the zen of python](https://www.python.org/dev/peps/pep-0020/):

> Namespaces are one honking great idea -- let's do more of those!

So first things first, we'll create a separate schema named `audit` to house our auditing entities.

`
create schema if not exists audit;
`

### Storage [\#](https://supabase.com/blog/postgres-audit\#storage)

Next, we need a table to track inserts, updates and deletes.

Classically, an audit table's schema mirrors the table being audited and appends some metadata columns like the commit's timestamp. That solution has a few maintenance challenges:

- enabling auditing on a table requires a database migration
- when the source table's schema changes, the audit table's schema must also change

So instead, we'll lean on PostgreSQL's schema-less [`JSONB` data type](https://www.postgresql.org/docs/current/datatype-json.html) to store each record's data in a single column.
That approach has the added benefit of allowing us to store multiple tables' audit history in a single audit table.

`
create table audit.record_version (
id bigserial primary key,
  -- auditing metadata
record_id uuid, -- identifies a new record by it's table + primary key
old_record_id uuid, -- ^
op varchar(8) not null, -- INSERT/UPDATE/DELETE/TRUNCATE
ts timestamptz not null default now(),
  -- table identifiers
table_oid oid not null, -- pg internal id for a table
table_schema name not null, -- audited table's schema name e.g. 'public'
table_name name not null, -- audited table's table name e.g. 'account'
  -- record data
record jsonb, -- contents of the new record
old_record jsonb -- previous record contents (for UPDATE/DELETE)
);
`

Postgres version compatibility

The table above uses PostgreSQL's built-in
[uuid functionality](https://www.postgresql.org/docs/14/functions-uuid.html), which is
available from version 14. For backwards compatibility you can use the uuid-ossp extension.

`create extension if not exists "uuid-ossp";`

### Query Patterns [\#](https://supabase.com/blog/postgres-audit\#query-patterns)

An audit log doesn't do us much good if its too slow to query! There are 2 query patterns we think are table stakes (😉) for an audit system:

**Changes to a Table in a Time Range**

For time slices, we need an index on the `ts` column. Since the table is append-only and the `ts` column is populated by insertion date, our values for `ts` are naturally in ascending order.

PostgreSQL's builtin [BRIN index](https://www.postgresql.org/docs/current/brin-intro.html) can leverage that correlation between value and physical location to produce an index that, at scale, is many hundreds of times smaller than the default (BTREE index) with faster lookup times.

`
-- index ts for time range filtering
create index record_version_ts
on audit.record_version
using brin(ts);
`

For table filtering, we've included a `table_oid` column which tracks PostgreSQL's internal numeric table identifier. We can add an index to this column instead of the `table_schema` and `table_name` columns, minimizing the index size and offering better performance.

`
-- index table_oid for table filtering
create index record_version_table_oid
on audit.record_version
using btree(table_oid);
`

**Changes to a Record Over Time**

One of the downsides to storing each row's data as `jsonb` is that filtering based on a column's value becomes very inefficient. If we want to look up a row's history quickly, we need to extract and index a unique identifier for each row.

For the globally unique identifier, we'll use the following structure

`
[table_oid, primary_key_value_1, primary_key_value_2, ...]
`

and hash that array as a UUID v5 to get an efficiently indexable UUID type to identify the row that is robust to data changes.

We'll use one utility function to lookup a record's primary key column names:

`
create or replace function audit.primary_key_columns(entity_oid oid)
    returns text[]
    stable
    security definer
    language sql
as $$
    -- Looks up the names of a table's primary key columns
    select
        coalesce(
            array_agg(pa.attname::text order by pa.attnum),
            array[]::text[]
        ) column_names
    from
        pg_index pi
        join pg_attribute pa
            on pi.indrelid = pa.attrelid
            and pa.attnum = any(pi.indkey)
    where
        indrelid = $1
        and indisprimary
$$;
`

and another to consume the `table_oid` and primary key, converting the result into the record's UUID.

`
create or replace function audit.to_record_id(
		entity_oid oid,
		pkey_cols text[],
		rec jsonb
)
    returns uuid
    stable
    language sql
as $$
    select
        case
            when rec is null then null
						-- if no primary key exists, use a random uuid
            when pkey_cols = array[]::text[] then gen_random_uuid()
            else (
                select
                    uuid_generate_v5(
                        'fd62bc3d-8d6e-43c2-919c-802ba3762271',
                        (
													jsonb_build_array(to_jsonb($1))
													|| jsonb_agg($3 ->> key_)
												)::text
                    )
                from
                    unnest($2) x(key_)
            )
        end
$$;
`

Finally, we index the `record_id` and `old_record_id` columns that contain these unique identifiers for fast querying.

`
-- index record_id for fast searching
create index record_version_record_id on audit.record_version (record_id)
where record_id is not null;
-- index old_record_id for fast searching
create index record_version_old_record_id on audit.record_version (record_id)
where old_record_id is not null;
`

### Enrollment [\#](https://supabase.com/blog/postgres-audit\#enrollment)

Okay, so we have a home for our audit data that we're confident it can be queried efficiently. Now how do we populate it?

We need the audit table to populate without end-users making any changes to their transactions. So we'll set up a [trigger](https://www.postgresql.org/docs/current/sql-createtrigger.html) to fire when the data changes. In this case, we'll fire the trigger once for every inserted/updated/deleted row.

`
create or replace function audit.insert_update_delete_trigger()
    returns trigger
    security definer
    language plpgsql
as $$
declare
    pkey_cols text[] = audit.primary_key_columns(TG_RELID);
    record_jsonb jsonb = to_jsonb(new);
    record_id uuid = audit.to_record_id(TG_RELID, pkey_cols, record_jsonb);
    old_record_jsonb jsonb = to_jsonb(old);
    old_record_id uuid = audit.to_record_id(TG_RELID, pkey_cols, old_record_jsonb);
begin
    insert into audit.record_version(
        record_id,
        old_record_id,
        op,
        table_oid,
        table_schema,
        table_name,
        record,
        old_record
    )
    select
        record_id,
        old_record_id,
        TG_OP,
        TG_RELID,
        TG_TABLE_SCHEMA,
        TG_TABLE_NAME,
        record_jsonb,
        old_record_jsonb;
    return coalesce(new, old);
end;
$$;
`

## Public API [\#](https://supabase.com/blog/postgres-audit\#public-api)

Finally, we'll wrap up the trigger creation and removal process behind a clean, idempotent, user facing API.

The API we'll expose for enabling auditing on a table is

`
select audit.enable_tracking('<schema>.<table>'::regclass);
`

and for disabling tracking

`
select audit.disable_tracking('<schema>.<table>'::regclass);
`

Under the hood, those functions register our auditing trigger against the requested table.

`
create or replace function audit.enable_tracking(regclass)
    returns void
    volatile
    security definer
    language plpgsql
as $$
declare
    statement_row text = format('
        create trigger audit_i_u_d
            before insert or update or delete
            on %I
            for each row
            execute procedure audit.insert_update_delete_trigger();',
        $1
    );
    pkey_cols text[] = audit.primary_key_columns($1);
begin
    if pkey_cols = array[]::text[] then
        raise exception 'Table % can not be audited because it has no primary key', $1;
    end if;
    if not exists(select 1 from pg_trigger where tgrelid = $1 and tgname = 'audit_i_u_d') then
        execute statement_row;
    end if;
end;
$$;
create or replace function audit.disable_tracking(regclass)
    returns void
    volatile
    security definer
    language plpgsql
as $$
declare
    statement_row text = format(
        'drop trigger if exists audit_i_u_d on %I;',
        $1
    );
begin
    execute statement_row;
end;
$$;
`

And we're done with 2 lines of code to spare!

### Performance [\#](https://supabase.com/blog/postgres-audit\#performance)

Auditing tables always reduces throughput of inserts, updates, and deletes. In cases where throughput is less than 1000 writes per second the overhead is typically negligible. For tables with a higher write frequency, consider logging changes outside of SQL with a tool like [pgAudit](https://www.pgaudit.org/).

### Do I really expect you to copy/paste all that? [\#](https://supabase.com/blog/postgres-audit\#do-i-really-expect-you-to-copypaste-all-that)

Nope, for a turnkey solution to auditing in PostgreSQL, we've packaged this script into an extension with some extra goodies like `TRUNCATE` support. Check it out at [https://github.com/supabase/supa\_audit](https://github.com/supabase/supa_audit).

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&text=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&text=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&t=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)

[Last post\\
\\
**Supabase Launch Week 4** \\
\\
25 March 2022](https://supabase.com/blog/supabase-launch-week-four)

[Next post\\
\\
**Supabase Beta January 2022** \\
\\
22 February 2022](https://supabase.com/blog/supabase-beta-january-2022)

[postgres](https://supabase.com/blog/tags/postgres) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Lets get building](https://supabase.com/blog/postgres-audit#lets-get-building)
  - [Namespace](https://supabase.com/blog/postgres-audit#namespace)
  - [Storage](https://supabase.com/blog/postgres-audit#storage)
  - [Query Patterns](https://supabase.com/blog/postgres-audit#query-patterns)
  - [Enrollment](https://supabase.com/blog/postgres-audit#enrollment)
- [Public API](https://supabase.com/blog/postgres-audit#public-api)
  - [Performance](https://supabase.com/blog/postgres-audit#performance)
  - [Do I really expect you to copy/paste all that?](https://supabase.com/blog/postgres-audit#do-i-really-expect-you-to-copypaste-all-that)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&text=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&text=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-audit&t=Postgres%20Auditing%20in%20150%20lines%20of%20SQL)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)