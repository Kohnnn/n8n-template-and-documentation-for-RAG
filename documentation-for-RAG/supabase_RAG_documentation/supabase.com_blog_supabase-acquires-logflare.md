---
url: "https://supabase.com/blog/supabase-acquires-logflare"
title: "Supabase acquires Logflare"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase acquires Logflare

02 Dec 2021

•

6 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Supabase acquires Logflare](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fsupabase-acquires-logflare%2Fsupabase-acquires-logflare-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Back in May 2020, we [tweeted about](https://twitter.com/supabase/status/1265922290237071361?lang=bg) one of the most impressive products we had ever used: Logflare, a log ingestion platform.

> Really impressed with
> [@logflare\_logs](https://twitter.com/logflare_logs?ref_src=twsrc%5Etfw). We've been
> on the front page of
>
>  [#hackernews](https://twitter.com/hashtag/hackernews?src=hash&ref_src=twsrc%5Etfw)
>
> for 24 hours anticipating the HN hug of death. Looks like we made it through OK and Logflare has
> been ingesting everything without breaking a sweat [https://t.co/RWKHIgmWh6](https://t.co/RWKHIgmWh6) [pic.twitter.com/dQ2xqFTdco](https://t.co/dQ2xqFTdco)
>
> — Supabase (@supabase) [May 28, 2020](https://twitter.com/supabase/status/1265922290237071361?ref_src=twsrc%5Etfw)

Today, we're ecstatic to announce that Logflare is joining Supabase.

## Why logging? [\#](https://supabase.com/blog/supabase-acquires-logflare\#why-logging)

A log platform might seem like a strange acquisition for Supabase - after all, there are no "Firebase Logs".

Logging is one of the most unappreciated parts of a tech stack, often an after-thought. But when leveraged correctly, logs give developers superpowers.

### Debugging [\#](https://supabase.com/blog/supabase-acquires-logflare\#debugging)

Logs are an integral part of the developer workflow. When you're programming in Javascript, or Rust, or Go, how often do you rely on the console output to inspect and fix errors? Database debuggers have a lot to learn from programmer tooling.

We want to provide the best database developer experience in the world, and so we're making debugging a first-class citizen.

### Observability [\#](https://supabase.com/blog/supabase-acquires-logflare\#observability)

Databases can be a black box when it comes to spotting errors, finding slow queries, and testing performance optimizations.

The full Supabase stack is more than just a database. It includes various tools working together - APIs, Storage, Auth, and CDNs. A broad tech stack needs a unified measurement system to give a birds-eye view of everything happening within your Supabase project.

This is especially true for our enterprise customers, who need to know that their servers are not just operating, but optimized with alerting the instant anything goes wrong.

### Analytics [\#](https://supabase.com/blog/supabase-acquires-logflare\#analytics)

While it's not immediately apparent, logs are analytics! Especially when a developer can correlate log entries, and enrich them with database data.

Imagine tracing one of your user's network requests from the browser to a database query. Perhaps you'd like to know which of your users are making the most API requests, or downloading the most files, or spending the most time connected to the application?

With granular logs, this becomes possible and paves the way for an incredible developer experience: managing your API versioning, predicting growth, and managing billing costs.

## Why Logflare? [\#](https://supabase.com/blog/supabase-acquires-logflare\#why-logflare)

Since that first tweet in May 2020, our platform has generated billions of log entries. During that time, Logflare has been a staple product in our day-to-day operations. There are a few reasons why Logflare is such a great match for Supabase.

- Chase! The founder of Logflare, [Chase](https://twitter.com/chasers), is an accomplished founder, incredibly product-focused, and an all-around mensch. With over 10 years of experience in data aggregation, Chase is the type of talented person that every team dreams of working with.
- Elixir. Logflare is built with Elixir, the same as our Realtime Engine. We love Elixir at Supabase, and it's nice to have it power another key part of the Supabase stack.
- Real-time. Logflare isn't just for querying logs, it displays what's happening in realtime, allowing you to debug your systems live.
- Branding. Who doesn't love the vivid green with dark mode? 😎

![supabase-realtime-processing-per-subscription](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Fsupabase-acquires-logflare%2Flogflare-screenshot.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Why is Logflare joining Supabase? [\#](https://supabase.com/blog/supabase-acquires-logflare\#why-is-logflare-joining-supabase)

> I really like how Supabase is taking an existing, proven, piece of technology and making it more
> accessible for more users. A lot of people already use Postgres, but they don't take advantage
> of powerful features built into the database. Supabase is exposing these features more
> prominently, making them more accessible to more developers with technology, and educating
> people on how to leverage these features for a better experience for end users.
>
> With Logflare, we've been trying to do this exact thing for analytics oriented databases. We've
> started with BigQuery. Logflare makes it easier to stream inserts with by automatically adapting
> the underlying schema for you. We make it easier to inspect and query your stream. And with
> Logflare Endpoints we're starting to make it easier to operationalize analytics by allowing
> people to build APIs from SQL statements. With Endpoints developers can enhance user facing
> applications without setting up traditionally tedious and brittle data pipelines. We've started
> with BigQuery but will soon be supporting other backends optimized for various analytics use
> cases.
>
> ![Chase Granberry, Founder of Logflare. avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fchase-granberry.png&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Chase Granberry, Founder of Logflare.

## Supabase + Logs [\#](https://supabase.com/blog/supabase-acquires-logflare\#supabase--logs)

We still have a lot of technical work to integrate Logflare into Supabase, with plans of fully supporting the existing Vercel and Cloudflare integrations.

In just the past 10 days, we've been working on a few of the new Dashboard features, which you'll be able to see very soon.

Over the next few weeks, we plan to release these features (once we have a chance to polish them up), and you'll be able to query your logs with your favorite language - SQL 😀.

Supabase Sneak Peek: Query your logs with SQL - YouTube

Supabase

54.4K subscribers

[Supabase Sneak Peek: Query your logs with SQL](https://www.youtube.com/watch?v=MdKWR_Zpu50)

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

[Watch on](https://www.youtube.com/watch?v=MdKWR_Zpu50&embeds_referring_euri=https%3A%2F%2Fsupabase.com%2F)

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=MdKWR_Zpu50 "Watch on YouTube")

## Open source [\#](https://supabase.com/blog/supabase-acquires-logflare\#open-source)

Right now, Logflare works natively with Big Query. But as our track record has proven, we're 100% committed to open source. We're working on the future of a fully open-source version of Logflare, with support for various storage engines.

## Next steps [\#](https://supabase.com/blog/supabase-acquires-logflare\#next-steps)

If you're an existing Logflare user, we'll be migrating everything to Supabase in the coming months. We'll work closely with you to ensure that the transition is seamless, and introduce the same [pricing levels](https://logflare.app/pricing) that Logflare offers today.

We've worked with Chase on a list of potential questions you might have about the transition. If you have any concerns or questions, you can reach out to [support@supabase.io](mailto:support@supabase.io).

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-acquires-logflare&text=Supabase%20acquires%20Logflare)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-acquires-logflare&text=Supabase%20acquires%20Logflare)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-acquires-logflare&t=Supabase%20acquires%20Logflare)

[Last post\\
\\
**Kicking off the Holiday Hackdays** \\
\\
3 December 2021](https://supabase.com/blog/supabase-holiday-hackdays-hackathon)

[Next post\\
\\
**Realtime Postgres RLS now available on Supabase** \\
\\
1 December 2021](https://supabase.com/blog/realtime-row-level-security-in-postgresql)

[launch-week](https://supabase.com/blog/tags/launch-week) [logging](https://supabase.com/blog/tags/logging)

On this page

- [Why logging?](https://supabase.com/blog/supabase-acquires-logflare#why-logging)
  - [Debugging](https://supabase.com/blog/supabase-acquires-logflare#debugging)
  - [Observability](https://supabase.com/blog/supabase-acquires-logflare#observability)
  - [Analytics](https://supabase.com/blog/supabase-acquires-logflare#analytics)
- [Why Logflare?](https://supabase.com/blog/supabase-acquires-logflare#why-logflare)
- [Why is Logflare joining Supabase?](https://supabase.com/blog/supabase-acquires-logflare#why-is-logflare-joining-supabase)
- [Supabase + Logs](https://supabase.com/blog/supabase-acquires-logflare#supabase--logs)
- [Open source](https://supabase.com/blog/supabase-acquires-logflare#open-source)
- [Next steps](https://supabase.com/blog/supabase-acquires-logflare#next-steps)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-acquires-logflare&text=Supabase%20acquires%20Logflare)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-acquires-logflare&text=Supabase%20acquires%20Logflare)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-acquires-logflare&t=Supabase%20acquires%20Logflare)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)