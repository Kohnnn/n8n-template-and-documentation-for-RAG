---
url: "https://supabase.com/blog/supabase-beta-january-2023"
title: "Supabase Beta January 2023"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta January 2023

08 Feb 2023

•

5 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta January 2023](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-08-january-beta-update%2Fsupabase-beta-update-january-2023.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We have so much good stuff this month that it’s hard to fit in a single blog post 🚢.

We’ve got some new Postgres extensions, GraphQL updates, changes to Edge Functions, and more!

## Storing OpenAI embeddings in Postgres with pgvector [\#](https://supabase.com/blog/supabase-beta-january-2023\#storing-openai-embeddings-in-postgres-with-pgvector)

![Storing OpenAI embeddings in Postgres with pgvector](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-08-january-beta-update%2Fpgvector.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

pgvector is a popular PostgreSQL extension for storing embeddings and performing vector similarity search. It was one of the most requested extensions by the AI/ML community and is now available thanks to [gregnr](https://github.com/gregnr).

[Read the announcement](https://supabase.com/blog/openai-embeddings-postgres-vector)

## Meet Supabase Clippy: ChatGPT for Docs [\#](https://supabase.com/blog/supabase-beta-january-2023\#meet-supabase-clippy-chatgpt-for-docs)

![Meet Supabase Clippy: ChatGPT for Docs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-08-january-beta-update%2Fchatgpt-for-supabase-docs.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Greg wasted no time and took pgvector for a spin, he combined it with OpenAI to build Supabase Clippy, a next-generation doc search. The first implementation is a 1-week MVP and fully open source, so you can build on top of it.

- [Read the blog post](https://supabase.com/blog/chatgpt-supabase-docs)
- [Watch the video tutorial](https://www.youtube.com/watch?v=Yhtjd7yGGGA)

## Client library reference: Python and C\# [\#](https://supabase.com/blog/supabase-beta-january-2023\#client-library-reference-python-and-c)

![Client library reference: Python and C#](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-08-january-beta-update%2Freferences.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We have released extensive reference docs for C# and Python, detailing every object and method. What are you going to build?

- [C# Client Library](https://supabase.com/docs/reference/csharp/)
- [Python Client Library](https://supabase.com/docs/reference/python/initializing)

## pg\_graphql now supports Views, Materialized Views, and Foreign Tables [\#](https://supabase.com/blog/supabase-beta-january-2023\#pg_graphql-now-supports-views-materialized-views-and-foreign-tables)

![pg_graphql now supports Views, Materialized Views, and Foreign Tables](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-08-january-beta-update%2Fpg-graphql.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Views, Materialized Views, and Foreign Tables are three database objects that provide a powerful way to access and organize and transform data without duplication.

[Read the docs](https://supabase.github.io/pg_graphql/views/)

## Automatic WebP detection for Image Transformation [\#](https://supabase.com/blog/supabase-beta-january-2023\#automatic-webp-detection-for-image-transformation)

![Automatic WebP detection for Image Transformation](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-08-january-beta-update%2Fimage-transformation.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

WebP is a modern image format that provides superior lossless and lossy compression for images on the web. We are enabling format conversion by default for anyone who has Image Transformations. You can opt out by including format: origin in the transformation parameters.

[Read the docs](https://supabase.com/docs/guides/storage/serving/image-transformations#automatic-image-optimisation-webp)

## Quick product updates [\#](https://supabase.com/blog/supabase-beta-january-2023\#quick-product-updates)

-  Postgres Extension: Another powerful and time-tested extension, pg\_repack, is added to Supabase. [\[PR\]](https://github.com/supabase/postgres/pull/492)

- Auth: Multi-tab session support using the new browser BroadcastChannel API. If a user logs out on one tab, they will now be logged out on all tabs. [\[PR\]](https://github.com/supabase/gotrue-js/pull/566)

- Postgres: Superior speed with lz4 database compression. [\[PR\]](https://github.com/supabase/postgres/pull/490)

- Postgres: Use ICU locales and collations for text attribute ordering in database queries. [\[PR\]](https://github.com/supabase/postgres/pull/491)

- Docs: New guide on scheduling functions with pg\_cron. [\[Guide\]](https://supabase.com/docs/guides/functions/schedule-functions)

- Edge Functions: You can now download source codes of deployed edge functions from the CLI. [\[Doc\]](https://supabase.com/docs/reference/cli/supabase-functions-download)

- Edge Functions: building a Discord Slash Bot. [\[Video Tutorial\]](https://www.youtube.com/watch?v=J24Bvo_m7DM)

## Deploy Supabase on DigitalOcean [\#](https://supabase.com/blog/supabase-beta-january-2023\#deploy-supabase-on-digitalocean)

![Deploy Supabase on DigitalOcean](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-08-january-beta-update%2Fself-host-supabase-digital-ocean.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We teamed up with DigitalOcean to level up self-hosted Supabase. This guide shows how to host Supabase on DigitalOcean using Sendgrid, Packer, and Terraform. More collaborations coming soon!

[Get started](https://docs.digitalocean.com/developer-center/hosting-supabase-on-digitalocean/).

## 45k Github stars (and counting!) [\#](https://supabase.com/blog/supabase-beta-january-2023\#45k-github-stars-and-counting)

![45k Github stars (and counting!)](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-08-january-beta-update%2Fgithub-45k.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We hit two big milestones: 45k stars and Supabase is one the top 200 most-popular repos on Github 💥

Massive thanks to the community for all the support 👁️⚡️👁️

[Supabase Repo.](https://github.com/supabase/supabase)

## Made with Supabase [\#](https://supabase.com/blog/supabase-beta-january-2023\#made-with-supabase)

![Made with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-12-07-november-beta-update%2Fmadewithsupabase.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[supermeme.ai](https://www.supermeme.ai/) \| Two things that we are fans of are memes and AI. Just describe your thoughts and let AI create original memes for you. Available in 110+ languages!

Discover other great projects: [Made with Supabase](https://www.madewithsupabase.com/).

## Extended Community Highlights [\#](https://supabase.com/blog/supabase-beta-january-2023\#extended-community-highlights)

![Community](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fcommunity.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

- JWT Helper for Supabase by Zuplo. [Tool](https://zuplo.com/blog/2023/01/05/supabase-jwt-auth-helper/)

- ClickHouse and PostgreSQL - a Match Made in Data Heaven - Part 2. [Blog Post](https://clickhouse.com/blog/migrating-data-between-clickhouse-postgres-part-2)
- Building a Startup from Scratch: My Mistakes as CTO. [Blog Post](https://egor-romanov.medium.com/building-a-startup-from-scratch-my-mistakes-as-cto-b20b463e0058)
- We are sponsoring TreeHacks, Stanford University's premier hackathon and one of the largest hackathons in the USA. [Hackathon](https://www.treehacks.com/)
- Set up a Svelte to-do list on self-hosted Supabase + authentication. [Tutorial](https://blog.cpbprojects.me/set-up-a-svelte-todo-list-on-self-hosted-supabase-email-sign-up-google-facebook-auth-host-on-github-pages)
- Vercel wrote a case study about how much we love TurboRepo (and Vercel in general 🖤). [Case Study](https://vercel.com/customers/how-supabase-elevated-their-developer-experience-with-turborepo)
- A Very Basic Scraper/Aggregator Site in Next.js with Go Cloud Functions and Supabase. [Article](https://chriscoyier.net/2023/01/23/a-very-basic-scraper-aggregator-site-in-next-js-with-go-cloud-functions-and-supabase/)
- Supabase CDC Webhooks to Memphis REST Gateway. [Article](https://memphis.dev/blog/supabase-cdc-webhooks-to-memphis-rest-gateway/)
- How I Replaced Revue With a Custom-Built Newsletter Service Using Nuxt 3, Supabase, Serverless, and Amazon SES. [Article](https://mokkapps.de/blog/how-i-replaced-revue-with-a-custom-built-newsletter-service-using-nuxt-3-supabase-serverless-and-amazon-ses/)
- Nuxt 3, Tailwind, and Supabase Crash Course. [Video Course](https://www.youtube.com/watch?v=A-G6lPHctPs)
- WhatsApp in React Native. [Part 1](https://dev.to/jacksbridger/whatsapp-ui-in-react-native-part-1-4nbm), [Part 2](https://dev.to/nsmet/chat-backend-with-supabase-socketio-55nn), [Part 3](https://dev.to/jacksbridger/whatsapp-in-react-native-part-3-1gmf)
- Distributed GraphQL with Hasura and Supabase. [Docs](https://www.section.io/docs/tutorials/distributed-apis/distributed-hasura-supabase/)

## We're Hiring [\#](https://supabase.com/blog/supabase-beta-january-2023\#were-hiring)

Come join one of the fastest-growing open source projects ever 🤗

- [Integrations / Marketplace Lead](https://boards.greenhouse.io/supabase/jobs/4775849004)

- [Cloud Platform / Site Reliability Engineer](https://boards.greenhouse.io/supabase/jobs/4307459004)

- [Social Media and Community Manager](https://boards.greenhouse.io/supabase/jobs/4777008004)

We've redesigned our [Careers page](https://supabase.com/careers) to better reflect our mission, values, and culture.

## Meme Zone [\#](https://supabase.com/blog/supabase-beta-january-2023\#meme-zone)

As always, one of our favorite memes from last month. [Follow us on Twitter](https://twitter.com/supabase) for more.

![Best meme from January 2023](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-08-january-beta-update%2Fbeta-update-january-meme.jpeg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

See you next month!

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2023&text=Supabase%20Beta%20January%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2023&text=Supabase%20Beta%20January%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2023&t=Supabase%20Beta%20January%202023)

[Last post\\
\\
**How to build a real-time multiplayer game with Flutter Flame** \\
\\
14 February 2023](https://supabase.com/blog/flutter-real-time-multiplayer-game)

[Next post\\
\\
**Supabase Clippy: ChatGPT for Supabase Docs** \\
\\
7 February 2023](https://supabase.com/blog/chatgpt-supabase-docs)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Storing OpenAI embeddings in Postgres with pgvector](https://supabase.com/blog/supabase-beta-january-2023#storing-openai-embeddings-in-postgres-with-pgvector)
- [Meet Supabase Clippy: ChatGPT for Docs](https://supabase.com/blog/supabase-beta-january-2023#meet-supabase-clippy-chatgpt-for-docs)
- [Client library reference: Python and C#](https://supabase.com/blog/supabase-beta-january-2023#client-library-reference-python-and-c)
- [pg\_graphql now supports Views, Materialized Views, and Foreign Tables](https://supabase.com/blog/supabase-beta-january-2023#pg_graphql-now-supports-views-materialized-views-and-foreign-tables)
- [Automatic WebP detection for Image Transformation](https://supabase.com/blog/supabase-beta-january-2023#automatic-webp-detection-for-image-transformation)
- [Quick product updates](https://supabase.com/blog/supabase-beta-january-2023#quick-product-updates)
- [Deploy Supabase on DigitalOcean](https://supabase.com/blog/supabase-beta-january-2023#deploy-supabase-on-digitalocean)
- [45k Github stars (and counting!)](https://supabase.com/blog/supabase-beta-january-2023#45k-github-stars-and-counting)
- [Made with Supabase](https://supabase.com/blog/supabase-beta-january-2023#made-with-supabase)
- [Extended Community Highlights](https://supabase.com/blog/supabase-beta-january-2023#extended-community-highlights)
- [We're Hiring](https://supabase.com/blog/supabase-beta-january-2023#were-hiring)
- [Meme Zone](https://supabase.com/blog/supabase-beta-january-2023#meme-zone)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2023&text=Supabase%20Beta%20January%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2023&text=Supabase%20Beta%20January%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2023&t=Supabase%20Beta%20January%202023)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)