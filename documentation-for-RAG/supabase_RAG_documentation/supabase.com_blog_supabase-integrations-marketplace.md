---
url: "https://supabase.com/blog/supabase-integrations-marketplace"
title: "Supabase Integrations Marketplace"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Integrations Marketplace

10 Aug 2023

•

5 minute read

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Supabase Integrations Marketplace](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fintegration-marketplace-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've been running our [Integrations Marketplace](https://supabase.com/partners) in “stealth mode” for about a year now. What started as a dog-fooding project has now transformed into a marketplace with [over 60 integrations](https://supabase.com/partners/integrations). (It's also an [open source template](https://vercel.com/templates/next.js/supabase-partner-gallery) that you can use yourself).

![Featured](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Ffeatured-integrations.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase Integrations allows Partners to extend the Supabase platform with useful tooling. Today we're adding [OAuth2.0 Applications](https://supabase.com/docs/guides/platform/oauth-apps/publish-an-oauth-app). For Supabase users, this makes it even easier to connect their favorite tools to their Supabase projects. Within minutes you can:

- Add your favorite [Low Code](https://supabase.com/partners/integrations#low-code) tools on top of your Supabase database.
- Integrate your favorite [DevTools](https://supabase.com/partners/integrations#devtools): including secrets managers and database management tools.
- Add [caching](https://supabase.com/partners/integrations#caching%20/%20offline-first) to your Supabase database.
- Not a fan of the Supabase admin dashboard? Try [one of these](https://supabase.com/partners/integrations#data%20platform).
- Try out a different [SMS and email provider](https://supabase.com/partners/integrations#messaging).

## Featured Partners [\#](https://supabase.com/blog/supabase-integrations-marketplace\#featured-partners)

For the initial launch we've started with a few partners to help us build and test the OAuth functionality.

### Cloudflare [\#](https://supabase.com/blog/supabase-integrations-marketplace\#cloudflare)

![Cloudflare x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-cloudflare.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We worked with Cloudflare to build [support for databases](https://blog.cloudflare.com/announcing-database-integrations/) inside Cloudflare Workers. The Cloudflare integration makes it incredibly easy to connect to your Supabase database directly from the Cloudflare Dashboard.

Check out the [latest episode](https://cloudflare.tv/event/using-supabase-with-cloudflare-workers/dgM90RgD) on Cloudflare TV to see it in action.

### Resend [\#](https://supabase.com/blog/supabase-integrations-marketplace\#resend)

![Resend x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-resend.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Resend](https://resend.com/) (YC [W23](https://www.ycombinator.com/companies/resend)) is building the modern email sending platform. If you're using Supabase for Auth, then you'll know already that we handle all your Auth emails. But did you know that the email configuration we provide you is only for testing purposes? When you're [going into production](https://supabase.com/docs/guides/platform/going-into-prod#restricted-access-levels-for-team-members), you need to integrate your own email provider. That's where Resend come in. They've built a one-click integration to add Resend as a custom SMTP provider for Supabase.

Read more on [Resend's blog](https://resend.com/blog/how-to-configure-supabase-to-send-emails-from-your-domain).

### Snaplet [\#](https://supabase.com/blog/supabase-integrations-marketplace\#snaplet)

![Snaplet x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-snaplet.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Snaplet is a tool for Typescript developers to copy your database, transform sensitive data, and share it with your team without worrying about PII. If you followed our [Tuesday launch](https://supabase.com/blog/supabase-local-dev#database-seeding) you'll be familiar with Snaplet - they are one of the best tools for [generating seed data](https://supabase.com/docs/guides/cli/seeding-your-database#generating-seed-data) for your local development environment. Now they are making it even easier, with their official OAuth App, to spin up production-like development environments for your team.

[Learn more on snaplet.dev](https://www.snaplet.dev/post/now-live-supabase-x-snaplet-integration).

### Trigger.dev [\#](https://supabase.com/blog/supabase-integrations-marketplace\#triggerdev)

![Trigger x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-triggerdev.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Trigger.dev](http://trigger.dev/) (YC [W23](https://www.ycombinator.com/companies/trigger-dev)) is the open source Background Jobs framework for Next.js. You can create long-running Jobs directly in your codebase with features like API integrations, webhooks, scheduling and delays. And today you can use their one-click integration to [trigger anything from a database change](https://trigger.dev/supabase) in Supabase.

Learn more about their integration at: [trigger.dev/supabase](http://trigger.dev/supabase)

### Vercel [\#](https://supabase.com/blog/supabase-integrations-marketplace\#vercel)

![Vercel x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-vercel.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

One that requires no introduction - since so many of you use Vercel, we've dedicated an entire blog post to the upgraded Vercel integration.

Learn more about the Vercel integration [updates we're launching](https://supabase.com/blog/using-supabase-with-vercel) today.

### Windmill [\#](https://supabase.com/blog/supabase-integrations-marketplace\#windmill)

![Windmill x Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fmarketplace-windmill.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Windmill](https://windmill.dev/) (YC [S22](https://www.ycombinator.com/companies/windmill)) is an open source alternative to Retool and a modern Airflow. They provide a developer platform to quickly build production-grade complex workflows and integrations from minimal Python and Typescript scripts. Their one-click integration with Supabase makes it simple to launch new databases, process large quantities of data (maybe even convert them into [embeddings](https://supabase.com/vector)), and build internal dashboards.

Read the [official blog post on windmill.dev](https://www.windmill.dev/blog/2023/08/10/supabase-partnership).

## Building Supabase Integrations [\#](https://supabase.com/blog/supabase-integrations-marketplace\#building-supabase-integrations)

We've released full instructions in our [Build with Supabase](https://supabase.com/docs/guides/platform/oauth-apps/build-a-supabase-integration) documentation so that you can build your own Supabase OAuth application for your users. Simply visit your [Organization settings](https://supabase.com/dashboard/org/_/apps) and click “Add application” to get started:

Manage Supabase projects in code with the new Management API 🚀 - YouTube

Supabase

54.4K subscribers

[Manage Supabase projects in code with the new Management API 🚀](https://www.youtube.com/watch?v=gtJo1lTxHfs)

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

[Watch on YouTube](https://www.youtube.com/watch?v=gtJo1lTxHfs "Watch on YouTube")

The Integrations marketplace is open to everyone. After your submission is complete, you can share the integration with your own users - simply create a button to launch your new app. We've provided some [brand assets](https://supabase.com/brand-assets) so that developers can quickly identify the integration on your site.

## Building custom integrations [\#](https://supabase.com/blog/supabase-integrations-marketplace\#building-custom-integrations)

You don't actually need to build an OAuth Application to build an integration with Supabase. If you're building something for yourself or your team, the [Management API](https://supabase.com/docs/reference/api/introduction) is the way to go.

The [Trigger.dev](https://trigger.dev/) team deserve a special shout out. While developing their Integration they also developed [supabase-management-js](https://github.com/supabase-community/supabase-management-js), a Typescript library for the [Supabase Management API](https://supabase.com/docs/reference/api/introduction). This makes it even easier to get started with the Supabase API.

It's useful beyond just integrations. Want to programmatically spin up databases? Easy:

`
import { SupabaseManagementAPI } from "supabase-management-js";
const client = new SupabaseManagementAPI({
	accessToken: "<access token>"
})
const newProject = await client.createProject({
	  name: 'staging',
		db_pass: 'XXX',
    organization_id: 'XXX'
		plan: 'free',
    region: 'us-east-1'
})
`

## Become a Partner [\#](https://supabase.com/blog/supabase-integrations-marketplace\#become-a-partner)

Supabase is a collaborative company. We love working with other communities (especially open source ones!), and we'd love to work with you. Get started today:

- [Build an OAuth integration](https://supabase.com/docs/guides/platform/oauth-apps/build-a-supabase-integration)
- [Learn more about our Management API](https://supabase.com/docs/reference/api/introduction)

![Partner with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fpartner-with-supabase.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## More Launch Week 8 [\#](https://supabase.com/blog/supabase-integrations-marketplace\#more-launch-week-8)

- [Supabase Local Dev: migrations, branching, and observability](https://supabase.com/blog/supabase-local-dev)
- [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
- [Launch Week 8](https://supabase.com/launch-week)
- [Coding the stars - an interactive constellation with Three.js and React Three Fiber](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber)
- [Why we'll stay remote](https://supabase.com/blog/why-supabase-remote)
- [Postgres Language Server](https://github.com/supabase/postgres_lsp)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&text=Supabase%20Integrations%20Marketplace)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&text=Supabase%20Integrations%20Marketplace)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&t=Supabase%20Integrations%20Marketplace)

[Last post\\
\\
**Supavisor: Scaling Postgres to 1 Million Connections** \\
\\
11 August 2023](https://supabase.com/blog/supavisor-1-million)

[Next post\\
\\
**Vercel Integration and Next.js App Router Support** \\
\\
10 August 2023](https://supabase.com/blog/using-supabase-with-vercel)

[launch-week](https://supabase.com/blog/tags/launch-week) [integrations](https://supabase.com/blog/tags/integrations)

On this page

- [Featured Partners](https://supabase.com/blog/supabase-integrations-marketplace#featured-partners)
  - [Cloudflare](https://supabase.com/blog/supabase-integrations-marketplace#cloudflare)
  - [Resend](https://supabase.com/blog/supabase-integrations-marketplace#resend)
  - [Snaplet](https://supabase.com/blog/supabase-integrations-marketplace#snaplet)
  - [Trigger.dev](https://supabase.com/blog/supabase-integrations-marketplace#triggerdev)
  - [Vercel](https://supabase.com/blog/supabase-integrations-marketplace#vercel)
  - [Windmill](https://supabase.com/blog/supabase-integrations-marketplace#windmill)
- [Building Supabase Integrations](https://supabase.com/blog/supabase-integrations-marketplace#building-supabase-integrations)
- [Building custom integrations](https://supabase.com/blog/supabase-integrations-marketplace#building-custom-integrations)
- [Become a Partner](https://supabase.com/blog/supabase-integrations-marketplace#become-a-partner)
- [More Launch Week 8](https://supabase.com/blog/supabase-integrations-marketplace#more-launch-week-8)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&text=Supabase%20Integrations%20Marketplace)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&text=Supabase%20Integrations%20Marketplace)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-integrations-marketplace&t=Supabase%20Integrations%20Marketplace)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)