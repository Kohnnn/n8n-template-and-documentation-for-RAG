---
url: "https://supabase.com/blog/graphql-now-available"
title: "GraphQL is now available in Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# GraphQL is now available in Supabase

29 Mar 2022

•

10 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

[![David Thyresson avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdthyresson.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
David ThyressonEngineering](https://github.com/dthyresson)

![GraphQL is now available in Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Ftuesday-graphql%2Fgraphql-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

🆕 `pg_graphql` has undergone significant enhancements since this announcement. Here is what is new:

- [pg\_graphql v1.0](https://supabase.com/blog/pg-graphql-v1)
- [New Features in pg\_graphql v1.2](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2)

GraphQL support is now in general availability on the Supabase platform via our [open source](https://github.com/supabase/pg_graphql/) PostgreSQL extension, [`pg_graphql`](https://supabase.github.io/pg_graphql/).

`pg_graphql` enables you to query existing PostgreSQL databases using GraphQL, either from within SQL or over HTTP:

From SQL:

`
select graphql.resolve($$
    {
      accountCollection(first: 1) {
        edges {
          node {
            id
            firstName
            address {
              countryCode
            }
          }
        }
      }
    }
$$);
`

or over HTTP:

`
curl -X POST https://<PROJECT_REF>.supabase.co/graphql/v1 \
    -H 'apiKey: <API_KEY>'\
    -H 'Content-Type: application/json' \
    --data-raw '
    {
      "query":"{ accountCollection(first: 3) { edges { node { id } } } }"
    }'
`

## Schema Reflection [\#](https://supabase.com/blog/graphql-now-available\#schema-reflection)

GraphQL types and fields are reflected from the SQL schema:

- Tables become types
- Columns become fields
- Foreign keys become relations

For example:

`
create table "Account" (
"id" serial primary key,
"email" varchar(255) not null,
"createdAt" timestamp not null,
"updatedAt" timestamp not null
);
`

Translates to the GraphQL base type

`
type Account {
id: Int!
email: String!
createdAt: DateTime!
updatedAt: DateTime!
}
`

And exposes bulk CRUD operations on the `Query` and `Mutation` types, complete with relay style keyset pagination, filters, and ordering and (optional) name inflection.

`
type Query {
accountCollection(
    first: Int
    last: Int
    before: Cursor
    after: Cursor
    filter: AccountFilter
    orderBy: [AccountOrderBy!]
): AccountConnection
}
type Mutation {
	insertIntoAccountCollection(
		objects: [AccountInsertInput!]!
	): AccountInsertResponse
	updateAccountCollection(
    set: AccountUpdateInput!
    filter: AccountFilter
    atMost: Int! = 1
): AccountUpdateResponse!
deleteFromAccountCollection(
filter: AccountFilter
    atMost: Int! = 1
): AccountDeleteResponse!
`

For a complete example with relationships, check out the [API docs](https://supabase.github.io/pg_graphql/api/).

## Security [\#](https://supabase.com/blog/graphql-now-available\#security)

An advantage to embedding GraphQL directly in the database is that we can lean on PostgreSQL's built-in primitives for authentication and authorization.

### Authentication [\#](https://supabase.com/blog/graphql-now-available\#authentication)

The GraphQL types exposed by `pg_graphql` are filtered according to the SQL role's [INSERT/UPDATE/DELETE permissions](https://www.postgresql.org/docs/current/sql-grant.html). At Supabase, each API request is resolved in the database using the role in the request's JWT.

Anonymous users receive the `anon` role, and logged in users get the `authenticated` role. In either case, pg\_graphql resolves requests according to the SQL permissions.
The [introspection schema](https://graphql.org/learn/introspection/) is similarly filtered to limit exposed types and fields to those that the user has permission to access.
That means we can serve multiple GraphQL schemas for users of differing privilege levels from a single endpoint!

### Authorization [\#](https://supabase.com/blog/graphql-now-available\#authorization)

Another nice side effect of making PostgreSQL do the heavy lifting is that GraphQL queries respect your existing
[row level security policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) right out-of-the-box. No additional configuration required.

## Performance [\#](https://supabase.com/blog/graphql-now-available\#performance)

To squeeze the most out of limited hardware we had to make a few significant optimizations:

**GraphQL queries are always transpiled into exactly one SQL query**

The SQL queries select and aggregate requested data into the shape of the GraphQL JSON response.
In addition to solving the [N+1 query problem](https://medium.com/the-marcy-lab-school/what-is-the-n-1-problem-in-graphql-dd4921cb3c1a), a common issue with GraphQL resolvers,
GraphQL queries requiring multiple joins typically produce significantly less IO due to reduced data duplication.

For example, when selecting all comments for a blog post:

`
select
blog_posts.title,
comments.body as comment_body
from
blog_posts
join comments on blog_posts.id = comments.blog_post_id;
`

a SQL response would duplicate all data from the `blog_posts` table (title).

`
| title      | comment_body                   |
| ---------- | ------------------------------ |
| F1sRt P0$T | this guy gets it!              |
| F1sRt P0$T | you should re-write it in rust |
| F1sRt P0$T | 10% off daily vitamin http:... |
`

Compared to the equivalent GraphQL response.

`
{
	"blogPostCollection": {
    "edges": {
      "node":
        "title": "F1sRt P0$T"
        "commentCollection": {
          "edges": [\
            "node": {\
			        "body": "this guy gets it!"\
						},\
						"node": {\
			        "body": "you should re-write it in rust"\
						},\
						"node": {\
				      "body": "10% off daily vitamin http:..."\
      			}\
          ]
        }
      }
    }
}
}
`

Which has no duplication of data.

The difference in payload size is negligible in this case, but as the number of 1-to-many joins grows, data duplication in the SQL response grows geometrically.

![supameme.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Ftuesday-graphql%2Fsupameme.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

**Queries are cached as prepared statements**

After a GraphQL query is transpiled to SQL, it is added to the [prepared statement](https://www.postgresql.org/docs/current/sql-prepare.html) cache so subsequent requests with the same structure (think pagination) can skip the transpilation step.

Using prepared statements also allows PostgreSQL to skip the overhead of computing a query plan. For small, on-index, queries,
the query planning step can take several times as long as the query's execution time, so the saving is significant at scale.

**All operations are bulk**

Finally, all reflected query and mutation fields support bulk operations to nudge users towards consuming the API efficiently.
Batching similar operations reduces network round-trips and time spent in the database.

**Result**

As a result of these optimizations, the throughput of a “hello world” equivalent query on Supabase Free Plan hardware is:

- 377.4 requests/second through the API (mean)
- 656.2 queries/second through SQL (single connection, mean)

## Getting Started [\#](https://supabase.com/blog/graphql-now-available\#getting-started)

To enable GraphQL in your Supabase instance, enable `pg_graphql` from the [dashboard](https://supabase.com/dashboard/).

Or create the extension in your database

`
create extension pg_graphql;
`

And we're done!

The GraphQL endpoint is available at: `https://<project_ref>.supabase.co/graphql/v1`

## Example app: Build a HN clone with Postgres and GraphQL [\#](https://supabase.com/blog/graphql-now-available\#example-app-build-a-hn-clone-with-postgres-and-graphql)

![graph-ql-example-app.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Ftuesday-graphql%2Fgraph-ql-example-app.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We're excited to have worked with [The Guild](https://www.the-guild.dev/) to show you [how to use](https://supabase-graphql-example.vercel.app/about) `pg_graphql`
and their tools to build a [HackerNews clone](https://supabase-graphql-example.vercel.app/).

The [demo application](https://supabase-graphql-example.vercel.app/) showcases:

- **CRUD (Query + Mutation Operations).**
Data is fetched from the GraphQL layer auto-generated via `pg_graphql`.
- **Cursor Based Pagination.** `pg_graphql` generates standardized pagination types and fields as defined by the GraphQL Cursor Connections Specification.
- **Authorization / RLS.**
GraphQL requests made include Supabase authorization headers so that Row Level Security on the Postgres layer ensures that viewers can only access what they are allowed to — and authenticated users can only update what they should.
- **Code generation.**
Introspect your GraphQL schema and operations to generates the types for full backend to frontend type-safety.
- **Postgres Triggers and Functions.**
Recalculate the feed scoring each time someone votes.
- **Supabase UI.**
Use Auth widget straight out the box to handle logins and access tokens.

![graph-ql-example-app-2.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Ftuesday-graphql%2Fgraph-ql-example-app-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Now instead of using the Supabase PostgREST API to query your database ...

`
// using Supabase PostgREST
const { data, error } = await supabase
.from('profile')
.select('id, username, bio, avatarUrl, website')
`

... all data fetching and updates are done using the same GraphQL operations you know and love! 🤯

`
// using GraphQL
query ProfilesQuery {
    profileCollection {
      edges {
        node {
          id
          username
          bio
          avatarUrl
          website
      }
    }
}
}
`

🎁  Get the code on GitHub here: [github.com/supabase-community/supabase-graphql-example](https://github.com/supabase-community/supabase-graphql-example)

## Supabase + The Guild [\#](https://supabase.com/blog/graphql-now-available\#supabase--the-guild)

![graphql-supabase-guild.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Ftuesday-graphql%2Fgraphql-supabase-guild.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This is just the start of what we hope to be a close collaboration with the Guild, whose expertise of the GraphQL ecosystem will guide the development of Supabase's GraphQL features.
The Guild and Supabase share a similar approach to open source - we both favor collaboration and composability, making collaboration easy and productive.

Be sure to visit [The Guild](https://www.the-guild.dev/) and [follow them](https://twitter.com/TheGuildDev) to stay informed of the latest developments in GraphQL.

## Limitations & Roadmap [\#](https://supabase.com/blog/graphql-now-available\#limitations--roadmap)

Our first general availability release of `pg_graphql` supports:

- Full CRUD on table columns with scalar types
- Read only support for array types
- Extending types with [computed fields](https://supabase.github.io/pg_graphql/computed_fields/)
- Configuration with [SQL comments](https://supabase.github.io/pg_graphql/configuration/)

In the near term, we plan to fully support array and json/b types. Longer term, we intend to support views and custom mutations from user defined functions.

Didn't see the feature you're interested in? [Let us know](https://github.com/supabase/pg_graphql/issues)

## More pg\_graphql [\#](https://supabase.com/blog/graphql-now-available\#more-pg_graphql)

- [Introducing pg\_graphql: A GraphQL extension for PostgreSQL](https://supabase.com/blog/pg-graphql)
- [pg\_graphql v1.0](https://supabase.com/blog/pg-graphql-v1)
- [pg\_graphql v1.2](https://supabase.com/blog/whats-new-in-pg-graphql-v1-2)
- [pg\_graphql: Postgres functions now supported](https://supabase.com/blog/pg-graphql-postgres-functions)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgraphql-now-available&text=GraphQL%20is%20now%20available%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgraphql-now-available&text=GraphQL%20is%20now%20available%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fgraphql-now-available&t=GraphQL%20is%20now%20available%20in%20Supabase)

[Last post\\
\\
**Introducing Supabase Enterprise** \\
\\
30 March 2022](https://supabase.com/blog/supabase-enterprise)

[Next post\\
\\
**Community Day** \\
\\
28 March 2022](https://supabase.com/blog/community-day-lw4)

[launch-week](https://supabase.com/blog/tags/launch-week) [graphql](https://supabase.com/blog/tags/graphql)

On this page

- [Schema Reflection](https://supabase.com/blog/graphql-now-available#schema-reflection)
- [Security](https://supabase.com/blog/graphql-now-available#security)
  - [Authentication](https://supabase.com/blog/graphql-now-available#authentication)
  - [Authorization](https://supabase.com/blog/graphql-now-available#authorization)
- [Performance](https://supabase.com/blog/graphql-now-available#performance)
- [Getting Started](https://supabase.com/blog/graphql-now-available#getting-started)
- [Example app: Build a HN clone with Postgres and GraphQL](https://supabase.com/blog/graphql-now-available#example-app-build-a-hn-clone-with-postgres-and-graphql)
- [Supabase + The Guild](https://supabase.com/blog/graphql-now-available#supabase--the-guild)
- [Limitations & Roadmap](https://supabase.com/blog/graphql-now-available#limitations--roadmap)
- [More pg\_graphql](https://supabase.com/blog/graphql-now-available#more-pg_graphql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgraphql-now-available&text=GraphQL%20is%20now%20available%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgraphql-now-available&text=GraphQL%20is%20now%20available%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fgraphql-now-available&t=GraphQL%20is%20now%20available%20in%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)