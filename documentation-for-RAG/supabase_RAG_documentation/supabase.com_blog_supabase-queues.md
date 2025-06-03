---
url: "https://supabase.com/blog/supabase-queues"
title: "Supabase Queues"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Queues

05 Dec 2024

•

7 minute read

[![Ivan Vasilov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fivasilov.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ivan VasilovEngineering](https://twitter.com/ivasilov)

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![Supabase Queues](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we're releasing [Supabase Queues](https://supabase.com/modules/queues), for durable background task processing.

Supabase Queues is a Postgres-native, durable Message Queue with guaranteed delivery, improving the scalability and resiliency of your applications. It's designed to work seamlessly with the entire Supabase platform.

We added the missing piece! 🧩 - YouTube

Supabase

54.4K subscribers

[We added the missing piece! 🧩](https://www.youtube.com/watch?v=UEwfaElBnZk)

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

[Watch on YouTube](https://www.youtube.com/watch?v=UEwfaElBnZk "Watch on YouTube")

Supabase Queues is built on the [pgmq](https://github.com/tembo-io/pgmq) extension by the team at [Tembo](https://github.com/tembo-io).

It's a Supabase policy to [support existing tools](https://supabase.com/docs/guides/getting-started/architecture#support-existing-tools) wherever possible, and the Tembo team have generously licensed their extension with the OSI-compatible [PostgreSQL license](https://github.com/tembo-io/pgmq?tab=PostgreSQL-1-ov-file).

We're very thankful to all the contributors and we look forward to working with the Tembo community.

## Supabase Queues Features [\#](https://supabase.com/blog/supabase-queues\#supabase-queues-features)

1. **Postgres Native**: Built on top of the open source `pgmq` database extension, create and manage Queues with any Postgres tooling.
2. **Granular Authorization**: Control client-side consumer access to Queues with API permissions and Row Level Security (RLS) policies.
3. **Guaranteed Message Delivery**: Messages added to Queues are guaranteed to be delivered to your consumers.
4. **Exactly Once Message Delivery**: A Message is delivered exactly once to a consumer within a customizable visibility window.
5. **Queue Management and Monitoring**: Create, manage, and monitor Queues and Messages in the Supabase Dashboard.
6. **Message Durability and Archival**: Messages are stored in Postgres and you can choose to archive them for analytical or auditing purposes.

## Do You Need Queues? [\#](https://supabase.com/blog/supabase-queues\#do-you-need-queues)

A Queue is used to manage and process tasks asynchronously. Typically, you use a Queue for long-running tasks to ensure that your application is robust.

**For example, sending emails:**

Let's say you want to send a welcome email to a user after they register on your website. Instead of sending the email immediately within the registration process - which could slow down the user's experience - you can place the “email task” into a Queue.A separate email service can then process this task, sending the email without affecting the registration flow. Even better: if the email bounces then the task could "reappear" in the Queue to get processed again.

In this scenario, Queues have improved your application's _performance_ and _resilience_. Other cases include:

- **Process tasks asynchronously**: offload time-consuming operations, like sending emails, processing images, and generating embeddings.
- **Communication between services:** decouple your services by passing messages through a central queue.
- **Load Balancing**: Distribute tasks evenly across multiple workers.

## Creating Queues [\#](https://supabase.com/blog/supabase-queues\#creating-queues)

Queues can be created in the Dashboard or using SQL / database migrations.

For this section we'll focus on the Dashboard. You can refer to the
[documentation](https://supabase.com/docs/guides/queues/api) for SQL.

### Types of Queues [\#](https://supabase.com/blog/supabase-queues\#types-of-queues)

There are several types of queues available:

![Queue types](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fqueue-types.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

**Basic Queues**: Simple, reliable queues with core functionality, ideal for most use cases. Messages are stored and processed within Postgres using standard transactional guarantees.

**Unlogged Queues**: Optimized for performance, unlogged queues avoid writing messages to disk, making them faster but less durable in case of a database crash. Suitable for transient or less critical workloads.

**Partitioned Queues** (coming soon): Designed for high throughput and scalability, partitioned queues distribute messages across multiple partitions, enabling parallel processing and more efficient load handling.

### Queues with Postgres Row-Level Security [\#](https://supabase.com/blog/supabase-queues\#queues-with-postgres-row-level-security)

Supabase Queues are compatible with Postgres Row-Level Security (RLS), providing fine-grained access control to Messages. RLS Policies restrict which users or roles can insert, select, update, or delete messages in specific queues.

## Adding Messages [\#](https://supabase.com/blog/supabase-queues\#adding-messages)

Once your Queue is configured you can begin adding Messages.

![Add a message](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fadd-message.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### From the Dashboard [\#](https://supabase.com/blog/supabase-queues\#from-the-dashboard)

Let's create a new Basic Queue and add a Message.

![Create a queue](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fcreate-a-queue.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Add a message](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fadd-message.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Message details](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fadd-message-modal.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### From the server [\#](https://supabase.com/blog/supabase-queues\#from-the-server)

If you're [connecting](https://supabase.com/docs/guides/database/connecting-to-postgres) to your Postgres database from a server, you can add messages using SQL from any Postgres client:

`
select * from pgmq.send(
queue_name  => 'foo',
msg         => '{ "hello": "world" }',
);
`

### From the client [\#](https://supabase.com/blog/supabase-queues\#from-the-client)

We have provided several functions that can be invoked from the [client libraries](https://supabase.com/docs#client-libraries) if you need to add messages from a browser or mobile app. For example:

`
import { createClient } from '@supabase/supabase-js'
const url = 'SUPABASE_URL'
const key = 'SUPABASE_ANON_KEY'
const queues = createClient(url, key, {
db: { schema: 'pgmq_public' },
})
const { data, error } = await queues.rpc('send', {
queue_name: 'foo',
message: { hello: 'world' },
})
console.log('Message: ', data)
`

For security, this feature is [disabled by default](https://supabase.com/blog/supabase-queues#security-and-permissions). There are several functions defined in the `pgmq_public` schema: `send`, `send_batch`, `read`, `pop`, `archive`, `delete`. You can find more details in the [docs](https://supabase.com/docs/guides/queues/api).

## Security and Permissions [\#](https://supabase.com/blog/supabase-queues\#security-and-permissions)

By default, Queues are only accessible via SQL and not exposed over the Supabase Data API. You can manage this in the Data API settings by [exposing the pgmq\_public schema](https://supabase.com/docs/guides/api/using-custom-schemas). If you expose this schema, you must use [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) (RLS) to manage access to your queues.

Beyond RLS, Postgres roles can be granted granular permissions to interact with Queues.

For example, the following permissions allow authenticated users can fully manipulate messages, whereas anonymous users can only retrieve messages:

![Queue permissions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fpermissions.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The `postgres` and `service_role` roles receive permissions by default and should remain enabled for server-side operations.

## Monitoring Queues and Messages [\#](https://supabase.com/blog/supabase-queues\#monitoring-queues-and-messages)

You can use the Dashboard to inspect your Messages, including: status, number of retries, and payload. You can also postpone, archive, or delete messages at any time.

From the Queues page, just click on a Queue to inspect it. From there you can click on a message to see more details:

![Message details](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fmessage-detail.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Try Supabase Queues Today [\#](https://supabase.com/blog/supabase-queues\#try-supabase-queues-today)

1. Visit the [Integrations page](https://supabase.com/dashboard/project/_/integrations) in your project.
2. Enable the **Queues** Postgres Module.
3. Create your first Queue.

![Enable queues](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fintegrations.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Pricing [\#](https://supabase.com/blog/supabase-queues\#pricing)

Supabase Queues runs entirely in your database so there's no additional costs to use the functionality.

We recommend you configure your database's Compute and Disk settings appropriately to support your Queues workload.

## Postgres for Everything [\#](https://supabase.com/blog/supabase-queues\#postgres-for-everything)

Using Postgres for your Queue system keeps your stack lean and familiar. You can add Messages to Queues within the same transaction that modifies related data, preventing inconsistencies and reducing the need for additional coordination. Postgres' robust indexing, JSONB support, and partitioning also enable scalable, high-performance queue management directly in your database.

By eliminating the need for separate infrastructure like RabbitMQ or Kafka, you reduce costs, streamline deployments, and leverage existing Postgres tools for monitoring, backups, and security. Features like Row-Level Security, rich SQL querying, and built-in archiving make Postgres a powerful, unified solution for both data storage and messaging.

[Launch Week13](https://supabase.com/launch-week/13)

2-6 December 24

[Day 1 -Supabase AI Assistant v2](https://supabase.com/blog/supabase-ai-assistant-v2)

[Day 2 -Supabase Functions: Background Tasks and WebSockets](https://supabase.com/blog/edge-functions-background-tasks-websockets)

[Day 3 -Supabase Cron: Schedule Recurring Jobs in Postgres](https://supabase.com/blog/supabase-cron)

[Day 4 -Supabase Queues](https://supabase.com/blog/supabase-queues)

[Day 5 -database.build v2: Bring-Your-Own-LLM](https://supabase.com/blog/database-build-v2)

Build Stage

[01 -OrioleDB Public Alpha](https://supabase.com/blog/orioledb-launch)

[02 -Supabase CLI v2: Config as Code](https://supabase.com/blog/cli-v2-config-as-code)

[03 -High Performance Disks](https://supabase.com/blog/high-performance-disks)

[04 -Restore to a New Project](https://supabase.com/blog/restore-to-a-new-project)

[05 -Hack the Base! with Supabase](https://supabase.com/blog/hack-the-base)

[Community Meetups](https://supabase.com/events?category=meetup)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-queues&text=Supabase%20Queues)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-queues&text=Supabase%20Queues)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-queues&t=Supabase%20Queues)

[Last post\\
\\
**Top 10 Launches of Launch Week 13** \\
\\
6 December 2024](https://supabase.com/blog/launch-week-13-top-10)

[Next post\\
\\
**High Performance Disk** \\
\\
5 December 2024](https://supabase.com/blog/high-performance-disks)

[queues](https://supabase.com/blog/tags/queues) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [Supabase Queues Features](https://supabase.com/blog/supabase-queues#supabase-queues-features)
- [Do You Need Queues?](https://supabase.com/blog/supabase-queues#do-you-need-queues)
- [Creating Queues](https://supabase.com/blog/supabase-queues#creating-queues)
  - [Types of Queues](https://supabase.com/blog/supabase-queues#types-of-queues)
  - [Queues with Postgres Row-Level Security](https://supabase.com/blog/supabase-queues#queues-with-postgres-row-level-security)
- [Adding Messages](https://supabase.com/blog/supabase-queues#adding-messages)
  - [From the Dashboard](https://supabase.com/blog/supabase-queues#from-the-dashboard)
  - [From the server](https://supabase.com/blog/supabase-queues#from-the-server)
  - [From the client](https://supabase.com/blog/supabase-queues#from-the-client)
- [Security and Permissions](https://supabase.com/blog/supabase-queues#security-and-permissions)
- [Monitoring Queues and Messages](https://supabase.com/blog/supabase-queues#monitoring-queues-and-messages)
- [Try Supabase Queues Today](https://supabase.com/blog/supabase-queues#try-supabase-queues-today)
- [Pricing](https://supabase.com/blog/supabase-queues#pricing)
- [Postgres for Everything](https://supabase.com/blog/supabase-queues#postgres-for-everything)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-queues&text=Supabase%20Queues)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-queues&text=Supabase%20Queues)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-queues&t=Supabase%20Queues)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Queue types](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fqueue-types.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Add a message](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fadd-message.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Create a queue](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fcreate-a-queue.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Add a message](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fadd-message.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Message details](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fadd-message-modal.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Queue permissions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fpermissions.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Message details](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fmessage-detail.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Enable queues](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fintegrations.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)