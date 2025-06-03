---
url: "https://supabase.com/partners/integrations/cyberduck"
title: "Cyberduck | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Cyberduck](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fcyberduck%2Fcyberduck-icon-384.png&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Cyberduck

## Overview

Cyberduck is a free and open-source file manager for Windows and macOS that can be used to connect to Supabase Storage S3.
In this guide, you'll learn how to connect to Supabase Storage S3 with Cyberduck.

![Supabase Cyberduck](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cyberduck/cyberduck-files.png?t=2024-04-18T08%3A39%3A48.575Z)

## Prerequisites

You'll need valid credentials to connect to Supabase Storage S3. You can generate these credentials from the [Supabase Dashboard](https://supabase.com/dashboard/project/_/settings/storage).

## Download Cyberduck

You can download Cyberduck from the [Download Page](https://cyberduck.io/download/).

## Configure Cyberduck Profile

To configure cyberduck to connect to Supabase Storage S3 you need to create a custom profile.

Copy the following profile into a file called `supabase.cyberduckprofile`

`
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>Protocol</key>
        <string>s3</string>
        <key>Vendor</key>
        <string>Supabase Storage S3</string>
        <key>Scheme</key>
        <string>https</string>
        <key>Description</key>
        <string>Supabase Storage (S3)</string>
        <key>Default Hostname</key>
        <string>YOUR_PROJECT_REF.supabase.co</string>
        <key>Default Port</key>
        <string>443</string>
        <key>Region</key>
        <string>YOUR_REGION</string>
        <key>Properties</key>
        <array>
            <string>s3.storage.class.options=STANDARD</string>
            <string>s3.bucket.virtualhost.disable=true</string>
        </array>
        <key>Context</key>
        <string>/storage/v1/s3</string>
        <key>Help</key>
        <string>https://supabase.com/docs/guides/storage</string>
    </dict>
</plist>
`

Change the following values in the profile:

- `YOUR_PROJECT_REF` with your Supabase project reference.
- `YOUR_REGION` with your Supabase region.

Save the profile and double click on the file to open it with Cyberduck.

## Connect to Supabase Storage S3

You'll be presented with the following screen, fill in the `Access Key ID` and the `Secret Access Key` with your credentials.

![credentials](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/cyberduck/credentials.png)

Close the window, and double click on the profile to connect to Supabase Storage S3.

## Details

DeveloperSupabase

Category [Storage](https://supabase.com/partners/integrations#storage)

Website [cyberduck.io](https://cyberduck.io/)

Documentation [Learn](https://cyberduck.io/)

Third-party integrations and docs are managed by Supabase partners.