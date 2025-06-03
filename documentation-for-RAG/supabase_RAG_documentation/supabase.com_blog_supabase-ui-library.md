---
url: "https://supabase.com/blog/supabase-ui-library"
title: "Introducing the Supabase UI Library"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Introducing the Supabase UI Library

31 Mar 2025

•

5 minute read

[![Ivan Vasilov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fivasilov.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ivan VasilovEngineering](https://twitter.com/ivasilov)

[![Jonny Summers-Muir avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmildtomato.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jonny Summers-MuirProduct Design](https://github.com/mildtomato)

[![Saxon Fletcher avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaxonf.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Saxon FletcherProduct Design](https://github.com/saxonf)

[![Terry Sutton avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaltcod.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Terry SuttonEngineering](https://github.com/saltcod)

![Introducing the Supabase UI Library](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fthumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We're excited to release an [official Supabase UI Library](https://supabase.com/ui)—a collection of ready-to-use components built on top of [shadcn/ui](https://ui.shadcn.com/). Designed for flexibility, these components can be dropped into any Next.js, React Router, TanStack Start, or plain React app.

Announcing the Supabase UI Library - YouTube

Supabase

54.4K subscribers

[Announcing the Supabase UI Library](https://www.youtube.com/watch?v=2TIuUjkCDFE)

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

[Why am I seeing this?](https://support.google.com/youtube/answer/9004474?hl=en)

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=2TIuUjkCDFE "Watch on YouTube")

Installing components from the Supabase UI Library is as easy as installing a component from shadcn/ui.

![Install](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Finstall.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The library is 100% shadcn/ui compatible by leveraging the [component registry](https://x.com/shadcn/status/1829646556318089509) feature. It follows the conventions for theming and reuses existing components like buttons and inputs.

Our UI registry is a collection of reusable components designed for use in several popular React frameworks. Components are styled with shadcn/ui and Tailwind CSS and are completely customizable.

![UI Library files](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Ffolder-structure.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It's designed to take both the time and the pain out of building complex functionality like user sign-up in your apps. All components work with new or existing projects.

## What's included? [\#](https://supabase.com/blog/supabase-ui-library\#whats-included)

- [Supabase client](https://supabase.com/ui/docs/nextjs/client) initialization for client-side and server-side use
- [Password-based authentication](https://supabase.com/ui/docs/nextjs/password-based-auth)
- [File Upload Dropzone](https://supabase.com/ui/docs/nextjs/dropzone)
- [Realtime Cursor Sharing](https://supabase.com/ui/docs/nextjs/realtime-cursor)
- [Current User Avatar](https://supabase.com/ui/docs/nextjs/current-user-avatar)
- [Realtime Avatar Stack](https://supabase.com/ui/docs/nextjs/realtime-avatar-stack)
- [Realtime Chat](https://supabase.com/ui/docs/tanstack/realtime-chat)

We intend to release more Supabase UI Library components, and we'd love to get your feedback. Got a favorite component you want for your applications? Let us know on [X](https://x.com/supabase) or [Discord](https://discord.supabase.com/), or we'd be happy to get a [pull request](https://github.com/supabase/supabase).

Let's look at some of the components.

## Password-based authentication [\#](https://supabase.com/blog/supabase-ui-library\#password-based-authentication)

Setting up authentication in your projects can be complicated and time-consuming. The Password-Based Authentication block provides all the necessary components and pages to implement a secure, user-friendly authentication flow in your projects in seconds.

![Authentication files](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fsupabase-ui-password-based-auth-02.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It includes everything you need to get started—fully built components for signing up, signing in, resetting a password, and handling forgotten passwords. These components are styled, responsive, and production-ready out of the box, so you don't have to worry about the design or flow. Just drop them into your project, and you're ready to sign up users.

![Sign up](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fsupabase-ui-password-based-auth.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Easy file uploads [\#](https://supabase.com/blog/supabase-ui-library\#easy-file-uploads)

The File Upload Dropzone component lets you add file upload and storage in your application in seconds. It features drag-and-drop support,
multiple file uploads, file size and count limits, image previews and MIME type restrictions.

File upload components are often complicated to set up. Spend your time working on what happens after the files are on the server.

![File upload dropzone](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fsupabase-ui-dropzone.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Realtime cursor sharing [\#](https://supabase.com/blog/supabase-ui-library\#realtime-cursor-sharing)

The Realtime Cursor component gets you started building multiplayer experiences in your applications. You can just drop this component into your project and you're ready to use Realtime in seconds.

![Realtime cursors](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fsupabase-ui-realtime-cursors.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## See who's online [\#](https://supabase.com/blog/supabase-ui-library\#see-whos-online)

With the User Avatar and Realtime Avatar Stack components, you can add Realtime Presence to your apps in a few minutes. See who's online in your collaborative apps, just like in Notion or Figma.

![Who's Online](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fwhos-online.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Realtime Chat [\#](https://supabase.com/blog/supabase-ui-library\#realtime-chat)

The Realtime Chat component is a complete chat interface, letting users exchange messages in real-time within a shared room. It features real-time, low-latency updates, message synchronization, message persistence support, customizable message appearance, automatic scroll-to-bottom on new messages and more.

![Realtime Chat](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Frealtime-chat.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Rules for AI Code Editors for Supabase [\#](https://supabase.com/blog/supabase-ui-library\#rules-for-ai-code-editors-for-supabase)

Alongside our UI components, we're also shipping a curated set of LLM rules tailored for Supabase and Postgres. These rules help AI code editors understand and work with features like Row Level Security (RLS), Postgres functions, RLS policies, and Supabase Edge Functions. These rules help guide models toward best practices and valid syntax, improving your developer experience. Install them all in a single command.

* * *

## Why build on shadcn/ui? [\#](https://supabase.com/blog/supabase-ui-library\#why-build-on-shadcnui)

[Shadcn/ui](https://ui.shadcn.com/) has been the [top project](https://risingstars.js.org/2024/en#section-all) on JavaScript Rising Stars for two years running—and for good reason. It offers a unique approach: instead of installing a component library as a dependency, you copy and paste the actual component code into your project. You get complete control over customization, styling, and behavior, with components that feel like part of your project.

## Get started today [\#](https://supabase.com/blog/supabase-ui-library\#get-started-today)

Skip the boilerplate and long setup times—focus on what really matters: building and shipping fast. Explore the Supabase UI Component Library, drop it into your projects, and let us know what you think. Be sure to [submit components](https://github.com/orgs/supabase/discussions/34578) you want to see next!

Visit the [Supabase UI Library](https://supabase.com/ui).

[Launch Week 14](https://supabase.com/launch-week)

Mar 31 - Apr 04 '25

[Day 1 -Supabase UI Library](https://supabase.com/blog/supabase-ui-library)

[Day 2 -Supabase Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1)

[Day 3 -Realtime: Broadcast from Database](https://supabase.com/blog/realtime-broadcast-from-database)

[Day 4 -Declarative Schemas for Simpler Database Management](https://supabase.com/blog/declarative-schemas)

[Day 5 -Supabase MCP Server](https://supabase.com/blog/mcp-server)

Build Stage

[01 -Postgres Language Server](https://supabase.com/blog/postgres-language-server)

[02 -Supabase Auth: Bring Your Own Clerk](https://supabase.com/blog/clerk-tpa-pricing)

[03 -Automatic Embeddings in Postgres](https://supabase.com/blog/automatic-embeddings)

[04 -Keeping Tabs: What's New in Supabase Studio](https://supabase.com/blog/tabs-dashboard-updates)

[05 -Dedicated Poolers](https://supabase.com/blog/dedicated-poolers)

[06 -Data API Routes to Nearest Read Replica](https://supabase.com/blog/data-api-nearest-read-replica)

[Community Meetups](https://supabase.com/events?category=meetup)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ui-library&text=Introducing%20the%20Supabase%20UI%20Library)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ui-library&text=Introducing%20the%20Supabase%20UI%20Library)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ui-library&t=Introducing%20the%20Supabase%20UI%20Library)

[Last post\\
\\
**Automatic Embeddings in Postgres** \\
\\
1 April 2025](https://supabase.com/blog/automatic-embeddings)

[Next post\\
\\
**Supabase Auth: Bring Your Own Clerk** \\
\\
31 March 2025](https://supabase.com/blog/clerk-tpa-pricing)

[launch-week](https://supabase.com/blog/tags/launch-week) [design](https://supabase.com/blog/tags/design)

On this page

- [What's included?](https://supabase.com/blog/supabase-ui-library#whats-included)
- [Password-based authentication](https://supabase.com/blog/supabase-ui-library#password-based-authentication)
- [Easy file uploads](https://supabase.com/blog/supabase-ui-library#easy-file-uploads)
- [Realtime cursor sharing](https://supabase.com/blog/supabase-ui-library#realtime-cursor-sharing)
- [See who's online](https://supabase.com/blog/supabase-ui-library#see-whos-online)
- [Realtime Chat](https://supabase.com/blog/supabase-ui-library#realtime-chat)
- [Rules for AI Code Editors for Supabase](https://supabase.com/blog/supabase-ui-library#rules-for-ai-code-editors-for-supabase)
- [Why build on shadcn/ui?](https://supabase.com/blog/supabase-ui-library#why-build-on-shadcnui)
- [Get started today](https://supabase.com/blog/supabase-ui-library#get-started-today)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ui-library&text=Introducing%20the%20Supabase%20UI%20Library)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ui-library&text=Introducing%20the%20Supabase%20UI%20Library)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-ui-library&t=Introducing%20the%20Supabase%20UI%20Library)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Install](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Finstall.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![UI Library files](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Ffolder-structure.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Authentication files](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fsupabase-ui-password-based-auth-02.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Sign up](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fsupabase-ui-password-based-auth.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![File upload dropzone](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fsupabase-ui-dropzone.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Realtime cursors](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fsupabase-ui-realtime-cursors.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Who's Online](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Fwhos-online.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Realtime Chat](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-1-supabase-ui-library%2Frealtime-chat.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)