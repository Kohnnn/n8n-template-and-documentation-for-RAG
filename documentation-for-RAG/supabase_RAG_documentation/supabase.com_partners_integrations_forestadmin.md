---
url: "https://supabase.com/partners/integrations/forestadmin"
title: "Forest Admin | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Forest Admin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fforestadmin%2Fforestadmin_logo.png&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Forest Admin

![Forest Admin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fforestadmin%2Fforestadmin_og.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Forest Admin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fforestadmin%2Fforest-admin-live-demo-transactions-monitoring-dashboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Forest Admin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fforestadmin%2Fforest-admin-live-demo-mobility-workspace.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Forest Admin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fforestadmin%2Fforest-admin-live-demo-finance.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Forest Admin](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fforestadmin%2Fforest-admin-live-demo-finance-workspace.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

For web companies that need to manage their application's data to support internal operations, Forest Admin provides a SaaS admin panel that is automatically generated on top of their database. Thanks to its user-friendly GUI, both developers and non-dev users can manage data, create custom dashboards, and perform a wide range of administrative tasks for their applications. On top of that, Forest Admin provides a powerful system for managing user permissions and access control, allowing users to create custom roles and assign different levels of access to different users.

Simply provide your Supabase URI, and in just 30 seconds you’ll have a powerful admin panel that goes beyond basic CRUD operations, offering enhanced data handling capabilities through powerful smart actions.

## Documentation

This guide outlines how to instantly generate an Admin Panel on top of your Supabase backend.

[Forest Admin](https://www.forestadmin.com/) offers an off-the-shelf Admin Panel system that can reduce the amount of time and effort needed to create, maintain, and manage internal tools.
It automatically builds a backend API and provides a user-friendly interface to Create, Read, Update and Delete, Search, Segment your data, trigger custom actions, control permissions, and set up workflows on top of your app's data.

![forest-admin-collections](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/forestadmin/documentation/forest-admin-collections.png)

If you don’t have a Forest Admin account, you can create one in a few minutes [here](https://app.forestadmin.com/signup).

Let’s get started!

## Step 1: Configure your Supabase Backend

If you already have a Supabase project set up, simply go to the Project Settings / Database tab to access the Database Settings and retrieve the connection string (URI tab). This is the only information you will need to connect your Supabase account to Forest Admin.

![Connection parameters for forestadmin](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/forestadmin/connection-string.png)

If you don't have anything set up on Supabase yet, you can [create a Project](https://supabase.com/dashboard/new/_) in just a few seconds. Once done, just go to the Database tab and create your first table.

![New table for forestadmin](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/forestadmin/new-table.png)

## Step 2: Connect the database to Forest Admin

First, you have to create a new project on Forest Admin:
![forestadmin-create-project](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/forestadmin/documentation/forestadmin-create-project.png)

Then, you can use Forest Admin's Instant Setup for the Cloud mode to quickly get started. Alternatively, you can host the generated backend admin API on your own (Advanced setup), giving you full control of the backend code. In this guide, we will use the Cloud mode and the Instant Setup.
![forestadmin-hosting](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/forestadmin/documentation/forestadmin-hosting.png)

Finally, you can enter the database credentials you obtained in Step 1 and set them in Forest Admin by using the Connection URI mode. Don't forget to replace the password in the connection string with the database password you set in Supabase. Note that if you forget it, you can always go to your Supabase Database settings and reset your database password.
![forestadmin-db-credentials](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/forestadmin/documentation/forestadmin-db-credentials.png)

## You're all done!

There it is, the configuration of Forest Admin is now complete and your admin panel is now ready-to-use with all the features of an admin panel provided out of the box. You can now browse or manipulate all your data in a structured way, use search with support for complex filters, build dashboards, invite your team mates and start collaborating around your business operations and much more.

## Resources

- [Forest Admin](https://www.forestadmin.com/) official website.
- [Forest Admin GitHub](https://github.com/ForestAdmin).
- [Forest Admin](https://docs.forestadmin.com/documentation-portal/) documentation.

## Details

Watch an introductory video

![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

DeveloperForest Admin

Category [Low-Code](https://supabase.com/partners/integrations#low-code)

Website [www.forestadmin.com](https://www.forestadmin.com/integrations/supabase)

Documentation [Learn](https://docs.forestadmin.com/cloud)

Third-party integrations and docs are managed by Supabase partners.