---
url: "https://supabase.com/blog/beta-update-june-2022"
title: "Supabase Beta June 2022"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta June 2022

06 Jul 2022

•

6 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta June 2022](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

There was so much stuff happening during June that we had to cut some updates from the newsletter! But don't worry, we are doing an extended version for the blog post, so go ahead and read on!

## Auth Helpers for Next.js revamped [\#](https://supabase.com/blog/beta-update-june-2022\#auth-helpers-for-nextjs-revamped)

![Auth Helpers for Next.js](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fauth-helpers.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase Auth Helpers are a collection of framework specific Auth utilities for getting user authentication and authorization set up in seconds. We have now separated the libraries into their own packages, which can now be installed individually: [@supabase/auth-helpers-nextjs](https://www.npmjs.com/package/@supabase/auth-helpers-nextjs) and [@supabase/auth-helpers-react](https://www.npmjs.com/package/@supabase/auth-helpers-react).

And here is a [step by step migration guide](https://github.com/supabase-community/auth-helpers/tree/main/packages/nextjs#migrating-from-supabasesupabase-auth-helpers-to-supabaseauth-helpers). Sveltekit and Remix helpers coming soon!

## Unlimited free projects [\#](https://supabase.com/blog/beta-update-june-2022\#unlimited-free-projects)

![Unlimited free projects](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Funlimited-paused.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Head on over to project settings to pause and restore projects on demand. This new feature gives you virtually unlimited free projects, so you can build as many things as you want. Want to experiment? Build a new demo? Just pause a project and start a new one. [Check the PR](https://github.com/supabase/supabase/pull/7384).

## Create projects from the Supabase CLI [\#](https://supabase.com/blog/beta-update-june-2022\#create-projects-from-the-supabase-cli)

![Create projects from the Supabase CLI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fcli.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It's here! Now you can create a project from the Supabase CLI. We will be extending the CLI with more features to manage your project, so stay tuned! [See the doc](https://supabase.com/docs/reference/cli/supabase-projects-create).

## Enable realtime for your table via the table editor [\#](https://supabase.com/blog/beta-update-june-2022\#enable-realtime-for-your-table-via-the-table-editor)

![Enable realtime for your table via the table editor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fenable-realtime.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've added an option to toggle realtime for a table in the table editor side panel editor. Never forget to add realtime again! [Full PR](https://github.com/supabase/supabase/pull/7346).

## Quick product announcements [\#](https://supabase.com/blog/beta-update-june-2022\#quick-product-announcements)

- We're migrating projects to new infra to support upcoming Multiplayer features. Check out [multiplayer.dev](http://multiplayer.dev/) and submit your info to be the first to know when these features drop.
- GoTrue now bubbles up PostgreSQL errors if the underlying error is from a RaiseException or if they were Integrity Constraint Violations. [PR](https://github.com/supabase/gotrue/pull/404)
- Added auth.jwt() function to return the user's jwt claims and we'll be deprecating auth.email() and auth.role() in a few months. [PR](https://github.com/supabase/gotrue/pull/484)
- Supabase Auth now provides IP addresses in the Audit Log. [PR](https://github.com/supabase/gotrue/pull/499)
- Random password generator when creating projects. [PR](https://github.com/supabase/supabase/pull/7249)

## Supabase Happy Hour [\#](https://supabase.com/blog/beta-update-june-2022\#supabase-happy-hour)

![Supabase Happy Hour](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fhappy-hour.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We just wrapped our new weekly live stream, [building a multi-platform app with Next.js and Flutter](https://youtube.com/playlist?list=PL5S4mPUpp4OvEgxBhoVxXb5YS1ZAZih2l). Since kicking off this new series, we've had endless requests from our US friends to "please stop dev'ing in the middle of the night" so they can join in the fun. You got it! 🎉

Tune in every Thursday at 17:00 PT \| 20:00 ET on [YouTube](https://www.youtube.com/c/supabase) or [Twitch](https://www.twitch.tv/supabase_tv).

## Matterday [\#](https://supabase.com/blog/beta-update-june-2022\#matterday)

![Matterday](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fmatterday.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Matterday](https://matterday.netlify.com/) is a supa-cool microsite with ideas of what development teams can do with the time saved from using tools like Netlify and Supabase. Here are the behind-the-scenes of how it was built: [Article and](https://jonmeyers.io/blog/how-i-built-the-back-end-for-netlify%27s-matterday-project-with-supabase) [Live Stream.](https://www.youtube.com/watch?v=bl4k4IiYYAQ)

## Made with Supabase [\#](https://supabase.com/blog/beta-update-june-2022\#made-with-supabase)

[PennySeed](https://www.pennyseed.fund/) \| A crowdfunding platform where the funding goal is divided by the number of pledges. Built with Supabase, Stripe, Next.js, Tailwindcss, and hosted on Vercel.

Discover other projects: [Made with Supabase](https://www.madewithsupabase.com/)

## Community highlights (extended) [\#](https://supabase.com/blog/beta-update-june-2022\#community-highlights-extended)

![Community](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fcommunity.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The Supabase community is exploding and we’ve reached a point where we can’t fit everything into our monthly newsletter so here’s the full list of community updates from June:

- We are sponsoring Elixir's creator to research and develop a type system powered by set-theoretic types for Elixir. [Tweet](https://mobile.twitter.com/josevalim/status/1535008937640181760)
- A low-code experiment: using Retool, Airbyte, and Supabase to bulk identify and fix product issues in Shopify. [Blog](https://www.galenking.com/experimentations-using-retool-to-bulk-identify-and-fix-product-issues-in-shopify/)
- Build a Flutter app with Very Good CLI and Supabase. [Tutorial](https://verygood.ventures/blog/flutter-app-very-good-cli-supabase)
- Replicache's guide for deploying on Vercel and Supabase. [Guide](https://doc.replicache.dev/deploy-vercel-supabase)
- Using Edge Functions in Supabase: A complete guide by LogRocket. [Blog post.](https://blog.logrocket.com/using-edge-functions-supabase-complete-guide/)
- We've started a new Youtube Series: [SupabaseTips](https://www.youtube.com/watch?v=Jx8unDjLaKg&list=PL5S4mPUpp4OtesRpEKe2zdNzClH-6chOE).
- The complete saga of Jason Lengstorf building a realtime app with Supabase. [Part 1](https://www.youtube.com/watch?v=bcE_X2N1B40), [Part 2](https://www.youtube.com/watch?v=eNVCjPbsWPo), [Part 3](https://www.youtube.com/watch?v=HFi89g21DVE).
- NuxtSupabase reached 100 stars on GitHub and it has a new doc. [Tweet](https://twitter.com/baptistelprx/status/1535157225722941442)
- How to build a performant dynamic dashboard from your Supabase data in less than 15 minutes using Cube and React. [Tutorial](https://www.notion.so/Beta-Update-June-2022-bfedb1d17b264f2ca7ccfffb1cc581f9)
- Supabase for Persistence & Server-to-Client Push in Vanilla HTML/JS Web App. [Tutorial](https://javascript.plainenglish.io/supabase-for-persistence-and-server-to-client-push-in-vanilla-html-javascript-web-application-a-99ddd9e4e307)
- Arengu now lets you authenticate users with Supabase in your signup and login processes. [Blog](https://www.arengu.com/blog/product-update-june-2022#signup-and-auto-login-with-supabase)
- Build a Full-Stack App with Next.js, Supabase & Prisma. [Course](https://themodern.dev/courses/build-a-fullstack-app-with-nextjs-supabase-and-prisma-322389284337222224)
- Jon Meyers looks at using Row Level Security policies to limit the number of rows a particular user can insert into a table. [Article](https://jonmeyers.io/blog/using-a-row-level-security-policy-to-limit-the-number-of-rows-inserted-per-user)
- How to use Realtime Functionality in Supabase Postgress Database. [Tutorial](https://nextdev1111.hashnode.dev/how-to-use-realtime-functionality-in-supabase-postgress-database)
- A brand new Flutter Tutorial Series. The first post: [Building a realtime Flutter chat app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app).
- Python, Metabase, and Supabase: [Part 1](https://supabase.com/blog/loading-data-supabase-python) and [Part 2](https://supabase.com/blog/visualizing-supabase-data-using-metabase).

## Singapore CityJS [\#](https://supabase.com/blog/beta-update-june-2022\#singapore-cityjs)

> Excited for some awesome talks by
> [@supabase](https://twitter.com/supabase?ref_src=twsrc%5Etfw)
> community members
> [@estee\_tey](https://twitter.com/estee_tey?ref_src=twsrc%5Etfw)
> and
> [@sam\_poder](https://twitter.com/sam_poder?ref_src=twsrc%5Etfw), as well as Singapore
> legends like
> [@swyx](https://twitter.com/swyx?ref_src=twsrc%5Etfw) and
> [@serrynaimo](https://twitter.com/serrynaimo?ref_src=twsrc%5Etfw)!
>
> And even a free JS community meetup with a little Edge Functions workshop!
>
> Check out the schedule 👉
> [https://t.co/T6CAyjpWSa](https://t.co/T6CAyjpWSa) [https://t.co/SNCAAQeCmz](https://t.co/SNCAAQeCmz)
>
> — Thor 雷神 ⚡️in Singapore 🇸🇬 (@thorwebdev)
>
>  [July 5, 2022](https://twitter.com/thorwebdev/status/1544198199912841216?ref_src=twsrc%5Etfw)

If you liked Thor’s MC work during Launch Week, you can’t miss him at [CityJS Singapore](https://singapore.cityjsconf.org/). He will also be hosting a live coding workshop on day 1, and our SupaSquad member [Estee](https://twitter.com/estee_tey) will present: [Building Billy with Supabase](https://singapore.cityjsconf.org/speaker/6I8t2MoYGJ915dtK7jXglY).

## We’re hiring [\#](https://supabase.com/blog/beta-update-june-2022\#were-hiring)

Come join one of the fastest growing open source projects ever 🤗

- [Lead Edge Functions Engineer](https://boards.greenhouse.io/supabase/jobs/4568813004)
- [Lead Storage Engineer](https://boards.greenhouse.io/supabase/jobs/4568811004)
- [Support Engineers](https://boards.greenhouse.io/supabase/jobs/4191650004)
- [View all our openings](https://boards.greenhouse.io/supabase)

* * *

We hit 50k stars! Thanks to all our [stargazers](https://github.com/supabase/supabase/stargazers).

![Community](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fstars-june-2022.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

* * *

## Meme Zone [\#](https://supabase.com/blog/beta-update-june-2022\#meme-zone)

If you made it this far in the blog post you deserve a treat. [Follow us on Twitter](https://twitter.com/supabase) for more.

![Supabase meme june 2022](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fmeme.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Get started [\#](https://supabase.com/blog/beta-update-june-2022\#get-started)

- Start using Supabase today: **[supabase.com/dashboard](https://supabase.com/dashboard/)**
- Make sure to **[star us on GitHub](https://github.com/supabase/supabase)**
- Follow us **[on Twitter](https://twitter.com/supabase)**
- Subscribe to our **[YouTube channel](https://www.youtube.com/c/supabase)**
- Become a **[sponsor](https://github.com/sponsors/supabase)**

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-june-2022&text=Supabase%20Beta%20June%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-june-2022&text=Supabase%20Beta%20June%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-june-2022&t=Supabase%20Beta%20June%202022)

[Last post\\
\\
**Revamped Auth Helpers for Supabase (with SvelteKit support)** \\
\\
13 July 2022](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support)

[Next post\\
\\
**Flutter Tutorial: building a Flutter chat app** \\
\\
30 June 2022](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Auth Helpers for Next.js revamped](https://supabase.com/blog/beta-update-june-2022#auth-helpers-for-nextjs-revamped)
- [Unlimited free projects](https://supabase.com/blog/beta-update-june-2022#unlimited-free-projects)
- [Create projects from the Supabase CLI](https://supabase.com/blog/beta-update-june-2022#create-projects-from-the-supabase-cli)
- [Enable realtime for your table via the table editor](https://supabase.com/blog/beta-update-june-2022#enable-realtime-for-your-table-via-the-table-editor)
- [Quick product announcements](https://supabase.com/blog/beta-update-june-2022#quick-product-announcements)
- [Supabase Happy Hour](https://supabase.com/blog/beta-update-june-2022#supabase-happy-hour)
- [Matterday](https://supabase.com/blog/beta-update-june-2022#matterday)
- [Made with Supabase](https://supabase.com/blog/beta-update-june-2022#made-with-supabase)
- [Community highlights (extended)](https://supabase.com/blog/beta-update-june-2022#community-highlights-extended)
- [Singapore CityJS](https://supabase.com/blog/beta-update-june-2022#singapore-cityjs)
- [We’re hiring](https://supabase.com/blog/beta-update-june-2022#were-hiring)
- [Meme Zone](https://supabase.com/blog/beta-update-june-2022#meme-zone)
- [Get started](https://supabase.com/blog/beta-update-june-2022#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-june-2022&text=Supabase%20Beta%20June%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-june-2022&text=Supabase%20Beta%20June%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-june-2022&t=Supabase%20Beta%20June%202022)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)