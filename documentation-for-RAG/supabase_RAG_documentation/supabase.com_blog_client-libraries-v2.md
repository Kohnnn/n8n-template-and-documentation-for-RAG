---
url: "https://supabase.com/blog/client-libraries-v2"
title: "Supabase Libraries V2: Python, Swift, Kotlin, Flutter, and Typescript"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Libraries V2: Python, Swift, Kotlin, Flutter, and Typescript

15 Dec 2023

•

7 minute read

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

[![Andrew Smith avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsilentworks.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Andrew SmithDevRel & DX](https://github.com/silentworks)

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Supabase Libraries V2: Python, Swift, Kotlin, Flutter, and Typescript](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-client-libs%2Fclient-libs-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Here is what you need to know:

- [Swift](https://supabase.com/docs/reference/swift/introduction), [Kotlin](https://supabase.com/docs/reference/kotlin/introduction), [C#](https://supabase.com/docs/reference/csharp/introduction), and [Python](https://supabase.com/docs/reference/python/introduction) are now stable.
- We’ve added even more support for mobile using React Native and [Expo](https://supabase.com/docs/guides/getting-started/tutorials/with-expo-react-native).
- We’re consolidating all client libraries onto the same version number (v2) so that you get a consistent API across all libraries.

## Version 2, for all libraries [\#](https://supabase.com/blog/client-libraries-v2\#version-2-for-all-libraries)

All of the libraries mentioned in this post are now on v2. We want the API for each library to “move in lock step”. You should be able to jump around each of the client libraries and they should operate the same, barring any language idiosyncrasies.

## Supabase Python v2 [\#](https://supabase.com/blog/client-libraries-v2\#supabase-python-v2)

Supabase Python is now stable thanks to the following maintainers: [Anand](https://github.com/anand2312), [Daniel Reinón García](https://github.com/dreinon), [Leynier Gutiérrez González](https://github.com/leynier), [Joel Lee](https://github.com/J0), and [Andrew Smith](https://github.com/silentworks/).

Check out the [docs](https://supabase.com/docs/reference/python/introduction), as well as these Python examples to help you get started:

- [Slack Consolidate: a slackbot built with Python and Supabase](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages)
- [Python data loading with Supabase](https://supabase.com/blog/loading-data-supabase-python)
- [GitHub OAuth in your Python Flask app](https://supabase.com/blog/oauth2-login-python-flask-apps)

##### Python library for vectors and embeddings

Don’t forget that we also have Vecs, a Python client for managing and querying vector stores in Postgres with the pgvector extension. [Get started](https://supabase.com/docs/guides/ai/python/api)!

## Supabase Swift v2 [\#](https://supabase.com/blog/client-libraries-v2\#supabase-swift-v2)

Supabase Swift is now stable thanks to [Guilherme Souza](https://github.com/grdsdev) and [Maail](https://github.com/maail).

Check out the [docs](https://supabase.com/docs/reference/swift/introduction), as well as these Swift examples to help you get started:

- [Getting started with Swift](https://supabase.com/docs/guides/getting-started/tutorials/with-swift)
- [iOS Swift Database & Auth](https://www.youtube.com/watch?v=enVDRqzmudo) (video tutorial)

## Supabase Kotlin v2 [\#](https://supabase.com/blog/client-libraries-v2\#supabase-kotlin-v2)

Supabase Kotlin is now stable thanks to [Jan Tennert](https://github.com/jan-tennert)

Check out the [docs](https://supabase.com/docs/reference/kotlin/introduction), as well as these Kotlin guides to help you get started:

- [Getting started with Android Kotlin](https://supabase.com/docs/guides/getting-started/quickstarts/kotlin)
- [Getting started with Supabase on Android](https://youtu.be/_iXUVJ6HTHU) (Video)
- Demos:
  - [Chat Demo (Desktop/Android/Browser)](https://github.com/supabase-community/supabase-kt/tree/master/demos/chat-demo-mpp)
  - [File Upload Demo (Desktop/Android)](https://github.com/supabase-community/supabase-kt/tree/master/demos/file-upload)
  - [Android Native Google login & in-app OAuth (Android)](https://github.com/supabase-community/supabase-kt/tree/master/demos/android-login)
  - [Multi-Factor Authentication (Desktop/Android/Browser)](https://github.com/supabase-community/supabase-kt/tree/master/demos/multi-factor-authentication)
  - [Multiplatform Deep Linking (Desktop/Android)](https://github.com/supabase-community/supabase-kt/tree/master/demos/multiplatform-deeplinks)
  - [Groceries Store App (Android)](https://github.com/hieuwu/android-groceries-store)

## Typescript v2 updates [\#](https://supabase.com/blog/client-libraries-v2\#typescript-v2-updates)

We’ve made several updates for Typescript support in `supabase-js`:

- the Supabase CLI now generates [Table and Enum shorthands](https://supabase.com/docs/guides/api/rest/generating-types#type-shorthands)
- new helpers `QueryResult` and `QueryData` extract the result types for [complex queries and joins](https://supabase.com/docs/guides/api/rest/generating-types#response-types-for-complex-queries)
- relationships between tables are now supported:
  - one-to-many relationships are typed as `T[]`
  - many-to-one relationships are typed as `T | null`

## Flutter v2 updates [\#](https://supabase.com/blog/client-libraries-v2\#flutter-v2-updates)

The core theme of Flutter v2 has been stability and better DX. Shout-out to [Vinzent](https://github.com/Vinzent03), a community maintainer who has done the majority of the work. Some notable improvements:

- **Type safety for queries:** The return type of a query will automatically be set to `List` of `Map` depending on return type ( `single()` or `maybeSingle()` )
- **Type safety for Realtime:** Realtime broadcast and presence get their own methods to make it more easily accessible.
- **Performance:**
  - Initialization time has been reduced by lazily refreshing the session in the background.
  - Lighter package size. We have removed some dependencies

## React Native and Expo support [\#](https://supabase.com/blog/client-libraries-v2\#react-native-and-expo-support)

We’ve [worked with the Expo team](https://docs.expo.dev/guides/using-supabase/) to improve support for React Native.

Expo 🤝 Supabase - YouTube

Supabase

54.4K subscribers

[Expo 🤝 Supabase](https://www.youtube.com/watch?v=7DYZdAPPJOw)

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

[Watch on YouTube](https://www.youtube.com/watch?v=7DYZdAPPJOw "Watch on YouTube")

By default, `supabase-js` uses the browser's `localStorage` mechanism to persist the user's session. This can be extended with platform-specific implementations. React Native can target native mobile and web applications with the same code base, so we need a storage implementation that works for all these platforms. Now you can use [react-native-async-storage](https://supabase.com/blog/react-native-authentication#authentication-storage) or a combination with [expo-secure-sorage](https://supabase.com/blog/react-native-authentication#encrypting-the-user-session) for AES encrypted sessions.

Beyond that we’ve focused on making supabase-js highly compatible with React Native and created plenty of [video tutorials](https://youtube.com/playlist?list=PL5S4mPUpp4OsrbRTx21k34aACOgpqQGlx&si=Ez-0S4QhBxtayYsq) and documentation for:

- [crafting an offline-first experience](https://supabase.com/blog/react-native-offline-first-watermelon-db)
- [uploading files to Supabase Storage](https://supabase.com/blog/react-native-storage)
- [sending push notifications](https://supabase.com/docs/guides/functions/examples/push-notifications).

## Our approach to client libraries [\#](https://supabase.com/blog/client-libraries-v2\#our-approach-to-client-libraries)

We have a strong preference to develop the client libraries with our community. This is part of our open source philosophy:

### The Cathedral or the Bazaar? [\#](https://supabase.com/blog/client-libraries-v2\#the-cathedral-or-the-bazaar)

If you haven’t already, it’s worth reading “ [The Cathedral and the Bazaar](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar)” by Eric S. Raymond. In short, it contrasts two software development approaches:

1. The **Cathedral** represents closed, centralized development, where a small group of developers work in isolation.
2. The **Bazaar** symbolizes open, decentralized collaboration, where a large community of developers openly shares and collaborates on code.

We believe the “bazaar” model is the right model for an open source business. If you aren’t constantly pushing in this direction then it’s extremely likely that the company will relicense (seen most recently with [Hashi](https://news.ycombinator.com/item?id=37081306)). The way we see it, the more we can foster our community the less power we have.

### Fostering the community [\#](https://supabase.com/blog/client-libraries-v2\#fostering-the-community)

We just reached 1000 contributors to our [main repo](https://github.com/supabase/supabase). It’s not easy to build a community of contributors, it’s something that need to be fostered. (Shout out to [@tobiastornros](https://github.com/tobiastornros), contributor #1000 - and everyone else who [contributed yesterday](https://x.com/kiwicopple/status/1735282666872987673?s=20))

The client libs are one of the best ways to foster the community because they are lower-complexity than some of the tools we maintain (do you know [Haskell](https://github.com/PostgREST/postgrest)?).

![Diagram explaining Supabase community](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-client-libs%2Fcommunity-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We want the Supabase community to outlive us. With more community maintainers, you should feel _even safer_ knowing that there is already a continuity plan in place. We’re [giving back to the community](https://supabase.com/blog/supabase-series-b#giving-back) and we hope to expand this as we become even more commercially successful.

### Modularity [\#](https://supabase.com/blog/client-libraries-v2\#modularity)

As a [Principle](https://supabase.com/docs/guides/getting-started/architecture#product-principles), we develop a library for each tool we support. While Supabase may “feel” like a single tool when you’re using it, it's actually a set of tools which you can use independently (especially useful for self hosting):

![Diagram explaining how Supabase is built behind the scenes](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-client-libs%2Fmodularity-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We have libraries for each of the middleware components. For example, `supabase-js` is simply a wrapper around `postgres-js`, `storage-js`, etc. If you want to self-host PostgREST with your database, it should feel very familiar:

`
// supabase-js
const supabase = createClient('SUPABASE_URL', 'SUPABASE_KEY')
const { data } = supabase.from('countries').select('id, name')
// postgres-js
const postgrest = new PostgrestClient('POSTGREST_URL')
const { data } = postgrest.from('countries').select('id, name')
`

### Why not auto-generate the libraries? [\#](https://supabase.com/blog/client-libraries-v2\#why-not-auto-generate-the-libraries)

We’re not completely against this idea, but from what we’ve seen so far:

- Each language has its idiosyncrasies. Developers using generated libraries often find themselves writing code that feels unnatural in their chosen language.
- Generated libraries are somewhat bloated. We want to keep the libraries extremely small.

That said, we may look into this approach in the future, perhaps starting with one of the tools.

## Get involved [\#](https://supabase.com/blog/client-libraries-v2\#get-involved)

If you want to become a maintainer, please just get started with PRs. If, after a few PRs, you enjoy the process, ping one of the teams on Discord and let us know - we’ll work with you to become a community maintainer.

[Launch Week![Supabase Launch Week X icon](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Flwx%2Flogos%2Flwx_logo.svg&w=32&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/launch-week)

11-15 Dec

Main Stage

[Day 1 -Supabase Studio: introducing an **AI Assistant**, **Postgres roles**, and **user impersonation**](https://supabase.com/blog/studio-introducing-assistant)

[Day 2 -Edge Functions: **Node** and native **npm** compatibility](https://supabase.com/blog/edge-functions-node-npm)

[Day 3 -Introducing Supabase **Branching**, a Postgres database for every pull request](https://supabase.com/blog/supabase-branching)

[Day 4 -Supabase Auth: **Identity Linking**, **Session Control**, **Password Protection** and **Hooks**](https://supabase.com/blog/supabase-auth-identity-linking-hooks)

[Day 5 -Introducing **Read Replicas** for low latency](https://supabase.com/blog/introducing-read-replicas)

Build Stage

[01 -Supabase Album](https://supabase.productions/)

[02 -Postgres Language Server](https://supabase.com/blog/postgres-language-server-implementing-parser)

[03 -Design at Supabase](https://supabase.com/blog/how-design-works-at-supabase)

[04 -Supabase Grafana](https://github.com/supabase/supabase-grafana)

[05 -pg\_graphql: Postgres functions](https://supabase.com/blog/pg-graphql-postgres-functions)

[06 -PostgREST 12](https://supabase.com/blog/postgrest-12)

[07 -Supavisor 1.0](https://supabase.com/blog/supavisor-postgres-connection-pooler)

[08 -Supabase Wrappers v0.2](https://supabase.com/blog/supabase-wrappers-v02)

[09 -Supabase Libraries V2](https://supabase.com/blog/client-libraries-v2)

[10 -Supabase x Fly.io](https://supabase.com/blog/postgres-on-fly-by-supabase)

[11 -Top 10 Launches of LWX](https://supabase.com/blog/launch-week-x-best-launches)

[Supabase Launch Week X Hackathon](https://supabase.com/blog/supabase-hackathon-lwx)

[Supabase Launch Week X Community Meetups](https://supabase.com/blog/community-meetups-lwx)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclient-libraries-v2&text=Supabase%20Libraries%20V2%3A%20Python%2C%20Swift%2C%20Kotlin%2C%20Flutter%2C%20and%20Typescript)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclient-libraries-v2&text=Supabase%20Libraries%20V2%3A%20Python%2C%20Swift%2C%20Kotlin%2C%20Flutter%2C%20and%20Typescript)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fclient-libraries-v2&t=Supabase%20Libraries%20V2%3A%20Python%2C%20Swift%2C%20Kotlin%2C%20Flutter%2C%20and%20Typescript)

[Last post\\
\\
**Top 10 Launches of LWX** \\
\\
19 December 2023](https://supabase.com/blog/launch-week-x-best-launches)

[Next post\\
\\
**Introducing Read Replicas** \\
\\
15 December 2023](https://supabase.com/blog/introducing-read-replicas)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Version 2, for all libraries](https://supabase.com/blog/client-libraries-v2#version-2-for-all-libraries)
- [Supabase Python v2](https://supabase.com/blog/client-libraries-v2#supabase-python-v2)
- [Supabase Swift v2](https://supabase.com/blog/client-libraries-v2#supabase-swift-v2)
- [Supabase Kotlin v2](https://supabase.com/blog/client-libraries-v2#supabase-kotlin-v2)
- [Typescript v2 updates](https://supabase.com/blog/client-libraries-v2#typescript-v2-updates)
- [Flutter v2 updates](https://supabase.com/blog/client-libraries-v2#flutter-v2-updates)
- [React Native and Expo support](https://supabase.com/blog/client-libraries-v2#react-native-and-expo-support)
- [Our approach to client libraries](https://supabase.com/blog/client-libraries-v2#our-approach-to-client-libraries)
  - [The Cathedral or the Bazaar?](https://supabase.com/blog/client-libraries-v2#the-cathedral-or-the-bazaar)
  - [Fostering the community](https://supabase.com/blog/client-libraries-v2#fostering-the-community)
  - [Modularity](https://supabase.com/blog/client-libraries-v2#modularity)
  - [Why not auto-generate the libraries?](https://supabase.com/blog/client-libraries-v2#why-not-auto-generate-the-libraries)
- [Get involved](https://supabase.com/blog/client-libraries-v2#get-involved)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclient-libraries-v2&text=Supabase%20Libraries%20V2%3A%20Python%2C%20Swift%2C%20Kotlin%2C%20Flutter%2C%20and%20Typescript)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclient-libraries-v2&text=Supabase%20Libraries%20V2%3A%20Python%2C%20Swift%2C%20Kotlin%2C%20Flutter%2C%20and%20Typescript)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fclient-libraries-v2&t=Supabase%20Libraries%20V2%3A%20Python%2C%20Swift%2C%20Kotlin%2C%20Flutter%2C%20and%20Typescript)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Diagram explaining Supabase community](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-client-libs%2Fcommunity-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Diagram explaining how Supabase is built behind the scenes](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-client-libs%2Fmodularity-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)