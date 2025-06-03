---
url: "https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm"
title: "Postgres Foreign Data Wrappers with Wasm"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Postgres Foreign Data Wrappers with Wasm

16 Aug 2024

•

8 minute read

[![Bo Lu avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fburmecia.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Bo LuEngineering](https://github.com/burmecia)

![Postgres Foreign Data Wrappers with Wasm](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fthumb_FDW-with-WASM.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Foreign Data Wrappers (FDWs) allow Postgres to interact with externally hosted data. To operate a FDW, the user creates a foreign table. When queried, the foreign table reaches out to the 3rd party service, collects the requested data, and returns it to the query in the shape defined by the foreign table. This allows seamless querying and data manipulation across different tools as if they were local tables from within Postgres.

[Wrappers](https://github.com/supabase/wrappers) is a Rust framework for creating Postgres Foreign Data Wrappers. Today we're releasing support for [Wasm (WebAssembly)](https://webassembly.org/) wrappers.

With this feature, anyone can create a Wasm wrapper to an external service and run it directly from e.g. GitHub:

`
-- An Example Google Sheets Wasm Wrapper:
create server google_sheets
foreign data wrapper wasm_wrapper
options (
    -- Install from GitHub
    fdw_package_url 'https://github.com/<ORG>/<REPO>/releases/download/v0.2.0/google_sheets_fdw.wasm',
    fdw_package_name 'my-company:google-sheets-fdw',
    fdw_package_version '0.2.0',
    fdw_package_checksum '338674c4c983aa6dbc2b6e63659076fe86d847ca0da6d57a61372b44e0fe4ac9',
	-- Provide custom options
	base_url 'https://docs.google.com/spreadsheets/d'
);
`

This feature is available today in public alpha for all new projects.

You don't need a Database - use this instead! - YouTube

Supabase

54.4K subscribers

[You don't need a Database - use this instead!](https://www.youtube.com/watch?v=wCwEWR4k0no)

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

[Watch on YouTube](https://www.youtube.com/watch?v=wCwEWR4k0no "Watch on YouTube")

## What are Foreign Data Wrappers? [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#what-are-foreign-data-wrappers)

[Foreign Data Wrappers (FDW)](https://wiki.postgresql.org/wiki/Foreign_data_wrappers) are a powerful feature of Postgres that allows you to connect to and query external data sources as if they were regular tables.

![Foreign Data Wrappers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2FFDW.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[Wrappers](https://github.com/supabase/wrappers) is an open source project that simplifies the creation of Postgres Foreign Data Wrappers using [Rust](https://www.rust-lang.org/).

## Why WebAssembly? [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#why-webassembly)

[WebAssembly (Wasm)](https://webassembly.org/) is a binary instruction format that enables secure and high-performance execution of code on the web. It is originally designed for web browsers, but now can also be used in server-side environments like Postgres.

Here's how the Wasm FDW benefits us:

- **Improved Security:** Wasm's sandboxed execution runtime with minimum interfaces enhances the security of FDW.
- **Simplified Development:** Developers can use [Rust](https://www.rust-lang.org/) to create complex FDWs without diving deep into Postgres internal API.
- **Simplified Distribution:** Easily distribute your Wasm FDW through any URL-accessible storage (such as GitHub or S3).
- **Enhanced Performance:** Wasm's near-native speed ensures FDWs operate with minimal overhead.
- **Increased Modularity:** Each Wasm FDW is an isolated package which is dynamically loaded and executed by Wrappers individually.

## Architecture [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#architecture)

To better understand how the Wasm FDW works, let's take a look at the architecture:

![Wasm FDW architecture](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2FFDW-architecture.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The above diagram illustrates the key components and how they interact:

1. **Supabase Wrappers Extension (Host):** This is the core component that runs within Postgres. It includes below modules:
   - **Wasm Runtime:** Provides runtime environment to executes the Wasm FDW package.
   - **HTTP Interface:** Manages communication with external data sources through HTTP.
   - **Utilities:** Helper tools and functions to support FDW operations.
   - Other modules providing specific functionalities, such like JWT, stats and etc.
2. **Wasm FDWs (Guests):** Isolated, dynamically-loaded Wasm packages that perform data fetching and processing. They execute in a sandboxed environment to ensure security and performance. For example:
   - **Snowflake Wasm FDW:** A foreign data wrapper specifically designed to interact with [Snowflake](https://www.snowflake.com/).
   - **Paddle Wasm FDW:** Another FDW example, tailored for [Paddle](https://www.paddle.com/) integration.
3. **Web Storage:** Represents external storage services like [GitHub](https://github.com/) or [S3](https://aws.amazon.com/s3/), where Wasm packages can be publicly stored and downloaded from.
4. **External Data Source:** Various external systems which data is fetched from or pushed to, such as [Snowflake](https://www.snowflake.com/) and [Paddle](https://www.paddle.com/). Data is accessed using RESTful APIs.

## Data fetching [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#data-fetching)

Wasm FDWs are loaded dynamically when the first request is made. The interaction flow is:

1. **Wasm download:** The Wasm FDWs are dynamically downloaded from web storage services, like GitHub or S3, and cached locally. This happens the first time the `SELECT` statement is initiated.
2. **Initialization and Execution:** Once downloaded, the Wasm FDWs are initialized and executed within the embedded Wasm runtime environment. This provides a secure, sandboxed execution environment that isolates the packages from the main Postgres system.
3. **Data Fetching via RESTful API:** The Wasm FDWs interact with their respective external data sources via RESTful APIs.
4. **Query Handling and Data Integration:** When a query is executed against a foreign table in Postgres, the Supabase Wrappers extension invokes the appropriate Wasm FDW, fetches data from the external source, processes it, and returns it to the Supabase Wrappers, which integrates it back into the Postgres query execution pipeline.

The Wasm FDW currently only supports data sources which have HTTP(s) based JSON API, other sources such like TCP/IP based DBMS or local files are not supported yet.

## Developing your own Wasm FDW [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#developing-your-own-wasm-fdw)

A major benefit of Wasm FDW is that you can build your own FDW and use it on Supabase. To get started, clone the [Postgres Wasm FDW \[Template\]](https://github.com/supabase-community/postgres-wasm-fdw). Building your own Wasm FDWs opens up a world of possibilities for integrating diverse data sources into Postgres.

Visit [Wrappers docs and guides](https://fdw.dev/guides/create-wasm-wrapper/) to learn more about how to develop a Wasm FDW.

As the Wasm FDW can access external data sources, you should never install Wasm Wrappers from untrusted source. Always use official Supabase FDWs, or use sources which you have full visibility and control.

## Try it now on Supabase [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#try-it-now-on-supabase)

The Wasm FDW feature is available today on the Supabase platform. We have 2 new built-in Wasm FDWs: [Snowflake](https://supabase.com/docs/guides/database/extensions/wrappers/snowflake) and [Paddle](https://supabase.com/docs/guides/database/extensions/wrappers/paddle).

To get started, follow below steps:

1. Create a new Supabase project: [database.new](http://database.new/)
2. Navigate to the [Database -> Wrappers](https://supabase.com/dashboard/project/_/database/wrappers) section and enable Wrappers.
3. Add `Snowflake` or `Paddle` wrapper, follow the instructions and create foreign tables.

![Supabase Dashboard Wrappers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fdashboard-wrappers.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We can also use SQL. Let's try, using the Paddle FDW as an example.

### Enable Wasm Wrappers [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#enable-wasm-wrappers)

Inside the [SQL editor](https://supabase.com/dashboard/project/_/sql/new), enable the Wasm Wrapper feature:

`
-- install Wrappers extension
create extension if not exists wrappers with schema extensions;
-- create Wasm foreign data wrapper
create foreign data wrapper wasm_wrapper
handler wasm_fdw_handler
validator wasm_fdw_validator;
`

### Get your Paddle credentials [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#get-your-paddle-credentials)

Sign up for [a sandbox account](https://developer.paddle.com/api-reference/overview#base-url) and [get API key](https://sandbox-vendors.paddle.com/authentication-v2) with Paddle.

### Save your Paddle credentials [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#save-your-paddle-credentials)

Create a Paddle server in Postgres using the Wasm FDW created above:

`
-- create Paddle foreign server
create server paddle_server
foreign data wrapper wasm_wrapper
options (
    -- check all available versions at
    -- https://fdw.dev/catalog/paddle/#available-versions
    fdw_package_url 'https://github.com/supabase/wrappers/releases/download/wasm_paddle_fdw_v0.1.1/paddle_fdw.wasm',
    fdw_package_name 'supabase:paddle-fdw',
    fdw_package_version '0.1.1',
    fdw_package_checksum 'c5ac70bb2eef33693787b7d4efce9a83cde8d4fa40889d2037403a51263ba657',
    -- save your Paddle credentials
    api_url 'https://sandbox-api.paddle.com',
    api_key '<your Paddle sandbox API key>'
);
`

### Set up your Foreign Tables [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#set-up-your-foreign-tables)

Create a table for Paddle data:

`
-- create dedicated schema for Paddle foreign tables
create schema if not exists paddle;
-- create foreign table
create foreign table paddle.customers (
id text,
name text,
email text,
status text,
custom_data jsonb,
created_at timestamp,
updated_at timestamp,
attrs jsonb
)
server paddle_server
options (
object 'customers',
rowid_column 'id'
);
`

### Query Paddle from Postgres [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#query-paddle-from-postgres)

Now let's query the foreign table and check the result:

`
select id, name, email, status
from paddle.customers;
`

![Paddle FDW Output](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fpaddle-fdw-output.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

That's it. Head over to the [Supabase Wrappers documentation](https://fdw.dev/) to find more detailed guides on setting up and using Wasm FDWs.

## Thanks to our community contributors [\#](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm\#thanks-to-our-community-contributors)

None of this innovation would have been possible without the relentless efforts and contributions of our vibrant community. We'd like to thank all the following developers for their contributions:

[Aayushya Vajpayee](https://github.com/AayushyaVajpayee), [Romain Graux](https://github.com/romaingrx)

Want to join the Supabase Wrappers community contributors? [Check out our contribution docs](https://fdw.dev/contributing/core/).

[Launch Week12](https://supabase.com/launch-week/12)

12-16 August

[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)

[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)

[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)

[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)

[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage

[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)

[02 -pg\_replicate](https://news.ycombinator.com/item?id=41209994)

[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)

[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)

[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)

[06 -vec2pg](https://supabase.com/blog/vec2pg)

[07 -pg\_graphql](https://supabase.com/blog/pg-graphql-1-5-7)

[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)

[09 -python-support](https://supabase.com/blog/python-support)

[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)

[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-foreign-data-wrappers-with-wasm&text=Postgres%20Foreign%20Data%20Wrappers%20with%20Wasm)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-foreign-data-wrappers-with-wasm&text=Postgres%20Foreign%20Data%20Wrappers%20with%20Wasm)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-foreign-data-wrappers-with-wasm&t=Postgres%20Foreign%20Data%20Wrappers%20with%20Wasm)

[Last post\\
\\
**Introducing New Platform Access Control** \\
\\
16 August 2024](https://supabase.com/blog/platform-access-control)

[Next post\\
\\
**PostgREST 12.2: Prometheus metrics** \\
\\
16 August 2024](https://supabase.com/blog/postgrest-12-2)

[launch-week](https://supabase.com/blog/tags/launch-week) [wasm](https://supabase.com/blog/tags/wasm) [wrappers](https://supabase.com/blog/tags/wrappers)

On this page

- [What are Foreign Data Wrappers?](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#what-are-foreign-data-wrappers)
- [Why WebAssembly?](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#why-webassembly)
- [Architecture](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#architecture)
- [Data fetching](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#data-fetching)
- [Developing your own Wasm FDW](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#developing-your-own-wasm-fdw)
- [Try it now on Supabase](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#try-it-now-on-supabase)
  - [Enable Wasm Wrappers](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#enable-wasm-wrappers)
  - [Get your Paddle credentials](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#get-your-paddle-credentials)
  - [Save your Paddle credentials](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#save-your-paddle-credentials)
  - [Set up your Foreign Tables](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#set-up-your-foreign-tables)
  - [Query Paddle from Postgres](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#query-paddle-from-postgres)
- [Thanks to our community contributors](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm#thanks-to-our-community-contributors)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-foreign-data-wrappers-with-wasm&text=Postgres%20Foreign%20Data%20Wrappers%20with%20Wasm)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-foreign-data-wrappers-with-wasm&text=Postgres%20Foreign%20Data%20Wrappers%20with%20Wasm)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fpostgres-foreign-data-wrappers-with-wasm&t=Postgres%20Foreign%20Data%20Wrappers%20with%20Wasm)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Wasm FDW architecture](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2FFDW-architecture.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Paddle FDW Output](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fpaddle-fdw-output.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Foreign Data Wrappers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2FFDW.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Supabase Dashboard Wrappers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fdashboard-wrappers.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)