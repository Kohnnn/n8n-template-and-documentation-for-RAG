---
url: "https://supabase.com/blog/introducing-read-replicas"
title: "Introducing Read Replicas"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Introducing Read Replicas

15 Dec 2023

•

8 minute read

[![Angelico de los Reyes avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdragarcia.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Angelico de los ReyesEngineering](https://github.com/dragarcia)

![Introducing Read Replicas](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-read-replicas%2Fread-replicas-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today, we are launching support for Postgres Read Replicas. You can use Read Replicas to:

1. Distribute load across various databases.
2. Serve data closer to your users.
3. Provide data redundancy.
4. Run complex queries without affecting your primary database.

You can create read replicas in any of our 12 supported regions. To start, each project supports up to two replicas.

## What are Read Replicas? [\#](https://supabase.com/blog/introducing-read-replicas\#what-are-read-replicas)

Read replicas continuously, well, _replicate_ data from a primary database. It contains a constantly-updated copy of the data in the Primary.

You can both read and write data on the Primary database. You can _only_ read, on a Read Replica:

|  | `select` | `insert` | `update` | `delete` |
| --- | --- | --- | --- | --- |
| Primary | ✅ | ✅ | ✅ | ✅ |
| Read Replica | ✅ | - | - | - |

Replication is asynchronous. It happens in the background so that transactions aren't blocked on the primary. The delay between writing data to the primary and the read replica receiving the change is called _replication lag_.

Globally Distributed Databases with Read Replicas - YouTube

Supabase

54.4K subscribers

[Globally Distributed Databases with Read Replicas](https://www.youtube.com/watch?v=PX3R1fXjJ2M)

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

[Watch on YouTube](https://www.youtube.com/watch?v=PX3R1fXjJ2M "Watch on YouTube")

## Why Read Replicas? [\#](https://supabase.com/blog/introducing-read-replicas\#why-read-replicas)

To scale your database, you have two choices: horizontal scaling and vertical scaling. Vertical scaling involves adding more RAM and CPU to your existing server. Our 16XL [compute add-on](https://supabase.com/docs/guides/platform/compute-add-ons) has 64 cores CPU and 256 GB RAM - sufficient for almost any well-architected workload.

However, certain workloads may push against the CPU and memory limits of a single server. There’s a limit to how much you can scale vertically. Most cloud providers do not provide instances larger than our 16XL specifications.

This is where horizontal scaling is useful. You can add read replicas to scale more easily. Instead of a single database handling all of your traffic, you can split the traffic across multiple databases.

##### Compute Size

Our read replicas will inherit the compute size of its primary. They will eventually scale independently.

Read replicas are great for reducing the load on your primary database. For instance, you can designate one of your read replicas for analytical tasks. This way, a runaway query in a read replica won't impact the primary.

One of the best features of read replicas is that you can launch them in a different region from your primary. This moves the data closer to your users - querying the nearest read replica for data minimizes overall application latency. We are working on making this easier, stay tuned!

The main drawback of horizontal scaling is complexity. Typically, you need to manage replication lag, handle recovery when a replica fails, and implement some level of application level changes to fully utilize the read replica. In line with our promise to “make Postgres simpler for developers”, we have handled most of that complexity for you:

## Using Read Replicas [\#](https://supabase.com/blog/introducing-read-replicas\#using-read-replicas)

You can manage and visualize read replicas from the [infrastructure settings page](https://supabase.com/dashboard/project/_/settings/infrastructure).

![Read Replicas in the dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-read-replicas%2Fread-replicas-02.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

In the SQL editor, you can choose if you want to run the query on the primary or one of the read replicas.

![Read Replicas](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-read-replicas%2Fread-replicas.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

To make use of your read replicas, copy your connection string for the read replica, update your apps to use the new read replica and you are done! A unique connection pool is also provisioned for each read replica via [Supavisor](https://github.com/supabase/supavisor).

Each replica also has its own associated instance of [PostgREST](https://supabase.com/docs/guides/api), a Data API for [REST](https://supabase.com/docs/guides/api) and [GraphQL](https://supabase.com/docs/guides/graphql). You can directly access each PostgREST instance, similar to connecting to a specific read replica. Alternatively, we offer a load-balancing endpoint which uses a round-robin strategy to route to each of the PostgREST instances.

## Implementation [\#](https://supabase.com/blog/introducing-read-replicas\#implementation)

Postgres offers various methods to replicate data, each with trade-offs. We use the following native methods:

### Streaming replication [\#](https://supabase.com/blog/introducing-read-replicas\#streaming-replication)

Postgres generates a Write Ahead Log (WAL) as database changes occur. With streaming replication, these changes stream from the primary to the read replica server. The WAL alone is sufficient to reconstruct the database to its current state.

This replication method is fast, since changes are streamed directly from the primary to the read replica. On the other hand, it faces challenges when the read replica can't keep up with the WAL changes from its primary. This can happen when the read replica is too small, running on degraded hardware, or has a heavier workload running.

To address this, Postgres does provide tunable configuration, like `wal_keep_size`, to adjust the WAL retained by the primary. If the read replica fails to “catch up” before the WAL surpasses the `wal_keep_size` setting, the replication is terminated. Tuning is a bit of an art - the amount of WAL required is variable for every situation.

### File-based Log shipping [\#](https://supabase.com/blog/introducing-read-replicas\#file-based-log-shipping)

In this replication method, the primary continuously buffers WAL changes to a local file and then sends the file to the read replica. If multiple read replicas are present, files could also be sent to an intermediary location accessible by all. The read replica then reads the WAL files and applies those changes. There is higher replication lag than streaming replication since the primary buffers the changes locally first. It also means there is a small chance that WAL changes do not reach read replicas if the primary goes down before the file is transferred. In these cases, if the primary fails a replica using streaming replication would (in most cases) be more up-to-date than a replica using file-based log shipping.

### File-Based Log shipping 🤝 Streaming replication [\#](https://supabase.com/blog/introducing-read-replicas\#file-based-log-shipping-streaming-replication)

We use a hybrid approach to address the limitations of each method.

![Streaming replication](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-read-replicas%2Fstreaming-replication-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Streaming replication minimizes replication lag, while file-based log shipping provides a fallback. For file-based log shipping, we use our existing Point In Time Recovery (PITR) infrastructure. We regularly archive files from the primary using [WAL-G](https://github.com/wal-g/wal-g), an open source archival and restoration tool, and ship the WAL files to S3.

We combine it with streaming replication to reduce replication lag. Once WAL-G files have been synced from S3, read replicas connect to the primary and stream the WAL directly.

## What's coming [\#](https://supabase.com/blog/introducing-read-replicas\#whats-coming)

### Automatic Failover [\#](https://supabase.com/blog/introducing-read-replicas\#automatic-failover)

With automatic failovers, a read replica is promoted to be the primary if the primary is unhealthy. This feature is currently only available on our Enterprise Plan. However, we are planning to extend this to all paid plans. The introduction of self-serve read replicas is a step in that direction.

### Geo-based load balancing [\#](https://supabase.com/blog/introducing-read-replicas\#geo-based-load-balancing)

Currently, we have implemented a round-robin strategy of routing PostgREST requests to the different databases. This is useful for sharing the load across the primary and the read replica, but in cases where latency is important, you might want to always route to the closest database instead.

### Supabase Products leveraging Replicas [\#](https://supabase.com/blog/introducing-read-replicas\#supabase-products-leveraging-replicas)

We are working on support for database-level load balancing through [Supavisor](https://supabase.com/blog/supavisor-postgres-connection-pooler). When routing database traffic through Supavisor, it routes write queries to the primary and splits read queries between the primary and read replica. This distributes load to all your databases without any changes to your application. Other Supabase products like Auth, Storage, and Realtime use the database heavily. We are working on adding read replica support to these products, so that they can leverage the read replica when appropriate. This means they won’t just query the primary but will also use the read replica’s compute when possible.

## Pricing and Availability [\#](https://supabase.com/blog/introducing-read-replicas\#pricing-and-availability)

Read replicas are priced like regular databases for compute and storage. There is also a per-GB cost for WAL transfer between the primary and read replica. The total price is the sum of:

- The compute instance of the read replica. The compute hours used by your read replica will be added to the total compute hours used by your organization and charged at the same rate.
- The disk size of the read replica will be charged at the same rate of 0.125$ / GB
- Any WAL transfer between the primary and read replica will be charged at 9c / GB

[Sign-ups](https://forms.supabase.com/read-replica) for early access of self-serve Read Replica support are now open. Following which we will progressively rollout self-serve Read Replica support to all paid plans over the next few months.

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fintroducing-read-replicas&text=Introducing%20Read%20Replicas)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fintroducing-read-replicas&text=Introducing%20Read%20Replicas)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fintroducing-read-replicas&t=Introducing%20Read%20Replicas)

[Last post\\
\\
**Supabase Libraries V2: Python, Swift, Kotlin, Flutter, and Typescript** \\
\\
15 December 2023](https://supabase.com/blog/client-libraries-v2)

[Next post\\
\\
**Fly Postgres, managed by Supabase** \\
\\
15 December 2023](https://supabase.com/blog/postgres-on-fly-by-supabase)

[launch-week](https://supabase.com/blog/tags/launch-week) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [What are Read Replicas?](https://supabase.com/blog/introducing-read-replicas#what-are-read-replicas)
- [Why Read Replicas?](https://supabase.com/blog/introducing-read-replicas#why-read-replicas)
- [Using Read Replicas](https://supabase.com/blog/introducing-read-replicas#using-read-replicas)
- [Implementation](https://supabase.com/blog/introducing-read-replicas#implementation)
  - [Streaming replication](https://supabase.com/blog/introducing-read-replicas#streaming-replication)
  - [File-based Log shipping](https://supabase.com/blog/introducing-read-replicas#file-based-log-shipping)
  - [File-Based Log shipping 🤝 Streaming replication](https://supabase.com/blog/introducing-read-replicas#file-based-log-shipping-%F0%9F%A4%9D-streaming-replication)
- [What's coming](https://supabase.com/blog/introducing-read-replicas#whats-coming)
  - [Automatic Failover](https://supabase.com/blog/introducing-read-replicas#automatic-failover)
  - [Geo-based load balancing](https://supabase.com/blog/introducing-read-replicas#geo-based-load-balancing)
  - [Supabase Products leveraging Replicas](https://supabase.com/blog/introducing-read-replicas#supabase-products-leveraging-replicas)
- [Pricing and Availability](https://supabase.com/blog/introducing-read-replicas#pricing-and-availability)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fintroducing-read-replicas&text=Introducing%20Read%20Replicas)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fintroducing-read-replicas&text=Introducing%20Read%20Replicas)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fintroducing-read-replicas&t=Introducing%20Read%20Replicas)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Read Replicas in the dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-read-replicas%2Fread-replicas-02.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Read Replicas](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-read-replicas%2Fread-replicas.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Streaming replication](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-read-replicas%2Fstreaming-replication-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)