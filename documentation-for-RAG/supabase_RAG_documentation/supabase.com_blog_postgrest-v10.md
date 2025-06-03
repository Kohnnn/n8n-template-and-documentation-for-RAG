---
url: "https://supabase.com/blog/postgrest-v10"
title: "PostgREST v10: EXPLAIN and Improved Relationship Detection"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# PostgREST v10: EXPLAIN and Improved Relationship Detection

19 Aug 2022

•

8 minute read

[![Steve Chavez avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsteve-chavez.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Steve ChavezEngineering & PostgREST maintainer](https://github.com/steve-chavez)

![PostgREST v10: EXPLAIN and Improved Relationship Detection](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5%2Fpostgrest-v10.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

PostgREST turns your PostgreSQL database automatically into a RESTful API. Today, PostgREST v10 was [released](https://github.com/PostgREST/postgrest/releases/tag/v10.0.0). v10 is not available on the Supabase Platform yet, but it is available for [self-hosting](https://supabase.com/docs/guides/hosting/overview) or as a executable binary from the GitHub release page.

Let's take a look at some of its new features that go hand in hand with [supabase-js v2](https://supabase.com/blog/supabase-js-v2).

## EXPLAIN [\#](https://supabase.com/blog/postgrest-v10\#explain)

Akin to the [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/sql-explain.html) command, you can now get the execution plan of a request through HTTP or `supabase-js`. This works transparently for reads, writes and RPC because every request to PostgREST generates a single SQL query.

This is only suitable for development environments and is only enabled when the `db-plan-enabled` config is set to `true`.

### Getting the execution plan through HTTP [\#](https://supabase.com/blog/postgrest-v10\#getting-the-execution-plan-through-http)

Using `curl`, you can obtain the execution plan by specifying a vendor media type on the `Accept` header.

`
$ curl -H 'Accept: application/vnd.pgrst.plan' \
       'https://<project>.supabase.co/rest/v1/clients?select=*&id=eq.1'
Aggregate  (cost=8.18..8.20 rows=1 width=112)
  ->  Index Scan using clients_pkey on clients  (cost=0.15..8.17 rows=1 width=36)
        Index Cond: (id = 1)
`

The `text` format is used by default, which gives you the same output you’d get in other SQL clients like `psql`. You can change the format to JSON by using a media type suffix `application/vnd.pgrst.plan+json`.

### Explaining supabase-js queries [\#](https://supabase.com/blog/postgrest-v10\#explaining-supabase-js-queries)

For `supabase-js`, you can get the execution plan using the `explain()` transform. This works for every `supabase-js` method, including `rpc()`. Here’s an example for `select()`.

`
const { data, error } = await supabase
.from('projects')
.select('*')
.eq('id', 1)
.explain()
console.log(data)
`

hideCopy

`
Aggregate  (cost=8.18..8.20 rows=1 width=112)
  ->  Index Scan using projects_pkey on projects  (cost=0.15..8.17 rows=1 width=40)
        Index Cond: (id = 1)
`

Explaining the plan output in detail is beyond the scope of this blog post but basically it’s a tree of operations that PostgreSQL will follow for executing a query. Here we see the “Aggregate” node which corresponds to the `json_agg` function used by the PostgREST generated query(more details on how to find these later) and the “Index Scan” node which means an index on “id” was used for a fast search.

### Explaining RLS policies [\#](https://supabase.com/blog/postgrest-v10\#explaining-rls-policies)

The raison d'etre of `explain()` is to provide quicker feedback on the performance of queries, especially in the presence of RLS policies. For instance, let’s say we have this basic policy:

`
create policy "anon can't read"
on projects for select to anon
using (
false
);
`

And we use `explain()` again, this time with the `analyze` option(executes the query, same as the EXPLAIN ANALYZE counterpart in SQL) so we can see the execution time.

`
const { data, error } = await supabase
.from('projects')
.select('*')
.eq('id', 1)
.explain({ analyze: true })
console.log(data)
`

hideCopy

`
Aggregate  (cost=8.18..8.20 rows=1 width=112) (actual time=0.017..0.018 rows=1 loops=1)
  ->  Index Scan using projects_pkey on projects  (cost=0.15..8.17 rows=1 width=40) (actual time=0.012..0.012 rows=0 loops=1)
        Index Cond: (id = 1)
        Filter: false
        Rows Removed by Filter: 1
Planning Time: 0.092 ms
Execution Time: 0.046 ms
`

Here you can see the “Filter” node, which is a simple `false` as defined by the above policy, this proves that the RLS policy is getting applied. Also the actual “Execution Time” is shown, which is a fraction of a millisecond. Note that this is only the query execution time, it doesn’t account for the latency for transferring the data from the database to the frontend.

### Getting the Query Identifier [\#](https://supabase.com/blog/postgrest-v10\#getting-the-query-identifier)

`explain()` is also useful for getting the [pg\_stat\_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) query identifier, which you can use in the Supabase logs to obtain the generated SQL queries. Here we use the json `format` and the `verbose` option to get it.

`
const { data, error } = await supabase
.from('projects')
.select('*')
.eq('id', 1)
.explain({ format: 'json', verbose: true })
console.log(data[0]['Query Identifier'])
// 2811722635570756600
`

For getting more detailed information, you can also use the `settings`, `buffers`, `wal` options with `explain()` .

## Improved Relationship Detection [\#](https://supabase.com/blog/postgrest-v10\#improved-relationship-detection)

### One-to-one relationships [\#](https://supabase.com/blog/postgrest-v10\#one-to-one-relationships)

To avoid unnecessary JSON arrays in a query result, one-to-one relationships are now automatically detected. For this you can use a:

`
-- A unique constraint on a foreign key
create table country (
id serial primary key,
name text
);
create table capital (
id serial primary key,
name text,
country_id int unique,
foreign key (country_id) references country (id)
);
-- or a primary key on a foreign key
create table country (
id serial primary key,
name text
);
create table capital (
id serial primary key,
name text,
foreign key (id) references country (id)
);
`

Both options should give you a json object when embedding one table with the other.

`
const { data, error } = await supabase
.from('country')
.select('name,capital(name)')
.in('id', [1, 2])
console.log(data)
`

noCopy

`
[\
{ "name": "Afghanistan", "capital": { "name": "Kabul" } },\
{ "name": "Algeria", "capital": { "name": "Algiers" } }\
]
`

### Computed relationships [\#](https://supabase.com/blog/postgrest-v10\#computed-relationships)

PostgREST uses foreign keys to detect relationships. This poses a problem on database objects that cannot have foreign keys, like views. Though PostgREST tries to infer relationships based on the views’ source tables foreign keys( [docs](https://postgrest.org/en/latest/api.html#embedding-views)), this is not infallible - in particular, it fails when views have a complex definition (e.g. multiple UNIONs). For this you can use “computed relationships”, which are “inlinable” SQL functions similar to computed columns.

Let’s assume we have a `players` view, a `scores` materialized view and we want to define a one-to-many relationship on them.

`
create view players as
select id, name from players_a
union
select id, name from players_b;
create materialized view scores as
select
name as lvl_name,
compute_score(stats) as total, player_id
from level_1;
union
select
name as lvl_name,
compute_score(stats) as total,
player_id
from level_2;
`

For this we can define a couple of computed relationships.

`
-- many-to-one relationship on scores -> players
create function player(scores)
returns setof players rows 1 -- rows 1 defines a "one" end
language sql stable
as $$
select *
	from players
	where id = $1.player_id;
$$;
-- one-to-many relationship on players -> scores
create function scores(players)
returns setof scores -- there's an implicit rows 1000 here, which is assumed to be "many"
language sql stable
as $$
select *
	from scores
	where player_id = $1.id;
$$;
`

And now we can embed both views from one end to the other. Note that the function names are arbitrary, here we named them similar to the views for convenience.

`
const { data, error } = await supabase
.from('scores')
.select('lvl_name, player(name)')
.eq('lvl_name', "Grand Prix 1")
.single()
console.log(data)
{
	"lvl_name": "Grand Prix 1",
	"player": { "name": "Ben Richards"}
}
const { data, error } = await supabase
.from('players')
.select('name,scores(lvl_name, total)')
.eq('id', 1)
.single()
console.log(data)
{
	"name":"Ben Richards",
	"scores":[\
		{"lvl_name": "Grand Prix 1", "total": 48761.24},\
		{"lvl_name": "Grand Prix 2", "total": -40.25}\
	]
}
`

Computed relationships follow the rules of [Inlining of SQL Functions](https://wiki.postgresql.org/wiki/Inlining_of_SQL_functions), which basically allows them to be injected into PostgREST generated queries, making them efficient to use. You can also use computed relationships to override detected relationships.

### Breaking change on many-to-many relationships [\#](https://supabase.com/blog/postgrest-v10\#breaking-change-on-many-to-many-relationships)

Detecting join tables for many-to-many relationships has been working for many releases. However on complex schemas join tables can be incorrectly detected, causing errors when used in resource embedding. For this the following BREAKING CHANGE had to be made:

`
-- for "books_authors" to be detected as a join table,
-- the primary key must include the foreign key columns
-- of the many-to-many ends
create table books (
id int primary key,
name text
);
create table books_authors (
book_id int references books (id),
author_id int references authors (id),
primary key (book_id, author_id) -- this is now necessary
);
create table authors (
id int primary key,
name text
);
`

If changing the PK is not feasible for a particular case, the alternative would be using computed relationships to define the many-to-many.

One-to-many and many-to-one relationships keep working as always, no change in their detection.

## Closing up [\#](https://supabase.com/blog/postgrest-v10\#closing-up)

Computed relationships are the first step towards PostgREST extensibility, customizing the aggregate used for the response and custom operators are planned for next releases.

We’ll release PostgREST 10 on the Supabase platform over the next month.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-v10&text=PostgREST%20v10%3A%20EXPLAIN%20and%20Improved%20Relationship%20Detection)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-v10&text=PostgREST%20v10%3A%20EXPLAIN%20and%20Improved%20Relationship%20Detection)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-v10&t=PostgREST%20v10%3A%20EXPLAIN%20and%20Improved%20Relationship%20Detection)

[Last post\\
\\
**pg\_jsonschema: JSON Schema support for Postgres** \\
\\
19 August 2022](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation)

[Next post\\
\\
**Supabase Vault** \\
\\
19 August 2022](https://supabase.com/blog/supabase-vault)

[postgres](https://supabase.com/blog/tags/postgres) [launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [EXPLAIN](https://supabase.com/blog/postgrest-v10#explain)
  - [Getting the execution plan through HTTP](https://supabase.com/blog/postgrest-v10#getting-the-execution-plan-through-http)
  - [Explaining supabase-js queries](https://supabase.com/blog/postgrest-v10#explaining-supabase-js-queries)
  - [Explaining RLS policies](https://supabase.com/blog/postgrest-v10#explaining-rls-policies)
  - [Getting the Query Identifier](https://supabase.com/blog/postgrest-v10#getting-the-query-identifier)
- [Improved Relationship Detection](https://supabase.com/blog/postgrest-v10#improved-relationship-detection)
  - [One-to-one relationships](https://supabase.com/blog/postgrest-v10#one-to-one-relationships)
  - [Computed relationships](https://supabase.com/blog/postgrest-v10#computed-relationships)
  - [Breaking change on many-to-many relationships](https://supabase.com/blog/postgrest-v10#breaking-change-on-many-to-many-relationships)
- [Closing up](https://supabase.com/blog/postgrest-v10#closing-up)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-v10&text=PostgREST%20v10%3A%20EXPLAIN%20and%20Improved%20Relationship%20Detection)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-v10&text=PostgREST%20v10%3A%20EXPLAIN%20and%20Improved%20Relationship%20Detection)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-v10&t=PostgREST%20v10%3A%20EXPLAIN%20and%20Improved%20Relationship%20Detection)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)