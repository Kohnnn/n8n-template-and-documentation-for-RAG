---
url: "https://supabase.com/blog/supabase-beta-august-2021"
title: "Supabase Beta August 2021"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta August 2021

10 Sep 2021

•

5 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Supabase Beta August 2021](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Frelease-august-2021-cover.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've raised $30M and shipped a bunch of features. Let's dive into what's been happening at Supabase during the month of August.

### Quick recap [\#](https://supabase.com/blog/supabase-beta-august-2021\#quick-recap)

Watch a recap of this month's release.

Supabase Beta \| August 2021 - YouTube

Supabase

54.4K subscribers

[Supabase Beta \| August 2021](https://www.youtube.com/watch?v=YYpTh2DAvho)

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

[Watch on](https://www.youtube.com/watch?v=YYpTh2DAvho&embeds_referring_euri=https%3A%2F%2Fsupabase.com%2F)

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=YYpTh2DAvho "Watch on YouTube")

## We raised $30 million [\#](https://supabase.com/blog/supabase-beta-august-2021\#we-raised-30-million)

Hot off the press, we raised our Series A.
We'll use the funds to do more of the same - ship features and hire open source developers.
We'll release more details soon. Read more on [TechCrunch](https://techcrunch.com/2021/09/09/supabase-raises-30m-for-its-open-source-insta-backend/).

![Supabase Series A](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fsupabase-series-a.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Realtime Security, codename: WALRUS [\#](https://supabase.com/blog/supabase-beta-august-2021\#realtime-security-codename-walrus)

If you've been waiting for Row Level Security to land in Postgres [subscriptions](https://supabase.com/docs/reference/javascript/subscribe),
then you're going to love our new repo:
[Write Ahead Log Realtime Unified Security (WALRUS)](https://github.com/supabase/walrus).
The name might be a bit forced, but the security design is deliberate.
It's not in production yet, but we're making the repo public for comments using an
[RFC process](https://github.com/supabase/walrus/blob/master/README.md#rfc-process).

![Realtime Security, codename: WALRUS](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fwalrus.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Custom SMS templates [\#](https://supabase.com/blog/supabase-beta-august-2021\#custom-sms-templates)

If you're using SMS login in [Auth v2](https://supabase.com/blog/2021/07/28/supabase-auth-passwordless-sms-login), you can now customize the SMS which is sent to your users. Read more in the [docs](https://supabase.com/docs/guides/auth/phone-login/twilio#sms-custom-template).

![Custom SMS templates](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fcustom-sms.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Dart and Flutter Docs [\#](https://supabase.com/blog/supabase-beta-august-2021\#dart-and-flutter-docs)

Thanks entirely to [@dshukertjr](https://twitter.com/dshukertjr), we now have in-depth [reference Dart documentation](https://supabase.com/docs/reference/dart/installing) for CRUD, Auth, Realtime and more!

![Dart and Flutter Docs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fsupabase-flutter.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## We launched the South Korea region [\#](https://supabase.com/blog/supabase-beta-august-2021\#we-launched-the-south-korea-region)

We added another region for those wanting to host their data and APIs in Seoul. We now have 12 regions to choose from

![We launched the South Korea Region](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fsouth-korea.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Table creation is even easier [\#](https://supabase.com/blog/supabase-beta-august-2021\#table-creation-is-even-easier)

You can now create columns while creating your table. We've also added improvements for composite primary keys and foreign key creation.

![Table creation is even easier](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fcreate-tables.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Unbreakable CSV Imports [\#](https://supabase.com/blog/supabase-beta-august-2021\#unbreakable-csv-imports)

Our previous importer would choke on CSV files which were too large. Not any more!

![Unbreakable CSV Imports](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fcsv-imports.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Connection strings [\#](https://supabase.com/blog/supabase-beta-august-2021\#connection-strings)

We now provide a handy copy utility for various database connection strings because we were so tired of looking them up on Stack Overflow.

![Caption](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fconnection-strings.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## We released a primer on Row Level Security [\#](https://supabase.com/blog/supabase-beta-august-2021\#we-released-a-primer-on-row-level-security)

RLS can be a bit foreign for developers getting started with Postgres.
This video by [@\_dijonmusters](https://twitter.com/_dijonmusters) demystifies it. If you find the video a useful medium for learning, consider [subscribing to our channel](https://www.youtube.com/c/supabase).

Implement Authorization using Row Level Security (RLS) with Supabase (Step By Step Guide) - YouTube

Supabase

54.4K subscribers

[Implement Authorization using Row Level Security (RLS) with Supabase (Step By Step Guide)](https://www.youtube.com/watch?v=Ow_Uzedfohk)

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

[Watch on YouTube](https://www.youtube.com/watch?v=Ow_Uzedfohk "Watch on YouTube")

## Community [\#](https://supabase.com/blog/supabase-beta-august-2021\#community)

### We had a community Hackathon [\#](https://supabase.com/blog/supabase-beta-august-2021\#we-had-a-community-hackathon)

We held a one-week async Hackathon. Check out [all the winners](https://supabase.com/blog/hackathon-winners) \- it was truly impressive what people were able to build in just 7 days.

![We had a community Hackathon](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fhackathon.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### We had a team Hackathon [\#](https://supabase.com/blog/supabase-beta-august-2021\#we-had-a-team-hackathon)

The Supabase team didn't want to miss out on the fun so we held our own hackathon. It was a good way to dog food. Some notable projects include

- [Supaflix](https://supaflix.vercel.app/) by [@abc3](https://twitter.com/abc3erl) \[ [GitHub](https://github.com/abc3/supaflix)\] \- a Netflix clone build with Supabase
- [Personal-Casts](https://github.com/inian/personal-casts) by [@everconfusedguy](https://twitter.com/everconfusedguy) \[ [GitHub](https://github.com/inian/personal-casts)\] \- converts Youtube videos and articles into a personal podcast feed.
- And it wouldn't be a Supabase hackathon without a high-effort meme entry.
Check out [meme.town](http://meme.town/) by [@Joshenlimek](https://twitter.com/joshenlimek) \[ [GitHub](https://github.com/joshenlim/meme-maker)\]

![We had a team Hackathon](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fmeme-town.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### GitHub Trending [\#](https://supabase.com/blog/supabase-beta-august-2021\#github-trending)

We hit 18,000 stars on GitHub, and got to the [top of GitHub trending](https://twitter.com/supabase/status/1435868863518760964) for Typescript.

![GitHub Trending](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2021-august%2Fgithub-stars.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Source: [repository.surf/supabase](https://repository.surf/supabase)

If you want to keep up to date, make sure you [subscribe to our YouTube channel](https://www.youtube.com/c/supabase) or
[follow us on Twitter](https://twitter.com/supabase).

## Dependency contributions [\#](https://supabase.com/blog/supabase-beta-august-2021\#dependency-contributions)

### GoTrue (Auth) [\#](https://supabase.com/blog/supabase-beta-august-2021\#gotrue-auth)

- HCaptcha - users can add captcha on their passwordless logins to prevent abuse

[https://github.com/supabase/gotrue/pull/192](https://github.com/supabase/gotrue/pull/192)
- Email change endpoint is fixed (sends out 2 emails, one to the old email and one to the new one)

[https://github.com/supabase/gotrue/pull/132](https://github.com/supabase/gotrue/pull/132)

### PostgREST (APIs) [\#](https://supabase.com/blog/supabase-beta-august-2021\#postgrest-apis)

- Allow a function with single unnamed parameter to be called with POST

[https://github.com/PostgREST/postgrest/issues/1735](https://github.com/PostgREST/postgrest/issues/1735)

### pg\_net (Database Webhooks) [\#](https://supabase.com/blog/supabase-beta-august-2021\#pg_net-database-webhooks)

- Better handling of URL errors

[https://github.com/supabase/pg\_net/issues/39](https://github.com/supabase/pg_net/issues/39)

## Coming Next [\#](https://supabase.com/blog/supabase-beta-august-2021\#coming-next)

Last December we [moved from Alpha to Beta](https://supabase.com/beta), with a focus on Security, Performance, and Reliability. After a couple of Launch Weeks pushing out new and sexy features, we have decided it's time to focus on these again.

By the time we're done, Supabase will be production-ready for all use cases.

## Get started [\#](https://supabase.com/blog/supabase-beta-august-2021\#get-started)

- Start using Supabase today: [supabase.com/dashboard](https://supabase.com/dashboard/)
- Make sure to [star us on GitHub](https://github.com/supabase/supabase)
- Follow us [on Twitter](https://twitter.com/supabase)
- Subscribe to our [YouTube channel](https://www.youtube.com/c/supabase)
- Become a [sponsor](https://github.com/sponsors/supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-august-2021&text=Supabase%20Beta%20August%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-august-2021&text=Supabase%20Beta%20August%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-august-2021&t=Supabase%20Beta%20August%202021)

[Last post\\
\\
**Supabase Hacktoberfest Hackathon 2021** \\
\\
28 September 2021](https://supabase.com/blog/supabase-hacktoberfest-hackathon-2021)

[Next post\\
\\
**Supabase Beta July 2021** \\
\\
12 August 2021](https://supabase.com/blog/supabase-beta-july-2021)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Quick recap](https://supabase.com/blog/supabase-beta-august-2021#quick-recap)

- [We raised $30 million](https://supabase.com/blog/supabase-beta-august-2021#we-raised-30-million)
- [Realtime Security, codename: WALRUS](https://supabase.com/blog/supabase-beta-august-2021#realtime-security-codename-walrus)
- [Custom SMS templates](https://supabase.com/blog/supabase-beta-august-2021#custom-sms-templates)
- [Dart and Flutter Docs](https://supabase.com/blog/supabase-beta-august-2021#dart-and-flutter-docs)
- [We launched the South Korea region](https://supabase.com/blog/supabase-beta-august-2021#we-launched-the-south-korea-region)
- [Table creation is even easier](https://supabase.com/blog/supabase-beta-august-2021#table-creation-is-even-easier)
- [Unbreakable CSV Imports](https://supabase.com/blog/supabase-beta-august-2021#unbreakable-csv-imports)
- [Connection strings](https://supabase.com/blog/supabase-beta-august-2021#connection-strings)
- [We released a primer on Row Level Security](https://supabase.com/blog/supabase-beta-august-2021#we-released-a-primer-on-row-level-security)
- [Community](https://supabase.com/blog/supabase-beta-august-2021#community)
  - [We had a community Hackathon](https://supabase.com/blog/supabase-beta-august-2021#we-had-a-community-hackathon)
  - [We had a team Hackathon](https://supabase.com/blog/supabase-beta-august-2021#we-had-a-team-hackathon)
  - [GitHub Trending](https://supabase.com/blog/supabase-beta-august-2021#github-trending)
- [Dependency contributions](https://supabase.com/blog/supabase-beta-august-2021#dependency-contributions)
  - [GoTrue (Auth)](https://supabase.com/blog/supabase-beta-august-2021#gotrue-auth)
  - [PostgREST (APIs)](https://supabase.com/blog/supabase-beta-august-2021#postgrest-apis)
  - [pg\_net (Database Webhooks)](https://supabase.com/blog/supabase-beta-august-2021#pg_net-database-webhooks)
- [Coming Next](https://supabase.com/blog/supabase-beta-august-2021#coming-next)
- [Get started](https://supabase.com/blog/supabase-beta-august-2021#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-august-2021&text=Supabase%20Beta%20August%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-august-2021&text=Supabase%20Beta%20August%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-august-2021&t=Supabase%20Beta%20August%202021)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)