---
url: "https://supabase.com/blog/launch-week-7-community-highlights"
title: "Launch Week 7 Community Highlights"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Launch Week 7 Community Highlights

14 Apr 2023

•

10 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Launch Week 7 Community Highlights](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-community-highlights%2Fday-5-community-highlights-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase is a collaborative company. We work with, sponsor, and support as many open source tools as possible. Here’s a few of this community highlights from the past 3 months.

## Ecosystem Partners [\#](https://supabase.com/blog/launch-week-7-community-highlights\#ecosystem-partners)

![Ecosystem Partners](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-community-highlights%2Fday-5-community-highlights-partners.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Our [Integrations Marketplace](https://supabase.com/docs/guides/integrations) continues to grow. This past few months has brought a number of new partners and collaborations:

### AWS RDS [\#](https://supabase.com/blog/launch-week-7-community-highlights\#aws-rds)

We’ve worked with the RDS team to build out the pg\_tle extension and tooling and integrating it into Supabase. These changes are a stepping stone towards running the Supabase stack on AWS RDS. Special shoutout to [@jkatz](https://github.com/jkatz), who was an instrumental collaborator and the rest of the RDS team who have been helping to transition [PL/Rust](https://github.com/tcdi/plrust) into a Trusted Language.

[Read the press announcement on Amazon.com.](https://aws.amazon.com/blogs/opensource/supabase-makes-extensions-easier-for-developers-with-trusted-language-extensions-for-postgresql/)

[Read about pg\_tle at Supabase and our collaboration with AWS.](https://www.notion.so/6f1bac83308846488ee7b01ae5c20200)

[Read about our experimental database registry, database.dev.](https://supabase.com/blog/dbdev)

### Clickhouse [\#](https://supabase.com/blog/launch-week-7-community-highlights\#clickhouse)

Along with our new Clickhouse [Foreign Data Wrapper](https://supabase.github.io/wrappers/clickhouse/), our friends at Clickhouse created guides showing the bidirectional capabilities between Supabase Postgres and Clickhouse Cloud. This is a perfect pairing when you’re consolidating your operational data with your analytical data, or if you have long-running queries that you need to offload to an analytical database like Clickhouse.

[Read the guide.](https://clickhouse.com/blog/migrating-data-between-clickhouse-postgres)

### LangChain [\#](https://supabase.com/blog/launch-week-7-community-highlights\#langchain)

It’s always fun when two open source communities join forces. LangChain is an open source framework for developing applications powered by language models. This week, to support the Supabase AI Hackathon, they released a [Supabase x LangChain template](https://github.com/langchain-ai/langchain-template-supabase), one of the fastest ways to build AI applications. Their community recently made two contributions for Supabase: adding Supabase as a [Vector Store](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase), and a neat [Hybrid Search](https://js.langchain.com/docs/modules/indexes/retrievers/supabase-hybrid) algorithm using Postgres’ Full Text Search. The also

[Read the integration docs.](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/supabase)

[Clone the template.](https://github.com/langchain-ai/langchain-template-supabase)

### Vercel + OpenAI [\#](https://supabase.com/blog/launch-week-7-community-highlights\#vercel--openai)

Do we even need to introduce Vercel and OpenAI? We have a new template in the [Vercel Marketplace](https://vercel.com/templates/next.js/openai-doc-search-starter) for creating GPT-search for your MDX files. The templates takes all the `.mdx` files in the `pages` directory and processes them to use as custom context within [OpenAI Text Completion](https://platform.openai.com/docs/guides/completion) prompts.

[View the template.](https://vercel.com/templates/next.js/openai-doc-search-starter)

### Doppler [\#](https://supabase.com/blog/launch-week-7-community-highlights\#doppler)

Doppler is a fully managed SecretOps platform that helps centralize, orchestrate, and rotate secrets in any environment. Your team can mitigate and remediate risks while using tools that fit natively into existing developer workflows.They just released an integration to automatically sync all of your team's secrets to Supabase.

[Check out the docs.](https://docs.doppler.com/docs/supabase)

### Redwood [\#](https://supabase.com/blog/launch-week-7-community-highlights\#redwood)

The RedwoodJS team has contributed a new framework [Quick Start](https://supabase.com/docs/guides/getting-started/quickstarts/redwoodjs) to our docs that will get you from zero to fullstack app with Prisma in just 2 minutes. Big shoutout to [@dthyresson](https://github.com/dthyresson) who continues to be a valuable contributor across many open source communities.

[Read the QuickStart.](https://supabase.com/docs/guides/getting-started/quickstarts/redwoodjs)

### Dart Edge for Supabase Edge Functions [\#](https://supabase.com/blog/launch-week-7-community-highlights\#dart-edge-for-supabase-edge-functions)

Dart Edge, built by [Invertase](https://invertase.io/), allows developers to write edge functions in Dart. Previously, Flutter developers had to use TypeScript for their edge functions, as it was the only supported language. However, with Dart Edge, Flutter developers can write backend code using their favorite programming language, Dart!

[Check out the guide.](https://supabase.com/docs/guides/functions/dart-edge)

### T3 Turbo x Supabase [\#](https://supabase.com/blog/launch-week-7-community-highlights\#t3-turbo-x-supabase)

T3 Turbo is a type-safe, full-stack template to create Next.js and Expo React Native applications. Using our recent [Mobile Auth updates](https://supabase.com/blog/supabase-auth-sso-pkce), the T3 community has helped build the [Supabase Create T3 Turbo template](https://github.com/supabase-community/create-t3-turbo), the fastest and easiest way to get started with Supabase and the T3 Stack. Huge shout out to [Julius](https://twitter.com/jullerino) who single-handedly created the template!

[Use the template.](https://github.com/supabase-community/create-t3-turbo)

## Self-hosting with Digital Ocean and Stackgres [\#](https://supabase.com/blog/launch-week-7-community-highlights\#self-hosting-with-digital-ocean-and-stackgres)

![Self-hosting with Digital Ocean and Stackgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-community-highlights%2Fday-5-community-highlights-digitalocean-and-stackgres.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This Launch Week had a big focus on self-hosting, adding support for self-hosted [Logs](https://supabase.com/blog/supabase-logs-self-hosted) and [Edge Functions](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions). Along with our official [self-hosting guides](https://supabase.com/docs/guides/self-hosting) (and existing community support for [AWS](https://github.com/supabase-community/supabase-on-aws), [k8s](https://github.com/supabase-community/supabase-kubernetes), [Traefik](https://github.com/supabase-community/supabase-traefik), and [Terraform](https://github.com/supabase-community/supabase-terraform)), we have a couple of new entrants into the community:

- [Digital Ocean](https://github.com/digitalocean/supabase-on-do)
- [Stackgres](https://stackgres.io/blog/running-supabase-on-top-of-stackgres/)

Self Host Supabase on DigitalOcean - YouTube

DigitalOcean

56.8K subscribers

[Self Host Supabase on DigitalOcean](https://www.youtube.com/watch?v=dDhy6pk282U)

DigitalOcean

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

[Watch on YouTube](https://www.youtube.com/watch?v=dDhy6pk282U "Watch on YouTube")

We’re looking for more self-hosting maintainers, especially for the self-hosted guides. Everything we do is MIT, Apache2, or PostgreSQL licensed, but our team is relatively small and we don’t have expertise for every deployment strategy that our community might want. If you are willing to help out on a regular basis please reach out!

## Postgres Extensions and improvements [\#](https://supabase.com/blog/launch-week-7-community-highlights\#postgres-extensions-and-improvements)

![Postgres Extensions and improvements](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-community-highlights%2Fday-5-community-highlights-extensions.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The community continues to add and improve the extensions and configuration for our [Postgres image](https://github.com/supabase/postgres). Here are a few of the crowd favorites:

### pgvector: Open-source vector similarity search for Postgres [\#](https://supabase.com/blog/launch-week-7-community-highlights\#pgvector-open-source-vector-similarity-search-for-postgres)

Just as it says on the label: `pgvector` enables vector functionality within Postgres. It’s been, by far, our most popular addition to date as it can be used to store OpenAI embeddings and serves as an alternative to Pinecone and Milvus.

[Read the announcement.](https://supabase.com/blog/openai-embeddings-postgres-vector)

### **HypoPG: Hypothetical indexes** [\#](https://supabase.com/blog/launch-week-7-community-highlights\#hypopg-hypothetical-indexes)

HypoPG allows you to create hypothetical indexes that are visible to the PostgreSQL query
planner, with no resource cost (CPU, disk, memory). This allows users to “try out” an index without waiting for the server to build them. We have big plans for this extension - we’ll integrate this functionality into the dashboard with an Index Advisor to help you optimize slow-running queries.

[Read the docs.](https://supabase.com/docs/guides/database/extensions/hypopg)

### pg\_tle: Install your own extensions [\#](https://supabase.com/blog/launch-week-7-community-highlights\#pg_tle-install-your-own-extensions)

We’ve been working with the RDS team to make Postgres _even more_ extensible. While you typically need to wait for Cloud Providers to add extension support to their Postgres offering, pg _tle is a step towards making this \_user managed_. We’ve even built a proof-of-concept registry (similar to NPM or Cargo) where you can upload extensions and share them with the community.

Link to blog post.

### PGroonga v3.0 [\#](https://supabase.com/blog/launch-week-7-community-highlights\#pgroonga-v30)

PGroonga is an extension implementing full-text search in multiple languages. In v3, PGroonga becomes fully compatible with the Supabase _extensions_ schema deprecating the need to explicitly write a schema for operators. It also increases support for _text_ and _varchar_ array types. They just released this in time for Supabase Launch Week, so we’ll roll it out to the platform in the next month.

[Read the announcement.](https://groonga.org/en/blog/2023/04/13/pgroonga-3.0.0.html)

### LZ4 compression [\#](https://supabase.com/blog/launch-week-7-community-highlights\#lz4-compression)

PG has supported LZ4 page and row compression since v14, with WAL compression added in v15. LZ4 is faster than the standard pglz method. Supabase is now fully-compatible with this option. This is especially useful for TOAST values and WAL compression.

### ICU compatibility [\#](https://supabase.com/blog/launch-week-7-community-highlights\#icu-compatibility)

Supabase Postgres has been configured with ICU support. This makes it possible to use ICU locales as collation providers. ICU supports many languages and makes the ordering of text type attributes according to these language rules.

## Client Libraries and utilities [\#](https://supabase.com/blog/launch-week-7-community-highlights\#client-libraries-and-utilities)

![Client Libraries and utilities](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-community-highlights%2Fday-5-community-highlights-libraries.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It’s becoming easier to build applications with any language.

### Support for Swift, Python, and C\# [\#](https://supabase.com/blog/launch-week-7-community-highlights\#support-for-swift-python-and-c)

In the past few months, the community has rallied and shipped 3 new client libraries, complete with Docs:

- Swift:
  - [Documentation](https://supabase.com/docs/reference/swift/introduction) \| [Source Code](https://github.com/supabase/supabase-swift)
  - Shout-out to: [grsouza](https://github.com/grsouza) & [@maail](https://github.com/maail)
- Python:
  - [Documentation](https://supabase.com/docs/reference/python/initializing) \| [Source Code](https://github.com/supabase-community/supabase-py)
  - Shout-out to: @
- C#
  - [Documentation](https://supabase.com/docs/reference/csharp/introduction) \| [Source Code](https://github.com/supabase-community/supabase-csharp)
  - Maintainers: [@acupofjose](https://github.com/acupofjose), [@veleek](https://github.com/veleek), and [@rhuanbarros](https://github.com/rhuanbarros)

These libraries are in various stages of readiness, so if you find anything that can be improved don’t hesitate to jump into the source code and help out.

### Supabase Cache Helpers [\#](https://supabase.com/blog/launch-week-7-community-highlights\#supabase-cache-helpers)

[Philipp](https://github.com/psteinroe) just released 1.0 of “Supabase Cache Helpers”, a collection of cache utilities for Supabase. With just a line of code, you can simplify the logic of **f** etching, subscribing to updates, and mutating data as well as storage objects in your project, and have all the amazing features of SWR or React Query. The cache helpers parse queries into a unique and definite query keys, automatically populating the query cache with every mutation using implicit knowledge of the schema.

[Check it out on GitHub.](https://github.com/psteinroe/supabase-cache-helpers)

[Read the docs.](https://supabase-cache-helpers.vercel.app/)

### SupaShim by Roboflow [\#](https://supabase.com/blog/launch-week-7-community-highlights\#supashim-by-roboflow)

The team at [Roboflow](https://roboflow.com/) just released [`supashim`](https://github.com/roboflow/supashim), which hooks into the Firebase calls from your app and translates them into the Supabase equivalents. With supashim, you can take an existing Firebase app, swap out the `firebase` global for `supashim`, then point it to a self-hosted Supabase instance without changing any application code. Pretty neat!

[Check it out on GitHub.](https://github.com/roboflow/supashim)

## Giving back [\#](https://supabase.com/blog/launch-week-7-community-highlights\#giving-back)

We’ve been upstreaming as many changes as possible for Supabase stack.

### Postgres Patches [\#](https://supabase.com/blog/launch-week-7-community-highlights\#postgres-patches)

We’ve submitted a number of patches to the Postgres Core:

- Added the “USER SET” parameter values for `pg_db_role_setting`. This GUC variable lets ordinary roles set placeholder variables, when permission requirements are not known yet \[ [Patch](https://www.postgresql.org/message-id/flat/20230102154240.GL1153%40telsasoft.com#c04239ecde38752a3132236306784250)\]
- Added support for custom tuple slots in the custom executor nodes. This is useful for custom table access methods. \[ [Patch](https://www.postgresql.org/message-id/flat/CAPpHfduJUU6ToecvTyRE_yjxTS80FyPpct4OHaLFk3OEheMTNA%40mail.gmail.com)\]
- Optimizations for LWlock waiting queue scalability. Long LWlock wait queues were not effective at unlocking. We’ve submitted proposals to make the queue lockless (still under community consideration). \[Discussion [one](https://www.postgresql.org/message-id/flat/CALT9ZEEz%2B%3DNepc5eti6x531q64Z6%2BDxtP3h-h_8O5HDdtkJcPw%40mail.gmail.com), [two](https://www.postgresql.org/message-id/flat/20221120204310.xywrhyxyytsajuuq%40awork3.anarazel.de), [three](https://www.postgresql.org/message-id/flat/20221027165914.2hofzp4cvutj6gin%40awork3.anarazel.de)\]

### OrioleDB Patches [\#](https://supabase.com/blog/launch-week-7-community-highlights\#orioledb-patches)

We continue to support the development of [OrioleDB](https://github.com/orioledb/orioledb), who are building scalable storage mechanisms for Postgres using table access methods. The OrioleDB extension is now version [Alpha12](https://github.com/orioledb/orioledb/releases/tag/alpha12) and compatible with Postgres 15.

This release includes various improvements and fixes, including parallel sequential scan of OrioleDB relations. This allows multi-CPU systems to speed up select queries that involve sequential scans. It’s an analogue of heap parallel scan in Postgres core but for index-organized tables. With this base, we’re now implementing methods to build Orioledb indexes using many parallel workers.

[Read the release notes.](https://github.com/orioledb/orioledb/releases/tag/alpha12)

## Contributors [\#](https://supabase.com/blog/launch-week-7-community-highlights\#contributors)

We also want to highlight all the humans who have made meaningful contributions to the Supabase ecosystem since our last Launch Week:

- [Gary](https://github.com/GaryAustin1) and [Olyno](https://github.com/olyno) \- official moderators of our [Discord](https://discord.supabase.com/) and overall incredibly helpful people. The community would not be the same without them
- [Bruno D'Luka](https://github.com/bdlukaa) \- Caring for the details of Flutter SDK so that we can provide the best DX for Flutter devs
- [CodewithGuillaume](https://twitter.com/blackevilgoblin) \- Creating a series of YouTube videos explaining different components of Supabase.
- [Daniel Mossaband](https://github.com/DanMossa) \- Worked on fixing bugs and adding features to bring the mobile auth to Supabase
- [David Plugge](https://github.com/david-plugge) \- Working on improving the [auth-helpers](https://github.com/supabase/auth-helpers) and fixing issues users report.
- [Jonathan Wilke](https://twitter.com/jonathan_wilke) \- built [SupaStarter.dev](https://supastarter.dev/). A SaaS for building SaaSes.
- [grsouza](https://github.com/grsouza) & [Maail](https://github.com/maail) \- Built the Swift libraries and documentation.
- [Raphaël Moreau](https://twitter.com/rphlmr) \- Built the [supa-stripe-stack](https://github.com/rphlmr/supa-stripe-stack) for Remix to get started building your SaaS in one command. Also the creator the [supa-fly-stack](https://github.com/rphlmr/supa-fly-stack) and [supa-remix-stack](https://github.com/rphlmr/supa-remix-stack)
- [Vinzent](https://github.com/Vinzent03) \- Constantly smashing it on the Flutter SDK adding major features such as MFA.
- [Tiniscule](https://twitter.com/tiniscule) \- for his open source [Supabase Starter kit](https://github.com/usebasejump/basejump).

## Community [\#](https://supabase.com/blog/launch-week-7-community-highlights\#community)

And you, our community. Thank you for using Supabase, reading our blog posts, and showing your support. With [over 48,000 GitHub stars](https://github.com/supabase/supabase), we are now in the top 180 most-popular repositories in all of GitHub. We still have a long way to go, but it’s a lot more fun doing it collaboratively.

### More Launch Week 7

[Designing with AI\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fai-images%2F00-ai-images-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/designing-with-ai-midjourney)

[Supavisor\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fsupavisor%2Fsupavisor-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://github.com/supabase/supavisor)

[Open Source Logging\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday1%2Fself-hosted-logs-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-logs-self-hosted)

[Self-hosted Deno Edge Functions\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday2%2Fself-hosted-edge-functions-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)

[Storage v3: Resumable Uploads with support for 50GB files\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday3%2Fstorage-v3-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/storage-v3-resumable-uploads)

[Supabase Auth: SSO, Mobile, and Server-side support\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday4%2Fsso-support-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-auth-sso-pkce)

[Community Highlight\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fcommunity%2Fcommunity-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/launch-week-7-community-highlights)

[Studio Updates\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fstudio%2Fstudio-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-studio-2.0)

[dbdev\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2Fdbdev-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/dbdev)

[Postgres TLE\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2FpgTLE-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/pg-tle)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-7-community-highlights&text=Launch%20Week%207%20Community%20Highlights)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-7-community-highlights&text=Launch%20Week%207%20Community%20Highlights)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-7-community-highlights&t=Launch%20Week%207%20Community%20Highlights)

[Last post\\
\\
**dbdev: PostgreSQL Package Manager** \\
\\
14 April 2023](https://supabase.com/blog/dbdev)

[Next post\\
\\
**Trusted Language Extensions for Postgres** \\
\\
14 April 2023](https://supabase.com/blog/pg-tle)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Ecosystem Partners](https://supabase.com/blog/launch-week-7-community-highlights#ecosystem-partners)
  - [AWS RDS](https://supabase.com/blog/launch-week-7-community-highlights#aws-rds)
  - [Clickhouse](https://supabase.com/blog/launch-week-7-community-highlights#clickhouse)
  - [LangChain](https://supabase.com/blog/launch-week-7-community-highlights#langchain)
  - [Vercel + OpenAI](https://supabase.com/blog/launch-week-7-community-highlights#vercel--openai)
  - [Doppler](https://supabase.com/blog/launch-week-7-community-highlights#doppler)
  - [Redwood](https://supabase.com/blog/launch-week-7-community-highlights#redwood)
  - [Dart Edge for Supabase Edge Functions](https://supabase.com/blog/launch-week-7-community-highlights#dart-edge-for-supabase-edge-functions)
  - [T3 Turbo x Supabase](https://supabase.com/blog/launch-week-7-community-highlights#t3-turbo-x-supabase)
- [Self-hosting with Digital Ocean and Stackgres](https://supabase.com/blog/launch-week-7-community-highlights#self-hosting-with-digital-ocean-and-stackgres)
- [Postgres Extensions and improvements](https://supabase.com/blog/launch-week-7-community-highlights#postgres-extensions-and-improvements)
  - [pgvector: Open-source vector similarity search for Postgres](https://supabase.com/blog/launch-week-7-community-highlights#pgvector-open-source-vector-similarity-search-for-postgres)
  - [**HypoPG: Hypothetical indexes**](https://supabase.com/blog/launch-week-7-community-highlights#hypopg-hypothetical-indexes)
  - [pg\_tle: Install your own extensions](https://supabase.com/blog/launch-week-7-community-highlights#pg_tle-install-your-own-extensions)
  - [PGroonga v3.0](https://supabase.com/blog/launch-week-7-community-highlights#pgroonga-v30)
  - [LZ4 compression](https://supabase.com/blog/launch-week-7-community-highlights#lz4-compression)
  - [ICU compatibility](https://supabase.com/blog/launch-week-7-community-highlights#icu-compatibility)
- [Client Libraries and utilities](https://supabase.com/blog/launch-week-7-community-highlights#client-libraries-and-utilities)
  - [Support for Swift, Python, and C#](https://supabase.com/blog/launch-week-7-community-highlights#support-for-swift-python-and-c)
  - [Supabase Cache Helpers](https://supabase.com/blog/launch-week-7-community-highlights#supabase-cache-helpers)
  - [SupaShim by Roboflow](https://supabase.com/blog/launch-week-7-community-highlights#supashim-by-roboflow)
- [Giving back](https://supabase.com/blog/launch-week-7-community-highlights#giving-back)
  - [Postgres Patches](https://supabase.com/blog/launch-week-7-community-highlights#postgres-patches)
  - [OrioleDB Patches](https://supabase.com/blog/launch-week-7-community-highlights#orioledb-patches)
- [Contributors](https://supabase.com/blog/launch-week-7-community-highlights#contributors)
- [Community](https://supabase.com/blog/launch-week-7-community-highlights#community)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-7-community-highlights&text=Launch%20Week%207%20Community%20Highlights)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-7-community-highlights&text=Launch%20Week%207%20Community%20Highlights)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-7-community-highlights&t=Launch%20Week%207%20Community%20Highlights)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)