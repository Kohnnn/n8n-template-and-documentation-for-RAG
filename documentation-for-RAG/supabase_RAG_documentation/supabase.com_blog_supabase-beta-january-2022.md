---
url: "https://supabase.com/blog/supabase-beta-january-2022"
title: "Supabase Beta January 2022"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta January 2022

22 Feb 2022

•

6 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Supabase Beta January 2022](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-january%2Fthumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This month's beta update is more stacked than the Superbowl (\*Supa-bowl) halftime show. Here’s all of the highlights from January...

## New OAuth providers [\#](https://supabase.com/blog/supabase-beta-january-2022\#new-oauth-providers)

![New 0Auth Providers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-january%2Fnew-auth-providers-supabase_monthly-email-jan-2022.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’re continually amazed by how quickly new auth providers are being added into Supabase, and last month, 2 more have been added.

### Notion [\#](https://supabase.com/blog/supabase-beta-january-2022\#notion)

Added by [zernonia](https://github.com/zernonia).
You may already know him as the maintainer of [madewithsupabase.com](https://www.madewithsupabase.com/).

### LinkedIn [\#](https://supabase.com/blog/supabase-beta-january-2022\#linkedin)

Added by [riderx](https://github.com/riderx).
You may already be familiar with Martin from his podcast [Indie Makers](https://podcasts.apple.com/us/podcast/indie-makers/id1488437972).

## New SMS providers [\#](https://supabase.com/blog/supabase-beta-january-2022\#new-sms-providers)

![New SMS Providers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-january%2Fnew-sms-providers-supabase_monthly-email-jan-2022.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Along with the new 0Auth providers above, last month saw the addition of two more SMS phone providers to allow you to authenticate users via an SMS OTP (One-Time Password) token.

### Vonage [\#](https://supabase.com/blog/supabase-beta-january-2022\#vonage)

**[Vonage](https://www.vonage.com/)** is a US-based cloud communications provider.
Added by [devkiran](https://github.com/devkiran) (from [BoxyHQ](https://twitter.com/BoxyHQ)).

### Textlocal [\#](https://supabase.com/blog/supabase-beta-january-2022\#textlocal)

We are now fulfilling a popular request with this Indian-compliant SMS provider, [Textlocal](https://www.textlocal.com/).
Also added by [devkiran](https://github.com/devkiran).

### Other SMS providers [\#](https://supabase.com/blog/supabase-beta-january-2022\#other-sms-providers)

Just a reminder, we also support [Twilio](https://supabase.com/docs/guides/auth/phone-login/twilio) and [MessageBird](https://supabase.com/docs/guides/auth/phone-login/messagebird).

On a final note, we are hiring for an [Auth Engineer](https://about.supabase.com/careers/auth-engineers).

## Query logs with SQL [\#](https://supabase.com/blog/supabase-beta-january-2022\#query-logs-with-sql)

Supabase logs are more powerful with the [newly added SQL querying](https://github.com/supabase/supabase/pull/4734).

We added [timestamp filtering](https://github.com/supabase/supabase/pull/4904), and you’ll notice our usage charts have [more time spans available](https://github.com/supabase/supabase/pull/4732).

We’re enabling developers to quickly diagnose issues with their projects with powerful logging and observability tools and we have a lot more to come.

## GraphQL v0.1.0 [\#](https://supabase.com/blog/supabase-beta-january-2022\#graphql-v010)

![Graph QL v0.1.0](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-january%2Fpg_graphql_0.1.0_monthly-email-dec-2021.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Last month we released [`pg_graphql`](https://github.com/supabase/pg_graphql) v0.1.0, which includes [Comment Directives](https://supabase.github.io/pg_graphql/configuration/#comment-directives).

We haven’t released GraphQL onto the platform yet because we it's still under heavy development. You can expect availability in the next few months.

Example

`
create table account(
    id serial primary key
);
comment on table public.account is
e'@graphql({ "name": "AccountHolder" })';
`

Result

`
// Renames "Account" to "AccountHolder"
type AccountHolder {
id: Int!
}
`

## New examples [\#](https://supabase.com/blog/supabase-beta-january-2022\#new-examples)

### Remix Auth [\#](https://supabase.com/blog/supabase-beta-january-2022\#remix-auth)

It’s all anyone seems to be [talking about](https://twitter.com/jkup/status/1456360115205033989). We genuinely love what [Remix](https://remix.run/) are doing, so it’s only right that we show off how Remix and Supabase work well together.

Check out the new [Remix Auth example](https://github.com/supabase/examples/tree/main/supabase-js-v1/auth/remix-auth), and let us know what you think.

### Expo Todo List [\#](https://supabase.com/blog/supabase-beta-january-2022\#expo-todo-list)

Our React Native example has been correctly updated to be an Expo example.
[Check it out here](https://github.com/supabase/examples/tree/main/supabase-js-v1/todo-list/expo-todo-list).

## Video: API requests with Database Webhooks [\#](https://supabase.com/blog/supabase-beta-january-2022\#video-api-requests-with-database-webhooks)

There's no stopping [Jon Meyers](https://jonmeyers.io/videos)! He’s back with an in-depth video on how to easily [automate API requests](https://www.youtube.com/watch?v=codAs9-NeHM&feature=emb_title) using our very own Database Webhooks.

You'll learn how to listen to _any_ database change, then send those changes [in a payload](https://supabase.com/blog/supabase-functions-updates#hook-payload) via HTTP request.

Automate API requests with Database Webhooks in Supabase - YouTube

Supabase

54.4K subscribers

[Automate API requests with Database Webhooks in Supabase](https://www.youtube.com/watch?v=codAs9-NeHM)

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

[Watch on YouTube](https://www.youtube.com/watch?v=codAs9-NeHM "Watch on YouTube")

## Set your own support ticket priority [\#](https://supabase.com/blog/supabase-beta-january-2022\#set-your-own-support-ticket-priority)

As with any platform, there can be the occasional glitch.

The Supabase Dashboard includes a dedicated support form that goes straight to our support inbox. This support form includes your project information and,
since we all want to see your issues solved, we thought it would make sense that _you_ could set the priority of your support tickets.

This change has drastically improved response times for urgent support tickets.
The form includes extra “urgent” levels for the PRO and Pay As You Go projects.

And, as part of our continued commitment to Support, we are hiring [Support Engineers](https://about.supabase.com/careers/support-and-qa).

## Community [\#](https://supabase.com/blog/supabase-beta-january-2022\#community)

As always, the community has been amazing during the month of February.

### Supabase + Snaplet [\#](https://supabase.com/blog/supabase-beta-january-2022\#supabase--snaplet)

Are you maintaining multiple environments? Snaplet helps you copy a production database and clone it into different environments.

Check out the [Supabase clone environments](https://docs.snaplet.dev/tutorials/supabase-clone-environments) tutorial on the Snaplet docs.

Supabase Environment Parity with Snaplet - YouTube

Snaplet

70 subscribers

[Supabase Environment Parity with Snaplet](https://www.youtube.com/watch?v=oPtMMhdhEP4)

Snaplet

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

[Watch on YouTube](https://www.youtube.com/watch?v=oPtMMhdhEP4 "Watch on YouTube")

### Supabase + Retool [\#](https://supabase.com/blog/supabase-beta-january-2022\#supabase--retool)

Retool has put together a brilliant 10 minute admin panel setup using Supabase with Retool.

How to build an admin panel for Supabase in 10 minutes - YouTube

Retool

9.46K subscribers

[How to build an admin panel for Supabase in 10 minutes](https://www.youtube.com/watch?v=AgB2-CSrnoI)

Retool

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

[Watch on YouTube](https://www.youtube.com/watch?v=AgB2-CSrnoI "Watch on YouTube")

### Learn with Jason [\#](https://supabase.com/blog/supabase-beta-january-2022\#learn-with-jason)

Jason Lengstorf caught up with our very own [Jon Meyers](https://jonmeyers.io/) on his awesome show, [Learn with Jason](https://www.youtube.com/watch?v=8vqY1KT4TLU), to talk about building an app [with Supabase and Next.js](https://supabase.com/docs/guides/with-nextjs).

Build an App With Supabase and NextJS - YouTube

CodeTV (formerly Learn With Jason)

95.7K subscribers

[Build an App With Supabase and NextJS](https://www.youtube.com/watch?v=8vqY1KT4TLU)

CodeTV (formerly Learn With Jason)

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

[Watch on YouTube](https://www.youtube.com/watch?v=8vqY1KT4TLU "Watch on YouTube")

### New article highlights [\#](https://supabase.com/blog/supabase-beta-january-2022\#new-article-highlights)

- Arctype published a new guide showing how to connect to your Supabase database. [Link](https://arctype.com/postgres/connect/supabase-postgres)
- Marmalabs built a Supabase adapter for react-admin, the frontend framework for building admin applications on top of REST/GraphQL services. [Link](https://github.com/marmelab/ra-supabase)
- HotGlue created a guide showing how easy it is to integrate Salesforce and Supabase. [Link](https://www.notion.so/Supabase-and-hotglue-article-9e7f5583d27c419490ee7d536d6d269d)

### PostgREST [\#](https://supabase.com/blog/supabase-beta-january-2022\#postgrest)

One of Supabase’s key tools that allow a lot of our functionality has had some updates.

- `pg_listen` was removed in favor of PostgREST’s built-in schema reloading.
- PostgREST database connection pool size gets scaled with compute size for better performance for certain workload shapes.

## Coming Next: Launch Week 4 [\#](https://supabase.com/blog/supabase-beta-january-2022\#coming-next-launch-week-4)

Preparation for Launch Week 4 is underway!

Of course, we can’t tell you what will happen (perhaps because we don’t know ourselves yet), but you can always speculate in the community [Discord server](https://discord.supabase.com/), or even [tweet us your predictions](https://twitter.com/supabase).

## Get started [\#](https://supabase.com/blog/supabase-beta-january-2022\#get-started)

- Start using Supabase today: **[supabase.com/dashboard](https://supabase.com/dashboard/)**
- Make sure to **[star us on GitHub](https://github.com/supabase/supabase)**
- Follow us **[on Twitter](https://twitter.com/supabase)**
- Subscribe to our **[YouTube channel](https://www.youtube.com/c/supabase)**
- Become a **[sponsor](https://github.com/sponsors/supabase)**

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2022&text=Supabase%20Beta%20January%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2022&text=Supabase%20Beta%20January%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2022&t=Supabase%20Beta%20January%202022)

[Last post\\
\\
**Postgres Auditing in 150 lines of SQL** \\
\\
8 March 2022](https://supabase.com/blog/postgres-audit)

[Next post\\
\\
**Golden Kitty Awards Ceremony Watch Party with Supabase** \\
\\
20 January 2022](https://supabase.com/blog/product-hunt-golden-kitty-awards-2021)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [New OAuth providers](https://supabase.com/blog/supabase-beta-january-2022#new-oauth-providers)
  - [Notion](https://supabase.com/blog/supabase-beta-january-2022#notion)
  - [LinkedIn](https://supabase.com/blog/supabase-beta-january-2022#linkedin)
- [New SMS providers](https://supabase.com/blog/supabase-beta-january-2022#new-sms-providers)
  - [Vonage](https://supabase.com/blog/supabase-beta-january-2022#vonage)
  - [Textlocal](https://supabase.com/blog/supabase-beta-january-2022#textlocal)
  - [Other SMS providers](https://supabase.com/blog/supabase-beta-january-2022#other-sms-providers)
- [Query logs with SQL](https://supabase.com/blog/supabase-beta-january-2022#query-logs-with-sql)
- [GraphQL v0.1.0](https://supabase.com/blog/supabase-beta-january-2022#graphql-v010)
- [New examples](https://supabase.com/blog/supabase-beta-january-2022#new-examples)
  - [Remix Auth](https://supabase.com/blog/supabase-beta-january-2022#remix-auth)
  - [Expo Todo List](https://supabase.com/blog/supabase-beta-january-2022#expo-todo-list)
- [Video: API requests with Database Webhooks](https://supabase.com/blog/supabase-beta-january-2022#video-api-requests-with-database-webhooks)
- [Set your own support ticket priority](https://supabase.com/blog/supabase-beta-january-2022#set-your-own-support-ticket-priority)
- [Community](https://supabase.com/blog/supabase-beta-january-2022#community)
  - [Supabase + Snaplet](https://supabase.com/blog/supabase-beta-january-2022#supabase--snaplet)
  - [Supabase + Retool](https://supabase.com/blog/supabase-beta-january-2022#supabase--retool)
  - [Learn with Jason](https://supabase.com/blog/supabase-beta-january-2022#learn-with-jason)
  - [New article highlights](https://supabase.com/blog/supabase-beta-january-2022#new-article-highlights)
  - [PostgREST](https://supabase.com/blog/supabase-beta-january-2022#postgrest)
- [Coming Next: Launch Week 4](https://supabase.com/blog/supabase-beta-january-2022#coming-next-launch-week-4)
- [Get started](https://supabase.com/blog/supabase-beta-january-2022#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2022&text=Supabase%20Beta%20January%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2022&text=Supabase%20Beta%20January%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2022&t=Supabase%20Beta%20January%202022)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)