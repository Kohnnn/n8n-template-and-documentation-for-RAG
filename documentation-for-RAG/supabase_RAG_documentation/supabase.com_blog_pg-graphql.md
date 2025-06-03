---
url: "https://supabase.com/blog/pg-graphql"
title: "pg_graphql: A GraphQL extension for PostgreSQL"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# pg\_graphql: A GraphQL extension for PostgreSQL

03 Dec 2021

•

7 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![pg_graphql: A GraphQL extension for PostgreSQL](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Ffive-more-things%2Fsupabase-pg-graphql-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

🆕 `pg_graphql` is now generally available and has undergone significant enhancements since this announcement. Here is what is new:

- [pg\_graphql v1.0](https://supabase.com/blog/pg-graphql-v1)
- [New Features in pg\_graphql v1.2](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2)

Today we're open sourcing [`pg_graphql`](https://github.com/supabase/pg_graphql), a native PostgreSQL extension adding GraphQL support. The extension keeps schema generation, query parsing, and resolvers all neatly contained on your database server requiring no external services.

`pg_graphql` inspects an existing PostgreSQL schema and reflects a GraphQL schema with resolvers that are:

- performant
- always up-to-date
- compliant with best practices
- serverless
- open source

Interested? You're [3 commands away](https://supabase.github.io/pg_graphql/quickstart/) from a live [GraphiQL](https://graphql-dotnet.github.io/docs/getting-started/graphiql/) demo.

## Motivation [\#](https://supabase.com/blog/pg-graphql\#motivation)

The Supabase stack is centered around PostgreSQL as the single source of truth. All data, configuration, and security are housed in the database so any GraphQL solution needed to be equivalently SQL-centric.

With that in mind, we took a look at the landscape and considered two excellent technologies, [Graphile](https://www.graphile.org/postgraphile/), and [Hasura](https://hasura.io/).

| Requirements | Graphile | Hasura |
| --- | --- | --- |
| Open Source | ✅ | ✅ |
| Reflected GraphQL Schema | ✅ | ✅ |
| Reflected Resolvers | ✅ | ✅ |
| Always up-to-date | ✅ | ✅ |
| Performant | ✅ | ✅ |

We found both options to be largely viable for the core feature set.

Which left us with one final hang-up: we host free-tier projects on VMs with 1 GB of memory. After tallying the resources reserved for PostgreSQL, PostgREST, Kong, GoTrue, and a handful of smaller services, we were left with a total memory budget of ... 0 MB 😬. Unsurprisingly, our pathological memory target disqualified any option that required launching another process in those VMs.

For that reason, we decided to invest in a lightweight alternative that runs in the database, and can be exposed over HTTP using the existing [PostgREST](https://supabase.com/docs/guides/database/api) deployments' [RPC functionality.](https://postgrest.org/en/v8.0/api.html#stored-procedures)

By our most conservative estimate, that reduces the platform's memory requirements by 525 TB/hours every month, saving 💰 and 🌳.

## Design [\#](https://supabase.com/blog/pg-graphql\#design)

As a native PostgreSQL extension, `pg_graphl` is written in a combination of C and SQL. Each GraphQL query is parsed, validated, and transpiled to SQL, all within the database.

Each GraphQL request is resolved by a single SQL statement. That SQL statement aggregates requested data as a JSON document to return to the caller. This approach results in blazing fast response times, avoids the [N+1 query problem](https://medium.com/the-marcy-lab-school/what-is-the-n-1-problem-in-graphql-dd4921cb3c1a), and hits the theoretical minimum achievable network IO overhead of any GraphQL to SQL resolver. No special permissions are required for the PostgreSQL role executing queries, so `pg_graphql` is fully compatible with your existing [row level security policies](https://supabase.com/docs/guides/auth/row-level-security).

Embedding the GraphQL server directly in the database allows us to leverage PostgreSQL's built-in solutions for common challenges:

Caching → `PREPARE STATEMENT`

Errors → `RAISE EXCEPTION`

Bad Data → `ROLLBACK`

Authorization → `CREATE POLICY`

Similarly, `pg_graphql` benefits from PostgreSQL's strong [ACID](https://database.guide/what-is-acid-in-databases/) guarantees and can expose them through its API.

Ever wanted to execute multiple operations in a single transaction? Each request is managed in a single transaction so with a multi-operation GraphQL request and `pg_graphql`, that behavior falls out for free!

### Schema Reflection [\#](https://supabase.com/blog/pg-graphql\#schema-reflection)

As a limited example of how the reflection engine works, here's how it converts a single table into a full GraphQL schema.

hideCopy

`
# schema.sql
create table account (
id serial primary key,
email varchar(255) not null,
created_at timestamp not null,
updated_at timestamp not null
);
`

Translates into

hideCopy

`
# schema.graphql
scalar Cursor
scalar DateTime
scalar JSON
scalar UUID
scalar BigInt
type PageInfo {
hasNextPage: Boolean!
hasPreviousPage: Boolean!
startCursor: String!
endCursor: String!
}
type Query {
account(nodeId: ID!): Account
allAccounts(after: Cursor, before: Cursor, first: Int, last: Int): AccountConnection
}
type Account {
nodeId: ID!
id: String!
email: String!
createdAt: DateTime!
updatedAt: DateTime!
}
type AccountEdge {
cursor: String!
node: Account
}
type AccountConnection {
totalCount: Int!
pageInfo: PageInfo!
edges: [AccountEdge]
}
`

Where `Query` type's `account` field selects a single account by its globally unique `ID` and `allAccounts` enables pagination via the [relay connections specification](https://relay.dev/graphql/connections.htm). Under the SQL hood, iterating through pages is handled using keyset pagination giving consistent retrieval times on every page.

For a more complete examples with relationships, enums, and more exotic types check out the [API doc](https://supabase.github.io/pg_graphql/api).

### API [\#](https://supabase.com/blog/pg-graphql\#api)

`pg_graphql`'s public API is a single SQL function that returns JSON.

hideCopy

`
gql.resolve(
    stmt text, -- the graphql query/mutation
    variables jsonb default '{}'::jsonb, -- key value pairs
)
    returns jsonb
`

For example, a GraphQL query selecting the `id` field for a collection of type `Book` would look like this:

hideCopy

`
gqldb= select gql.resolve($$
query {
allBooks {
    edges {
      node {
        id
      }
    }
}
}
$$);
             resolve
----------------------------------------------------------------------
{"data": {"allBooks": {"edges": [{"node": {"id": 1}}]}}, "errors": []}
`

We're opting to expose the function over HTTP through PostgREST but you could also connect to the PostgreSQL database and call the function directly from your server code in any programming language.

## Performance [\#](https://supabase.com/blog/pg-graphql\#performance)

When it comes to APIs, performance counts. Here are some figures from [Apache Bench](https://www.tutorialspoint.com/apache_bench/apache_bench_quick_guide.htm) showing 2,205 requests/second on a 4 core machine with 16 GB of memory.

hideCopy

`
Concurrency Level:      8
Time taken for tests:   3.628 seconds
Complete requests:      8000
Failed requests:        0
Total transferred:      1768000 bytes
Total body sent:        1928000
HTML transferred:       368000 bytes
Requests per second:    2205.21 [#/sec] (mean)
Time per request:       3.628 [ms] (mean)
Time per request:       0.453 [ms] (mean, across all concurrent requests)
Transfer rate:          475.93 [Kbytes/sec] received
`

Full steps to reproduce this output are available in [the docs](https://supabase.github.io/pg_graphql).

## Open Source [\#](https://supabase.com/blog/pg-graphql\#open-source)

`pg_graphql` is [open source software](https://github.com/supabase/pg_graphql/). As always, Issues and PRs are welcome.

[Try `pg_graphql`](https://supabase.github.io/pg_graphql/quickstart/) today to see a live [GraphiQL](https://graphql-dotnet.github.io/docs/getting-started/graphiql/) demo.

## More pg\_graphql [\#](https://supabase.com/blog/pg-graphql\#more-pg_graphql)

- [pg\_graphql v1.0](https://supabase.com/blog/pg-graphql-v1)
- [New Features in pg\_graphql v1.2](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2)
- [pg\_graphql: Postgres functions now supported](https://supabase.com/blog/pg-graphql-postgres-functions)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&text=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&text=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&t=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)

[Last post\\
\\
**Five more things** \\
\\
3 December 2021](https://supabase.com/blog/launch-week-three-friday-five-more-things)

[Next post\\
\\
**Kicking off the Holiday Hackdays** \\
\\
3 December 2021](https://supabase.com/blog/supabase-holiday-hackdays-hackathon)

[launch-week](https://supabase.com/blog/tags/launch-week) [community](https://supabase.com/blog/tags/community) [graphql](https://supabase.com/blog/tags/graphql)

On this page

- [Motivation](https://supabase.com/blog/pg-graphql#motivation)
- [Design](https://supabase.com/blog/pg-graphql#design)
  - [Schema Reflection](https://supabase.com/blog/pg-graphql#schema-reflection)
  - [API](https://supabase.com/blog/pg-graphql#api)
- [Performance](https://supabase.com/blog/pg-graphql#performance)
- [Open Source](https://supabase.com/blog/pg-graphql#open-source)
- [More pg\_graphql](https://supabase.com/blog/pg-graphql#more-pg_graphql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&text=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&text=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-graphql&t=pg_graphql%3A%20A%20GraphQL%20extension%20for%20PostgreSQL)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)