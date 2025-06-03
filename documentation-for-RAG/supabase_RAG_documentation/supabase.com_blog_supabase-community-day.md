---
url: "https://supabase.com/blog/supabase-community-day"
title: "Supabase Community Day"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Community Day

26 Jul 2021

•

5 minute read

[![Steve Chavez avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsteve-chavez.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Steve ChavezEngineering & PostgREST maintainer](https://github.com/steve-chavez)

![Supabase Community Day](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-1-community-day%2Flaunch-week-sql-day-1-community-day-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase has grown a lot [1](https://supabase.com/blog/supabase-community-day#user-content-fn-1) since last [Launch Week](https://supabase.com/blog/launch-week),
but it wouldn't be possible without some amazing open source tools.
Since we're shipping a few upgrades this week we feel it's only fair
to shine a spotlight on some tools and community efforts that make Supabase possible.

## PostgreSQL version 13.3 [\#](https://supabase.com/blog/supabase-community-day\#postgresql-version-133)

![Postgres version 13 released](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-1-community-day%2Flaunch-week-sql-day-1-community-day-postgres-upgrade.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

PostgreSQL is a big part of Supabase, and it's also a huge inspiration - the speed that they ship, their community organization,
and their absolute dedication towards reliability. PostgreSQL 13.3 was released in June and (from today) every new Supabase project will
be on [PostgreSQL version 13.3](https://supabase.com/blog/supabase-postgres-13).

### Giving back [\#](https://supabase.com/blog/supabase-community-day\#giving-back)

Supabase makes it easy to get started with Postgres, but we think you should try it even if you don't want to use Supabase. Here's a
few ways we make it easy to use PostgreSQL without Supabase:

- Supabase was the first company to put Postgres in the [Digital Ocean Marketplace](https://marketplace.digitalocean.com/apps/supabase-postgres).
Since then it's been installed over 1000 times (not by us!).
- We provide a Postgres image in the [AWS marketplace](https://aws.amazon.com/marketplace/pp/prodview-lk2pfa5nafecg).
- We're packaging the Marketplace version, [along with "Bundles"](https://supabase.com/blog/supabase-postgres-13#postgresql-bundles)
- We're developing a few extensions: [supautils](https://github.com/supabase/supautils), [pg\_net](https://github.com/supabase/pg_net), and a couple more soon to be announced.

### Get involved [\#](https://supabase.com/blog/supabase-community-day\#get-involved)

- Follow the official [PostgreSQL Twitter](https://twitter.com/PostgreSQL) account.
- Join the official [mailing lists](https://www.postgresql.org/community/).

## PostgREST version 8.0 [\#](https://supabase.com/blog/supabase-community-day\#postgrest-version-80)

![PostgREST version 8.0 released](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-1-community-day%2Flaunch-week-sql-day-1-community-day-postgrest.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This new PostgREST stable version comes with the improvements we've made to make it truly enterprise-grade. Due to our commitment with OSS,
all of our improvements are upstreamed, so you can fully use them on your own self-hosted projects.

### Highlights [\#](https://supabase.com/blog/supabase-community-day\#highlights)

**Improved Performance**: Due to Supabase's high throughput requirements, PostgREST 8.0 handles up to 50% more throughput on
GET requests, according to our benchmarks. We converted all SELECT queries to use prepared statements and reduced logging
verbosity to make this possible.

**Reduced downtime**: we need PostgREST to be more "set it and forget it", so reloading schema cache now has zero downtime.

**Dynamic Configuration**: we've made it easier to handle PostgREST configuration at scale (we manage thousands of PostgREST instances).
This new version includes the ability to use an in-database configuration that is reloadable through a `NOTIFY` command.

**Less admin burden**: PostgREST previously required the `pg_listen` utility to reload its schema cache. This is no longer needed.
The schema cache is reloadable with a simple `NOTIFY` command.

**Better diagnostic information**: in the rare cases where PostgREST fails, we want to find the exact root cause quickly.
For this we've improved its logging by adding logging levels and timestamps to all server errors.

**Simpler OpenAPI**: showing a complete OpenAPI output used to require a highly-privileged `anon` role. With the new `openapi-mode`,
this is no longer needed and `anon` can be kept with minimal privileges.

The community has made many more enhancements and bug fixes for the new version. See
[v8.0 CHANGELOG](https://github.com/PostgREST/postgrest/releases/tag/v8.0.0) for the full list.

### Get Started [\#](https://supabase.com/blog/supabase-community-day\#get-started)

Want to get started with PostgREST? The Supabase community has built a number of client libraries to make it simpler to use:

- Javascript: [postgrest-js](https://github.com/supabase/postgrest-js)
- Rust: [postgrest-rs](https://github.com/supabase/postgrest-rs)
- Go: [postgrest-go](https://github.com/supabase/postgrest-go)
- Python: [postgrest-py](https://github.com/supabase/postgrest-py)
- Dart: [postgrest-dart](https://github.com/supabase/postgrest-dart)
- C#: [postgrest-csharp](https://github.com/supabase/postgrest-csharp)
- Swift: [postgrest-swift](https://github.com/supabase/postgrest-swift)
- Ruby: [postgrest-rb](https://github.com/supabase/postgrest-rb)
- Kotlin: [postgrest-kt](https://github.com/supabase/postgrest-kt)

### Get involved [\#](https://supabase.com/blog/supabase-community-day\#get-involved-1)

- Help with [PostgREST development](https://github.com/PostgREST/postgrest/blob/main/.github/CONTRIBUTING.md).
- Help with [PostgREST docs translations](https://github.com/PostgREST/postgrest-docs/issues/393).
- Follow the official [PostgREST Twitter](https://twitter.com/postgrest_org) account.

## Supabase Flutter/Dart (Beta release) [\#](https://supabase.com/blog/supabase-community-day\#supabase-flutterdart-beta-release)

![Supabase Flutter Beta release](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-1-community-day%2Flaunch-week-sql-day-1-community-day-flutter-library.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

While the Supabase team have been busy with the Javascript libraries, the community have been beavering away with Dart. They've even
[built fully-functional apps](https://www.producthunt.com/posts/spot-2d300f54-7a0a-4dbf-aee2-4a75311217cc) using Supabase Auth and Storage.

Today the Community are releasing both the Flutter and Dart libraries in Beta (with a bit of help from the Supabase team).

### Get started [\#](https://supabase.com/blog/supabase-community-day\#get-started-1)

- Check out the [Flutter Quickstart Guide](https://supabase.com/docs/guides/with-flutter)
- Check out the code:
  - Supabase Flutter: [GitHub](https://github.com/supabase/supabase-flutter/tree/main/packages/supabase_flutter) \| [Release](https://pub.dev/packages/supabase_flutter)
  - Supabase Dart: [GitHub](https://github.com/supabase/supabase-flutter/tree/main/packages/supabase) \| [Release](https://pub.dev/packages/supabase)

### Get involved [\#](https://supabase.com/blog/supabase-community-day\#get-involved-2)

- Help [write](https://supabase.com/supasquad#author) the Flutter Docs.
- Help [maintain](https://supabase.com/supasquad#maintainer) the [Flutter](https://github.com/supabase/supabase-flutter/tree/main/packages/supabase_flutter)
and [Dart](https://github.com/supabase/supabase-flutter/tree/main/packages/supabase) libraries.

## Supabase Discord [\#](https://supabase.com/blog/supabase-community-day\#supabase-discord)

![Supabase Discord](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-sql-day-1-community-day%2Flaunch-week-sql-day-1-community-day-discord-server.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

OK, OK, we get it - GitHub [Discussions](https://github.com/supabase/supabase/discussions) aren't enough for y'all. While we've been trying
to keep the conversation contained to our GitHub org, the community has been creating [subreddits](https://www.reddit.com/r/Supabase/),
StackOverflow [tags](https://stackoverflow.com/questions/tagged/supabase), and GitHub [topics](https://github.com/topics/supabase).

A few weeks ago one of the community created a Community-led Discord, and so the team figured we might as well join the fun.

We'll still be using Discussions for debugging, but if you're looking for a place to hang out with Supabase developers, Discord is where to find it.

### Get involved [\#](https://supabase.com/blog/supabase-community-day\#get-involved-3)

Join the Supabase Community Discord: [discord.supabase.com](http://discord.supabase.com/), say hi, and start building.

## Footnotes [\#](https://supabase.com/blog/supabase-community-day\#footnote-label)

1. Supabase has been one of the fastest growing startups [on GitHub](https://github.com/supabase/supabase) for four consecutive quarters:
207% in [Q3](https://runacap.com/ross-index/q3-2020/) 2020; 1,373% in [Q4](https://runacap.com/ross-index/q4-2020/) 2020;
462% in [Q1](https://runacap.com/ross-index/q1-2021/) 2021; 1,653% in [Q2](https://runacap.com/ross-index/q2-2021/) 2021\. [↩](https://supabase.com/blog/supabase-community-day#user-content-fnref-1)


Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-community-day&text=Supabase%20Community%20Day)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-community-day&text=Supabase%20Community%20Day)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-community-day&t=Supabase%20Community%20Day)

[Last post\\
\\
**Epsilon3 Self-Host Supabase To Revolutionize Space Operations** \\
\\
26 July 2021](https://supabase.com/blog/epsilon3-self-hosting)

[Next post\\
\\
**Supabase is now on Postgres 13.3** \\
\\
26 July 2021](https://supabase.com/blog/supabase-postgres-13)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [PostgreSQL version 13.3](https://supabase.com/blog/supabase-community-day#postgresql-version-133)
- [PostgREST version 8.0](https://supabase.com/blog/supabase-community-day#postgrest-version-80)
- [Supabase Flutter/Dart (Beta release)](https://supabase.com/blog/supabase-community-day#supabase-flutterdart-beta-release)
- [Supabase Discord](https://supabase.com/blog/supabase-community-day#supabase-discord)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-community-day&text=Supabase%20Community%20Day)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-community-day&text=Supabase%20Community%20Day)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-community-day&t=Supabase%20Community%20Day)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)