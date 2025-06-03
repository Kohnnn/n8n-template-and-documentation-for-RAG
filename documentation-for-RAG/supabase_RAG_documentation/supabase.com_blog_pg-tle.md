---
url: "https://supabase.com/blog/pg-tle"
title: "Trusted Language Extensions for Postgres"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Trusted Language Extensions for Postgres

14 Apr 2023

•

6 minute read

[![Michel Pelletier avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmichelp.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Michel PelletierEngineering](https://github.com/michelp)

[![John Dalton avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdaltjoh-aws.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
John DaltonProduct Management Leader @ AWS](https://github.com/daltjoh-aws)

![Trusted Language Extensions for Postgres](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-5-supabase-pg-tle%2Fday-5-postgres-tle-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Most PostgreSQL cloud providers, such as Supabase and AWS RDS, do not allow users to install Postgres extensions into their databases until they have been rigorously vetted. Because of this, many useful Postgres extensions cannot be used on cloud platforms. To solve this, the RDS team has developed a new kind of extension called a **Trusted Language Extension** (TLE).

A TLE is a Postgres extension that is written in a Trusted Language, and it can be installed in any Postgres provider that has the [pg\_tle](https://github.com/aws/pg_tle) extension installed. The goal is to make more extensions available to developers, even if your database is hosted on the cloud.

## How Postgres extensions work [\#](https://supabase.com/blog/pg-tle\#how-postgres-extensions-work)

Before exploring what a Trusted Language Extension is, let’s cover the basics of Postgres Extensions and the notion of “Trusted Languages” in general.

A Postgres Extension is a bundle of SQL and other code, primarily [Data Definition Language](https://www.postgresql.org/docs/current/ddl.html) (DDL) code installed into the server’s filesystem, and instantiated in a database with the [`CREATE EXTENSION`](https://www.postgresql.org/docs/current/sql-createextension.html) command. This code can contain any SQL, but almost always includes additional function objects created with the [`CREATE FUNCTION`](https://www.postgresql.org/docs/current/sql-createfunction.html) DDL statement that expose the core features of the extension to the database in some programming language, including an external library function written in C.

Extensions provide a variety of additional functionality and allow third-party feature distribution without requiring changes to the Postgres database itself - including new data types, storage engines, helper functions, and even entire language runtimes like Javascript or Python.

Some examples of popular Postgres extensions include:

- [PostGIS](https://postgis.net/): for working with geospatial data
- [Timescale DB](https://www.timescale.com/): for working with timeseries data
- [Citus](https://www.citusdata.com/): for working with distributed tables
- [plv8](https://plv8.github.io/): for running Node.js inside Postgres
- [pgsodium](https://github.com/michelp/pgsodium): for accessing the libsodium encryption API

Before extensions can be created, they must first be installed on the filesystem of the database server, which is an important security measure because in some cases extensions may require external libraries and can interact with Postgres internals. Their installation is something that requires careful consideration.

## Trusted vs Untrusted [\#](https://supabase.com/blog/pg-tle\#trusted-vs-untrusted)

Many extensions provide functions whose implementation is written in C, and creating them in a database means that the compiled C code is “dynamically linked” into your running Postgres process. These dynamically-loaded libraries can now access every aspect of your running database process, right down to raw memory. They are essentially database superusers on steroids. Because of this, C is an “untrusted language” and installing extensions written in C requires filesystem access.

However there are several _trusted_ languages in Postgres that don’t provide raw access to process memory, the filesytem, or other system functions. These languages obey the security rules of Postgres. The most obvious example of these trusted languages is SQL itself. Another built-in trusted language in Postgres is called [pl/pgsql](https://www.postgresql.org/docs/current/plpgsql.html). It looks a lot like SQL but with some imperative programming features like `IF` blocks and `FOR` loops. The aforementioned plv8 is also a trusted language, as are the languages [pl/perl](https://www.postgresql.org/docs/current/plperl.html) and [pl/tcl](https://www.postgresql.org/docs/current/pltcl.html). Other languages like [pl/python](https://www.postgresql.org/docs/current/plpython.html) are **_not_** trusted because of the way they are integrated into Postgres, they do not obey the “rules” of Postgres security, and so are not included in most cloud provider platforms since they would allow database users to effectively act as a superuser.

## Trusted Language Extensions [\#](https://supabase.com/blog/pg-tle\#trusted-language-extensions)

Near the end of 2022, we got a surprise gift from the team at Amazon Web Services, a new Postgres extension called `pg_tle`, that allows you to **Trusted Language Extensions (TLEs).** A TLE is just like a regular Postgres extension, except that **does not need to be installed on the server filesystem** it is written in a **trusted language** you can install extensions from any database client using the function `pgtle.install_extension()`, just like you can create other objects like tables and views.

Of course, TLEs _must_ be written in trusted languages as described above, hence the name, so no extensions that are written in C can be TLEs. There are still many extensions that are already written in trusted languages, and soon many more to come with some exciting progress in more performant trusted languages like [pl/rust](https://github.com/tcdi/plrust) which recently reached an official 1.0.0 version release. By removing the constraint that extensions must be installed on the server filesystem, TLEs open up a whole new world of possibilities for packaging and distributing new and modular functionality for Postgres.

## Collaborating with AWS [\#](https://supabase.com/blog/pg-tle\#collaborating-with-aws)

Because untrusted extensions are, by nature, able to break the security rules of Postgres, cloud providers are quite conservative about what extensions to provide to their customers. New extensions are rarely adopted quickly. This slows down the speed that new software can be created and shared. Open source requires opportunity and momentum, and by closing off the opportunity for Postgres users to quickly create, install, evaluate and iterate extensions, progress is slowed. TLEs offer an opportunity for open source developers to create and share code without having to wait for cloud providers or other gatekeepers to install it.

When AWS released `pg_tle`, we realized immediately how powerful the tool is, and how it will change the way people release and install trusted extensions forever. We started collaborating with the TLE team at AWS, exchanging ideas and resources to further promote TLEs in both our database platform and theirs. By providing the TLE extension in both Supabase and AWS, we are unifying a standard package platform across two of the largest Postgres providers. We hope that other Postgres cloud providers will join the collaboration so that extension developers can leverage a large community base that greatly multiplies the reach of their efforts.

## Installing TLEs with database.dev [\#](https://supabase.com/blog/pg-tle\#installing-tles-with-databasedev)

pg\_tle is available on new Supabase projects and on Amazon RDS for Postgres 14.5 and higher. Supabase also includes an extension called [pgsql-http](https://github.com/pramsey/pgsql-http) for making HTTP calls from SQL to REST APIs. So, naturally putting two and two together, we thought it would be cool to see if it’s possible to install TLEs from a REST API using only SQL!

We've created a new package registry, dbdev, that makes it easy to install extensions in your database migrations - as easy as: `select dbdev.install('langchain-embedding_search')`.
You can read more about dbdev in our other blog post: [dbdev: a PostgreSQL Package Manager](https://supabase.com/blog/dbdev).

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-tle&text=Trusted%20Language%20Extensions%20for%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-tle&text=Trusted%20Language%20Extensions%20for%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-tle&t=Trusted%20Language%20Extensions%20for%20Postgres)

[Last post\\
\\
**Launch Week 7 Community Highlights** \\
\\
14 April 2023](https://supabase.com/blog/launch-week-7-community-highlights)

[Next post\\
\\
**Supabase Studio 2.0: help when you need it most** \\
\\
14 April 2023](https://supabase.com/blog/supabase-studio-2.0)

[launch-week](https://supabase.com/blog/tags/launch-week) [postgres](https://supabase.com/blog/tags/postgres)

On this page

- [How Postgres extensions work](https://supabase.com/blog/pg-tle#how-postgres-extensions-work)
- [Trusted vs Untrusted](https://supabase.com/blog/pg-tle#trusted-vs-untrusted)
- [Trusted Language Extensions](https://supabase.com/blog/pg-tle#trusted-language-extensions)
- [Collaborating with AWS](https://supabase.com/blog/pg-tle#collaborating-with-aws)
- [Installing TLEs with database.dev](https://supabase.com/blog/pg-tle#installing-tles-with-databasedev)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-tle&text=Trusted%20Language%20Extensions%20for%20Postgres)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-tle&text=Trusted%20Language%20Extensions%20for%20Postgres)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpg-tle&t=Trusted%20Language%20Extensions%20for%20Postgres)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)