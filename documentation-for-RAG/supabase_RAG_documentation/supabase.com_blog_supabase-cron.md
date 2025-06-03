---
url: "https://supabase.com/blog/supabase-cron"
title: "Supabase Cron"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Cron

04 Dec 2024

•

4 minute read

[![Ivan Vasilov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fivasilov.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ivan VasilovEngineering](https://twitter.com/ivasilov)

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

[![Terry Sutton avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaltcod.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Terry SuttonEngineering](https://github.com/saltcod)

![Supabase Cron](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fthumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we're releasing [Supabase Cron](https://supabase.com/modules/cron), a new Postgres Module that makes recurring Jobs simple and intuitive inside your database.

It's designed to work seamlessly with the entire Supabase platform. Create recurring Jobs to run SQL snippets and call database functions, Supabase Edge Functions, and even remote webhooks.

We made Cron EASY! - YouTube

Supabase

54.4K subscribers

[We made Cron EASY!](https://www.youtube.com/watch?v=miRQPbIJOuQ)

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

[Watch on YouTube](https://www.youtube.com/watch?v=miRQPbIJOuQ "Watch on YouTube")

Supabase Cron is built on the powerful [`pg_cron`](https://github.com/citusdata/pg_cron) extension by the team at [Citus Data](https://github.com/citusdata).

It's a Supabase policy to [support existing tools](https://supabase.com/docs/guides/getting-started/architecture#support-existing-tools) wherever possible, and the Citus Data team have generously licensed their extension with the OSI-compatible [PostgreSQL license](https://github.com/citusdata/pg_cron?tab=PostgreSQL-1-ov-file).

We're very thankful to all the contributors and we look forward to our continued work with the community.

### What's a Cron? [\#](https://supabase.com/blog/supabase-cron\#whats-a-cron)

[**Cron**](https://en.wikipedia.org/wiki/Cron) is a tool for scheduling recurring tasks that run at specified intervals. These periodic tasks are called “Cron Jobs”. Common use-cases include:

- **Maintenance:** delete or archive old data.
- **Reporting and analytics:** save daily or weekly reports for analysis.
- **Automation:** send periodic emails, like newsletters or reminders.
- **Monitoring**: perform health checks on your database and log the results.
- **Performance:** automate vacuuming tables and rebuilding indexes.

Supabase Cron stores the scheduling logic within Postgres and runs your Jobs accordingly while integrating with the rest of the Supabase primitives - Dashboard, Edge Functions, and AI Assistant.

## How Do You Use Supabase Cron? [\#](https://supabase.com/blog/supabase-cron\#how-do-you-use-supabase-cron)

You can create Jobs either via the Dashboard or SQL.

For this post we'll focus on the Dashboard. You can refer to the [documentation](https://supabase.com/docs/guides/cron/quickstart) for SQL.

Within the Dashboard you can define schedules using standard cron syntax and the special `pg_cron` seconds syntax for sub-minute schedules or use natural language.

![Natural language scheduling](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fnatural-language.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Job Types [\#](https://supabase.com/blog/supabase-cron\#job-types)

You can choose between four types of Jobs based on what you need to execute:

![Job types](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fjob-types.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### SQL Snippets [\#](https://supabase.com/blog/supabase-cron\#sql-snippets)

Create an inline SQL query or command to run on your database periodically. Use this for tasks like:

- Generating reports.
- Cleaning up stale data.
- Refreshing [Materialized Views](https://supabase.com/docs/guides/database/tables?queryGroups=database-method&database-method=sql#materialized-views).

### Database Functions [\#](https://supabase.com/blog/supabase-cron\#database-functions)

Call a Postgres function. This is useful for workflows, such as:

- Batch processing operations.
- Running periodic maintenance tasks.
- Performing multi-step updates using transactions.

### HTTP Requests (webhooks) [\#](https://supabase.com/blog/supabase-cron\#http-requests-webhooks)

Trigger an external HTTP endpoint. Use this for:

- Starting external workflows.
- Syncing data with third-party APIs.
- Sending notifications to external systems.

### Supabase Edge Functions [\#](https://supabase.com/blog/supabase-cron\#supabase-edge-functions)

Run a serverless function to execute custom logic. Examples include:

- Creating embeddings.
- Sending automated email updates.
- Fetching external data and storing it in your database.

These options cover a wide range of use cases, helping with everything from database management to external integrations.

### Observe and Debug Jobs [\#](https://supabase.com/blog/supabase-cron\#observe-and-debug-jobs)

Wondering why a Job failed? You can view the history of all Jobs and their logs in the Dashboard. You can see when a Job started, how long it took, and what the result was.

![View Job history](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fhistory-button.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Observe and debug Jobs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fhistory.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

For a deeper dive, you can view Jobs in the [Logs Explorer](https://supabase.com/dashboard/project/_zvmkyvanngopzqaabmvx_/logs/pgcron-logs).

![View cron logs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Flogs.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Try Supabase Cron today [\#](https://supabase.com/blog/supabase-cron\#try-supabase-cron-today)

Getting started is easy:

1. Visit the [Integrations page](https://supabase.com/dashboard/project/_/integrations) in your project.
2. Enable the **Cron** Postgres Module.
3. Create your first scheduled Job.

![Integrations page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fintegrations.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Create a new Job](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fcreate-job.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We're looking forward to seeing how you use Supabase Cron to help automate your workflows!

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cron&text=Supabase%20Cron)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cron&text=Supabase%20Cron)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cron&t=Supabase%20Cron)

[Last post\\
\\
**High Performance Disk** \\
\\
5 December 2024](https://supabase.com/blog/high-performance-disks)

[Next post\\
\\
**Supabase CLI v2: Config as Code** \\
\\
4 December 2024](https://supabase.com/blog/cli-v2-config-as-code)

[cron](https://supabase.com/blog/tags/cron) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [What's a Cron?](https://supabase.com/blog/supabase-cron#whats-a-cron)

- [How Do You Use Supabase Cron?](https://supabase.com/blog/supabase-cron#how-do-you-use-supabase-cron)
- [Job Types](https://supabase.com/blog/supabase-cron#job-types)
  - [SQL Snippets](https://supabase.com/blog/supabase-cron#sql-snippets)
  - [Database Functions](https://supabase.com/blog/supabase-cron#database-functions)
  - [HTTP Requests (webhooks)](https://supabase.com/blog/supabase-cron#http-requests-webhooks)
  - [Supabase Edge Functions](https://supabase.com/blog/supabase-cron#supabase-edge-functions)
  - [Observe and Debug Jobs](https://supabase.com/blog/supabase-cron#observe-and-debug-jobs)
  - [Try Supabase Cron today](https://supabase.com/blog/supabase-cron#try-supabase-cron-today)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cron&text=Supabase%20Cron)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cron&text=Supabase%20Cron)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-cron&t=Supabase%20Cron)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Natural language scheduling](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fnatural-language.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Job types](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fjob-types.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![View Job history](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fhistory-button.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Observe and debug Jobs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fhistory.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![View cron logs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Flogs.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Integrations page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fintegrations.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Create a new Job](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fcreate-job.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)