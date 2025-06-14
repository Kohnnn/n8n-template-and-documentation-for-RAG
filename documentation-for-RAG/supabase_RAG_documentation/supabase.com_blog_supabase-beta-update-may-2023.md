---
url: "https://supabase.com/blog/supabase-beta-update-may-2023"
title: "Supabase Beta May 2023"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta May 2023

09 Jun 2023

•

5 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta May 2023](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-09-06-may-2023-beta-update%2Fmonthly-update-may-2023.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We have two big product announcements this month, new integrations with products we love, and exciting highlights from our amazing community.

We're also absolutely stoked to let you know that we've hit a massive milestone: [50k GitHub Stars](https://github.com/supabase/supabase)! 🌟. Much love to everyone who helped us get there!

## Supabase Vector: the open source Vector Toolkit for Postgres [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#supabase-vector-the-open-source-vector-toolkit-for-postgres)

![Supabase Vector: the open source Vector Toolkit for Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-09-06-may-2023-beta-update%2Fsupabase-vector.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Storing vector embeddings in Postgres with `pgvector` is becoming increasingly popular for AI applications, so we're building out a collection of tools to store, index, and query embeddings at scale.

[Supabase Vector](https://supabase.com/vector)

## Vault is now available for all projects [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#vault-is-now-available-for-all-projects)

![Vault is now available for all projects](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-09-06-may-2023-beta-update%2Fvault.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Vault is a Postgres extension and accompanying Supabase UI that makes it safe and easy to store encrypted secrets and other data in your database.

[Learn how to use Vault.](https://supabase.com/docs/guides/database/vault)

## Auth Helpers now include server-side Auth and full support for the Next.js App Router [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#auth-helpers-now-include-server-side-auth-and-full-support-for-the-nextjs-app-router)

![Auth Helpers now include server-side Auth and full support for the Next.js App Router](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-09-06-may-2023-beta-update%2Fauth-helpers-nextjs-with-nextjs13.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We have updated the [Next.js Auth Helpers package](https://github.com/supabase/auth-helpers) to make it available across the client and server of the App Router. They also now implement server-side auth by default with PKCE - meaning the entire auth flow is now possible server-side.

[Updated docs](https://supabase.com/docs/guides/auth/auth-helpers/nextjs)

[Video course](https://www.youtube.com/playlist?list=PL5S4mPUpp4OtMhpnp93EFSo42iQ40XjbF)

## Improving our dashboard with user feedback [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#improving-our-dashboard-with-user-feedback)

As we plan the next few months of Dashboard development, we're reaching out to users to see all the different ways people use the Dashboard in their work.

Last month, we opened up a public [RFC for the Dashboard SQL Editor](https://github.com/orgs/supabase/discussions/14206). It's been amazing to see how people use this tool to build their projects. If you're a heavy user of the SQL Editor, we'd love to get your feedback.

We also started doing user interviews to understand how users use the Dashboard. Our goal is to build the best possible Dashboard for all of our users, and you can help! Reach out to [Terry](https://twitter.com/saltcod) you would like to share your experience.

## Quick product announcements [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#quick-product-announcements)

- \[Auth\] You can now use Turnstile as a Captcha provider. [Doc](https://supabase.com/docs/guides/auth/auth-captcha#sign-up-for-captcha)

- \[Auth\] How to send a password reauthentication nonce. [Doc](https://supabase.com/docs/reference/javascript/auth-resend)

- \[Dashboard\] Supabase Wrappers UI that supports pulling data in from Firebase, Stripe, S3, and Clickhouse. [Create a Wrapper](https://supabase.com/dashboard/project/_/database/wrappers)

- \[Edge Functions\] Support for deploying all Edge Functions via CLI. [Doc](https://supabase.com/docs/guides/functions/quickstart#deploy-all-functions)

- \[Edge Functions\] Custom domains and vanity domains support for Edge Functions. [PR](https://github.com/supabase/supabase-js/pull/778)

- \[Storage\] Image Transformation is now out of Beta. [Doc](https://supabase.com/docs/guides/storage/serving/image-transformations)

- \[Postgres Extensions\] pg\_cron 1.5.2 (new projects only) now supports sub-minute schedules. [PR](https://github.com/citusdata/pg_cron)


## AI resources & examples [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#ai-resources--examples)

![AI resources & examples](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-09-06-may-2023-beta-update%2Fai-resources.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The whole team has been busy building with ChatGPT, pgvector, and creating valuable resources so the community can unleash their imagination and build great AI apps faster than ever.

- [Supabase Vecs: a vector client for Postgres](https://supabase.com/blog/vecs)

- [ChatGPT plugins now support Postgres & Supabase](https://supabase.com/blog/chatgpt-plugins-support-postgres)

- [Building ChatGPT Plugins with Supabase Edge Runtime](https://supabase.com/blog/building-chatgpt-plugins-template)

- [Using AI to Generate a PostgreSQL Database for Tony Hawk’s Pro Skater 2 with Zero SQL Experience](https://www.youtube.com/watch?v=ffdUZbYov9g)


## Flutter Hackathon winners [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#flutter-hackathon-winners)

![Flutter Hackathon winners](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-09-06-may-2023-beta-update%2Fflutter-hackathon-winners.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We hosted our first-ever Flutter Hackathon, in partnership with FlutterFlow and Invertase. Samuel Philip built [Syno](https://github.com/ineffablesam/Syno), a YouTube summarizer app that uses OpenAI, and won the limited Flutter-themed Supabase keyboard 💙, and there are tons of other great open source projects to check out.

[Read the blog post with all the winners](https://supabase.com/blog/flutter-hackathon-winners)

[Watch the live announcement with Pooja and Majid](https://www.youtube.com/watch?v=AazB9mQetkw)

## Made with Supabase [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#made-with-supabase)

![Made with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-09-06-may-2023-beta-update%2Fquivr-second-brain.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Quivr](https://github.com/stangirard/quivr), your second brain in the cloud, utilizes the power of GenerativeAI to store and retrieve unstructured information. Built by [Stan Girard](https://twitter.com/_StanGirard) using LangChain, OpenAI, and Supabase Vector.

Bonus track: make sure to also check out [ChartGPT](https://www.chartgpt.dev/), which just launched V2.0 with a big UI refresh ✨

## Extended Community Highlights [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#extended-community-highlights)

![Community](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fcommunity.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

- We worked with Cloudflare on a new integration that makes it super easy to connect your Supabase database from Cloudflare Workers. [Doc](https://supabase.com/partners/integrations/cloudflare-workers)

- Deno Fresh Starter: ChatGPT-style doc search. [Blog post](https://deno.com/blog/build-chatgpt-doc-search-with-supabase-fresh)

- Vector Similarity Search in Bubble using Supabase Vector. [Integration](https://medium.com/@ivbran/vector-similarity-search-in-bubble-io-using-supabase-and-pgvector-672a2e69fbc7)

- Supabase RLS with Typescryp.

- How Supabase does performance benchmarking using k6, with Egor Romanov. [Webinar](https://www.youtube.com/watch?v=VcrQidYBjEg)

- Code With Antonio - Spotify Clone with Next.js Auth Helpers. [Video tutorial](https://www.youtube.com/watch?v=2aeMRB8LL4o)

- Our friends from 1Password announced Passage and wrote an integration guide. [Doc](https://supabase.com/partners/integrations/passageidentity)

- How to create a chatbot with OpenAI's API: a conceptual cheat sheet. [Tutorial](https://dev.to/farez/how-to-create-a-chatbot-with-openais-api-a-conceptual-cheat-sheet-2o5p)

- How to Implement Role-Based Access with Supabase. [Tutorial](https://dev.to/akkilah/how-to-implement-role-based-access-with-supabase-3a2)

- Rodrigo Mansueli, Developer Support Enginere here at Supabase, started a blog that is starting to become go-to resource for leveling up with Supabase and Postgres. [Blog](https://blog.mansueli.com/)

- Building a mobile authentication flow for your SaaS with Expo and Supabase. [Tutorial](https://blog.spirokit.com/building-a-mobile-authentication-flow-for-your-saas-with-expo-and-supabase)

- Huntabyte released a new course: Modern SaaS Apps with SvelteKit, Stripe, & Supabase. [Full Course](https://courses.huntabyte.com/modern-saas)

- Setting Up n8n on Railway with Postgres Database. [Tutorial](https://nesin.io/blog/host-n8n-railway-external-database)


## We're hiring [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#were-hiring)

Great opportunity to be an early and key member of our Customer Success team. Come join one of the fastest-growing open source projects ever 🤗

- [Customer Solution Architect](https://boards.greenhouse.io/supabase/jobs/4888237004)

## Meme Zone [\#](https://supabase.com/blog/supabase-beta-update-may-2023\#meme-zone)

As always, one of our favorite memes from last month. [Follow us on Twitter](https://twitter.com/supabase) for more.

![Meme May 2023](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-09-06-may-2023-beta-update%2Fbeta-update-may-2023-meme.jpeg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-may-2023&text=Supabase%20Beta%20May%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-may-2023&text=Supabase%20Beta%20May%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-may-2023&t=Supabase%20Beta%20May%202023)

[Last post\\
\\
**Native Mobile Auth Support for Google and Apple Sign in** \\
\\
27 June 2023](https://supabase.com/blog/native-mobile-auth)

[Next post\\
\\
**Flutter Hackathon Winners** \\
\\
29 May 2023](https://supabase.com/blog/flutter-hackathon-winners)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Supabase Vector: the open source Vector Toolkit for Postgres](https://supabase.com/blog/supabase-beta-update-may-2023#supabase-vector-the-open-source-vector-toolkit-for-postgres)
- [Vault is now available for all projects](https://supabase.com/blog/supabase-beta-update-may-2023#vault-is-now-available-for-all-projects)
- [Auth Helpers now include server-side Auth and full support for the Next.js App Router](https://supabase.com/blog/supabase-beta-update-may-2023#auth-helpers-now-include-server-side-auth-and-full-support-for-the-nextjs-app-router)
- [Improving our dashboard with user feedback](https://supabase.com/blog/supabase-beta-update-may-2023#improving-our-dashboard-with-user-feedback)
- [Quick product announcements](https://supabase.com/blog/supabase-beta-update-may-2023#quick-product-announcements)
- [AI resources & examples](https://supabase.com/blog/supabase-beta-update-may-2023#ai-resources--examples)
- [Flutter Hackathon winners](https://supabase.com/blog/supabase-beta-update-may-2023#flutter-hackathon-winners)
- [Made with Supabase](https://supabase.com/blog/supabase-beta-update-may-2023#made-with-supabase)
- [Extended Community Highlights](https://supabase.com/blog/supabase-beta-update-may-2023#extended-community-highlights)
- [We're hiring](https://supabase.com/blog/supabase-beta-update-may-2023#were-hiring)
- [Meme Zone](https://supabase.com/blog/supabase-beta-update-may-2023#meme-zone)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-may-2023&text=Supabase%20Beta%20May%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-may-2023&text=Supabase%20Beta%20May%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-may-2023&t=Supabase%20Beta%20May%202023)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)