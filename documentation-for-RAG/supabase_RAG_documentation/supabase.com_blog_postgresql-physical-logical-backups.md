---
url: "https://supabase.com/blog/postgresql-physical-logical-backups"
title: "Physical vs Logical Backups in PostgreSQL"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Physical vs Logical Backups in PostgreSQL

07 Jul 2020

•

5 minute read

[![Angelico de los Reyes avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdragarcia.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Angelico de los ReyesEngineering](https://github.com/dragarcia)

PostgreSQL backups can be categorized into two types: _logical_ and _physical_. This post briefly covers each type and discusses the situations where you would use either one.

We'll cover some of the many tools you can use for Postgres backups in future posts.

## Logical Backups [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#logical-backups)

This form of backup is typically achieved by [translating all the data into a set of SQL commands and writing it into a single file](https://www.postgresql.org/docs/current/backup-dump.html). This can then be fed to any database cluster to recreate everything. In your CLI, performing logical backups can be as easy as:

`
pg_dump db_name > file_name.sql
`

for a single database, and:

`
pg_dumpall > file_name.sql
`

for an entire database cluster. Both the [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) and [pg\_dumpall](https://www.postgresql.org/docs/current/app-pg-dumpall.html) utilities have their respective additional options for you to choose from and set up your desired logical backup setting. Recovering from them is comparably as simple:

`
psql -d db_name -f file_name.sql
`

### What is it good for? [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#what-is-it-good-for)

#### Simpler and quicker way of performing backups [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#simpler-and-quicker-way-of-performing-backups)

As shown above, a single command is enough to perform a logical backup and another to recover from it. As a novice with databases, this would be an ideal and non-intimidating ensure that your database is backed up at all times.

#### Migration between different major versions of Postgres [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#migration-between-different-major-versions-of-postgres)

If you are planning to migrate to a different major version of Postgres (for example, from Postgres 11 to Postgres 12), logical backups via `pg_dumpall` would surely be your [tool of choice](https://www.postgresql.org/docs/current/upgrading.html). This is mainly because internal data storage formats may differ between major versions. This is the basis of physical backups, eliminating it as an option when upgrading. We'll go deeper into migrations and how to perform them in another post.

#### Backing up a single specific database [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#backing-up-a-single-specific-database)

With `pg_dump`, you can constantly back up a single, targeted database.

## Physical Backups [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#physical-backups)

Physical backups pertain to the actual set of files or file systems where your database data is stored. One option for physical backups involves [taking a snapshot](https://www.postgresql.org/docs/current/backup-file.html) of your data files by making a copy of them.

### What is it good for? [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#what-is-it-good-for-1)

#### More ideal for larger databases [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#more-ideal-for-larger-databases)

As your database grows to the size of a few gigabytes, backing it up through physical backups is more ideal than through logical backups. As explained [here](https://devcenter.heroku.com/articles/heroku-postgres-data-safety-and-continuous-protection#the-performance-impact-of-logical-backups), over time, performing logical backups in large databases could lead to degraded performance for other queries. Given the long run time as well to successfully perform a logical backup on a large database, errors have a higher chance of occurring, making the eventual backup unusable.

#### Achieving Point in Time Recovery [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#achieving-point-in-time-recovery)

Postgres also generates [Write Ahead Log](https://www.postgresql.org/docs/current/wal-intro.html) (WAL) files, which can be used together with a backed-up file system to [recover a database up to any chosen point in time](https://www.postgresql.org/docs/current/continuous-archiving.html). When disaster strikes, this is one of the best options for recreating your database up to the point right before the unfortunate happens. This greatly minimizes [Recovery Point Objective (RPO)](https://www.ibm.com/services/business-continuity/rpo) along the way. Even better, tools such as [WAL-G](https://github.com/wal-g/wal-g) are readily available to simplify the steps involved in setting this up.

## Conclusion [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#conclusion)

All in all, logical and physical backups are generated differently from one another. Neither has an advantage over the other. Depending on your needs, each brings unique uses to the table:

| Logical | Physical |
| :-- | :-- |
| Simpler way of getting started with backups. | Better way of handling backups for larger database clusters. |
| Using it to migrate between different major versions of Postgres. | Using it for Point in Time Recovery. |
| Having the option to back up a single database. |  |

## More Postgres resources [\#](https://supabase.com/blog/postgresql-physical-logical-backups\#more-postgres-resources)

- [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
- [Partial data dumps using Postgres Row Level Security](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls)
- [Postgres Views](https://supabase.com/blog/postgresql-views)
- [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
- [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
- [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
- [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-physical-logical-backups&text=Physical%20vs%20Logical%20Backups%20in%20PostgreSQL)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-physical-logical-backups&text=Physical%20vs%20Logical%20Backups%20in%20PostgreSQL)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-physical-logical-backups&t=Physical%20vs%20Logical%20Backups%20in%20PostgreSQL)

[Last post\\
\\
**What are PostgreSQL Templates?** \\
\\
9 July 2020](https://supabase.com/blog/postgresql-templates)

[Next post\\
\\
**Supabase Alpha June 2020** \\
\\
1 July 2020](https://supabase.com/blog/supabase-alpha-june-2020)

[postgres](https://supabase.com/blog/tags/postgres) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Logical Backups](https://supabase.com/blog/postgresql-physical-logical-backups#logical-backups)
- [Physical Backups](https://supabase.com/blog/postgresql-physical-logical-backups#physical-backups)
- [Conclusion](https://supabase.com/blog/postgresql-physical-logical-backups#conclusion)
- [More Postgres resources](https://supabase.com/blog/postgresql-physical-logical-backups#more-postgres-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-physical-logical-backups&text=Physical%20vs%20Logical%20Backups%20in%20PostgreSQL)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-physical-logical-backups&text=Physical%20vs%20Logical%20Backups%20in%20PostgreSQL)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgresql-physical-logical-backups&t=Physical%20vs%20Logical%20Backups%20in%20PostgreSQL)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)