---
url: "https://supabase.com/blog/s3-compatible-storage"
title: "Supabase Storage: now supports the S3 protocol"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Storage: now supports the S3 protocol

18 Apr 2024

•

5 minute read

[![Fabrizio Fenoglio avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ffenos.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Fabrizio FenoglioEngineering](https://github.com/fenos)

![Supabase Storage: now supports the S3 protocol](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fs3-compatible-storage%2Fthumb.png%3Fv%3D2&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase Storage is now officially an S3-Compatible Storage Provider. This is one of the most-requested features and is available today in public alpha. Resumable Uploads are also transitioning from Beta to Generally Available.

The [Supabase Storage Engine](https://github.com/supabase/storage) is fully open source and is one of the few storage solutions that offer 3 interoperable protocols to manage your files:

- [Standard uploads](https://supabase.com/docs/guides/storage/uploads/standard-uploads): simple to get started
- [Resumable uploads](https://supabase.com/docs/guides/storage/uploads/resumable-uploads): for resumable uploads with large uploads
- [S3 uploads](https://supabase.com/docs/guides/storage/s3/compatibility): for compatibility across a plethora of tools

A new way to use Supabase Storage - YouTube

Supabase

54.4K subscribers

[A new way to use Supabase Storage](https://www.youtube.com/watch?v=WvvGhcNeSPk)

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

[Watch on YouTube](https://www.youtube.com/watch?v=WvvGhcNeSPk "Watch on YouTube")

## S3 compatibility [\#](https://supabase.com/blog/s3-compatible-storage\#s3-compatibility)

We always strive to adopt industry standards at Supabase. Supporting standards makes workloads portable, [a key product principle](https://supabase.com/docs/guides/getting-started/architecture#everything-is-portable). The S3 API is undoubtedly a storage standard, and we're making it accessible to developers of various experience-levels.

The S3 protocol is backwards compatible with our other APIs. If you are already using Storage via our REST or TUS APIs, today you can use any S3 client to interact with your buckets and files: upload with TUS, serve them with REST, and manage them with the S3 protocol.

The protocol works on the cloud, local development, and self-hosting. Check out the API compatibility [in our docs](https://supabase.com/docs/guides/storage/s3/compatibility)

### Authenticating with Supabase S3 [\#](https://supabase.com/blog/s3-compatible-storage\#authenticating-with-supabase-s3)

To authenticate with Supabase S3 you have 2 options:

1. **The standard `access_key` and `secret_key` credentials.** You can generate these from the [storage settings page](https://supabase.com/dashboard/project/_/settings/storage). This authentication method is widely compatible with tools supporting the S3 protocol. It is also meant to be used _exclusively serverside_ since it provides full access to your Storage resources.

We will add scoped access key credentials in the near future which can have access to specific buckets.

2. **User-scoped credentials with RLS.** This takes advantage of a well-adopted concept across all Supabase services, [Row Level Security](https://supabase.com/docs/guides/auth/auth-deep-dive/auth-row-level-security). It allows you to interact with the S3 protocol by scoping storage operations to a particular authenticated user or role, respecting your existing RLS policies. This method is made possible by using the Session token header which the S3 protocol supports. You can find more information on how to use the Session token mechanism in the [doc](https://supabase.com/docs/guides/storage/s3/authentication#session-token).


### S3-compatible Integrations [\#](https://supabase.com/blog/s3-compatible-storage\#s3-compatible-integrations)

With the support of the S3 protocol, you can now connect Supabase Storage to many 3rd-party tools and services by providing a pair of credentials which can be revoked at any time.

You can use popular tools for backups and migrations, such as:

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/s3/): The official AWS CLI
- [rclone](https://rclone.org/): a command-line program to manage files on cloud storage.
- [Cyberduck](https://cyberduck.io/): a cloud storage browser for Mac and Windows.
- and any other s3-compatible tool ...

![Supabase Cyberduck](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fcyberduck%2Fcyberduck-files.png%3Ft%3D2024-04-18T08%253A39%253A48.575Z&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Check out our Cyberduck guide [here](https://supabase.com/partners/integrations/cyberduck).

### S3 for Data Engineers [\#](https://supabase.com/blog/s3-compatible-storage\#s3-for-data-engineers)

S3 compatibility provides a nice primitive for Data Engineers. You can use it with many popular tools:

- Data Warehouses like ClickHouse
- Query engines like DuckDB, Spark, Trino, & Snowflake External Table
- Data Loaders like Fivetran & Airbyte

In this example our incredible data analyst, Tyler, demonstrates how to store Parquet files in Supabase Storage and query them directly using DuckDB:

File-based Postgres Analytics with DuckDB and AWS S3 - YouTube

Supabase

54.4K subscribers

[File-based Postgres Analytics with DuckDB and AWS S3](https://www.youtube.com/watch?v=diL00ZZ-q50)

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

[Watch on YouTube](https://www.youtube.com/watch?v=diL00ZZ-q50 "Watch on YouTube")

### Multipart Uploads in S3 [\#](https://supabase.com/blog/s3-compatible-storage\#multipart-uploads-in-s3)

In addition to the standard uploads and resumable uploads, we now support multipart uploads via the S3 protocol.
This allows you to maximize upload throughput by uploading chunks in parallel, which are then concatenated at the end.

# Resumable uploads is Generally Available [\#](https://supabase.com/blog/s3-compatible-storage\#resumable-uploads-is-generally-available)

Along with the [platform GA announcement](https://supabase.com/ga), we are also thrilled to announce that resumable uploads are also generally available.

Resumable uploads are powered by the [TUS protocol](https://tus.io/). The journey to get here was immensely rewarding, working closely with the TUS team. A big shoutout to the maintainers of the TUS protocol, [@murderlon](https://github.com/Murderlon) and [@acconut](https://github.com/Acconut), for their collaborative approach to open source.

Supabase contributed [some advanced features](https://github.com/tus/tus-node-server/pulls?q=is%3Apr+sort%3Aupdated-desc+author%3Afenos) from the Node implementation of TUS Spec including [distributed locks](https://github.com/tus/tus-node-server/pull/514), [max file size](https://github.com/tus/tus-node-server/pull/517), [expiration extension](https://github.com/tus/tus-node-server/pull/513) and numerous bug fixes:

![Supabase contributions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fs3-compatible-storage%2Fsupabase-contributions.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

These features were essential for Supabase, and since the [TUS node server](https://github.com/tus/tus-node-server) is open source, they are also available for you to use. This is another core principle: wherever possible, we [use and support existing tools](https://supabase.com/docs/guides/getting-started/architecture#support-existing-tools) rather than developing from scratch.

- **Cross-bucket transfers:** We have added the availability to copy and move objects across buckets, where previously you could do these operations only within the same Supabase bucket.
- **Standardized error codes:** Error codes have now been standardized across the Storage server and now will be much easier to branch logic on specific errors. You can find the list of error codes [here](https://supabase.com/docs/guides/storage/debugging/error-codes).
- **Multi-tenant migrations:** We made significant improvements to the running migrations across all our tenants. This has reduced migration errors across the fleet and enables us to run long running migrations in an asynchronous manner. Stay tuned for a separate blog post with more details.
- **Decoupled dependencies:** Storage is fully decoupled from other Supabase products, which means you can run Storage as a standalone service. Get started with this [docker-compose file](https://github.com/supabase/storage/blob/master/docker-compose.yml).

# Getting started [\#](https://supabase.com/blog/s3-compatible-storage\#getting-started)

- Check out the S3 API compatibility [in our docs](https://supabase.com/docs/guides/storage/s3/compatibility)
- Request a feature on the [Storage Github repo](https://github.com/supabase/storage)
- Learn about [S3 Authentication](https://supabase.com/docs/guides/storage/s3/authentication)
- Try S3 with Cyberduck: follow our [integration guide](https://supabase.com/partners/integrations/cyberduck)
- Try S3 with DuckDB: follow the guide [on YouTube](https://www.youtube.com/watch?v=diL00ZZ-q50)

[![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-black.svg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-white.svg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)Week](https://supabase.com/ga-week)

15-19 April

[Day 1 -Supabase is officially launching into General Availability](https://supabase.com/ga)

[Day 2 -Supabase Functions now supports AI models](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions)

[Day 3 -Supabase Auth now supports Anonymous sign-ins](https://supabase.com/blog/anonymous-sign-ins)

[Day 4 -Supabase Storage: now supports the S3 protocol](https://supabase.com/blog/s3-compatible-storage)

[Day 5 -Supabase Security Advisor & Performance Advisor](https://supabase.com/blog/security-performance-advisor)

Build Stage

[01 -PostgreSQL Index Advisor](https://github.com/supabase/index_advisor)

[02 -Branching now Publicly Available](https://supabase.com/blog/branching-publicly-available)

[03 -Oriole joins Supabase](https://supabase.com/blog/supabase-acquires-oriole)

[04 -Supabase on AWS Marketplace](https://supabase.com/blog/supabase-aws-marketplace)

[05 -Supabase Bootstrap](https://supabase.com/blog/supabase-bootstrap)

[06 -Supabase Swift](https://supabase.com/blog/supabase-swift)

[07 -Top 10 Launches from Supabase GA Week](https://supabase.com/blog/ga-week-summary)

[Open Source Hackathon 2024](https://supabase.com/blog/supabase-oss-hackathon)

[Community Meetups](https://supabase.com/ga-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fs3-compatible-storage&text=Supabase%20Storage%3A%20now%20supports%20the%20S3%20protocol)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fs3-compatible-storage&text=Supabase%20Storage%3A%20now%20supports%20the%20S3%20protocol)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fs3-compatible-storage&t=Supabase%20Storage%3A%20now%20supports%20the%20S3%20protocol)

[Last post\\
\\
**Packaging Supabase with Nix** \\
\\
25 April 2024](https://supabase.com/blog/nix-postgres)

[Next post\\
\\
**Top 10 Launches from Supabase GA Week** \\
\\
18 April 2024](https://supabase.com/blog/ga-week-summary)

[launch-week](https://supabase.com/blog/tags/launch-week) [storage](https://supabase.com/blog/tags/storage)

On this page

- [S3 compatibility](https://supabase.com/blog/s3-compatible-storage#s3-compatibility)
  - [Authenticating with Supabase S3](https://supabase.com/blog/s3-compatible-storage#authenticating-with-supabase-s3)
  - [S3-compatible Integrations](https://supabase.com/blog/s3-compatible-storage#s3-compatible-integrations)
  - [S3 for Data Engineers](https://supabase.com/blog/s3-compatible-storage#s3-for-data-engineers)
  - [Multipart Uploads in S3](https://supabase.com/blog/s3-compatible-storage#multipart-uploads-in-s3)

- [Resumable uploads is Generally Available](https://supabase.com/blog/s3-compatible-storage#resumable-uploads-is-generally-available)
- [Getting started](https://supabase.com/blog/s3-compatible-storage#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fs3-compatible-storage&text=Supabase%20Storage%3A%20now%20supports%20the%20S3%20protocol)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fs3-compatible-storage&text=Supabase%20Storage%3A%20now%20supports%20the%20S3%20protocol)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fs3-compatible-storage&t=Supabase%20Storage%3A%20now%20supports%20the%20S3%20protocol)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)