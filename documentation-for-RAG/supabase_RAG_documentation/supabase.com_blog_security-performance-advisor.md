---
url: "https://supabase.com/blog/security-performance-advisor"
title: "Supabase Security Advisor & Performance Advisor"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Security Advisor & Performance Advisor

18 Apr 2024

•

6 minute read

[![Terry Sutton avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaltcod.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Terry SuttonEngineering](https://github.com/saltcod)

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![Supabase Security Advisor & Performance Advisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fsecurity-peformance-advisor%2Fthumb.png%3Fv%3D3&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We're dropping some handy tools in Supabase Studio this week to help with security and performance:

1. **Security Advisor:** for detecting insecure database configuration
2. **Performance Advisor**: for suggesting database optimizations
3. **Index Advisor**: for suggesting indexes on slow-running queries

We [announced General Availability](https://supabase.com/ga) this week, reaching a point where we feel confident our organization can support all types of customers and help them become successful, regardless of their demands. It's a big milestone after four years of building.

As we've grown up as a company, so too have our customers. Many of you have been with us since the start and have seen your projects grow from 0 to literally millions of users, scaling from the Free Plan up to the largest size servers we offer.

8 things you should NEVER do in a Database! - YouTube

Supabase

54.4K subscribers

[8 things you should NEVER do in a Database!](https://www.youtube.com/watch?v=NZEbVe47DfA)

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

[Watch on](https://www.youtube.com/watch?v=NZEbVe47DfA&embeds_referring_euri=https%3A%2F%2Fsupabase.com%2F)

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=NZEbVe47DfA "Watch on YouTube")

## Helping you help yourself [\#](https://supabase.com/blog/security-performance-advisor\#helping-you-help-yourself)

Along with this growth, we've learned many lessons about the types of issues developers encounter using Postgres, especially as they start to get traction. We've built tooling, documentation, and support processes around common issues related to security, performance, resource usage, and slow queries.

As we've helped hundreds of thousands of customers through issues like these, a trend emerged: developers want their problems resolved quickly, but they also want to know what happened and why. This is the typical profile of a Supabase developer - thoughtful, curious, and hungry to learn more about the inner workings of Postgres.

This week, we're adding features into Supabase Studio to address common issues as you scale up. These are powered by tools that we have open sourced this week: [index\_advisor](https://github.com/supabase/index_advisor) and [splinter](https://github.com/supabase/splinter) (“ **S** upabase **P** ostgres **linter**").

## Security Advisor [\#](https://supabase.com/blog/security-performance-advisor\#security-advisor)

![security-peformance-advisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fsecurity-peformance-advisor%2Fsecurity-advisor.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This week we're adding a Security Advisor to Supabase Studio. This is a new interface for exploring security issues with your database because, well, sometimes even Postgres veterans get it wrong. The Security Advisor runs a set queries on your database to identify configuration issues.

The Security Advisor is helpful in pointing out security issues that you might have forgotten or not yet be aware: some lints are general purpose for Postgres projects, while others are specific to Supabase.

As with all of our tooling, it's designed to both help and to teach. The suggestions are well-documented with a rationale, descriptions, examples and remediation steps. Did you know, for example, that views don't respect RLS policies unless you've set `security_invoker=on`? Now you do!

## Performance Advisor [\#](https://supabase.com/blog/security-performance-advisor\#performance-advisor)

![security-peformance-advisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fsecurity-peformance-advisor%2Fperformance-advisor.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

While database tuning is a speciality on its own, many projects have simple optimizations to improve performance. We're releasing a new Performance Advisor in Supabase Studio to surface the low-hanging fruit.

The Performance Advisor checks for misconfigurations, like tables with unindexed foreign key columns, inefficient RLS policies, or columns with duplicate indexes. As a project grows, issues like this can sneak in and slow your projects down (and fill up your disks).

If you're looking for ways to speed up your database, this is the place to start.

## Bonus: Index Advisor [\#](https://supabase.com/blog/security-performance-advisor\#bonus-index-advisor)

![security-peformance-advisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fsecurity-peformance-advisor%2Findex-advisor.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Speaking of performance, we have another treat for you. Last week, we announced [PostgreSQL index advisor](https://news.ycombinator.com/item?id=40028111) on Hacker News. This is a Postgres extension that can determine if a given query should have an index. It's already proving useful:

> Awesome, the Index Advisor sped my slowest query 4x!
>
> ![noob-4-life on Hacker News avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fyc.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> noob-4-life on Hacker News

The Supabase [Index Advisor](https://github.com/supabase/index_advisor) is now available inside Supabase Studio. We've integrated the Index Advisor into our existing Query Performance tool so that you can find your slowest queries and check recommendations. As its name suggests, this analyzes your queries and make recommendations to add or remove table indexes.

What is an index?

Not sure what an index is? Imagine having to look up a person's name in a phonebook where the
entries are not alphabetical. This is what your database tables look like by default. Finding a
number from a randomly sorted list of records would take a long time. When you add an index, the
database stores the sorted values, allowing it to quickly locate a row without having to search
through every record sequentially.

This is just the beginning of our plan to make automated data analysis tooling available to all developers. Even if you're experienced with databases, this will be a huge help with the optimization work you have already planned to do. If you're new to databases, the Index Advisor will help you level-up, surfacing issues and showing you how to fix them.

Let's have a look at some queries:

![security-peformance-advisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fsecurity-peformance-advisor%2Fno-index.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)This query doesn't need an index![security-peformance-advisor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fsecurity-peformance-advisor%2Fneeds-index.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)This query would benefit from an index

## What's next [\#](https://supabase.com/blog/security-performance-advisor\#whats-next)

We plan to expand the set of suggestions available in Studio to cover more areas of potential improvement for security and performance. Some of the ideas we have in mind for the future include:

- checking for liberally-permissioned columns that contain personally identifiable information (PII)
- identifying bloated tables/indexes
- advanced Postgres configuration
- suggestions for tighting up Supabase Auth as you move into production

### Contributions welcome [\#](https://supabase.com/blog/security-performance-advisor\#contributions-welcome)

Community feedback plays a key role in helping us determine where to invest time developing future lints. We encourage contributions by suggesting new lints or enhancements.

If you have ideas for new lints or wish to report problems you can open an issue on our GitHub repository [`splinter`](https://github.com/supabase/splinter) or [`index_advisor`](https://github.com/supabase/index_advisor).

[![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-black.svg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-white.svg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)Week](https://supabase.com/ga-week)

15-19 April

[Day 1 -Supabase is officially launching into General Availability](https://supabase.com/ga)

[Day 2 -Supabase Functions now supports AI models](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions)

[Day 3 -Supabase Auth now supports Anonymous sign-ins](https://supabase.com/blog/anonymous-sign-ins)

[Day 4 -Supabase Storage: now supports the S3 protocol](https://supabase.com/blog/s3-compatible-storage)

[Day 5 -Supabase Security Advisor & Performance Advisor](https://supabase.com/blog/security-performance-advisor)

Build Stage

[01 -PostgreSQL Index Advisor](https://github.com/supabase/index_advisor)

[02 -Branching now Publicly Available](https://supabase.com/blog/branching-publicly-available)

[03 -Oriole joins Supabase](https://supabase.com/blog/supabase-acquires-oriole)

[04 -Supabase on AWS Marketplace](https://supabase.com/blog/supabase-aws-marketplace)

[05 -Supabase Bootstrap](https://supabase.com/blog/supabase-bootstrap)

[06 -Supabase Swift](https://supabase.com/blog/supabase-swift)

[07 -Top 10 Launches from Supabase GA Week](https://supabase.com/blog/ga-week-summary)

[Open Source Hackathon 2024](https://supabase.com/blog/supabase-oss-hackathon)

[Community Meetups](https://supabase.com/ga-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsecurity-performance-advisor&text=Supabase%20Security%20Advisor%20%26%20Performance%20Advisor)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsecurity-performance-advisor&text=Supabase%20Security%20Advisor%20%26%20Performance%20Advisor)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsecurity-performance-advisor&t=Supabase%20Security%20Advisor%20%26%20Performance%20Advisor)

[Last post\\
\\
**Top 10 Launches from Supabase GA Week** \\
\\
18 April 2024](https://supabase.com/blog/ga-week-summary)

[Next post\\
\\
**Supabase Auth now supports Anonymous Sign-ins** \\
\\
17 April 2024](https://supabase.com/blog/anonymous-sign-ins)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Helping you help yourself](https://supabase.com/blog/security-performance-advisor#helping-you-help-yourself)
- [Security Advisor](https://supabase.com/blog/security-performance-advisor#security-advisor)
- [Performance Advisor](https://supabase.com/blog/security-performance-advisor#performance-advisor)
- [Bonus: Index Advisor](https://supabase.com/blog/security-performance-advisor#bonus-index-advisor)
- [What's next](https://supabase.com/blog/security-performance-advisor#whats-next)
  - [Contributions welcome](https://supabase.com/blog/security-performance-advisor#contributions-welcome)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsecurity-performance-advisor&text=Supabase%20Security%20Advisor%20%26%20Performance%20Advisor)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsecurity-performance-advisor&text=Supabase%20Security%20Advisor%20%26%20Performance%20Advisor)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsecurity-performance-advisor&t=Supabase%20Security%20Advisor%20%26%20Performance%20Advisor)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)