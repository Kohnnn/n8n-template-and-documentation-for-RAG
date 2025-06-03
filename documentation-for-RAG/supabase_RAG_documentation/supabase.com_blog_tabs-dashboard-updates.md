---
url: "https://supabase.com/blog/tabs-dashboard-updates"
title: "Keeping Tabs on What's New in Supabase Studio"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Keeping Tabs on What's New in Supabase Studio

02 Apr 2025

•

6 minute read

[![Jordi Enric avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F37541088%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jordi EnricEngineering](https://x.com/jordienr)

[![Jonny Summers-Muir avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmildtomato.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jonny Summers-MuirProduct Design](https://github.com/mildtomato)

[![Joshen Lim avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjoshenlim.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Joshen LimEngineering](https://github.com/joshenlim)

[![Saxon Fletcher avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaxonf.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Saxon FletcherProduct Design](https://github.com/saxonf)

![Keeping Tabs on What's New in Supabase Studio](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Ftabs-dashboard-updates-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've had a busy few months working on Studio improvements and new features—big and small—to help you build, debug, and ship faster.

Here's a quick rundown of what's new:

- [**Tabs!**](https://supabase.com/blog/tabs-dashboard-updates#tabs): The Table Editor and SQL Editor now have tabs!

- [**Customizable Reports**](https://supabase.com/blog/tabs-dashboard-updates#customizable-reports): create reports to show
data exactly how you want to see it

- [**SQL Blocks in Custom reports**](https://supabase.com/blog/tabs-dashboard-updates#sql-blocks-in-custom-reports): use SQL Snippets in blocks inside your custom reports

- [**Inline SQL Editor**](https://supabase.com/blog/tabs-dashboard-updates#inline-sql-editor): use a mini SQL Editor anywhere in the Dashboard

- [**Multiple AI Assistant chats**](https://supabase.com/blog/tabs-dashboard-updates#multiple-ai-assistant-chats): maintain history of your Assistant chats

- [**Logs improvements**](https://supabase.com/blog/tabs-dashboard-updates#logs-improvements): more detailed inspect panel, and stacked charts


### Tabs! [\#](https://supabase.com/blog/tabs-dashboard-updates\#tabs)

This has been a common request for a long time, and should make working with data much easier. We've added Tabs to our two most-used tools: the Table Editor and the SQL Editor.

### Tabs in the Table Editor [\#](https://supabase.com/blog/tabs-dashboard-updates\#tabs-in-the-table-editor)

In the Table Editor, you can open multiple tables at a time and easily switch between them using tabs. This makes it easier to compare data, edit schemas, or reference related tables without losing your place. Enabled under Feature Previews ( [see below](https://supabase.com/blog/tabs-dashboard-updates#enabling-feature-previews))

![Table Editor tabs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Ftable-editor-tabs.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Tabs work the same as in VS Code, opening in preview mode. This is useful if you're quickly browsing files and don't want every visited file to have its own tab. A new tab will only be dedicated to that file when you start editing or simply click into it. Preview mode is indicated by _italics_ in the tab heading.

The New Tab page also gives you quick access to create a new table or open a recently visited one.

![Creating a new tab](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Fnew-tab.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Tabs in the SQL Editor [\#](https://supabase.com/blog/tabs-dashboard-updates\#tabs-in-the-sql-editor)

In the SQL Editor, you can now write and run multiple scripts at a time, without having to constantly change between snippets. The SQL Editor tabs also have preview mode, so you can quickly flip through snippets without leaving a bunch of tabs to clean up after. Enabled under Feature Previews ( [see below](https://supabase.com/blog/tabs-dashboard-updates#enabling-feature-previews))

![SQL Editor tabs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Fsql-editor-tabs.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Multiple tabs will make it easier to work across datasets, debug, or compare different queries, all without losing your place.

## Customizable reports [\#](https://supabase.com/blog/tabs-dashboard-updates\#customizable-reports)

Reports in the Dashboard recently got a refresh. You can now resize and reorder chart blocks, giving you full control over the layout. It's perfect for crafting reports that look exactly how you want.

![Customizable reports](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Fcustomizable-reports.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## SQL blocks in custom reports [\#](https://supabase.com/blog/tabs-dashboard-updates\#sql-blocks-in-custom-reports)

We've also added inline SQL execution within blocks, so you can run your own queries directly and build fully customized, data-driven reports. Just create a snippet in the SQL Editor and it will be available to use here.

![Customizable reports](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Fcustom-reports-sql.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can show your data as a table of results:

![Customizable reports](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Fcustom-reports-sql-query.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Or display them as a chart:

![Customizable reports](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Frefinements-completed.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The sky is the limit for these. You could query a Foreign Data Wrapper, join multiple tables, create a View to highlight key information, and much more.

## Inline SQL Editor [\#](https://supabase.com/blog/tabs-dashboard-updates\#inline-sql-editor)

You can now run SQL from anywhere in the Dashboard via the Inline SQL Editor. You can query and modify tables, add triggers, functions, RLS policies, and anything else you can do from the main SQL Editor, anywhere in the Dashboard. Enabled under Feature Previews ( [see below](https://supabase.com/blog/tabs-dashboard-updates#enabling-feature-previews)).

![Customizable reports](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Finline-sql-editor.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Multiple AI Assistant chats [\#](https://supabase.com/blog/tabs-dashboard-updates\#multiple-ai-assistant-chats)

The AI Assistant now lets you create and store multiple chats. Create, rename, switch to and delete chats, all without losing your place. Chats are scoped to the current project, so switching your project also switches chat history. The chat history is stored in local storage.

![Customizable reports](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Fchat-history.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Logs improvements [\#](https://supabase.com/blog/tabs-dashboard-updates\#logs-improvements)

We've updated the [log detail panel](https://github.com/supabase/supabase/pull/33536) to show more info in the API log detail:

![New Logs detail panel](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Flog-detail-panel.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can also quickly add a property or value from the detail panel to search and filter the results:

![Logs property search](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Flogs-search.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

And we've added http status to available filters to help you narrow in on specific logs while debugging:

![Customizable reports](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Fhttp-filters.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Enabling Feature Previews [\#](https://supabase.com/blog/tabs-dashboard-updates\#enabling-feature-previews)

Tabs and the Inline SQL Editor can be enabled via Feature Preview. Click your user avatar in the bottom right and click Feature previews.

![Click your user avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Favatar.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Enable features via Preview](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-tabs-dashboard-updates%2Ffeature-preview.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Get started [\#](https://supabase.com/blog/tabs-dashboard-updates\#get-started)

You can see all these improvements in the Supabase Dashboard now.

- [Get started with Supabase](https://supabase.com/dashboard/sign-in?returnTo=%2Fprojects) and try it out today

[Launch Week 14](https://supabase.com/launch-week)

Mar 31 - Apr 04 '25

[Day 1 -Supabase UI Library](https://supabase.com/blog/supabase-ui-library)

[Day 2 -Supabase Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)

[Day 3 -Realtime: Broadcast from Database](https://supabase.com/blog/realtime-broadcast-from-database)

[Day 4 -Declarative Schemas for Simpler Database Management](https://supabase.com/blog/declarative-schemas)

[Day 5 -Supabase MCP Server](https://supabase.com/blog/mcp-server)

Build Stage

[01 -Postgres Language Server](https://supabase.com/blog/postgres-language-server)

[02 -Supabase Auth: Bring Your Own Clerk](https://supabase.com/blog/clerk-tpa-pricing)

[03 -Automatic Embeddings in Postgres](https://supabase.com/blog/automatic-embeddings)

[04 -Keeping Tabs: What's New in Supabase Studio](https://supabase.com/blog/tabs-dashboard-updates)

[05 -Dedicated Poolers](https://supabase.com/blog/dedicated-poolers)

[06 -Data API Routes to Nearest Read Replica](https://supabase.com/blog/data-api-nearest-read-replica)

[Community Meetups](https://supabase.com/events?category=meetup)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ftabs-dashboard-updates&text=Keeping%20Tabs%20on%20What%27s%20New%20in%20Supabase%20Studio)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ftabs-dashboard-updates&text=Keeping%20Tabs%20on%20What%27s%20New%20in%20Supabase%20Studio)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Ftabs-dashboard-updates&t=Keeping%20Tabs%20on%20What%27s%20New%20in%20Supabase%20Studio)

[Last post\\
\\
**Realtime: Broadcast from Database** \\
\\
2 April 2025](https://supabase.com/blog/realtime-broadcast-from-database)

[Next post\\
\\
**Edge Functions: Deploy from the Dashboard + Deno 2.1** \\
\\
1 April 2025](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)

[launch-week](https://supabase.com/blog/tags/launch-week) [studio](https://supabase.com/blog/tags/studio)

On this page

- [Tabs!](https://supabase.com/blog/tabs-dashboard-updates#tabs)
- [Tabs in the Table Editor](https://supabase.com/blog/tabs-dashboard-updates#tabs-in-the-table-editor)
- [Tabs in the SQL Editor](https://supabase.com/blog/tabs-dashboard-updates#tabs-in-the-sql-editor)

- [Customizable reports](https://supabase.com/blog/tabs-dashboard-updates#customizable-reports)
- [SQL blocks in custom reports](https://supabase.com/blog/tabs-dashboard-updates#sql-blocks-in-custom-reports)
- [Inline SQL Editor](https://supabase.com/blog/tabs-dashboard-updates#inline-sql-editor)
- [Multiple AI Assistant chats](https://supabase.com/blog/tabs-dashboard-updates#multiple-ai-assistant-chats)
- [Logs improvements](https://supabase.com/blog/tabs-dashboard-updates#logs-improvements)
- [Enabling Feature Previews](https://supabase.com/blog/tabs-dashboard-updates#enabling-feature-previews)
- [Get started](https://supabase.com/blog/tabs-dashboard-updates#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ftabs-dashboard-updates&text=Keeping%20Tabs%20on%20What%27s%20New%20in%20Supabase%20Studio)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ftabs-dashboard-updates&text=Keeping%20Tabs%20on%20What%27s%20New%20in%20Supabase%20Studio)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Ftabs-dashboard-updates&t=Keeping%20Tabs%20on%20What%27s%20New%20in%20Supabase%20Studio)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)