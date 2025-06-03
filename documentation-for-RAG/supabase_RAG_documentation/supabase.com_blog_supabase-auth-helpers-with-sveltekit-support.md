---
url: "https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support"
title: "Revamped Auth Helpers for Supabase (with SvelteKit support)"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Revamped Auth Helpers for Supabase (with SvelteKit support)

13 Jul 2022

•

3 minute read

[![Andrew Smith avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsilentworks.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Andrew SmithDevRel & DX](https://github.com/silentworks)

![Revamped Auth Helpers for Supabase (with SvelteKit support)](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupabase-auth-helpers-sveltekit.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've been hard at work making an Auth experience that is as smooth as possible for Supabase developers. One of the challenges has been creating a simple experience for server-side rendering (SSR) environments. We [previously released](https://supabase.com/blog/community-day#server-side-auth-for-nextjs-and-nuxt-sveltekit-and-remix-coming-soon) our Auth Helpers libraries with support for React and Next.js, and today we’re announcing some exciting updates.

## What are Auth Helpers? [\#](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support\#what-are-auth-helpers)

Auth Helpers are a collection of framework-specific utilities for Supabase Auth. They allow you to implement secure applications with little effort. These libraries include functions for protecting API routes and pages in your applications.

## SvelteKit support [\#](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support\#sveltekit-support)

Today, we’re adding support for SvelteKit. We’ve tried to keep the library’s interface similar to the other frameworks. This makes transitioning between frameworks seamless. You can follow our [step by step guide](https://github.com/supabase-community/auth-helpers/tree/main/packages/sveltekit) on how to get this setup.

## Name change [\#](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support\#name-change)

We’ve changed the name from `@supabase/supabase-auth-helpers` to `@supabase/auth-helpers`. With this change we:

- **Reset to a sub `0.x` version number.** This makes sense given that SvelteKit itself is still pre-1.0. And being pre-1.0 helps to manage expectations for future breaking changes.
- **Removed an extra “supabase”.** We realized that the namespace already contained `supabase` in it and we didn’t want to double up (naming is hard!).

## GitHub structure [\#](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support\#github-structure)

We’ve moved the Auth Helpers into a monorepo so that we can publish packages individually rather than using the same package name for every framework. Each package only includes relevant dependencies - (eg, Next.js helpers don’t include SvelteKit dependencies).

We use [Turborepo](https://turborepo.org/) for managing our monorepo pipelines and have been incredibly pleased with its caching and performance. For packaging, we use [changesets](https://github.com/changesets/changesets) and GitHub Actions to create the release and publish to the npm registry. Each library lives in its own directory inside of the [**packages**](https://github.com/supabase-community/auth-helpers/tree/main/packages) directory, with accompanying example applications making use of the library inside the [**examples**](https://github.com/supabase-community/auth-helpers/tree/main/examples) directory.

## Migration path [\#](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support\#migration-path)

We minimized the breaking changes as much as possible, but there were a few that were necessary. With that in mind we have provided a guide for migrating away from the old `@supabase/supabase-auth-helpers` library over to [the new `@supabase/auth-helpers` library](https://github.com/supabase-community/auth-helpers/tree/main/packages/nextjs#migrating-from-supabasesupabase-auth-helpers-to-supabaseauth-helpers).

## Examples available [\#](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support\#examples-available)

Having good documentation is great, especially when there are [examples](https://github.com/supabase-community/auth-helpers/tree/main/examples) to augment. We’re always looking for community support in expanding our list of examples. If you have an interesting use case that you thing others may benefit from please consider contributing it.

## Coming soon [\#](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support\#coming-soon)

Remix Auth Helpers are in the works. You can follow the development of this on our [GitHub repo](https://github.com/supabase-community/auth-helpers), or subscribe to our Supabase YouTube channel as we build it live on air.

Supabase Auth Helpers with Remix! 💿 - YouTube

Supabase

54.4K subscribers

[Supabase Auth Helpers with Remix! 💿](https://www.youtube.com/watch?v=VgYPGOr3F-4)

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

[Watch on YouTube](https://www.youtube.com/watch?v=VgYPGOr3F-4 "Watch on YouTube")

## Contribute [\#](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support\#contribute)

Contributors are welcome! You can help by creating pull requests, reporting bugs, writing documentation, replying to issues on our GitHub issue tracker, and helping others with questions they may have about using the library. If you’re already an active contributor to Supabase or any associated open source projects, consider applying to join the [SupaSquad](https://supabase.com/supasquad).

> Big shoutout to [Willow aka GHOST](https://twitter.com/onlyspaceghost) for her help with the Svelte/SvelteKit auth helper libraries.

## Resources [\#](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support\#resources)

- [Quickstart: SvelteKit](https://supabase.com/docs/guides/with-sveltekit)
- [SvelteKit and Supabase Tutorial with Authentication - Video Tutorial by James Quick](https://www.youtube.com/watch?v=YqIyET7XKIQ)
- [Waiting List App showing how to use the inviteUserByEmail API to invite users to your application.](https://github.com/silentworks/waiting-list)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-helpers-with-sveltekit-support&text=Revamped%20Auth%20Helpers%20for%20Supabase%20(with%20SvelteKit%20support))[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-helpers-with-sveltekit-support&text=Revamped%20Auth%20Helpers%20for%20Supabase%20(with%20SvelteKit%20support))[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-helpers-with-sveltekit-support&t=Revamped%20Auth%20Helpers%20for%20Supabase%20(with%20SvelteKit%20support))

[Last post\\
\\
**Implementing "seen by" functionality with Postgres** \\
\\
18 July 2022](https://supabase.com/blog/seen-by-in-postgresql)

[Next post\\
\\
**Supabase Beta June 2022** \\
\\
6 July 2022](https://supabase.com/blog/beta-update-june-2022)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [What are Auth Helpers?](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support#what-are-auth-helpers)
- [SvelteKit support](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support#sveltekit-support)
- [Name change](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support#name-change)
- [GitHub structure](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support#github-structure)
- [Migration path](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support#migration-path)
- [Examples available](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support#examples-available)
- [Coming soon](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support#coming-soon)
- [Contribute](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support#contribute)
- [Resources](https://supabase.com/blog/supabase-auth-helpers-with-sveltekit-support#resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-helpers-with-sveltekit-support&text=Revamped%20Auth%20Helpers%20for%20Supabase%20(with%20SvelteKit%20support))[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-helpers-with-sveltekit-support&text=Revamped%20Auth%20Helpers%20for%20Supabase%20(with%20SvelteKit%20support))[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-helpers-with-sveltekit-support&t=Revamped%20Auth%20Helpers%20for%20Supabase%20(with%20SvelteKit%20support))

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)