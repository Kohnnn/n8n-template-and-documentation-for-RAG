---
url: "https://supabase.com/partners/integrations/artie"
title: "Artie | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Artie](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fartie%2Fartie-logo.png&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Artie

![Artie](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fartie%2Fartie-og.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

Artie is a real-time database replication platform that leverages change data capture. We help companies replicate data from databases like Supabase to their data warehouse (Snowflake, BigQuery, Redshift) and ensure data consistency.

Artie is fully-managed and quick to set up. We take care of historical backfills, provide analytics, monitoring, schema change alerts and more - all out-of-the-box.

### Step \#1 - Enable IPv4 Add On

Artie does not support IPv6. Please ensure that you have IPv4 enabled as an add on.

To do this:

1. Go to your project settings in Supabase
2. Click on Add Ons
3. Enable IPv4

![Screenshot 1](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image1.png)

### Step \#2 - Create an Artie account

Go to Artie's website and fill out the contact form ( [https://www.artie.com/contact](https://www.artie.com/contact)). We will reach out shortly with an account activation link.

![Screenshot 2](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image2.png)

### Step \#3 - Find your Supabase database credentials

You can find this under Settings > Database > Connection Parameters.

We will need the following:

- Database Host (Uncheck Display connection pooler)
- Database Port (Should be 5432)
- Username
- Password
- Database

To create a service account, please run the following commands in Supabase.

`
CREATE USER artie_transfer WITH PASSWORD 'password';
-- Grant replication permissions
ALTER USER artie_transfer REPLICATION;
-- Grant read-only access to future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO artie_transfer;
-- Grant access to existing tables
GRANT SELECT ON ALL TABLES IN SCHEMA public TO artie_transfer;
CREATE PUBLICATION dbz_publication FOR ALL TABLES;
`

### Step \#4 - Create a new deployment in Artie

Head over to Artie with the information you have gathered from Step #2 and create a new deployment.

![Screenshot 3](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image3.png)

- Pick the tables you want to replicate
- (Optional) You can also enable [history mode](https://www.artie.com/blogs/history-table) (which will create a SCD Type 4 table with `__history` suffix) and record every database change. Consider enabling history mode if you need audit logs or to replace existing daily snapshot processes.
- Pick your destination. Destination setup instructions will appear on the right hand side of the screen.

Check out our [docs](https://artie.com/docs/start) if you need additional help.

## Product Screenshots

![Screenshot 4](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image4.png)

![Screenshot 5](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image5.png)

![Screenshot 6](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/artie/image6.png)

## Details

DeveloperArtie

Category [Data Platform](https://supabase.com/partners/integrations#data%20platform)

Website [artie.com](https://artie.com/)

Documentation [Learn](https://docs.artie.com/real-time-sources/postgresql)

Third-party integrations and docs are managed by Supabase partners.

# Get started with Artie and Supabase.

[Add integration](https://docs.artie.com/real-time-sources/postgresql/supabase)