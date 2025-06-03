---
url: "https://supabase.com/blog/pg-graphql-postgres-functions"
title: "pg_graphql: Postgres functions now supported"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# pg\_graphql: Postgres functions now supported

12 Dec 2023

•

7 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![pg_graphql: Postgres functions now supported](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flwx-pg-graphql%2Fpg-graphql-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase GraphQL (pg\_graphql) 1.4+ supports the most requested feature: Postgres functions a.k.a. User Defined Functions (UDFs). This addition marks a significant improvement in GraphQL flexibility at Supabase, both as a novel approach to defining entry points into the Graph and as an escape hatch for users to implement custom/complex operations.

As with all entities in Supabase GraphQL, UDFs support is based on automatically reflecting parts of the SQL schema. The feature allow for the execution of custom SQL logic within GraphQL queries to help support complex, user defined, server-side operations with a simple GraphQL interface.

## Minimal Example [\#](https://supabase.com/blog/pg-graphql-postgres-functions\#minimal-example)

Consider a function **`addNums`** for a basic arithmetic operation:

`
create function "addNums"(a int, b int default 1)
returns int
immutable
language sql
as $$
	select a + b;
$$;
`

when reflected in the GraphQL schema, the function is exposed as:

`
type Query {
addNums(a: Int!, b: Int): Int
}
`

To use this entry point, you could run:

`
query {
addNums(a: 2, b: 3)
}
`

which returns the JSON payload:

`
{
"data": {
    "addNums": 5
}
}
`

Supabase GraphQL does its best to reflect a coherent GraphQL API from all the information known to the SQL layer. For example, the argument `a` is non-null because it doesn't have a default value while `b` can be omitted since it does have a default. We also detected that this UDF can be displayed in the `Query` type rather than the `Mutation` type because the function was declared as `immutable`, which means it can not edit the database. Of the other [function volatility categories](https://www.postgresql.org/docs/current/xfunc-volatility.html), `stable` similarly translates into a `Query` field while `volatile` (the default) becomes a `Mutation` field.

### Returning Records [\#](https://supabase.com/blog/pg-graphql-postgres-functions\#returning-records)

In a more realistic example, we might want to return a set of an existing object type like `Account`. For example, lets say we want to search for accounts based on their email address domains matching a string:

`
create table "Account"(
id serial primary key,
email varchar(255) not null
);
insert into "Account"(email)
values
('a@foo.com'),
('b@bar.com'),
('c@foo.com');
create function "accountsByEmailDomain"("domainToSearch" text)
returns setof "Account"
stable
language sql
as $$
	select
		id, email
	from
		"Account"
	where
		email ilike ('%@' || "domainToSearch");
$$;
`

Since our function is `stable`, it continues to be a field on the `Query` type. Notice that since we're returning a collection of `Account` we automatically get support for [Relay style pagination](https://relay.dev/graphql/connections.htm) on the response including `first`, `last`, `before`, `after` as well as filtering and sorting.

``
type Query {
accountsByEmailDomain(
    domainToSearch: String!
    """
    Query the first `n` records in the collection
    """
    first: Int
    """
    Query the last `n` records in the collection
    """
    last: Int
    """
    Query values in the collection before the provided cursor
    """
    before: Cursor
    """
    Query values in the collection after the provided cursor
    """
    after: Cursor
    """
    Filters to apply to the results set when querying from the collection
    """
    filter: AccountFilter
    """
    Sort order to apply to the collection
    """
    orderBy: [AccountOrderBy!]
): AccountConnection
}
``

To complete the example, here's a call to our user defined function:

`
query {
accountsByEmailDomain(domainToSearch: "foo.com", first: 2) {
    edges {
      node {
        id
        email
      }
    }
}
}
`

and the response:

`
{
"data": {
    "accountsByEmail": {
      "edges": [\
        {\
          "node": {\
            "id": 1,\
            "email": "a@foo.com"\
          }\
        },\
          "node": {\
            "id": 3,\
            "email": "c@foo.com"\
          }\
      ]
    }
}
}
`

While not shown here, any relationships defined by foreign keys on the response type `Account` are fully functional so our UDF result is completely connected to the existing Graph.

It’s worth mentioning that we could have supported this query using the default `accountCollection` field that `pg_graphql` exposes on the `Query` type using an `ilike` filter so the example is only for illustrative purposes.

i.e.:

`
query {
accountCollection(filter: { email: { ilike: "%foo.com" } }, first: 2) {
    edges {
      node {
        id
        email
      }
    }
}
}
`

would give the same result as our UDF.

### Limitations [\#](https://supabase.com/blog/pg-graphql-postgres-functions\#limitations)

The API surface area of SQL functions is surprisingly large. In an effort to bring this feature out sooner, some lesser-used parts have not been implemented yet. Currently functions using the following features are excluded from the GraphQL API:

- Overloaded functions
- Functions with a nameless argument
- Functions returning void
- Variadic functions
- Functions that accept a table/views's tuple type as an argument
- Functions that accept an array type

We look forward to implementing support for many of these features in coming releases.

## Takeaways [\#](https://supabase.com/blog/pg-graphql-postgres-functions\#takeaways)

If you're an existing Supabase user, but new to GraphQL, head over to [GraphiQL built right into Supabase Studio](https://supabase.com/dashboard/project/_/api/graphiql) for your project to interactively explore your projects through the GraphQL API. User defined function support is new in pg\_graphql 1.4+. You can check your project's GraphQL version with:

`
select *
from pg_available_extensions
where name = 'pg_graphql';
`

To upgrade, check out [our upgrade guide](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects).

For new Supabase users, [creating a new project](http://database.new/) will get you the latest version of Supabase GraphQL with UDF support.

If you're not ready to start a new project but want to learn more about `pg_graphql`/Supabase GraphQL, our [API docs](https://supabase.github.io/pg_graphql/api/) are a great place to learn about how your SQL schema is transformed into a GraphQL API.

[Launch Week![Supabase Launch Week X icon](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Flwx%2Flogos%2Flwx_logo.svg&w=32&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/launch-week)

11-15 Dec

Main Stage

[Day 1 -Supabase Studio: introducing an **AI Assistant**, **Postgres roles**, and **user impersonation**](https://supabase.com/blog/studio-introducing-assistant)

[Day 2 -Edge Functions: **Node** and native **npm** compatibility](https://supabase.com/blog/edge-functions-node-npm)

[Day 3 -Introducing Supabase **Branching**, a Postgres database for every pull request](https://supabase.com/blog/supabase-branching)

[Day 4 -Supabase Auth: **Identity Linking**, **Session Control**, **Password Protection** and **Hooks**](https://supabase.com/blog/supabase-auth-identity-linking-hooks)

[Day 5 -Introducing **Read Replicas** for low latency](https://supabase.com/blog/introducing-read-replicas)

Build Stage

[01 -Supabase Album](https://supabase.productions/)

[02 -Postgres Language Server](https://supabase.com/blog/postgres-language-server-implementing-parser)

[03 -Design at Supabase](https://supabase.com/blog/how-design-works-at-supabase)

[04 -Supabase Grafana](https://github.com/supabase/supabase-grafana)

[05 -pg\_graphql: Postgres functions](https://supabase.com/blog/pg-graphql-postgres-functions)

[06 -PostgREST 12](https://supabase.com/blog/postgrest-12)

[07 -Supavisor 1.0](https://supabase.com/blog/supavisor-postgres-connection-pooler)

[08 -Supabase Wrappers v0.2](https://supabase.com/blog/supabase-wrappers-v02)

[09 -Supabase Libraries V2](https://supabase.com/blog/client-libraries-v2)

[10 -Supabase x Fly.io](https://supabase.com/blog/postgres-on-fly-by-supabase)

[11 -Top 10 Launches of LWX](https://supabase.com/blog/launch-week-x-best-launches)

[Supabase Launch Week X Hackathon](https://supabase.com/blog/supabase-hackathon-lwx)

[Supabase Launch Week X Community Meetups](https://supabase.com/blog/community-meetups-lwx)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-postgres-functions&text=pg_graphql%3A%20Postgres%20functions%20now%20supported)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-postgres-functions&text=pg_graphql%3A%20Postgres%20functions%20now%20supported)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-postgres-functions&t=pg_graphql%3A%20Postgres%20functions%20now%20supported)

[Last post\\
\\
**Edge Functions: Node and native npm compatibility** \\
\\
12 December 2023](https://supabase.com/blog/edge-functions-node-npm)

[Next post\\
\\
**Supabase Studio: AI Assistant and User Impersonation** \\
\\
11 December 2023](https://supabase.com/blog/studio-introducing-assistant)

[launch-week](https://supabase.com/blog/tags/launch-week) [pg-graphql](https://supabase.com/blog/tags/pg-graphql) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Minimal Example](https://supabase.com/blog/pg-graphql-postgres-functions#minimal-example)
  - [Returning Records](https://supabase.com/blog/pg-graphql-postgres-functions#returning-records)
  - [Limitations](https://supabase.com/blog/pg-graphql-postgres-functions#limitations)
- [Takeaways](https://supabase.com/blog/pg-graphql-postgres-functions#takeaways)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-postgres-functions&text=pg_graphql%3A%20Postgres%20functions%20now%20supported)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-postgres-functions&text=pg_graphql%3A%20Postgres%20functions%20now%20supported)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql-postgres-functions&t=pg_graphql%3A%20Postgres%20functions%20now%20supported)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)