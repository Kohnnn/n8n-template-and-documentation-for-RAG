---
url: "https://supabase.com/alternatives/supabase-vs-heroku-postgres"
title: "Supabase vs Heroku Postgres"
---

Alternative

# Supabase vs Heroku Postgres

2022-05-26

•

4 minute read

[![author avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fawalias.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Ant WilsonCTO and Co-Founder](https://github.com/awalias)

## What is Heroku Postgres? [\#](https://supabase.com/alternatives/supabase-vs-heroku-postgres\#what-is-heroku-postgres)

Heroku is a cloud application platform that offers managed PostgreSQL as a service. They offer 5 levels of Postgres support from the Hobby Tier up to the Shield Tier, each with different levels of features and pricing. Heroku announced that starting November 28, 2022, they will [stop offering free product plans and will shut down free dynos and data services](https://blog.heroku.com/next-chapter). Since the announcement, developers started migrating their projects to Supabase.

## What is Supabase? [\#](https://supabase.com/alternatives/supabase-vs-heroku-postgres\#what-is-supabase)

Supabase also offers managed Postgres, the main difference is that with each deployment you also get:

- Auto-generated API - [never write an API again](https://supabase.com/docs/guides/api#rest-api-overview)
- Realtime - [subscribe to data changes via websockets](https://supabase.com/docs/reference/dart/subscribe)
- Auth - [users can log in and out of your application](https://supabase.com/auth)
- Functions - [deploy custom logic to the edge](https://supabase.com/edge-functions)
- Storage - [serve large files and folders](https://supabase.com/storage)
- Supavisor - [connection pooling useful for serverless computing](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler)

## How are they similar? [\#](https://supabase.com/alternatives/supabase-vs-heroku-postgres\#how-are-they-similar)

Heroku Postgres and Supabase both offer:

- [A web UI for managing your instance](https://supabase.com/docs/guides/database#table-view)
- SLAs and Enterprise-grade support packages
- Direct SSL connections to Postgres
- Postgres Extensions (see [Supabase Extensions](https://supabase.com/docs/guides/database/extensions), [Heroku Extensions](https://devcenter.heroku.com/articles/heroku-postgres-extensions-postgis-full-text-search))
- [Backups and PITR](https://supabase.com/blog/continuous-postgresql-backup-walg)
- [Postgres logs](https://supabase.com/docs/guides/platform/logs)
- Encryption-at-rest

## What are the differences? [\#](https://supabase.com/alternatives/supabase-vs-heroku-postgres\#what-are-the-differences)

### Core Features [\#](https://supabase.com/alternatives/supabase-vs-heroku-postgres\#core-features)

These are some of the key differences between Heroku Postgres and Supabase in terms of features:

- Supabase is more than just the raw database, it also comes with:
  - [Connection pooling](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pool) so that you won’t run out of connections in a serverless environment.
  - [Auto-generated APIs](https://supabase.com/docs/guides/api#rest-api-overview) based on your schema, so you can communicate with your database directly from the client.
  - [Realtime API](https://supabase.com/docs/reference/dart/subscribe) is useful for when you want to subscribe to changes to your database over websockets.
  - [Auth API](https://supabase.com/auth) can be used to leverage Postgres’s Row Level Security model, and control access to sensitive data on a per user, or per group level.
  - [Functions](https://supabase.com/edge-functions) can be deployed out to the edge directly from the Supabase CLI, which means you can run sensitive business logic or transformations in a serverless fashion.
    - You can also deploy edge functions to Heroku using their [Dynos](https://www.heroku.com/dynos) runtime in conjunction with something like [Fastly](https://www.fastly.com/).
  - [File Storage](https://supabase.com/storage) is useful for when your app needs to store large files and folders that aren’t suitable for storing within Postgres itself.
  - A spreadsheet-like web interface for building your schemas and inspecting data.

### Pricing [\#](https://supabase.com/alternatives/supabase-vs-heroku-postgres\#pricing)

The two services price quite differently, the key differences being:

- [Supabase pricing is based around usage](https://supabase.com/pricing), so you only pay for what you use.
- Heroku prices based on a tier model with [37 plans to choose from](https://elements.heroku.com/addons/heroku-postgresql#pricing).

Supabase’s Free Plan also includes a dedicated Postgres instance, and the best bit is you can upgrade to pro later without any interruptions.

### Global Deployments [\#](https://supabase.com/alternatives/supabase-vs-heroku-postgres\#global-deployments)

You may have strict data regulations that you must comply with, so choosing your region can be very important. Here’s how the deployment options stack up:

- Supabase can be deployed to any one of [12 data centers across the globe](https://github.com/supabase/supabase/discussions/4815#discussioncomment-1915129) (Free Plan included).
  - Since Supabase is fully open source - you can also [self host wherever you like](https://supabase.com/docs/guides/hosting/overview).
- You can deploy Heroku Postgres to two data centers (US and Europe) however [6 more data centers](https://devcenter.heroku.com/articles/regions) are available on the Enterprise plan.

## How to migrate from Heroku Postgres to Supabase [\#](https://supabase.com/alternatives/supabase-vs-heroku-postgres\#how-to-migrate-from-heroku-postgres-to-supabase)

Migrating is surprisingly simple. You just need to use the standard Postgres `pg_dump` and `psql` tools to export your Heroku database and import to Supabase. We created a handy guide for [migrating from Heroku to Supabase](https://supabase.com/docs/guides/migrations/heroku).

Share this article

[Previous comparison\\
\\
**Supabase vs Firebase** \\
\\
2022-05-26](https://supabase.com/alternatives/supabase-vs-firebase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)