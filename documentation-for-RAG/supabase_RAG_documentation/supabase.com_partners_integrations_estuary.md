---
url: "https://supabase.com/partners/integrations/estuary"
title: "Estuary | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Estuary](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Festuary%2Festuary_logo.jpeg&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Estuary

![Estuary](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Festuary%2Festuary_updated.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

Analytics for your Supabase data. Estuary helps seamlessly migrate your data from Firestore to a Supabase Postgres database.

Estuary Flow: Extracting Data from Supabase for analytics in Snowflake

![](https://cdn.loom.com/avatars/15652856_55024652c70443868677335f1f559c12_192.jpg)

[Estuary Flow: Extracting Data from Supabase for analytics in Snowflake](https://www.loom.com/share/a8eb6fa3bece4f89835c778011637a6c?source=embed_watch_on_loom_cta&t=0 "Estuary Flow: Extracting Data from Supabase for analytics in Snowflake")

3 min

151 views

0

[Open video in Loom](https://www.loom.com/share/a8eb6fa3bece4f89835c778011637a6c?source=embed_watch_on_loom_cta&t=0 "Open video in Loom")

1.2×

2 min 40 sec⚡️3 min 20 sec2 min 40 sec2 min 13 sec1 min 47 sec1 min 34 sec1 min 20 sec1 min 4 sec

Powered by

👍

Sourabh Gupta

Introduction

Your user agent does not support the HTML5 Video element.

![](https://cdn.loom.com/avatars/15652856_55024652c70443868677335f1f559c12_192.jpg)

[Estuary Flow: Extracting Data from Supabase for analytics in Snowflake](https://www.loom.com/share/a8eb6fa3bece4f89835c778011637a6c?source=embed_watch_on_loom_cta&t=0 "Estuary Flow: Extracting Data from Supabase for analytics in Snowflake")

3 min

151 views

0

[Open video in Loom](https://www.loom.com/share/a8eb6fa3bece4f89835c778011637a6c?source=embed_watch_on_loom_cta&t=0 "Open video in Loom")

1.2×

2 min 40 sec⚡️3 min 20 sec2 min 40 sec2 min 13 sec1 min 47 sec1 min 34 sec1 min 20 sec1 min 4 sec

Powered by

👍

Sourabh Gupta

Introduction

Estuary is a real-time data pipeline platform, enabling seamless capture from sources, historical backfill and real-time synchronization between sources and destinations. This makes it simple to continuously extract data from Supabase for analytics or creating data products.

## Benefits

As a real-time platform, Estuary continuously extracts data from sources like Supabase using CDC.  This has a few main benefits:

- Access real-time analytics in your warehouse or destination of choice
- Least impact on your Supabase DB
- The ability to push to any destination that either Estuary or Kafka Connect and push to

## Overview

Details on how to use Estuary's Supabase specific connector can be found [here](https://docs.estuary.dev/reference/Connectors/capture-connectors/PostgreSQL/Supabase/).  Setting up Estuary is straightforward and has a few main requirements:

1. Create a free account [here](https://dashboard.estuary.dev/register).  Note that Estuary provides lifetime free service for anyone whose monthly usage is less than 10 GB and 2 connectors.  A 30 day free trial is automatically applied for accounts that exceed that usage.
2. Capture data from your Supabse instance using the [relevant documentation](https://docs.estuary.dev/reference/Connectors/capture-connectors/PostgreSQL/Supabase/).  Note that you will need to create a dedicated IPV4 address to use as your hostname within Estuary.
3. Push that data to your destination of choice.  Example docs for Snowflake can be found [here](https://docs.estuary.dev/reference/Connectors/materialization-connectors/Snowflake/).

## Detailed Documentation

### Prerequisites

You'll need a Supabase PostgreSQL database setup with the following:

- A Supabase IPV4 address. This can be configured under "Project Settings" -> "Add ons" within Supabase's UI.
- [Logical replication enabled](https://www.postgresql.org/docs/current/runtime-config-wal.html) - `wal_level=logical`
- [User role](https://www.postgresql.org/docs/current/sql-createrole.html) with `REPLICATION` attribute
- A [replication slot](https://www.postgresql.org/docs/current/warm-standby.html#STREAMING-REPLICATION-SLOTS). This represents a "cursor" into the PostgreSQL write-ahead log from which change events can be read.
  - Optional; if none exist, one will be created by the connector.
  - If you wish to run multiple captures from the same database, each must have its own slot. You can create these slots yourself, or by specifying a name other than the default in the advanced [configuration](https://docs.estuary.dev/reference/Connectors/capture-connectors/PostgreSQL/Supabase/#configuration).
- A [publication](https://www.postgresql.org/docs/current/sql-createpublication.html). This represents the set of tables for which change events will be reported.
  - In more restricted setups, this must be created manually, but can be created automatically if the connector has suitable permissions.
- A watermarks table. The watermarks table is a small "scratch space" to which the connector occasionally writes a small amount of data to ensure accuracy when backfilling preexisting table contents.
  - In more restricted setups, this must be created manually, but can be created automatically if the connector has suitable permissions.

#### Configuration Tip

To configure this connector to capture data from databases hosted on your internal network, you must set up SSH tunneling. For more specific instructions on setup, see [configure connections with SSH tunneling](https://docs.estuary.dev/guides/connect-network/).

### Setup

The simplest way to meet the above prerequisites is to change the WAL level and have the connector use a database superuser role.

For a more restricted setup, create a new user with just the required permissions as detailed in the following steps:

1. Connect to your instance and create a new user and password:



`
CREATE USER flow_capture WITH PASSWORD 'secret' REPLICATION;
`

2. Assign the appropriate role.

a. If using PostgreSQL v14 or later:



`
GRANT pg_read_all_data TO flow_capture;
`



b. If using an earlier version:



`
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES to flow_capture;
GRANT SELECT ON ALL TABLES IN SCHEMA public, <other_schema> TO flow_capture;
GRANT SELECT ON ALL TABLES IN SCHEMA information_schema, pg_catalog TO flow_capture;
`



where `<other_schema>` lists all schemas that will be captured from.

INFO

If an even more restricted set of permissions is desired, you can also grant SELECT on just the specific table(s) which should be captured from. The 'information\_schema' and 'pg\_catalog' access is required for stream auto-discovery, but not for capturing already configured streams.

3. Create the watermarks table, grant privileges, and create publication:


`
CREATE TABLE IF NOT EXISTS public.flow_watermarks (slot TEXT PRIMARY KEY, watermark TEXT);
GRANT ALL PRIVILEGES ON TABLE public.flow_watermarks TO flow_capture;
CREATE PUBLICATION flow_publication;
ALTER PUBLICATION flow_publication SET (publish_via_partition_root = true);
ALTER PUBLICATION flow_publication ADD TABLE public.flow_watermarks, <other_tables>;
`

where `<other_tables>` lists all tables that will be captured from. The `publish_via_partition_root` setting is recommended (because most users will want changes to a partitioned table to be captured under the name of the root table) but is not required.

4. Set WAL level to logical:

`
ALTER SYSTEM SET wal_level = logical;
`

5. Restart PostgreSQL to allow the WAL level change to take effect.

## Resources

For more information, visit the [Flow docs](https://docs.estuary.dev/). In particular:

- [Guide to create a Data Flow](https://docs.estuary.dev/guides/create-dataflow/)
- [Firestore capture connector](https://docs.estuary.dev/reference/Connectors/capture-connectors/google-firestore/)
- [Postgres materializaiton connector](https://docs.estuary.dev/reference/Connectors/materialization-connectors/PostgreSQL/)

## Details

DeveloperEstuary

Category [DevTools](https://supabase.com/partners/integrations#devtools)

Website [www.estuary.dev](https://www.estuary.dev/)

Documentation [Learn](https://www.estuary.dev/)

Third-party integrations and docs are managed by Supabase partners.