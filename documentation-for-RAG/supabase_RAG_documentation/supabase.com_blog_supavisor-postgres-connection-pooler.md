---
url: "https://supabase.com/blog/supavisor-postgres-connection-pooler"
title: "Supavisor 1.0: a scalable connection pooler for Postgres"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supavisor 1.0: a scalable connection pooler for Postgres

13 Dec 2023

•

7 minute read

[![Stanislav Muzhyk avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fabc3.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Stanislav MuzhykEngineering](https://github.com/abc3)

![Supavisor 1.0: a scalable connection pooler for Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supavisor%2Fsupavisor-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

After [launching Supavisor in August](https://supabase.com/blog/supavisor-1-million), we've successfully migrated all projects on the platform. Every new Supabase project launched now gets a Supavisor connection string to use for connection pooling.

Supavisor 1.0 symbolizes production readiness and comes with many bug fixes. It includes three important features:

1. query load balancing
2. named prepared statement support
3. query cancelation

## What is connection pooling? [\#](https://supabase.com/blog/supavisor-postgres-connection-pooler\#what-is-connection-pooling)

Supavisor is built with Elixir. Since the [Dashbit](https://dashbit.co/) team have been helping with the development we invited Jose Valim, the creator of Elixir, to explain connection pooling, OTP, and why Elixir is a great fit for a connection pooler:

Supavisor 1.0: Postgres connection pooler - YouTube

Supabase

54.4K subscribers

[Supavisor 1.0: Postgres connection pooler](https://www.youtube.com/watch?v=ogYNmJOFEpk)

Supabase

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=ogYNmJOFEpk "Watch on YouTube")

## SQL parsing with Rust [\#](https://supabase.com/blog/supavisor-postgres-connection-pooler\#sql-parsing-with-rust)

To implement the latest set of features, we now parse all SQL statements from connected clients.

Supavisor, developed in Elixir, supports high concurrency and rapid I/O. Elixir doesn't have great performance for parsing, but it provides excellent interop with Rust via [Rustler](https://github.com/rusterlium/rustler). For efficient SQL parsing, we use [`pg_query.rs`](https://github.com/pganalyze/pg_query.rs).

## Load Balancing [\#](https://supabase.com/blog/supavisor-postgres-connection-pooler\#load-balancing)

When set up with a Postgres cluster, Supavisor load-balances read requests between the primary server and its replicas. It randomly distributes these read requests across the entire Postgres cluster.

Supavisor targets write operations to the primary automatically by probing read replicas until it hits the primary with a successful write, [similar to libpq](https://www.percona.com/blog/seamless-application-failover-using-libpq-features-in-postgresql/). The trade-off here is that writes may take a few milliseconds longer to complete in favor of zero additional client-side complexity. This write strategy also makes transparent primary failovers painless because detecting the primary for writes is automatic.

### Read-after-writes [\#](https://supabase.com/blog/supavisor-postgres-connection-pooler\#read-after-writes)

With automatic primary detection, it's easy to guarantee read-after-writes from the same client by wrapping the read and write in a transaction.

Future work is planned to allow custom server targeting with SQL statements such as `SET SERVER 'primary'` to let clients guarantee read-after-writes outside of transactions or across clients.

## Named Prepared Statements [\#](https://supabase.com/blog/supavisor-postgres-connection-pooler\#named-prepared-statements)

Many clients use named [prepared statements](https://www.postgresql.org/docs/current/sql-prepare.html) when generating parameterized SQL. During statement preparation Postgres parses, plans, and optimizes queries.

If a client can create named prepared statements, then such a client can re-use these query plans and simply submit parameters for them.

The problem with named prepared statements and pooling in the transaction mode is that statements are not shared across Postgres backends (connections). Each client connection must issue prepared statements for each query they will run.

Supavisor now supports named prepared statements. Supavisor parses each query and identifies `PREPARE` statements. When a `PREPARE` statement is received on one connection, it is broadcast across all connections. This approach allows every client to access named prepared statements that have been issued by other connections. This adds a slight increase in memory overhead when duplicating query plans for each Postgres connection but should come with significant throughput gains.

![Diagram explaining how named prepared statements work in Supavisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supavisor%2Fprepared-statements-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Query Cancelation [\#](https://supabase.com/blog/supavisor-postgres-connection-pooler\#query-cancelation)

With 1.0 we get query official cancelation as well. If you're in `psql` typing `Ctrl+C` will actually cancel your query now.

Especially useful if you accidentally run a heavy query!

## Platform Updates [\#](https://supabase.com/blog/supavisor-postgres-connection-pooler\#platform-updates)

For the Supavisor rollout, we maintained consistent pooling settings between PgBouncer and Supavisor.

Now, we're raising the client connection limit for smaller projects in Supavisor. Here are the updated default configurations:

| Database Size | default\_pool\_size | max\_connections | default\_max\_clients |
| --- | --- | --- | --- |
| Micro | 15 | 60 | 200 |
| Small | 15 | 90 | 400 (previously 200) |
| Medium | 15 | 120 | 600 (previously 200) |
| Large | 20 | 160 | 800 (previously 300) |
| XL | 20 | 240 | 1,000 (previously 700) |
| 2XL | 25 | 380 | 1,500 |
| 4XL | 32 | 480 | 3,000 |
| 8XL | 64 | 490 | 6,000 |
| 12XL | 96 | 500 | 9,000 |
| 16XL | 128 | 500 | 12,000 |

In this table:

- `default_pool_size`: the number of connections from Supavisor to your database (configurable)
- `max_connections`: the max number of direct connections Postgres is configured to allow (configurable)
- `default_max_clients` : the maximum number of clients allowed to connect to Supavisor (upgrade to increase)

### IPv4 Deprecation [\#](https://supabase.com/blog/supavisor-postgres-connection-pooler\#ipv4-deprecation)

Effective February 1, 2024 [AWS is charging for all allocated IPV4 addresses](https://aws.amazon.com/blogs/aws/new-aws-public-ipv4-address-charge-public-ip-insights/). Rather than passing that fee onto our customers Supavisor can mediate connections from IPv4 to IPv6.

If you're using the PgBouncer connection string and haven't migrated to the new Supavisor connection string make sure to do this before January 15th, 2024.

## Getting started [\#](https://supabase.com/blog/supavisor-postgres-connection-pooler\#getting-started)

If you're using the Supabase platform, you can already access the pooler URL in your [project connect page](https://supabase.com/dashboard/project/_?showConnect=true).

If you're looking to self-host Supavisor, check out [GitHub repository](https://github.com/supabase/supavisor) and [documentation](https://supabase.github.io/supavisor/).

You can expect Supavisor 1.0 to hit the platform next week along with the new pooling configuration changes. If you've set a custom pooler configuration, or we've set one for you, your settings won't change.

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-postgres-connection-pooler&text=Supavisor%201.0%3A%20a%20scalable%20connection%20pooler%20for%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-postgres-connection-pooler&text=Supavisor%201.0%3A%20a%20scalable%20connection%20pooler%20for%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-postgres-connection-pooler&t=Supavisor%201.0%3A%20a%20scalable%20connection%20pooler%20for%20Postgres)

[Last post\\
\\
**Supabase Branching** \\
\\
13 December 2023](https://supabase.com/blog/supabase-branching)

[Next post\\
\\
**Edge Functions: Node and native npm compatibility** \\
\\
12 December 2023](https://supabase.com/blog/edge-functions-node-npm)

[launch-week](https://supabase.com/blog/tags/launch-week) [supavisor](https://supabase.com/blog/tags/supavisor) [postgres](https://supabase.com/blog/tags/postgres) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [What is connection pooling?](https://supabase.com/blog/supavisor-postgres-connection-pooler#what-is-connection-pooling)
- [SQL parsing with Rust](https://supabase.com/blog/supavisor-postgres-connection-pooler#sql-parsing-with-rust)
- [Load Balancing](https://supabase.com/blog/supavisor-postgres-connection-pooler#load-balancing)
  - [Read-after-writes](https://supabase.com/blog/supavisor-postgres-connection-pooler#read-after-writes)
- [Named Prepared Statements](https://supabase.com/blog/supavisor-postgres-connection-pooler#named-prepared-statements)
- [Query Cancelation](https://supabase.com/blog/supavisor-postgres-connection-pooler#query-cancelation)
- [Platform Updates](https://supabase.com/blog/supavisor-postgres-connection-pooler#platform-updates)
  - [IPv4 Deprecation](https://supabase.com/blog/supavisor-postgres-connection-pooler#ipv4-deprecation)
- [Getting started](https://supabase.com/blog/supavisor-postgres-connection-pooler#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-postgres-connection-pooler&text=Supavisor%201.0%3A%20a%20scalable%20connection%20pooler%20for%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-postgres-connection-pooler&text=Supavisor%201.0%3A%20a%20scalable%20connection%20pooler%20for%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupavisor-postgres-connection-pooler&t=Supavisor%201.0%3A%20a%20scalable%20connection%20pooler%20for%20Postgres)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Diagram explaining how named prepared statements work in Supavisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supavisor%2Fprepared-statements-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)