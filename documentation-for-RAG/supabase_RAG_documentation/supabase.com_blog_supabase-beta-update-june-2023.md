---
url: "https://supabase.com/blog/supabase-beta-update-june-2023"
title: "Supabase Beta June 2023"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta June 2023

06 Jul 2023

•

4 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta June 2023](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-07-06-beta-update-june%2Fbeta-update-june-2023.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Guess what? We've got some sizzling updates for you this month! Our partnership with Mozilla, Native mobile auth support, revamped billinx experience, real-time debugging magic, and great stuff from the community. Dive in now 🤿

## Mozilla uses Supabase to build AI Help. [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#mozilla-uses-supabase-to-build-ai-help)

![Mozilla uses Supabase to build AI Help.](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjuly2023%2Fmdn_search.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

MDN is one of the richest sources of developer documentation on the internet, and it just received an upgrade. Mozilla built AI Help, an AI chatbot to help with search and discovery. Mozilla chose Supabase Vector and OpenAI to power their new tool which you can try for free.

[Read the announcement](https://developer.mozilla.org/en-US/blog/introducing-ai-help/)

## Native Mobile Auth Support for Google and Apple Sign in [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#native-mobile-auth-support-for-google-and-apple-sign-in)

![Native Mobile Auth Support for Google and Apple Sign in](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjuly2023%2Fnative-phone-support.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase Auth now has full native support for Sign in with Apple and Google, which means it can now be used with one-tap sign in methods like Sign in with Apple JS, Sign in with Google for Web, or even in Chrome extensions.

[Learn more](https://supabase.com/blog/native-mobile-auth)

## Supabase CLI: what is new? [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#supabase-cli-what-is-new)

![Supabase CLI: what is new?](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjuly2023%2Fsupabase-cli-cache-hi.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It’s been a busy month for the Supabase CLI. We have added a tonne of new features:

- **Migrations:** view all your migrations inside the Dashboard with the SQL [code that was executed](https://github.com/supabase/cli/pull/1181).
- **Functions:** the CLI now [serves all Functions](https://github.com/supabase/cli/pull/1171) when developing locally.
- **Database monitoring**: we’ve added a `usage` flag for [monitoring key Postgres statistics](https://github.com/supabase/cli/pull/1070).

[See all updates](https://github.com/supabase/cli/releases)

## Revamped billing experience [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#revamped-billing-experience)

![Revamped billing experience](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjuly2023%2Fbilling.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We have made huge improvements to the billing tooling inside Supabase Studio, including:

- Easy monitoring of current usage, overage, and plan limits.
- Streamlined subscription management for upgrades or downgrades.
- Detailed usage billing breakdowns and compute instance specifications.
- And more!

[New subscription page](https://app.supabase.com/org/_/billing) \| [New usage page](https://app.supabase.com/org/_/usage)

## Login with Kakao [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#login-with-kakao)

![Login with Kakao](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjuly2023%2Fkakao-social-login.png%3Ft%3D2023-07-06T13%253A26%253A11.108Z&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Added the popular social platform Kakao as new social provider. Allow your users to effortlessly sign in using their Kakao accounts and make authentication a breeze while expanding your app's reach to a wider audience.

[Login with Kakao](https://supabase.com/docs/guides/auth/social-login/auth-kakao)

## Quick product updates [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#quick-product-updates)

- \[ **Postgres Tooling**\] Implemented parallel Index build in regular and recovery state into OrioleDB. \[ [PR](https://github.com/orioledb/orioledb/commit/8c4a50175cf39a97ac0555ea3f969fe7e40dba21)\]
- \[ **Edge Functions**\] Edge Functions troubleshooting guide. \[ [Doc](https://supabase.com/docs/guides/functions/troubleshooting)\]
- \[ **Storage**\] Object id is now returned in the response when uploading an object. \[ [PR](https://github.com/supabase/storage-api/pull/332)\]
- \[ **Realtime**\] A new debugging tool to test your realtime endpoints together with your JWTs and Row Level Security policies. \[ [Realtime Inspector](https://realtime.supabase.com/inspector/new)\]
- \[ **Docs**\] A full guide on database partitions for developers looking to scale up. \[ [Guide](https://supabase.com/docs/guides/database/partitions)\]

## Made with Supabase [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#made-with-supabase)

![Chat Thing is Made with Supabase](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fchatting-ai.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Chat Thing](https://chatthing.ai/), is an innovative project that allows you to create AI chatbots using your existing data from Notion, uploaded files, websites and more. Built by [pixelhop](https://twitter.com/pixelhopio) using Vue, Nuxt, Railway, and Supabase for database, auth, and vector store.

## Extended Community Highlights [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#extended-community-highlights)

![Some of the faces from the community](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjuly2023%2Fflutter_auth.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

- Using Supabase with Cloudflare Workers. [Cloudflare TV](https://cloudflare.tv/event/using-supabase-with-cloudflare-workers/dgM90RgD)
- Build a Chatbot with Next.js, LangChain, OpenAI, and Supabase Vector. [Video Tutorial](https://www.youtube.com/watch?v=Tt45NrVIBn8)
- The refine open source Hackathon is in full swing. [Join now](https://discord.com/channels/@me/1118414473108148296/1123933930702262312)
- Flutter database and user authentication. [Video guide](https://www.youtube.com/watch?v=r7ysVtZ5Row)
- Google authentication with Expo & Supabase. [Tutorial](https://blog.spirokit.com/google-authentication-with-expo-supabase)
- Building Stripe integrations with Supabase. [Video](https://www.youtube.com/watch?v=D5kOnnB72WA)
- Build a Supabase + Drizzle-orm + Express backend. [Video Tutorial](https://www.youtube.com/watch?v=k0uC35J_xJ4)
- LogRocker blog: Authenticate React Applications: Supabase Auth. [Tutorial](https://blog.logrocket.com/authenticate-react-applications-supabase-auth/)
- Using Supabase Vault to store secrets. [Tutorial](https://makerkit.dev/blog/tutorials/supabase-vault)
- Nuxt + Supabase = Technology Stack of Dreams. [Blog post](https://dev.to/jacobandrewsky/nuxt-supabase-technology-stack-of-dreams-4dop)
- Build a to-do app with toddle and Supabase. [Video](https://www.youtube.com/watch?v=SHJ3EadcrgY)

## We're Hiring [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#were-hiring)

Come join one of the fastest-growing open source projects ever:

- [Front-End Developer (o11y focus)](https://boards.greenhouse.io/supabase/jobs/4910374004)
- [Rust developer](https://boards.greenhouse.io/supabase/jobs/4917893004)

## ⚠️ Baking hot meme zone ⚠️ [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#%EF%B8%8F-baking-hot-meme-zone-%EF%B8%8F)

![Our favorite meme from June 2023](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjuly2023%2Fbeta-update-june-2023-meme.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Launch Week alert: save the date [\#](https://supabase.com/blog/supabase-beta-update-june-2023\#launch-week-alert-save-the-date)

![Launch Week 8 is announced - From Monday 07/08 till Friday 11/08](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fjuly2023%2Flw8-teaser.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-june-2023&text=Supabase%20Beta%20June%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-june-2023&text=Supabase%20Beta%20June%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-june-2023&t=Supabase%20Beta%20June%202023)

[Last post\\
\\
**What is new in PostgREST v11.1?** \\
\\
12 July 2023](https://supabase.com/blog/postgrest-11-1-release)

[Next post\\
\\
**Native Mobile Auth Support for Google and Apple Sign in** \\
\\
27 June 2023](https://supabase.com/blog/native-mobile-auth)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Mozilla uses Supabase to build AI Help.](https://supabase.com/blog/supabase-beta-update-june-2023#mozilla-uses-supabase-to-build-ai-help)
- [Native Mobile Auth Support for Google and Apple Sign in](https://supabase.com/blog/supabase-beta-update-june-2023#native-mobile-auth-support-for-google-and-apple-sign-in)
- [Supabase CLI: what is new?](https://supabase.com/blog/supabase-beta-update-june-2023#supabase-cli-what-is-new)
- [Revamped billing experience](https://supabase.com/blog/supabase-beta-update-june-2023#revamped-billing-experience)
- [Login with Kakao](https://supabase.com/blog/supabase-beta-update-june-2023#login-with-kakao)
- [Quick product updates](https://supabase.com/blog/supabase-beta-update-june-2023#quick-product-updates)
- [Made with Supabase](https://supabase.com/blog/supabase-beta-update-june-2023#made-with-supabase)
- [Extended Community Highlights](https://supabase.com/blog/supabase-beta-update-june-2023#extended-community-highlights)
- [We're Hiring](https://supabase.com/blog/supabase-beta-update-june-2023#were-hiring)
- [⚠️ Baking hot meme zone ⚠️](https://supabase.com/blog/supabase-beta-update-june-2023#%E2%9A%A0%EF%B8%8F-baking-hot-meme-zone-%E2%9A%A0%EF%B8%8F)
- [Launch Week alert: save the date](https://supabase.com/blog/supabase-beta-update-june-2023#launch-week-alert-save-the-date)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-june-2023&text=Supabase%20Beta%20June%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-june-2023&text=Supabase%20Beta%20June%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-june-2023&t=Supabase%20Beta%20June%202023)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)