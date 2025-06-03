---
url: "https://supabase.com/blog/chatgpt-supabase-docs"
title: "Supabase Clippy: ChatGPT for Supabase Docs"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Clippy: ChatGPT for Supabase Docs

07 Feb 2023

•

5 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Supabase Clippy: ChatGPT for Supabase Docs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdocsgpt%2Fog_supabase_clippy.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

🆕 Want to build your own Clippy based on your own content? Use our [Next.js OpenAI Doc Search Template](https://github.com/supabase-community/nextjs-openai-doc-search) to deploy your own now!

We all know that Microsoft's real agenda for pouring billions into OpenAI is to revive their favorite friend Clippy.
Today, we're doing our part to support the momentum by releasing “Supabase Clippy” for our docs (and we don't expect this name to last long before the lawyers catch on).

![Clippy](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdocsgpt%2Fclippy.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Want to try it out? It's a hidden feature while in MVP - visit [supabase.com/docs](https://supabase.com/docs) and hit `cmd` \+ `/` to pull up the search box (sorry mobile users).

# ChatGPT for Supabase Docs [\#](https://supabase.com/blog/chatgpt-supabase-docs\#chatgpt-for-supabase-docs)

Last launch week we [released](https://supabase.com/blog/new-supabase-docs-built-with-nextjs) our new documentation site to improve the developer experience, especially for new users.

When we first started Supabase our docs were very concise. We deliberately withheld "non-critical information" so that developers could consume everything in one sitting.

Our product suite has grown in the past 2 years and our docs have grown as a result. There's a lot to read. We're also attracting developers who've never used Postgres before, and it's becoming incumbent on us to train these developers on best-practices.

![Missing indexes](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdocsgpt%2Findexes.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### The “ask” interface [\#](https://supabase.com/blog/chatgpt-supabase-docs\#the-ask-interface)

Developers have recently gained the ability to trust a bot. Where Clippy failed, ChatGPT succeeded.

This is convenient timing for us, since our documentation content is more than the average developer wants to consume in one go. Today we're providing a similar interface to ChatGPT which is trained on our own docs.

To keep your expectations low, this implementation is a 1-week MVP. We're sharing this iteration to gather feedback and to teach you how to build something similar.

## How it's built [\#](https://supabase.com/blog/chatgpt-supabase-docs\#how-its-built)

It's built with Supabase/Postgres, and consists of several key parts:

1. Parsing the Supabase docs into sections.
2. Creating embeddings for each section using OpenAI's embeddings API.
3. Storing the embeddings in Postgres using the pgvector extension.
4. Getting a user's question.
5. Query the Postgres database for the most relevant documents related to the question.
6. Inject these documents as context for GPT-3 to reference in its answer.
7. Streaming the results back to the user in realtime.

All the changes we made are in [this](https://github.com/supabase/supabase/pull/12056) Pull Request. Greg is here to explain every step in full detail:

ClippyGPT - How I Built Supabase’s OpenAI Doc Search (Embeddings) - YouTube

Rabbit Hole Syndrome

26.1K subscribers

[ClippyGPT - How I Built Supabase’s OpenAI Doc Search (Embeddings)](https://www.youtube.com/watch?v=Yhtjd7yGGGA)

Rabbit Hole Syndrome

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

Full screen is unavailable. [Learn More](https://support.google.com/youtube/answer/6276924)

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

[Watch on YouTube](https://www.youtube.com/watch?v=Yhtjd7yGGGA "Watch on YouTube")

You can find a full write up in our previous blog post: [Storing OpenAI embeddings in Postgres with pgvector](https://supabase.com/blog/openai-embeddings-postgres-vector).

## What's next [\#](https://supabase.com/blog/chatgpt-supabase-docs\#whats-next)

This current version is very basic, which makes it a good starting point if you want to build something similar.

- **Expand the knowledge base:** Create embeddings for our reference docs, GitHub Discussions, Discord discussions, etc. The current iteration is only using the Guides.
- **Caching:** Cache queries so that we can provide answers instantly to similar/matching questions.
- **User-assisted improvements:** Ability to thumbs-up responses for relevance.
- **Beyond search:** perhaps we can make this interface interactive, guiding users through instructions.

## Bonus: The power of open source [\#](https://supabase.com/blog/chatgpt-supabase-docs\#bonus-the-power-of-open-source)

One of the most interesting things about this feature was _how_ it happened - almost completely from open source contributions. A short series of events:

### A friendly email [\#](https://supabase.com/blog/chatgpt-supabase-docs\#a-friendly-email)

A few weeks ago I received an email, drawing our attention to a [Pull Request](https://github.com/supabase/postgres/pull/472) in our [`postgres`](https://github.com/supabase/postgres) GitHub repo:

![Greg](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdocsgpt%2Fgreg.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### A friendly chat [\#](https://supabase.com/blog/chatgpt-supabase-docs\#a-friendly-chat)

After we merged the PR, I reached out to see if Greg was interested in helping with some documentation or a blog post to help the community to use pgvector. On the call, Greg surprised me with an initial prototype where he had ingested the Supabase docs for a ChatGPT-like experience. I was suitably impressed and suggested that we could explore ways to work together to build it into the Supabase docs. He wasted no time:

Supabase + OpenAI Embeddings + pgvector - YouTube

Rabbit Hole Syndrome

26.1K subscribers

[Supabase + OpenAI Embeddings + pgvector](https://www.youtube.com/watch?v=yAsR7oe5vng)

Rabbit Hole Syndrome

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

Full screen is unavailable. [Learn More](https://support.google.com/youtube/answer/6276924)

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

[Watch on](https://www.youtube.com/watch?v=yAsR7oe5vng&embeds_referring_euri=https%3A%2F%2Fsupabase.com%2F)

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=yAsR7oe5vng "Watch on YouTube")

### A friendly collaboration [\#](https://supabase.com/blog/chatgpt-supabase-docs\#a-friendly-collaboration)

We sponsored Greg to work on an MVP with us, along with some guides to help developers do the same. He [pushed all his changes](https://github.com/supabase/supabase/pull/12056) to the Supabase Docs, and we wrote a [blog post](https://supabase.com/blog/openai-embeddings-postgres-vector) together to help developers build something similar.

If you re-read the events above and swap “Supabase” for any other big-tech company, you'll grasp how impossible this series of events is for any company that's not open source. All the code that was contributed is licensed liberally, so we didn't need to jump through IP checklists. Our docs are publicly available on GitHub, so Greg could build his prototype without being granted access.

We're incredibly grateful for Greg's work here, so if you like what he's done then consider supporting him by checking out [prmpts.ai](https://prmpts.ai/) and following him on twitter: [@ggrdson](https://twitter.com/ggrdson).

While you're at it, consider supporting [@ankane](https://github.com/ankane)'s great work on [pgvector](https://github.com/pgvector/pgvector) by starring them on GitHub, and sending your thanks.

## Try it out [\#](https://supabase.com/blog/chatgpt-supabase-docs\#try-it-out)

Want to try Supabase Clippy? It's a hidden feature while in MVP - visit [supabase.com/docs](https://supabase.com/docs) and hit `cmd` \+ `/` to pull up the search box (sorry mobile users).

## More pgvector and ChatGPT resources [\#](https://supabase.com/blog/chatgpt-supabase-docs\#more-pgvector-and-chatgpt-resources)

- [AI docs](https://supabase.com/docs/guides/ai)
- [A ChatGPT Plugins Template built with Supabase Edge Runtime](https://supabase.com/blog/building-chatgpt-plugins-template)
- [Template for building your own custom ChatGPT style doc search](https://github.com/supabase-community/nextjs-openai-doc-search)
- [Supabase + LangChain Starter Template](https://blog.langchain.dev/langchain-x-supabase/)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-supabase-docs&text=Supabase%20Clippy%3A%20ChatGPT%20for%20Supabase%20Docs)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-supabase-docs&text=Supabase%20Clippy%3A%20ChatGPT%20for%20Supabase%20Docs)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-supabase-docs&t=Supabase%20Clippy%3A%20ChatGPT%20for%20Supabase%20Docs)

[Last post\\
\\
**Supabase Beta January 2023** \\
\\
8 February 2023](https://supabase.com/blog/supabase-beta-january-2023)

[Next post\\
\\
**Storing OpenAI embeddings in Postgres with pgvector** \\
\\
6 February 2023](https://supabase.com/blog/openai-embeddings-postgres-vector)

[AI](https://supabase.com/blog/tags/AI) [docs](https://supabase.com/blog/tags/docs)

On this page

- [ChatGPT for Supabase Docs](https://supabase.com/blog/chatgpt-supabase-docs#chatgpt-for-supabase-docs)

  - [The “ask” interface](https://supabase.com/blog/chatgpt-supabase-docs#the-ask-interface)

  - [How it's built](https://supabase.com/blog/chatgpt-supabase-docs#how-its-built)
  - [What's next](https://supabase.com/blog/chatgpt-supabase-docs#whats-next)
  - [Bonus: The power of open source](https://supabase.com/blog/chatgpt-supabase-docs#bonus-the-power-of-open-source)
    - [A friendly email](https://supabase.com/blog/chatgpt-supabase-docs#a-friendly-email)
    - [A friendly chat](https://supabase.com/blog/chatgpt-supabase-docs#a-friendly-chat)
    - [A friendly collaboration](https://supabase.com/blog/chatgpt-supabase-docs#a-friendly-collaboration)
  - [Try it out](https://supabase.com/blog/chatgpt-supabase-docs#try-it-out)
  - [More pgvector and ChatGPT resources](https://supabase.com/blog/chatgpt-supabase-docs#more-pgvector-and-chatgpt-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-supabase-docs&text=Supabase%20Clippy%3A%20ChatGPT%20for%20Supabase%20Docs)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-supabase-docs&text=Supabase%20Clippy%3A%20ChatGPT%20for%20Supabase%20Docs)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fchatgpt-supabase-docs&t=Supabase%20Clippy%3A%20ChatGPT%20for%20Supabase%20Docs)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)