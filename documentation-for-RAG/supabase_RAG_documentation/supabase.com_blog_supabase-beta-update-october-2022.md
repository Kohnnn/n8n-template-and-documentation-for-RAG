---
url: "https://supabase.com/blog/supabase-beta-update-october-2022"
title: "Supabase Beta October 2022"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta October 2022

02 Nov 2022

•

4 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta October 2022](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-october%2Fmonthly-update-october-2022.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

During October, we shipped something for everybody: new SDKs, quickstarts, Functions tricks, and more. All are listed here just for you. But, more importantly, Launch Week 6️⃣ has a date!

## supabase-js v2 and supabase-flutter v1 released [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#supabase-js-v2-and-supabase-flutter-v1-released)

![supabase-js v2 and supabase-flutter v1 released](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-october%2Fsupabase-js-v2-supabase-flutter-v1-header.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The new versions of our two most popular SDKs have been fully released. It couldn’t have happened without our amazing community, thanks to everyone involved. Now, it’s time to build 🛠

[Try supabase-js V2](https://supabase.com/docs/reference/javascript/)

[Try flutter-supabase V1](https://supabase.com/docs/reference/dart)

## New Next.js quickstart & Next.js 13 example [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#new-nextjs-quickstart--nextjs-13-example)

![New Next.js quickstart & Next.js 13 example](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-october%2Fnext-header.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Next.js is all the rage right now 🔥

Next.js Conf raised the bar for dev conferences. We had the honor of being a Gold Sponsor, so we revamped our [Next.js Quickstart guide](https://supabase.com/docs/guides/with-nextjs) to include our pre-built Auth UI and [Auth Helpers.](https://supabase.com/docs/guides/auth/auth-helpers/nextjs)

And Next.js 13 was announced! Making it extremely easy to fetch and cache data from our [Serverless API](https://supabase.com/docs/guides/database/api). So we put together an [example to try it out](https://github.com/supabase/supabase/tree/master/examples/caching/with-nextjs-13).

## Supabase Auth and Server-Side Rendering [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#supabase-auth-and-server-side-rendering)

![Supabase Auth and Server-Side Rendering](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-october%2Fauthentication-server-side-docs.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The Auth team published an in-depth doc explaining how Supabase Auth supports server-side rendering. Includes an explanation of the authentication flow and answers to some of the more common questions.

[Read the docs](https://supabase.com/docs/guides/auth/server-side-rendering).

## Database Testing with pgTAP [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#database-testing-with-pgtap)

![Database Testing with pgTAP](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-october%2Fdatabase-testing-postgres-pgtap.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Do you have 100% code coverage? Probably not, because that’s usually the last thing you think of, but _definitely_ not if you don’t have database tests. We just shipped a framework for Database Tests which makes it incredibly easy to test your database using pgTAP and pg\_prove.

[Learn how it works](https://supabase.com/docs/guides/database/testing).

## Edge Functions Update [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#edge-functions-update)

![Edge Functions Update](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-october%2Ffunctions-new-methods.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Functions now support GET requests! Other HTTP verbs such as PUT, PATCH, and DELETE are supported too.

[Check this example](https://github.com/supabase/supabase/blob/master/examples/edge-functions/supabase/functions/restful-tasks/index.ts)

## Quick Product Updates [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#quick-product-updates)

- supabase-py 🐍 now has functions support! [PR](https://github.com/supabase-community/supabase-py/pull/179)
- You can now detect users’ location from Edge Functions easily by using `X-Forwarded-For header`. [Example](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/location)
- Return `provider_refresh_token` along with `provider_access_token`. [PR](https://github.com/supabase/gotrue/pull/641)
- Added a `refreshSession` method to allow users to forcefully refresh a session instead of waiting for it to autorefresh upon expiry. Thanks to [@j4w8n](https://github.com/j4w8n) for the [PR](https://github.com/supabase/gotrue-js/pull/505) 🙇🏻‍♂️
- Logging: realtime, storage, postgrest, and pgbouncer released.
- Trigger a file download by adding the download query parameter to your storage objects. storage-api. [PR](https://github.com/supabase/storage-api/issues/122)

## Made with Supabase [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#made-with-supabase)

![Made with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-october%2Ftwitter-card-header.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

There were so many amazing apps Made with Supabase this month that we couldn’t choose just one… so here are three:

🚰 [Remote Water Feeder](https://twitter.com/SomangshuG/status/1581888060643774465) by Somangshu Goswami

📊 [Decile App](https://github.com/decileapp/decile) by [Krishna](https://twitter.com/ntkris)

📑 [Explainpaper](https://www.explainpaper.com/) by [Aman Jha](https://twitter.com/amanjha__) and [Jade](https://twitter.com/functionofjade)

If you want to see +100 other apps, check [the replies](https://twitter.com/supabase/status/1585226233742229504).

## Extended Community Highlights [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#extended-community-highlights)

![Community](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fcommunity.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

- Mark Buggraf sat down to chat about postgres-wasm with LogRocket. [Podcast](https://podrocket.logrocket.com/opensourcing-postgres-wasm)
- A collection of awesome Supabase resources. [awesome-supabase](https://github.com/lyqht/awesome-supabase)
- All the Happy Hour Hacktoberfest episodes. [Episode 1](https://www.youtube.com/watch?v=qRSYenBLHHQ) \| [Episode 2](https://www.youtube.com/watch?v=-RlivqzNIso) \| [Episode 3](https://www.youtube.com/watch?v=LzDIptBGtUw)
- Hacking the PostgREST Headers: Oh, the Things You Can Do! [Article](https://dev.to/burggraf/hacking-the-postgrest-headers-oh-the-things-you-can-do-ck2)
- Why we’re moving away from Firebase. [Blog post](https://koptional.com/article/why-we%E2%80%99re-moving-away-from-firebase)
- Basejump SaaS starter for Supabase. [Repo](https://github.com/usebasejump/basejump)
- SvelteKit + Supabase CRUD with RLS: Row-Level Security! [Video](https://www.youtube.com/watch?v=iKzjfHARXpc)
- Building a startup (build log 2#): Authenticating students with Supabase. [Blog Post](https://dev.to/paul_emechebe/building-a-startup-build-log-2-authenticating-users-with-supabase-1p1b)
- CRUD with Supabase in Flutter. [Tutorial](https://sadabwasim.medium.com/crud-with-supabase-in-flutter-dbe97fa0c15)
- Phone Auth with self-hosted Supabase. [Video](https://www.youtube.com/watch?v=z3sE-ix2uok)
- My Future with Elixir: set-theoretic types. [Blog Post](https://elixir-lang.org/blog/2022/10/05/my-future-with-elixir-set-theoretic-types/)
- Upload media to Supabase from remote URL with nodejs. [Blog Post](https://www.antoinemesnil.com/posts/upload-media-supabase)
- Say goodbye to backend development. [Video](https://www.youtube.com/watch?v=9CuTxeioKF4)

## Launch Week 6 date announced [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#launch-week-6-date-announced)

We are ending 2022 on a high note ✊. Mark your calendars: Launch Week 6 is happening on **December 12-16**.

In the meantime, [revisit LW5](https://supabase.com/launch-week).

## We’re hiring [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#were-hiring)

Come join one of the fastest-growing open source projects ever 🤗

- [Sales Engineer](https://boards.greenhouse.io/supabase/jobs/4711141004)
- [Lead Billing and API Engineer](https://boards.greenhouse.io/supabase/jobs/4652333004)
- [View all our openings](https://boards.greenhouse.io/supabase)

## Meme Zone [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#meme-zone)

If you made it this far in the blog post you deserve a treat. [Follow us on Twitter](https://twitter.com/supabase) for more.

![Supabase meme October 2022](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-october%2Fbeta-update-october-meme.jpeg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Get started [\#](https://supabase.com/blog/supabase-beta-update-october-2022\#get-started)

- Start using Supabase today: **[supabase.com/dashboard](https://supabase.com/dashboard/)**
- Make sure to **[star us on GitHub](https://github.com/supabase/supabase)**
- Follow us **[on Twitter](https://twitter.com/supabase)**
- Subscribe to our **[YouTube channel](https://www.youtube.com/c/supabase)**

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-october-2022&text=Supabase%20Beta%20October%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-october-2022&text=Supabase%20Beta%20October%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-october-2022&t=Supabase%20Beta%20October%202022)

[Last post\\
\\
**Authentication in Ionic Angular with Supabase** \\
\\
8 November 2022](https://supabase.com/blog/authentication-in-ionic-angular)

[Next post\\
\\
**What is PostgreSQL commitfest and how to contribute** \\
\\
27 October 2022](https://supabase.com/blog/postgresql-commitfest)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [supabase-js v2 and supabase-flutter v1 released](https://supabase.com/blog/supabase-beta-update-october-2022#supabase-js-v2-and-supabase-flutter-v1-released)
- [New Next.js quickstart & Next.js 13 example](https://supabase.com/blog/supabase-beta-update-october-2022#new-nextjs-quickstart--nextjs-13-example)
- [Supabase Auth and Server-Side Rendering](https://supabase.com/blog/supabase-beta-update-october-2022#supabase-auth-and-server-side-rendering)
- [Database Testing with pgTAP](https://supabase.com/blog/supabase-beta-update-october-2022#database-testing-with-pgtap)
- [Edge Functions Update](https://supabase.com/blog/supabase-beta-update-october-2022#edge-functions-update)
- [Quick Product Updates](https://supabase.com/blog/supabase-beta-update-october-2022#quick-product-updates)
- [Made with Supabase](https://supabase.com/blog/supabase-beta-update-october-2022#made-with-supabase)
- [Extended Community Highlights](https://supabase.com/blog/supabase-beta-update-october-2022#extended-community-highlights)
- [Launch Week 6 date announced](https://supabase.com/blog/supabase-beta-update-october-2022#launch-week-6-date-announced)
- [We’re hiring](https://supabase.com/blog/supabase-beta-update-october-2022#were-hiring)
- [Meme Zone](https://supabase.com/blog/supabase-beta-update-october-2022#meme-zone)
- [Get started](https://supabase.com/blog/supabase-beta-update-october-2022#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-october-2022&text=Supabase%20Beta%20October%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-october-2022&text=Supabase%20Beta%20October%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-october-2022&t=Supabase%20Beta%20October%202022)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)