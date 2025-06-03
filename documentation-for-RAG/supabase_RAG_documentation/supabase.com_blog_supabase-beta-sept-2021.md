---
url: "https://supabase.com/blog/supabase-beta-sept-2021"
title: "Supabase Beta Sept 2021"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta Sept 2021

04 Oct 2021

•

3 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Supabase Beta Sept 2021](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Frelease-sept-2021-cover.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Did you know it's been 2 years since the [first commit](https://github.com/supabase/realtime/commit/175f649784147af80acfc9ff5be9d160285c76ea) to Realtime, our real-time engine for Postgres? Before we even existed as a company!
We spent this month updating docs and content, improving UX, and [onboarding Developer Advocates](https://twitter.com/thorwebdev/status/1441041268411277322)!

## Hackathon v2 [\#](https://supabase.com/blog/supabase-beta-sept-2021\#hackathon-v2)

To kick off [Hacktoberfest](https://hacktoberfest.digitalocean.com/), another Supabase Hackathon is happening [right now](https://supabase.com/blog/2021/09/28/supabase-hacktoberfest-hackathon-2021). You've got another 7 days to be in to win a limited edition t-shirt.

![Hackathon](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Fhacktober.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Abort Requests [\#](https://supabase.com/blog/supabase-beta-sept-2021\#abort-requests)

We added support for [AbortController](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) in our Javascript library so that you can abort long-running queries. \[ [Docs](https://supabase.com/docs/reference/javascript/select#aborting-requests-in-flight)\]

![Abort Requests](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2FSupabase_abort_requests.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Improved table management [\#](https://supabase.com/blog/supabase-beta-sept-2021\#improved-table-management)

We've made a number of changes to the Dashboard to expose some great features of PostgreSQL including:

### Column types [\#](https://supabase.com/blog/supabase-beta-sept-2021\#column-types)

We've improved the column Type field so that it supports your [custom types](https://www.postgresql.org/docs/current/sql-createtype.html).

![Column types](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Fcolumns.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Is Unique [\#](https://supabase.com/blog/supabase-beta-sept-2021\#is-unique)

We've made it simple to add a unique constraint when creating or editing a table.

![Is Unique](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Fis-unique.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Edit columns [\#](https://supabase.com/blog/supabase-beta-sept-2021\#edit-columns)

By popular request, you can now view all columns in a table at a glance and edit them in bulk.

![Edit columns](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Fedit-columns.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Cross-schema relationships [\#](https://supabase.com/blog/supabase-beta-sept-2021\#cross-schema-relationships)

We updated our [grid](https://github.com/supabase/grid) to support relationships across multiple schemas.

![Cross-schema relationships](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Frelationships.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Improved Auth Docs [\#](https://supabase.com/blog/supabase-beta-sept-2021\#improved-auth-docs)

We've revamped the Auth docs - The docs are now broken down into [Authentication](https://supabase.com/docs/guides/auth/social-login/auth-apple) and [Authorization](https://supabase.com/docs/guides/auth/row-level-security), and organized alongside our [Deep Dive](https://supabase.com/docs/learn/auth-deep-dive/auth-deep-dive-jwts) series.

![Auth Docs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Fauth-docs.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Low Code demo [\#](https://supabase.com/blog/supabase-beta-sept-2021\#low-code-demo)

Low Code demo, Using Supabase with [Clutch.io](http://clutch.io/) \- [@\_dijonmusters](https://twitter.com/_dijonmusters) ran a [session at General Assembly](https://www.youtube.com/watch?t=642&v=5fsKMTeBKKY) showing how to use these two tools together to create apps using a low code approach.

Is the Future of Coding Code-Less - presented by General Assembly - YouTube

Supabase

54.4K subscribers

[Is the Future of Coding Code-Less - presented by General Assembly](https://www.youtube.com/watch?v=5fsKMTeBKKY)

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

[Watch on YouTube](https://www.youtube.com/watch?v=5fsKMTeBKKY "Watch on YouTube")

## Community [\#](https://supabase.com/blog/supabase-beta-sept-2021\#community)

There was a lot of new content this month.

### Videos [\#](https://supabase.com/blog/supabase-beta-sept-2021\#videos)

- How I built the #10 product in 30 days - [Gary Tokman \[video\]](https://www.youtube.com/watch?v=CS1myTKJBR4)
- GitHub OAuth flow with Supabase + React - [Nader Dabit \[video\]](https://www.youtube.com/watch?v=jSqTzZk9UMg)
- The Best Stack for Web Developers - [Christopher Kapic \[video\]](https://www.youtube.com/watch?v=-2s_87QkPEI)
- Flutter + Supabase Course - [Abhishvek \[video\]](https://www.youtube.com/watch?v=PjVG6QtUYw4)
- React Native Mobile Auth - [Aaron Saunders \[video\]](https://www.youtube.com/watch?v=aBuB-Q6vHDE)
- Self Hosting Supabase - [Kelvin Pompey \[video\]](https://www.youtube.com/watch?v=HCqta43JHkU)
- Teta Flutter Frontend builder - [Teta Team \[product\]](https://www.youtube.com/watch?v=rooTglpUuvE)
- Magic Link + Route Controls in Next.js - [Nader Dabit \[Video\]](https://www.youtube.com/watch?v=oXWImFqsQF4)
- Supabase in 6 minutes - [Nader Dabit \[video\]](https://www.youtube.com/watch?v=ogEitL8RwtQ)

### Twitter [\#](https://supabase.com/blog/supabase-beta-sept-2021\#twitter)

We hit 16.5k followers. [Follow us](https://twitter.com/supabase/status/1441428275176247302) there for advance frontend tips and 👁️⚡👁️

![Twitter](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Ftwitter.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### GitHub [\#](https://supabase.com/blog/supabase-beta-sept-2021\#github)

Not far from 20K stars: [github.com/supabase/supabase](http://github.com/supabase/supabase)

![GitHub](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Fstars.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Source: [repository.surf/supabase](https://repository.surf/supabase)

### Discord [\#](https://supabase.com/blog/supabase-beta-sept-2021\#discord)

Our Discord is growing fast. Come hangout with 3500+ developers building on Supabase today: [discord.supabase.com](http://discord.supabase.com/)

![Discord](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Fdiscord.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Hiring [\#](https://supabase.com/blog/supabase-beta-sept-2021\#hiring)

We're Hiring [SREs](https://about.supabase.com/careers/sre). We're fully remote and we love Open Source. [See open roles](https://about.supabase.com/careers).

![hiring](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-sept%2Fhiring.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Coming Next [\#](https://supabase.com/blog/supabase-beta-sept-2021\#coming-next)

We're warming up for another Launch Week! Last time was " [Launch Week II: the SQL](https://supabase.com/blog/supabase-launch-week-sql)". We're going to need another month to come up with a good pun again, so we'll aim for November.

## Get started [\#](https://supabase.com/blog/supabase-beta-sept-2021\#get-started)

- Start using Supabase today: **[supabase.com/dashboard](https://supabase.com/dashboard/)**
- Make sure to **[star us on GitHub](https://github.com/supabase/supabase)**
- Follow us **[on Twitter](https://twitter.com/supabase)**
- Subscribe to our **[YouTube channel](https://www.youtube.com/c/supabase)**
- Become a **[sponsor](https://github.com/sponsors/supabase)**

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-sept-2021&text=Supabase%20Beta%20Sept%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-sept-2021&text=Supabase%20Beta%20Sept%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-sept-2021&t=Supabase%20Beta%20Sept%202021)

[Last post\\
\\
**Hacktoberfest Hackathon Winners 2021** \\
\\
14 October 2021](https://supabase.com/blog/hacktoberfest-hackathon-winners-2021)

[Next post\\
\\
**Supabase Hacktoberfest Hackathon 2021** \\
\\
28 September 2021](https://supabase.com/blog/supabase-hacktoberfest-hackathon-2021)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Hackathon v2](https://supabase.com/blog/supabase-beta-sept-2021#hackathon-v2)
- [Abort Requests](https://supabase.com/blog/supabase-beta-sept-2021#abort-requests)
- [Improved table management](https://supabase.com/blog/supabase-beta-sept-2021#improved-table-management)
  - [Column types](https://supabase.com/blog/supabase-beta-sept-2021#column-types)
  - [Is Unique](https://supabase.com/blog/supabase-beta-sept-2021#is-unique)
  - [Edit columns](https://supabase.com/blog/supabase-beta-sept-2021#edit-columns)
- [Cross-schema relationships](https://supabase.com/blog/supabase-beta-sept-2021#cross-schema-relationships)
- [Improved Auth Docs](https://supabase.com/blog/supabase-beta-sept-2021#improved-auth-docs)
- [Low Code demo](https://supabase.com/blog/supabase-beta-sept-2021#low-code-demo)
- [Community](https://supabase.com/blog/supabase-beta-sept-2021#community)
  - [Videos](https://supabase.com/blog/supabase-beta-sept-2021#videos)
  - [Twitter](https://supabase.com/blog/supabase-beta-sept-2021#twitter)
  - [GitHub](https://supabase.com/blog/supabase-beta-sept-2021#github)
  - [Discord](https://supabase.com/blog/supabase-beta-sept-2021#discord)
- [Hiring](https://supabase.com/blog/supabase-beta-sept-2021#hiring)
- [Coming Next](https://supabase.com/blog/supabase-beta-sept-2021#coming-next)
- [Get started](https://supabase.com/blog/supabase-beta-sept-2021#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-sept-2021&text=Supabase%20Beta%20Sept%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-sept-2021&text=Supabase%20Beta%20Sept%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-sept-2021&t=Supabase%20Beta%20Sept%202021)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)