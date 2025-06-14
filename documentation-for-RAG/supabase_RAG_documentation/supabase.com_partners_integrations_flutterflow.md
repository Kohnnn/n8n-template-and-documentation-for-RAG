---
url: "https://supabase.com/partners/integrations/flutterflow"
title: "FlutterFlow | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![FlutterFlow](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fflutterflow%2Fflutterflow-logo.jpeg&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# FlutterFlow

![FlutterFlow](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fflutterflow%2Fflutterflow-1.jpeg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![FlutterFlow](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fflutterflow%2Fflutterflow-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

FlutterFlow is a low-code builder for developing native mobile applications using Flutter. You can use the simple drag-and-drop interface to build your app faster than traditional development.

## Documentation

FlutterFlow and Supabase integration is currently in alpha, and supported features may be limited.

[FlutterFlow](https://flutterflow.io/) is a low-code builder for developing native mobile applications using Flutter. You can use the simple drag-and-drop interface to build your app faster than traditional development.

This guide gives you a quick overview of implementing basic CRUD operations using FlutterFlow and Supabase. You can find the full docs on FlutterFlow and Supabase [here](https://docs.flutterflow.io/actions/actions/backend-database/supabase).

FlutterFlow + Supabase \| Setup & Tutorial - YouTube

FlutterFlow

106K subscribers

[FlutterFlow + Supabase \| Setup & Tutorial](https://www.youtube.com/watch?v=hw9Q-NjASbU)

FlutterFlow

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

[Watch on YouTube](https://www.youtube.com/watch?v=hw9Q-NjASbU "Watch on YouTube")

## Step 1: Connect FlutterFlow to Supabase

Before we dive into the code, this guide assumes that you have the following ready:

- [Supabase](https://database.new/) project created
- Have setup tables in your Supabase project
- [FlutterFlow](https://app.flutterflow.io/) project created

You can then connect your Supabase project to your FlutterFlow project with the following steps:

1. In your Supabase project, navigate to Project Settings > API. Copy the Project URL.
2. Return to FlutterFlow, navigate to Settings and Integrations > Integrations > Supabase. Turn on the toggle (i.e., enable Supabase) and paste the API URL.
3. Similarly, from the Supabase API section, copy the anon key (under Project API keys) and paste it inside the FlutterFlow > Settings and Integrations > Integrations > Supabase > Anon Key.
4. Click on the Get Schema button. This will show the list of all tables with their schema (structure) created in Supabase.
5. (Optional) If you have defined an Array for any Column Data Type in Supabase, you must set its type here. To do so, tap the "Click to set Array type" and choose the right one.

## Step 2: Inserting rows

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the Widget (e.g., Button) on which you want to define the action.
2. Select Actions from the Properties panel (the right menu), and click Open. This will open an Action flow Editor in a new popup window.
1. Click on + Add Action.
2. On the right side, search and select the Supabase > Insert Row action.
3. Set the Table to your table name (e.g., assignments).
4. Under the Set Fields section, click on the + Add Field button.
5. Click on the Field name and scroll down to find the Value Source dropdown and change it to From Variable.
6. Click on UNSET and select Widget State > Name of the TextField.
7. Similarly, add the field for the other UI elements.

## Step 3: Selecting and displaying rows

To query a Supabase table on a ListView:

1. Select the ListView widget. Make sure you choose the ListView widget, not the ListTile.
2. Select Backend Query from the properties panel (the right menu), and click Add Backend Query.
3. Set the Query Type to Supabase Query.
4. Select your Table from the dropdown list
5. Set the Query Type to List of Rows.
6. Optional: If you want to display the limited result, say, for example, you have thousands of entries, but you want to display only 100, you can specify the limit.
7. Click Confirm.

## Step 4: Updating rows

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the Widget (e.g., Button) on which you want to define the action.
2. Select Actions from the Properties panel (the right menu), and click Open. This will open an Action flow Editor in a new popup window.
01. Click on + Add Action.
02. On the right side, search and select the Supabase > Update Row action.
03. Set the Table to your table name (e.g., assignments).
04. Optional: If you want to get the rows after the update is finished, enable the Return Matching Rows option.
05. Now, you must set the row you want to update. Usually, this is done by finding a row in a table that matches the current row ID. To do so, click + Add Filter button inside the Matching Rows section.
       1. Set the Field Name to the field that contains the IDs. Typically, this is the id column.
       2. Set the Relation to Equal To because you want to find a row with the exact id.
       3. Into the Value Source, you can select the From Variable and provide the id of the row for which you just updated values in the UI.
06. Under the Set Fields section, click on the + Add Field button.
07. Click on the field name.
08. Scroll down to find the Value Source dropdown and change it to From Variable.
09. Click on UNSET and select Widget State > Name of the TextField.
10. Similarly, add the field for the other UI elements.

## Step 5: Deleting rows

Go to your project page on FlutterFlow and follow the steps below to define the Action to any widget.

1. Select the Widget (e.g., Button) on which you want to define the action.
2. Select Actions from the Properties panel (the right menu), and click Open. This will open an Action flow Editor in a new popup window.
1. Click on + Add Action.
2. On the right side, search and select the Supabase -> Delete Row action.
3. Set the Table to your table name (e.g., assignments).
4. Optional: Later, if you want to know which rows were deleted from a table, enable the Return Matching Rows option.
5. Now, you must set the row you want to delete. Usually, this is done by finding a row in a table that matches the current row ID. To do so, click + Add Filter button inside the Matching Rows section.
      1. Set the Field Name to the field that contains the IDs. Typically, this is the id column.
      2. Set the Relation to Equal To because you want to find a row with the exact id.
      3. Into the Value Source, you can select the From Variable and provide the id of the row you want to delete.

## Resources

You can find more detailed guides on FlutterFlow’s docs.

- [FlutterFlow Supabase available actions](https://docs.flutterflow.io/actions/actions/backend-database/supabase)
- [Retrieving Data from Supabase on FlutterFlow](https://docs.flutterflow.io/data-and-backend/supabase/supabase-database/retrieving-data)
- [Adding data to Supabase DB from FlutterFlow](https://docs.flutterflow.io/data-and-backend/supabase/supabase-database/adding-data)

## Details

Watch an introductory video

![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

DeveloperFlutterFlow

Category [Low-Code](https://supabase.com/partners/integrations#low-code)

Website [flutterflow.io](https://flutterflow.io/)

Documentation [Learn](https://docs.flutterflow.io/)

Third-party integrations and docs are managed by Supabase partners.