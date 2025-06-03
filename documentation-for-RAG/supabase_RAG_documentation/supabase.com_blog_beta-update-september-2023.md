---
url: "https://supabase.com/blog/beta-update-september-2023"
title: "Supabase Beta September 2023"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta September 2023

04 Oct 2023

•

5 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta September 2023](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-10-04-beta-update-september%2Fmonthly-update-september-2023.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’ve come a long way since our first update email in April 2020. We’ve gone from 6 hosted databases on our platform to over 650,000 (and that doesn’t even include [database branches](https://supabase.com/blog/supabase-local-dev). As always we’ve had another hectic month of shipping fast, and community involvement in our [open source repos](https://github.com/supabase/supabase), meaning we can iterate on Supabase faster than ever. Here’s a small sample of some of the things we shipped during September…

## Broadcast realtime messages via REST API [\#](https://supabase.com/blog/beta-update-september-2023\#broadcast-realtime-messages-via-rest-api)

![Broadcast realtime messages via REST API](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsep1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can now broadcast Realtime messages to all your connected users by simply using a REST API call, removing the need to connect to a WebSocket. This will be especially useful with our Edge Functions!

[Broadcast docs](https://supabase.com/docs/guides/realtime/broadcast#send-messages-using-rest-calls)

## Supavisor is now used for connection pooling in all new projects [\#](https://supabase.com/blog/beta-update-september-2023\#supavisor-is-now-used-for-connection-pooling-in-all-new-projects)

![Supavisor is now used for connection pooling in all new projects](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsep2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Less than two months ago, we announced Supavisor, our own Postgres connection pooler that handles millions of connections. It’s now available in all new projects. You can continue using pgbouncer alongside Supavisor, however, it will be deprecated effective January 15th, 2024.

[Learn more](https://github.com/orgs/supabase/discussions/17817)

### Moving to IPV6 for Database Connection Strings [\#](https://supabase.com/blog/beta-update-september-2023\#moving-to-ipv6-for-database-connection-strings)

With IPv4 addresses becoming increasingly scarce and [cloud providers starting to charge](https://aws.amazon.com/blogs/aws/new-aws-public-ipv4-address-charge-public-ip-insights/) for it, we won’t be assigning IPv4 addresses to Supabase projects from January 15th, 2024. `[db.projectref.supabase.co](http://db.projectref.supabase.co)` will start resolving to a IPv6 address instead. If you plan on connecting to your database directly, you must ensure that your network can communicate over IPv6. Supavisor will continue to return IPv4 addresses, so you can update your applications to connect to Supavisor instead.

[Learn more](https://github.com/orgs/supabase/discussions/17817)

## New Foreign Data Wrapper: Airtable [\#](https://supabase.com/blog/beta-update-september-2023\#new-foreign-data-wrapper-airtable)

![New Foreign Data Wrapper: Airtable](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsep3.png%3Ft%3D2023-10-03T11%253A36%253A04.651Z&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Introducing the latest addition to our Wrappers lineup: Airtable! You can use it to query data from your Airtable bases and tables directly from Postgres:

`
select * from my_airtable_table;
# data from Airtable
`

[Read the Airtable Wrapper docs](https://supabase.com/docs/guides/database/extensions/wrappers/airtable) [Learn about Wrappers](https://supabase.com/blog/postgres-foreign-data-wrappers-rust)

## Supabase Studio's latest enhancements [\#](https://supabase.com/blog/beta-update-september-2023\#supabase-studios-latest-enhancements)

![Supabase Studio's latest enhancements](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsupabase-studio-json.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase Studio is under constant improvement, here is what’s new:

- Added UI support for cascade updates
- Improved JSON previewing and editing
- Button for toggling Realtime right from the Table Editor
- See View definition and open it in the SQL Editor to modify
- UI to view and unban IP addresses to manage banned IPs more conveniently
- Import CSV files at the table creation stage and a new button to download the table as CSV

[Try them out](https://supabase.com/dashboard/project/_)

## HNSW Support for Vecs + pgvector [\#](https://supabase.com/blog/beta-update-september-2023\#hnsw-support-for-vecs--pgvector)

![HNSW Support for Vecs + pgvector](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsupabase-vector%3Ft%3D2023-10-03T11%253A39%253A09.327Z&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Added HNSW support inside Vecs, our Python library for `pgvector`. Vecs automatically creates schemas and collections inside your database, making it one of the easiest ways to get started with `pgvector`.

[Read the HNSW docs](https://supabase.com/docs/guides/ai/python/api#create-an-index)

## Quick product announcements [\#](https://supabase.com/blog/beta-update-september-2023\#quick-product-announcements)

- \[PostgREST\] JWT caching just landed. API requests are about to get 100ms faster. \[ [PR](https://github.com/PostgREST/postgrest/pull/2928)\]
- \[Auth\] Added a default in-memory storage mechanism to allow using `supabase-js` in these environments to fall back to use this default storage mechanism now. Upgrade to supabase-js v2.36.0 or gotrue-js v2.54.0 for the latest changes. \[ [PR](https://github.com/supabase/gotrue-js/pull/774)\]
- \[Edge Functions\] Supports much simpler API for creating functions `Deno.serve(req => new Response("ok"))`. No `http` standard library dependency needed. (Thanks eifr for contributing with updated CLI templates. \[ [PR](https://github.com/supabase/cli/pull/1504)\]
- \[Edge Functions\] You can manage the secrets for your project's Edge Functions via the dashboard. \[ [Try it now](https://supabase.com/dashboard/project/_/settings/functions)\]

## Supabase at the AI Engineer Summit [\#](https://supabase.com/blog/beta-update-september-2023\#supabase-at-the-ai-engineer-summit)

![Supabase at the AI Engineer Summit](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsep5.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’re sponsoring a conference for the first time. We'll be participating in the keynote and hosting a workshop on pgvector. Our team of AI experts will be on hand at booth D2 to introduce you to Supabase Vector (and handing out exclusive swag 🛍️).

[Participate both physically and remotely](https://www.ai.engineer/summit)

## Made with Supabase [\#](https://supabase.com/blog/beta-update-september-2023\#made-with-supabase)

![Made with Supabase](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsep6.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Discover the stories of two innovative developers who used Supabase to build AI applications that reached remarkable achievements:

- 🧠 [Quivr](https://supabase.com/customers/quivr): an open source second brain that went viral and became one of the most popular Generative AI projects, launching 5000 databases on Supabase.
- 💬 [Chatbase](https://supabase.com/customers/chatbase): an AI chatbot builder that scaled to $1M in 5 months, making it one of the most successful single-founder AI products in the industry.

## Extended Community Highlights [\#](https://supabase.com/blog/beta-update-september-2023\#extended-community-highlights)

![Community Highlights](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsep7.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

- Sign in with Apple on Expo React Native. [Video](https://www.youtube.com/watch?v=-tpcZzTdvN0)
- Infra & remote working AMA with the Fly team. [Twitter Space](https://twitter.com/supabase/status/1704023293295243600)
- Supaweek: build a production-ready API backed by Supabase, OpenAI, and Zuplo. [Day 1](https://zuplo.com/blog/2023/09/25/using-openai-and-supabase-db-to-create-an-api) \| [Day 2](https://zuplo.com/blog/2023/09/26/handling-user-requests-dynamically) \| [Day 3](https://zuplo.com/blog/2023/09/27/documentation-for-your-supabase-api) \| [Day 4](https://zuplo.com/blog/2023/09/28/monetizing-apis) \| [Day 5](https://zuplo.com/blog/2023/09/29/announcing-supabase-auth-for-dev-portal)
- Building a real-time WhatsApp Web Clone with Next.js, Supabase, and Stream. [Full series](https://getstream.io/blog/whatsapp-nextjs/)
- Full Stack Calendly Clone using SwiftUI & Supabase. [Video](https://www.youtube.com/watch?v=SKkh2ZFTgdY)
- Using Supabase’s vector database with PostgreSQL. [Article](https://blog.logrocket.com/using-supabases-vector-database-postgresql/)
- Build A Complex Supabase App w/NoCode. [Video](https://www.youtube.com/watch?v=1n4UGyNDAis)
- Configuring Office365 as the SMTP Provider in Supabase Auth: A Comprehensive Guide. [Guide](https://blog.mansueli.com/configuring-office365-as-the-smtp-provider-in-supabase-auth-a-comprehensive-guide)
- The Edgiest Stack of 2023: Next.js, ShadCN UI, OpenAI, and Supabase. [Article](https://programmingfire.com/the-edgiest-stack-of-2023-nextjs-shadcn-ui-openai-and-supabase)
- Live coding: Harnessing the Power of Vector Embedding Search with Supabase. [Live video](https://www.youtube.com/watch?v=NtOi784Evls)
- Deploying Documenso with Vercel, Supabase and Resend. [Article](https://dev.to/documenso/deploying-documenso-with-vercel-supabase-and-resend-foi)
- Next x Nest - Using Supabase & Google OAuth in NestJS. [Tutorial](https://dev.to/abhikbanerjee99/next-x-nest-using-supabase-google-oauth-in-nestjs-1m7j)

## We are hiring [\#](https://supabase.com/blog/beta-update-september-2023\#we-are-hiring)

Come join one of the fastest-growing open source projects ever 🤗

- [Head of Data](https://boards.greenhouse.io/supabase/jobs/4981444004)
- [Support Engineer (Americas)](https://boards.greenhouse.io/supabase/jobs/4973255004)
- [Technical Documentation Lead (Frontend Engineer)](https://boards.greenhouse.io/supabase/jobs/4965064004)

## **⚠️ Baking hot meme zone ⚠️** [\#](https://supabase.com/blog/beta-update-september-2023\#%EF%B8%8F-baking-hot-meme-zone-%EF%B8%8F)

![Meme about how developers prepare to write SQL](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2023%2Fsupabase-update-september-2023-meme.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-september-2023&text=Supabase%20Beta%20September%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-september-2023&text=Supabase%20Beta%20September%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-september-2023&t=Supabase%20Beta%20September%202023)

[Last post\\
\\
**Offline-first React Native Apps with Expo, WatermelonDB, and Supabase** \\
\\
8 October 2023](https://supabase.com/blog/react-native-offline-first-watermelon-db)

[Next post\\
\\
**Dynamic Table Partitioning in Postgres** \\
\\
3 October 2023](https://supabase.com/blog/postgres-dynamic-table-partitioning)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Broadcast realtime messages via REST API](https://supabase.com/blog/beta-update-september-2023#broadcast-realtime-messages-via-rest-api)
- [Supavisor is now used for connection pooling in all new projects](https://supabase.com/blog/beta-update-september-2023#supavisor-is-now-used-for-connection-pooling-in-all-new-projects)
  - [Moving to IPV6 for Database Connection Strings](https://supabase.com/blog/beta-update-september-2023#moving-to-ipv6-for-database-connection-strings)
- [New Foreign Data Wrapper: Airtable](https://supabase.com/blog/beta-update-september-2023#new-foreign-data-wrapper-airtable)
- [Supabase Studio's latest enhancements](https://supabase.com/blog/beta-update-september-2023#supabase-studios-latest-enhancements)
- [HNSW Support for Vecs + pgvector](https://supabase.com/blog/beta-update-september-2023#hnsw-support-for-vecs--pgvector)
- [Quick product announcements](https://supabase.com/blog/beta-update-september-2023#quick-product-announcements)
- [Supabase at the AI Engineer Summit](https://supabase.com/blog/beta-update-september-2023#supabase-at-the-ai-engineer-summit)
- [Made with Supabase](https://supabase.com/blog/beta-update-september-2023#made-with-supabase)
- [Extended Community Highlights](https://supabase.com/blog/beta-update-september-2023#extended-community-highlights)
- [We are hiring](https://supabase.com/blog/beta-update-september-2023#we-are-hiring)
- [**⚠️ Baking hot meme zone ⚠️**](https://supabase.com/blog/beta-update-september-2023#%E2%9A%A0%EF%B8%8F-baking-hot-meme-zone-%E2%9A%A0%EF%B8%8F)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-september-2023&text=Supabase%20Beta%20September%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-september-2023&text=Supabase%20Beta%20September%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-september-2023&t=Supabase%20Beta%20September%202023)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)