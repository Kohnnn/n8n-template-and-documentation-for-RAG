---
url: "https://supabase.com/partners/integrations/readyset"
title: "Readyset | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Readyset](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Freadyset%2Freadyset_logo.svg%3Ft%3D2024-07-19T15%253A00%253A46.274Z&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Readyset

![Readyset](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Freadyset%2Freadyset_og.jpeg%3Ft%3D2024-07-19T14%253A57%253A24.186Z&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

Readyset is a SQL caching engine that helps developers build performant, real-time applications without making code changes or switching databases.

## Ready to use Readyset?

We're excited to onboard you onto Readyset. Before we can get started, we'll need to make sure your database is configured correctly. Please verify the following list of requirements on Supabase:

### Request access to `prep_readyset` function via support ticket

There are few required queries that need to be run in order to prepare your cluster for Readyset use. A predefined function that will perform all those actions can be requested from the Supabase Support team. Open a support ticket requesting access to `prep_readyset` function and provide your Reference ID. You can get your Reference ID by navigating to Settings > General:

![screenshot-5](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/readyset/screenshot-0.png?t=2024-07-19T14%3A31%3A22.455Z)

Once created, you can run `select prep_readyset();` from the SQL editor in the Dashboard.

### Enable IPv4

Navigate to Settings > Add Ons and click on Change IPv4 Address

![screenshot-1](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/readyset/screenshot-1.png?t=2024-07-19T14%3A31%3A22.455Z)

Select IPv4 Address and click in Confirm.

![screenshot-2](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/readyset/screenshot-2.png?t=2024-07-19T14%3A31%3A22.455Z)

### Disable Connection Pooling

Navigate to Settings > Database and unselect Use connection pooling:

![screenshot-3](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/readyset/screenshot-3.png?t=2024-07-19T14%3A31%3A22.455Z)

Grab your connection ID to be used in Readyset Cloud.

### Run Readyset with Required Flags

Once everything is set, the only remaining step is running `readyset` with two additional options.
You can either pass the `--disable-setup-ddl-replication` and `--disable-create-publication` flags directly to the CLI,
or you can set `DISABLE_SETUP_DDL_REPLICATION` and `DISABLE_CREATE_PUBLICATION` options if you are using configuration file.

## Details

DeveloperReadyset

Category [Caching / Offline-First](https://supabase.com/partners/integrations#caching%20/%20offline-first)

Website [readyset.io](https://readyset.io/?utm_source=supabase-partner-gallery)

Documentation [Learn](https://readyset.io/docs/get-started/install-rs/binaries/install-package)

Third-party integrations and docs are managed by Supabase partners.