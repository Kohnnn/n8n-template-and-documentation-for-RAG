---
url: "https://supabase.com/blog/supabase-local-dev"
title: "Supabase Local Dev: migrations, branching, and observability"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Local Dev: migrations, branching, and observability

08 Aug 2023

•

16 minute read

[![Qiao Han avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsweatybridge.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Qiao HanEngineering](https://github.com/sweatybridge)

[![Bobbie Soedirgo avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsoedirgo.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Bobbie SoedirgoEngineering](https://github.com/soedirgo)

[![Jonny Summers-Muir avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmildtomato.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jonny Summers-MuirProduct Design](https://github.com/mildtomato)

![Supabase Local Dev: migrations, branching, and observability](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fthumb-day2.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

One of our goals at Supabase is to make Postgres development delightful. To do this, we need to simplify the experience between our CLI, your code editor, and the remote Postgres database powering your applications.

We received feedback recently about our local development experience, encouraging us to improve. This iteration introduces many new features to address that feedback. Let’s jump into a few of the features we’re launching today.

Local Development and Database Branching // a more collaborative Supabase workflow 🚀 - YouTube

Supabase

54.4K subscribers

[Local Development and Database Branching // a more collaborative Supabase workflow 🚀](https://www.youtube.com/watch?v=N0Wb85m3YMI)

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

[Watch on YouTube](https://www.youtube.com/watch?v=N0Wb85m3YMI "Watch on YouTube")

## Postgres Language Server [\#](https://supabase.com/blog/supabase-local-dev\#postgres-language-server)

![Postgres Language Server](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fpostgres-language-server.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

One of the unique features of Supabase is the ability to access your Postgres database directly from a browser or mobile app through our [Serverless APIs](https://supabase.com/docs/guides/api). This means that developers are writing more [PL/pgSQL](https://www.postgresql.org/docs/current/plpgsql.html).

While code editors have great support for most programming languages, SQL support is underwhelming. We want to make Postgres as simple as Python. Our recently announced [Postgres Language Server](https://github.com/supabase/postgres_lsp) takes us a step in that direction - eventually it will provide first-class support for Postgres in your favorite code editor including Linting, Syntax Highlighting, Migrations Parsing, SQL Auto-complete, and Intellisense.

The Postgres Language Server is not ready for Production just yet. The majority of work is still ahead, but we've verified that the technical approach works and we're making it public now so that we can develop it in the open with input from the community. We’re already receiving amazing [feedback](https://github.com/supabase/postgres_lsp/discussions) and [support](https://news.ycombinator.com/item?id=37020610).

Follow the progress of the [Postgres Language Server on GitHub](https://github.com/supabase/postgres_lsp).

## Observability tools for Postgres [\#](https://supabase.com/blog/supabase-local-dev\#observability-tools-for-postgres)

![Inspect your database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Finspect-your-database.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’ve added [debugging utilities](https://supabase.com/docs/guides/database/inspect) to our CLI to identify production issues via the `supabase inspect db` command. This interface includes 19 different commands to help you solve everything from slow queries to redundant indexes.

A lot of the credit for this belongs to [Heroku’s pg-extras](https://github.com/heroku/heroku-pg-extras) feature, an amazingly useful set of functionality. We’ve adapted the work they started, added a few additional commands, and made it available for any Postgres database. Simply append the `--db-url` param to use these commands with your own Postgres database.

This is just a starting point for the Supabase inspector. We’ll grow this feature to become an essential part of your Postgres toolkit.

See full command

Read the docs

## Easier backups [\#](https://supabase.com/blog/supabase-local-dev\#easier-backups)

![How to back up your database with Supabase CLI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fbackup-your-database.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’ve made it even easier to backup and migrate your database, using `supabase db dump`. Under the hood, this simply uses [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) (it's just Postgres, after all). However we also handle a few of the hairy issues that you might need to navigate on your own, like object permissions.

See full command

## Improved Database Migrations [\#](https://supabase.com/blog/supabase-local-dev\#improved-database-migrations)

![modify your database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fmodify-your-database.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’ve extended the CLI migration feature and added Dashboard support. Database migrations give you a way to update your database using version-controlled SQL files. We’ve built a lot of tooling around our migrations, including [reparation](https://supabase.com/docs/reference/cli/supabase-migration-repair), migration cleanup using the [squash](https://supabase.com/docs/reference/cli/supabase-migration-squash) command, and [diffing](https://supabase.com/docs/reference/cli/supabase-db-diff) (using [migra](https://github.com/djrobstep/migra)) to generate a new migration or to detect schema drift.

With the new Postgres Language Server, we hope to make it as easy to write Postgres migrations as it is to develop applications in TypeScript, Go, Python, or Rust.

Finally, we’ve added a Migrations view [in the dashboard](https://app.supabase.com/project/_/database/migrations) to track your migration history to improve the discoverability of migrations.

See full command

## Test and lint your database [\#](https://supabase.com/blog/supabase-local-dev\#test-and-lint-your-database)

![Test your database](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Ftest-your-database.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’ve simplified the database testing experience, with `supabase test`. Running `supabase test new` stubs out a [pgTAP test](https://pgtap.org/) for you to fill with testing logic. The CLI includes [pg\_prove and the TAP harness](https://pgtap.org/pg_prove), so all you need to do is run `supabase test db`.

To make life even easier, our friends at [Basejump](https://usebasejump.com/) have created an entire suite of [Supabase Test Helpers](https://github.com/usebasejump/supabase-test-helpers) which make it simple to create users, run tests as an [authenticated user](https://usebasejump.com/blog/testing-on-supabase-with-pgtap#testing-authenticated), and test your [RLS policies](https://usebasejump.com/blog/testing-on-supabase-with-pgtap#rls-testing).

Finally, while you wait for us to make progress on the Language Server, we’ve added [support for linting](https://supabase.com/docs/guides/cli/testing-and-linting#linting-your-database) through the excellent [plpgsql\_check](https://github.com/okbob/plpgsql_check) extension.

See full command

## Database seeding [\#](https://supabase.com/blog/supabase-local-dev\#database-seeding)

![Support for seeding](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fsupport-for-seeding.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Seeding is the process of populating a database with initial data, typically used to provide sample or default records for testing and development purposes. This gives you a reproducible development environment across your entire team.

We’ve added [support for seeding](https://supabase.com/docs/guides/cli/seeding-your-database) to populate your local databases with data whenever you run `supabase start` or `supabase db reset`.

We’ve also worked with our friends at Snaplet to [generate seed data](https://supabase.com/docs/guides/cli/seeding-your-database#generating-seed-data) directly from your database:

`
npx snaplet generate --sql > supabase/seed.sql
`

## Type generators [\#](https://supabase.com/blog/supabase-local-dev\#type-generators)

![End to end Type Safety](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fend-to-end-type-safety.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Type generators introspect a PostgreSQL schema and automatically generate TypeScript definitions. This gives you [end-to-end type safety](https://www.youtube.com/watch?v=VSNgAIObBdw) from the database to the browser.

In the past month, we've added relationship detection in supabase-js. Foreign keys are now included in the generated types so that supabase-js can detect whether a referenced table should be an array (one-to-many) or an object (many-to-one). We've also added Helper Types to improve the developer experience for common scenarios, like short-hand accessors:

`
// Before
let movie: Database['public']['Tables']['movies']['Row'] = // ...
// After
let movie: Tables<'movies'> = // ...
`

See full command

## Official GitHub Action [\#](https://supabase.com/blog/supabase-local-dev\#official-github-action)

![Support for GitHub Actions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fsupport-for-github-actions.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’ve developed an official [GitHub Action](https://github.com/marketplace/actions/supabase-cli-action) which leverages the CLI. You can [generate types on every PR](https://supabase.com/docs/guides/cli/github-action/generating-types), or run [your tests on every commit](https://supabase.com/docs/guides/cli/github-action/testing).

## Local Logging and Debugging [\#](https://supabase.com/blog/supabase-local-dev\#local-logging-and-debugging)

Logs are now accessible locally in the Dashboard. Last launch week we released an open source logging server, with support for BigQuery. In the past few months we’ve added Postgres support to this server. This means that all of your local logs are accessible with no additional config - simply run supabase start and then visit the local dashboard to start debugging.

![Logs are now accessible locally in the dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Flocal-logging-debugging.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Stable releases [\#](https://supabase.com/blog/supabase-local-dev\#stable-releases)

We’ve moved the Supabase CLI to a fortnightly stable-release cycle. Every 2 weeks, we will update the [`latest`](https://www.npmjs.com/package/supabase?activeTab=versions) tag on npm, the [`supabase/tap`](https://github.com/supabase/homebrew-tap/blob/main/supabase.rb) for homebrew, and the [`supabase`](https://github.com/supabase/homebrew-tap/blob/main/supabase.rb) scoop bucket. You can find the binary downloads in our GitHub [latest release](https://github.com/supabase/cli/releases/latest).

For the adventurous feature hunters, we’ve added a `beta` release channel for the CLI, with new releases on every PR merged. You can follow [this guide](https://github.com/supabase/cli#install-the-cli) to install Supabase CLI (beta).

## Branching and Preview Environments [\#](https://supabase.com/blog/supabase-local-dev\#branching-and-preview-environments)

And finally, probably our most anticipated feature - branching:

![Searching branches with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-8%2Fday-2%2Fbranching-02.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’ve made major improvements to our local development with the features above - but we have bigger ambitions. For several months we’ve been developing Supabase branching and today we're opening it up for alpha testers.

Supabase isn’t simply a database, it’s an entire backend - everything from your Postgres database to your [50GB videos](https://supabase.com/blog/storage-v3-resumable-uploads). Branching improves the experience of managing environments so that developers and teams spend less time on DevOps and more time building.

### Supabase branching is hard [\#](https://supabase.com/blog/supabase-local-dev\#supabase-branching-is-hard)

Every project is a Postgres database, wrapped in a suite of tools like [Auth](https://supabase.com/auth), [Storage](https://supabase.com/storage), [Edge Functions](https://supabase.com/edge-functions), [Realtime](https://supabase.com/realtime) and [Vectors](https://supabase.com/vector), and encompassed by [API middleware](https://supabase.com/docs/guides/api) and [logs](https://supabase.com/blog/supabase-logs-self-hosted).

A good branching solution requires each tool to provide multi-tenancy support so that:

1. Data can be isolated from production for security.
2. Compute can be isolated from each other to avoid noisy-neighbors.

### How does branching work? [\#](https://supabase.com/blog/supabase-local-dev\#how-does-branching-work)

We use Git to bridge the gap between your local development environment and your hosted database. For now, we’ve focused on GitHub.

Every time you open a new Pull Request on GitHub, a corresponding “Preview Environment” is created. Each preview branch is an isolated Firecracker instance that pauses automatically after a period of inactivity. Every time a change is pushed to GitHub, the migrations within the `./supabase/migrations` folder are run against the Preview Branch so that your entire team is working from the same source of truth.

When you hit merge on your Pull Request we run the migrations on your Production database.

### What about data? [\#](https://supabase.com/blog/supabase-local-dev\#what-about-data)

We’re starting with seed data. Any SQL with `./supabase/seed.sql` will populate your Preview Branch. This provides your entire team with an isolated and reproducible environment, safe from any data privacy concerns.

Importantly, we _aren’t_ cloning production data until we find something appropriate for data security. We know that copy-on-write is an available option, and with the appropriate anonymization techniques it seems like a promising way to provide a “production-like” test environment.

We’ll also need to figure out what this means for large files in Supabase Storage. Do you need to anonymize your photos and videos? This is a work in progress and we’re open to feedback.

Either way, we want to support _both_ seed data and anonymized production data, so that teams can choose their preference based on their risk profile. It makes sense to start with a seed.

### Is it available yet? [\#](https://supabase.com/blog/supabase-local-dev\#is-it-available-yet)

##### Branching update 12/13/2023

We are [rolling out access](https://supabase.com/blog/supabase-branching) and we'll be onboarding organizations in batches over the next few weeks. You can still [sign up for access](https://forms.supabase.com/branching-request).

## Get started [\#](https://supabase.com/blog/supabase-local-dev\#get-started)

Jump into our updated [Local Development documentation](https://supabase.com/docs/guides/cli) to get started with the CLI.

If you’re an existing user simply [update your CLI](https://supabase.com/docs/guides/cli/getting-started#updating-the-supabase-cli) and check out the [full command reference](https://supabase.com/docs/reference/cli/introduction) for all the latest commands.

## More Launch Week 8 [\#](https://supabase.com/blog/supabase-local-dev\#more-launch-week-8)

- [Hugging Face is now supported in Supabase](https://supabase.com/blog/hugging-face-supabase)
- [Launch Week 8](https://supabase.com/launch-week)
- [Coding the stars - an interactive constellation with Three.js and React Three Fiber](https://supabase.com/blog/interactive-constellation-threejs-react-three-fiber)
- [Why we'll stay remote](https://supabase.com/blog/why-supabase-remote)
- [Postgres Language Server](https://github.com/supabase/postgres_lsp)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-local-dev&text=Supabase%20Local%20Dev%3A%20migrations%2C%20branching%2C%20and%20observability)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-local-dev&text=Supabase%20Local%20Dev%3A%20migrations%2C%20branching%2C%20and%20observability)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-local-dev&t=Supabase%20Local%20Dev%3A%20migrations%2C%20branching%2C%20and%20observability)

[Last post\\
\\
**Supabase Studio 3.0: AI SQL Editor, Schema Diagrams, and new Wrappers** \\
\\
9 August 2023](https://supabase.com/blog/supabase-studio-3-0)

[Next post\\
\\
**Hugging Face is now supported in Supabase** \\
\\
7 August 2023](https://supabase.com/blog/hugging-face-supabase)

[launch-week](https://supabase.com/blog/tags/launch-week) [announcements](https://supabase.com/blog/tags/announcements)

On this page

- [Postgres Language Server](https://supabase.com/blog/supabase-local-dev#postgres-language-server)
- [Observability tools for Postgres](https://supabase.com/blog/supabase-local-dev#observability-tools-for-postgres)
- [Easier backups](https://supabase.com/blog/supabase-local-dev#easier-backups)
- [Improved Database Migrations](https://supabase.com/blog/supabase-local-dev#improved-database-migrations)
- [Test and lint your database](https://supabase.com/blog/supabase-local-dev#test-and-lint-your-database)
- [Database seeding](https://supabase.com/blog/supabase-local-dev#database-seeding)
- [Type generators](https://supabase.com/blog/supabase-local-dev#type-generators)
- [Official GitHub Action](https://supabase.com/blog/supabase-local-dev#official-github-action)
- [Local Logging and Debugging](https://supabase.com/blog/supabase-local-dev#local-logging-and-debugging)
- [Stable releases](https://supabase.com/blog/supabase-local-dev#stable-releases)
- [Branching and Preview Environments](https://supabase.com/blog/supabase-local-dev#branching-and-preview-environments)
  - [Supabase branching is hard](https://supabase.com/blog/supabase-local-dev#supabase-branching-is-hard)
  - [How does branching work?](https://supabase.com/blog/supabase-local-dev#how-does-branching-work)
  - [What about data?](https://supabase.com/blog/supabase-local-dev#what-about-data)
  - [Is it available yet?](https://supabase.com/blog/supabase-local-dev#is-it-available-yet)
- [Get started](https://supabase.com/blog/supabase-local-dev#get-started)
- [More Launch Week 8](https://supabase.com/blog/supabase-local-dev#more-launch-week-8)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-local-dev&text=Supabase%20Local%20Dev%3A%20migrations%2C%20branching%2C%20and%20observability)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-local-dev&text=Supabase%20Local%20Dev%3A%20migrations%2C%20branching%2C%20and%20observability)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-local-dev&t=Supabase%20Local%20Dev%3A%20migrations%2C%20branching%2C%20and%20observability)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)