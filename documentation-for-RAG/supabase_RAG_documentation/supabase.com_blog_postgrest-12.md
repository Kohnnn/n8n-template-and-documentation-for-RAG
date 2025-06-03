---
url: "https://supabase.com/blog/postgrest-12"
title: "PostgREST 12"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# PostgREST 12

13 Dec 2023

•

4 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![PostgREST 12](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-postgrest-12%2Fpostgrest12-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

PostgREST 12 is out. In this post, we'll focus on a few of the major features. For the complete list, check out the [release on GitHub](https://github.com/PostgREST/postgrest/releases/tag/v12.0.0).

## Performance: JWT Caching [\#](https://supabase.com/blog/postgrest-12\#performance-jwt-caching)

Until now, PostgREST has validated JWTs on every request. As of PostgREST 12, the JWT is cached on the first request using the `exp` claim to set the cache entry's lifetime.

Why is that a big deal? Well, it turns out decoding JWTs is expensive. Very expensive.

`
## before
$ curl 'localhost:3000/authors_only' -H "Authorization: Bearer $JWT" -D -
HTTP/1.1 200 OK
Server-Timing: jwt;dur=147.7
## after, with JWT caching
$ curl 'localhost:3000/authors_only' -H "Authorization: Bearer $JWT" -D -
HTTP/1.1 200 OK
Server-Timing: jwt;dur=14.1
`

The JWT cache shaves over 130ms off the server side timing. For projects with a high volume of API calls, upgrading to PostgREST 12 gives you faster responses, higher throughput, and lower resource consumption.

## Server Timing Header [\#](https://supabase.com/blog/postgrest-12\#server-timing-header)

Did you notice the `Server-Timing` header in the last example? [That's new too](https://postgrest.org/en/v12.0/references/admin.html#server-timing-header) and it does more than measure JWT decoding duration.

Here's a complete reference to what you can extract from your responses:

`
Server-Timing:
	jwt;dur=14.9,
	parse;dur=71.1,
	plan;dur=109.0,
	transaction;dur=353.2,
	response;dur=4.4
`

Where the information from each phase is internally timed by PostgREST for better visibility into server side performance.

## Aggregate Functions [\#](https://supabase.com/blog/postgrest-12\#aggregate-functions)

Support for aggregate functions has been [much requested feature](https://github.com/supabase/postgrest-js/issues/206) that went through multiple iterations of design and review.

Currently, PostgREST supports `avg`, `count`, `max`, `min`, `sum`. Here's a minimal example using `count`:

`
$ curl 'http://postgrest/blog_post?select=id.count()'
[\
{\
    "count": 51,\
}\
]
`

We can also add a “group by” simply by adding another element to the select clause.

`
$ curl 'http://postgrest/blog_post?select=title,id.count()'
[\
{\
    "title": "Supabase Blog",\
    "count": 40\
},\
{\
    "title": "Contributors Blog",\
    "count": 11\
},\
...\
`\
\
This example only scratches the surface. Aggregates are fully-compatible with [resource embedding](https://postgrest.org/en/stable/references/api/resource_embedding.html) which yields an extremely versatile interface. We'll explore this feature more in a deep-dive coming soon.\
\
## Media Type Handlers [\#](https://supabase.com/blog/postgrest-12\#media-type-handlers)\
\
PostgREST now gives you the flexibility to [handle your custom media types and override the built-in ones](https://postgrest.org/en/v12.0/references/api/media_type_handlers.html). Among other things, that enables [serving HTML, javascript, or whatever you can think of, straight from your database](https://postgrest.org/en/latest/how-tos/providing-html-content-using-htmx.html).\
\
`\
create domain "text/html" as text;\
create or replace function api.index()\
returns "text/html"\
language sql\
as $$\
select $html$\
    <!DOCTYPE html>\
    <html>\
    <head>\
      <meta charset="utf-8">\
      <meta name="viewport" content="width=device-width, initial-scale=1">\
      <title>PostgREST + HTMX To-Do List</title>\
      <!-- Tailwind for CSS styling -->\
      <link href="https://unpkg.com/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">\
    </head>\
    <body class="bg-gray-900">\
      <div class="flex justify-center">\
        <div class="max-w-lg mt-5 p-6 bg-gray-800 border border-gray-800 rounded-lg shadow-xl">\
          <h5 class="mb-3 text-2xl font-bold tracking-tight text-white">PostgREST + HTMX To-Do List</h5>\
        </div>\
      </div>\
    </body>\
    </html>\
$html$;\
$$;\
`\
\
With PostgREST running locally we can then navigate to [localhost:3000/rpc/index](http://localhost:3000/rpc/index) to see\
\
![Media Type Handlers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-postgrest-12%2Fpostgrest-12-media-type-handlers.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\
\
We're still working through the full implications of this feature, but we're very excited internally about the possibilities it unlocks! Similar to aggregate functions, there's a dedicated post for this feature on the way.\
\
## Availability [\#](https://supabase.com/blog/postgrest-12\#availability)\
\
For self-hosting, check out the PostgREST [release on GitHub](https://github.com/PostgREST/postgrest/releases/tag/v12.0.0).\
\
The latest version will be rolled out across all projects on the managed platform soon. Keep an eye out for notifications inside [Supabase Studio](https://supabase.com/dashboard).\
\
[Launch Week![Supabase Launch Week X icon](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Flwx%2Flogos%2Flwx_logo.svg&w=32&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/launch-week)\
\
11-15 Dec\
\
Main Stage\
\
[Day 1 -Supabase Studio: introducing an **AI Assistant**, **Postgres roles**, and **user impersonation**](https://supabase.com/blog/studio-introducing-assistant)\
\
[Day 2 -Edge Functions: **Node** and native **npm** compatibility](https://supabase.com/blog/edge-functions-node-npm)\
\
[Day 3 -Introducing Supabase **Branching**, a Postgres database for every pull request](https://supabase.com/blog/supabase-branching)\
\
[Day 4 -Supabase Auth: **Identity Linking**, **Session Control**, **Password Protection** and **Hooks**](https://supabase.com/blog/supabase-auth-identity-linking-hooks)\
\
[Day 5 -Introducing **Read Replicas** for low latency](https://supabase.com/blog/introducing-read-replicas)\
\
Build Stage\
\
[01 -Supabase Album](https://supabase.productions/)\
\
[02 -Postgres Language Server](https://supabase.com/blog/postgres-language-server-implementing-parser)\
\
[03 -Design at Supabase](https://supabase.com/blog/how-design-works-at-supabase)\
\
[04 -Supabase Grafana](https://github.com/supabase/supabase-grafana)\
\
[05 -pg\_graphql: Postgres functions](https://supabase.com/blog/pg-graphql-postgres-functions)\
\
[06 -PostgREST 12](https://supabase.com/blog/postgrest-12)\
\
[07 -Supavisor 1.0](https://supabase.com/blog/supavisor-postgres-connection-pooler)\
\
[08 -Supabase Wrappers v0.2](https://supabase.com/blog/supabase-wrappers-v02)\
\
[09 -Supabase Libraries V2](https://supabase.com/blog/client-libraries-v2)\
\
[10 -Supabase x Fly.io](https://supabase.com/blog/postgres-on-fly-by-supabase)\
\
[11 -Top 10 Launches of LWX](https://supabase.com/blog/launch-week-x-best-launches)\
\
[Supabase Launch Week X Hackathon](https://supabase.com/blog/supabase-hackathon-lwx)\
\
[Supabase Launch Week X Community Meetups](https://supabase.com/blog/community-meetups-lwx)\
\
Share this article\
\
[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12&text=PostgREST%2012)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12&text=PostgREST%2012)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12&t=PostgREST%2012)\
\
[Last post\\
\\
**Supabase Wrappers v0.2: Query Pushdown & Remote Subqueries** \\
\\
14 December 2023](https://supabase.com/blog/supabase-wrappers-v02)\
\
[Next post\\
\\
**Supabase Branching** \\
\\
13 December 2023](https://supabase.com/blog/supabase-branching)\
\
[launch-week](https://supabase.com/blog/tags/launch-week) [postgrest](https://supabase.com/blog/tags/postgrest) [planetpg](https://supabase.com/blog/tags/planetpg)\
\
On this page\
\
- [Performance: JWT Caching](https://supabase.com/blog/postgrest-12#performance-jwt-caching)\
- [Server Timing Header](https://supabase.com/blog/postgrest-12#server-timing-header)\
- [Aggregate Functions](https://supabase.com/blog/postgrest-12#aggregate-functions)\
- [Media Type Handlers](https://supabase.com/blog/postgrest-12#media-type-handlers)\
- [Availability](https://supabase.com/blog/postgrest-12#availability)\
\
Share this article\
\
[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12&text=PostgREST%2012)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12&text=PostgREST%2012)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12&t=PostgREST%2012)\
\
## Build in a weekend, scale to millions\
\
[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)