---
url: "https://supabase.com/blog/supabase-beta-february-2021"
title: "Supabase Beta February 2021"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta February 2021

02 Mar 2021

•

3 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

Supabase is an open source Firebase alternative. We've now been building for one year. Here's what we released last month.

### Quick demo [\#](https://supabase.com/blog/supabase-beta-february-2021\#quick-demo)

Watch a full demo:

Supabase Beta \| February 2021 - YouTube

Supabase

54.4K subscribers

[Supabase Beta \| February 2021](https://www.youtube.com/watch?v=h-ses99G45g)

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

[Watch on YouTube](https://www.youtube.com/watch?v=h-ses99G45g "Watch on YouTube")

### Dashboard Sidebars [\#](https://supabase.com/blog/supabase-beta-february-2021\#dashboard-sidebars)

We've improved the UX of our Dashboard with sidebars in every section, including the Table view, the Auth section, and the SQL Editor.

![Our dashboard has sidebars](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffeb%2Fsidebar-tables.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### SQL Autocomplete [\#](https://supabase.com/blog/supabase-beta-february-2021\#sql-autocomplete)

Writing SQL just got 10x easier. We added autocomplete to the SQL editor, including table & column suggestions.

### Auth Redirects [\#](https://supabase.com/blog/supabase-beta-february-2021\#auth-redirects)

Redirect your users to specific route within your site on [`signIn()`](https://supabase.com/docs/reference/javascript/v1/auth-signin#sign-in-with-redirect) and [`signUp()`](https://supabase.com/docs/reference/javascript/auth-signup#sign-up-with-redirect).

![Redirect your users after sign up](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffeb%2Fauth-redirect.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Replication management [\#](https://supabase.com/blog/supabase-beta-february-2021\#replication-management)

We added a page to the Database section for managing Postgres Replication. It's still basic, but you can use it to manage your realtime API - choosing which tables are enabled, and which events to send.

![Replication management](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffeb%2Fmanage-replication.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Learning Resources [\#](https://supabase.com/blog/supabase-beta-february-2021\#learning-resources)

We've released a new [Resources](https://supabase.com/docs/resources) section in our docs, as well as two new Auth modules: [GoTrue Overview](https://supabase.com/docs/learn/auth-deep-dive/auth-gotrue) and [Google OAuth](https://supabase.com/docs/learn/auth-deep-dive/auth-google-oauth).

![Our dashboard has sidebars](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffeb%2Fdocs-resources.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### New Region [\#](https://supabase.com/blog/supabase-beta-february-2021\#new-region)

Launch your database in South Africa.

![Launch your database in South Africa](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffeb%2Fnew-region-south-africa.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Kaizen [\#](https://supabase.com/blog/supabase-beta-february-2021\#kaizen)

- We filled up our [Examples](https://supabase.com/docs/guides/examples) page with a lot of new content.
- We released a [Docker Compose](https://github.com/supabase/supabase/blob/master/docker/docker-compose.yml) file for running Supabase locally. This will be used in our upcoming CLI.
- We have a couple of pending RFCs which you may want to participate in:
  - [Planning our CLI and Local Development](https://github.com/supabase/cli/pull/2)
  - [Connection Pooling on Supabase](https://github.com/supabase/postgres/blob/rfc/connection_pooling/rfcs/0001-connection-pooling.md)

### Community [\#](https://supabase.com/blog/supabase-beta-february-2021\#community)

One of the community, [@ftonato](https://github.com/ftonato), has built an amazing [example](https://github.com/supabase/examples/tree/main/supabase-js-v1/with-stencil) that shows how to use Supabase with [Stencil](https://stenciljs.com/) (a Web Component compiler built by they [Ionic](https://ionicframework.com/) team.)

[Check it out!](https://github.com/supabase/examples/tree/main/supabase-js-v1/with-stencil)

![Supabase with Stencil](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffeb%2Fsupabase-stencil.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

- @kiwicopple on the LogRocket Podcast. [Link](https://podrocket.logrocket.com/9)
- @bdougie Livestream: More Fullstack React w RedwoodJS + Supabase. [Link](https://www.twitch.tv/videos/907698954)
- @gbibeaul created `useSupabase`: Supabase React Hooks. [GitHub](https://www.npmjs.com/package/use-supabase)

We hit 6000 GitHub stars on [GitHub](https://github.com/supabase/supabase)

![This image shows the Supabase GitHub star growth.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffeb%2Fgithub-stars-feb-2021.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Source: [repository.surf/supabase](https://repository.surf/supabase)

### Coming next [\#](https://supabase.com/blog/supabase-beta-february-2021\#coming-next)

Waiting for Supabase Storage? Here's a sneak peek for the upcoming Launch Week at the end of March.

![Supabase Storage coming soon](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Ffeb%2Fsupabase-storage.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Get started [\#](https://supabase.com/blog/supabase-beta-february-2021\#get-started)

- Start using Supabase today: [supabase.com/dashboard](https://supabase.com/dashboard/)
- Make sure to [star us on GitHub](https://github.com/supabase/supabase)
- Follow us [on Twitter](https://twitter.com/supabase)
- Subscribe to our [YouTube channel](https://www.youtube.com/c/supabase)
- Become a [sponsor](https://github.com/sponsors/supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-february-2021&text=Supabase%20Beta%20February%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-february-2021&text=Supabase%20Beta%20February%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-february-2021&t=Supabase%20Beta%20February%202021)

[Last post\\
\\
**Postgres as a CRON Server** \\
\\
5 March 2021](https://supabase.com/blog/postgres-as-a-cron-server)

[Next post\\
\\
**Cracking PostgreSQL Interview Questions** \\
\\
27 February 2021](https://supabase.com/blog/cracking-postgres-interview)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-february-2021&text=Supabase%20Beta%20February%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-february-2021&text=Supabase%20Beta%20February%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-february-2021&t=Supabase%20Beta%20February%202021)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)