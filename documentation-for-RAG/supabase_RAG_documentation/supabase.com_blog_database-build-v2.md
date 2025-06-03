---
url: "https://supabase.com/blog/database-build-v2"
title: "database.build v2: Bring-your-own-LLM"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# database.build v2: Bring-your-own-LLM

06 Dec 2024

•

16 minute read

[![Greg Richardson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgregnr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Greg RichardsonEngineering](https://github.com/gregnr)

[![Julien Goux avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjgoux.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Julien GouxEngineering](https://github.com/jgoux)

![database.build v2: Bring-your-own-LLM](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've been hard at work since launching [database.build](https://database.build/) (formerly postgres.new), and we're thrilled to unveil a lineup of new features, starting with: Bring-your-own-LLM.

These 3 AI models tried to build me a database - YouTube

Supabase

54.4K subscribers

[These 3 AI models tried to build me a database](https://www.youtube.com/watch?v=IQ8xqmht-gk)

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

[Watch on YouTube](https://www.youtube.com/watch?v=IQ8xqmht-gk "Watch on YouTube")

You can now use your own Large Language Model (LLM) via any OpenAI-compatible provider.

In case you missed it, database.build is an [in-browser Postgres sandbox with AI assistance](https://supabase.com/blog/postgres-new). You can spin up an unlimited number of Postgres databases and interact with them using natural language (via LLM). This is possible thanks to [PGlite](https://pglite.dev/) \- a WASM build of Postgres that can run directly in the browser.

With database.build, simply describe what you would like to build and AI will help you scaffold your tables. You can also drag-and-drop CSVs to automatically generate tables based on their contents, then query them using regular SQL.

## Bring your own LLM [\#](https://supabase.com/blog/database-build-v2\#bring-your-own-llm)

Since day one, our goal has been to make database.build freely accessible to everyone. To achieve this while also mitigating abuse (and sky-high OpenAI bills), we required users to sign in with their GitHub accounts. We also introduced modest rate limits to throttle excessive AI usage and ensure fair access for everyone.

Though this setup has worked well for most users, power users have reported regularly hitting these rate limits. Others have expressed interest in experimenting with alternative models or even running database.build entirely locally. These are all valid use cases we're excited to support. That's why today, we're introducing a new option: connect your own Large Language Model (LLM) via any OpenAI-compatible provider.

When you bring your own LLM, you get:

- **No login required**: Build AI-assisted databases without needing a GitHub account.
- **No rate limits:** Your usage is only limited by your chosen provider.
- **More control:** Ensure your chat messages go only to providers you trust.
- **Greater flexibility:** Choose your model and customize prompts to suit your needs.

For organizations with strict AI policies or firewall restrictions, BYO-LLM makes it easy to route AI messages through company-approved API endpoints, like Azure's OpenAI Service.

### OpenAI compatibility [\#](https://supabase.com/blog/database-build-v2\#openai-compatibility)

If you've worked with large language models, you've probably noticed that OpenAI's API structure has become an unofficial standard. Many LLM providers now offer OpenAI-compatible APIs, making it easier to use alternative models with existing tools and libraries built around OpenAI's APIs.

This is great news for BYO-LLM, as it means connecting to other LLM providers beyond OpenAI (such as [xAI](https://x.ai/)) is trivial - as long as they provide an OpenAI-compatible API.

You might be wondering: does this mean you connect database.build locally to [Ollama](https://ollama.com/), since it also has an OpenAI-compatible API? The answer is yes! But with a few limitations, keep reading!

### How to use it [\#](https://supabase.com/blog/database-build-v2\#how-to-use-it)

At the left of database.build's header you'll find a new button labeled **Bring your own LLM**. Tap this button to open a sidebar where you can connect your own LLM provider.

![database.build v2 BYO-LLM](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fbyo-llm.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

From here, pass in your LLM provider's base URL, your associated API key, and the model you wish to use.

![database.build v2 BYO-LLM API key](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fbyo-llm-api-key.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Note that all settings and keys are stored locally and never leave your browser. Even the API requests themselves are [sent directly from the browser](https://github.com/supabase-community/database-build/blob/5b23ed1a5bc306ed202dcc726dfeb5efe1696abc/apps/web/sw.ts) without a backend proxy - keep reading!

It's important to note that the model you choose will drastically impact your experience with database.build. To work properly, database.build requires a few key features from the model:

- **Tool calling**: In order to execute SQL on your behalf, generate charts, and everything else available today, the model needs to support tool (functional) calls. Recent state-of-the-art models support this, but many others still don't and won't work with database.build.
- **SQL understanding**: It sounds obvious, but without a model trained on a moderate-to-high amount of SQL knowledge, database.build will struggle to build anything useful.
- **Chart.js knowledge**: This is important if you plan on generating charts, since the model is responsible for generating the chart configuration passed into Chart.js.

Because of this, we recommend sticking with OpenAI's gpt-4o if you wish for the same experience you are used to. To save on API costs, you could try gpt-4o-mini, though keep in mind that it may sometimes miss important information or fail to build more complex schemas. If you're feeling a bit adventurous, we would love to see what other providers and models you try with database.build and your experience with each of them.

Finally, we give you the freedom to customize the system prompt passed to the model. So far this has been catered for interactions with gpt-4o, so you'll likely want to adjust this if you are using another model.

### Under the hood [\#](https://supabase.com/blog/database-build-v2\#under-the-hood)

To make this work in a privacy-first way, all LLM API requests are sent directly from the browser. This means that all of your messages, schema, data, and API keys will only be sent directly to your provider's API without routing through a backend proxy.

This is possible thanks to two important pieces:

- CORS-friendly APIs
- Service workers

### CORS-friendly APIs [\#](https://supabase.com/blog/database-build-v2\#cors-friendly-apis)

If you've developed any browser app that connects to a backend API, you've likely experienced CORS. CORS stands for cross-origin-resource-sharing, and is a security mechanism built into browsers to prevent websites from connecting to APIs from a different domain. Quite often though there are legitimate reasons to connect to a different domain, and to support this, the server simply has to send back HTTP response headers that explicitly allow your app to connect to it.

In the case of database.build, we need to connect directly to APIs like OpenAI's [https://api.openai.com/v1](https://api.openai.com/v1) or any other provider that you choose - and this will always be cross-origin since requests are coming from the browser. The good news is: most LLM providers add CORS headers by default which means we can connect directly to their APIs from the browser with no extra work. Without this, our only option would be to route every request through a backend proxy (which is not subject to CORS restrictions).

### Service workers [\#](https://supabase.com/blog/database-build-v2\#service-workers)

If you've ever dug into database.build's [source code](https://github.com/supabase-community/database-build), you'll know that we heavily use Vercel's [AI SDK](https://sdk.vercel.ai/docs/introduction) to simplify LLM streaming and client side tool calls. Vercel has built a great DX around inference by providing convenient hooks like `useChat()` to manage AI chat messages in React.

The challenge with Vercel's AI SDK for BYO-LLM is that the SDK expects a client-server API structure. ` useChat()` connects to a server-side `/api/chat` route that is responsible for sending these messages downstream to the appropriate provider. In normal situations, this is the best architecture to protect API keys and custom logic on the server side. In our case though where users dynamically provide their own API keys, our preference is to send downstream requests directly from the browser. If we wish to continue using our existing `useChat()` infrastructure, we need a way to intercept requests to `/api/chat` and handle them ourselves in-browser.

[Service workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) to the rescue! One of the core features of service workers is the ability to intercept fetch requests and handle them client side - exactly what we need. With this approach, we can simply leave our `useChat()` logic as-is, then create a lightweight service worker that does the following:

1. Detects whether you're using your own model by reading local state from [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) (service workers don't have access to local storage, so we opt for IndexedDB).
2. If detected, it serves a local HTTP handler on `/api/chat`, sending the request directly to your provider's API.
3. Otherwise, it forwards the request to our backend as it did before.

![database.build v2 BYO-LLM API key](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fllm-service-worker-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Worth mentioning - we later learned that `useChat()` allows you to pass a custom `fetch` function directly to the hook which we could use to intercept API requests in the same way. We might switch to this approach in the future to simplify the solution with less moving parts.

### Ollama [\#](https://supabase.com/blog/database-build-v2\#ollama)

Can you connect database.build to [Ollama](https://github.com/ollama/ollama) for a fully local AI experience? Technically, yes—but there are a few caveats:

1. **Local models aren't great at tool calling (yet)**. While the latest state-of-the-art models like Llama 3.1/3.2 and Qwen 2.5 Coder technically support tool calls, versions that can run on consumer-grade hardware (like quantized models or lower-parameter variants) don't perform as consistently as their larger counterparts. These smaller models often fail to make tool calls when needed, call nonexistent tools, or pass invalid arguments.
2. **Tool streaming challenges**. database.build relies on both tool calls and streaming to function. Ollama recently [added support](https://github.com/ollama/ollama/pull/7836) for tool streaming (shout out to [@thanosthinking](https://x.com/thanosthinking)), making it possible to use with database.build as long as the model can handle tool calls correctly. However, while Ollama does provide a tool streaming API, the current behavior buffers the entire response until it's complete before sending it in a single delta message. This creates the impression of slower performance on the frontend, even though the backend processes normally. The Ollama team is [actively working on improving this](https://github.com/ollama/ollama/issues/7886).

Even with these challenges, we'd love to see someone get a local model working. Feel free to experiment, tweak the system prompt to better steer the model, and let us know if you make it work!

Open-weight models are improving rapidly, and as consumer hardware continues to progress, local setups will likely become a more practical option for a broader range of use cases—including (hopefully) database.build.

## Live Share [\#](https://supabase.com/blog/database-build-v2\#live-share)

Live Share allows you to connect to your in-browser PGlite databases from _outside the browser_—using any PostgreSQL client.

You could, for example, copy-paste the provided connection string into `psql`. Once connected, you can interact with your in-browser PGlite instance in real time as if it were any regular Postgres database.

Some other tools you might want to connect to this:

- pg\_dump: export your in-browser databases to other platforms!
- ORM: test out your database directly within your app
- IDE: browse your data using your favorite database IDE

For a behind-the-scenes look at the engineering behind this, check out our dedicated [blog post](https://supabase.com/blog/database-build-live-share).

## Deployments [\#](https://supabase.com/blog/database-build-v2\#deployments)

One of the most requested features has been a way to easily deploy your databases to the cloud with a single click.

As a quick reminder - all database.build databases run directly in your browser using PGlite. This client-side approach makes it easy to spin up virtually limitless databases for design and experimentation. But when it's time to use your database in production, the options have been somewhat cumbersome:

- Manually copy-pasting the generated migrations and running them against a real database
- Using Live Share with `pg_dump` and `pg_restore` to back up and restore your browser database to a production-ready database

Now with deployments, you can deploy your database.build creations directly to a cloud database provider, starting with Supabase (and AWS coming soon).

### Deploy to Supabase [\#](https://supabase.com/blog/database-build-v2\#deploy-to-supabase)

After building your database schema, click the **Deploy** button in the app's header.

The first time you deploy to Supabase, you will need to connect your database.build account with your Supabase account. If you don't already have a Supabase account, you'll be given the option to create a new one here. Supabase includes a Free plan, so if this is your first project there will be no cost to deploy. Follow the steps outlined in the dialog to connect your account with a Supabase org.

Once your account is connected you will be presented with a preview of the org and project name that will be created. If you are happy with this, click **Deploy**. Be sure to keep your browser tab open to ensure a successful deployment.

Finally you will be presented with connection strings and a password to connect to your new database.

### Behind the scenes [\#](https://supabase.com/blog/database-build-v2\#behind-the-scenes)

Getting deployments to work took quite a bit more engineering than it might seem at first glance. To copy your in-browser database to the cloud accurately, we needed a way to dump and restore.

We decided to piggyback on top of our existing Live Share feature, which creates a reverse connection between your in-browser database and an external PostgreSQL client. With Live Share enabled, we connect a server-side `pg_dump` program directly to your in-browser database. The resulting dump is then piped into `pg_restore`, which transfers it to your new cloud database.

![database.build v2 Deploy to Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fdeploy-to-supabase-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Yes, it's a lot of moving parts! It's worth mentioning that Electric SQL [_just_](https://github.com/electric-sql/pglite/releases/tag/%40electric-sql%2Fpglite-tools%400.2.1) released a WASM version of `pg_dump` that we're excited to integrate in the future. Generating the dump directly in the browser will likely be faster and more reliable with less moving parts.

### What about serverless PGlite? [\#](https://supabase.com/blog/database-build-v2\#what-about-serverless-pglite)

Back when we first launched database.build, we shared plans to explore a serverless PGlite deployment option. However as we moved forward, we encountered a number of small but significant challenges that added up over time. PGlite's memory usage in multi-tenant environments turned out to be higher than anticipated—a problem the ElectricSQL team is actively working to address. Given PGlite's single-connection limit, anything more than a few megabytes of RAM will not be practical in a serverless environment. Additionally, our initial reliance on `s3fs` for storage proved to be less reliable than expected, making it difficult to meet the requirements for a seamless serverless experience.

While these challenges have pushed us to focus on alternative deployment options for now, we remain committed to revisiting serverless options as these issues are resolved and the ecosystem continues to evolve.

## Drag and drop SQL files [\#](https://supabase.com/blog/database-build-v2\#drag-and-drop-sql-files)

You've always been able to drag and drop CSV files into the chat, but what about SQL files? In this new release, simply dropping a SQL file onto that chat will automatically load its contents into your browser DB.

This can be useful if you have existing schema or migrations that were designed elsewhere that you wish to extend or ask questions about.

## Download PGlite databases via `pg_dump` [\#](https://supabase.com/blog/database-build-v2\#download-pglite-databases-via-pg_dump)

You can now dump your in-browser database to a SQL file using a WASM version of `pg_dump`.

Previously when you went to download your database, we were exporting PGlite's internal `pgdata` directory as a `.tar.gz` file. This format was a bit cumbersome to work with, and was only compatible with other PGlite instances. Now when you hit **Download**, you'll get a `.sql` file that you can import into any Postgres database.

Kudos to the ElectricSQL team for continually breaking new ground with embeddable Postgres. WASM `pg_dump` is a huge step forward for the project, and we're excited to see what other tools they bring to the browser in the future.

## Redesign [\#](https://supabase.com/blog/database-build-v2\#redesign)

We're thrilled to announce a complete redesign of database.build, bringing a sleek new look and enhanced functionality.

The update includes seamless support for both desktop and mobile platforms, ensuring a smooth and intuitive experience across all devices. Get ready to build your databases anytime, anywhere!

![database.build v2 desktop support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fbyo-llm.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Mobile support [\#](https://supabase.com/blog/database-build-v2\#mobile-support)

Whether you're on the train, stuck in a meeting, or lounging on the couch, you can spin up databases and tweak your schema with just a few taps.

With mobile support, you officially have no excuse not to ship that feature you've been procrastinating on. We're excited to see what you build!

![database.build v2 mobile support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fmobile-support.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Wrapping up [\#](https://supabase.com/blog/database-build-v2\#wrapping-up)

Everything we've shipped today - BYO-LLM, Live Share, Deployments, drag-drop SQL, and mobile support - is built on an open-source foundation. We believe in transparency, community collaboration, and making tools like database.build accessible to everyone.

If you're curious about how it all works under the hood or want to contribute, you can find the entire project on GitHub: [https://github.com/supabase-community/database-build](https://github.com/supabase-community/database-build).

As always, we'd love to hear your feedback, ideas, or just see what you're building!

[Launch Week13](https://supabase.com/launch-week/13)

2-6 December 24

[Day 1 -Supabase AI Assistant v2](https://supabase.com/blog/supabase-ai-assistant-v2)

[Day 2 -Supabase Functions: Background Tasks and WebSockets](https://supabase.com/blog/edge-functions-background-tasks-websockets)

[Day 3 -Supabase Cron: Schedule Recurring Jobs in Postgres](https://supabase.com/blog/supabase-cron)

[Day 4 -Supabase Queues](https://supabase.com/blog/supabase-queues)

[Day 5 -database.build v2: Bring-Your-Own-LLM](https://supabase.com/blog/database-build-v2)

Build Stage

[01 -OrioleDB Public Alpha](https://supabase.com/blog/orioledb-launch)

[02 -Supabase CLI v2: Config as Code](https://supabase.com/blog/cli-v2-config-as-code)

[03 -High Performance Disks](https://supabase.com/blog/high-performance-disks)

[04 -Restore to a New Project](https://supabase.com/blog/restore-to-a-new-project)

[05 -Hack the Base! with Supabase](https://supabase.com/blog/hack-the-base)

[Community Meetups](https://supabase.com/events?category=meetup)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-v2&text=database.build%20v2%3A%20Bring-your-own-LLM)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-v2&text=database.build%20v2%3A%20Bring-your-own-LLM)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-v2&t=database.build%20v2%3A%20Bring-your-own-LLM)

[Last post\\
\\
**Running Durable Workflows in Postgres using DBOS** \\
\\
10 December 2024](https://supabase.com/blog/durable-workflows-in-postgres-dbos)

[Next post\\
\\
**Restore to a New Project** \\
\\
6 December 2024](https://supabase.com/blog/restore-to-a-new-project)

[launch-week](https://supabase.com/blog/tags/launch-week) [AI](https://supabase.com/blog/tags/AI) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [Bring your own LLM](https://supabase.com/blog/database-build-v2#bring-your-own-llm)
  - [OpenAI compatibility](https://supabase.com/blog/database-build-v2#openai-compatibility)
  - [How to use it](https://supabase.com/blog/database-build-v2#how-to-use-it)
  - [Under the hood](https://supabase.com/blog/database-build-v2#under-the-hood)
  - [CORS-friendly APIs](https://supabase.com/blog/database-build-v2#cors-friendly-apis)
  - [Service workers](https://supabase.com/blog/database-build-v2#service-workers)
  - [Ollama](https://supabase.com/blog/database-build-v2#ollama)
- [Live Share](https://supabase.com/blog/database-build-v2#live-share)
- [Deployments](https://supabase.com/blog/database-build-v2#deployments)
  - [Deploy to Supabase](https://supabase.com/blog/database-build-v2#deploy-to-supabase)
  - [Behind the scenes](https://supabase.com/blog/database-build-v2#behind-the-scenes)
  - [What about serverless PGlite?](https://supabase.com/blog/database-build-v2#what-about-serverless-pglite)
- [Drag and drop SQL files](https://supabase.com/blog/database-build-v2#drag-and-drop-sql-files)
- [Download PGlite databases via `pg_dump`](https://supabase.com/blog/database-build-v2#download-pglite-databases-via-pg_dump)
- [Redesign](https://supabase.com/blog/database-build-v2#redesign)
  - [Mobile support](https://supabase.com/blog/database-build-v2#mobile-support)
- [Wrapping up](https://supabase.com/blog/database-build-v2#wrapping-up)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-v2&text=database.build%20v2%3A%20Bring-your-own-LLM)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-v2&text=database.build%20v2%3A%20Bring-your-own-LLM)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdatabase-build-v2&t=database.build%20v2%3A%20Bring-your-own-LLM)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![database.build v2 BYO-LLM](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fbyo-llm.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![database.build v2 BYO-LLM API key](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fbyo-llm-api-key.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![database.build v2 BYO-LLM API key](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fllm-service-worker-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![database.build v2 Deploy to Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fdeploy-to-supabase-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![database.build v2 desktop support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fbyo-llm.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![database.build v2 mobile support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-5-database-build-v2%2Fmobile-support.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)