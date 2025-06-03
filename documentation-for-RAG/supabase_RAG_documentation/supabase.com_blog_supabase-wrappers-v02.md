---
url: "https://supabase.com/blog/supabase-wrappers-v02"
title: "Supabase Wrappers v0.2: Query Pushdown & Remote Subqueries"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Wrappers v0.2: Query Pushdown & Remote Subqueries

14 Dec 2023

•

6 minute read

[![Bo Lu avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fburmecia.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Bo LuEngineering](https://github.com/burmecia)

![Supabase Wrappers v0.2: Query Pushdown & Remote Subqueries](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-wrappers%2Fwrappers-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase Wrappers v0.2 is out and now available on the Supabase platform. Wrappers is a Postgres extension that provides integrations with external sources so you can interact with third-party data using SQL.

`
-- Connect Postgres to Stripe
create foreign table products (
id text,
name text,
description text,
default_price text
)
server my_stripe_server
options ( object 'products' );
-- Fetch all your Stripe products in Postgres
select * from products limit 10;
`

**Key Features and Improvements in Wrappers v0.2:**

- [New Wrappers](https://supabase.com/blog/supabase-wrappers-v02#new-wrappers-and-improvements)
- [Query Pushdown](https://supabase.com/blog/supabase-wrappers-v02#support-for-query-pushdown)
- [Remote Subqueries](https://supabase.com/blog/supabase-wrappers-v02#remote-subqueries)
- [Usage Statistics](https://supabase.com/blog/supabase-wrappers-v02#fdw-usage-statistics)

To start using Wrappers on the Supabase platform, check out the [Wrappers docs](https://supabase.com/docs/guides/database/extensions/wrappers/overview).

## New Wrappers and Improvements [\#](https://supabase.com/blog/supabase-wrappers-v02\#new-wrappers-and-improvements)

- [Airtable](https://supabase.com/docs/guides/database/extensions/wrappers/airtable) (Read-only): query your Airtable bases with [support for jsonb](https://github.com/supabase/wrappers/pull/181)
- [AWS S3](https://supabase.com/docs/guides/database/extensions/wrappers/s3) (Read-only): with support for CSV, JSON, and Parquet
- [Clerk](https://github.com/tembo-io/clerk_fdw) (from the team at [Tembo](https://tembo.io/)). Not yet available on our platform since it is a community wrapper, see below for details.
- And a WIP Wrapper for [Auth0](https://github.com/supabase/wrappers/pull/183)

We cannot support community Wrappers inside the Supabase Dashboard until the Wrappers API is stabilized. You can vote your favorite Wrapper if you'd like it to be added to Supabase in the future. If you have developed a Wrapper that you want inside the Supabase Dashboard, please contribute it as a PR in [the wrappers repo](https://github.com/supabase/wrappers). Once we release Wrappers 1.0, we will support community Wrappers within the Supabase Dashboard.

More improvements and updates can be found on [Wrappers release page](https://github.com/supabase/wrappers/releases), including support for Query Pushdown, Remote Subqueries, and Usage Statistics which we’ll explore below.

## Support for Query Pushdown [\#](https://supabase.com/blog/supabase-wrappers-v02\#support-for-query-pushdown)

The Wrappers v0.2 framework now supports Query Pushdown.

### What is Query Pushdown? [\#](https://supabase.com/blog/supabase-wrappers-v02\#what-is-query-pushdown)

Query pushdown is a technique that enhances query performance by executing parts of the query directly on the data source. It reduces data transfer between the database and the application, enabling faster execution and improved performance.

![Examples of Query Pushdown: with and without it.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-wrappers%2Fquery-pushdown-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### How to Use Query Pushdown in Wrappers [\#](https://supabase.com/blog/supabase-wrappers-v02\#how-to-use-query-pushdown-in-wrappers)

In Wrappers, the pushdown logic is integrated into each extension. You don’t need to modify your queries to benefit from this feature. For example, the [Stripe FDW](https://supabase.com/docs/guides/database/extensions/wrappers/stripe) automatically applies query pushdown for `id` within the `customer` object:

`
select *
from stripe.customers
where id = 'cus_N5WMk7pvQPkY3B';
`

This approach contrasts with fetching and filtering all customers locally, which is less efficient. Query pushdown translates this into a single API call, significantly speeding up the process:

`
https://api.stripe.com/v1/customers/cus_N5WMk7pvQPkY3B
`

We can use push down criteria and other query parameters too. For example, [ClickHouse FDW](https://supabase.com/docs/guides/database/extensions/wrappers/clickhouse) supports `order by` and `limit` pushdown:

`
select *
from clickhouse.people
order by name
limit 20;
`

This query executes `order by name limit 20` on ClickHouse before transferring the result to Postgres.

For details on where pushdown is supported, consult each FDW's documentation in the [Wrappers Documentation](https://supabase.com/docs/guides/database/extensions/wrappers/overview).

## Remote Subqueries [\#](https://supabase.com/blog/supabase-wrappers-v02\#remote-subqueries)

Remote subqueries enable the use of prepared data on a remote server, which is beneficial for complex queries or sensitive data protection.

### Static Subqueries [\#](https://supabase.com/blog/supabase-wrappers-v02\#static-subqueries)

In its most basic form, you can map a query on the remote server into a foreign table in Postgres. For instance:

`
create foreign table clickhouse.people (
id bigint,
name text,
age bigint
)
server clickhouse_server
options (
table '(select * from people where age < 25)'
);
`

In this example, the foreign table `clickhouse.people` data is read from the result of the subquery `select * from people where age < 25` which runs on ClickHouse server.

### Dynamic Subqueries [\#](https://supabase.com/blog/supabase-wrappers-v02\#dynamic-subqueries)

What if the query is not fixed and needs to be dynamic? For example, ClickHouse provides [Parameterized Views](https://clickhouse.com/docs/en/sql-reference/statements/create/view#parameterized-view) which can accept parameters for a view. Wrappers v0.2 supports this by defining a column for each parameter. Let's take a look at an example:

`
create foreign table clickhouse.my_table (
id bigint,
col1 text,
col2 bigint,
_param1 text,
_param2 bigint
)
server clickhouse_server
options (
table '(select * from my_view(column1=${_param1}, column2=${_param2}))'
);
`

You can then pass values to these parameters in your query:

`
select id, col1, col2
from clickhouse.my_table
where _param1 = 'abc' and _param2 = 42;
`

Currently, this feature is supported by [ClickHouse FDW](https://supabase.com/docs/guides/database/extensions/wrappers/clickhouse) and [BigQuery FDW](https://supabase.com/docs/guides/database/extensions/wrappers/bigquery), with plans to expand support in the future.

## FDW Usage Statistics [\#](https://supabase.com/blog/supabase-wrappers-v02\#fdw-usage-statistics)

Quantitative metrics play a pivotal role when working with Postgres FDWs because of their impact on performance optimisation, monitoring, and query planning across distributed databases. We introduced a FDW usage statistics table `wrappers_fdw_stats` in Wrappers v0.2, storing:

- `create_times` \- number of times the FDW instance has been created
- `rows_in` \- number of rows transferred from source
- `rows_out` \- number of rows transferred to source
- `bytes_in` \- number of bytes transferred from source
- `bytes_out` \- number of bytes transferred to source
- `metadata` \- additional usage statistics specific to a FDW

We can use these to identify bottlenecks, latency issues, and inefficiencies in data retrieval. Access this table on the Supabase platform using the following:

`
select *
from extensions.wrappers_fdw_stats;
`

## Thanks to Our Community Contributors [\#](https://supabase.com/blog/supabase-wrappers-v02\#thanks-to-our-community-contributors)

We couldn't build Wrappers v0.2 without our community and we'd like to thank all the following people for their contributions:

[Dom Jocubeit,](https://github.com/jocubeit) [0xflotus,](https://github.com/0xflotus) [Glitch,](https://github.com/zer0eXploit) [Tobias Florek,](https://github.com/ibotty) [Jubilee,](https://github.com/workingjubilee) [Germán Larraín,](https://github.com/glarrain-cdd) [Kavanaugh Latiolais,](https://github.com/kav) [tedverse](https://github.com/tedverse).

A separate shout-out belongs to the [pgrx](https://github.com/pgcentralfoundation/pgrx) team, which allows us to write Wrappers with Rust.

Want to join the Supabase Wrappers community contributors? [Check out our contribution docs](https://supabase.github.io/wrappers/contributing/). We'd love to add you to the list next time.

## More About Wrappers [\#](https://supabase.com/blog/supabase-wrappers-v02\#more-about-wrappers)

- [Wrappers: 3rd Party Integrations](https://supabase.com/docs/guides/database/extensions/wrappers/overview)
- [Wrappers Documentation](https://supabase.github.io/wrappers/)
- [Blog Post: Supabase Wrappers, a Postgres FDW framework written in Rust](https://supabase.com/blog/postgres-foreign-data-wrappers-rust)
- [Blog Post: Wrappers UI](https://supabase.com/blog/supabase-studio-3-0#wrappers-ui)

[Launch Week![Supabase Launch Week X icon](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Flwx%2Flogos%2Flwx_logo.svg&w=32&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/launch-week)

11-15 Dec

Main Stage

[Day 1 -Supabase Studio: introducing an **AI Assistant**, **Postgres roles**, and **user impersonation**](https://supabase.com/blog/studio-introducing-assistant)

[Day 2 -Edge Functions: **Node** and native **npm** compatibility](https://supabase.com/blog/edge-functions-node-npm)

[Day 3 -Introducing Supabase **Branching**, a Postgres database for every pull request](https://supabase.com/blog/supabase-branching)

[Day 4 -Supabase Auth: **Identity Linking**, **Session Control**, **Password Protection** and **Hooks**](https://supabase.com/blog/supabase-auth-identity-linking-hooks)

[Day 5 -Introducing **Read Replicas** for low latency](https://supabase.com/blog/introducing-read-replicas)

Build Stage

[01 -Supabase Album](https://supabase.productions/)

[02 -Postgres Language Server](https://supabase.com/blog/postgres-language-server-implementing-parser)

[03 -Design at Supabase](https://supabase.com/blog/how-design-works-at-supabase)

[04 -Supabase Grafana](https://github.com/supabase/supabase-grafana)

[05 -pg\_graphql: Postgres functions](https://supabase.com/blog/pg-graphql-postgres-functions)

[06 -PostgREST 12](https://supabase.com/blog/postgrest-12)

[07 -Supavisor 1.0](https://supabase.com/blog/supavisor-postgres-connection-pooler)

[08 -Supabase Wrappers v0.2](https://supabase.com/blog/supabase-wrappers-v02)

[09 -Supabase Libraries V2](https://supabase.com/blog/client-libraries-v2)

[10 -Supabase x Fly.io](https://supabase.com/blog/postgres-on-fly-by-supabase)

[11 -Top 10 Launches of LWX](https://supabase.com/blog/launch-week-x-best-launches)

[Supabase Launch Week X Hackathon](https://supabase.com/blog/supabase-hackathon-lwx)

[Supabase Launch Week X Community Meetups](https://supabase.com/blog/community-meetups-lwx)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-wrappers-v02&text=Supabase%20Wrappers%20v0.2%3A%20Query%20Pushdown%20%26%20Remote%20Subqueries)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-wrappers-v02&text=Supabase%20Wrappers%20v0.2%3A%20Query%20Pushdown%20%26%20Remote%20Subqueries)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-wrappers-v02&t=Supabase%20Wrappers%20v0.2%3A%20Query%20Pushdown%20%26%20Remote%20Subqueries)

[Last post\\
\\
**Supabase Auth: Identity Linking, Hooks, and HaveIBeenPwned integration** \\
\\
14 December 2023](https://supabase.com/blog/supabase-auth-identity-linking-hooks)

[Next post\\
\\
**PostgREST 12** \\
\\
13 December 2023](https://supabase.com/blog/postgrest-12)

[launch-week](https://supabase.com/blog/tags/launch-week) [foreign-data-wrappers](https://supabase.com/blog/tags/foreign-data-wrappers) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [New Wrappers and Improvements](https://supabase.com/blog/supabase-wrappers-v02#new-wrappers-and-improvements)
- [Support for Query Pushdown](https://supabase.com/blog/supabase-wrappers-v02#support-for-query-pushdown)
  - [What is Query Pushdown?](https://supabase.com/blog/supabase-wrappers-v02#what-is-query-pushdown)
  - [How to Use Query Pushdown in Wrappers](https://supabase.com/blog/supabase-wrappers-v02#how-to-use-query-pushdown-in-wrappers)
- [Remote Subqueries](https://supabase.com/blog/supabase-wrappers-v02#remote-subqueries)
  - [Static Subqueries](https://supabase.com/blog/supabase-wrappers-v02#static-subqueries)
  - [Dynamic Subqueries](https://supabase.com/blog/supabase-wrappers-v02#dynamic-subqueries)
- [FDW Usage Statistics](https://supabase.com/blog/supabase-wrappers-v02#fdw-usage-statistics)
- [Thanks to Our Community Contributors](https://supabase.com/blog/supabase-wrappers-v02#thanks-to-our-community-contributors)
- [More About Wrappers](https://supabase.com/blog/supabase-wrappers-v02#more-about-wrappers)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-wrappers-v02&text=Supabase%20Wrappers%20v0.2%3A%20Query%20Pushdown%20%26%20Remote%20Subqueries)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-wrappers-v02&text=Supabase%20Wrappers%20v0.2%3A%20Query%20Pushdown%20%26%20Remote%20Subqueries)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-wrappers-v02&t=Supabase%20Wrappers%20v0.2%3A%20Query%20Pushdown%20%26%20Remote%20Subqueries)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Examples of Query Pushdown: with and without it.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-wrappers%2Fquery-pushdown-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)