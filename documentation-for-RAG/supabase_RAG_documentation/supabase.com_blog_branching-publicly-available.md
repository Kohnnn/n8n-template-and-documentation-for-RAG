---
url: "https://supabase.com/blog/branching-publicly-available"
title: "Branching now Publicly Available"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Branching now Publicly Available

15 Apr 2024

•

3 minute read

[![Alaister Young avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Falaister.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Alaister YoungEngineering](https://github.com/alaister)

[![Qiao Han avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsweatybridge.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Qiao HanEngineering](https://github.com/sweatybridge)

![Branching now Publicly Available](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fbranching-publicly-available%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

tl;dr: Supabase Branching is now in open beta! You can enable it on any project that's Pro Plan or above.

## What is Branching? [\#](https://supabase.com/blog/branching-publicly-available\#what-is-branching)

Branching is a seamless integration of Git with your development workflow, extending beyond your local environment to a remote database. Leveraging Git, particularly focusing on GitHub initially, each time a Pull Request is opened, a corresponding "Preview Environment" is spawned.

![Every Supabase Preview is a dedicated instance, with a full suite of Supabase services.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-branching%2Fisolated-instances--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Every Supabase Preview is a dedicated instance, with a full suite of Supabase services.

Preview Branches are essentially full Supabase instances. Every push triggers migrations from the `./supabase/migrations` folder, ensuring team synchronization and a shared source of truth. When you merge a Pull Request, your migrations are applied to the Production database.

We [announced Branching](https://supabase.com/blog/supabase-branching) a few months ago in our previous Launch Week, with a deep dive on a few of the features like data seeding, integrations with Vercel, and seamless handling of environment variables. Since launching Branching for early-access we've worked with early users of all sizes. Today we're making Branching available to everyone.

## New Features [\#](https://supabase.com/blog/branching-publicly-available\#new-features)

Our open Beta introduces a number of requested features:

### Edge Function support [\#](https://supabase.com/blog/branching-publicly-available\#edge-function-support)

Branching now deploys your Edge Functions along with your migrations. Any Functions added or changed in your `./supabase/functions` will automatically be deployed without any extra configuration.

### Monorepo support [\#](https://supabase.com/blog/branching-publicly-available\#monorepo-support)

You can now set a custom Supabase directory path which allows for monorepo support. You can also choose to only spin up new branches when there are changes inside your Supabase directory. See all the configuration settings in your projects [here](https://supabase.com/dashboard/project/_/settings/integrations).

### Persistent branches [\#](https://supabase.com/blog/branching-publicly-available\#persistent-branches)

![Every Supabase Preview is a dedicated instance, with a full suite of Supabase services.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fbranching-publicly-available%2Fpersistent-branches--dark.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We had quite a few users of branching request for long-running branches so we added the concept of persistent branches. In persistent mode, a branch will remain active even after the underlying PR merges or closes.

Please note that branches should still be treated as replaceable at any time. Persistent or ephemeral Branches should not be used for production data.

## Feedback [\#](https://supabase.com/blog/branching-publicly-available\#feedback)

A special thank you to all our early-access branching users who provided lots of actionable feedback. Our feature development was largely driven by the direct feedback from our users.

We still have many features to add to branching before 1.0, so please continue [sending us your feedback](https://github.com/orgs/supabase/discussions/18937)!

## Getting Started [\#](https://supabase.com/blog/branching-publicly-available\#getting-started)

You can easily get started with Branching by following our [Getting Started Guide](https://supabase.com/docs/guides/platform/branching#how-to-use-supabase-branching).

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbranching-publicly-available&text=Branching%20now%20Publicly%20Available)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbranching-publicly-available&text=Branching%20now%20Publicly%20Available)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbranching-publicly-available&t=Branching%20now%20Publicly%20Available)

[Last post\\
\\
**AI Inference now available in Supabase Edge Functions** \\
\\
16 April 2024](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions)

[Next post\\
\\
**Oriole joins Supabase** \\
\\
15 April 2024](https://supabase.com/blog/supabase-acquires-oriole)

[launch-week](https://supabase.com/blog/tags/launch-week) [database](https://supabase.com/blog/tags/database)

On this page

- [What is Branching?](https://supabase.com/blog/branching-publicly-available#what-is-branching)
- [New Features](https://supabase.com/blog/branching-publicly-available#new-features)
  - [Edge Function support](https://supabase.com/blog/branching-publicly-available#edge-function-support)
  - [Monorepo support](https://supabase.com/blog/branching-publicly-available#monorepo-support)
  - [Persistent branches](https://supabase.com/blog/branching-publicly-available#persistent-branches)
- [Feedback](https://supabase.com/blog/branching-publicly-available#feedback)
- [Getting Started](https://supabase.com/blog/branching-publicly-available#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbranching-publicly-available&text=Branching%20now%20Publicly%20Available)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbranching-publicly-available&text=Branching%20now%20Publicly%20Available)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbranching-publicly-available&t=Branching%20now%20Publicly%20Available)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Every Supabase Preview is a dedicated instance, with a full suite of Supabase services.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-supabase-branching%2Fisolated-instances--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Every Supabase Preview is a dedicated instance, with a full suite of Supabase services.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fbranching-publicly-available%2Fpersistent-branches--dark.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)