---
url: "https://supabase.com/blog/beta-update-may-2022"
title: "Supabase Beta May 2022"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta May 2022

01 Jun 2022

•

5 minute read

[![Ant Wilson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

![Supabase Beta May 2022](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fthumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It's been another packed month of shipping like crazy at Supabase, here's the update on what you might have seen appearing in the product and beyond during the month of May...

## Wildcard Auth Redirects [\#](https://supabase.com/blog/beta-update-may-2022\#wildcard-auth-redirects)

Wildcard redirects are especially useful for Jamstack platforms with preview deployments, like Vercel and Netlify. Now you can add a wildcard domain, like `*.mydomain.com/welcome` and both `x.mydomain.com/welcome` and `y.mydomain.com/welcome` will be accepted. [Read the Pull Request](https://github.com/supabase/gotrue/pull/334).

[![Wildcard Auth Redirects](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fwildcard.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://github.com/supabase/gotrue/pull/334)

## Supabase Edge functions with Webhooks [\#](https://supabase.com/blog/beta-update-may-2022\#supabase-edge-functions-with-webhooks)

Now you can deploy functions with optional JWT verification. This makes it easier to trigger Edge Functions with webhooks. Use the -no-verify-jwt flag when deploying your functions via the CLI to enable this mode. You can test this out with our [Edge Functions Telegram Bot example](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/telegram-bot).

[![graphql](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fstripe-webhook.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/telegram-bot)

## Metrics for everybody [\#](https://supabase.com/blog/beta-update-may-2022\#metrics-for-everybody)

We are making another enterprise feature available for all of our users. Our Prometheus-compatible metrics endpoint gives you granular insights on the health and status of your projects, allowing for real-time monitoring, debugging, and alerting for all. [Read the docs](https://supabase.com/docs/guides/platform/metrics).

[![realtime](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fprometheus.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/docs/guides/platform/metrics)

## Improved Policy Editor [\#](https://supabase.com/blog/beta-update-may-2022\#improved-policy-editor)

The Policy editor now includes a “Target roles” field. We now have a strong recommendation to use this over the auth.role() = 'authenticated' technique. In one customer’s database, this reduced a query from 46 seconds to 7 milliseconds. Sometimes even we get it wrong - luckily you can trust that Postgres has it right. [Check it out](https://supabase.com/dashboard/project/_/auth/policies).

[![enterprise](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fpolicy.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/dashboard/project/_/auth/policies)

## State of DB 2022 [\#](https://supabase.com/blog/beta-update-may-2022\#state-of-db-2022)

Basedash conducted a survey that takes the pulse of the current databases that teams, individuals, startups, enterprises and hobbyists are using.

Supabase was listed in two categories, including the first place in satisfaction for hosting providers (84% of users would use us again 🙏). [Full results](https://stateofdb.com/).

[![secret scanning](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fdatabasesurvey.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://stateofdb.com/)

## Supabase Happy Hour \#5 [\#](https://supabase.com/blog/beta-update-may-2022\#supabase-happy-hour-5)

For the fifth edition of our Happy Hour streaming, we had a chat with our CEO and co-founder, Paul Copplestone. We went through some of the history of Supabase, our culture, why PostgreSQL was the right call, and hints about the future of the product. [Watch the episode](https://www.youtube.com/watch?v=_k7GqVDSFvw).

[![community day](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fhappyhour.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://www.youtube.com/watch?v=_k7GqVDSFvw)

## Supabase on Software Engineering Radio [\#](https://supabase.com/blog/beta-update-may-2022\#supabase-on-software-engineering-radio)

I chatted with SE Radio host Jeremy Jung about all things Supabase: building an API layer with postgREST, authentication using GoTrue, row-level security, forking open source projects, using the write ahead log to implement real time updates, provisioning and monitoring databases, user support, incidents, and open source licenses. [Listen to the podcast](https://www.se-radio.net/2022/05/episode-511-ant-wilson-on-supabase-postgres-as-a-service/).

[![open source](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fse_radio_image.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://www.se-radio.net/2022/05/episode-511-ant-wilson-on-supabase-postgres-as-a-service/)

## Supabase is Hiring for Sales Assist [\#](https://supabase.com/blog/beta-update-may-2022\#supabase-is-hiring-for-sales-assist)

There is an opportunity to work inside the growth team at Supabase. It's still a small team so you'd be getting in at the ground floor. If you love dev tools and are passionate about talking to customers, then you're who we're looking for! [Read the role spec here](https://boards.greenhouse.io/supabase/jobs/4530789004).

[![supabrew](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fhiring.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://boards.greenhouse.io/supabase/jobs/4530789004)

## Partner Showcase [\#](https://supabase.com/blog/beta-update-may-2022\#partner-showcase)

### Deepnote [\#](https://supabase.com/blog/beta-update-may-2022\#deepnote)

Deepnote is a data notebook that’s built for collaboration — Jupyter compatible, works magically in the cloud, and sharing is as easy as sending a link.

You can connect your Supabase Postgres Database to your Deepnote notebooks to quickly analyze data and share your findings with others. [Check out the guide](https://docs.deepnote.com/integrations/supabase).

[![supabrew](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fgraph.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://docs.deepnote.com/integrations/supabase)

## Made with Supabase [\#](https://supabase.com/blog/beta-update-may-2022\#made-with-supabase)

### Polypane [\#](https://supabase.com/blog/beta-update-may-2022\#polypane)

A browser that help you design, build and test better websites. Who doesn't want that? [Polypane](https://polypane.app/) helps with responsive design, accessibility, SEO, performance, design accuracy, semantic HTML, social media tags... and everything else. Built by: [@kilianvalkhof](https://twitter.com/kilianvalkhof).

[![supabrew](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fpolypane.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://polypane.app/)

### Pawternity Hub [\#](https://supabase.com/blog/beta-update-may-2022\#pawternity-hub)

[Pawternity Hub](https://pawternityhub.netlify.app/) is a Pet Adoption website where people can find local pets around their area to adopt. Started in a hackathon while brainstorming ideas to help the community, it was built with React and Bootstrap and uses the PetFinder API. Built by [@NathanJoSuarez](https://twitter.com/NathanJoSuarez).

[![supabrew](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fpawhub.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://pawternityhub.netlify.app/)

Discover other projects: Made with Supabase

## Issue Bounties [\#](https://supabase.com/blog/beta-update-may-2022\#issue-bounties)

- Fix: [crash in aws sdk](https://issuehunt.io/r/supabase/storage-api/issues/141)

## Quick Product Updates [\#](https://supabase.com/blog/beta-update-may-2022\#quick-product-updates)

- Fix: [Added reuse interval for token refresh](https://github.com/supabase/gotrue/pull/466)

## Community Highlights [\#](https://supabase.com/blog/beta-update-may-2022\#community-highlights)

- Morrow is looking for a full Senior Full Stack TypeScript Developer (Supabase Focus): [Job post](https://jobs.themorrow.digital/24826)
- The StackOverflow podcast with Matt and Cassidoo talking about Supabase’s Series B and open source. [Podcast](https://stackoverflow.blog/2022/05/17/open-source-is-winning-over-developers-and-investors-ep-442/)
- Migrate your MySQL database to Postgres with Supabase, Hasura & pgloader. [Blog](https://medium.com/@adi_myth/migrate-your-mysql-database-to-postgres-with-supabase-hasura-pgloader-3ef63bedd38)
- Here’s Why You Should Ditch MongoDB and Switch to Supabase. [Blog](https://javascript.plainenglish.io/heres-why-you-should-ditch-mongodb-and-switch-to-supabase-374b43f4ebc2)
- What is Supabase? [Video](https://www.youtube.com/watch?v=v2W7QJMMIA0)
- Anima converted Supabase’s Social Auth component into a native Figma component, with over 400 variants. [Link](https://unruffled-hoover-de9320.netlify.app/?path=/story/auth-auth--with-coloured-social-auth&args=socialLayout:horizontal)
- How To Build A Nuxt 3 Ionic Capacitor Starter App, Supabase Setup and Authentication. [Blog](https://dev.to/aaronksaunders/how-to-build-a-nuxt-3-ionic-capacitor-starter-app-supabase-setup-and-authentication-3gd0)
- How to create and test a GitHub Action that generates Supabase database types. [Blog](https://dev.to/lyqht/how-to-create-and-test-a-github-action-that-generates-supabase-database-types-1l6b)

## Supabase GitHub [\#](https://supabase.com/blog/beta-update-may-2022\#supabase-github)

We hit 49K stars!!: [repository.surf/supabase](https://repository.surf/supabase)

[![swag store](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fstars.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://repository.surf/supabase)

## Meme Zone [\#](https://supabase.com/blog/beta-update-may-2022\#meme-zone)

If you made it this far in the blog post you deserve a treat. [Follow us on Twitter](https://twitter.com/supabase) for more.

[![swag store](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-may%2Fmeme.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://twitter.com/supabase)

## Get started with Supabase [\#](https://supabase.com/blog/beta-update-may-2022\#get-started-with-supabase)

- Start using Supabase today: **[supabase.com/dashboard](https://supabase.com/dashboard/)**
- Make sure to **[star us on GitHub](https://github.com/supabase/supabase)**
- Follow us **[on Twitter](https://twitter.com/supabase)**
- Subscribe to our **[YouTube channel](https://www.youtube.com/c/supabase)**
- Become a **[sponsor](https://github.com/sponsors/supabase)**
- Join the **[team](https://about.supabase.com/careers)**

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-may-2022&text=Supabase%20Beta%20May%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-may-2022&text=Supabase%20Beta%20May%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-may-2022&t=Supabase%20Beta%20May%202022)

[Last post\\
\\
**Python data loading with Supabase** \\
\\
17 June 2022](https://supabase.com/blog/loading-data-supabase-python)

[Next post\\
\\
**How Mike Lyndon is using Supabase to accelerate development of AllPullTogether** \\
\\
26 May 2022](https://supabase.com/blog/how-supabase-accelerates-development-of-all-pull-together)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Wildcard Auth Redirects](https://supabase.com/blog/beta-update-may-2022#wildcard-auth-redirects)
- [Supabase Edge functions with Webhooks](https://supabase.com/blog/beta-update-may-2022#supabase-edge-functions-with-webhooks)
- [Metrics for everybody](https://supabase.com/blog/beta-update-may-2022#metrics-for-everybody)
- [Improved Policy Editor](https://supabase.com/blog/beta-update-may-2022#improved-policy-editor)
- [State of DB 2022](https://supabase.com/blog/beta-update-may-2022#state-of-db-2022)
- [Supabase Happy Hour #5](https://supabase.com/blog/beta-update-may-2022#supabase-happy-hour-5)
- [Supabase on Software Engineering Radio](https://supabase.com/blog/beta-update-may-2022#supabase-on-software-engineering-radio)
- [Supabase is Hiring for Sales Assist](https://supabase.com/blog/beta-update-may-2022#supabase-is-hiring-for-sales-assist)
- [Partner Showcase](https://supabase.com/blog/beta-update-may-2022#partner-showcase)
  - [Deepnote](https://supabase.com/blog/beta-update-may-2022#deepnote)
- [Made with Supabase](https://supabase.com/blog/beta-update-may-2022#made-with-supabase)
  - [Polypane](https://supabase.com/blog/beta-update-may-2022#polypane)
  - [Pawternity Hub](https://supabase.com/blog/beta-update-may-2022#pawternity-hub)
- [Issue Bounties](https://supabase.com/blog/beta-update-may-2022#issue-bounties)
- [Quick Product Updates](https://supabase.com/blog/beta-update-may-2022#quick-product-updates)
- [Community Highlights](https://supabase.com/blog/beta-update-may-2022#community-highlights)
- [Supabase GitHub](https://supabase.com/blog/beta-update-may-2022#supabase-github)
- [Meme Zone](https://supabase.com/blog/beta-update-may-2022#meme-zone)
- [Get started with Supabase](https://supabase.com/blog/beta-update-may-2022#get-started-with-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-may-2022&text=Supabase%20Beta%20May%202022)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-may-2022&text=Supabase%20Beta%20May%202022)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fbeta-update-may-2022&t=Supabase%20Beta%20May%202022)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)