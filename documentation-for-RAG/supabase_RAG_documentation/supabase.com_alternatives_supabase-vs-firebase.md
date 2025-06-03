---
url: "https://supabase.com/alternatives/supabase-vs-firebase"
title: "Supabase vs Firebase"
---

Alternative

# Supabase vs Firebase

2022-05-26

•

4 minute read

[![author avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

## What is Firebase? [\#](https://supabase.com/alternatives/supabase-vs-firebase\#what-is-firebase)

Now owned by Google, Firebase is a collection of tools aimed at mobile and web developers. At its core is the Firestore database.

Firestore allows you to store “documents”. These are collections of key:value pairs where the value can be another sub-document. Document based storage is perfect for unstructured data, since two documents in a collection do not necessarily need to have the same structure.

Firebase also offers other things that web developers find useful like an auth service for user management, and wrappers for other Google services such as Cloud Functions, and File Storage.

## What is Supabase? [\#](https://supabase.com/alternatives/supabase-vs-firebase\#what-is-supabase)

Supabase is an open source firebase alternative, but instead of being built around a document-based datastore, Supabase offers a relational database management system called PostgreSQL. This comes with a few advantages:

- It’s open source, so there is zero lock in.
- You can query it with SQL, a proven and powerful query language.
- It has a long track record of being used at scale.
- It’s the database of choice for transactional workloads (think apps and websites, or other things that require near-instant responses to queries).
- It comes with decades of [useful postgres extensions and plug-ins](https://supabase.com/docs/guides/database/extensions).

At Supabase we’ve always been huge fans of Firebase - so we started adding a few things on top of PostgreSQL in an attempt to reach feature parity, including:

- Auto-generated API - [query your data straight from the client](https://supabase.com/docs/guides/api#rest-api-overview).
- Realtime - [changes in your data will be streamed directly to your application](https://supabase.com/docs/reference/dart/subscribe).
- Auth - [a simple to integrate auth system and SQL based rules engine](https://supabase.com/auth).
- Functions - [javascript and typescript functions that deploy out globally](https://supabase.com/edge-functions).
- Storage - [hosting images, videos, and pdfs easily](https://supabase.com/storage).

## How are they similar? [\#](https://supabase.com/alternatives/supabase-vs-firebase\#how-are-they-similar)

Both Firebase and Supabase are based on the idea of bringing a superior developer experience to databases. With both platforms you can spin up a new project from directly inside the browser without the need to download any extra tools or software to your machine. Both platforms come with a useful dashboard UI for debugging your data in realtime, which is especially useful for fast iterations when in development.

Both Firebase and Supabase have invested heavily in client side libraries so you can communicate with your database directly from the client. Firebase has their [Firebase Javascript SDK](https://github.com/firebase/firebase-js-sdk) and Supabase has [supabase-js an isomorphic client](https://github.com/supabase/supabase-js/) that can be used both on the client also on the server in a node-js environment.

## How are they different? [\#](https://supabase.com/alternatives/supabase-vs-firebase\#how-are-they-different)

Firebase and Supabase differ in several ways. The main one being that Firebase is a document store, whereas Supabase is based on PostgreSQL - a relational, SQL-based database management system.

There are some other important differences.

### Open Source [\#](https://supabase.com/alternatives/supabase-vs-firebase\#open-source)

Supabase is open source. Along with the hosted cloud platform, you can also take the Supabase stack and host it inside your own cloud or run it locally on your machine. There is no vendor lock in.

### Pricing [\#](https://supabase.com/alternatives/supabase-vs-firebase\#pricing)

[Firebase charges for reads, writes and deletes](https://firebase.google.com/pricing), which can lead to some unpredictability, especially in the early stages of a project when your application is in heavy development. Supabase [charges based on the amount of data stored](https://supabase.com/pricing), with breathing room for unlimited API requests and an unlimited number of Auth users.

### Performance [\#](https://supabase.com/alternatives/supabase-vs-firebase\#performance)

We created a benchmarking repo where you can compare the performance of both services in different scenarios. Our most recent results show that [Supabase outperforms Firebase by up to 4x](https://github.com/supabase/benchmarks/issues/8) on number of reads per second, and 3.1x on writes per second.

## How do I migrate from Firebase to Supabase? [\#](https://supabase.com/alternatives/supabase-vs-firebase\#how-do-i-migrate-from-firebase-to-supabase)

Since Firebase is document based, migrating into a relational database requires you to map your data structure across into a SQL schema. Luckily we’ve built a [handy conversion tool to do it for you](https://supabase.com/docs/guides/migrations/firestore-data).

We also have guides and tools for [migrating Firebase Auth to Supabase Auth](https://supabase.com/docs/guides/migrations/firebase-auth) for [migrating Firebase Storage files to Supabase Storage](https://supabase.com/docs/guides/migrations/firebase-storage).

These are by far the most complete Firebase to Postgres migration tools available anywhere on the web.

You can [try Supabase for free](https://supabase.com/dashboard). If you require Enterprise level support with your project or migration, please get in touch using our [Enterprise contact form](https://forms.supabase.com/enterprise).

Share this article

[Previous comparison\\
\\
**Supabase vs Auth0** \\
\\
2023-11-24](https://supabase.com/alternatives/supabase-vs-auth0)

[Next comparison\\
\\
**Supabase vs Heroku Postgres** \\
\\
2022-05-26](https://supabase.com/alternatives/supabase-vs-heroku-postgres)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)