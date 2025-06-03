---
url: "https://supabase.com/blog/new-supabase-docs-built-with-nextjs"
title: "New Supabase Docs, built with Next.js"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# New Supabase Docs, built with Next.js

12 Dec 2022

•

6 minute read

[![Jonny Summers-Muir avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmildtomato.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jonny Summers-MuirProduct Design](https://github.com/mildtomato)

New Supabase Docs, built with Next.js - YouTube

Supabase

54.4K subscribers

[New Supabase Docs, built with Next.js](https://www.youtube.com/watch?v=Q1Amk6iDlF8)

Supabase

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=Q1Amk6iDlF8&embeds_referring_euri=https%3A%2F%2Fsupabase.com%2F)

0:00

0:00 / 9:52
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=Q1Amk6iDlF8 "Watch on YouTube")

For a developer tool, documentation is more than a resource - it’s part of the product. For the past two years at Supabase, this part of our product hasn’t been great. Today’s release fixes that.

## A brief history of documentation at Supabase [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#a-brief-history-of-documentation-at-supabase)

When Supabase started in 2020, our website and our docs were powered by (the wonderful) [Docusaurus](https://docusaurus.io/), which allowed us to move quickly and efficiently.

However, as time went on, we began to face some challenges:

- We added versioning to our client libraries. Supabase maintains multiple client libraries, each with different versions. This increased the complexity and reduced maintainability of our Docusaurus setup. Contributors and team members had trouble figuring out how to contribute fixes and write new docs.
- It introduced friction with the rest of our stack (Next.js & Turborepo). At Supabase, we try and share as much setup and config as possible across projects. We have a monorepo of various Next.js sites with [shared](https://github.com/supabase/supabase/tree/master/packages) [Turborepo internal packages](https://turbo.build/repo/docs/handbook/sharing-code/internal-packages) including our Supabase UI library and configs for linting, Typescript, Tailwind and more. Having UI components and configs that we share across all projects is huge. The docs site was the only project not using Next.js and this internal packages setup.

In short: we outgrew Docusaurus.

## Documentation as a product [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#documentation-as-a-product)

Docs are the first thing you see when exploring a new tool. We wanted them to be as good as the rest of Supabase. We wanted to unify our frontend stack and build an “integrated” experience using the same UI libraries across all of our sites, and a unified Auth session so that we could tailor the documentation for our users.

### Building an MVP [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#building-an-mvp)

We tried to migrate several times and failed because we couldn’t keep up with the divergences between the two sites. The temptation was to build a “better experience” as a part of the migration, to fit with “documentation as a product” values. This was a mistake. As with any product - you start with an MVP.

We broke down the challenge into a single goal: migrate to Next.js, a carbon copy of Docusaurus. This took about 1 week, and we switched to the new Next.js MVP about one month ago. Did you notice?

With the site running on Next, things started to accelerate. For the past month, we’ve had two developers working full-time to build what you see today.

## Supabase Docs: v2, built with Next.js [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#supabase-docs-v2-built-with-nextjs)

This release adds a few new features:

### New design [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#new-design)

We’ve started implementing a set of new UI components to help facilitate our growing documentation content. While working on these, we’ve started to also refine how we want to present this information with more care on the smaller things we'd overlooked before, such as panels, buttons and icons.

![New reference docs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fday-1-new-docs%2Fredesign.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Better navigation [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#better-navigation)

Landing on a documentation site for a product as large as Supabase can be daunting.
There’s a lot to read. The problem is one of discoverability, which even a search interface can’t fix (how do you know what to search if you don’t know what a product can do?).

To solve this, we built everything into a single sidebar. From a glance, you can see everything we offer without clicking three-levels-deep into a maze of content. For a first-time reader, you should never feel lost in the docs.

Inspiration: [Airwallex](https://www.airwallex.com/docs)

### Better reference docs [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#better-reference-docs)

![New reference docs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fday-1-new-docs%2Freference-screenshot.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Previously when browsing through our reference docs, each function lived on a separate page. This release changes that behaviour - the new layout has all of a library’s functions on one page. This promotes discoverability within a single tool. Developers have the ability to use the search bar _or_ they can just `cmd+f` in their browser.

We’ve also re-engineered how our reference docs are generated from typedoc, so it’s easier for contributors and our own team members to edit and add to Supabase documentation.

Inspiration: [Stripe](https://stripe.com/docs/cli).

## What’s next [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#whats-next)

With this foundation, we hope to re-imagine what a documentation experience can be. Some things we’re working on:

### Fully integrated experience [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#fully-integrated-experience)

- **Unified Authentication:** If you’re logged into the Dashboard, then you’re logged into Supabase docs. That means personalization and project-specific documentation. No more placeholders like “ `SUPABASE_URL`". We will add URLs and Keys for the project you’ve selected, making it easier to copy and run code snippets.
- **Auto docs:** We may also move AutoDocs (currently in the dashboard) into the main Docs website. Reference docs are then just, reference docs, but you can see it in context with the table/schema you're interested in.

### Runnable code blocks [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#runnable-code-blocks)

With [Postgres WASM](https://supabase.com/blog/postgres-wasm), you could run code examples against a full Postgres database (in the browser).

### Tutorials [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#tutorials)

In the background, we’ve been working with the creator of [CodeHike](https://codehike.org/), [sponsoring](https://github.com/sponsors/pomber#sponsors) him to re-imagine what a fully interactive tutorial for Supabase could look like.

### Improved search [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#improved-search)

We’re happy users of Algolia search and their extremely generous [Open Source](https://www.algolia.com/for-open-source/) plan.
That said, we’re a Postgres company, and it would only be right for us to dog-food (and help to improve) all the features that Postgres have to offer.
We hope to go deep in Postgres FTS (small hint: check back on [Friday](https://supabase.com/launch-week) for a search-related announcement).

### More (and less!) content [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#more-and-less-content)

Docs are more than just the tech behind them. The goal of docs is to give you, the developer, everything you need to learn Supabase - no matter your level of knowledge. In some areas, our docs are too verbose. In most areas, they are too sparse. Our new docs give us the foundation to solve both of these problems so that you spend _less_ time in our docs, and more time shipping your product.

## More Launch Week 6 [\#](https://supabase.com/blog/new-supabase-docs-built-with-nextjs\#more-launch-week-6)

- [Day 2: Supabase Storage v2: Image resizing and Smart CDN](https://supabase.com/blog/storage-image-resizing-smart-cdn)
- [Day 3: Multi-factor Authentication via Row Level Security Enforcement](https://supabase.com/blog/mfa-auth-via-rls)
- [Day 4: Supabase Wrappers, a Postgres FDW framework written in Rust](https://supabase.com/blog/postgres-foreign-data-wrappers-rust)
- [Day 5: Supabase Vault is now in Beta](https://supabase.com/blog/vault-now-in-beta)
- [Community Day](https://supabase.com/blog/launch-week-6-community-day)
- [Point in Time Recovery is now available](https://supabase.com/blog/postgres-point-in-time-recovery)
- [Custom Domain Names are now available](https://supabase.com/blog/custom-domain-names)
- [Wrap Up: everything we shipped](https://supabase.com/blog/launch-week-6-wrap-up)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-supabase-docs-built-with-nextjs&text=New%20Supabase%20Docs%2C%20built%20with%20Next.js)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-supabase-docs-built-with-nextjs&text=New%20Supabase%20Docs%2C%20built%20with%20Next.js)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-supabase-docs-built-with-nextjs&t=New%20Supabase%20Docs%2C%20built%20with%20Next.js)

[Last post\\
\\
**Supabase Storage v2: Image resizing and Smart CDN** \\
\\
13 December 2022](https://supabase.com/blog/storage-image-resizing-smart-cdn)

[Next post\\
\\
**pg\_crdt - an experimental CRDT extension for Postgres** \\
\\
10 December 2022](https://supabase.com/blog/postgres-crdt)

[launch-week](https://supabase.com/blog/tags/launch-week) [docs](https://supabase.com/blog/tags/docs)

On this page

- [A brief history of documentation at Supabase](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#a-brief-history-of-documentation-at-supabase)
- [Documentation as a product](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#documentation-as-a-product)
  - [Building an MVP](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#building-an-mvp)
- [Supabase Docs: v2, built with Next.js](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#supabase-docs-v2-built-with-nextjs)
  - [New design](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#new-design)
  - [Better navigation](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#better-navigation)
  - [Better reference docs](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#better-reference-docs)
- [What’s next](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#whats-next)
  - [Fully integrated experience](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#fully-integrated-experience)
  - [Runnable code blocks](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#runnable-code-blocks)
  - [Tutorials](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#tutorials)
  - [Improved search](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#improved-search)
  - [More (and less!) content](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#more-and-less-content)
- [More Launch Week 6](https://supabase.com/blog/new-supabase-docs-built-with-nextjs#more-launch-week-6)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-supabase-docs-built-with-nextjs&text=New%20Supabase%20Docs%2C%20built%20with%20Next.js)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-supabase-docs-built-with-nextjs&text=New%20Supabase%20Docs%2C%20built%20with%20Next.js)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-supabase-docs-built-with-nextjs&t=New%20Supabase%20Docs%2C%20built%20with%20Next.js)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)