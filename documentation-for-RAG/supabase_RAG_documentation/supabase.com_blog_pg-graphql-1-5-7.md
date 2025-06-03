---
url: "https://supabase.com/blog/pg-graphql-1-5-7"
title: "pg_graphql 1.5.7: pagination and multi-tenancy support"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# pg\_graphql 1.5.7: pagination and multi-tenancy support

15 Aug 2024

•

4 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![pg_graphql 1.5.7: pagination and multi-tenancy support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fthumb_pg_graphql.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# What's new in pg\_graphql 1.5.7 [\#](https://supabase.com/blog/pg-graphql-1-5-7\#whats-new-in-pg_graphql-157)

Since our [last check-in on pg\_graphql](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2) there have been a few quality of life improvements worth calling out. A quick roundup of the key differences includes:

- Pagination via First/Offset
- Schema based multi-tenancy
- Filtering on array typed columns with `contains`, `containedBy` and `overlaps`

## First/Offset pagination [\#](https://supabase.com/blog/pg-graphql-1-5-7\#firstoffset-pagination)

Since the earliest days of pg\_graphql, [keyset pagination](https://supabase.github.io/pg_graphql/api/#keyset-pagination) has been supported. Keyset pagination allows for paging forwards and backwards through a collection by specifying a number of records and the unique id of a record within the collection. For example:

`
{
blogCollection(
    first: 2,
    after: "Y3Vyc29yMQ=="
) {
...
}
`

to retrieve the first 2 records after the record with unique id `Y3Vyc29yMQ==` .

Starting in version `1.5.0` there is support for `offset` based pagination, which is based on skipping `offset` number of records before returning the results.

`
{
blogCollection(
    first: 2,
    offset: 5
) {
...
}
`

That is roughly equivalent to the SQL

`
select
    *
from
    blog
limit
    2
offset
    5
`

In general as offset values increase, the performance of the query will decrease. For that reason its important to use keyset pagination where possible.

## Performance schema based multi-tennancy [\#](https://supabase.com/blog/pg-graphql-1-5-7\#performance-schema-based-multi-tennancy)

pg\_graphql caches the database schema on first query and rebuilds that cache any time the schema changes. The cache key is a combination of the postgres role and the database schema's version number. Initially, the structure of all schemas was loaded for all roles, and table/column visibility was filtered down within `pg_graphql`.

In multi-tenant environments with 1 schema per tenant, that meant every time a tenant updated their schema, all tenants had to rebuild the cache. When the number of tenants gets large, that burdens the database if its under heavy load.

Following version `1.5.2` each tenant's cache only loads the schemas that they have `usage` permission for, which greatly reduces the query time in multi-tenant environments and the size of the schema cache. At time of writing this solution powers a project with >2200 tenants.

## Filtering array column types [\#](https://supabase.com/blog/pg-graphql-1-5-7\#filtering-array-column-types)

From `1.5.6` pg\_graphql has added `contains`, `containedBy`, `overlaps` filter operators for scalar array fields like `text[]` or `int[]`.

For example, given a table

`
create table blog (
id int primary key,
name text not null,
tags text[] not null,
created_at timestamp not null
);
`

the `tags` column with type `text[]` can be filtered on.

`
{
blogCollection(filter: { tags: { contains: ["tech", "innovation"] } }) {
    edges {
      cursor
      node {
        name
        tags
        createdAt
      }
    }
}
}
`

In this case, the result set is filtered to records where the `tags` column contains both `tech` and `innovation`.

## Roadmap [\#](https://supabase.com/blog/pg-graphql-1-5-7\#roadmap)

The headline features we aim to launch in coming releases of pg\_graphql include support for:

- Insert on conflict / Upsert
- Nested inserts

If you want to get started with GraphQL today, check out the [Docs](https://supabase.com/docs/guides/graphql) or the [source code](https://github.com/supabase/pg_graphql/).

[Launch Week12](https://supabase.com/launch-week/12)

12-16 August

[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)

[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)

[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)

[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)

[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage

[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)

[02 -pg\_replicate](https://news.ycombinator.com/item?id=41209994)

[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)

[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)

[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)

[06 -vec2pg](https://supabase.com/blog/vec2pg)

[07 -pg\_graphql](https://supabase.com/blog/pg-graphql-1-5-7)

[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)

[09 -python-support](https://supabase.com/blog/python-support)

[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)

[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&text=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&text=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&t=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)

[Last post\\
\\
**Introducing Log Drains** \\
\\
15 August 2024](https://supabase.com/blog/log-drains)

[Next post\\
\\
**Snaplet is now open source** \\
\\
14 August 2024](https://supabase.com/blog/snaplet-is-now-open-source)

[launch-week](https://supabase.com/blog/tags/launch-week) [graphql](https://supabase.com/blog/tags/graphql)

On this page

- [What's new in pg\_graphql 1.5.7](https://supabase.com/blog/pg-graphql-1-5-7#whats-new-in-pg_graphql-157)
  - [First/Offset pagination](https://supabase.com/blog/pg-graphql-1-5-7#firstoffset-pagination)
  - [Performance schema based multi-tennancy](https://supabase.com/blog/pg-graphql-1-5-7#performance-schema-based-multi-tennancy)
  - [Filtering array column types](https://supabase.com/blog/pg-graphql-1-5-7#filtering-array-column-types)
  - [Roadmap](https://supabase.com/blog/pg-graphql-1-5-7#roadmap)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&text=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&text=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-1-5-7&t=pg_graphql%201.5.7%3A%20pagination%20and%20multi-tenancy%20support)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)