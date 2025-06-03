---
url: "https://supabase.com/blog/partial-postgresql-data-dumps-with-rls"
title: "Partial data dumps using Postgres Row Level Security"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Partial data dumps using Postgres Row Level Security

28 Jun 2022

•

6 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Partial data dumps using Postgres Row Level Security](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fpartial-dumps%2Fog-partial-dumps-with-rls.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

When working with databases, it's common to create a `seed.sql` file which contains a subset of production data for testing.

During early development, it's fine to dump the entire database and restore it on your development machine.
However, once you have production users this becomes a security issue - do you really want to dump your users' data onto your local machines?

There are many ways to solve this, but recently I stumbled upon a neat way to do it using PostgreSQL's Row Level Security (RLS).

The concept is simple:

1. Create a database user with restricted access.
2. Define some RLS rules for that user, limiting what data they can access.
3. Run `pg_dump` as that user.

For this scenario, let's imagine that you have a table called `profiles` in your database:

hideCopy

`
create table profiles (
id serial primary key,
name text,
email text
);
`

| `id` | `name` | `email` |
| --- | --- | --- |
| `1` | `Employee 1` | `employee1@supabase.com` |
| `2` | `Employee 2` | `employee2@supabase.com` |
| `3` | `Employee 3` | `employee3@supabase.com` |
| `4` | `Jenny` | `jenny@example.com` |
| `5` | `Joe` | `joe@example.com` |

In this case, if we ran a `pg_dump` we will save Jenny and Joe's personal data. We don't want that, so let's create a Postgres user called `exporter`, who can only dump the data we want.

### Step 1: Prepare a user [\#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls\#step-1-prepare-a-user)

Create a user to connect to the database. We'll call them `exporter` and grant them access to the public schema:

hideCopy

`
-- Create a new user with login privileges
create user exporter
with password 'exporter_secure_password';
-- Allow this user to select the rows we need
grant usage on schema public to exporter;
grant select on profiles to exporter;
`

### Step 2: Create data access rules [\#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls\#step-2-create-data-access-rules)

Let's turn on RLS for this table and limit the data which `exporter` can access:

hideCopy

`
-- Turn on Row Level Security
alter table profiles
enable row level security;
-- Only dump data for internal team members 1, 2, 3
create policy "Data dump rule" on profiles
for select
to exporter
using (
    id in (1, 2, 3)
);
`

### Step 3: Export the data [\#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls\#step-3-export-the-data)

Now we can use `pg_dump` to get only the data that we need.

Run the dump with the `exporter` user that we created above and use the `--enable-row-security` flag to ensure that the dump succeeds.

hideCopy

`
# Dump all the data into a "seed.sql" file
# which we can use to restore our local databases.
pg_dump \
-h db.host.supabase.co \
-U exporter \
-d postgres \
-n public \
--data-only \
--enable-row-security \
--table=profiles \
> seed.sql
`

hideCopy

`
-h db.host.supabase.co \
`

And that's it. You can follow this same pattern for any tables that you want to dump.

## Data access patterns [\#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls\#data-access-patterns)

RLS is a bit like appending a “where” clause to a `select`, so you can create all sorts of data access patterns. Let's see a few more which are useful for extracting seed data.

### Using email rules [\#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls\#using-email-rules)

Instead of using hardcoded numbers in our RLS policies, we could use email extensions to determine the users who we want to export:

hideCopy

`
-- Only dump data for supabase employees
create policy "Data dump rule" on profiles
for select
to exporter
using (
    substring(email from '@(.*)$') = 'supabase.com'
);
`

### Only recent data [\#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls\#only-recent-data)

If we have a table with a lot of data, like an `analytics` table, we might only care about the last 2 months of data.

hideCopy

`
-- A fake analytics table where we store actions a user takes
create table analytics (
id serial primary key,
ts timestamptz default now(),
profile_id references profiles,
event text
);
alter table profiles
enable row level security;
-- Here is an "age" rule so that we only dump the most recent analytics
create policy "Data dump rule" on logs
for select
to exporter
using (
    profile_id in (1, 2, 3) and
    ts > now() - interval '2 MONTHS' -- here's the magic
);
`

### Using flags [\#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls\#using-flags)

If you don't mind having some additional columns in you database, you can add flags to each row to determine whether it's safe to export.

hideCopy

`
create table profiles (
id serial primary key,
name text,
email text,
is_exportable boolean -- make this "TRUE" if you want to allow access
);
alter table profiles
enable row level security;
-- Only dump data for internal team members 1, 2, 3
create policy "Data dump rule" on profiles
for select
to exporter
using ( is_exportable = true );
`

## Conclusion [\#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls\#conclusion)

Using `seed` data isn't the only way to run development environments. It's also possible to run fully-masked copies of your database using tools like
[Snaplet](https://docs.snaplet.dev/tutorials/supabase-clone-environments).

We're also bullish on copy-on-write strategies which allow users to "fork" a database at a point in time,
a strategy used by [Database Lab Engine](https://postgres.ai/docs/database-lab).
DLE uses the ZFS file system to achieve this, but it's within reach of the Postgres core once alternative storage strategies become easier to implement.

If you want to try out the steps we described in this article, fire up a full PostgreSQL database: [database.new](https://database.new/)

## More Postgres resources [\#](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls\#more-postgres-resources)

- [Implementing "seen by" functionality with Postgres](https://supabase.com/blog/seen-by-in-postgresql)
- [Postgres Views](https://supabase.com/blog/postgresql-views)
- [Postgres Auditing in 150 lines of SQL](https://supabase.com/blog/audit)
- [Cracking PostgreSQL Interview Questions](https://supabase.com/blog/cracking-postgres-interview)
- [What are PostgreSQL Templates?](https://supabase.com/blog/postgresql-templates)
- [Realtime Postgres RLS on Supabase](https://supabase.com/blog/realtime-row-level-security-in-postgresql)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&text=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&text=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&t=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)

[Last post\\
\\
**Visualizing Supabase Data using Metabase** \\
\\
29 June 2022](https://supabase.com/blog/visualizing-supabase-data-using-metabase)

[Next post\\
\\
**Python data loading with Supabase** \\
\\
17 June 2022](https://supabase.com/blog/loading-data-supabase-python)

[postgresql](https://supabase.com/blog/tags/postgresql) [data](https://supabase.com/blog/tags/data) [planetpg](https://supabase.com/blog/tags/planetpg)

On this page

- [Step 1: Prepare a user](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#step-1-prepare-a-user)
- [Step 2: Create data access rules](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#step-2-create-data-access-rules)
- [Step 3: Export the data](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#step-3-export-the-data)

- [Data access patterns](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#data-access-patterns)
  - [Using email rules](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#using-email-rules)
  - [Only recent data](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#only-recent-data)
  - [Using flags](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#using-flags)
- [Conclusion](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#conclusion)
- [More Postgres resources](https://supabase.com/blog/partial-postgresql-data-dumps-with-rls#more-postgres-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&text=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&text=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpartial-postgresql-data-dumps-with-rls&t=Partial%20data%20dumps%20using%20Postgres%20Row%20Level%20Security)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)