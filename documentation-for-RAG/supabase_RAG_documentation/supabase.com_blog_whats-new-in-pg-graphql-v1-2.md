---
url: "https://supabase.com/blog/whats-new-in-pg-graphql-v1-2"
title: "What's New in pg_graphql v1.2"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# What's New in pg\_graphql v1.2

21 Apr 2023

•

6 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![What's New in pg_graphql v1.2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-6%2Fpggraphql%2Fog-pg-graphql.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

It's been 4 months since the [1.0.0 release of pg\_graphql](https://supabase.com/blog/pg-graphql-v1).
Since then, we’ve pushed several features to improve the APIs that `pg_graphql` produces.

In this article, we’ll walk through those features and show examples of each.

📢 These features are only available on projects with Postgres version `15.1.0.63` or higher. For help with upgrading, please review the [migrating and upgrading projects guide](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects).

### View Support [\#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2\#view-support)

Prior to `v1.1`, `pg_graphql` would only reflect standard tables. Since then, views, materialized views, and foreign tables are now also reflected in the GraphQL schema.

For example:

`
create view "ProjectOwner" as
select
    acc.id,
    acc.name
from
    account as acc
    join role as r on r.id = acc.role_id
where acc.role = 'project_owner';
`

Since all entities exposed by `pg_graphql` require primary keys, we must define that constraint for the view. We do that using a comment directive:

`
comment on view "ProjectOwner"
is '@graphql({"primary_key_columns": ["id"]})';
`

Which yields the GraphQL type:

`
type ProjectOwner implements Node {
nodeId: ID!
id: UUID!
name: String
}
`

With associated `Edge` and `Connection` types. That enables querying via:

`
{
projectOwnerCollection(first: 2) {
    edges {
      node {
        nodeId
        name
      }
    }
}
}
`

Additionally, simple views automatically support mutation events like inserts and updates. You might use these to migrate underlying tables while maintaining backwards compatibility with previous API versions.

## Filtering [\#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2\#filtering)

Filtering in SQL is endlessly flexible. We’ve taken two incremental steps to bring more of that flexibility to the GraphQL interface.

### `is null` and `is not null` [\#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2\#is-null-and-is-not-null)

Handling `null` values can be tricky in both SQL and GraphQL. However, there are similarities we can take advantage of.
In `pg_graphql`, every scalar data type has its own filter type, such as `IntFilter` and `StringFilter`.
Each of these filter types now includes an `is` argument, which allows you to filter based on whether a value is null or not null.
You can do this by using `{is: NULL}` for `null` values and `{is: NOT_NULL}` for non- `null` values.

`
enum FilterIs {
    NULL
    NOT_NULL
}
type IntFilter {
    ...
    is: FilterIs
}
`

For example:

`
{
blogCollection(filter: { name: {is: NULL}}) {
    ...
}
}
`

to return all `blog` s where the `name` is `null`.

### **`like`**, **`ilike`**, and **`startsWith`** [\#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2\#like-ilike-and-startswith)

Text filtering options in `pg_graphql` have historically been restricted to equality checks. The hesitation was due to concerns about exposing a default filter that is difficult to index. The combination of [citext](https://www.postgresql.org/docs/current/citext.html) and [PGroonga available on the platform](https://supabase.com/docs/guides/database/extensions/pgroonga) solves those scalability risks and enabled us to expand the `StringFilter` with options for `like` `ilike` and `startsWith`.

`
input StringFilter {
eq: String
...
startsWith: String
like: String
ilike: String
}
`

Note that `startsWith` filters should be preferred where appropriate because they can leverage simple B-Tree indexes to improve performance.

`
{
generalLedgerCollection(filter: { identifierCode: { startsWith: "BX1:" } }) {
    edges {
      node {
        nodeId
        identifierCode
        amount
      }
    }
}
}
`

### GraphQL directives `@skip` and `@include` [\#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2\#graphql-directives-skip-and-include)

The GraphQL spec has evolved over time. Although the spec is clear, it is common for GraphQL servers to selectively omit some chunks of functionality. For example, some frameworks intentionally do not expose an introspection schema as a form of security through obscurity.

`pg_graphql` aims to be unopinionated and adhere exactly to the spec. The `@skip` and `@include` directives are part of the [GraphQL core specification](https://spec.graphql.org/October2021/#sec--skip) and are now functional.

The **`@skip`** directive in GraphQL is used to conditionally skip a field or fragment during query execution based on a Boolean variable. It can be used to make the query more efficient by reducing the amount of data retrieved from the server.

The **`@include`** directive is the mirror of **`@skip`** where a field or fragment is conditionally included depending on the value of a Boolean variable.

Here's an example of how the **`@skip`** directive can be used in a GraphQL query:

`
query getBooks($includeDetails: Boolean!) {
booksCollection {
    edges {
      node {
        id
        title
        description @skip(if: $includeDetails)
      }
    }
}
}
`

### User Defined Descriptions [\#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2\#user-defined-descriptions)

Users can now use the [comment directive system to assign descriptions](https://supabase.github.io/pg_graphql/configuration/#description) to tables, views and columns.

`
create table public.book(
    id int primary key,
    title text not null
);
comment on table public.book
is e'@graphql({"description": "a library book"})';
comment on column public.book.title
is e'@graphql({"description": "the title of the book"})';
`

GraphQL IDEs, such as GraphiQL render those descriptions, allowing developers to provide clearer API documentation.

![description comment directive](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-04-19-pg_graphql-v1_2%2Fdescription_directive.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Roadmap [\#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2\#roadmap)

The headline features we aim to launch in coming releases of `pg_graphql` include:

1. Support for user-defined functions: [GitHub issue](https://github.com/supabase/pg_graphql/issues/222)
2. Support for nested inserts: [GitHub issue](https://github.com/supabase/pg_graphql/issues/294)
3. An alternative approach to computed relationships based on SQL functions returning **`SET OF`** rather than comment directives (compatible with PostgREST)

## More pg\_graphql [\#](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2\#more-pg_graphql)

- [Introducing pg\_graphql: A GraphQL extension for PostgreSQL](https://supabase.com/blog/pg-graphql)
- [GraphQL is now available in Supabase](https://supabase.com/blog/graphql-now-available)
- [pg\_graphql v1.0](https://supabase.com/blog/pg-graphql-v1)
- [pg\_graphql: Postgres functions now supported](https://supabase.com/blog/pg-graphql-postgres-functions)

### More Launch Week 7

[Designing with AI\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fai-images%2F00-ai-images-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/designing-with-ai-midjourney)

[Supavisor\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fsupavisor%2Fsupavisor-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://github.com/supabase/supavisor)

[Open Source Logging\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday1%2Fself-hosted-logs-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-logs-self-hosted)

[Self-hosted Deno Edge Functions\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday2%2Fself-hosted-edge-functions-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)

[Storage v3: Resumable Uploads with support for 50GB files\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday3%2Fstorage-v3-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/storage-v3-resumable-uploads)

[Supabase Auth: SSO, Mobile, and Server-side support\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday4%2Fsso-support-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-auth-sso-pkce)

[Community Highlight\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fcommunity%2Fcommunity-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/launch-week-7-community-highlights)

[Studio Updates\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fstudio%2Fstudio-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-studio-2.0)

[dbdev\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2Fdbdev-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/dbdev)

[Postgres TLE\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2FpgTLE-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/pg-tle)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&text=What%27s%20New%20in%20pg_graphql%20v1.2)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&text=What%27s%20New%20in%20pg_graphql%20v1.2)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&t=What%27s%20New%20in%20pg_graphql%20v1.2)

[Last post\\
\\
**Launch Week 7 Hackathon Winners** \\
\\
24 April 2023](https://supabase.com/blog/launch-week-7-hackathon-winners)

[Next post\\
\\
**dbdev: PostgreSQL Package Manager** \\
\\
14 April 2023](https://supabase.com/blog/dbdev)

[postgres](https://supabase.com/blog/tags/postgres) [graphql](https://supabase.com/blog/tags/graphql) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [View Support](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#view-support)

- [Filtering](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#filtering)
  - [`is null` and `is not null`](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#is-null-and-is-not-null)
  - [**`like`**, **`ilike`**, and **`startsWith`**](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#like-ilike-and-startswith)
  - [GraphQL directives `@skip` and `@include`](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#graphql-directives-skip-and-include)
  - [User Defined Descriptions](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#user-defined-descriptions)
- [Roadmap](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#roadmap)
- [More pg\_graphql](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2#more-pg_graphql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&text=What%27s%20New%20in%20pg_graphql%20v1.2)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&text=What%27s%20New%20in%20pg_graphql%20v1.2)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fwhats-new-in-pg-graphql-v1-2&t=What%27s%20New%20in%20pg_graphql%20v1.2)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![description comment directive](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-04-19-pg_graphql-v1_2%2Fdescription_directive.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)