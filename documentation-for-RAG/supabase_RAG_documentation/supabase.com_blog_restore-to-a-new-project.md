---
url: "https://supabase.com/blog/restore-to-a-new-project"
title: "Restore to a New Project"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Restore to a New Project

06 Dec 2024

•

3 minute read

[![Paul Caselton avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fcrispy1975.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CaseltonEngineering](https://github.com/crispy1975)

![Restore to a New Project](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Frestore-to-a-new-project%2Fthumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we’re adding [Restore to a New Project](https://supabase.com/docs/guides/platform/backups#restore-to-a-new-project).

You can use this new tool to copy data easily from an existing Supabase project to a new one. **Restore to a New Project** integrates seamlessly with daily physical backups and Point-in-Time Recovery (PITR) to provide flexible restoration options.

Restore to a New Project requires physical backups to be enabled. It is available to all customers on a paid plan.

## How it Works [\#](https://supabase.com/blog/restore-to-a-new-project\#how-it-works)

When physical backups are enabled, Supabase triggers daily backups of project data. You can use this backup to restore to a new Supabase project. The new project should match the original project attributes:

- Size of compute instance.
- Disk settings; volume type, size, IOPS, and throughput.
- SSL enforcement configuration.
- Network restrictions.
- Cloud region.

After launching your restored project, the rest of the process is automated. The length of time for a new project to provision will depend on the size of the source dataset.

The new project will be available in the Supabase Dashboard as soon as the copy process has completed. This project will behave as any other Supabase project and is completely independent of the source.

### Point-in-Time Recovery [\#](https://supabase.com/blog/restore-to-a-new-project\#point-in-time-recovery)

In addition to daily backups it is possible to restore from a project with PITR enabled. This allows for very fine granularity when selecting the desired point to restore from. The process is very similar as with daily backup with the exception of being asked to select a specific time.

## Unlimited Cloning from a Source Project [\#](https://supabase.com/blog/restore-to-a-new-project\#unlimited-cloning-from-a-source-project)

To ensure maximum flexibility a source project can be _copied_ as many times as required, making the tool perfect for testing, development environments etc. However, please note that cloning from an already cloned project is not currently supported (this is in the works).

New projects created with this process, as with any new Supabase project, will incur the usual compute and disk costs. These costs are displayed ahead of time to ensure there are no surprises.

## Accessing Restore to a New Project [\#](https://supabase.com/blog/restore-to-a-new-project\#accessing-restore-to-a-new-project)

The Restore to a New Project feature can be found on the Supabase dashboard under [database backups](https://supabase.com/dashboard/project/_/database/backups/restore-to-new-project).

Please be aware that Restore to a New Project is currently in Public Alpha. You can reach out to [Supabase support](https://supabase.help/) if you experience any issues.

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&text=Restore%20to%20a%20New%20Project)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&text=Restore%20to%20a%20New%20Project)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&t=Restore%20to%20a%20New%20Project)

[Last post\\
\\
**database.build v2: Bring-your-own-LLM** \\
\\
6 December 2024](https://supabase.com/blog/database-build-v2)

[Next post\\
\\
**Hack the Base! with Supabase** \\
\\
6 December 2024](https://supabase.com/blog/hack-the-base)

[cloning](https://supabase.com/blog/tags/cloning) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [How it Works](https://supabase.com/blog/restore-to-a-new-project#how-it-works)
  - [Point-in-Time Recovery](https://supabase.com/blog/restore-to-a-new-project#point-in-time-recovery)
- [Unlimited Cloning from a Source Project](https://supabase.com/blog/restore-to-a-new-project#unlimited-cloning-from-a-source-project)
- [Accessing Restore to a New Project](https://supabase.com/blog/restore-to-a-new-project#accessing-restore-to-a-new-project)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&text=Restore%20to%20a%20New%20Project)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&text=Restore%20to%20a%20New%20Project)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Frestore-to-a-new-project&t=Restore%20to%20a%20New%20Project)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)