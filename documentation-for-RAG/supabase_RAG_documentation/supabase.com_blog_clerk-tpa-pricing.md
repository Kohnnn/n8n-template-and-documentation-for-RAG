---
url: "https://supabase.com/blog/clerk-tpa-pricing"
title: "Supabase Auth: Bring Your Own Clerk"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Auth: Bring Your Own Clerk

31 Mar 2025

•

3 minute read

[![Stojan Dimitrovski avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fhf.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Stojan DimitrovskiEngineering](https://github.com/hf)

![Supabase Auth: Bring Your Own Clerk](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-clerk-tpa-pricing%2Fclerk-tpa-pricing-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we're expanding our official Third-party Auth integrations to include [Clerk](https://clerk.com/).

[Third-party Auth](https://supabase.com/docs/guides/auth/third-party/overview) allows you to use external Auth providers with the Supabase as a drop-in replacement for Supabase Auth. This modular design is [intentional](https://supabase.com/docs/guides/getting-started/architecture#product-principles), allowing you to pick and choose features of Supabase. Our platform makes it easy to get started with Postgres and _any_ of your favorite tools.

![Clerk TPA diagram](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw14-clerk-tpa-pricing%2Fclerk-tpa-diagram.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It was [already possible](https://supabase.com/partners/integrations/clerk) to use Clerk with Supabase, however the previous method was a bit of a hack that required sharing your project's secret and JWT templates from Clerk. We've worked with the Clerk team on the new implementation. Now you can enjoy better security and the same developer experience you've come to expect from Supabase.

To get started with Clerk and Supabase, visit Clerk's [Connect with Supabase](https://dashboard.clerk.com/setup/supabase) page.

Register your Clerk domain [in the Supabase Dashboard](https://supabase.com/dashboard/project/_/auth/third-party) or in the CLI:

`
[auth.third_party.clerk]
enabled = true
domain = "example.clerk.accounts.dev"
`

In your JavaScript app all you need to do is write the following code:

`
import { createClient } from '@supabase/supabase-js'
const SUPABASE_URL = 'https://<supabase-project>.supabase.co'
const SUPABASE_ANON_KEY = '<SUPABASE_ANON_KEY>'
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
accessToken: () => {
    return Clerk.session?.getToken()
},
})
`

[Read the docs](https://supabase.com/docs/guides/auth/third-party/clerk) to set up Flutter and Swift (iOS) applications, and to learn how to use Postgres Row-level Security (RLS) Policies.

## Third-Party Auth is now a lot cheaper [\#](https://supabase.com/blog/clerk-tpa-pricing\#third-party-auth-is-now-a-lot-cheaper)

One more thing: today we're making Third-party Auth cheaper so that it has pricing parity with Supabase Auth.

You can have up to 50,000 MAU on the Free plan, or 100,000 MAU on the Pro plan and $0.00325 per MAU above that number.

|  | Free Plan | Pro Plan |
| --- | --- | --- |
| Previously | 50 MAUs included | 50,000 MAUs included |
| Now | 50,000 MAUs included | 100,000 MAUs included |

## Get started today [\#](https://supabase.com/blog/clerk-tpa-pricing\#get-started-today)

Supabase Auth makes it easy to implement authentication and authorization in your app. We provide client SDKs and API endpoints to help you create and manage users.

- [Read the documentation](https://supabase.com/docs/guides/auth/third-party/overview) for Third-party Auth
- [Learn how to use Clerk with Supabase](https://supabase.com/docs/guides/auth/third-party/clerk)
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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&text=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&text=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&t=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)

[Last post\\
\\
**Introducing the Supabase UI Library** \\
\\
31 March 2025](https://supabase.com/blog/supabase-ui-library)

[Next post\\
\\
**Postgres Language Server: Initial Release** \\
\\
29 March 2025](https://supabase.com/blog/postgres-language-server)

[launch-week](https://supabase.com/blog/tags/launch-week) [auth](https://supabase.com/blog/tags/auth)

On this page

- [Third-Party Auth is now a lot cheaper](https://supabase.com/blog/clerk-tpa-pricing#third-party-auth-is-now-a-lot-cheaper)
- [Get started today](https://supabase.com/blog/clerk-tpa-pricing#get-started-today)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&text=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&text=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fclerk-tpa-pricing&t=Supabase%20Auth%3A%20Bring%20Your%20Own%20Clerk)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)