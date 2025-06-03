---
url: "https://supabase.com/blog/supabase-pgbouncer"
title: "PgBouncer is now available in Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# PgBouncer is now available in Supabase

02 Apr 2021

•

5 minute read

[![Angelico de los Reyes avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdragarcia.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Angelico de los ReyesEngineering](https://github.com/dragarcia)

![PgBouncer is now available in Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fbouncer%2Fpgbouncer-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

PgBouncer is now deprecated. Use
[Supavisor](https://supabase.com/blog/supavisor-postgres-connection-pooler) instead.

Javascript Frameworks like [Next.js,](https://nextjs.org/) [Redwood](https://redwoodjs.com/), [Blitz](https://blitzjs.com/), and tools
like [Prisma](https://www.prisma.io/docs/guides/deployment/deployment#pgbouncer) are all moving in one direction. Serverless.

Serverless functions work great for developers using the Supabase API because we manage a [PostgREST](https://postgrest.org/en/v7.0.0/)
server for every project. Supabase also provides direct access to the Postgres database, so that developers can connect any tool they want.
Unfortunately, Serverless function don't work well for direct Postgres connections (for reasons we'll discuss soon).

Jamstack developers make up a large portion of the Supabase Community. While we'd love for developers to use PostgREST, we mostly want
developers to use Postgres. This means supporting the tools which they already love.

So today we are adding [PgBouncer](https://www.pgbouncer.org/), an open source connection pooler for Postgres.

## What is Connection Pooling? [\#](https://supabase.com/blog/supabase-pgbouncer\#what-is-connection-pooling)

![Connection Pooling](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fbouncer%2Fconnection-pool.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Typically when a client connects to a PostgreSQL database, they need to open and manage their own database connection. With a connection pool,
connections are already opened and available for use. When a client makes a request, they use a connection from the pool. When the transaction
or session is completed the underlying connection is simply returned to the pool and is once again free to be used by another user or application.

### Handling connection surges [\#](https://supabase.com/blog/supabase-pgbouncer\#handling-connection-surges)

In a traditional architecture, middleware servers (e.g. APIs) manage a small number of connection to a Postgres database.
Essentially, the middleware server is a connection pool.

In a Serverless environment, there is no middleware server to maintain a connection, so they create a **new** connection for
each concurrent request. Since Serverless functions are typically used for bursty workloads, this can end up opening a lot of
connections to the database and overwhelm your Postgres server.

Connection pools mitigate this. Connections are opened beforehand and recycled across users and applications. What's more,
[connection pools are specialized for this task](https://medium.com/@k.wahome/database-connections-less-is-more-86c406b6fad).
A small number of connections is sufficient to handle demand ten, twenty times its size, or even more. Whenever a new connection
is required it is taken from a pool of open and available connections instead of initializing an entirely new one. This eliminates
the need to spawn a new process.

## Misconceptions [\#](https://supabase.com/blog/supabase-pgbouncer\#misconceptions)

It's a common misconception that PgBouncer increases the number of connections a Postgres instance can open.
This is not the case. If Postgres is configured for a maximum of 50 connections before connection pooling, it
will still only be able to open 50. Connection pooling simply keeps connections open and idle, ready to accept clients. Nevertheless,
as mentioned above, PgBouncer allows your database to be able to handle more than it can without a connection pool.

## Connection "Queuing" [\#](https://supabase.com/blog/supabase-pgbouncer\#connection-queuing)

PgBouncer is like a Queue. With regular Postgres, when you hit your connection limit, new connections are rejected. PgBouncer overcomes this
limitation. When all connections in the pool are in-use, it doesn't reject any incoming requests. Instead,
[PgBouncer queues them](https://www.percona.com/blog/connection-queuing-in-pgbouncer-is-it-a-magical-remedy/) until a
connection is returned to the pool and made available. This doesn't mean connection pooling is a magic bullet. If your clients is
running expensive queries then the connections might take a long time before they are returned to the pool. The natural solution to
this is to increase your database resources so that it processes queries faster or PgBouncer can open more connections.

## Using Connection Pooling in Supabase [\#](https://supabase.com/blog/supabase-pgbouncer\#using-connection-pooling-in-supabase)

![Pooling UI](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fbouncer%2Fpooler-supabase.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

From today, all new projects will include connection pooling. In the `Database` section of our dashboard, you will notice a new section for it.
Under the hood, we utilise PgBouncer which is installed in the same server as PostgreSQL. Through the dashboard, we provide you with the
necessary connection details to start using the connection pool as well as the ability to modify `Pool Mode`. Not sure which mode to use?
Below is a quick primer on each mode.

## Pool modes [\#](https://supabase.com/blog/supabase-pgbouncer\#pool-modes)

`Pool Mode` determines how PgBouncer handles a connection.

### Session [\#](https://supabase.com/blog/supabase-pgbouncer\#session)

When a new client connects, a connection is assigned to the client until it disconnects. Afterward, the connection is returned back to the pool. All PostgreSQL features can be used with this option.

### Transaction [\#](https://supabase.com/blog/supabase-pgbouncer\#transaction)

This is the suggested option for serverless functions. With this, the connection is only assigned to the client for the duration of a transaction. Once done, the connection is returned to the pool. Two consecutive transactions from the same client could be done over two, different connections. Some session-based PostgreSQL features such as prepared statements are not available with this option. A more comprehensive list of incompatible features can be found [here](https://www.pgbouncer.org/features.html).

### Statement [\#](https://supabase.com/blog/supabase-pgbouncer\#statement)

This is the most granular option. Connections are returned to the pool after every statement. Transactions with multiple statements are not allowed. This is best used when `AUTOCOMMIT` is in use.

## What's next? [\#](https://supabase.com/blog/supabase-pgbouncer\#whats-next)

Try out connection pooling now with a new project in the [dashboard.](https://supabase.com/dashboard) For now, we do not have any plans to port this over to older projects.

Eventually, we will expose more PgBouncer settings to the UI such as `Pool Size`. At the moment it is set to `15`.

We are still working towards getting the latest version of Supabase Postgres to both the AWS and Digital Ocean marketplaces. Follow us on [Twitter](https://twitter.com/supabase) to be informed once it's released!

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-pgbouncer&text=PgBouncer%20is%20now%20available%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-pgbouncer&text=PgBouncer%20is%20now%20available%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-pgbouncer&t=PgBouncer%20is%20now%20available%20in%20Supabase)

[Last post\\
\\
**Supabase Dot Com** \\
\\
2 April 2021](https://supabase.com/blog/supabase-dot-com)

[Next post\\
\\
**Workflows are coming to Supabase** \\
\\
2 April 2021](https://supabase.com/blog/supabase-workflows)

[database](https://supabase.com/blog/tags/database) [engineering](https://supabase.com/blog/tags/engineering)

On this page

- [What is Connection Pooling?](https://supabase.com/blog/supabase-pgbouncer#what-is-connection-pooling)
- [Misconceptions](https://supabase.com/blog/supabase-pgbouncer#misconceptions)
- [Connection "Queuing"](https://supabase.com/blog/supabase-pgbouncer#connection-queuing)
- [Using Connection Pooling in Supabase](https://supabase.com/blog/supabase-pgbouncer#using-connection-pooling-in-supabase)
- [Pool modes](https://supabase.com/blog/supabase-pgbouncer#pool-modes)
- [What's next?](https://supabase.com/blog/supabase-pgbouncer#whats-next)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-pgbouncer&text=PgBouncer%20is%20now%20available%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-pgbouncer&text=PgBouncer%20is%20now%20available%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-pgbouncer&t=PgBouncer%20is%20now%20available%20in%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)