---
url: "https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1"
title: "Edge Functions: Deploy from the Dashboard + Deno 2.1"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Edge Functions: Deploy from the Dashboard + Deno 2.1

01 Apr 2025

•

4 minute read

[![Saxon Fletcher avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaxonf.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Saxon FletcherProduct Design](https://github.com/saxonf)

[![Nyannyacha avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fnyannyacha.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
NyannyachaEngineering](https://github.com/nyannyacha)

[![Lakshan Perera avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Flaktek.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Lakshan PereraEngineering](https://github.com/laktek)

![Edge Functions: Deploy from the Dashboard + Deno 2.1](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Now you can create, test, edit, and deploy Edge Functions directly from the Supabase Dashboard. We're also releasing Deno 2.1 Preview today but more on that later.

Announcing Updates to Edge Functions - YouTube

Supabase

54.4K subscribers

[Announcing Updates to Edge Functions](https://www.youtube.com/watch?v=Pn7xyTbsxPI)

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

[Watch on](https://www.youtube.com/watch?v=Pn7xyTbsxPI&embeds_referring_euri=https%3A%2F%2Fsupabase.com%2F)

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=Pn7xyTbsxPI "Watch on YouTube")

## Creating Edge Functions from the Supabase Dashboard [\#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1\#creating-edge-functions-from-the-supabase-dashboard)

To write an Edge Functions previously, you had to install the Supabase CLI, spin up Docker, and then set up your editor to use Deno. Those steps are no longer necessary. The Edge Functions editor in the Dashboard has built-in syntax highlighting and type-checking for Deno and Supabase-specific APIs.

![Create a Function from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fcreate-function.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The Edge Functions editor includes templates for common use cases, such as Stripe WebHooks, OpenAI proxying, uploading files to Supabase Storage, and sending emails.

![Function Templates](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Ffunction-templates.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Once a Function has been deployed you can make edits directly within the Dashboard, and if you get stuck you can summon an inline AI Assistant to explain, debug or write code.

![Edit Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fedit-function.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Downloading Edge Functions [\#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1\#downloading-edge-functions)

You can download Edge Functions source code via Supabase CLI using `supabase functions download FUNCTION_NAME` or by clicking the Download button in the dashboard.

![Download Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fdownload-function.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The Dashboard's Edge Function editor currently does not support versioning or rollbacks. We recommend using it only for quick testing and prototypes. When you’re ready to go to production, store Edge Functions code in a source code repository (e.g. git) and deploy it using one of the [CI integrations](https://supabase.com/docs/guides/functions/cicd-workflow).

## Testing Edge Functions from the Supabase Dashboard [\#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1\#testing-edge-functions-from-the-supabase-dashboard)

We are introducing a built-in tool for testing your Edge Functions from the Supabase Dashboard. You can execute your Edge Function with different request payloads, headers, and query parameters. The built-in tester returns the response status, headers, and body.

![Test Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Ftest-function.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

With the built-in editor and tester, you have a streamlined workflow for creating, testing, and refactoring your Edge Functions without leaving the Supabase Dashboard.

## Deploying Edge Functions no longer requires Docker [\#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1\#deploying-edge-functions-no-longer-requires-docker)

By popular request, you can now deploy Edge Functions from the Supabase CLI with the `--use-api` flag, which will not use Docker. We will make this the default behavior in future releases (with a `--use-docker` flag as a fallback option.)

`
supabase functions deploy MY_FUNCTION --use-api
`

## New APIs for Deploying Edge Functions [\#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1\#new-apis-for-deploying-edge-functions)

The ability to deploy without Docker in both the Edge Functions editor and Supabase CLI are made possible by new APIs we introduced to deploy and update Edge Functions. These APIs are publicly available for you to build custom integrations and workflows.

You can check [the Changelog announcement](https://github.com/orgs/supabase/discussions/33720) for more details and official references to these API endpoints.

## Deno 2.1 Preview [\#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1\#deno-21-preview)

Last, but not least, we have added Deno 2.1 support for Supabase Edge Runtime. With Deno 2.1, you can use built-in Deno commands to scaffold a new project, manage dependencies, run tests, and lints.

Check [our guide on how to start using Deno 2.1](https://github.com/orgs/supabase/discussions/34054) tooling for your Edge Functions.

Note that the Supabase hosted platform is still using Deno 1.45. In the coming weeks, we will provide more details on deploying Deno 2.1 projects in the hosted platform.

## Conclusion [\#](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1\#conclusion)

These changes to Supabase Edge Functions make it easier and more accessible for all developers to build powerful functionality into their applications.

- Read the [Edge Functions documentation](https://supabase.com/docs/guides/functions) to learn more
- [Sign up for Supabase](https://supabase.com/dashboard/sign-up) and get started today

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&text=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&text=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&t=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)

[Last post\\
\\
**Keeping Tabs on What's New in Supabase Studio** \\
\\
2 April 2025](https://supabase.com/blog/tabs-dashboard-updates)

[Next post\\
\\
**Automatic Embeddings in Postgres** \\
\\
1 April 2025](https://supabase.com/blog/automatic-embeddings)

[launch-week](https://supabase.com/blog/tags/launch-week) [functions](https://supabase.com/blog/tags/functions)

On this page

- [Creating Edge Functions from the Supabase Dashboard](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#creating-edge-functions-from-the-supabase-dashboard)
- [Downloading Edge Functions](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#downloading-edge-functions)
- [Testing Edge Functions from the Supabase Dashboard](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#testing-edge-functions-from-the-supabase-dashboard)
- [Deploying Edge Functions no longer requires Docker](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#deploying-edge-functions-no-longer-requires-docker)
- [New APIs for Deploying Edge Functions](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#new-apis-for-deploying-edge-functions)
- [Deno 2.1 Preview](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#deno-21-preview)
- [Conclusion](https://supabase.com/blog/supabase-edge-functions-deploy-dashboard-deno-2-1#conclusion)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&text=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&text=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions-deploy-dashboard-deno-2-1&t=Edge%20Functions%3A%20Deploy%20from%20the%20Dashboard%20%2B%20Deno%202.1)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Create a Function from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fcreate-function.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Function Templates](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Ffunction-templates.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Edit Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fedit-function.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Download Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Fdownload-function.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Test Functions from Dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-14%2Fday-2-edge-functions-dashboard%2Ftest-function.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)