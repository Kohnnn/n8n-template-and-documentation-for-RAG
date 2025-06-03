---
url: "https://supabase.com/partners/integrations/loops"
title: "Loops | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Loops](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Floops%2Flogo.png%3Ft%3D2024-11-18T09%253A19%253A41.390Z&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Loops

## Overview

Loops is an email platform for software companies letting you send your product, marketing, and transactional email from one simple interface.

This integration allows you to send Supabase Authentication emails over Loops' SMTP service.

There are two big benefits to using Loops for sending your Supabase emails:

- **More control over design**: You can use [Loops' design editor](https://loops.so/docs/creating-emails/editor) to create (and then easily edit) beautiful transactional emails instead of having to code them with HTML.
- **Better visibility of sent email**: You get full visibility on which emails are being sent, when, and to whom in your Loops account (something not offered in Supabase).

### 1\. Set up Loops SMTP in Supabase

Go to your Authentication settings in Supabase ( **Project Settings -> Authentication**) to tell Supabase to send emails using Loops' SMTP service.

Scroll down and toggle the **Enable Custom SMTP** option on.

In the Sender details section, you will need to enter some values into the "Sender email" and "Sender name" fields. However, _these values will always be overwritten by the values set in your Loops templates_ from the next step.

In the **SMTP Provider Settings** section enter the following data:

| Field | Value |
| --- | --- |
| Host | `smtp.loops.so` |
| Port number | `587` |
| Username | `loops` |
| Password | An API key copied from your [API settings](https://app.loops.so/settings?page=api) in Loops |

![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/loops/supabase-smtp-settings.png)

Note that for the interval and rate limit settings, you will be bound by Loops' [API rate limit](https://loops.so/docs/api-reference/intro#rate-limiting) of 10 requests per second.

One final step is to check that the "Confirm email" toggle is turned on in the Email section in **Authentication -> Providers**.

### 2\. Create Transactional emails in Loops

Next, create new transactional emails for the emails listed in Supabase ( **Authentication -> Email Templates**). You need to create both **Confirm signup** and **Magic Link** emails to be able to properly set up the integration.

- Confirm signup (required)
- Invite user
- Magic Link (required)
- Change Email Address
- Reset Password

Note that if a Supabase user has not previously confirmed their email, they will be sent a **Confirm signup** email when you request a **Magic Link** email.

To create new transactional emails, go to the [Transactional page](https://app.loops.so/transactional) in Loops and click **New**. Alternatively, you can select one of our many ready-made templates from the [Templates page](https://app.loops.so/templates).

![Supabase template in the editor](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/loops/supabase-template.png)

You can then use [the Loops editor](https://loops.so/docs/creating-emails/editor) to create nicely-designed templates or make them as simple as you like.

You can even [save styles](https://loops.so/docs/creating-emails/styles#saved-styles) so you can easily apply consistent branding to all of your emails.

![Saved styles](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/loops/supabase-editor.png)

For each Loops template you create, you need to [add data variables](https://loops.so/docs/creating-emails/personalizing-emails#add-dynamic-content-to-emails), which allow data from Supabase to be inserted into each email.

For example, you could add a `confirmationUrl` data variable that you can map to the `{{ .ConfirmationURL }}` value from Supabase.

You can also build URLs by including values like `{{ .SiteUrl }}` or add in a confirmation code using `{{ .Token }}`.

![Supabase values](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/loops/supabase-values.png)

Once you're done creating the email and adding data variables, click **Next**. On the next page, click the **Show payload** button to view the API payload for your template. You will need this for the next step.

![Email payload](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/loops/supabase-payload.png)

Make sure to also publish your email! It won't send unless it's published.

[Read our detailed guide](https://loops.so/docs/transactional/guide) for sending transactional emails.

### 3\. Configure email templates in Supabase

The final step is to make sure your emails in Supabase are configured to send the correct data to Loops.

Loops SMTP integrations work a bit differently than most. Instead of sending a text or HTML email body, you set them up to send API-like data.

In Supabase, go to **Authentication -> Email Templates**, then edit each template to contain the payload as shown in the previous step (you can click the clipboard icon in Loops to copy the full payload).

Once pasted into the Message body, you need to add the Supabase message variables into the payload.

Important: Make sure you set up at least the **Confirm signup** and **Magic Link** templates in Supabase, otherwise emails will not be sent.

Also, any variables added in the **Confirm signup** template need to also be available in **Magic link** email, because Supabase will send a **Confirm signup** email instead of a **Magic Link** email if a user hasn't confirmed their email address.

Here is an example **Confirm signup** email template. This payload was copied from the template's Publish page in Loops, then the `{{ .Email }}` and `{{ .ConfirmationURL }}` Supabase variables were added.

`
{
"transactionalId": "clvmzp39u035tl50pw7wrl0ri",
"email": "{{ .Email }}",
"dataVariables": {
    "confirmationUrl": "{{ .ConfirmationURL }}"
}
}
`

Here's how it looks in the Supabase editor:

![Supabase editor](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/loops/supabase-email.png)

With the integration now all set up, your Supabase authentication emails will be sent via Loops, giving you more visibility on your email sends and the great addition of being able to build beautiful and easy-to-update emails in the Loops editor.

To view all sends of your transactional emails, click through to the email from the [Transactional](https://app.loops.so/transactional) page in Loops, where you'll find the Metrics page containing a table showing all sends and some statistics.

## Important notes

- You need to add a template in Loops and set up the email in Supabase for at least the **Confirm signup** and **Magic Link** templates.
- The subject in Supabase templates is always overwritten by the subject added to the corresponding template in Loops.
- The sender name and sender email configured in your Supabase SMTP settings are always overwritten by the sender details added to your templates in Loops.
- Any Supabase email not set up with the correct API-like payload will fail to send.

## Details

DeveloperLoops

Category [Messaging](https://supabase.com/partners/integrations#messaging)

Website [loops.so](https://loops.so/)

Documentation [Learn](https://loops.so/docs/integrations/supabase)

Third-party integrations and docs are managed by Supabase partners.