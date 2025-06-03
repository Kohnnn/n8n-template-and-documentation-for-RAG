---
url: "https://supabase.com/blog/ga-week-summary"
title: "Top 10 Launches from Supabase GA Week"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Top 10 Launches from Supabase GA Week

18 Apr 2024

•

5 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Top 10 Launches from Supabase GA Week](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fga-week-summary%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

There's always a lot to cover in Launch Weeks. Here are a few highlights:

### \#10: Bootstrap: the fastest way to launch a project [\#](https://supabase.com/blog/ga-week-summary\#10-bootstrap-the-fastest-way-to-launch-a-project)

Supabase Bootstrap is the fastest way to spin up a new hosted Supabase project from existing starter templates. Just run `supabase bootstrap` with our CLI and we'll help you launch a new application and attach a remote database to get you started.

[Read more.](https://supabase.com/blog/supabase-bootstrap)

### \#9: Branching is now Publicly available [\#](https://supabase.com/blog/ga-week-summary\#9-branching-is-now-publicly-available)

Supabase Branching is now in open beta. You can enable it on any project that's Pro Plan or above. Branching is a seamless integration of Git with your development workflow, extending beyond your local environment to a remote database.

[Read more.](https://supabase.com/blog/branching-publicly-available)

### \#8: Postgres Index Advisor [\#](https://supabase.com/blog/ga-week-summary\#8-postgres-index-advisor)

We shipped a Postgres extension for recommending indexes to improve query performance. It leans heavily on [HypoPG](https://github.com/HypoPG/hypopg), an excellent extension to determine if Postgres will use a given index without spending resources to create them.

[See the HN discussion.](https://github.com/supabase/index_advisor)

### \#7: Official Swift support [\#](https://supabase.com/blog/ga-week-summary\#7-official-swift-support)

The Supabase Swift libraries are now officially supported by Supabase. This makes it simple to interact with Supabase from applications on Apple's platforms, including iOS, macOS, watchOS, tvOS, and visionOS.

[Read more.](https://supabase.com/blog/supabase-swift)

### \#6: Security Advisor + Performance Advisor [\#](https://supabase.com/blog/ga-week-summary\#6-security-advisor--performance-advisor)

We're dropping some handy tools in Supabase Studio this week to help with security and performance: a **Security Advisor** for detecting insecure database configuration, and a **Performance Advisor** for suggesting database optimizations.

[Read more.](https://supabase.com/blog/security-performance-advisor)

### \#5: Native AI support in Edge Functions [\#](https://supabase.com/blog/ga-week-summary\#5-native-ai-support-in-edge-functions)

We're making it super easy to run AI models within Supabase Edge Functions. We have a new API to generate embeddings and upcoming support for Large Language Models like `llama3` and `mistral`.

[Read more.](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions)

### \#4: S3 compatibility in Supabase Storage [\#](https://supabase.com/blog/ga-week-summary\#4-s3-compatibility-in-supabase-storage)

Supabase Storage is now officially an S3-Compatible Storage Provider. With the support of the S3 protocol, you can now connect Supabase Storage to thousands of 3rd-party tools and services, and make it even easier to use Supabase for data engineering.

[Read more.](https://supabase.com/blog/s3-compatible-storage)

### \#3: Anonymous sign-ins [\#](https://supabase.com/blog/ga-week-summary\#3-anonymous-sign-ins)

Anonymous sign-ins can be used to create **temporary users** who haven't signed up for your application yet. This lowers the friction for new users to try out your product since they don't have to provide any signup credentials. One of our [most-requested features](https://github.com/supabase/auth/issues/68) by the community!

[Read more.](https://supabase.com/blog/anonymous-sign-ins)

### \#2: Oriole joins Supabase [\#](https://supabase.com/blog/ga-week-summary\#2-oriole-joins-supabase)

[Oriole](https://github.com/orioledb/orioledb) is a table storage extension for Postgres. It is designed to be a drop-in replacement for Postgres' existing storage engine, and benchmarks show that it's significantly faster. Over time we hope that it can become available for any Postgres installation and we will continue to work with Oriole and the Postgres community to make this happen.

[Read more.](https://supabase.com/blog/supabase-acquires-oriole)

### \#1: General Availability [\#](https://supabase.com/blog/ga-week-summary\#1-general-availability)

Supabase is now GA. During the first year of Supabase we set ourselves a goal: build a managed platform capable of securely running 1 million databases. Today we've proven that metric and we're announcing the General Availability of the platform that will serve the next 99 million.

[Check out the journey so far.](https://supabase.com/ga)

## More updates [\#](https://supabase.com/blog/ga-week-summary\#more-updates)

There's been a few other highlights this week:

### Supabase + Fly updates [\#](https://supabase.com/blog/ga-week-summary\#supabase--fly-updates)

In the previous Launch Week we started working on [Fly Postgres, a managed offering from Supabase](https://supabase.com/blog/postgres-on-fly-by-supabase). We've received a lot of feedback from early testers, and we're working hard to make the service available and as resilient for production workloads.

Today we're opening up access to everyone **for testing**. Testers can also try [Branching](https://supabase.com/docs/guides/platform/branching), an opt-in feature which creates an ephemeral test environment for your git branches. These instances automatically pause when you aren't using them.

##### Testing only

The service is in public alpha. We don't recommend using it for production.

### Meetups in 27 cities [\#](https://supabase.com/blog/ga-week-summary\#meetups-in-27-cities)

We started GA Week with 10 confirmed community meetups. Over the week, more community members volunteered to host meetups in their own cities. With 25 meetups across the world, some with just 3 people and some with over 50, the Supabase community has truly made our team feel thankful. A huges shout out to these organizers:

Rita & Ann (New York), Mansueli & Guilherme (Maringá), Florian (Seoul), Jose & Aile (Miami), Philippe (Berlin), Tyler (Tokyo), Ivan (Tenerife), Thor (Singapore), Jack (London), Fatuma (Nairobi), Emilio (Milan), Jay Raj Mishra (Kathmandu), Bharat (New Delhi), Abdulhakeem Adams (Ilorin, Nigeria), Kyle Rummens (Utah, USA), Laksh (Nagpur, India), Cam Blackwood (Edinburgh, Scotland), Harry (Central Manchester), Guilleume (Dubai), Kristian (Bergen, Norway), Andrei (Zagreb, Croatia), Misel (Serbia), Matthew (Toronto, Canada), Charlie Coppinger (Wellington, NZ), Nicolas Montone (Buenos Aires, Argentina), Ryan Griffin (Melbourne, Australia), Isheanesu (Cape Town, SA), Aileen (Monterrey, Mexico), Martin (Hong Kong), Bilal Aamer (Hyderabad, India), Gabriel Pan Gantes (Barcelona, Spain).

### Upcoming Meetup in SF [\#](https://supabase.com/blog/ga-week-summary\#upcoming-meetup-in-sf)

We're also hosting a bigger meeting in San Fransisco in June, with a few friends like [Fly.io](http://fly.io/), [Ollama](https://ollama.com/), and [Tigris](https://www.tigrisdata.com/). If you want to hang out with Ant & I, sign up for a full day of hacking at the a16z office:

[Register here](https://lu.ma/gvgaqkrt)

### Hackathon [\#](https://supabase.com/blog/ga-week-summary\#hackathon)

The 10-day hackathon is still going! If you want a chance to win a set of Apple AirPods along with extremely limited edition Supabase swag check out [all the details here](https://supabase.com/blog/supabase-oss-hackathon).

Until next Launch Week, keep building cool stuff.

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fga-week-summary&text=Top%2010%20Launches%20from%20Supabase%20GA%20Week)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fga-week-summary&text=Top%2010%20Launches%20from%20Supabase%20GA%20Week)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fga-week-summary&t=Top%2010%20Launches%20from%20Supabase%20GA%20Week)

[Last post\\
\\
**Supabase Storage: now supports the S3 protocol** \\
\\
18 April 2024](https://supabase.com/blog/s3-compatible-storage)

[Next post\\
\\
**Supabase Security Advisor & Performance Advisor** \\
\\
18 April 2024](https://supabase.com/blog/security-performance-advisor)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [#10: Bootstrap: the fastest way to launch a project](https://supabase.com/blog/ga-week-summary#10-bootstrap-the-fastest-way-to-launch-a-project)
- [#9: Branching is now Publicly available](https://supabase.com/blog/ga-week-summary#9-branching-is-now-publicly-available)
- [#8: Postgres Index Advisor](https://supabase.com/blog/ga-week-summary#8-postgres-index-advisor)
- [#7: Official Swift support](https://supabase.com/blog/ga-week-summary#7-official-swift-support)
- [#6: Security Advisor + Performance Advisor](https://supabase.com/blog/ga-week-summary#6-security-advisor--performance-advisor)
- [#5: Native AI support in Edge Functions](https://supabase.com/blog/ga-week-summary#5-native-ai-support-in-edge-functions)
- [#4: S3 compatibility in Supabase Storage](https://supabase.com/blog/ga-week-summary#4-s3-compatibility-in-supabase-storage)
- [#3: Anonymous sign-ins](https://supabase.com/blog/ga-week-summary#3-anonymous-sign-ins)
- [#2: Oriole joins Supabase](https://supabase.com/blog/ga-week-summary#2-oriole-joins-supabase)
- [#1: General Availability](https://supabase.com/blog/ga-week-summary#1-general-availability)

- [More updates](https://supabase.com/blog/ga-week-summary#more-updates)
  - [Supabase + Fly updates](https://supabase.com/blog/ga-week-summary#supabase--fly-updates)
  - [Meetups in 27 cities](https://supabase.com/blog/ga-week-summary#meetups-in-27-cities)
  - [Upcoming Meetup in SF](https://supabase.com/blog/ga-week-summary#upcoming-meetup-in-sf)
  - [Hackathon](https://supabase.com/blog/ga-week-summary#hackathon)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fga-week-summary&text=Top%2010%20Launches%20from%20Supabase%20GA%20Week)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fga-week-summary&text=Top%2010%20Launches%20from%20Supabase%20GA%20Week)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fga-week-summary&t=Top%2010%20Launches%20from%20Supabase%20GA%20Week)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)