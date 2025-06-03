---
url: "https://supabase.com/blog/dedicated-poolers"
title: "Dedicated Poolers"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Dedicated Poolers

07 Mar 2025

•

3 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Dedicated Poolers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdedicated-poolers%2Fdedicated-poolers-og.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we're announcing **Dedicated Poolers** \- a Postgres connection pooler that's co-located with your database for maximum performance and reliability.

Don't know what a Pooler is? Check out our [docs](https://supabase.com/docs/guides/database/connecting-to-postgres#serverside-poolers).

This is available today for select customers, and will be generally available by 20th March, 2025. If you want to be notified when it's ready, [sign up here](https://forms.supabase.com/dedicated-pooler).

### Supabase Dedicated Pooler [\#](https://supabase.com/blog/dedicated-poolers\#supabase-dedicated-pooler)

The Dedicated Pooler is a [PgBouncer](https://www.pgbouncer.org/) instance that's co-located with your Postgres database. This will require you to connect with IPv6 or, if that's not an option, you can use the [IPv4 add-on](https://supabase.com/guides/platform/ipv4-address).

The dedicated pooler is isolated to your own project and grants you fine-grained control over the configuration.

### Connecting to your database [\#](https://supabase.com/blog/dedicated-poolers\#connecting-to-your-database)

This gives you now 3 options for connecting to your database:

![3 different connection options](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdedicated-poolers%2Fconnection-options.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

3 different connection options

1. **Direct connections (free):** recommended for when you are connecting using servers.
2. **Shared Pooler (free):** recommended for when you are connecting using serverless functions (like Next.js or AWS Lambda)
3. **Dedicated Pooler (Pro Plan and above):** recommended for when you are connecting using serverless functions and you start to scale up. It is available on the Pro Plan and above.

## Choosing between Supavisor and PgBouncer [\#](https://supabase.com/blog/dedicated-poolers\#choosing-between-supavisor-and-pgbouncer)

A year ago AWS [started charging for IPv4 addresses](https://supabase.com/blog/ipv6). We introduced [Supavisor](https://supabase.com/blog/supavisor-postgres-connection-pooler) to ensure that you didn't need to pay to connect to your database if your network didn't support IPv6. Only ~45% of the world have adopted IPv6, so this was a great solution for many.

![IPv6 adoption](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdedicated-poolers%2Fipv6-adoption.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Source: https://www.google.com/intl/en/ipv6/statistics.html

In the recent months, our platform has seen unprecedented growth. Tens of thousands of new developers are pouring into Supabase every week, doing weird and wonderful things with their databases:

![3 different connection options](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdedicated-poolers%2Fsignups.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase weekly sign ups

Introducing Dedicated Poolers gives you the flexibility to choose the right connection type for your use case. If you need dedicated hardware, you can now opt for a Dedicated Pooler on the Pro Plan and above for lower latency, better performance, and higher reliability.

### Getting started [\#](https://supabase.com/blog/dedicated-poolers\#getting-started)

Dedicated Poolers are available today for our Enterprise customers, and will be generally available by 20th March, 2025. If you want to be notified when it's ready, [sign up here](https://forms.supabase.com/dedicated-pooler).

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdedicated-poolers&text=Dedicated%20Poolers)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdedicated-poolers&text=Dedicated%20Poolers)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdedicated-poolers&t=Dedicated%20Poolers)

[Last post\\
\\
**Migrating from the MongoDB Data API to Supabase** \\
\\
20 March 2025](https://supabase.com/blog/migrating-mongodb-data-api-with-supabase)

[Next post\\
\\
**Postgres as a Graph Database: (Ab)using pgRouting** \\
\\
25 February 2025](https://supabase.com/blog/pgrouting-postgres-graph-database)

[postgres](https://supabase.com/blog/tags/postgres)

On this page

- [Supabase Dedicated Pooler](https://supabase.com/blog/dedicated-poolers#supabase-dedicated-pooler)
- [Connecting to your database](https://supabase.com/blog/dedicated-poolers#connecting-to-your-database)

- [Choosing between Supavisor and PgBouncer](https://supabase.com/blog/dedicated-poolers#choosing-between-supavisor-and-pgbouncer)
  - [Getting started](https://supabase.com/blog/dedicated-poolers#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdedicated-poolers&text=Dedicated%20Poolers)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fdedicated-poolers&text=Dedicated%20Poolers)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fdedicated-poolers&t=Dedicated%20Poolers)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![3 different connection options](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdedicated-poolers%2Fconnection-options.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![IPv6 adoption](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdedicated-poolers%2Fipv6-adoption.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![3 different connection options](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdedicated-poolers%2Fsignups.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)