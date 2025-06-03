---
url: "https://supabase.com/blog/supabase-realtime-with-multiplayer-features"
title: "Supabase Realtime, with Multiplayer Features"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Realtime, with Multiplayer Features

01 Apr 2022

•

3 minute read

[![Wen Bo Xie avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fw3b6x9.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Wen Bo XieProduct](https://twitter.com/wenboxie)

![Supabase Realtime, with Multiplayer Features](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Ffriday-realtime%2Fmultiplayer-realtime-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today is the 1st of April, or April Fool's Day, but I like to think of today as Supabase Realtime Day where we announce and demo the next version of Realtime.

Here's the next version of Realtime, with multiplayer features.

Supabase Realtime, with Multiplayer Features - YouTube

Supabase

54.4K subscribers

[Supabase Realtime, with Multiplayer Features](https://www.youtube.com/watch?v=BelYEMJ2N00)

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

[Watch on YouTube](https://www.youtube.com/watch?v=BelYEMJ2N00 "Watch on YouTube")

We've made quite a few iterations on Realtime in the past. The first major version of Realtime listened to a single database by streaming changes from PostgreSQL's Write-Ahead Log and sending them to clients via WebSockets. The second major version introduced better security via WALRUS (Write Ahead Log Realtime Unified Security) which adheres to a database's RLS policies to determine authorized clients. However, this version continues to be single tenant as it can only poll one database at a time.

The next and third major version, announced today on new Supabase Realtime Day, introduces multi-tenancy to listen to many databases. Additionally, this new version introduces a distributed cluster of nodes, which introduces better resource utilization, fault-tolerance, and lower latencies that directly translates to better performance for developers. We're fortunate to have built Realtime on Elixir and Phoenix, as the language and framework are great for concurrency, distributed computing, and WebSockets. We'll continue to support the existing Realtime feature of listening to database changes, but now we're also introducing the ability for developers to use WebSockets to build multiplayer games, collaborative apps, and support a wide array of use cases.

## New Features [\#](https://supabase.com/blog/supabase-realtime-with-multiplayer-features\#new-features)

### Presence [\#](https://supabase.com/blog/supabase-realtime-with-multiplayer-features\#presence)

![realtime-multiplayer-presence.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Ffriday-realtime%2Frealtime-multiplayer-presence.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Presence is great for showing when your users are online. When a user connects or disconnects (even accidentally!), the server automatically detects this and let's everyone else know.
Presence is powered by [CRDTs](https://crdt.tech/) (Conflict-free Replicated Data Type) on a distributed cluster useful for storing synced data across nodes.

### Broadcast [\#](https://supabase.com/blog/supabase-realtime-with-multiplayer-features\#broadcast)

![realtime-multiplayer-broadcast.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Ffriday-realtime%2Frealtime-multiplayer-broadcast.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Broadcasts are perfect for sending ephemeral events, like cursor movements. It's incredibly useful for gaming where you need to send messages across all connected users without storing them in the database.
In Realtime, connected users communicate with other subscribing & publishing to topics.

### Extensions [\#](https://supabase.com/blog/supabase-realtime-with-multiplayer-features\#extensions)

In this version of Realtime we're re-architecting the way that we listen to PostgreSQL databases by opening the WebSocket functionality for general use.
Instead of only using WebSockets to broadcast database changes, we are now moving the PostgreSQL listener to an “extension” architecture. This opens up numerous new ways of extending the server.
Here are just a few that we've heard:

- Multiple Postgres: listen to multiple PostgreSQL databases at the same time.
- Other databases: Listen to database changes from other databases, like MySQL.
- Finance: Listen to stock market events and broadcast them to connected users.
- Web3: Listen to blockchain events and broadcast them to connected users.
- A server clock which broadcasts a timer to every connected client (e.g. auction sites)

We're extremely excited about what the community develops.

## Demo [\#](https://supabase.com/blog/supabase-realtime-with-multiplayer-features\#demo)

To show off the functionality that we're releasing, we've built a demo application.

[multiplayer.dev](https://multiplayer.dev/)

Tech stack:

- [Realtime](https://github.com/supabase/realtime), powered by the [Phoenix Web Framework](https://www.phoenixframework.org/) and [Elixir](https://elixir-lang.org/).
- [Next.js](https://nextjs.org/) by [Vercel](https://vercel.com/).
- Deployed on a [Fly.io](https://fly.io/) \- cluster of 20 nodes distributed around the world 🌍.

## Getting started [\#](https://supabase.com/blog/supabase-realtime-with-multiplayer-features\#getting-started)

Sign up for the waitlist at [multiplayer.dev](https://multiplayer.dev/).

You can follow development in our [open source repository on GitHub](https://github.com/supabase/realtime/tree/develop).

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-with-multiplayer-features&text=Supabase%20Realtime%2C%20with%20Multiplayer%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-with-multiplayer-features&text=Supabase%20Realtime%2C%20with%20Multiplayer%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-with-multiplayer-features&t=Supabase%20Realtime%2C%20with%20Multiplayer%20Features)

[Last post\\
\\
**Supabase Beta March 2022** \\
\\
15 April 2022](https://supabase.com/blog/beta-update-march-2022)

[Next post\\
\\
**Hackathon: Bring the Func(🕺)** \\
\\
1 April 2022](https://supabase.com/blog/hackathon-bring-the-func)

[launch-week](https://supabase.com/blog/tags/launch-week) [realtime](https://supabase.com/blog/tags/realtime)

On this page

- [New Features](https://supabase.com/blog/supabase-realtime-with-multiplayer-features#new-features)
  - [Presence](https://supabase.com/blog/supabase-realtime-with-multiplayer-features#presence)
  - [Broadcast](https://supabase.com/blog/supabase-realtime-with-multiplayer-features#broadcast)
  - [Extensions](https://supabase.com/blog/supabase-realtime-with-multiplayer-features#extensions)
- [Demo](https://supabase.com/blog/supabase-realtime-with-multiplayer-features#demo)
- [Getting started](https://supabase.com/blog/supabase-realtime-with-multiplayer-features#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-with-multiplayer-features&text=Supabase%20Realtime%2C%20with%20Multiplayer%20Features)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-with-multiplayer-features&text=Supabase%20Realtime%2C%20with%20Multiplayer%20Features)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-with-multiplayer-features&t=Supabase%20Realtime%2C%20with%20Multiplayer%20Features)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)