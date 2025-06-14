---
url: "https://supabase.com/docs/guides/api"
title: "REST API | Supabase Docs"
---

REST API

# REST API

* * *

Supabase auto-generates an API directly from your database schema allowing you to connect to your database through a restful interface, directly from the browser.

The API is auto-generated from your database and is designed to get you building as fast as possible, without writing a single line of code.

You can use them directly from the browser (two-tier architecture), or as a complement to your own API server (three-tier architecture).

## Features [\#](https://supabase.com/docs/guides/api\#rest-api-overview)

Supabase provides a RESTful API using [PostgREST](https://postgrest.org/). This is a very thin API layer on top of Postgres.
It exposes everything you need from a CRUD API at the URL `https://<project_ref>.supabase.co/rest/v1/`.

The REST interface is automatically reflected from your database's schema and is:

- **Instant and auto-generated.**

As you update your database the changes are immediately accessible through your API.
- **Self documenting.**

Supabase generates documentation in the Dashboard which updates as you make database changes.
- **Secure.**

The API is configured to work with PostgreSQL's Row Level Security, provisioned behind an API gateway with key-auth enabled.
- **Fast.**

Our benchmarks for basic reads are more than 300% faster than Firebase. The API is a very thin layer on top of Postgres, which does most of the heavy lifting.
- **Scalable.**

The API can serve thousands of simultaneous requests, and works well for Serverless workloads.

The reflected API is designed to retain as much of Postgres' capability as possible including:

- Basic CRUD operations (Create/Read/Update/Delete)
- Arbitrarily deep relationships among tables/views, functions that return table types can also nest related tables/views.
- Works with Postgres Views, Materialized Views and Foreign Tables
- Works with Postgres Functions
- User defined computed columns and computed relationships
- The Postgres security model - including Row Level Security, Roles, and Grants.

The REST API resolves all requests to a single SQL statement leading to fast response times and high throughput.

Reference:

- [Docs](https://postgrest.org/)
- [Source Code](https://github.com/PostgREST/postgrest)

## API URL and keys [\#](https://supabase.com/docs/guides/api\#api-url-and-keys)

You can find the API URL and Keys in the [Dashboard](https://supabase.com/dashboard/project/_/settings/api).

### Is this helpful?

NoYes

### On this page

[Features](https://supabase.com/docs/guides/api#rest-api-overview) [API URL and keys](https://supabase.com/docs/guides/api#api-url-and-keys)