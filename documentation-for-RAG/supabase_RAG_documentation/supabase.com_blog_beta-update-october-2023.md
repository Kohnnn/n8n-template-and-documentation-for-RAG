---
url: "https://supabase.com/blog/beta-update-october-2023"
title: "Supabase Beta October 2023"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta October 2023

06 Nov 2023

•

4 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta October 2023](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-06-october-beta-update%2Fmonthly-update-october-2023.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Last month we merged over 800 PRs from more than 100 contributors. If you want to play a part in building Supabase, check out our [core](https://github.com/supabase) and [community](https://github.com/supabase-community/) repos. More hands are always welcome, and no matter your framework of choice there are always interesting problems to work on.

Here are some of the major items we shipped during October…

## Server-Side Auth in Next.js 14 [\#](https://supabase.com/blog/beta-update-october-2023\#server-side-auth-in-nextjs-14)

![Server-Side Auth in Next.js 14](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Foctober2023%2F1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've released `@supabase/ssr`, which makes it super easy to use cookies for storing user sessions. We’ve updated `npx create-next-app -e with-supabase` to use `@supabase/ssr` and made it compatible with Next.js 14.

[Read the blog post](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14).

## pgvector vs Pinecone [\#](https://supabase.com/blog/beta-update-october-2023\#pgvector-vs-pinecone)

![pgvector vs Pinecone](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Foctober2023%2F2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

pgvector is becoming the vector store of choice for developers. We’ve put it to the test against Pinecone and found that it performs better on cost and query throughput, without sacrificing accuracy.

[See the full benchmarks](https://supabase.com/blog/pgvector-vs-pinecone)

## Manage storage buckets from the command line [\#](https://supabase.com/blog/beta-update-october-2023\#manage-storage-buckets-from-the-command-line)

![Manage storage buckets from the command line](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Foctober2023%2Fstorage-buckets-cli.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can now manage Storage buckets with the Supabase CLI:

- `supabase storage ls -r`: show all buckets and objects
- `supabase cp -r readme.md ss:///bucket`: upload local files to bucket
- `supabase cp -r ss:///bucket`: download objects from bucket
- `supabase rm -r ss:///bucket`: delete files from bucket

Managing Storage buckets with CLI works best if there are less than 100k objects in your bucket and each of them is smaller than 20MB. Reference docs are [here](https://supabase.com/docs/reference/cli/supabase-storage-ls).

## What's new in Supabase Studio? [\#](https://supabase.com/blog/beta-update-october-2023\#whats-new-in-supabase-studio)

![What's new in Supabase Studio?](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Foctober2023%2Fsupabase-studio.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase Studio is improved many times per day, here is some of what's new:

- Better error surfacing in SQL Editor. [\[PR\]](https://github.com/supabase/supabase/pull/18327)
- Break out auth rate limit fields into a separate page. [\[PR\]](https://github.com/supabase/supabase/pull/18265)
- Enumerated types management. [\[PR\]](https://github.com/supabase/supabase/pull/17953)
- New API side panel. [\[PR\]](https://github.com/supabase/supabase/pull/17880)
- Audit logs for organizations available on Team Plan.

[Check them out](https://supabase.com/dashboard/).

## Multi-factor Authentication in Supabase Studio [\#](https://supabase.com/blog/beta-update-october-2023\#multi-factor-authentication-in-supabase-studio)

![Multi-factor Authentication in Supabase Studio](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Foctober2023%2Fmfa-supabase-studio.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Secure your Supabase account with Multi-Factor Authentication. You can now add a time-based one-time password (TOTP), managed by apps such as 1Password, Authy, Google Authenticator or Apple's Keychain.

[Check out the doc](https://supabase.com/docs/guides/platform/multi-factor-authentication)

## Quick product announcements [\#](https://supabase.com/blog/beta-update-october-2023\#quick-product-announcements)

- \[Auth\] LinkedIn OIDC provider. [\[PR\]](https://github.com/supabase/supabase/pull/18225)
- \[Auth\] Use token to include the redirect URL in your email template. [\[PR\]](https://github.com/supabase/gotrue/pull/1276)
- \[pgvector\] Upgrade 0.5.1 (faster HNSW index builds). [\[Release\]](https://github.com/pgvector/pgvector/releases/tag/v0.5.1)
- \[Dashboard\] Scopes for OAuth apps. [\[PR\]](https://github.com/supabase/supabase/pull/17976)
- \[Postgres\] pg\_jsonschema upgrade 0.1.4 to 0.2.0. [\[Release\]](https://github.com/supabase/pg_jsonschema/releases/tag/v0.2.0)
- \[Supavisor\] Starts providing Docker Images. [\[Docker\]](https://hub.docker.com/r/supabase/supavisor/tags)
- \[GraphQL\] GraphQL user defined functions now supported following the pg\_graphql upgrade from 1.2.3 to 1.4.2. [\[Docs\]](https://supabase.github.io/pg_graphql/functions/)

## AI Content Storm [\#](https://supabase.com/blog/beta-update-october-2023\#ai-content-storm)

![AI Content Storm](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Foctober2023%2F4.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We compiled a looong list of AI examples and tutorials produced by the Supabase community. There is a wide variety of topics such as [Building an AI Coloring Book with Elixir](https://niklas.hashnode.dev/from-a-dream-to-reality-building-an-ai-coloring-book-with-elixir) and [Create your own ChatGPT in Dart](https://dartling.dev/create-your-own-chatgpt-in-dart-with-supabase-vector-and-openai).

[Read the blog post](https://dev.to/supabase/ai-ignites-the-rain-content-storm-is-back-kdl)

## Extended Community Highlights [\#](https://supabase.com/blog/beta-update-october-2023\#extended-community-highlights)

![Community Highlights](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsep7.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

- LottieFiles x Supabase Korea Meetup. [\[Apply to join\]](https://lu.ma/lottiekr_supabase_23)
- Sending authentication emails with Resend and Supabase. [\[Doc\]](https://resend.com/docs/knowledge-base/how-do-i-maximize-deliverability-for-supabase-auth-emails)
- Paul Copplestone's keynote at the AI Engineer Summit. [\[Video\]](https://www.youtube.com/live/qw4PrtyvJI0?feature=shared&t=10556)
- Using Expo and Supabase. [\[Doc\]](https://docs.expo.dev/guides/using-supabase/)
- We were part of Next.js Conf and chatted about the new announcements. [\[Video\]](https://www.youtube.com/watch?v=FdiX5rHS_0Y&t=3880s) \| [\[Twitter Space\]](https://twitter.com/i/spaces/1yoKMwNWbRjJQ?s=20)
- Offline-first React Native Apps with Expo, WatermelonDB, and Supabase. [Blog post](https://supabase.com/blog/react-native-offline-first-watermelon-db)
- Easy Deployment and Rollback of PostgreSQL Functions with Supabase. [Article](https://blog.mansueli.com/streamlining-postgresql-function-management-with-supabase)
- Supabase E2E testing just got so much easier. [Video](https://www.youtube.com/watch?v=JMJODiXFHBI)
- Cloud Storage using Supabase. Step-by-step Android tutorial. [Video](https://www.youtube.com/watch?v=BqxI7ViS_-M)
- Building Dynamic Web Apps: A Step-by-Step Guide to Supabase and Django Integration. [Guide](https://python.plainenglish.io/building-dynamic-web-apps-a-step-by-step-guide-to-supabase-and-django-integration-13d569a53f42)
- How to set up a Local Development Environment for Supabase. [Guide](https://aiherrera.medium.com/how-to-set-up-a-local-development-environment-for-supabase-dd80e16d050)

## Launch Week X [\#](https://supabase.com/blog/beta-update-october-2023\#launch-week-x)

![Launch Week X](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Foctober2023%2Flaunch-week-x.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Oh, and one more thing… this is definitely something you won’t want to miss. Mark your calendar!

## We are hiring [\#](https://supabase.com/blog/beta-update-october-2023\#we-are-hiring)

Come join one of the fastest-growing open source projects ever! 🤗

- [Technical Product Marketer](https://boards.greenhouse.io/supabase/jobs/5005843004)
- [Revenue Operations Lead](https://boards.greenhouse.io/supabase/jobs/5006313004)
- [Cloud Platform / Site Reliability Engineer](https://boards.greenhouse.io/supabase/jobs/5013075004)

## **⚠️ Baking hot meme zone ⚠️** [\#](https://supabase.com/blog/beta-update-october-2023\#%EF%B8%8F-baking-hot-meme-zone-%EF%B8%8F)

![Favorite meme from October 2023](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Foctober2023%2Fmeme-october-2023.png%3Ft%3D2023-11-06T15%253A12%253A17.052Z&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-october-2023&text=Supabase%20Beta%20October%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-october-2023&text=Supabase%20Beta%20October%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-october-2023&t=Supabase%20Beta%20October%202023)

[Last post\\
\\
**Getting started with React Native authentication** \\
\\
16 November 2023](https://supabase.com/blog/react-native-authentication)

[Next post\\
\\
**Supabase is now compatible with Next.js 14** \\
\\
1 November 2023](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Server-Side Auth in Next.js 14](https://supabase.com/blog/beta-update-october-2023#server-side-auth-in-nextjs-14)
- [pgvector vs Pinecone](https://supabase.com/blog/beta-update-october-2023#pgvector-vs-pinecone)
- [Manage storage buckets from the command line](https://supabase.com/blog/beta-update-october-2023#manage-storage-buckets-from-the-command-line)
- [What's new in Supabase Studio?](https://supabase.com/blog/beta-update-october-2023#whats-new-in-supabase-studio)
- [Multi-factor Authentication in Supabase Studio](https://supabase.com/blog/beta-update-october-2023#multi-factor-authentication-in-supabase-studio)
- [Quick product announcements](https://supabase.com/blog/beta-update-october-2023#quick-product-announcements)
- [AI Content Storm](https://supabase.com/blog/beta-update-october-2023#ai-content-storm)
- [Extended Community Highlights](https://supabase.com/blog/beta-update-october-2023#extended-community-highlights)
- [Launch Week X](https://supabase.com/blog/beta-update-october-2023#launch-week-x)
- [We are hiring](https://supabase.com/blog/beta-update-october-2023#we-are-hiring)
- [**⚠️ Baking hot meme zone ⚠️**](https://supabase.com/blog/beta-update-october-2023#%E2%9A%A0%EF%B8%8F-baking-hot-meme-zone-%E2%9A%A0%EF%B8%8F)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-october-2023&text=Supabase%20Beta%20October%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-october-2023&text=Supabase%20Beta%20October%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-october-2023&t=Supabase%20Beta%20October%202023)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)