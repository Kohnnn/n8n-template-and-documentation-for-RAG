---
url: "https://supabase.com/blog/using-supabase-with-vercel"
title: "Vercel Integration and Next.js App Router Support"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Vercel Integration and Next.js App Router Support

10 Aug 2023

•

6 minute read

[![Jonny Summers-Muir avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmildtomato.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jonny Summers-MuirProduct Design](https://github.com/mildtomato)

[![Jon Meyers avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdijonmusters.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jon MeyersDeveloper Advocate](https://twitter.com/jonmeyers_io)

![Vercel Integration and Next.js App Router Support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fvercel-and-supabase-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Vercel's open source framework, [Next.js](https://nextjs.org/), is the most popular frontend framework for Supabase developers.

At Supabase, we feel it's important to provide developers with the tools they need to build on the platforms they love. So for the past few months, we've doubled-down on the Vercel x Supabase experience. Here are a few of the newest improvements.

## The New Supabase x Vercel integration [\#](https://supabase.com/blog/using-supabase-with-vercel\#the-new-supabase-x-vercel-integration)

Our new [Vercel Integration](https://vercel.com/integrations/supabase) streamlines the process of creating, deploying, and maintaining web applications.

### Monorepo support [\#](https://supabase.com/blog/using-supabase-with-vercel\#monorepo-support)

You can now [link multiple](https://app.supabase.com/org/_/integrations) Vercel projects to a single Supabase project:

![Vercel in the Supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fvercel-dashboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Previously we mapped each Vercel project to a single Supabase project. With this release, we're introducing the concept of project 'Connections'. Supabase projects can have an unlimited number of Vercel Connections. This is especially useful for monorepos using [Turborepo](https://turbo.build/).

### Automatically managed Supabase config [\#](https://supabase.com/blog/using-supabase-with-vercel\#automatically-managed-supabase-config)

We've improved the way we manage your Supabase environment variables.

![Vercel config](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fvercel-config.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase keeps each of your Vercel Projects updated with Environment Variables, managing your secrets (like `service-role-key`) and public variables (like `supabase-url`).

Importantly, Supabase now updates the Auth Redirect URIs to match your main Vercel project domain and any preview deployment URLs. We listen to your Vercel deployment webhooks and adjust your redirects accordingly.

View the full list of environment variables

### Starter kits [\#](https://supabase.com/blog/using-supabase-with-vercel\#starter-kits)

Don't have a project to work on yet? Not a problem, Supabase has a range of Starter kits. With the click of a button you can you have an full-stack application running in less than a minute.

You can find a Vercel Starter kit by looking for Vercel's blue "Deploy Button". Clicking on any one of these buttons will:

1. Take you to Vercel to clone the repository to your own GitHub account/organization
2. Auto install the Supabase Integration (if not already done so).
3. Then we make things really easy: Supabase checks for any migrations in the Starter kit, and if so, we'll run them in your new Supabase project.

After Vercel has deployed the app, it works without any additional configuration. Starter kits include everything from table schemas, authentication, and sample data from the `seed.sql` file.

### Database Branching [\#](https://supabase.com/blog/using-supabase-with-vercel\#database-branching)

We announced Database Branching on [Tuesday](https://supabase.com/blog/supabase-local-dev#branching-and-preview-environments). We've designed this to work perfectly with Vercel's Preview Deployments.

![Vercel branching](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fsupabase-vercel-branching.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

For now, Branching in Supabase is limited to development partners. We'll be rolling it out to everyone over the coming months. If you're interested in testing the new features, [sign up for early access](https://forms.supabase.com/branching-request).

## Next.js 13 App Router Support [\#](https://supabase.com/blog/using-supabase-with-vercel\#nextjs-13-app-router-support)

The new App Router in Next.js adds a lot of exciting features, like React Suspense and Streaming. Supabase now fully-supports the App Router in Next.js:

YouTube

The Next.js App Router shifts a significant amount of your app development from the client to the server, using Server Components, Route Handlers and Server Actions. This means Supabase Auth needs to be configured to store session data in cookies - available in the browser and on the server - rather than Local Storage. We've simplified this process for you with our new [Next.js Auth Helpers package](https://supabase.com/docs/guides/auth/auth-helpers/nextjs).

This configures cookie-based Auth, making the user's session available throughout the entire Next.js App Router stack:

- [Client Components](https://supabase.com/docs/guides/auth/auth-helpers/nextjs#client-components) — `createClientComponentClient`
- [Server Components](https://supabase.com/docs/guides/auth/auth-helpers/nextjs#server-components) — `createServerComponentClient`
- [Server Actions](https://supabase.com/docs/guides/auth/auth-helpers/nextjs#server-actions) — `createServerActionClient`
- [Route Handlers](https://supabase.com/docs/guides/auth/auth-helpers/nextjs#route-handlers) — `createRouteHandlerClient`
- [Middleware](https://supabase.com/docs/guides/auth/auth-helpers/nextjs#middleware) — `createMiddlewareClient`

## Scaffolding a new Next.js app with Supabase [\#](https://supabase.com/blog/using-supabase-with-vercel\#scaffolding-a-new-nextjs-app-with-supabase)

[create-next-app](https://nextjs.org/docs/pages/api-reference/create-next-app) is one of the easiest way to get started with Next.js.

We've created a new template for `create-next-app` scaffolding Supabase projects:

`
npx create-next-app -e with-supabase
`

This creates a new Next.js app configured with:

- Server-side cookie-based Auth
- TypeScript
- Tailwind CSS

This is the perfect starting point for any application built with Next.js and Supabase! 🚀

Check out the [`/app/_examples`](https://github.com/vercel/next.js/blob/canary/examples/with-supabase/app/_examples) folder for an example of creating a Supabase client in:

- [Client Components](https://github.com/vercel/next.js/blob/canary/examples/with-supabase/app/_examples/client-component/page.tsx)
- [Server Components](https://github.com/vercel/next.js/blob/canary/examples/with-supabase/app/_examples/server-component/page.tsx)
- [Route Handlers](https://github.com/vercel/next.js/blob/canary/examples/with-supabase/app/_examples/route-handler/route.ts)
- [Server Actions](https://github.com/vercel/next.js/blob/canary/examples/with-supabase/app/_examples/server-action/page.tsx)

## More integrations [\#](https://supabase.com/blog/using-supabase-with-vercel\#more-integrations)

We've got plenty more in store for Next.js developers which we will be rolling out over the next few months. If you're looking for more integrations, or you want to build your own, we're also launching a new Supabase [Integrations Marketplace](https://supabase.com/blog/supabase-integrations-marketplace).

## More Launch Week 8 [\#](https://supabase.com/blog/using-supabase-with-vercel\#more-launch-week-8)

- [Supabase Local Dev: migrations, branching, and observability](https://supabase.com/blog/supabase-local-dev)
- [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
- [Launch Week 8](https://supabase.com/launch-week)
- [Coding the stars - an interactive constellation with Three.js and React Three Fiber](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber)
- [Why we'll stay remote](https://supabase.com/blog/why-supabase-remote)
- [Postgres Language Server](https://github.com/supabase/postgres_lsp)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-with-vercel&text=Vercel%20Integration%20and%20Next.js%20App%20Router%20Support)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-with-vercel&text=Vercel%20Integration%20and%20Next.js%20App%20Router%20Support)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-with-vercel&t=Vercel%20Integration%20and%20Next.js%20App%20Router%20Support)

[Last post\\
\\
**Supabase Integrations Marketplace** \\
\\
10 August 2023](https://supabase.com/blog/supabase-integrations-marketplace)

[Next post\\
\\
**Supabase Studio 3.0: AI SQL Editor, Schema Diagrams, and new Wrappers** \\
\\
9 August 2023](https://supabase.com/blog/supabase-studio-3-0)

[launch-week](https://supabase.com/blog/tags/launch-week) [integrations](https://supabase.com/blog/tags/integrations)

On this page

- [The New Supabase x Vercel integration](https://supabase.com/blog/using-supabase-with-vercel#the-new-supabase-x-vercel-integration)
  - [Monorepo support](https://supabase.com/blog/using-supabase-with-vercel#monorepo-support)
  - [Automatically managed Supabase config](https://supabase.com/blog/using-supabase-with-vercel#automatically-managed-supabase-config)
  - [Starter kits](https://supabase.com/blog/using-supabase-with-vercel#starter-kits)
  - [Database Branching](https://supabase.com/blog/using-supabase-with-vercel#database-branching)
- [Next.js 13 App Router Support](https://supabase.com/blog/using-supabase-with-vercel#nextjs-13-app-router-support)
- [Scaffolding a new Next.js app with Supabase](https://supabase.com/blog/using-supabase-with-vercel#scaffolding-a-new-nextjs-app-with-supabase)
- [More integrations](https://supabase.com/blog/using-supabase-with-vercel#more-integrations)
- [More Launch Week 8](https://supabase.com/blog/using-supabase-with-vercel#more-launch-week-8)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-with-vercel&text=Vercel%20Integration%20and%20Next.js%20App%20Router%20Support)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-with-vercel&text=Vercel%20Integration%20and%20Next.js%20App%20Router%20Support)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fusing-supabase-with-vercel&t=Vercel%20Integration%20and%20Next.js%20App%20Router%20Support)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Vercel in the Supabase dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fvercel-dashboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Vercel config](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fvercel-config.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Vercel branching](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-4%2Fsupabase-vercel-branching.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)