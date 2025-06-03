---
url: "https://supabase.com/blog/supabase-ai-assistant-v2"
title: "Supabase AI Assistant v2"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase AI Assistant v2

02 Dec 2024

•

4 minute read

[![Saxon Fletcher avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaxonf.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Saxon FletcherProduct Design](https://github.com/saxonf)

[![Joshen Lim avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjoshenlim.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Joshen LimEngineering](https://github.com/joshenlim)

![Supabase AI Assistant v2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fthumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we are releasing Supabase Assistant v2 in the Dashboard - a global assistant with several new abilities:

1. Postgres schema design
2. Data queries and charting
3. Error debugging
4. Postgres RLS Policies: create and edit
5. Postgres Functions: create and edit
6. Postgres Triggers: create and edit
7. SQL to `supabase-js` conversion

We improved Supabase AI ... A lot! - YouTube

Supabase

54.4K subscribers

[We improved Supabase AI ... A lot!](https://www.youtube.com/watch?v=_fdP-aaTHgw)

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

[Watch on YouTube](https://www.youtube.com/watch?v=_fdP-aaTHgw "Watch on YouTube")

## A new, unified approach to AI [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#a-new-unified-approach-to-ai)

Our new Assistant is more extensible, using a flexible system of components, tools, and APIs. You can provide context manually (e.g. an RLS Policy) or automatically based on whichever page you're visiting in the Dashboard (e.g. the specific table you're working on).

The result is a single panel that's persistent across the entire Dashboard. It sits alongside your workspace and can be called upon when needed ( `cmd+i`!). It automatically retrieves context for your prompt and can be provided with extra context similar to other AI tools like Cursor and GitHub Copilot.

## New abilities in Supabase Assistant v2 [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#new-abilities-in-supabase-assistant-v2)

Let's take a look at new abilities in this release.

### Schema design [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#schema-design)

If you are creating something new, the Assistant can guide or inspire you. It will show you how to structure your database and generate all the SQL queries to set it up.

![Design new database schemas](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fdesign.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Writing SQL [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#writing-sql)

Like our previous Assistant, the new Assistant will help you write queries based on your schema. This version has better contextual understanding and can provide more accurate suggestions.

### Debug your queries [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#debug-your-queries)

Writing SQL can be tough. You can use the new Assistant to debug database errors directly through the SQL Editor or within the Assistant panel.

![Debug your queries with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fdebug.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Discover data insights [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#discover-data-insights)

The new Assistant can run queries directly. This can be a useful (and fun) way to query your data through natural language. Basic select queries run automatically, and results are displayed within the conversation in tabular form or chart form. The chart axis are picked intuitively by the Assistant. No data is sent to the underlying LLM, only your schema structure. This is a helpful tool for folks who are not comfortable with SQL but are still interested in analyzing data insights.

![Query data with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fquery.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### SQL to REST [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#sql-to-rest)

Once your database is set up, you probably want to connect to it directly or with one of our client libraries. If you're using our `supabase-js` library, we've added a helpful tool to convert an SQL query to supabase-js client code. Simply ask the Assistant to convert a query, and it will respond with either a complete snippet for you to copy or a combination of function + RPC call. This is powered by the [sql-to-rest](https://supabase.com/docs/guides/api/sql-to-rest) tool.

![Convert SQL to supabase-js code](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fjs.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### RLS Policies: Protect your database [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#rls-policies-protect-your-database)

Use the Assistant to suggest, create or modify RLS Policies. Simply explain the desired behavior and the Assistant will generate a new Policy using the context of your database schema and existing policies. To edit an existing policy, click “edit with Assistant” within your Policy list. The Assistant will be provided the appropriate context for you to start prompting.

![Create and edit RLS Policies with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fpolicy.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Postgres Functions and Triggers [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#postgres-functions-and-triggers)

Suggest, create or update functions and triggers in a similar way to policies. Just describe what you want or select “Edit with Assistant” from your Function or Trigger list.

![Create and edit functions and triggers with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Ffunctions.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Feedback [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#feedback)

This release gives us a foundation to build off and incorporate into other parts of your database journey. Where are you struggling the most when using Postgres? How might the Assistant help you? Send us your thoughts, ideas, concerns via the feedback form in the Dashboard.

## How to access [\#](https://supabase.com/blog/supabase-ai-assistant-v2\#how-to-access)

Supabase Assistant v2 is available today.
Go to a Project and hit `cmd + i`, or alternatively click the Assistant icon in the top right toolbar.

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&text=Supabase%20AI%20Assistant%20v2)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&text=Supabase%20AI%20Assistant%20v2)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&t=Supabase%20AI%20Assistant%20v2)

[Last post\\
\\
**Supabase Edge Functions: Introducing Background Tasks, Ephemeral Storage, and WebSockets** \\
\\
3 December 2024](https://supabase.com/blog/edge-functions-background-tasks-websockets)

[Next post\\
\\
**OrioleDB Public Alpha** \\
\\
1 December 2024](https://supabase.com/blog/orioledb-launch)

[AI](https://supabase.com/blog/tags/AI) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [A new, unified approach to AI](https://supabase.com/blog/supabase-ai-assistant-v2#a-new-unified-approach-to-ai)
- [New abilities in Supabase Assistant v2](https://supabase.com/blog/supabase-ai-assistant-v2#new-abilities-in-supabase-assistant-v2)
  - [Schema design](https://supabase.com/blog/supabase-ai-assistant-v2#schema-design)
  - [Writing SQL](https://supabase.com/blog/supabase-ai-assistant-v2#writing-sql)
  - [Debug your queries](https://supabase.com/blog/supabase-ai-assistant-v2#debug-your-queries)
  - [Discover data insights](https://supabase.com/blog/supabase-ai-assistant-v2#discover-data-insights)
  - [SQL to REST](https://supabase.com/blog/supabase-ai-assistant-v2#sql-to-rest)
  - [RLS Policies: Protect your database](https://supabase.com/blog/supabase-ai-assistant-v2#rls-policies-protect-your-database)
  - [Postgres Functions and Triggers](https://supabase.com/blog/supabase-ai-assistant-v2#postgres-functions-and-triggers)
- [Feedback](https://supabase.com/blog/supabase-ai-assistant-v2#feedback)
- [How to access](https://supabase.com/blog/supabase-ai-assistant-v2#how-to-access)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&text=Supabase%20AI%20Assistant%20v2)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&text=Supabase%20AI%20Assistant%20v2)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ai-assistant-v2&t=Supabase%20AI%20Assistant%20v2)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Design new database schemas](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fdesign.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Debug your queries with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fdebug.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Query data with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fquery.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Convert SQL to supabase-js code](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fjs.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Create and edit RLS Policies with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fpolicy.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Create and edit functions and triggers with AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Ffunctions.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)