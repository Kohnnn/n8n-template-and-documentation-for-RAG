---
url: "https://supabase.com/blog/pg-graphql-v1"
title: "pg_graphql v1.0"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# pg\_graphql v1.0

16 Dec 2022

•

6 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![pg_graphql v1.0](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fpggraphql%2Fog-pg-graphql.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we're announcing the 1.0 release of [`pg_graphql`](https://github.com/supabase/pg_graphql) and its general availability on our platform. pg\_graphql is a PostgreSQL extension that allows you to query your database using GraphQL. It is the foundation of GraphQL support in the Supabase stack.

Since our first platform release, v0.2.1, the feature set of pg\_graphql has steadily grown and stabilized. Despite being a pre-1.0, we've been extremely cautious with each new feature and have yet to introduce a backwards-incompatible change. With the 1.0 release we're formalizing that guarantee, subject to the SemVer spec.

## Background [\#](https://supabase.com/blog/pg-graphql-v1\#background)

pg\_graphql was created to satisfy an extreme set of constraints. Mainly, [Supabase Free Plan](https://supabase.com/pricing) projects run on servers with 1 GB of memory. On those servers, we squeeze tuned versions of [PostgreSQL](https://github.com/supabase/postgres), [PostgREST](https://postgrest.org/en/stable/), and [GoTrue](https://github.com/supabase/gotrue). Every megabyte consumed by something that isn't PostgreSQL is another chance for an index to fall out of memory, or a large query to fail.

Our philosophy when adding to the stack is to use existing open source tools wherever possible. We surveyed the available GraphQL → SQL options and found some excellent candidates in Hasura and Graphile. Both support the set of features we're interested in, but consume significantly more memory than we could sacrifice on the Free Plan. Realizing that, we searched for an architecture that could meet our runtime constraints and performance requirements.

## Architecture [\#](https://supabase.com/blog/pg-graphql-v1\#architecture)

Our first prototype of pg\_graphql PostgreSQL extension had a parser written in C (libgraphqlparser) with all business logic of transpiling GraphQL to SQL **written** in SQL. We exposed the extensions sole SQL function `graphql.resolve(...)` over HTTP using PostgREST's [RPC functionality](https://postgrest.org/en/stable/api.html#s-procs). With this approach, the memory footprint was too small to measure when accessed over HTTP. While memory-use sent us down this path, we discovered that leaning into Postgres primitives lead to some incredible synergies. To name a few:

### Security [\#](https://supabase.com/blog/pg-graphql-v1\#security)

Since data are accessed through a standard, unprivileged, SQL function, Postgres role permissions and Row Level Security (RLS) policies work exactly like they do in Postgres. Define your security model once, and it applies everywhere: SQL, REST, Realtime, and GraphQL

### Always up-to-date [\#](https://supabase.com/blog/pg-graphql-v1\#always-up-to-date)

No separate process means no roundtrip time. Inspecting the database's schema does not require any caching and is always in-sync. Knowing that the GraphQL and SQL schemas are aligned give us the confidence to compile GraphQL requests of any complexity into exactly one SQL query, [solving the N+1 query problem](https://medium.com/the-marcy-lab-school/what-is-the-n-1-problem-in-graphql-dd4921cb3c1a) and producing high throughput.

### Scaling [\#](https://supabase.com/blog/pg-graphql-v1\#scaling)

As an extension, pg\_graphql's performance scales directly with the size of the database. When a user's performance needs grow, upgrading the database instance also scales up GraphQL throughput with no external processes to manage.

### ACID - Atomicity, Consistency, Isolation, and Durability [\#](https://supabase.com/blog/pg-graphql-v1\#acid---atomicity-consistency-isolation-and-durability)

Databases have strong ACID guarantees. Being embedded in the database lets us claim those guarantees through the GraphQL API. For example, if any part of a multi-mutation GraphQL request fails, the entire request can roll back to leave the database in a consistent state.

## From SQL to Rust [\#](https://supabase.com/blog/pg-graphql-v1\#from-sql-to-rust)

Our pure [SQL implementation of the pg\_graphql transpiler](https://github.com/supabase/pg_graphql/blob/bd0283718abaf329d98c69808f862594e9df5edc/pg_graphql--0.4.0.sql) carried us from v0.0.1 to v0.4.0. Ultimately, we started to feel some pain, although probably not in the way you'd expect.

Opinions about business logic in SQL are notoriously split. In my view, there are some foot guns, but:

- SQL has types
- SQL has functions
- Functions are composable

Ergo, keep your functions pure and you've got a strongly typed functional programming paradigm. Taking that approach, the developer experience for pg\_graphql was surprisingly excellent. The feedback cycle with [pg\_regress](https://www.postgresql.org/docs/9.1/regress.html) is fast, and occasionally the type system even caught a bug or two. What more could you ask for?

Somewhere around the 4,000 line count, things started to bog down. The rough shape of the codebase was coming into view, which made it clear where we could further extract common patterns into functions. At this point I learned two things:

- SQL functions are “pass by value” (copy) so passing state around can get expensive
- The query planner tends to stop inlining functions when calls are deeply nested

Combine those two facts with our GraphQL AST being a big ball of JSONB, and the GitHub issues about slow schema introspection on Free Plan started to trickle in.

Enter [pgx](https://github.com/tcdi/pgx)…

pgx is a rust framework for building Postgres extensions. It has a very polished onboarding experience and (as you would expect) full SQL interop. That made it straightforward to initially sprinkle some rust on pg\_graphql's hotspots. When that went well, we ultimately rewrote pg\_graphql from the ground up as a pure Rust project for the v0.5.0 release.

One of rust's main selling points is zero cost abstractions. That means high-level concepts like generics incur no runtime penalty. Transitioning from SQL's expensive abstractions to rust's zero cost abstractions has been hugely satisfying as it enabled refactoring the codebase into a more maintainable state. Development velocity is up. Code quality is up. Performance is WAY up.

As of 1.0, overhead introduced by pg\_graphql is sub 300 _micro_ seconds per request on free Plan hardware. When executed from SQL we see ~1060 queries per second per connection (no parallelism). If we include the entire Auth + HTTP stack, Free Plan can handle ~645 requests per second. On larger instance the stack handles upwards of 10k requests / second.

`
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Server Software:        postgrest/10.1.1
Document Path:          /graphql/v1
Concurrency Level:      10
Time taken for tests:   3.099 seconds
Complete requests:      2000
Requests per second:    645.40 [#/sec] (mean)
Time per request:       15.494 [ms] (mean)
Time per request:       1.549 [ms] (mean, across all concurrent requests)
`

## Roadmap [\#](https://supabase.com/blog/pg-graphql-v1\#roadmap)

🆕 Support for views, filtering options, and other new features were released with [pg\_graphql v1.2](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2)

While v1.0 is an important milestone for stability, there's plenty of room to expand the feature set. For example, some commonly requested features on the immediate roadmap are:

- Extended filtering options
  - `startsWith` for the `String` type
  - nestable `and`/ `or` blocks
- Support for user-defined functions
- Support for views

Longer term we look forward to experimenting with more ambitions features like an API for migrations, integrations with 3rd-party services through [supabase/wrappers](https://github.com/supabase/wrappers), and a scalable solution for subscriptions.

## More pg\_graphql [\#](https://supabase.com/blog/pg-graphql-v1\#more-pg_graphql)

- [Introducing pg\_graphql: A GraphQL extension for PostgreSQL](https://supabase.com/blog/pg-graphql)
- [GraphQL is now available in Supabase](https://supabase.com/blog/graphql-now-available)
- [pg\_graphql: Postgres functions now supported](https://supabase.com/blog/pg-graphql-postgres-functions)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-v1&text=pg_graphql%20v1.0)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-v1&text=pg_graphql%20v1.0)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-v1&t=pg_graphql%20v1.0)

[Last post\\
\\
**What's new in Postgres 15?** \\
\\
16 December 2022](https://supabase.com/blog/new-in-postgres-15)

[Next post\\
\\
**Point in Time Recovery is now available for Pro projects** \\
\\
16 December 2022](https://supabase.com/blog/postgres-point-in-time-recovery)

[graphql](https://supabase.com/blog/tags/graphql) [postgres](https://supabase.com/blog/tags/postgres) [launch-week](https://supabase.com/blog/tags/launch-week) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Background](https://supabase.com/blog/pg-graphql-v1#background)
- [Architecture](https://supabase.com/blog/pg-graphql-v1#architecture)
  - [Security](https://supabase.com/blog/pg-graphql-v1#security)
  - [Always up-to-date](https://supabase.com/blog/pg-graphql-v1#always-up-to-date)
  - [Scaling](https://supabase.com/blog/pg-graphql-v1#scaling)
  - [ACID - Atomicity, Consistency, Isolation, and Durability](https://supabase.com/blog/pg-graphql-v1#acid---atomicity-consistency-isolation-and-durability)
- [From SQL to Rust](https://supabase.com/blog/pg-graphql-v1#from-sql-to-rust)
- [Roadmap](https://supabase.com/blog/pg-graphql-v1#roadmap)
- [More pg\_graphql](https://supabase.com/blog/pg-graphql-v1#more-pg_graphql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-v1&text=pg_graphql%20v1.0)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-v1&text=pg_graphql%20v1.0)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-v1&t=pg_graphql%20v1.0)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)