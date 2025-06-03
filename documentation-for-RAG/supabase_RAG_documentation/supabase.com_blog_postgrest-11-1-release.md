---
url: "https://supabase.com/blog/postgrest-11-1-release"
title: "What is new in PostgREST v11.1?"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# What is new in PostgREST v11.1?

12 Jul 2023

•

6 minute read

[![Steve Chavez avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsteve-chavez.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Steve ChavezEngineering & PostgREST maintainer](https://github.com/steve-chavez)

![What is new in PostgREST v11.1?](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-community%2Fpostgrest.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

PostgREST 11.1 is now available on the Supabase platform. Besides the [pre-release](https://supabase.com/blog/postgrest-11-prerelease) features, we’ve added configuration and querying improvements. Here is what's new:

## Impersonated Role Settings [\#](https://supabase.com/blog/postgrest-11-1-release\#impersonated-role-settings)

Every role that passes [PostgREST JWT Authentication](https://postgrest.org/en/stable/references/auth.html#jwt-based-user-impersonation) is an _impersonated role_. On the Supabase platform, these are the `anon`, `authenticated` and `service_role` roles.

These roles can now have settings applied with a regular `ALTER ROLE .. SET`. This is useful, for example, to prevent web users from running expensive queries.

Let’s try it by setting a statement timeout and cost limit.

### Statement timeout [\#](https://supabase.com/blog/postgrest-11-1-release\#statement-timeout)

`statement_timeout` aborts any statement that takes more than the specified amount of time. Let’s set it for the `anon`, `authenticated` and `service_role` roles:

`
-- anonymous users can run queries that take 100 milliseconds max
alter
role anon
set
statement_timeout = '100ms';
-- authenticated users can run queries that take 5 seconds max
alter
role authenticated
set
statement_timeout = '5s';
-- backend-only users can run queries that take 15 seconds max
alter
role service_role
set
statement_timeout = '15s';
`

You need to reload PostgREST config cache to apply these changes.

`
NOTIFY pgrst,
'reload config';
`

Now, suppose you do an expensive query with the `anon` role. Like filtering on a big table's unindexed column (this will cause a full table scan):

`
const { data, error } = await supabase.from('big_table').select().eq('unindexed_column', 'value')
`

Then, after 5 seconds, the request will be aborted with the response:

`
{
"hint": null,
"details": null,
"code": "57014",
"message": "canceling statement due to statement timeout"
}
`

Which is what we wanted. Note that there's already a global `statement_timeout` set but you can be more fine-grained with this feature. See [timeouts](https://supabase.com/docs/guides/database/timeouts) for more details.

### Statement Cost Limit [\#](https://supabase.com/blog/postgrest-11-1-release\#statement-cost-limit)

With a statement timeout, expensive queries will still get executed for a length of time. They'll consume resources until they’re terminated.

The [pg\_plan\_filter](https://github.com/pgexperts/pg_plan_filter) extension (available on the Supabase platform), brings a statement cost limit. This abort queries at the planning phase, before they get executed.

You can use it like:

`
-- anonymous users can only run cheap queries
ALTER
USER anon
SET
plan_filter.statement_cost_limit = 10000;
-- authenticated users can run more expensive queries
ALTER
USER authenticated
SET
plan_filter.statement_cost_limit = 1e6;
-- backend-only users can run any query
ALTER
USER service_role
SET
plan_filter.statement_cost_limit = 0;
NOTIFY pgrst,
'reload config';
-- reload postgREST config cache to apply changes
`

Let’s repeat the previous expensive query with the `anon` role.

`
const { data, error } = await supabase.from('big_table').select().eq('unindexed_column', 'value')
`

Then, immediately, the request will be aborted and the response will be:

`
{
"hint": null,
"details": null,
"code": "54001",
"message": "plan cost limit exceeded"
}
`

Note that tuning is required to get the cost limit right. You should use the `plan_filter.statement_cost_limit` with care as it can invalidate legitimate queries.

## Configurable Transaction Isolation Level [\#](https://supabase.com/blog/postgrest-11-1-release\#configurable-transaction-isolation-level)

By default, all queries run in a transaction with the default _read committed_ isolation level.

You can now modify this with the `default_transaction_isolation` setting.

If you want a function to run with _repeatable read_ isolation level:

`
create function hello()
returns text as $$
select 'hello';
$$ language sql
set default_transaction_isolation = 'repeatable read';
`

Or if you want an impersonated role to run its queries with a _serializable_ isolation level:

`
alter
role service_role
set
default_transaction_isolation = 'serializable';
NOTIFY pgrst,
'reload config';
-- reload postgREST config cache
`

Note that the default _read committed_ is good enough for almost all use cases. Higher isolation levels incur in overhead as they use more sophisticated locking. They're only needed in special cases.

## Bulk insert JSON with default values [\#](https://supabase.com/blog/postgrest-11-1-release\#bulk-insert-json-with-default-values)

A long wanted feature was bulk inserting JSON while considering columns' default values.

Having the following sample table.

`
create table
foo (
    id bigint generated by default as identity primary key,
    bar text,
    baz int default 100
);
`

You can now do it like this:

`
const { error } = await supabase
.from('foo')
.insert([\
	  { "bar": "val1"\
	  }\
	, { "bar": "val2"\
	  , "baz": 15\
	  }\
	], defaultToNull: false)
.select()
`

And the response will be:

`
[\
{ "id": 1, "bar": "val1", "baz": 100 },\
{ "id": 2, "bar": "val2", "baz": 15 }\
]
`

As you can see, `id` and `baz` took their default values.

## ANY/ALL filter modifiers [\#](https://supabase.com/blog/postgrest-11-1-release\#anyall-filter-modifiers)

As a shortcut to `OR` filters, you can now use `any` modifiers on various filters. Take the `like` filter as an example:

`
const res = await postgrest
.from('users')
.select()
.likeAnyOf('username', ['%supa%', '%kiwi%'])
`

This is equivalent to the following in SQL.

`
select *
from users
where username like ANY('{%supa%,%kiwi%}');
`

`any` modifiers are available for the `eq,like,ilike,gt,gte,lt,lte,match,imatch` filters.

For completeness, the `all` modifier is also included.

## Minimal Breaking Changes from v10 [\#](https://supabase.com/blog/postgrest-11-1-release\#minimal-breaking-changes-from-v10)

If you only use PostgREST through Supabase client libraries (like [`supabase-js`](https://supabase.com/docs/reference/javascript/introduction)) then it's safe to upgrade to v11. If you use PostgREST with other HTTP clients (like `curl`), consider the breaking changes for this version:

- The `Range` header is now only considered on GET requests and is ignored for any other method. Previously PostgREST responded with an error but [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-range) dictates that we should ignore the `Range` header instead.
- RPC requests no longer consider the `Prefer: params=multiple-objects` header. This header was already deprecated on [v10.1.0](https://github.com/PostgREST/postgrest/releases/tag/v10.1.0).

By making use of [Logflare](https://logflare.app/), we detected that out of 20 thousands of projects:

- Only 7 projects used `Range` for HTTP methods other than GET. In these cases all responses were errors so in fact this breaking change is a fix for those requests.
- None were using `Prefer: params=multiple-objects`.

So overall the breaking changes are minimal.

## Closing up [\#](https://supabase.com/blog/postgrest-11-1-release\#closing-up)

There you have it, now you can make your API more secure with role settings and use higher isolation levels without resorting to direct PostgreSQL connections.

PostgREST v11.1 is available for all Supabase projects created after 5 July 2023. Existing projects can upgrade by doing a pause/unpause.

## More Postgres resources [\#](https://supabase.com/blog/postgrest-11-1-release\#more-postgres-resources)

- [Storing OpenAI embeddings in Postgres with pgvector](https://supabase.com/blog/openai-embeddings-postgres-vector)
- [Choosing a Postgres Primary Key](https://supabase.com/blog/choosing-a-postgres-primary-key)
- [SQL or NoSQL? Why not use both (with PostgreSQL)?](https://supabase.com/blog/sql-or-nosql-both-with-postgresql)
- [pg\_jsonschema: JSON Schema support for Postgres](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation)
- [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-1-release&text=What%20is%20new%20in%20PostgREST%20v11.1%3F)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-1-release&text=What%20is%20new%20in%20PostgREST%20v11.1%3F)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-1-release&t=What%20is%20new%20in%20PostgREST%20v11.1%3F)

[Last post\\
\\
**pgvector 0.4.0 performance** \\
\\
13 July 2023](https://supabase.com/blog/pgvector-performance)

[Next post\\
\\
**Supabase Beta June 2023** \\
\\
6 July 2023](https://supabase.com/blog/supabase-beta-update-june-2023)

[postgres](https://supabase.com/blog/tags/postgres)

On this page

- [Impersonated Role Settings](https://supabase.com/blog/postgrest-11-1-release#impersonated-role-settings)
  - [Statement timeout](https://supabase.com/blog/postgrest-11-1-release#statement-timeout)
  - [Statement Cost Limit](https://supabase.com/blog/postgrest-11-1-release#statement-cost-limit)
- [Configurable Transaction Isolation Level](https://supabase.com/blog/postgrest-11-1-release#configurable-transaction-isolation-level)
- [Bulk insert JSON with default values](https://supabase.com/blog/postgrest-11-1-release#bulk-insert-json-with-default-values)
- [ANY/ALL filter modifiers](https://supabase.com/blog/postgrest-11-1-release#anyall-filter-modifiers)
- [Minimal Breaking Changes from v10](https://supabase.com/blog/postgrest-11-1-release#minimal-breaking-changes-from-v10)
- [Closing up](https://supabase.com/blog/postgrest-11-1-release#closing-up)
- [More Postgres resources](https://supabase.com/blog/postgrest-11-1-release#more-postgres-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-1-release&text=What%20is%20new%20in%20PostgREST%20v11.1%3F)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-1-release&text=What%20is%20new%20in%20PostgREST%20v11.1%3F)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgrest-11-1-release&t=What%20is%20new%20in%20PostgREST%20v11.1%3F)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)