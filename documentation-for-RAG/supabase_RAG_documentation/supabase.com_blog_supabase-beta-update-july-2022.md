---
url: "https://supabase.com/blog/supabase-beta-update-july-2022"
title: "Supabase Beta July 2022"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta July 2022

03 Aug 2022

•

4 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta July 2022](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It’s happening! Launch Week is back ✊. We are preparing lots of product announcements and fun activities. Join us the week of August 15-19 for Launch Week 5️⃣.

We don't ship only during Launch Weeks, so this month we still bring you some great new stuff: Flutter SDK 1.0 (developer preview), Auth Helpers, pg\_jsonschema, and more.

## Launch Week Golden Ticket [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#launch-week-golden-ticket)

![Launch week golden ticket](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2Fteaser.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Register for [#SupaLaunchWeek 5](https://twitter.com/hashtag/SupaLaunchWeek) and if you are lucky, you may pull a golden ticket and win a limited edition Supabase goodie bag! [Get a ticket](https://supabase.com/launch-week).

## Supabase Flutter SDK 1.0 developer preview [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#supabase-flutter-sdk-10-developer-preview)

![flutter sdk 1.0](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2Fflutter-sdk.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase Flutter SDK is getting a major update, with a big focus on developer experience. We shared a preview of what is to come so you can help us make it even better with your feedback. [Read the blog.](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview)

## Revamped Auth Helpers (now with SvelteKit support) [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#revamped-auth-helpers-now-with-sveltekit-support)

![Sveltekit auth helpers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2Fauth-helpers.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've been hard at work making an Auth experience that is as smooth as possible for Supabase developers. The new Auth Helpers have a better experience for server-side rendering (SSR) environments, new Github structure, SvelteKit support, and more. [Read the blog](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support).

## pg\_jsonschema – A Postgres extension for JSON validation [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#pg_jsonschema--a-postgres-extension-for-json-validation)

![pg_jsonschema](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2Fpg_jsonschema.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Born as an excuse to play with pgx, pg\_jsonschema is a solution we're exploring to allow enforcing more structure on json and jsonb typed postgres columns. [Only 10 lines of code](https://github.com/supabase/pg_jsonschema/tree/fb7ab09bf6050130e8d656f2999ec0f6a3fedc0d) 😎

## hCaptcha integration [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#hcaptcha-integration)

![hCaptcha](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2FhCaptcha-1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The new hCpatcha integration allows you to implement captcha functionality for auth. Enable hCaptcha protection in the auth settings to stop bots attacks and protect your users' privacy. [Captcha settings](https://supabase.com/docs/reference/tools/reference-auth).

## Updated Settings UI in dashboard [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#updated-settings-ui-in-dashboard)

![supabase-updated-settings-ui-dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2Fauth-config.jpeg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've started updating our settings UI, starting with the Auth settings. You'll now see updated UI for setting up your [Auth providers](https://supabase.com/dashboard/project/_/auth/providers), [Email templates](https://supabase.com/dashboard/project/_/auth/templates), and [SMTP config](https://supabase.com/dashboard/project/_/auth/url-configuration).

## Quick product announcements [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#quick-product-announcements)

-  Email OTP now supports 6-10 digits length. [PR](https://github.com/supabase/gotrue/pull/513)
-  GenerateLink method now returns the email\_otp, the hashed\_token , the verification\_type and the redirect\_to. [PR](https://github.com/supabase/gotrue/pull/537)

## Nuxt 3 Quickstart [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#nuxt-3-quickstart)

![nuxt-3-supabase-quickstart](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2FNuxt-Supabase-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

There is a new quickstart in town. The guide, powered by [NuxtSupabase](https://supabase.nuxtjs.org/), shows how to build a simple user management app using Supabase and Nuxt 3, including Database, Auth, Storage, and more. [Get started](https://supabase.com/docs/guides/with-nuxt-3).

## Made with Supabase [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#made-with-supabase)

![made with supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2Fbuy-me-a-pizza.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[BuyMeAPizza](https://www.buymea.pizza/) \| A brand new, free, and open source service to accept donations in crypto on your website. Built with Next.js, Tailwind, Supabase, and Solana tools.

Discover other projects: [Made with Supabase](https://www.madewithsupabase.com/)

## Community highlights [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#community-highlights)

![Community](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2Fcommunity--dark.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The Supabase community is exploding and we’ve reached a point where we can’t fit everything into our monthly newsletter so here’s the full list of community updates from July:

- Netlify announced a new webinar series, Web Ecosystem, and we get to be part of it. [Blog Post](https://www.netlify.com/blog/web-ecosystem-webinar-series/)
- Implementing "seen by" functionality with Postgres. [Blog Post](https://supabase.com/blog/seen-by-in-postgresql)
- Open Source Startup Podcast with our CEO Paul Copplestone. [Podcast](https://anchor.fm/ossstartuppodcast/episodes/E43-Building-Supabase--the-Open-Source-Firebase-Alternative-e1ld637)
- Scaleway listed 40+ of the best open-source tools to build your startup. [Blog Post](https://blog.scaleway.com/40-open-source-projects/)
- Sign-up form with OTP and auto login using Supabase and Arengu. [Guide](https://www.arengu.com/tutorials/sign-up-form-with-otp-and-auto-login-using-supabase)
- Setup Supabase with Nest.js. [Tutorial](https://blog.devgenius.io/setup-supabase-with-nest-js-85041b03ec3a)
- Loading SportsDB data into Supabase. [Tutorial](https://dev.to/supabase/auto-generated-documentation-in-supabase-5e8o)
- Introduction to Supabase: Postgres Database using Python. [Tutorial](https://www.analyticsvidhya.com/blog/2022/07/introduction-to-supabase-postgres-database-using-python/)
- Supabase and SWR to fetch data updates in realtime using React Hooks. [Tutorial](https://dev.to/jakobpotosme/supabase-swr-3icp)
- Protected routes using Next.js Edge Middleware & Supabase. [Tutorial](https://engineering.udacity.com/protected-routes-using-next-js-edge-middleware-supabase-f197ba7f503c)
- Supabase backend demo with Bravo Studio. [Video](https://www.youtube.com/watch?v=ZWQeAmbYFzg)
- Building a live demo with Supabase and AppSmith. [Video](https://www.youtube.com/watch?v=xmb4JrTYhZg)
- Auto-generated documentation in Supabase. [Tutorial](https://dev.to/supabase/auto-generated-documentation-in-supabase-5ecd)
- Speeding Up Bulk Loading in PostgreSQL. [Blog Post](https://dev.to/supabase/speeding-up-bulk-loading-in-postgresql-41g5)
- Installing React-Admin In A Remix App. [Tutorial](https://marmelab.com/blog/2022/07/01/add-react-admin-to-your-remix-app-using-supabase.html)
- How to set up Supabase in React? And Some Useful Tips. [Tutorial](https://dev.to/eminvergil/how-to-setup-supabase-in-react-and-some-useful-tips-40oc)
- My approach to authentication with Next.JS, Prisma & Supabase. [Guide](https://ktra99.hashnode.dev/my-approach-to-authentication-with-nextjs-prisma-supabase)

## We’re hiring [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#were-hiring)

Come join one of the fastest growing open source projects ever 🤗

- [Customer Success (US time zone)](https://boards.greenhouse.io/supabase/jobs/4594393004)
- [Go-To-Market Recruiter](https://boards.greenhouse.io/supabase/jobs/4561503004)
- [View all our openings](https://boards.greenhouse.io/supabase)

* * *

## Meme Zone [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#meme-zone)

If you made it this far in the blog post you deserve a treat. [Follow us on Twitter](https://twitter.com/supabase) for more.

![Supabase meme june 2022](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-july%2FCSS-meme.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Get started [\#](https://supabase.com/blog/supabase-beta-update-july-2022\#get-started)

- Start using Supabase today: **[supabase.com/dashboard](https://supabase.com/dashboard/)**
- Make sure to **[star us on GitHub](https://github.com/supabase/supabase)**
- Follow us **[on Twitter](https://twitter.com/supabase)**
- Subscribe to our **[YouTube channel](https://www.youtube.com/c/supabase)**

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-july-2022&text=Supabase%20Beta%20July%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-july-2022&text=Supabase%20Beta%20July%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-july-2022&t=Supabase%20Beta%20July%202022)

[Last post\\
\\
**Slack Consolidate: a slackbot built with Python and Supabase** \\
\\
9 August 2022](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages)

[Next post\\
\\
**Supabase Flutter SDK 1.0 Developer Preview** \\
\\
2 August 2022](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Launch Week Golden Ticket](https://supabase.com/blog/supabase-beta-update-july-2022#launch-week-golden-ticket)
- [Supabase Flutter SDK 1.0 developer preview](https://supabase.com/blog/supabase-beta-update-july-2022#supabase-flutter-sdk-10-developer-preview)
- [Revamped Auth Helpers (now with SvelteKit support)](https://supabase.com/blog/supabase-beta-update-july-2022#revamped-auth-helpers-now-with-sveltekit-support)
- [pg\_jsonschema – A Postgres extension for JSON validation](https://supabase.com/blog/supabase-beta-update-july-2022#pg_jsonschema-%E2%80%93-a-postgres-extension-for-json-validation)
- [hCaptcha integration](https://supabase.com/blog/supabase-beta-update-july-2022#hcaptcha-integration)
- [Updated Settings UI in dashboard](https://supabase.com/blog/supabase-beta-update-july-2022#updated-settings-ui-in-dashboard)
- [Quick product announcements](https://supabase.com/blog/supabase-beta-update-july-2022#quick-product-announcements)
- [Nuxt 3 Quickstart](https://supabase.com/blog/supabase-beta-update-july-2022#nuxt-3-quickstart)
- [Made with Supabase](https://supabase.com/blog/supabase-beta-update-july-2022#made-with-supabase)
- [Community highlights](https://supabase.com/blog/supabase-beta-update-july-2022#community-highlights)
- [We’re hiring](https://supabase.com/blog/supabase-beta-update-july-2022#were-hiring)
- [Meme Zone](https://supabase.com/blog/supabase-beta-update-july-2022#meme-zone)
- [Get started](https://supabase.com/blog/supabase-beta-update-july-2022#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-july-2022&text=Supabase%20Beta%20July%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-july-2022&text=Supabase%20Beta%20July%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-july-2022&t=Supabase%20Beta%20July%202022)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)