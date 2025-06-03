---
url: "https://supabase.com/blog/supabase-clickhouse-partnership"
title: "ClickHouse Partnership, improved Postgres Replication, and Disk Management"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# ClickHouse Partnership, improved Postgres Replication, and Disk Management

30 Oct 2024

•

6 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![ClickHouse Partnership, improved Postgres Replication, and Disk Management](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fclickhouse-supabase%2Fsupabase-clickhouse-og.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We're seeing an emerging trend for AI customers: Postgres and ClickHouse is becoming the “default data stack”.

This makes sense - AI companies typically generate a lot of logs and analytical data, which is better suited for an OLAP database like ClickHouse.

> The combination of Supabase and ClickHouse together are perfect for [Helicone.ai](https://helicone.ai/), providing the flexibility of Postgres with the analytical power of ClickHouse — an open-source stack we can trust and customize.
>
> ![Justin Torre, CTO @ Helicone.ai avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fjustin-torre.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Justin Torre, CTO @ Helicone.ai

## Supabase + ClickHouse Partnership [\#](https://supabase.com/blog/supabase-clickhouse-partnership\#supabase--clickhouse-partnership)

The partnership between Supabase and ClickHouse aims to create a seamless experience, building on the already solid Postgres + ClickHouse foundation. Today, we're releasing new features to enhance this integration.

> ClickHouse is very excited to partner with Supabase to make it easy for customers to use both technologies together. Through this partnership, we aim to make it even simpler for Postgres developers to use ClickHouse in conjunction and build real-time, data-driven applications at scale.
>
> ![Aaron Katz, CEO @ ClickHouse Inc. avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Faaron-katz.jpg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Aaron Katz, CEO @ ClickHouse Inc.

## Using Postgres and ClickHouse together [\#](https://supabase.com/blog/supabase-clickhouse-partnership\#using-postgres-and-clickhouse-together)

Before diving into those changes, some context on how most customers use Supabase and ClickHouse together. While both are databases, they serve different use-cases:

- **Postgres:** Ideal for storing and querying application data, powering critical transactional and web app use cases.
- **ClickHouse:** Optimized for analytics and reporting, supporting both customer-facing and internal applications

Postgres is a row-oriented database, ClickHouse is column-oriented. The ClickHouse team have a [great write up about the difference](https://clickhouse.com/docs/en/intro#row-oriented-vs-column-oriented-storage) between the two formats.

![Browser proxy diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fclickhouse-supabase%2Fpostgres-clickhouse--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

To provide an interface between these, Supabase customers generally use:

1. [clickhouse\_fdw](https://supabase.com/docs/guides/database/extensions/wrappers/clickhouse) to query their ClickHouse data from their Postgres database.
2. [PeerDB](https://www.peerdb.io/) to replicate their data from Postgres to ClickHouse.

![Browser proxy diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fclickhouse-supabase%2Fpostgres-clickhouse-integration--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Improving the ClickHouse & Supabase experience [\#](https://supabase.com/blog/supabase-clickhouse-partnership\#improving-the-clickhouse--supabase-experience)

We're making a number of changes to our platform based on the feedback we've had from customers.

### Updated ClickHouse Foreign Data Wrapper [\#](https://supabase.com/blog/supabase-clickhouse-partnership\#updated-clickhouse-foreign-data-wrapper)

Using the [ClickHouse FDW](https://fdw.dev/catalog/clickhouse/), you can directly query your ClickHouse database from Postgres:

`
-- Connect Postgres to your ClickHouse database:
create foreign table user_analytics (
id bigint,
user_id bigint,
event text
)
server clickhouse_server
options ( table 'UserAnalytics' );
-- Query your ClickHouse instance from Postgres:
select * from user_analytics where user_id = 1;
`

This means you can query your ClickHouse data using the Postgres tooling that you're familiar with.

The Wrapper now has support for ClickHouse [Parameterized Views](https://clickhouse.com/docs/en/sql-reference/statements/create/view#parameterized-view). With this update, you can pass query parameters directly to ClickHouse, taking full advantage of its analytical engine::

`
create foreign table user_analytics (
id bigint,
user_id bigint,
_event text,
)
server clickhouse_server
options ( table '(select * from UserAnalytics(event=${_event}))' );
select * from user_analytics where _event='button_click';
`

### More granular replication control [\#](https://supabase.com/blog/supabase-clickhouse-partnership\#more-granular-replication-control)

Many of our customers use [PeerDB](https://www.peerdb.io/) to replicate data from Postgres to ClickHouse. This has occasionally presented challenges, particularly with Postgres's default 1GB WAL size, which, for large data volumes, can result in data loss if the WAL exceeds this size.

To resolve this, we've added 13 [configurable Postgres parameters](https://supabase.com/docs/guides/database/custom-postgres-config), enabling you to adjust replication settings through the CLI. For example, you can increase the default WAL size to 2GB:

`
supabase --experimental --project-ref xxxx-yyy \
postgres-config update --config max_slot_wal_keep_size=2GB
`

The new CLI config includes the following Postgres parameters:

01. [logical\_decoding\_work\_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-LOGICAL-DECODING-WORK-MEM): Controls memory used during logical decoding.
02. [max\_connections](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-MAX-CONNECTIONS): Limits total connections to the Postgres server.
03. [max\_locks\_per\_transaction](https://www.postgresql.org/docs/current/runtime-config-locks.html#GUC-MAX-LOCKS-PER-TRANSACTION): Sets the maximum locks allowed in a single transaction.
04. [max\_replication\_slots](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS): Defines the number of replication slots for data streaming.
05. [max\_slot\_wal\_keep\_size](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE): Limits disk space for WAL in replication slots.
06. [max\_standby\_archive\_delay](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-STANDBY-ARCHIVE-DELAY): Sets how long standby servers can wait for archive recovery.
07. [max\_standby\_streaming\_delay](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-STANDBY-STREAMING-DELAY): Controls delay on standby servers for streaming replication.
08. [max\_wal\_size](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-MAX-WAL-SIZE): Specifies the maximum size of the Write Ahead Log.
09. [max\_wal\_senders](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-WAL-SENDERS): Sets the maximum number of processes sending WAL data.
10. [max\_worker\_processes](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES): Defines the number of background worker processes.
11. [shared\_buffers](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-SHARED-BUFFERS): Determines the amount of memory for shared buffers.
12. [wal\_keep\_size](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-KEEP-SIZE): Sets minimum WAL size to keep for standby servers.
13. [wal\_sender\_timeout](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT): Specifies the timeout for inactive WAL sender processes.

### Improved Disk Management [\#](https://supabase.com/blog/supabase-clickhouse-partnership\#improved-disk-management)

Supabase now provides granular control over disk usage for your Postgres database:

![Disk management](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fclickhouse-supabase%2Fdisk-management.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This is driven directly by customers using tools like PeerDB. With adjustable WAL configuration, it's important that developers can manage the disk as well. For example, on the Pro Plan's 8GB disk, you can configure your project with options like:

- Default: 7GB database space, 1GB Write Ahead Log
- Custom example: 6GB database space, 2 GB Write Ahead Log

Additionally, we're introducing High-performance Disks. We'll release more details about this later.

### ClickHouse platform updates [\#](https://supabase.com/blog/supabase-clickhouse-partnership\#clickhouse-platform-updates)

The ClickHouse team have also been busy. They've released a number of updates to their platform, including:

1. A native Supabase OAuth integration in PeerDB for Postgres CDC to ClickHouse.
2. Support for IPV6 in PeerDB Cloud.

You can learn more about these features in the [Supabase Partnership](https://clickhouse.com/blog/supabase-partnership-native-postgres-replication-clickhouse-fdw) post they released today.

## What's next? [\#](https://supabase.com/blog/supabase-clickhouse-partnership\#whats-next)

Improving the experience between Postgres and ClickHouse is the first phase of this partnership. We're already working on native platform integrations. If you're using (or plan to use) Supabase and ClickHouse together please [reach out](https://supabase.com/enterprise) \- we'd love more design partners to help shape the future of this integration.

![Supabase integrations](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fclickhouse-supabase%2Fintegrations.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

If you simply want to try out the tools and updates we've described above, you can get started with all of them, free of charge:

- Supabase: [database.new](https://database.new/)
- ClickHouse: [clickhouse.com](https://clickhouse.com/)
- PeerDB: [peerdb.io](https://www.peerdb.io/)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-clickhouse-partnership&text=ClickHouse%20Partnership%2C%20improved%20Postgres%20Replication%2C%20and%20Disk%20Management)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-clickhouse-partnership&text=ClickHouse%20Partnership%2C%20improved%20Postgres%20Replication%2C%20and%20Disk%20Management)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-clickhouse-partnership&t=ClickHouse%20Partnership%2C%20improved%20Postgres%20Replication%2C%20and%20Disk%20Management)

[Last post\\
\\
**Executing Dynamic JavaScript Code on Supabase with Edge Functions** \\
\\
13 November 2024](https://supabase.com/blog/supabase-dynamic-functions)

[Next post\\
\\
**Live Share: Connect to in-browser PGlite with any Postgres client** \\
\\
10 October 2024](https://supabase.com/blog/database-build-live-share)

[postgres](https://supabase.com/blog/tags/postgres) [clickhouse](https://supabase.com/blog/tags/clickhouse)

On this page

- [Supabase + ClickHouse Partnership](https://supabase.com/blog/supabase-clickhouse-partnership#supabase--clickhouse-partnership)
- [Using Postgres and ClickHouse together](https://supabase.com/blog/supabase-clickhouse-partnership#using-postgres-and-clickhouse-together)
- [Improving the ClickHouse & Supabase experience](https://supabase.com/blog/supabase-clickhouse-partnership#improving-the-clickhouse--supabase-experience)
  - [Updated ClickHouse Foreign Data Wrapper](https://supabase.com/blog/supabase-clickhouse-partnership#updated-clickhouse-foreign-data-wrapper)
  - [More granular replication control](https://supabase.com/blog/supabase-clickhouse-partnership#more-granular-replication-control)
  - [Improved Disk Management](https://supabase.com/blog/supabase-clickhouse-partnership#improved-disk-management)
  - [ClickHouse platform updates](https://supabase.com/blog/supabase-clickhouse-partnership#clickhouse-platform-updates)
- [What's next?](https://supabase.com/blog/supabase-clickhouse-partnership#whats-next)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-clickhouse-partnership&text=ClickHouse%20Partnership%2C%20improved%20Postgres%20Replication%2C%20and%20Disk%20Management)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-clickhouse-partnership&text=ClickHouse%20Partnership%2C%20improved%20Postgres%20Replication%2C%20and%20Disk%20Management)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-clickhouse-partnership&t=ClickHouse%20Partnership%2C%20improved%20Postgres%20Replication%2C%20and%20Disk%20Management)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Browser proxy diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fclickhouse-supabase%2Fpostgres-clickhouse--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Browser proxy diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fclickhouse-supabase%2Fpostgres-clickhouse-integration--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Disk management](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fclickhouse-supabase%2Fdisk-management.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase integrations](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fclickhouse-supabase%2Fintegrations.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)