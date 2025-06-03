---
url: "https://supabase.com/blog/edge-functions-node-npm"
title: "Edge Functions: Node and native npm compatibility"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Edge Functions: Node and native npm compatibility

12 Dec 2023

•

6 minute read

[![Lakshan Perera avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Flaktek.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Lakshan PereraEngineering](https://github.com/laktek)

[![Andrees Pirela avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fandreespirela.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Andrees PirelaEngineering](https://github.com/andreespirela)

![Edge Functions: Node and native npm compatibility](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-2%2Fedge-runtime-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We are excited to announce that [Edge Functions](https://supabase.com/docs/guides/functions) now natively supports npm modules and Node built-in APIs. You can directly import millions of popular, commonly used npm modules into your Edge Functions.

`
import { drizzle } from 'npm:drizzle-orm/node-postgres'
`

## Migrate existing Node apps to Edge Functions [\#](https://supabase.com/blog/edge-functions-node-npm\#migrate-existing-node-apps-to-edge-functions)

You can migrate your existing Node apps to Supabase Edge Functions with minimal changes.

We created a demo to show how to migrate a Node app that uses Express, Node Postgres, and Drizzle. For more information on using npm modules and Node built-ins within your Edge Functions, see the [Managing dependencies guide](https://supabase.com/docs/guides/functions/dependencies).

Node compatibility just got a lot better in Deno - YouTube

Supabase

54.4K subscribers

[Node compatibility just got a lot better in Deno](https://www.youtube.com/watch?v=eCbiywoDORw)

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

[Watch on YouTube](https://www.youtube.com/watch?v=eCbiywoDORw "Watch on YouTube")

## How npm modules work under the hood [\#](https://supabase.com/blog/edge-functions-node-npm\#how-npm-modules-work-under-the-hood)

We run an open source Deno server for hosting Edge Functions called [Supabase Edge Runtime](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions). This custom version helps us keep Edge Functions working the same way no matter where it is deployed - on our hosted platform, in local development, or in your self-hosted environment.

The biggest challenge when adding npm support was finding an approach that would work across all environments. We wanted to keep the workflow close to the Deno CLI experience. It should be possible to import npm modules directly in your source code without an extra build step.

When deploying a Function, we serialize its module graph into a single file format (an [eszip](https://github.com/denoland/eszip)). In the hosted environment, all module references are then loaded from the eszip. This prevents any extra latency in fetching modules and potential conflicts between module dependencies.

We used the eszip module loader in the local and self-hosted environments too, so we only need to implement one module-loading strategy for all environments. As an additional benefit for local development, this approach avoids potential conflicts with npm modules installed in the user's system since the Edge Function's npm modules are self-contained within the eszip.

[Refactoring the module loader](https://github.com/supabase/edge-runtime/pull/223) fixes a few other bugs, such [edge functions erroring out](https://github.com/supabase/cli/issues/1584#issuecomment-1848799355) when an `deno.lock` file is already present in the project.

## A few other things you've asked for… [\#](https://supabase.com/blog/edge-functions-node-npm\#a-few-other-things-youve-asked-for)

### Regional Invocations [\#](https://supabase.com/blog/edge-functions-node-npm\#regional-invocations)

You now have the option to specify a region when running an Edge Function (perhaps we should change the name in the future). Usually, Edge Functions run in the region closest to the user invoking the Function. However, sometimes you want to run it closer to your Postgres database or another 3rd party API for optimal performance.

Functions are still deployed to all regions. However, during invocation, you can provide the `x-region` header to restrict the execution to a specific region.

cURL

JavaScript

`
# https://supabase.com/docs/guides/functions/deploy#invoking-remote-functions
curl --request POST 'https://<project_ref>.supabase.co/functions/v1/hello-world' \
  --header 'Authorization: Bearer ANON_KEY' \
  --header 'Content-Type: application/json' \
  --header 'x-region: eu-west-3' \
  --data '{ "name":"Functions" }'
`

ℹ️ Check out the [Regional Invocation guide](https://supabase.com/docs/guides/functions/regional-invocation) for more details.

### Better Metrics [\#](https://supabase.com/blog/edge-functions-node-npm\#better-metrics)

We've added more metrics in the Edge Functions section of the [Supabase Dashboard](https://supabase.com/dashboard/project/_/functions): it now shows CPU time and memory used. We've also broken down invocations by HTTP status codes.

These changes help you spot any issues with your Edge Functions and act on them.

ℹ️ See the [logging and metrics guide](https://supabase.com/docs/guides/functions/debugging) for Edge Functions to learn more.

![Supabase Dashboard - Edge Functions metrics view](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-2%2F1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Track errors with Sentry [\#](https://supabase.com/blog/edge-functions-node-npm\#track-errors-with-sentry)

Our friends at Sentry recently shipped an official [Sentry SDK for Deno](https://deno.land/x/sentry@7.76.0). With this, it's now easy to track errors and exceptions in your edge functions in Sentry.

Here is a simple example of how to handle exceptions within your function and send them to Sentry.

``
import * as Sentry from 'https://deno.land/x/sentry/index.mjs'
Sentry.init({
dsn: _DSN_,
integrations: [],
// Performance Monitoring
tracesSampleRate: 1.0,
// Set sampling rate for profiling - this is relative to tracesSampleRate
profilesSampleRate: 1.0,
})
// Set region and execution_id as custom tags
Sentry.setTag('region', Deno.env.get('SB_REGION'))
Sentry.setTag('execution_id', Deno.env.get('SB_EXECUTION_ID'))
Deno.serve(async (req) => {
try {
    const { name } = await req.json()
    const data = {
      message: `Hello ${name}!`,
    }
    return new Response(JSON.stringify(data), { headers: { 'Content-Type': 'application/json' } })
} catch (e) {
    Sentry.captureException(e)
    return new Response(JSON.stringify({ msg: 'error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
}
})
``

## What's next [\#](https://supabase.com/blog/edge-functions-node-npm\#whats-next)

NPM support was one of the most requested features for Edge Functions. If you couldn't use Edge Functions previously because of the lack of support, we hope this update will entice you to [try it again](https://supabase.com/dashboard/project/_/functions). If you run into any issues, we are just [one support request away](https://supabase.help/).

For existing Edge Functions users, regional invocations, better metrics, and error handling are just a glimpse of what will come next. We continue to iterate on platform stability and setting custom limits on resources Edge Functions can use. Watch out for another blog post in the new year.

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-node-npm&text=Edge%20Functions%3A%20Node%20and%20native%20npm%20compatibility)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-node-npm&text=Edge%20Functions%3A%20Node%20and%20native%20npm%20compatibility)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-node-npm&t=Edge%20Functions%3A%20Node%20and%20native%20npm%20compatibility)

[Last post\\
\\
**Supavisor 1.0: a scalable connection pooler for Postgres** \\
\\
13 December 2023](https://supabase.com/blog/supavisor-postgres-connection-pooler)

[Next post\\
\\
**pg\_graphql: Postgres functions now supported** \\
\\
12 December 2023](https://supabase.com/blog/pg-graphql-postgres-functions)

[launch-week](https://supabase.com/blog/tags/launch-week) [edge-functions](https://supabase.com/blog/tags/edge-functions)

On this page

- [Migrate existing Node apps to Edge Functions](https://supabase.com/blog/edge-functions-node-npm#migrate-existing-node-apps-to-edge-functions)
- [How npm modules work under the hood](https://supabase.com/blog/edge-functions-node-npm#how-npm-modules-work-under-the-hood)
- [A few other things you've asked for…](https://supabase.com/blog/edge-functions-node-npm#a-few-other-things-youve-asked-for)
  - [Regional Invocations](https://supabase.com/blog/edge-functions-node-npm#regional-invocations)
  - [Better Metrics](https://supabase.com/blog/edge-functions-node-npm#better-metrics)
  - [Track errors with Sentry](https://supabase.com/blog/edge-functions-node-npm#track-errors-with-sentry)
- [What's next](https://supabase.com/blog/edge-functions-node-npm#whats-next)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-node-npm&text=Edge%20Functions%3A%20Node%20and%20native%20npm%20compatibility)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-node-npm&text=Edge%20Functions%3A%20Node%20and%20native%20npm%20compatibility)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-node-npm&t=Edge%20Functions%3A%20Node%20and%20native%20npm%20compatibility)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Supabase Dashboard - Edge Functions metrics view](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-x%2Fday-2%2F1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)