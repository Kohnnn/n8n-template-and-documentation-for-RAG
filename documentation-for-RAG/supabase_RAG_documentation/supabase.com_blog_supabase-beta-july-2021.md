---
url: "https://supabase.com/blog/supabase-beta-july-2021"
title: "Supabase Beta July 2021"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta July 2021

12 Aug 2021

•

4 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta July 2021](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Frelease-july-2021-cover.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

July ended with our second "Launch Week", where we shipped something every day for a week. There's a lot to get through this time!

### Quick demo [\#](https://supabase.com/blog/supabase-beta-july-2021\#quick-demo)

Watch a full demo of this month's releases.

Build in Public 011: Launch Week Recap - YouTube

Supabase

54.4K subscribers

[Build in Public 011: Launch Week Recap](https://www.youtube.com/watch?v=Vj5fPA-vjfw)

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

[Watch on YouTube](https://www.youtube.com/watch?v=Vj5fPA-vjfw "Watch on YouTube")

## Launch Week II: The SQL [\#](https://supabase.com/blog/supabase-beta-july-2021\#launch-week-ii-the-sql)

Following the success of our first Launch Week in March, we finished July with " [Launch Week II: The SQL](https://supabase.com/blog/supabase-launch-week-sql)".
The community has been sieving through a slew of bad puns and retro memes to discover the new feature announcements.

![Launch Week II: The SQL](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fsupabase-launch-the-sql.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Auth v2 with Phone Auth [\#](https://supabase.com/blog/supabase-beta-july-2021\#auth-v2-with-phone-auth)

Your users can now log in with SMS based mobile auth! We have a Twilio integration ( [Guide Here](https://supabase.com/docs/guides/auth/phone-login/twilio)) and will be adding more providers soon.

Other Auth updating include, Twitch logins, and the ability to generate invite, recovery, confirmation, and magic links via the API,
for people who want more control over the email templating flow. Read the [blog post here](https://supabase.com/blog/supabase-auth-passwordless-sms-login).

![Auth v2 with Phone Auth](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fverify-phone.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Storage is now in Beta [\#](https://supabase.com/blog/supabase-beta-july-2021\#storage-is-now-in-beta)

Storage updates include Media Streaming, Public Buckets, Directory Uploads, and a Performance Improvements.

Streaming Media in particular opens up a whole new host of potential use cases, learn more about the [updates here](https://supabase.com/blog/storage-beta).

![Auth v2 with Phone Auth](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fstorage.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Dashboard v2 [\#](https://supabase.com/blog/supabase-beta-july-2021\#dashboard-v2)

We made some major new additions to the dashboard including usage statistics, a new project home, and tons of database insights.
Check the [post here](https://supabase.com/blog/supabase-reports-and-metrics) on what you get and how we built it.

![Dashboard v2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fdashboards.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## We launched a Discord server [\#](https://supabase.com/blog/supabase-beta-july-2021\#we-launched-a-discord-server)

You'll find us hanging out regularly in the #hangout channel.
We even "live-fixed" some production errors in there on Monday night (which occurred literally 1 hour before our first announcement of the week! Typical!).
We're fast approaching 1,500 members so come and join the action! [discord.supabase.com](https://discord.supabase.com/)

![We launched a Discord server](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fdiscord.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## PostgreSQL 13 [\#](https://supabase.com/blog/supabase-beta-july-2021\#postgresql-13)

All new Supabase projects will be launched with PostgreSQL 13.3, and we're working on a migration path for old projects.
This gives you [looooaads of new stuff out the box](https://supabase.com/blog/supabase-postgres-13).

![PostgreSQL 13](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fpostgres-13.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## PostgREST v8.0 [\#](https://supabase.com/blog/supabase-beta-july-2021\#postgrest-v80)

We worked with our friends at [PostgREST](https://postgrest.org/) to make some [huge improvements](https://supabase.com/blog/supabase-community-day#postgrest-version-80).
For those of you who don't know, every Supabase instance comes with a dedicated PostgREST server by default,
which provides the auto-generated CRUD API that we wrap with `supabase-js`.

![PostgREST v8.0](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fpostgrest-8.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Flutter/Dart support [\#](https://supabase.com/blog/supabase-beta-july-2021\#flutterdart-support)

Our community driven libs for the fast growing mobile and web framework are now in beta. Learn more by following the [Quickstart guide](https://supabase.com/docs/guides/with-flutter).

![Flutter/Dart support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fdart.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Hackathon [\#](https://supabase.com/blog/supabase-beta-july-2021\#hackathon)

We're running a week long hackathon starting NOW. There are some legit prizes, and you can win in a bunch of different categories.
Check the [full instructions here](https://supabase.com/blog/1-the-supabase-hackathon) on how to participate. Submissions close next Friday at midnight PST.

![Hackathon](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fhackathon.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Hooks & Functions [\#](https://supabase.com/blog/supabase-beta-july-2021\#hooks--functions)

We made an announcement on the progress of functions, and even shipped a few preliminary components, try them out and give us feedback as we continue to move towards this next major milestone.
Read the latest [updates here](https://supabase.com/blog/supabase-functions-updates).

![Hooks & Functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fhooks.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Swag Store [\#](https://supabase.com/blog/supabase-beta-july-2021\#swag-store)

Get your hands on some [Supabase Swag](https://supabase.store/), hand packed and mailed by our team based in Singapore.

![Swag Store](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fswag.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Community [\#](https://supabase.com/blog/supabase-beta-july-2021\#community)

- [@traversymedia](https://twitter.com/traversymedia) made a [Supabase Crash Course](https://www.youtube.com/watch?v=7uKQBl9uZ00) video
- [@themarcusbattle](https://twitter.com/themarcusbattle/status/1419638564573360130?s=20) wrote a [guide](https://www.twilio.com/blog/send-sms-notifications-supabase-users-node-js-twilio-messaging) on sending sms notifications using node.js, Twilio, and Supabase (this is different to sms auth above)
- [@dots\_hq](https://twitter.com/dots_hq) launched a slack/discord [community management tool](https://dots.community/) built on Supabase
- [@KennethCassel](https://twitter.com/KennethCassel) launched a [platform for building programming courses](https://www.slip.so/) using Supabase
- [@MobbinDesign](https://twitter.com/MobbinDesign) migrated their UI/UX library app to Supabase, currently [serving 200,000 users](https://supabase.com/blog/mobbin-supabase-200000-users)
- To the amazing users who are helping moderate our discord server, ya'll are amazing

**Supabase GitHub Star Growth**

![14200 stars on GitHub.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-july%2Fgithub-growth.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Source: [repository.surf/supabase](https://repository.surf/supabase)

If you want to keep up to date, make sure you [subscribe to our YouTube channel](https://www.youtube.com/c/supabase) or
[follow us on Twitter](https://twitter.com/supabase).

## Coming Next [\#](https://supabase.com/blog/supabase-beta-july-2021\#coming-next)

Security, stability, performance ... and Functions.

## Get started [\#](https://supabase.com/blog/supabase-beta-july-2021\#get-started)

- Start using Supabase today: [supabase.com/dashboard](https://supabase.com/dashboard/)
- Make sure to [star us on GitHub](https://github.com/supabase/supabase)
- Follow us [on Twitter](https://twitter.com/supabase)
- Subscribe to our [YouTube channel](https://www.youtube.com/c/supabase)
- Become a [sponsor](https://github.com/sponsors/supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-july-2021&text=Supabase%20Beta%20July%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-july-2021&text=Supabase%20Beta%20July%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-july-2021&t=Supabase%20Beta%20July%202021)

[Last post\\
\\
**Supabase Beta August 2021** \\
\\
10 September 2021](https://supabase.com/blog/supabase-beta-august-2021)

[Next post\\
\\
**Open Source Hackathon Winners** \\
\\
9 August 2021](https://supabase.com/blog/hackathon-winners)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Launch Week II: The SQL](https://supabase.com/blog/supabase-beta-july-2021#launch-week-ii-the-sql)
- [Auth v2 with Phone Auth](https://supabase.com/blog/supabase-beta-july-2021#auth-v2-with-phone-auth)
- [Storage is now in Beta](https://supabase.com/blog/supabase-beta-july-2021#storage-is-now-in-beta)
- [Dashboard v2](https://supabase.com/blog/supabase-beta-july-2021#dashboard-v2)
- [We launched a Discord server](https://supabase.com/blog/supabase-beta-july-2021#we-launched-a-discord-server)
- [PostgreSQL 13](https://supabase.com/blog/supabase-beta-july-2021#postgresql-13)
- [PostgREST v8.0](https://supabase.com/blog/supabase-beta-july-2021#postgrest-v80)
- [Flutter/Dart support](https://supabase.com/blog/supabase-beta-july-2021#flutterdart-support)
- [Hackathon](https://supabase.com/blog/supabase-beta-july-2021#hackathon)
- [Hooks & Functions](https://supabase.com/blog/supabase-beta-july-2021#hooks--functions)
- [Swag Store](https://supabase.com/blog/supabase-beta-july-2021#swag-store)
- [Community](https://supabase.com/blog/supabase-beta-july-2021#community)
- [Coming Next](https://supabase.com/blog/supabase-beta-july-2021#coming-next)
- [Get started](https://supabase.com/blog/supabase-beta-july-2021#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-july-2021&text=Supabase%20Beta%20July%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-july-2021&text=Supabase%20Beta%20July%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-july-2021&t=Supabase%20Beta%20July%202021)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)