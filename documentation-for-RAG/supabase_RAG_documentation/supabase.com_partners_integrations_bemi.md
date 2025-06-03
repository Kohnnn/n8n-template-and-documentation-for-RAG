---
url: "https://supabase.com/partners/integrations/bemi"
title: "Bemi | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Bemi](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fbemi%2Fbemi-logo.png%3Ft%3D2024-05-31T10%253A35%253A15.036Z&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Bemi

## Overview

Bemi is an open-source platform that provides automatic audit trails for PostgreSQL.

## Step \#1 - Find your Supabase database credentials

You can find these under `Settings` \> `Database` \> `Connection Parameters`. Untoggle "Use connection pooling". The string below will contain the database information required.

![Supabase Connection UI](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/bemi/screenshot.jpeg?t=2024-05-31T10%3A34%3A45.771Z)

For example, given a connection string like `postgresql://root:[YOUR-PASSWORD]@ db.fwlzplllytibpaignejo.supabase.co:5432/postgres`, the credentials would be:

- Database Host: `db.fwlzplllytibpaignejo.supabase.co`
- Database Port: `5432`
- Username: `root`
- Password: `[YOUR-PASSWORD]`
- Database: `postgres`

## Step \#2 - Create Bemi connection

Create a [new database connection](https://dashboard.bemi.io/databases/source/new) by logging in with Github and securely entering the credentials for your Supabase database. During the connection setup or any time after, you can configure what tables you want to track through the Bemi UI.

Please wait a few minutes while the infrastructure is being provisioned. Once this succeeds, you’ve successfully configured a Bemi Postgres source for your Supabase database.

## Details

Watch an introductory video

![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

DeveloperBemi

Category [Data Platform](https://supabase.com/partners/integrations#data%20platform)

Website [bemi.io](https://bemi.io/)

Documentation [Learn](https://docs.bemi.io/postgresql/source-database/#supabase)

Third-party integrations and docs are managed by Supabase partners.