---
url: "https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio"
title: "NoSQL Postgres: Add MongoDB compatibility to your Supabase projects with FerretDB"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# NoSQL Postgres: Add MongoDB compatibility to your Supabase projects with FerretDB

31 Jan 2024

•

6 minute read

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![NoSQL Postgres: Add MongoDB compatibility to your Supabase projects with FerretDB](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fgetting-started%2Fferretdb%2Fferretdb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[FerretDB](https://www.ferretdb.com/) is an open source document database that adds MongoDB compatibility to other database backends, such as [Postgres](https://www.postgresql.org/) and [SQLite](https://www.sqlite.org/).
By using FerretDB, developers can [access familiar MongoDB features and tools using the same syntax and commands](https://blog.ferretdb.io/mongodb-crud-operations-with-ferretdb/) for many of their use cases.

In this post, we'll start from scratch, running FerretDB locally via Docker, trying out the connection with `mongosh` and the MongoDB Node.js client, and finally deploy FerretDB to [Fly.io](https://fly.io/) for a production ready set up.

If you prefer video guide, you can follow along below. And make sure to subscribe to the [Supabase YouTube channel](https://www.youtube.com/channel/UCNTVzV1InxHV-YR0fSajqPQ?view_as=subscriber&sub_confirmation=1)!

Add MongoDB compatibility to Postgres with FerretDB - NoSQL Postgres - YouTube

Supabase

54.4K subscribers

[Add MongoDB compatibility to Postgres with FerretDB - NoSQL Postgres](https://www.youtube.com/watch?v=8EKi2dV51TY)

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

[Watch on YouTube](https://www.youtube.com/watch?v=8EKi2dV51TY "Watch on YouTube")

## Prerequisites [\#](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio\#prerequisites)

- A Supabase project. Create yours here: [database.new](https://database.new/).
- [Docker](https://www.docker.com/) or [Orbstack](https://orbstack.dev/).
- \[Optional\] A [Fly.io](https://fly.io/) account for production deployment.

## Run FerretDB locally with Docker [\#](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio\#run-ferretdb-locally-with-docker)

FerretDB provides a [Docker image](https://github.com/ferretdb/FerretDB/pkgs/container/ferretdb) allowing us to run it locally, for example via [Orbstack](https://orbstack.dev/), with a couple simple commands.

FerretDB only requires the Postgres database URI to be provided as the `FERRETDB_POSTGRESQL_URL` environment variable. Every Supabase project comes with a full Postgres database. You can find the connection URI string in your [Supabase Dashboard](https://supabase.com/dashboard/project/_/settings/database).

Make sure **Use connection pooling** is checked and **Session mode** is selected. Then copy the URI. Replace the password placeholder with your saved database password.

If your network supports IPv6 connections, you can also use the direct connection string. Uncheck **Use connection pooling** and copy the new URI.

Terminal

`
# Set the required environment variables
export DB_USER=postgres
export DB_PASSWORD=<your db password>
export SUPA_PROJECT_REF=<your Supabase project ref>
export SUPA_REGION=<your project region>
export DB_URL=postgres://$DB_USER.$SUPA_PROJECT_REF:$DB_PASSWORD@$SUPA_REGION.pooler.supabase.com:5432/postgres
# Run FerretDB in docker container
docker run -p 27017:27017 -p 8080:8080 -e FERRETDB_POSTGRESQL_URL=$DB_URL ghcr.io/ferretdb/ferretdb
`

FerretDB runs on the default MongoDB port `27017` and also spins up some monitoring tools on port `8080`. Once up and running you can access these at [localhost:8080](http://localhost:8080/).

Once up and running, constructing the MongoDB URI is easil:

Terminal

`
export MONGODB_URL=mongodb://$DB_USER.$SUPA_PROJECT_REF:$DB_PASSWORD@127.0.0.1:27017/ferretdb?authMechanism=PLAIN
`

## Test with `mongosh` [\#](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio\#test-with-mongosh)

If you have MongoDB installed locally on your machine, you can test via `mongosh`, the MongoDB shell.

Terminal

`
mongosh '$MONGODB_URL'
`

If you don't have MongoDB installed locally, you can run the shell via a Docker container:

Terminal

`
docker run --rm -it --entrypoint=mongosh mongo \
"$MONGODB_URL"
`

### Insert documents into FerretDB [\#](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio\#insert-documents-into-ferretdb)

With `mongosh` running, let's try to insert some documents into our FerretDB instance.
You are going to insert two footballer data into a `players` collection.

ferretdb>

`
db.players.insertMany([\
{\
       futbin_id: 3,\
       player_name: "Giggs",\
       player_extended_name: "Ryan Giggs",\
       quality: "Gold - Rare",\
       overall: 92,\
       nationality: "Wales",\
       position: "LM",\
       pace: 90,\
       dribbling: 91,\
       shooting: 80,\
       passing: 90,\
       defending: 44,\
       physicality: 67\
},\
{\
       futbin_id: 4,\
       player_name: "Scholes",\
       player_extended_name: "Paul Scholes",\
       quality: "Gold - Rare",\
       overall: 91,\
       nationality: "England",\
       position: "CM",\
       pace: 72,\
       dribbling: 80,\
       shooting: 87,\
       passing: 91,\
       defending: 64,\
       physicality: 82,\
       base_id: 246\
}\
]);
`

Great!
Now when you run `db.players.find()`, it should return all the documents stored in the collection.

### Update document record in FerretDB [\#](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio\#update-document-record-in-ferretdb)

Next, you need to update "Giggs" record to reflect his current position as a `CM`.
To do this, we can just run an `updateOne` command to target just that particular player:

ferretdb>

`
db.players.updateOne(
    { player_name: "Giggs" },
    { $set: { position: "CM" } }
);
`

Let's query the collection to see if the changes have been made:

ferretdb>

`
db.players.find({player_name: "Giggs"})
`

You can run many MongoDB operations on FerretDB. See the [list of supported commands](https://docs.ferretdb.io/reference/supported-commands/) in the FerretDB documentation for more.

## Inspect the JSONB data in the Supabase Dashboard [\#](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio\#inspect-the-jsonb-data-in-the-supabase-dashboard)

FerretDB stores each collection in a table on the `ferretdb` schema, each document represented by a JSONB entry. You can inspect this in the [Table Editor](https://supabase.com/dashboard/project/_/editor) in your Supabase Dashboard.

![Supabase Dashboard Table Editor Screenshot](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fgetting-started%2Fferretdb%2Ftable-editor.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Deploy to Fly.io [\#](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio\#deploy-to-flyio)

For production use cases, you can easily deploy FerretDB on Fly. Simply create a `fly.toml` file (make sure to [update `primary_region`](https://fly.io/docs/reference/regions/))

fly.toml

`
app = "supa-ferretdb-<your-supabase-project-ref>"
primary_region = "bos"
[build]
image = "ghcr.io/ferretdb/ferretdb"
[[services]]
internal_port = 27017
protocol = "tcp"
[[services.ports]]
    port = "27017"
[[vm]]
cpu_kind = "shared"
cpus = 1
memory_mb = 1024
`

And follow these [flyctl](https://fly.io/docs/hands-on/install-flyctl/) commands:

- fly launch --no-deploy
  - An existing fly.toml file was found for app supa-ferretdb?
  - Would you like to copy its configuration to the new app? (y/N) > y
- fly secrets set FERRETDB\_POSTGRESQL\_URL=$DB\_URL
- fly deploy
- fly ips allocate-v4
  - Note: this is a paid feature! You can test it for free as long as you [release the dedicated IPv4](https://community.fly.io/t/we-are-going-to-start-charging-for-dedicated-ipv4-in-january-1st/15970#how-not-to-be-billed-2) before the end of the billing period!

Now simply replace `127.0.0.1` in the `MONGODB_URL` with your dedicated IPv4 address and you're ready to roll!

## Conclusion [\#](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio\#conclusion)

FerretDB allows you to run MongoDB workloads on Postgres and SQLite. This flexibility means you can easily add MongoDB compatibility to your Supabase projects, while avoiding vendor lock-in and retaining control of your data architecture.

To get started with FerretDB, check out the [FerretDB quickstart guide](https://docs.ferretdb.io/quickstart-guide/).

## More Supabase [\#](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio\#more-supabase)

- [Migration guides](https://supabase.com/docs/guides/resources#migrate-to-supabase)
- [Options for connecting to your Postgres database](https://supabase.com/docs/guides/database/connecting-to-postgres)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnosql-mongodb-compatibility-with-ferretdb-and-flydotio&text=NoSQL%20Postgres%3A%20Add%20MongoDB%20compatibility%20to%20your%20Supabase%20projects%20with%20FerretDB)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnosql-mongodb-compatibility-with-ferretdb-and-flydotio&text=NoSQL%20Postgres%3A%20Add%20MongoDB%20compatibility%20to%20your%20Supabase%20projects%20with%20FerretDB)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnosql-mongodb-compatibility-with-ferretdb-and-flydotio&t=NoSQL%20Postgres%3A%20Add%20MongoDB%20compatibility%20to%20your%20Supabase%20projects%20with%20FerretDB)

[Last post\\
\\
**Matryoshka embeddings: faster OpenAI vector search using Adaptive Retrieval** \\
\\
13 February 2024](https://supabase.com/blog/matryoshka-embeddings)

[Next post\\
\\
**pgvector 0.6.0: 30x faster with parallel index builds** \\
\\
30 January 2024](https://supabase.com/blog/pgvector-fast-builds)

[postgres](https://supabase.com/blog/tags/postgres) [developers](https://supabase.com/blog/tags/developers) [mongodb](https://supabase.com/blog/tags/mongodb)

On this page

- [Prerequisites](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio#prerequisites)
- [Run FerretDB locally with Docker](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio#run-ferretdb-locally-with-docker)
- [Test with `mongosh`](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio#test-with-mongosh)
  - [Insert documents into FerretDB](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio#insert-documents-into-ferretdb)
  - [Update document record in FerretDB](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio#update-document-record-in-ferretdb)
- [Inspect the JSONB data in the Supabase Dashboard](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio#inspect-the-jsonb-data-in-the-supabase-dashboard)
- [Deploy to Fly.io](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio#deploy-to-flyio)
- [Conclusion](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio#conclusion)
- [More Supabase](https://supabase.com/blog/nosql-mongodb-compatibility-with-ferretdb-and-flydotio#more-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnosql-mongodb-compatibility-with-ferretdb-and-flydotio&text=NoSQL%20Postgres%3A%20Add%20MongoDB%20compatibility%20to%20your%20Supabase%20projects%20with%20FerretDB)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fnosql-mongodb-compatibility-with-ferretdb-and-flydotio&text=NoSQL%20Postgres%3A%20Add%20MongoDB%20compatibility%20to%20your%20Supabase%20projects%20with%20FerretDB)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fnosql-mongodb-compatibility-with-ferretdb-and-flydotio&t=NoSQL%20Postgres%3A%20Add%20MongoDB%20compatibility%20to%20your%20Supabase%20projects%20with%20FerretDB)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)