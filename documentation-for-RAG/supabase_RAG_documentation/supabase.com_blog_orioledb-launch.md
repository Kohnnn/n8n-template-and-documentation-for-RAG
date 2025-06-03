---
url: "https://supabase.com/blog/orioledb-launch"
title: "OrioleDB Public Alpha"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# OrioleDB Public Alpha

01 Dec 2024

•

2 minute read

[![Pavel Borisov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F63344111%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Pavel BorisovPostgres Engineer](https://github.com/pashkinelfe)

![OrioleDB Public Alpha](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-01-orioledb-release%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# OrioleDB Public Alpha [\#](https://supabase.com/blog/orioledb-launch\#orioledb-public-alpha)

Today, we're releasing the Public Alpha of [OrioleDB](https://www.orioledb.com/) on the Supabase platform.

### What’s OrioleDB? [\#](https://supabase.com/blog/orioledb-launch\#whats-orioledb)

OrioleDB is a **storage extension** which uses Postgres' pluggable storage system. It’s designed to be a drop-in replacement for Postgres’ default Heap storage.

You can read more about OrioleDB [here](https://www.orioledb.com/blog/orioledb-beta7-benchmarks) and learn why you might choose it over the default Postgres storage engine.

### Limitations [\#](https://supabase.com/blog/orioledb-launch\#limitations)

This initial release is a Public Alpha and you should _not_ use it for Production workloads. The release comes with several limitations:

- The release is restricted to Free organizations. You will not be able to upgrade OrioleDB projects to larger instance sizes. If you want to run OrioleDB on a larger instance we suggest following the [Getting Started](https://www.orioledb.com/docs/usage/getting-started) guide on OrioleDB’s official website.
- Index support is restricted to the Postgres default B-Tree index type. Other indexs like GIN/GiST/BRIN/Hash, and pgvector's HNSW/IVFFlat are not supported.

### Should you use it today? [\#](https://supabase.com/blog/orioledb-launch\#should-you-use-it-today)

At this stage, the goal of adding OrioleDB to the platform is to make it easier for testers to give feedback. If you’re running Production workloads, stick to the standard options available.

### Getting started and more info [\#](https://supabase.com/blog/orioledb-launch\#getting-started-and-more-info)

To get started today, go to [database.new](http://database.new/) and choose “Postgres with OrioleDB” under the "Advanced Configuration" section when launching a new database.

![orioledb-project-create](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-12-01-orioledb-release%2Forioledb-project-create.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

If you want to learn more about OrioleDB and their vision for the future, check out the [blog post the OrioleDB team released today](https://www.orioledb.com/blog/orioledb-beta7-benchmarks).

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Forioledb-launch&text=OrioleDB%20Public%20Alpha)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Forioledb-launch&text=OrioleDB%20Public%20Alpha)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Forioledb-launch&t=OrioleDB%20Public%20Alpha)

[Last post\\
\\
**Supabase AI Assistant v2** \\
\\
2 December 2024](https://supabase.com/blog/supabase-ai-assistant-v2)

[Next post\\
\\
**Executing Dynamic JavaScript Code on Supabase with Edge Functions** \\
\\
13 November 2024](https://supabase.com/blog/supabase-dynamic-functions)

[supabase-engineering](https://supabase.com/blog/tags/supabase-engineering)

On this page

- [OrioleDB Public Alpha](https://supabase.com/blog/orioledb-launch#orioledb-public-alpha)
  - [What’s OrioleDB?](https://supabase.com/blog/orioledb-launch#whats-orioledb)
  - [Limitations](https://supabase.com/blog/orioledb-launch#limitations)
  - [Should you use it today?](https://supabase.com/blog/orioledb-launch#should-you-use-it-today)
  - [Getting started and more info](https://supabase.com/blog/orioledb-launch#getting-started-and-more-info)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Forioledb-launch&text=OrioleDB%20Public%20Alpha)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Forioledb-launch&text=OrioleDB%20Public%20Alpha)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Forioledb-launch&t=OrioleDB%20Public%20Alpha)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)