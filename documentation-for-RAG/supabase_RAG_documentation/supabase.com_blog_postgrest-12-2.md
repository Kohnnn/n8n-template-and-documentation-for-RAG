---
url: "https://supabase.com/blog/postgrest-12-2"
title: "PostgREST 12.2: Prometheus metrics"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# PostgREST 12.2: Prometheus metrics

16 Aug 2024

•

2 minute read

[![Steve Chavez avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsteve-chavez.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Steve ChavezEngineering & PostgREST maintainer](https://github.com/steve-chavez)

![PostgREST 12.2: Prometheus metrics](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fthumb_postgREST.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[PostgREST 12.2](https://github.com/PostgREST/postgrest/releases/tag/v12.2.0) is out! It comes with Observability and API improvements. In this post, we'll see what's new.

## Prometheus Metrics [\#](https://supabase.com/blog/postgrest-12-2\#prometheus-metrics)

Version 12.2 ships with Prometheus-compatible metrics for PostgREST's schema cache and connection pool. These are useful for troubleshooting, for example, when PostgREST's pool is starved for connections.

`
curl localhost:3001/metrics
# HELP pgrst_db_pool_timeouts_total The total number of pool connection timeouts
# TYPE pgrst_db_pool_timeouts_total counter
pgrst_db_pool_timeouts_total 7.0
# ....
`

A full list of supported metrics is available in the [PostgREST documentation](https://postgrest.org/en/latest/references/observability.html#metrics).

## Hoisted Function Settings [\#](https://supabase.com/blog/postgrest-12-2\#hoisted-function-settings)

Sometimes it's handy to set a custom timeout per function. You can now do this on 12.2 projects with:

`
create or replace function special_function()
returns void as $$
select pg_sleep(3); -- simulating some long-running process
$$
language sql
set statement_timeout to '4s';
`

And calling the function with the [RPC interface](https://supabase.com/docs/reference/javascript/rpc).

When doing `set statement_timeout` on the function, the `statement_timeout` will be “hoisted” and applied per transaction.

By default this also works for other settings, namely `plan_filter.statement_cost_limit` and `default_transaction_isolation`. The list of hoisted settings can be extended by modifying the [db-hoisted-tx-settings](https://postgrest.org/en/latest/references/configuration.html#db-hoisted-tx-settings) configuration.

Before 12.2, this could be done by setting a `statement_timeout` on the API roles, but this affected all the SQL statements executed by those roles.

## Max Affected [\#](https://supabase.com/blog/postgrest-12-2\#max-affected)

In prior versions of PostgREST, users could limit the number of records impacted by mutations (insert/update/delete) to 1 row using vendor media type `application/vnd.pgrst.object+json`. That supports a common use case but is not flexible enough to support user defined values.

12.2 introduces the `max-affected` preference to limit the affected rows up to a custom value.

For example:

`
curl -i "http://localhost:3000/items?id=lt.15" -X DELETE \
  -H "Content-Type: application/json" \
  -H "Prefer: handling=strict, max-affected=10"
`

If the number of affected records exceeds `max-affected` , an error is returned:

`
HTTP/1.1 400 Bad Request
{
    "code": "PGRST124",
    "message": "Query result exceeds max-affected preference constraint",
    "details": "The query affects 14 rows",
    "hint": null
}
`

## **Try it out** [\#](https://supabase.com/blog/postgrest-12-2\#try-it-out)

PostgREST v12.2 is already available on the Supabase platform on its latest patch version ( [v12.2.3](https://github.com/PostgREST/postgrest/releases/tag/v12.2.3)) for new projects. Spin up a new project or upgrade your existing project to try it out!

[Launch Week12](https://supabase.com/launch-week/12)

12-16 August

[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)

[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)

[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)

[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)

[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage

[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)

[02 -pg\_replicate](https://news.ycombinator.com/item?id=41209994)

[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)

[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)

[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)

[06 -vec2pg](https://supabase.com/blog/vec2pg)

[07 -pg\_graphql](https://supabase.com/blog/pg-graphql-1-5-7)

[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)

[09 -python-support](https://supabase.com/blog/python-support)

[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)

[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12-2&text=PostgREST%2012.2%3A%20Prometheus%20metrics)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12-2&text=PostgREST%2012.2%3A%20Prometheus%20metrics)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12-2&t=PostgREST%2012.2%3A%20Prometheus%20metrics)

[Last post\\
\\
**Postgres Foreign Data Wrappers with Wasm** \\
\\
16 August 2024](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

[Next post\\
\\
**Supabase Python** \\
\\
16 August 2024](https://supabase.com/blog/python-support)

[launch-week](https://supabase.com/blog/tags/launch-week) [release-notes](https://supabase.com/blog/tags/release-notes) [tech](https://supabase.com/blog/tags/tech)

On this page

- [Prometheus Metrics](https://supabase.com/blog/postgrest-12-2#prometheus-metrics)
- [Hoisted Function Settings](https://supabase.com/blog/postgrest-12-2#hoisted-function-settings)
- [Max Affected](https://supabase.com/blog/postgrest-12-2#max-affected)
- [**Try it out**](https://supabase.com/blog/postgrest-12-2#try-it-out)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12-2&text=PostgREST%2012.2%3A%20Prometheus%20metrics)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12-2&text=PostgREST%2012.2%3A%20Prometheus%20metrics)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-12-2&t=PostgREST%2012.2%3A%20Prometheus%20metrics)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)