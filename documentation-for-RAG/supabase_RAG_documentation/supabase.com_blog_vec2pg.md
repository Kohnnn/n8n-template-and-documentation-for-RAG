---
url: "https://supabase.com/blog/vec2pg"
title: "vec2pg: Migrate to pgvector from Pinecone and Qdrant"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# vec2pg: Migrate to pgvector from Pinecone and Qdrant

16 Aug 2024

•

4 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![vec2pg: Migrate to pgvector from Pinecone and Qdrant](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fthumb_vec2pg.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[vec2pg](https://github.com/supabase-community/vec2pg) is a CLI utility for migrating data from vector databases to [Supabase](https://supabase.com/), or any Postgres instance with [pgvector](https://github.com/pgvector/pgvector).

![vec2pg help](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fvec2pg_1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Objective [\#](https://supabase.com/blog/vec2pg\#objective)

Our goal with [https://github.com/supabase-community/vec2pg](https://github.com/supabase-community/vec2pg) is to create an easy on-ramp to efficiently copy your data from various vector databases into Postgres with associated ids and metadata. The data loads into a new schema with a table name that matches the source e.g. `vec2pg.<collection_name>` . That output table uses [https://github.com/pgvector/pgvector's](https://github.com/pgvector/pgvector's) `vector` type for the embedding/vector and the builtin `json` type for additional metadata.

![vec2pg qudrant 1](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fvec2pg_qdrant_2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Once loaded, the data can be manipulated using SQL to transform it into your preferred schema.

When migrating, be sure to increase your Supabase project's [disk size](https://supabase.com/dashboard/project/_/settings/database) so there is enough space for the vectors.

## Vendors [\#](https://supabase.com/blog/vec2pg\#vendors)

At launch we support migrating to Postgres from [Pinecone](https://www.pinecone.io/) and [Qdrant](https://qdrant.tech/). You can vote for additional providers in the [issue tracker](https://github.com/supabase-community/vec2pg/issues/6) and we'll reference that when deciding which vendor to support next.

Throughput when migrating workloads is measured in records-per-second and is dependent on a few factors:

- the resources of the source data
- the size of your Postgres instance
- network speed
- vector dimensionality
- metadata size

When throughput is mentioned, we assume a [Small](https://supabase.com/docs/guides/platform/compute-add-ons) Supabase Instance, a 300 Mbps network, 1024 dimensional vectors, and reasonable geographic colocation of the developer machine, the cloud hosted source DB, and the Postgres instance.

### Pinecone [\#](https://supabase.com/blog/vec2pg\#pinecone)

vec2pg copies entire Pinecone indexes without the need to manage namespaces. It will iterate through all namespaces in the specified index and has a column for the namespace in its Postgres output table.

![vec2pg pinecone 1](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fvec2pg_pinecone_1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Given the conditions noted above, expect 700-1100 records per second.

### Qdrant [\#](https://supabase.com/blog/vec2pg\#qdrant)

The `qdrant` subcommand supports migrating from cloud and locally hosted Qdrant instances.

![vec2pg qdrant 2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fvec2pg_qdrant_3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Again, with the conditions mentioned above, Qdrant collections migrate at between 900 and 2500 records per second.

## Why Use Postgres/pgvector? [\#](https://supabase.com/blog/vec2pg\#why-use-postgrespgvector)

The main reasons to use Postgres for your vector workloads are the same reasons you use Postgres for all of your other data. Postgres is performant, scalable, and secure. Its a well understood technology with a wide ecosystem of tools that support needs from early stage startups through to large scale enterprise.

A few game changing capabilities that are old hat for Postgres that haven't made their way to upstart vector DBs include:

### **Backups** [\#](https://supabase.com/blog/vec2pg\#backups)

Postgres has extensive supports for backups and point-in-time-recovery (PITR). If your vectors are included in your Postgres instance you get backup and restore functionality for free. Combining the data results in one fewer systems to maintain. Moreover, your relational workload and your vector workload are transactionally consistent with full referential integrity so you never get dangling records.

### **Row Security** [\#](https://supabase.com/blog/vec2pg\#row-security)

[Row Level Security (RLS)](https://supabase.com/docs/guides/database/postgres/row-level-security) allows you to write a SQL expression to determine which users are allowed to insert/update/select individual rows.

For example

`
create policy "Individuals can view their own todos."
on public.todos
for select
using
    ( ( select auth.uid() ) = user_id );
`

Allows users of Supabase APIs to update their own records in the `todos` table.

Since `vector` is just another column type in Postgres, you can write policies to ensure e.g. each tenant in your application can only access their own records. That security is enforced at the database level so you can be confident each tenant only sees their own data without repeating that logic all over API endpoint code or in your client application.

### **Performance** [\#](https://supabase.com/blog/vec2pg\#performance)

pgvector has world class performance in terms of raw throughput and dominates in performance per dollar. Check out some of our prior blog posts for more information on functionality and performance:

- [**What's new in pgvector v0.7.0**](https://supabase.com/blog/pgvector-0-7-0)
- [**pgvector 0.6.0: 30x faster with parallel index builds**](https://supabase.com/blog/pgvector-fast-builds)
- [**Matryoshka embeddings: faster OpenAI vector search using Adaptive Retrieval**](https://supabase.com/blog/matryoshka-embeddings)

Keep an eye out for our upcoming post directly comparing pgvector with Pinecone Serverless.

## Next Steps [\#](https://supabase.com/blog/vec2pg\#next-steps)

To get started, head over to the [vec2pg GitHub Page](https://github.com/supabase-community/vec2pg), or if you're comfortable with CLI help guides, you can install it using `pip` :

`
pip install vec2pg
`

If your current vector database vendor isn't supported, be sure to weigh in on the [vendor support issue](https://github.com/supabase-community/vec2pg/issues/6).

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvec2pg&text=vec2pg%3A%20Migrate%20to%20pgvector%20from%20Pinecone%20and%20Qdrant)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvec2pg&text=vec2pg%3A%20Migrate%20to%20pgvector%20from%20Pinecone%20and%20Qdrant)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvec2pg&t=vec2pg%3A%20Migrate%20to%20pgvector%20from%20Pinecone%20and%20Qdrant)

[Last post\\
\\
**The Supabase Book by David Lorenz** \\
\\
16 August 2024](https://supabase.com/blog/supabase-book-by-david-lorenz)

[Next post\\
\\
**Introducing Log Drains** \\
\\
15 August 2024](https://supabase.com/blog/log-drains)

[launch-week](https://supabase.com/blog/tags/launch-week) [release-notes](https://supabase.com/blog/tags/release-notes) [tech](https://supabase.com/blog/tags/tech) [AI](https://supabase.com/blog/tags/AI)

On this page

- [Objective](https://supabase.com/blog/vec2pg#objective)
- [Vendors](https://supabase.com/blog/vec2pg#vendors)
  - [Pinecone](https://supabase.com/blog/vec2pg#pinecone)
  - [Qdrant](https://supabase.com/blog/vec2pg#qdrant)
- [Why Use Postgres/pgvector?](https://supabase.com/blog/vec2pg#why-use-postgrespgvector)
  - [**Backups**](https://supabase.com/blog/vec2pg#backups)
  - [**Row Security**](https://supabase.com/blog/vec2pg#row-security)
  - [**Performance**](https://supabase.com/blog/vec2pg#performance)
- [Next Steps](https://supabase.com/blog/vec2pg#next-steps)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvec2pg&text=vec2pg%3A%20Migrate%20to%20pgvector%20from%20Pinecone%20and%20Qdrant)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fvec2pg&text=vec2pg%3A%20Migrate%20to%20pgvector%20from%20Pinecone%20and%20Qdrant)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fvec2pg&t=vec2pg%3A%20Migrate%20to%20pgvector%20from%20Pinecone%20and%20Qdrant)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![vec2pg help](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fvec2pg_1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![vec2pg qudrant 1](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fvec2pg_qdrant_2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![vec2pg pinecone 1](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fvec2pg_pinecone_1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![vec2pg qdrant 2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fvec2pg_qdrant_3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)