---
url: "https://supabase.com/blog/studio-introducing-assistant"
title: "Supabase Studio: AI Assistant and User Impersonation"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Studio: AI Assistant and User Impersonation

11 Dec 2023

•

10 minute read

[![Alaister Young avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Falaister.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Alaister YoungEngineering](https://github.com/alaister)

[![Ivan Vasilov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fivasilov.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ivan VasilovEngineering](https://twitter.com/ivasilov)

[![Joshen Lim avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjoshenlim.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Joshen LimEngineering](https://github.com/joshenlim)

![Supabase Studio: AI Assistant and User Impersonation](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2Fday-1-supabase-assistant-og.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

During the previous Launch Week we introduced text-to-sql in the SQL Editor within Supabase Studio. This was our first step towards a full AI Assistant.

Today, we're introducing the Supabase Assistant, an AI side-kick inside the dashboard, and a few new features that will take you from idea to production even faster.

Use AI to enable and generate RLS policies for Postgres with Supabase - YouTube

Supabase

54.4K subscribers

[Use AI to enable and generate RLS policies for Postgres with Supabase](https://www.youtube.com/watch?v=hu2SQjvCXIw)

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

[Watch on YouTube](https://www.youtube.com/watch?v=hu2SQjvCXIw "Watch on YouTube")

Here's the birds-eye-view:

- [**Row Level Security Policies**](https://supabase.com/blog/studio-introducing-assistant#easy-rls-policies-with-ai): made easy with AI
- [**Postgres Roles**](https://supabase.com/blog/studio-introducing-assistant#postgres-roles): change the Studio's Postgres role
- [**User Impersonation**](https://supabase.com/blog/studio-introducing-assistant#user-impersonation): visualize your security policies
- [**Realtime Inspector**](https://supabase.com/blog/studio-introducing-assistant#realtime-inspector): inspect and debug Realtime requests
- [**Feature Previews**](https://supabase.com/blog/studio-introducing-assistant#feature-previews): see what's hot off the press in Studio

## Introducing the Supabase Assistant [\#](https://supabase.com/blog/studio-introducing-assistant\#introducing-the-supabase-assistant)

We're excited to expand Studio's AI capabilities with our new **Supabase Assistant**.

Developers have been telling us that the text-to-sql feature inside the SQL Editor has dramatically increased their velocity (and their SQL abilities). AI is extremely powerful when combined with a schema-based database, like Postgres, because it can infer so much context from the schema and the database provides stricter guarantees with generated code. Our previous release solidified our belief that AI will be a key part of the future of database development.

Today, we're rolling out Assistant support in our Row Level Security editor and soon will expand to other places in Studio: the Table Editor, Postgres Functions, Serverless Functions, and more.

Let's jump in to Row Level Security first.

![Supabase AI Assistant](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fsupabase-ai-loading-animation.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Easy RLS Policies with AI [\#](https://supabase.com/blog/studio-introducing-assistant\#easy-rls-policies-with-ai)

Of all the feature requests we get (and we get many!), an easier way to write [Row Level Security](https://supabase.com/docs/guides/auth/row-level-security) Policies is one of the most frequent.

Row Level Security (RLS) is a Postgres feature that provides fine-grained access to your database. While RLS is powerful, writing Policies can be a chore. Today, we're releasing an AI-powered RLS Editor that makes it simple to write security policies.

The new RLS Editor brings SQL front-and-center. We want to give developers access to the full potential of Postgres, rather than abstracting it away. This editor is really two tools:

1. A SQL Editor: if you know SQL really well, there's a new editor for you to quickly write your policies.
2. An Assistant: if you're new to RLS and need some help, you can use the Assistant and chat your way through it.

![Supabase new AI Assistant](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The Assistant has been tuned to produce SQL for Row Level Security, making it fast and easy to get your policies setup the way you need them.

We've explored various approaches and designs for the RLS Editor. This SQL-first approach, with assistance from AI, feels like the solution we've been seeking. The new RLS Editor can be enabled today via Feature Previews (more on that below). We'd love to [hear your feedback](https://github.com/orgs/supabase/discussions/19594).

## Postgres Roles [\#](https://supabase.com/blog/studio-introducing-assistant\#postgres-roles)

You may have never thought about this, but Studio connects to your database just like any other Postgres client.

It uses the default [Postgres role](https://supabase.com/docs/guides/database/postgres/roles), `postgres`. The `postgres` role functions like your `service role` key, granting it admin privileges to your database. It has admin read and write privileges, and bypasses Row Level Security.

If you use our client libs, you'll be familiar with the `anon` and `service_role` API keys. These keys actually resolve into Postgres roles, also called `anon` and `service_role`. These keys are actually JWT tokens that contain the Postgres role:

`
{
"role": "service_role", // the Postgres role
"iss": "supabase"       // the issuer of the JWT
"exp": 1445385600,      // the time the JWT will expire
}
`

What if you could run the queries in Studio using the same Postgres roles you use in your applications? What if you could have the Studio pretend to use a different role than the default `postgres` role? Today, you can:

![Supabase new postgres roles](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can use the new Role dropdown to select a different Postgres role for your queries in Studio. This is a powerful tool for testing your Row Level Security policies and determining which data each role can access.

Let's build a Twitter/X clone to illustrate. In a Twitter clone, you:

- have a `tweets` table with columns like `user_id` and `content`.
- can set up Row Level Security so that only the author of a tweet can access and modify their own tweets.
- can only see and edit the tweets you've authored

Here's our tweets table. Watch the table react when we change roles:

When we query with the `postgres` role, we can see all the data. When we query with the `anon` no data is returned. This makes sense as we haven't yet created a policy to allow for `anon` access to this table.

The Role dropdown unlocks another handy capability: when combined with Supabase Auth it can even pretend to be a different _user_.

## User Impersonation [\#](https://supabase.com/blog/studio-introducing-assistant\#user-impersonation)

Remember the API keys above? They can contain an additional field: `sub`. This is the user's ID. When you use the `authenticated` role, the `sub` field is the ID of the user who is logged in to your app:

`
{
"sub": "348b-some-user-uuid", // the ID of the user
"role": "authenticated",      // the Postgres role
"iss": "supabase"             // the issuer of the JWT
"exp": 1445385600,            // the time the JWT will expires
}
`

We can impersonate a user in Studio by "minting" a JWT with their ID and then running the queries using that JWT.

Let's see it in action after we've written an RLS policy to allow users to view _their own_ tweets. Here, we can choose the `authenticated` role, and select a specific user to see just their tweets. Here's all of our user's tweets:

![Supabase AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F7.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The Table Editor is now impersonating our user.

You can impersonate any user in your project and see things exactly as they would. Any conditions in your RLS policies will be automatically reflected here in the table.

✨ Magic ✨

You can create RLS policies and test that they work exactly as you expect, right from the Studio.

The fun doesn't stop with the Table Editor. We've added Roles support to both the SQL Editor and GraphiQL as well. Let's repeat what we've done above by trying to select a list of our own tweets in the SQL Editor:

![Supabase AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F8.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

And in GraphiQL:

![Supabase AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F11.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Combining this feature with the new RLS Editor, you're able to write and test RLS policies with real data in a matter of minutes. This makes the process of writing RLS policies many times faster and easier. If you've got feedback, [we'd love to hear it](https://github.com/orgs/supabase/discussions/19595).

## Realtime Inspector [\#](https://supabase.com/blog/studio-introducing-assistant\#realtime-inspector)

Supabase [Realtime](https://supabase.com/realtime) is great for building collaborative applications. You can receive database changes over websockets, store and synchronize data about user presence, and broadcast any data to clients via "channels".

Today we're releasing Realtime Inspector: an easy way to prototype, inspect, and debug Realtime directly in the Studio. You can use the Realtime Inspector to view messages being sent and received in channels. You can filter messages by type: presence, broadcast, and database changes.

![Supabase AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F6.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

And, of course, we've included the Roles dropdown here as well. You can view events by role and impersonate users just like the Table and SQL Editors.

If you use Realtime, you'll find the new inspector very handy. Please send along any [feedback](https://github.com/orgs/supabase/discussions/19596) you've got.

* * *

## Feature Previews [\#](https://supabase.com/blog/studio-introducing-assistant\#feature-previews)

Today we're releasing **Feature Previews**, our tool for unveiling new features. We release beta features as Previews before making them generally available. You can see a list of features that are available for preview along with a screenshot and a brief description. Each feature includes a link to a Github Discussion for feedback.

We have a couple of goals with Feature Previews. We want to:

- get features out to you faster
- make it easier for you to give us feedback
- shorten the iteration loop

The faster we can iterate with your feedback, the faster we can release features into general use.

While we consider these features to be beta releases, please know that we take your security, privacy and data integrity extremely seriously. Anything we release to Preview is tested with this in mind and is at a stage where we're looking for UX/UI feedback.

You can find our Feature Preview under the user avatar menu in the lower left:

![Supabase AI Feature Preview](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F4.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We currently have two features in preview:

`1.` The new RLS Assistant that we looked at earlier:

![Supabase AI new RLS Assistant](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F5.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

`2.` And a revised API side panel:

![Supabase AI revised API side panel](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F10.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We'll be actively keeping an eye on the Github Discussions and will be responding to your feedback.

## Wrapping up [\#](https://supabase.com/blog/studio-introducing-assistant\#wrapping-up)

In this update, we've taken huge strides in enhancing your experience with Supabase.

1. **Row Level Security Policies**: We've made it easier than ever to create Row Level Security policies with the help of our new Assistant. This feature dramatically simplifies the process of defining fine-grained access to your data.

2. **Postgres Roles and User Impersonation**: Our new Roles selector allows you to visualize the impact of your security policies directly within the Studio. This lets you to see how different roles interact with your data, offering a powerful tool for testing access control.

3. **Realtime Inspector**: With the Realtime Inspector, you can prototype, inspect, and debug Realtime messages. This tool will be very useful for those who use Supabase Realtime.

4. **Feature Previews**: We've introduced Feature Previews to bring you new tools and features in the beta stage, making it easier for you to provide feedback and shape the development process.


These updates reflect our commitment to a SQL-first approach and a user-centric development. We look forward to your feedback as we continue to work hard making Supabase faster and easier for you to get your ideas out into the wild.

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fstudio-introducing-assistant&text=Supabase%20Studio%3A%20AI%20Assistant%20and%20User%20Impersonation)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fstudio-introducing-assistant&text=Supabase%20Studio%3A%20AI%20Assistant%20and%20User%20Impersonation)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fstudio-introducing-assistant&t=Supabase%20Studio%3A%20AI%20Assistant%20and%20User%20Impersonation)

[Last post\\
\\
**pg\_graphql: Postgres functions now supported** \\
\\
12 December 2023](https://supabase.com/blog/pg-graphql-postgres-functions)

[Next post\\
\\
**How design works at Supabase** \\
\\
8 December 2023](https://supabase.com/blog/how-design-works-at-supabase)

[launch-week](https://supabase.com/blog/tags/launch-week) [studio](https://supabase.com/blog/tags/studio)

On this page

- [Introducing the Supabase Assistant](https://supabase.com/blog/studio-introducing-assistant#introducing-the-supabase-assistant)
- [Easy RLS Policies with AI](https://supabase.com/blog/studio-introducing-assistant#easy-rls-policies-with-ai)
- [Postgres Roles](https://supabase.com/blog/studio-introducing-assistant#postgres-roles)
- [User Impersonation](https://supabase.com/blog/studio-introducing-assistant#user-impersonation)
- [Realtime Inspector](https://supabase.com/blog/studio-introducing-assistant#realtime-inspector)
- [Feature Previews](https://supabase.com/blog/studio-introducing-assistant#feature-previews)
- [Wrapping up](https://supabase.com/blog/studio-introducing-assistant#wrapping-up)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fstudio-introducing-assistant&text=Supabase%20Studio%3A%20AI%20Assistant%20and%20User%20Impersonation)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fstudio-introducing-assistant&text=Supabase%20Studio%3A%20AI%20Assistant%20and%20User%20Impersonation)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fstudio-introducing-assistant&t=Supabase%20Studio%3A%20AI%20Assistant%20and%20User%20Impersonation)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Supabase new AI Assistant](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase new postgres roles](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F3.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F7.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F8.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F11.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase AI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F6.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase AI Feature Preview](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F4.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase AI new RLS Assistant](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F5.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase AI revised API side panel](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-1%2F10.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)