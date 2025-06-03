---
url: "https://supabase.com/blog/new-in-postgres-15"
title: "What's new in Postgres 15?"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# What's new in Postgres 15?

16 Dec 2022

•

5 minute read

[![Pavel Borisov avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F63344111%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Pavel BorisovPostgres Engineer](https://github.com/pashkinelfe)

![What's new in Postgres 15?](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw6-community%2Fpg15.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The PostgreSQL community [released](https://www.postgresql.org/docs/current/release-15.html) version 15 (stable) in October 2022. Let's review some of the new features.

## **The permission model is more secure** [\#](https://supabase.com/blog/new-in-postgres-15\#the-permission-model-is-more-secure)

`CREATE` permission is revoked from all users except the database owner. It makes permission assigning more tunable ( [details](https://www.postgresql.org/docs/15/ddl-schemas.html#DDL-SCHEMAS-PATTERNS)). And for the migrated database don't forget to revoke `CREATE` permission on the public schema manually to fit the new policy.

There is a useful option `CREATE VIEW .. WITH (security_invoker=on)` to create a view that uses permissions of a view caller rather than a view creator to access underlying tables. With this, you should not worry that a user that doesn't have access to a table could see its data through a view.

## **Performance speed-up** [\#](https://supabase.com/blog/new-in-postgres-15\#performance-speed-up)

Sorting rows of data is a frequent operation inside the PostgreSQL code. It is used not only when you use the ORDER BY clause, but also in indices creation, table partitioning, etc. Furthermore, sorting is one of the most algorithmically expensive operations. So increasing speed up to 4 times of both in-memory and on-disk sorts in version 15 is one of the main reasons to upgrade.

Window functions performance is also improved.

## The **MERGE operation was introduced** [\#](https://supabase.com/blog/new-in-postgres-15\#the-merge-operation-was-introduced)

A new `MERGE` operation is to modify target table data according to the provided source with many available conditional processing options. This allows data processing without writing procedural language functions or complex CTE queries. Essentially merge can work as conditional delete/insert/update and also this makes PostgreSQL syntax implementation closer to SQL:2008 standard. For details on MERGE uses see: [https://www.postgresql.org/docs/15/sql-merge.html](https://www.postgresql.org/docs/15/sql-merge.html)

## **New features for logical replication** [\#](https://supabase.com/blog/new-in-postgres-15\#new-features-for-logical-replication)

Logical replication is one of the fast-developing parts of PostgreSQL. Since version 15 two-phase commits are supported in logical replication. Also now you can choose parts of table data to logically replicate using i.e. some sets of rows and columns. In the case of replication conflict i.e. replicated data violate some constraint or there is a permission violation on a subscriber server user can choose to skip the conflicting transaction or disable the subscription until the user can decide how to handle the conflict.

## **Increase parallelization** [\#](https://supabase.com/blog/new-in-postgres-15\#increase-parallelization)

Parallel execution of queries using several worker processes is another part of PostgreSQL that develops fast. In version 15 `SELECT DISTINCT` queries that drop duplicate rows from output can improve performance by using parallel workers.

## **JSON logging** [\#](https://supabase.com/blog/new-in-postgres-15\#json-logging)

Output log data as JSON structure helps logs processing and structured output on the client's side.

## **Compressing options** [\#](https://supabase.com/blog/new-in-postgres-15\#compressing-options)

In version 15 _Zstandard_ and _ZL4_ can be chosen instead of _pglz_ as a WAL compression method. WAL compression is useful to decrease disk space usage while safeguarding data integrity.

When you make a database backup with the provided pg _basebackup extension you can also choose \_Zstandard_ or _ZL4_ to compress database backups on the server side, to transfer less data over the network.

## **New POSIX regexp functions** [\#](https://supabase.com/blog/new-in-postgres-15\#new-posix-regexp-functions)

There are several new regular expressions functions that you may find useful for strings processing i.e. regexp\_substr(), regexp\_count(), etc. [Details](https://www.postgresql.org/docs/15/functions-matching.html#FUNCTIONS-POSIX-REGEXP)

## **Full Changelog** [\#](https://supabase.com/blog/new-in-postgres-15\#full-changelog)

You can find a full changelog and full list of new features in the [official changelog](https://www.postgresql.org/docs/15/release-15.html#id-1.11.6.6.5).

## **Should you upgrade to PG15?** [\#](https://supabase.com/blog/new-in-postgres-15\#should-you-upgrade-to-pg15)

The main reason to switch to a new PostgreSQL version is the large number of bug fixes that each new version delivers. Bug fixes aren't as prominent as new features or performance improvements, but they often have a greater impact. While some bug fixes are applied to previous versions, these changes require modifications to the ABI, interface functions, and system catalog structures, often not possible in an already-released major version.

So, the TL;DR: yes, you should update to improve stability.

Upgrading is safe thanks to the half-year stabilization period between April's code freeze of every new feature and October's stable release. Generally, you'd rather find a bug in an old version than in a new one.

Before choosing to upgrade, don't forget to check the list of rare cases that need [manual actions](https://www.postgresql.org/docs/current/release-15.html#id-1.11.6.6.4) before or after the upgrade.

- If you're self-hosting, upgrading between major PostgreSQL is easily done with [pg\_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html) utility or a set of recommended practices in the [official docs](https://www.postgresql.org/docs/current/upgrading.html).
- If you're starting a new project on Supabase, you'll already be on PG15.
- If you want to upgrade an existing project, check out our [Upgrading](https://supabase.com/docs/guides/platform/migrating-and-upgrading-projects#upgrade-your-project) documentation.

## More Launch Week 6 [\#](https://supabase.com/blog/new-in-postgres-15\#more-launch-week-6)

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-in-postgres-15&text=What%27s%20new%20in%20Postgres%2015%3F)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-in-postgres-15&text=What%27s%20new%20in%20Postgres%2015%3F)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-in-postgres-15&t=What%27s%20new%20in%20Postgres%2015%3F)

[Last post\\
\\
**Launch Week 6: Wrap Up** \\
\\
16 December 2022](https://supabase.com/blog/launch-week-6-wrap-up)

[Next post\\
\\
**pg\_graphql v1.0** \\
\\
16 December 2022](https://supabase.com/blog/pg-graphql-v1)

[postgres](https://supabase.com/blog/tags/postgres) [launch-week](https://supabase.com/blog/tags/launch-week) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [**The permission model is more secure**](https://supabase.com/blog/new-in-postgres-15#the-permission-model-is-more-secure)
- [**Performance speed-up**](https://supabase.com/blog/new-in-postgres-15#performance-speed-up)
- [The **MERGE operation was introduced**](https://supabase.com/blog/new-in-postgres-15#the-merge-operation-was-introduced)
- [**New features for logical replication**](https://supabase.com/blog/new-in-postgres-15#new-features-for-logical-replication)
- [**Increase parallelization**](https://supabase.com/blog/new-in-postgres-15#increase-parallelization)
- [**JSON logging**](https://supabase.com/blog/new-in-postgres-15#json-logging)
- [**Compressing options**](https://supabase.com/blog/new-in-postgres-15#compressing-options)
- [**New POSIX regexp functions**](https://supabase.com/blog/new-in-postgres-15#new-posix-regexp-functions)
- [**Full Changelog**](https://supabase.com/blog/new-in-postgres-15#full-changelog)
- [**Should you upgrade to PG15?**](https://supabase.com/blog/new-in-postgres-15#should-you-upgrade-to-pg15)
- [More Launch Week 6](https://supabase.com/blog/new-in-postgres-15#more-launch-week-6)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-in-postgres-15&text=What%27s%20new%20in%20Postgres%2015%3F)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-in-postgres-15&text=What%27s%20new%20in%20Postgres%2015%3F)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnew-in-postgres-15&t=What%27s%20new%20in%20Postgres%2015%3F)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)