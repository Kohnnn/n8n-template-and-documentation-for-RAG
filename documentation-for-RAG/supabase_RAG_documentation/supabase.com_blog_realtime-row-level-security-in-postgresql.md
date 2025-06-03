---
url: "https://supabase.com/blog/realtime-row-level-security-in-postgresql"
title: "Realtime Postgres RLS now available on Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Realtime Postgres RLS now available on Supabase

01 Dec 2021

•

7 minute read

[![Oliver Rice avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Folirice.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Oliver RiceEngineering](https://github.com/olirice)

![Realtime Postgres RLS now available on Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Frealtime-row-level-security-in-postgresql%2Frealtime-row-level-security-in-postgresql-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Realtime is a server that listens to changes in your PostgreSQL database and broadcasts the changes to clients through a websocket connection.

Today, we're announcing security improvements to Realtime, where database changes will be broadcast to authenticated users, respecting the same PostgreSQL policies that you use for Row Level Security.

## Demo [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#demo)

Realtime Row Level Security in PostgreSQL - YouTube

Supabase

54.4K subscribers

[Realtime Row Level Security in PostgreSQL](https://www.youtube.com/watch?v=zHvatf2wySI)

Supabase

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

Watch later

Share

Copy link

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=zHvatf2wySI "Watch on YouTube")

## Overview [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#overview)

Since the first commit of Realtime server back in [September 2019](https://github.com/supabase/realtime/commit/175f649784147af80acfc9ff5be9d160285c76ea),
we've worked hard to improve its usability and scalability.

Until now, Realtime did not adhere to RLS policies and instead broadcast all database changes to all clients.
The unsafe nature of this behavior is the reason why Realtime has been an opt-in feature, and a key reason why we are still in Beta.

As more developers rely on Realtime to receive and send database changes in their apps and services,
security has become a primary concern for us and others in the community who wish to build secure systems with Realtime.

Supabase projects have supported Row Level Security (RLS) for API authorization since our [Auth launch](https://supabase.io/blog/supabase-auth).
In that time, it has quickly become the recommended way to implement authorization.

As we were evaluating possible solutions to improve Realtime security, we looked to our Auth implementation as inspiration for a cohesive security system.

Today, we're updating Realtime to respect PostgreSQL RLS policies, so you can define your security rules once and have them automatically apply everywhere!

Before diving deeper into our Realtime RLS implementation, let's briefly cover how RLS works in PostgreSQL.

## Row Level Security Primer [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#row-level-security-primer)

When you need to control access to individual rows of data, PostgreSQL has you covered with [Row Level Security (RLS) policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html).
An RLS policy is a snippet of SQL filtering which users have the authority to create/read/update/delete rows in a table.

For example, the following policy would allow users to select their own rows in a todos table:

hideCopy

`
create policy todo_select_policy
    on todos for select
    using ( (select auth.uid()) = user_id );
`

which is equivalent to adding

hideCopy

`
select *
from todos
where auth.uid() = todos.user_id; -- Policy is implicitly added.
`

to queries.

Check out the [Row Level Security guide](https://supabase.com/docs/guides/auth/row-level-security) for more info on how to use RLS with your project.

## Realtime Design [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#realtime-design)

Our Realtime server receives and decodes binary changes from PostgreSQL logical replication, converts those changes to JSON, and broadcasts them to all connected clients.

### Challenge for RLS [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#challenge-for-rls)

The challenge, when applying row level security to the replication stream is that the visibility of a row may be different for each user subscribed to a database table.

We recognized that to fully secure Realtime in accordance with row level security, a row's visibility must be checked separately for each user on every change.
However, this quickly becomes a performance bottleneck when the number of changes, or number of subscribers, is large.

Since we can't control the number of subscribers or the number of changed records, we instead focused on making the security check for each user on every change as fast as possible.

### Implementation Overview [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#implementation-overview)

With these challenges in mind, we upstreamed the security responsibility to the database. Write Ahead Log Realtime Unified Security (WALRUS) exposes a PostgreSQL
function that Realtime server invokes with database changes.

### WALRUS Implementation [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#walrus-implementation)

[WALRUS](https://github.com/supabase/walrus) inspects each record in the replication change to:

- Identify the source table (e.g. `public.notes`).
- Identify the change's action (INSERT/UPDATE/DELETE/TRUNCATE\*).
- Query the `subscription` table to determine the connected users who are actively subscribed to the source table. The `subscription` table is kept up to date by the Realtime server and tracks all connected users and the tables they are currently subscribed to.
- For each subscriber:
  - Assume the identity of the subscriber.
  - Query the source table to see if the record is visible to that subscriber.
- Report the list of subscribers who are authorized to view the record back to Realtime server.

\*Realtime server does not broadcast TRUNCATE changes

**Efficiently Query to Check Access**

To maximize throughput, the query used to evaluate if a row is visible to a subscriber always queries using the tables primary key.

For example:

hideCopy

`
select exists (select 1 from some_table where id = 806);
`

When more than one subscriber exists, the query is wrapped in a [prepared statement](https://www.postgresql.org/docs/13/sql-prepare.html) to remove the cost of the PostgreSQL
query planner on subsequent calls. The query planner time is frequently 2-3x execution time for simple queries, so this immediately multiplies throughput in the most common cases!

hideCopy

`
"Planning Time: 0.099 ms"
"Execution Time: 0.051 ms"
`

**Colocation**

Colocating the security engine with subscriber data inside PostgreSQL allows us to avoid significant overhead when applying RLS policies.
Namely, network round-trip latency and I/O bottlenecks are removed while connection overhead is reduced relative to testing each record's visibility by polling the database from a separate process.
Instead, the SQL function only consumes a single connection and performs no network I/O.

### Performance [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#performance)

The throughput performance of the database server is best measured in terms of record processing time. As the number of subscribers to a table grows, the time required to process each record,
and the resultant processing time also grows.

![supabase-realtime-processing-per-subscription](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-three%2Frealtime-row-level-security-in-postgresql%2Fsupabase-realtime-processing-per-subscription.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

| Subscribers | 1 | 5 | 10 | 25 | 50 | 100 | 250 | 500 | 1,000 | 2,000 | 5,000 | 10,000 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Processing Time (ms) | 11.2 | 12.5 | 14.2 | 16.7 | 18.8 | 24.5 | 27.8 | 29.1 | 64.7 | 75.5 | 158.4 | 303.8 |

## Best Practices for Performance [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#best-practices-for-performance)

To get the most out of Realtime row level security, follow these guidelines:

### Disable for public tables [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#disable-for-public-tables)

If your data is insensitive or publicly available, such as stock prices listed under NASDAQ, then don't enable row level security!

The fastest security policy is one that doesn't exist :)

### Optimize your policies [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#optimize-your-policies)

If you do need row level security, make sure that your policies are fast.

Remember that your policy is executed _each_ time a query touches the table that the policy is applied to. If your policy is slow, all access to that table will be slow.
Avoid joins within RLS policies when you can, and make sure all filter conditions use an index.

Additionally, keep in mind that if you use joins within an RLS policy, any RLS policies on the tables you're joining to will also be executed in turn, adding to the overall overhead.

### Small primary keys [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#small-primary-keys)

Keep your primary keys small and efficient.

Use single column primary keys with a fixed field size (integer, uuid, etc.) over text or multi-column indexes.

## Next Steps [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#next-steps)

Realtime RLS is available today on all existing and new Supabase projects. To get started, upgrade your Supabase JavaScript client to version v1.23.0
and launch your new PostgreSQL database today: [database.new](https://database.new/)

## More Postgres resources [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#more-postgres-resources)

- [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
- [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
- [Postgres Views](https://supabase.com/blog/postgresql-views)
- [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
- [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
- [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)

## Credits [\#](https://supabase.com/blog/realtime-row-level-security-in-postgresql\#credits)

Authored by:

- [Oliver Rice](https://github.com/olirice)
- [Wen Bo Xie](https://github.com/w3b6x9)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frealtime-row-level-security-in-postgresql&text=Realtime%20Postgres%20RLS%20now%20available%20on%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frealtime-row-level-security-in-postgresql&text=Realtime%20Postgres%20RLS%20now%20available%20on%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Frealtime-row-level-security-in-postgresql&t=Realtime%20Postgres%20RLS%20now%20available%20on%20Supabase)

[Last post\\
\\
**Supabase acquires Logflare** \\
\\
2 December 2021](https://supabase.com/blog/supabase-acquires-logflare)

[Next post\\
\\
**Supabase Studio** \\
\\
30 November 2021](https://supabase.com/blog/supabase-studio)

[launch-week](https://supabase.com/blog/tags/launch-week) [realtime](https://supabase.com/blog/tags/realtime) [security](https://supabase.com/blog/tags/security)

On this page

- [Demo](https://supabase.com/blog/realtime-row-level-security-in-postgresql#demo)
- [Overview](https://supabase.com/blog/realtime-row-level-security-in-postgresql#overview)
- [Row Level Security Primer](https://supabase.com/blog/realtime-row-level-security-in-postgresql#row-level-security-primer)
- [Realtime Design](https://supabase.com/blog/realtime-row-level-security-in-postgresql#realtime-design)
  - [Challenge for RLS](https://supabase.com/blog/realtime-row-level-security-in-postgresql#challenge-for-rls)
  - [Implementation Overview](https://supabase.com/blog/realtime-row-level-security-in-postgresql#implementation-overview)
  - [WALRUS Implementation](https://supabase.com/blog/realtime-row-level-security-in-postgresql#walrus-implementation)
  - [Performance](https://supabase.com/blog/realtime-row-level-security-in-postgresql#performance)
- [Best Practices for Performance](https://supabase.com/blog/realtime-row-level-security-in-postgresql#best-practices-for-performance)
  - [Disable for public tables](https://supabase.com/blog/realtime-row-level-security-in-postgresql#disable-for-public-tables)
  - [Optimize your policies](https://supabase.com/blog/realtime-row-level-security-in-postgresql#optimize-your-policies)
  - [Small primary keys](https://supabase.com/blog/realtime-row-level-security-in-postgresql#small-primary-keys)
- [Next Steps](https://supabase.com/blog/realtime-row-level-security-in-postgresql#next-steps)
- [More Postgres resources](https://supabase.com/blog/realtime-row-level-security-in-postgresql#more-postgres-resources)
- [Credits](https://supabase.com/blog/realtime-row-level-security-in-postgresql#credits)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frealtime-row-level-security-in-postgresql&text=Realtime%20Postgres%20RLS%20now%20available%20on%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Frealtime-row-level-security-in-postgresql&text=Realtime%20Postgres%20RLS%20now%20available%20on%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Frealtime-row-level-security-in-postgresql&t=Realtime%20Postgres%20RLS%20now%20available%20on%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)