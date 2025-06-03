---
url: "https://supabase.com/blog/postgres-on-fly-by-supabase"
title: "Fly Postgres, managed by Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Fly Postgres, managed by Supabase

15 Dec 2023

•

6 minute read

[![Inian Parameshwaran avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F2155545%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Inian ParameshwaranEngineering](https://twitter.com/everConfusedGuy)

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Fly Postgres, managed by Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supafly%2Ffly-postgres-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Fly Postgres has been deprecated. See [deprecation announcement](https://github.com/orgs/supabase/discussions/33413) for more details.

We're launching Fly Postgres, a managed Postgres offering by Supabase and [Fly.io](http://fly.io/).

Fly Postgres databases launch on Fly.io's edge computing platform from any of their 37+ locations. You get everything you expect from a Supabase managed database:

- a full-featured Postgres database with [over 40+ extensions](https://github.com/supabase/postgres)
- [pgvector](https://github.com/pgvector/pgvector/) support for [Vector/AI workloads](https://supabase.com/docs/guides/ai)
- [Supavisor](https://supabase.com/blog/supavisor-postgres-connection-pooler), our Postgres connection pooler
- Daily backups and point-in-time recovery
- [Branching](https://supabase.com/docs/guides/platform/branching), [observability](https://github.com/supabase/supabase-grafana), and migrations
- A [dashboard](https://supabase.com/blog/studio-introducing-assistant) for managing your database
- Auto-generated Data APIs:
  - [REST](https://supabase.com/docs/guides/api) (using [PostgREST](https://postgrest.org/))
  - [GraphQL](https://supabase.com/docs/guides/graphql) (using [pg\_graphql](https://github.com/supabase/pg_graphql/))

This is deployed within the Fly infrastructure, making it the fastest Postgres database for your data intensive applications deployed on Fly.

## Managing expectations [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#managing-expectations)

Before you get too excited, this will be a progressive rollout. It turns out that building inter-company integrations is a lot of work when you factor in billing, support handoff, and educating Supabase staff on how to understand [sandwich analogies](https://fly.io/blog/carving-the-scheduler-out-of-our-orchestrator/).

We've been working with a few early testers and we have some bugs to iron out. You can [sign up for the waitlist](https://forms.supabase.com/fly-postgres) if you want to help with testing. We'll accept more testers next month, and we'll communicate more release timelines as soon as we're confident that your data is safe.

## Supabase + Fly = SupaFly? [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#supabase--fly--supafly)

We're excited about what this partnership means for 2024. Namely, distributing Postgres across the planet. The Firecracker VM gives us some neat ideas for Postgres. Integrating with Fly also puts a bunch of easy-to-spin-up compute resources right next to the database. That sounds like fun.

## Managed vs unmanaged Postgres [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#managed-vs-unmanaged-postgres)

Fly's current Postgres offering is [unmanaged](https://fly.io/docs/postgres/getting-started/what-you-should-know). This means that you're responsible for handling scaling, point-in-time backups, replication, major version upgrades, etc. We'll run Fly's _managed_ Postgres, which means that we do all that for you, and you can concentrate on building.

The managed service is built with the [Fly extension API](https://fly.io/docs/reference/extensions_api/) (also used by [Fly Redis](https://fly.io/docs/reference/redis/)).

Testers can launch a Postgres database using the `fly extensions` command:

`
fly extensions supabase create
`

Once the service is stable, it will be swapped for the `postgres` namespace:

`
fly postgres create
`

With Fly Postgres, the database is deployed within Fly infrastructure leading to a much lower latency for data heavy applications.

## Under the hood [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#under-the-hood)

Let's dig into the implementation.

### **Working with Fly machines** [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#working-with-fly-machines)

Fly Postgres is built on top of [Fly machines](https://fly.io/docs/machines/). Machines are light-weight Firecracker VMs. The Machines API offers substantial control over an application's lifecycle. They can be suspended during inactivity and resumed within a couple of seconds whenever a new request arrives.

We built [fly-admin](https://github.com/supabase/fly-admin), a Typescript wrapper to simplify our interaction with the Fly API. Supabase bundles a few extra services into Postgres, so we prepared a single Docker image which we can pass to the Fly Machines API. Our current build process outputs an AMI for AWS using [Packer](https://www.packer.io/). We re-use parts of that pipeline to build an [All In One Image](https://github.com/supabase/postgres/tree/develop/docker/all-in-one). This image has all the services to run a Supabase project within a single Docker container.

### **Move to multi-cloud** [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#move-to-multi-cloud)

With this launch, Supabase is officially multi-cloud. We deliberately avoided using AWS's managed services when building Supabase to simplify our multi-cloud transition. These transitions are never simple - even the base primitives offered between cloud providers can vary significantly.

For example, Fly Machines offer a simple method for suspending a VM when it's not in use, transparently resuming it within seconds. This simplifies the process of pausing inactive databases. There is no direct primitive on AWS to achieve this.

On the other hand, we had to work around a few AWS primitives that Fly doesn't provide. Fly machines don't have network-attached storage, so we treat any data in Fly volumes as ephemeral. We run physical backups for all projects running on Fly using WAL-G. Database changes are continuously streamed to S3. When there is a host or volume corruption, we restore the project to a new Fly host using the latest data in S3.

To capture host issues on AWS, we listen to [AWS Health events](https://docs.aws.amazon.com/health/latest/ug/aws-health-concepts-and-terms.html). For Fly, we send the Machine logs to [Logflare](https://logflare.com/) using the [fly-log-shipper](https://github.com/superfly/fly-log-shipper).

In addition to publishing images in AWS's container registry, we publish the All In One image to Fly's Docker registry. This improved the reliability and performance of project launches on Fly.

### **Building the Fly extension** [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#building-the-fly-extension)

Fly has an [excellent approach](https://fly.io/docs/reference/extensions_api/) for extending their platform. We added a few routes to our API to provision users and projects and we were on our way.

Fly users can access the Supabase dashboard using their existing Fly credentials. The Supabase API initiates an OAuth flow with Fly to authenticate the user. Our Auth team created a [Fly OAuth provider](https://github.com/supabase/gotrue/pull/1261) to make the integration with our API easier.

## Challenges [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#challenges)

We're still working through a few challenges with the Fly team.

### Support for Network Restrictions [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#support-for-network-restrictions)

The [network restrictions](https://supabase.com/docs/guides/platform/network-restrictions) feature relies on the container receiving the correct IP of the client connecting to it. With our current setup, the container sees the Fly proxy IP instead. Connections run through the Fly proxy, which exposes the Proxy protocol. Postgres can't use this information directly, but we're looking at [making Supavisor proxy-protocol aware](https://github.com/supabase/supavisor).

### Backups within Fly [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#backups-within-fly)

Fly projects are backed up to AWS S3 as Fly doesn't provide managed Blob storage (yet). This incurs inter-cloud bandwidth fees. Luckily, Fly are working on [Blob Storage](https://fly.io/docs/flyctl/extensions-tigris-list/), watch this space.

## Getting started [\#](https://supabase.com/blog/postgres-on-fly-by-supabase\#getting-started)

Sign up for the preview [here](https://forms.supabase.com/fly-postgres), wait till we allowlist your org, and get started with the [Quickstart](https://supabase.com/docs/guides/platform/fly-postgres#quickstart) in our docs.

Fly organizations will get one free project. We're still working through some of the finer details on billing, but the pricing will remain relatively unchanged from our current [pricing](https://supabase.com/pricing).

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-on-fly-by-supabase&text=Fly%20Postgres%2C%20managed%20by%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-on-fly-by-supabase&text=Fly%20Postgres%2C%20managed%20by%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-on-fly-by-supabase&t=Fly%20Postgres%2C%20managed%20by%20Supabase)

[Last post\\
\\
**Introducing Read Replicas** \\
\\
15 December 2023](https://supabase.com/blog/introducing-read-replicas)

[Next post\\
\\
**Supabase Auth: Identity Linking, Hooks, and HaveIBeenPwned integration** \\
\\
14 December 2023](https://supabase.com/blog/supabase-auth-identity-linking-hooks)

[launch-week](https://supabase.com/blog/tags/launch-week) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [Managing expectations](https://supabase.com/blog/postgres-on-fly-by-supabase#managing-expectations)
- [Supabase + Fly = SupaFly?](https://supabase.com/blog/postgres-on-fly-by-supabase#supabase--fly--supafly)
- [Managed vs unmanaged Postgres](https://supabase.com/blog/postgres-on-fly-by-supabase#managed-vs-unmanaged-postgres)
- [Under the hood](https://supabase.com/blog/postgres-on-fly-by-supabase#under-the-hood)
  - [**Working with Fly machines**](https://supabase.com/blog/postgres-on-fly-by-supabase#working-with-fly-machines)
  - [**Move to multi-cloud**](https://supabase.com/blog/postgres-on-fly-by-supabase#move-to-multi-cloud)
  - [**Building the Fly extension**](https://supabase.com/blog/postgres-on-fly-by-supabase#building-the-fly-extension)
- [Challenges](https://supabase.com/blog/postgres-on-fly-by-supabase#challenges)
  - [Support for Network Restrictions](https://supabase.com/blog/postgres-on-fly-by-supabase#support-for-network-restrictions)
  - [Backups within Fly](https://supabase.com/blog/postgres-on-fly-by-supabase#backups-within-fly)
- [Getting started](https://supabase.com/blog/postgres-on-fly-by-supabase#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-on-fly-by-supabase&text=Fly%20Postgres%2C%20managed%20by%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-on-fly-by-supabase&text=Fly%20Postgres%2C%20managed%20by%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-on-fly-by-supabase&t=Fly%20Postgres%2C%20managed%20by%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)