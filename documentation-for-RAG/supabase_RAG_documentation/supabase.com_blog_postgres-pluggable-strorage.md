---
url: "https://supabase.com/blog/postgres-pluggable-strorage"
title: "Next steps for Postgres pluggable storage"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Next steps for Postgres pluggable storage

01 May 2023

•

4 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Next steps for Postgres pluggable storage](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpluggable-storage%2Fpluggable-storage.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You might have recently read “ [The Part of PostgreSQL We Hate the Most](https://ottertune.com/blog/the-part-of-postgresql-we-hate-the-most/)” which highlights some of the deficiencies with Postgres storage. Fortunately, there is ongoing work in the Postgres ecosystem to solve this using “pluggable storage”.

This article explores the history of Postgres pluggable storage and the possibility of landing it in the Postgres core.

## What is pluggable storage? [\#](https://supabase.com/blog/postgres-pluggable-strorage\#what-is-pluggable-storage)

Pluggable storage gives developers the ability to use different storage engines for different tables within the same database.

Developers will be able to choose a storage method that is optimized for their specific needs. Some tables could be configured for high transactional loads, others for analytics workloads, and still others for archiving.

Something like this is already [available in MySQL](https://en.wikipedia.org/wiki/Comparison_of_MySQL_database_engines), which uses the [InnoDB](https://en.wikipedia.org/wiki/InnoDB) as the default storage engine since MySQL 5.5. This replaced [MyISAM](https://en.wikipedia.org/wiki/MyISAM) which had it’s own [set of problems](https://www.percona.com/blog/using-myisam-in-production/).

The “pluggable” part refers to the ability for developers to develop their own storage methods, similar to Postgres Extensions. While some databases offer multiple built-in storage methods by default, Postgres follows a core philosophy of flexibility and extensibility, and using a pluggable approach makes a lot of sense.

## Current progress for pluggable storage [\#](https://supabase.com/blog/postgres-pluggable-strorage\#current-progress-for-pluggable-storage)

In version 12, PostgreSQL introduced basic support for pluggable storage with the goal of [adding ZHeap](https://anarazel.de/talks/2019-05-30-pgcon-pluggable-table-storage/pluggable.pdf). Andres Freund and several contributors enabled that feature by refactoring and expanding a variety of table access method (TAM) APIs.

ZHeap [was released](https://github.com/EnterpriseDB/zheap) with [promising results](https://www.pgcon.org/2018/schedule/attachments/501_zheap-a-new-storage-format-postgresql-5.pdf), providing an undo log and solving some long-term table bloat issues in Postgres.

While it was a great start, unfortunately it appears that the work on ZHeap and the TAM API [has stalled](https://twitter.com/andy_pavlo/status/1590703943176589312).
This leaves a few holes in that need to be fixed before the community can use the TAM API for pluggable storage. In particular:

- The TAM API doesn’t provide much flexibility for working with indexes. For example, when you update a row an index update is an all-or-nothing procedure.
- Row versions need to be identified by the pairing of a block number and offset number. This means you can’t implement some useful functions, like an index-organized table or undo-based versioning.

Even without a full API for pluggable storage, there are a couple of solutions available on the market today:

- **Citus’s** [Columnar Storage](https://docs.citusdata.com/en/v11.1/admin_guide/table_management.html#columnar-storage), which powers Microsoft’s [Hyperscale](https://azure.microsoft.com/en-us/updates/azure-database-for-postgresql-hyperscale-citus-is-now-available/) offering. Citus has a few [limitations](https://docs.citusdata.com/en/v11.1/admin_guide/table_management.html#limitations) due to the restrictions of the current API.
- EDB’s [Advanced Storage Pack](https://www.infoworld.com/article/3681112/3-key-features-in-edb-postgresql-15.html), which is appears to provide some enhancements to heap storage, although the source is not available for us to confirm.

## The future of pluggable storage [\#](https://supabase.com/blog/postgres-pluggable-strorage\#the-future-of-pluggable-storage)

Right now, pluggable storage requires a fork of Postgres. But there are several initiatives in the Postgres community that we’re excited about.

- There have been community updates for [custom resource managers](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commitdiff;h=5c279a6d350205cc98f91fb8e1d3e4442a6b25d1) that expand [write-ahead log (WAL)](https://www.postgresql.org/docs/current/wal-intro.html) support for TAM.
- The creators at [OrioleDB](https://github.com/orioledb/orioledb) started with a fork of Postgres and have been quietly upstreaming code that would make pluggable storage a reality. In Postgres 14 their patchset was ~5,000 lines of code, representing the total number of changes required in their fork. In the upcoming Postgres 16 release, it is ~2,000 lines of code. That means that around 60% of the code is already committed to the Postgres core. (Disclosure: Supabase started [sponsoring OrioleDB](https://supabase.com/blog/supabase-series-b#where-were-going) in 2022).

Alexander Korotkov, the maintainer of OrioleDB, will be talking at PGCON 23 about some of the [changes](https://www.pgcon.org/events/pgcon_2023/schedule/session/470-future-of-table-access-methods/) they are making. They are solving many ["wicked Postgres problems"](https://www.slideshare.net/AlexanderKorotkov/solving-postgresql-wicked-problems) with [dual pointers](https://www.orioledata.com/blog/buffer-management/) instead of buffer mapping, row-level WAL instead of block-level WAL, undo logs instead of bloat-prone MVCC, and index-organized tables instead of heap.

## Timelines for pluggable storage [\#](https://supabase.com/blog/postgres-pluggable-strorage\#timelines-for-pluggable-storage)

Ambitiously, many of the changes required for pluggable storage could land in Postgres 17. If that happens, new storage engines like OrioleDB would be available as a simple extension for developers to use in any Postgres instance. This paves the way for other Pluggable Storage Engines, just like MySQL’s [support for multiple storage engines](https://dev.mysql.com/doc/refman/5.7/en/storage-engines.html).

As a community project, Postgres requires support for these initiatives. You can support pluggable storage by getting involved during Postgres [Commitfests](https://supabase.com/blog/postgresql-commitfest). Postgres is already one of the best database engines in the world, and pluggable storage would make it even more attractive and maintainable.

## More Postgres content [\#](https://supabase.com/blog/postgres-pluggable-strorage\#more-postgres-content)

- [Storing OpenAI embeddings in Postgres with pgvector](https://supabase.com/blog/openai-embeddings-postgres-vector)
- [Choosing a Postgres Primary Key](https://supabase.com/blog/choosing-a-postgres-primary-key)
- [SQL or NoSQL? Why not use both (with PostgreSQL)?](https://supabase.com/blog/sql-or-nosql-both-with-postgresql)
- [pg\_jsonschema: JSON Schema support for Postgres](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation)
- [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-pluggable-strorage&text=Next%20steps%20for%20Postgres%20pluggable%20storage)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-pluggable-strorage&text=Next%20steps%20for%20Postgres%20pluggable%20storage)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-pluggable-strorage&t=Next%20steps%20for%20Postgres%20pluggable%20storage)

[Last post\\
\\
**Securing your Flutter apps with Multi-Factor Authentication** \\
\\
4 May 2023](https://supabase.com/blog/flutter-multi-factor-authentication)

[Next post\\
\\
**Launch Week 7 Hackathon Winners** \\
\\
24 April 2023](https://supabase.com/blog/launch-week-7-hackathon-winners)

[postgres](https://supabase.com/blog/tags/postgres) [database](https://supabase.com/blog/tags/database) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [What is pluggable storage?](https://supabase.com/blog/postgres-pluggable-strorage#what-is-pluggable-storage)
- [Current progress for pluggable storage](https://supabase.com/blog/postgres-pluggable-strorage#current-progress-for-pluggable-storage)
- [The future of pluggable storage](https://supabase.com/blog/postgres-pluggable-strorage#the-future-of-pluggable-storage)
- [Timelines for pluggable storage](https://supabase.com/blog/postgres-pluggable-strorage#timelines-for-pluggable-storage)
- [More Postgres content](https://supabase.com/blog/postgres-pluggable-strorage#more-postgres-content)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-pluggable-strorage&text=Next%20steps%20for%20Postgres%20pluggable%20storage)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-pluggable-strorage&text=Next%20steps%20for%20Postgres%20pluggable%20storage)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-pluggable-strorage&t=Next%20steps%20for%20Postgres%20pluggable%20storage)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)