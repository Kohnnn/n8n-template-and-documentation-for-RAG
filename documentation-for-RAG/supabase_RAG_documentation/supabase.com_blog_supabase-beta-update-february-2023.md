---
url: "https://supabase.com/blog/supabase-beta-update-february-2023"
title: "Supabase Beta February 2023"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta February 2023

09 Mar 2023

•

5 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta February 2023](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fsupabase-beta-update-february-2023.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

There’s something for everybody this month: AI, Auth, Database, Edge Functions, GraphQL … you name it!

## GraphiQL editor in the dashboard [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#graphiql-editor-in-the-dashboard)

![GraphiQL editor in the dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fgraphiql-dashboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The most popular GraphQL IDE/API explorer is now built into the dashboard! You can now explore and query your GraphQL API produced by `pg_graphql`.

[Try it now](https://supabase.com/dashboard/project/_/api/graphiql).

## Supabase + OpenAI search [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#supabase--openai-search)

![Supabase + OpenAI search](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fopenai-supabase.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've updated our Docs search functionality to use `pgvector` \+ OpenAI. Still no cease and desist from Microsoft, so you can continue to ask Clippy any Supabase-specific questions 📎💚

[Ask Clippy.](https://supabase.com/docs)

## Serve all the functions! [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#serve-all-the-functions)

![Serve all the functions!](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fsupabase-cli-edge-functions.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Do you use multiple Edge Functions in your project? Then celebrate! Supabase CLI 1.36+ now supports serving multiple Edge Functions at the same time.

To enable the feature, just run `supabase functions serve` in your project.

[Check the docs.](https://supabase.com/docs/reference/cli/supabase-functions-serve)

## Smaller Postgres docker images for everyone [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#smaller-postgres-docker-images-for-everyone)

![Smaller Postgres docker images for everyone](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fpostgres-docker-images.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We rewrote the Postgres Dockerfile with multi-stage builds so that each extension is compiled in its own separate stage. This reduces the size of the image from 1.3GB to 250MB, enabling a much faster boot time.

[See it yourself](https://hub.docker.com/r/supabase/postgres/tags)

## New UI for Postgres Roles [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#new-ui-for-postgres-roles)

![New UI for Postgres Roles](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fpostgres-roles.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've improved database role management. You can create, update, and delete database roles through the dashboard. Just one small step towards column-level security

[Check it out.](https://supabase.com/dashboard/project/_/editor)

## API docs in the table editor [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#api-docs-in-the-table-editor)

![API docs in the table editor](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fapi-docs.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

API docs got a light touchup and were moved to the table editor. You can now look up API methods and generate & download type files right there ✨

[Check it out.](https://supabase.com/dashboard/project/_/editor)

## Quick product updates [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#quick-product-updates)

- **Postgres Extensions**: We're rolling out some fixes for several Postgres extensions. Check your Dashboard notifications to see if you need to take any actions.

- **Auth**: Added full OpenAPI 3.0 spec which provides a comprehensive overview of the API with documentation on each request. [PR](https://github.com/supabase/gotrue/pull/918)

- **Database**: supabase-js now infers the response type from your query. If the inferred type is incorrect, you can use `.returns<MyType>()` to override it. [Doc](https://supabase.com/docs/reference/javascript/db-returns)

- **Dashboard**: Improved database roles management, you can now create, update and delete database roles through the dashboard. [Dashboard](https://supabase.com/dashboard/project/_/database/roles)

- **Dashboard**: We've provided a reference panel showing all available paths that can be queried from each respective source that improves the Logs Explorer experience. [Dashboard](https://supabase.com/dashboard/project/_/logs/explorer)


- **Edge Functions**: upgraded to Deno 1.30.3, that supports TypeScript 4.9.x and introduces `satisfies`. Thanks to [Benjamin Dobell](https://github.com/Benjamin-Dobell) 🙏. [PR](https://github.com/supabase/functions-relay/pull/30)

- Realtime: Broadcast only primary key(s) for deleting records when RLS is enabled and replica identity is full. [PR](https://github.com/supabase/realtime/pull/461)

## Next.js with Supabase [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#nextjs-with-supabase)

![Next.js with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fnextjs-supabase.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Building the next big thing with Supabase and Next.js? Then make sure to check Jon's new video series to help get you (and your app directory) off the ground.

- [Fetching and Caching data in Next.js Async Server Components](https://www.youtube.com/watch?v=GniRj1jIhFw)

- [Client vs Server Components in Next.js app directory // Merging server state with realtime updates](https://www.youtube.com/watch?v=YR-xP6PPXXA)

- [Delicious Server Component Cookies // Auth in the Next.js app directory](https://www.youtube.com/watch?v=Bh1TOpOcGJQ)


![Made with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-12-07-november-beta-update%2Fmadewithsupabase.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Domain-specific ChatGPT](https://github.com/gannonh/gpt3.5-turbo-pgvector) \| This starter app uses embeddings coupled with vector search to show how the OpenAI API can be used to create a conversational interface to domain-specific knowledge. Built by [Gannon Hall](https://github.com/gannonh) with Next.js, Vercel, gpt-3.5-turbo, pgvector, and Supabase.

Discover 100+ other apps in this [tweet](https://twitter.com/supabase/status/1628843899996209155).

## Extended Community Highlights [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#extended-community-highlights)

![Community](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-june%2Fcommunity.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

- LangChain supports our database as a vector store, using pgvector. [Doc](https://hwchase17.github.io/langchainjs/docs/modules/indexes/vector_stores/supabase/)

- refine week: building a CRUD app with refine & Supabase. [Full series](https://refine.dev/week-of-refine/)


- Build an Instagram Web App with Supabase and Next.js. [Tutorial](https://livecycle.io/blogs/nextjs-supabase-instagram/)

- Supabase GeoQueries with PostGIS and Storage Upload. [Video](https://www.youtube.com/watch?v=-_Wpr7rwU8I)

- How I used Supabase to build a winning hackathon project. [Article](https://blog.matt.lgbt/how-i-used-supabase-to-build-a-winning-hackathon-project)

- Using a Supabase API within FlutterFlow. [Video](https://www.youtube.com/watch?v=YzSXwlA3vWM)

- Getting started with Supabase in Android. [Part 1](https://www.youtube.com/watch?v=SGr73sWMX6w) \| [Part 2](https://www.youtube.com/watch?v=NWaIIRfVpuo)

- Streaming User Events from PostgreSQL (Supabase) to Serverless Kafka. [Article](https://upstash.com/blog/postgre-supabase-connector)


- Building a CRUD API with FastAPI and Supabase: A Step-by-Step Guide. [Tutorial](https://blog.theinfosecguy.xyz/building-a-crud-api-with-fastapi-and-supabase-a-step-by-step-guide)

- How to build a collaborative SaaS product using Next.js and ZenStack's access control policy. [Tutorial](https://zenstack.dev/blog/saas-demo)

- Nuxt 3, Tailwind, and Supabase Crash Course. [Course](https://dev.to/jacobandrewsky/nuxt-3-tailwind-and-supabase-crash-course-1482)

- A sneak peek at the Supabase and Next.js RSC SaaS kit. [Article](https://makerkit.dev/blog/changelog/nextjs-supabase-kit-update)

- Build a Fullstack serverless application using React, Chakra UI, Hookstate, and Supabase. [Tutorial](https://clx.hashnode.dev/build-a-fullstack-serverless-application-using-react-chakra-ui-hookstate-and-supabase)

- Implement Sign in with Google using Supabase Auth in Next.js. [Tutorial](https://dev.to/irwanphan/implement-sign-in-with-google-using-supabase-auth-in-nextjs-1jj1)


## We're Hiring [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#were-hiring)

Come join one of the fastest-growing open source projects ever 🤗

- [Technical partnerships lead (Next.js, Node,js, Supabase)](https://boards.greenhouse.io/supabase/jobs/4775849004)

- [Junior Developer Advocate (SMM & Community)](https://boards.greenhouse.io/supabase/jobs/4777008004)

## Meme Zone [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#meme-zone)

As always, one of our favorite memes from last month. [Follow us on Twitter](https://twitter.com/supabase) for more.

![Best meme from February 2023](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fbeta-update-february-meme.jpeg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## It's happening! Coming in April [\#](https://supabase.com/blog/supabase-beta-update-february-2023\#its-happening-coming-in-april)

![Supabase Launch Week 7](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-03-09-beta-update-february%2Fsupabase-launch-week-7.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-february-2023&text=Supabase%20Beta%20February%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-february-2023&text=Supabase%20Beta%20February%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-february-2023&t=Supabase%20Beta%20February%202023)

[Last post\\
\\
**SupaClub** \\
\\
1 April 2023](https://supabase.com/blog/supaclub)

[Next post\\
\\
**Geo Queries with PostGIS in Ionic Angular** \\
\\
1 March 2023](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [GraphiQL editor in the dashboard](https://supabase.com/blog/supabase-beta-update-february-2023#graphiql-editor-in-the-dashboard)
- [Supabase + OpenAI search](https://supabase.com/blog/supabase-beta-update-february-2023#supabase--openai-search)
- [Serve all the functions!](https://supabase.com/blog/supabase-beta-update-february-2023#serve-all-the-functions)
- [Smaller Postgres docker images for everyone](https://supabase.com/blog/supabase-beta-update-february-2023#smaller-postgres-docker-images-for-everyone)
- [New UI for Postgres Roles](https://supabase.com/blog/supabase-beta-update-february-2023#new-ui-for-postgres-roles)
- [API docs in the table editor](https://supabase.com/blog/supabase-beta-update-february-2023#api-docs-in-the-table-editor)
- [Quick product updates](https://supabase.com/blog/supabase-beta-update-february-2023#quick-product-updates)
- [Next.js with Supabase](https://supabase.com/blog/supabase-beta-update-february-2023#nextjs-with-supabase)
- [Extended Community Highlights](https://supabase.com/blog/supabase-beta-update-february-2023#extended-community-highlights)
- [We're Hiring](https://supabase.com/blog/supabase-beta-update-february-2023#were-hiring)
- [Meme Zone](https://supabase.com/blog/supabase-beta-update-february-2023#meme-zone)
- [It's happening! Coming in April](https://supabase.com/blog/supabase-beta-update-february-2023#its-happening-coming-in-april)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-february-2023&text=Supabase%20Beta%20February%202023)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-february-2023&text=Supabase%20Beta%20February%202023)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-update-february-2023&t=Supabase%20Beta%20February%202023)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)