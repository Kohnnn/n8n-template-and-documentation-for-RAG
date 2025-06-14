---
url: "https://supabase.com/partners/integrations/illa"
title: "ILLA | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![ILLA](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Filla%2Filla_logo.png&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# ILLA

![ILLA](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Filla%2Filla_og.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

ILLA is a low-code platform for developers that enables the rapid development and deployment of internal tools.

It allows for creating pages by dragging and dropping UI components, connecting to any database or API, and writing JavaScript.

## Documentation

This tutorial outlines the process of creating an Admin Panel using ILLA Builder and Supabase in a few simple steps. ILLA is a low-code platform for developers that enables the rapid development and deployment of internal tools. It allows for creating pages by dragging and dropping UI components, connecting to any database or API, and writing JavaScript. To learn more about ILLA and give it a try, visit their website at [https://www.illacloud.com/](https://www.illacloud.com/). Let's begin!

### Step 1: Set up your Back end on Supabase

On the [Supabase dashboard](https://supabase.com/dashboard/projects), click `New project` and set the name to adminPanel.

![Create Supabase Project for ILLA Admin Panel](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/illa/new-project.png)

Create a new table by clicking on the `Create a new table` .

Supabase offers a variety of options for populating tables with data, including writing queries, creating schemas through a user interface, and uploading CSV files.

![Create Supabase Table for ILLA Admin Panel](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/illa/new-table.png)

Fill out the info in the table. The database is now set up.

### Step 2: Build UI on ILLA Cloud

On [ILLA Cloud](https://cloud.illacloud.com/), click Create New to create a new application.

![Create new project on ILLA Builder](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/illa/documentation/supabase-illa-create-project.png)

Drag components from the `Insert` panel to the canvas.

Select the components on the canvas and configure the property on the `Inspect` panel.

As seen in the below screenshot, we have built a simple admin panel.

![Build UI with ILLA Builder](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/illa/documentation/supabase-illa-UI.png)

### Step 3: Connect to Supabase and config CRUD

Note down the database connection parameters information under [Database Settings](https://supabase.com/dashboard/project/hdcfnsxpwwgboqomdrhp/settings/database) in Supabase.

![Note information in supabase](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/illa/connection-string.png)

In the Action List, click `+ New` and select Supabase DB.

![Connect ILLA to Supabase](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/illa/documentation/supabase-illa-connect.png)

Fill out the form to connect to your Supabase instance. Test connection and save resource.

![Config Supabase in ILLA](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/illa/documentation/supabase-illa-connect-2.png)

Click `Create Action` to create an action with the Supabase resource and config your CRUD.

![Select Supabase resource in ILLA](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/illa/documentation/supabase-illa-select.png)

Use `{{` to get the front-end input data. The following is an example of the User Management page in the Admin Panel.

Search for a user by the name inputted in input1

`
SELECT *
FROM user
WHERE name = "{{input1.value}}"
;
`

Update user data. Update user information when id matches

`
UPDATE user
SET name = "{{input3.value}}"
, email = "{{input4.value}}"
WHERE id="{{input2.value}}"
;
`

Insert user data

`
INSERT INTO user VALUES("{{input5.value}}","{{input6.value}}","{{input7.value}}");
`

Delete a user by id

`
DELETE FROM user WHERE id = "{{input2.value}}";
`

### Step 4: Show data on components

Configure the properties of components with `{{` . For example:

![Show Supabase data on ILLA components](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/illa/documentation/supabase-illa-show-data.png)

## Resources

- [ILLA Cloud official website](https://www.illacloud.com/)
- [ILLA Cloud GitHub](https://github.com/illacloud/illa-builder)
- [ILLA Cloud documentation](https://www.illacloud.com/docs/about-illa)

## Details

DeveloperILLA

Category [Low-Code](https://supabase.com/partners/integrations#low-code)

Website [www.illacloud.com](https://www.illacloud.com/)

Documentation [Learn](https://www.illa.cloud/docs/supabase)

Third-party integrations and docs are managed by Supabase partners.