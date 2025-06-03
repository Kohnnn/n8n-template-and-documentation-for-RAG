---
url: "https://supabase.com/blog/supabase-book-by-david-lorenz"
title: "The Supabase Book by David Lorenz"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# The Supabase Book by David Lorenz

16 Aug 2024

•

6 minute read

[![David Lorenz avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Factivenode.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
David LorenzGuest Author](https://github.com/activenode)

![The Supabase Book by David Lorenz](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fsupabase-book%2Fthumb_supabse_book.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

> Hey folks. We're excited to share David's new guide to learning Supabase. He's spent a year
> working on it and we think it's one of the most thorough Supabase resources on the internet. If
> you're interested in leveling up your Supabase skills, you can support David and [purchase the book here](https://supa.guide/). Enjoy!
>
> ![Paul Copplestone, CEO @ Supabase avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fpaul-copplestone.jpg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Paul Copplestone, CEO @ Supabase

## Background [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#background)

Let me introduce myself, I'm David Lorenz, not a Supabase team member, but a Supabase user from the very early days. On the net you might know me as [@activenode](https://x.com/activenode/). I'm a software architect who's been building web apps for over two decades now—ever since I picked up my first HTML book at the age of 11.

I gravitate towards technologies that are flexible and portable. Proprietary solutions like Firebase, which bind clients to a single provider, simply don't align with my philosophy.

Supabase caught my attention from the get-go. A superpowered database with just Postgres under the hood—and I'm not locked in. But let's jump to why I wrote a book.

The Supabase Book: an interview with David Lorenz - YouTube

Supabase

54.4K subscribers

[The Supabase Book: an interview with David Lorenz](https://www.youtube.com/watch?v=ISFCooRMvbE)

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

[Watch on YouTube](https://www.youtube.com/watch?v=ISFCooRMvbE "Watch on YouTube")

## Why this book needed to exist [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#why-this-book-needed-to-exist)

Due to my presence on the web, I'm often in touch with people using Supabase through consultancy calls or on social media. Through these conversations I've run into many similar questions and discovered that although there are so many great resources for learning Supabase, many have repeated exercises and open questions. I felt there wasn't **that one resource** which you go through and then say “I know Supabase inside and out”. This book aims to change that.

Let's talk about the chosen approach next.

## Approach [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#approach)

When I first set out to write this book, I found myself asking, "How can I possibly satisfy everyone's expectations?" After hours of brainstorming and sketching out concepts, I realized I was asking the wrong question. Instead of trying to satisfy everyone's expectations, I needed to focus on finding the best way to truly teach Supabase so that after completing the book, readers could build anything they imagined.

It had be a full project, 0 to 100, explaining why things were done the way they were done. I decided on a Multi-Tenant Ticket Management system: this would allow me to explain rationally-modelled database design and clever file management, as well as what it means to work with multiple tenants in the same Supabase instance and how to optimize for that.

And because I felt it was most useful to walk through the project front to back, I had to choose a framework. For creating a UI, I decided to use Pico.css as it's one of the very rare CSS libraries that allow us to simply use basic HTML elements to create a UI.

For the business logic I chose Next.js as being not only one of the most popular frameworks but also providing ease of use without a lot of foundational setup.

Now let's have a look at what you'll take away.

## Goal / What you will learn [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#goal--what-you-will-learn)

One high-level goal of mine with the book is that even someone who thinks they _know_ Supabase, will have aha moments in every single chapter.

The book is divided into four parts with thirteen chapters in total and adds up to 500+ pages. Let's have a look at the parts:

### 1\. Creating the Foundations of the Ticket System App [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#1-creating-the-foundations-of-the-ticket-system-app)

We kick things off with an introduction, unveiling Supabase's “secret” sauce and history. Then you'll take a short trip through permission systems and learn how Supabase compares to traditional FGA and RBAC systems. From there, you'll setup Supabase locally, learn about its API and Keys, then create the initial layout with Pico to get started.

### 2\. **Adding Multi-Tenancy and Learning RLS** [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#2-adding-multi-tenancy-and-learning-rls)

Pass me the key to your house! Or should I say all of them - or none? Here we'll talk authentication and permissions in a multi-tenant world. After you add a login and learn how to authenticate with fully customised emails, you'll craft the database and app to become multi-tenant-aware. Then you'll learn about RLS complexity optimisation and working with external Auth providers.

### 3\. Managing Tickets and Interactions [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#3-managing-tickets-and-interactions)

Making things interactive is what this part is about: we'll add ticket data, sort it, filter it, and paginate it. We create performance-optimized RLS queries, add triggers for caching, and embrace realtime comments on tickets that include file uploads. There's much more too, e.g. learning how you can add plan-based storage restrictions for a user.

### 4\. **Diving Deeper into Security and Advanced Features** [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#4-diving-deeper-into-security-and-advanced-features)

In this part, things get more technical. These two chapters are packed with additional knowledge, covering advanced security aspects, techniques for hardening or cloaking your instance, Edge functions, environment-based webhooks, and creating an AI-based search. It's impossible to list everything covered in this part, but it will undoubtedly provide you with new perspectives on how to leverage Supabase's full potential.

## How to get the most out of this book [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#how-to-get-the-most-out-of-this-book)

This book is a deep dive so to make the most of it will take some time. During my step-by-step review of the book, it took me a little less than a full week to complete everything. So plan to spend about half a day per chapter with some extra time for any troubleshooting. If you do that, I can promise, you'll walk away with exceptional knowledge that sets you apart from the crowd. And the time you spend studying the book will be dwarfed by the time you'll save on future projects.

If you need breaks in between, it's best to finish an entire chapter before taking a pause. This way, you can digest the knowledge from that chapter in its completeness. Another opportune time for reflection is between the four main parts of the book.

## What if I face problems? [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#what-if-i-face-problems)

Let's use the power of the community. I've created a Discord channel where I'm active and where you can exchange ideas with other people reading the book. Find the link below.

## What else? [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#what-else)

I've invested one year of my life into this book and I'd love feedback of all kinds! You can find me and tag me on social media, I have the username `@activenode` on every platform. Also you'll find all of the contact data at [https://activeno.de](https://activeno.de/).

If you like the book, please spread the word. You can also book me as Supabase consultant and Architect for your next gig.

## Links [\#](https://supabase.com/blog/supabase-book-by-david-lorenz\#links)

The original page and newsletter: [https://supa.guide](https://supa.guide/)

Book Discord: [https://supa.guide/discord?ref=supabase](https://supa.guide/discord?ref=supabase) (tbl [https://discord.gg/qhAAYwKx3f](https://discord.gg/qhAAYwKx3f) )

Buy the book: [https://supa.guide/buy?ref=supabase](https://supa.guide/buy?ref=supabase)

[Launch Week12](https://supabase.com/launch-week/12)

12-16 August

[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)

[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)

[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)

[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)

[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage

[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)

[02 -pg\_replicate](https://news.ycombinator.com/item?id=41209994)

[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)

[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)

[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)

[06 -vec2pg](https://supabase.com/blog/vec2pg)

[07 -pg\_graphql](https://supabase.com/blog/pg-graphql-1-5-7)

[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)

[09 -python-support](https://supabase.com/blog/python-support)

[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)

[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-book-by-david-lorenz&text=The%20Supabase%20Book%20by%20David%20Lorenz)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-book-by-david-lorenz&text=The%20Supabase%20Book%20by%20David%20Lorenz)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-book-by-david-lorenz&t=The%20Supabase%20Book%20by%20David%20Lorenz)

[Last post\\
\\
**Supabase Python** \\
\\
16 August 2024](https://supabase.com/blog/python-support)

[Next post\\
\\
**vec2pg: Migrate to pgvector from Pinecone and Qdrant** \\
\\
16 August 2024](https://supabase.com/blog/vec2pg)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Background](https://supabase.com/blog/supabase-book-by-david-lorenz#background)
- [Why this book needed to exist](https://supabase.com/blog/supabase-book-by-david-lorenz#why-this-book-needed-to-exist)
- [Approach](https://supabase.com/blog/supabase-book-by-david-lorenz#approach)
- [Goal / What you will learn](https://supabase.com/blog/supabase-book-by-david-lorenz#goal--what-you-will-learn)
- [How to get the most out of this book](https://supabase.com/blog/supabase-book-by-david-lorenz#how-to-get-the-most-out-of-this-book)
- [What if I face problems?](https://supabase.com/blog/supabase-book-by-david-lorenz#what-if-i-face-problems)
- [What else?](https://supabase.com/blog/supabase-book-by-david-lorenz#what-else)
- [Links](https://supabase.com/blog/supabase-book-by-david-lorenz#links)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-book-by-david-lorenz&text=The%20Supabase%20Book%20by%20David%20Lorenz)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-book-by-david-lorenz&text=The%20Supabase%20Book%20by%20David%20Lorenz)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-book-by-david-lorenz&t=The%20Supabase%20Book%20by%20David%20Lorenz)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)