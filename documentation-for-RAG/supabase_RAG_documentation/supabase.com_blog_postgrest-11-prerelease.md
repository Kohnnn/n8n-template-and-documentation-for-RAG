---
url: "https://supabase.com/blog/postgrest-11-prerelease"
title: "PostgREST 11 pre-release"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# PostgREST 11 pre-release

16 Dec 2022

•

5 minute read

[![Steve Chavez avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsteve-chavez.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Steve ChavezEngineering & PostgREST maintainer](https://github.com/steve-chavez)

![PostgREST 11 pre-release](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-community%2Fpostgrest.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

PostgREST 11 is not wrapped up yet, however a pre-release with the **[latest features and fixes](https://github.com/PostgREST/postgrest/releases/tag/v10.1.1.20221212)**
is available on the Supabase CLI.

In this blog post we'll cover some of the improved querying capabilities: spreading related tables, related orders and anti-joins.

## Spreading related tables [\#](https://supabase.com/blog/postgrest-11-prerelease\#spreading-related-tables)

Very often the way we structure a database is not the way we want to present it to the frontend application. For example, let's assume we have a `films` and `technical_specs` tables and
they form a one-to-one relationship.

Using PostgREST resource embedding, we can query them in one request like so

From HTTP:

`
GET /films?select=title,technical_specs(camera,laboratory,sound_mix)
`

or JavaScript:

``
const { data, error } = await supabase.from('films').select(`
    title,
    technical_specs (
      camera, laboratory, duration
    )
`)
``

Response:

`
[\
{\
    "title": "Pulp Fiction",\
    "technical_specs": {\
      "camera": "Arriflex 35-III",\
      "laboratory": "DeLuxe, Hollywood (CA), USA (color)",\
      "duration": "02:34:00"\
    }\
},\
"..."\
]
`

But we'd like to present a “flattened” result to the frontend, without the `technical_specs` object. For this we could create a new database view or function that shapes the json the way we want, but creating extra database objects is not always convenient.

Using the new “spread” operator(syntax borrowed from [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)), we can expand a related table columns and remove the nested object.

From HTTP:

`
GET /films?select=title,...technical_specs(camera,laboratory,duration)
`

or JavaScript:

``
const { data, error } = await supabase.from('films').select(`
    title,
    ...technical_specs (
      camera, laboratory, duration
    )
`)
``

Response:

`
[\
{\
    "title": "Pulp Fiction",\
    "camera": "Arriflex 35-III",\
    "laboratory": "DeLuxe, Hollywood (CA), USA (color)",\
    "duration": "02:34:00"\
},\
"..."\
]
`

This only works for one-to-one and many-to-one relationships for now but we're looking at ways to remove this restriction.

## Order by related tables [\#](https://supabase.com/blog/postgrest-11-prerelease\#order-by-related-tables)

It's also a common use case to order a table by a related table column. For example, suppose you'd like to order `films` based on the `technical_specs.duration` column.

You can now do it like so:

From HTTP:

`
GET /films?select=title,...technical_specs(duration)&order=technical_specs(duration).desc
`

or JavaScript:

``
const { data, error } = await supabase
.from('films')
.select(`
    title,
    ...technical_specs (
      duration
    )
`)
.order('technical_specs(duration)', { descending: true }))
``

Response:

`
[\
{\
    "title": "Amra Ekta Cinema Banabo",\
    "duration": "21:05:00"\
},\
{\
    "title": "Resan",\
    "duration": "14:33:00"\
},\
"..."\
]
`

Similarly to spreading related tables, this only works for one-to-one and many-to-one relationships.

## Anti-Joins [\#](https://supabase.com/blog/postgrest-11-prerelease\#anti-joins)

To do the equivalent of a left anti-join, you can now filter the rows where the related table is `null`.

From HTTP:

`
GET /films?select=title,nominations()&nominations=is.null
`

or JavaScript:

``
const { data, error } = await supabase
.from('films')
.select(`
    title,
    nominations()
`)
.is('nominations', null))
``

Response:

`
[\
{\
    "title": "Memories of Murder"\
},\
{\
    "title": "Rush"\
},\
{\
    "title": "Groundhog Day"\
},\
"..."\
]
`

Note that `nominations` doesn't select any columns so they don't show on the resulting response.

The equivalent of an inner join can be done by filtering the rows where the related table is `not null`.

`
GET /films?select=title,nominations(rank,...competitions(name))&nominations=not.is.null
`

``
const { data, error } = await supabase
.from('films')
.select(
    `
    title,
    nominations(rank,...competitions(name))
`
)
.not('nominations', 'is', null)
``

Response:

`
[\
{\
    "title": "Pulp Fiction"\
    "nominations": [\
      {"rank": 1, "name": "Palme d'Or"},\
      {"rank": 1, "name": "BAFTA Film Award"},\
      {"..."}\
    ]\
},\
"..."\
]
`

This was already possible with the `!inner` modifier( [introduced on PostgREST 9](https://supabase.com/blog/postgrest-9#resource-embedding-with-inner-joins))
but the `not null` filter is more flexible and can be used with an [or filter](https://supabase.com/docs/reference/javascript/or) to combine related tables' conditions.

## Try it out [\#](https://supabase.com/blog/postgrest-11-prerelease\#try-it-out)

This pre-release is not deployed to Supabase cloud but you can try it out locally with the [Supabase CLI](https://supabase.com/docs/reference/cli/introduction).

`
$ supabase start
`

Please try it and report any bugs, suggestions or ideas!

## More Launch Week 6 [\#](https://supabase.com/blog/postgrest-11-prerelease\#more-launch-week-6)

- [Day 1: New Supabase Docs, built with Next.js](https://supabase.com/blog/new-supabase-docs-built-with-nextjs)
- [Day 2: Supabase Storage v2: Image resizing and Smart CDN](https://supabase.com/blog/storage-image-resizing-smart-cdn)
- [Day 3: Multi-factor Authentication via Row Level Security Enforcement](https://supabase.com/blog/mfa-auth-via-rls)
- [Day 4: Supabase Wrappers, a Postgres FDW framework written in Rust](https://supabase.com/blog/postgres-foreign-data-wrappers-rust)
- [Day 5: Supabase Vault is now in Beta](https://supabase.com/blog/vault-now-in-beta)
- [Community Day](https://supabase.com/blog/launch-week-6-community-day)
- [Point in Time Recovery is now available](https://supabase.com/blog/postgres-point-in-time-recovery)
- [Custom Domain Names are now available](https://supabase.com/blog/custom-domain-names)
- [Wrap Up: everything we shipped](https://supabase.com/blog/launch-week-6-wrap-up)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&text=PostgREST%2011%20pre-release)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&text=PostgREST%2011%20pre-release)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&t=PostgREST%2011%20pre-release)

[Last post\\
\\
**Point in Time Recovery is now available for Pro projects** \\
\\
16 December 2022](https://supabase.com/blog/postgres-point-in-time-recovery)

[Next post\\
\\
**Supabase Vault is now in Beta** \\
\\
16 December 2022](https://supabase.com/blog/vault-now-in-beta)

[postgres](https://supabase.com/blog/tags/postgres) [launch-week](https://supabase.com/blog/tags/launch-week) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Spreading related tables](https://supabase.com/blog/postgrest-11-prerelease#spreading-related-tables)
- [Order by related tables](https://supabase.com/blog/postgrest-11-prerelease#order-by-related-tables)
- [Anti-Joins](https://supabase.com/blog/postgrest-11-prerelease#anti-joins)
- [Try it out](https://supabase.com/blog/postgrest-11-prerelease#try-it-out)
- [More Launch Week 6](https://supabase.com/blog/postgrest-11-prerelease#more-launch-week-6)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&text=PostgREST%2011%20pre-release)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&text=PostgREST%2011%20pre-release)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-prerelease&t=PostgREST%2011%20pre-release)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)