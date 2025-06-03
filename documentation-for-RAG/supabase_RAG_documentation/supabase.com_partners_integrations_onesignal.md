---
url: "https://supabase.com/partners/integrations/onesignal"
title: "OneSignal | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![OneSignal](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fonesignal%2Fonesignal-logo.png&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# OneSignal

![OneSignal](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fonesignal%2Fonesignal-1.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![OneSignal](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fonesignal%2Fonesignal-2.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

OneSignal is a tool that allows you to send messages across different channels such as the following to keep your users engaged.

- Push notifications
- SMS
- Emails
- In-app notifications

Combined with Supabase Database Webhooks and you can provide realtime cloud messaging experience to your users.

You can get started with OneSignal and Supabase [here](https://supabase.com/docs/guides/integrations/onesignal).

## Documentation

[OneSignal](https://onesignal.com/) is a tool that allows you to send messages across different channels such as the following to keep your users engaged.

- Push notifications
- SMS
- Emails
- In-app notifications

Here is William giving us the overview of how OneSignal can work with Supabase to send notifications to your users.

Sending Push Notifications with Supabase - YouTube

OneSignal

2.61K subscribers

[Sending Push Notifications with Supabase](https://www.youtube.com/watch?v=mw0DLwItue4)

OneSignal

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

[Watch on YouTube](https://www.youtube.com/watch?v=mw0DLwItue4 "Watch on YouTube")

In this guide, we will build a similar app and steps you through how you can integrate OneSignal with Supabase to create a seamless cloud messaging experience for your users using Database webhooks and edge functions through a simple Next.js application.

![Entity Diagram](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/diagram.png)

We will create a simple ordering app and use Supabase Database Webhooks in conjunction with Edge Function to provide a real-time push notification experience.

You can find the complete example app along with the edge functions code to send the notifications [here](https://github.com/supabase-community/onesignal).

![Ordering app UI](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/app-ui.png)

## Step 1: Getting started

Before we dive into the code, this guide assumes that you have the following ready

- [Supabase](https://supabase.com/) project created
- [OneSignal](https://onesignal.com/) app created
- [Supabase CLI](https://supabase.com/docs/guides/cli) installed on your machine

Let’s create a Next.js app with tailwind CSS pre-installed

`
npx create-next-app -e with-tailwindcss --ts
`

We will then install the Supabase and OneSignal SDK.

`
npm i @supabase/supabase-js
npm i react-onesignal
`

After that, follow the instructions [here](https://documentation.onesignal.com/docs/web-push-custom-code-setup) to set up OneSignal for the web. You can set the URL of the app as a local host if you want to run the app locally, or add a remote URL if you want to deploy your app to a public hosting. You should add the file you obtain in step 4 of the instruction under the `public` directory of your Next.js app like [this](https://github.com/supabase-community/onesignal/tree/main/app/public).

## Step 2: Build Next.js app

The Next.js app will have a login form for the user to sign in, and a button that they can press to make an order once they are signed in. Update the `index.tsx` file to the following.

pages/index.tsx

`
import { createClient, User } from '@supabase/supabase-js'
import type { NextPage } from 'next'
import Head from 'next/head'
import React, { useEffect, useState } from 'react'
import OneSignal from 'react-onesignal'
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
const oneSignalAppId = process.env.NEXT_PUBLIC_ONESIGNAL_APP_ID!
const supabase = createClient(supabaseUrl, supabaseAnonKey)
const Home: NextPage = () => {
const [user, setUser] = useState<User | null>(null)
const [oneSignalInitialized, setOneSignalInitialized] =
    useState<boolean>(false)
/**
* Initializes OneSignal SDK for a given Supabase User ID
* @param uid Supabase User ID
*/
const initializeOneSignal = async (uid: string) => {
    if (oneSignalInitialized) {
      return
    }
    setOneSignalInitialized(true)
    await OneSignal.init({
      appId: oneSignalAppId,
      notifyButton: {
        enable: true,
      },
      allowLocalhostAsSecureOrigin: true,
    })
    await OneSignal.login(uid)
}
const sendMagicLink = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    const { email } = Object.fromEntries(new FormData(event.currentTarget))
    if (typeof email !== 'string') return
    const { error } = await supabase.auth.signInWithOtp({ email })
    if (error) {
      alert(error.message)
    } else {
      alert('Check your email inbox')
    }
}
// Place a order with the selected price
const submitOrder = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    const { price } = Object.fromEntries(new FormData(event.currentTarget))
    if (typeof price !== 'string') return
    const { error } = await supabase
      .from('orders')
      .insert({ price: Number(price) })
    if (error) {
      alert(error.message)
    }
}
useEffect(() => {
    const initialize = async () => {
      const initialUser = (await supabase.auth.getUser())?.data.user
      setUser(initialUser ?? null)
      if (initialUser) {
        initializeOneSignal(initialUser.id)
      }
    }
    initialize()
    const authListener = supabase.auth.onAuthStateChange(
      async (event, session) => {
        const user = session?.user ?? null
        setUser(user)
        if (user) {
          initializeOneSignal(user.id)
        }
      }
    )
    return () => {
      authListener.data.subscription.unsubscribe()
    }
}, [])
return (
    <>
      <Head>
        <title>OneSignal Order Notification App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="flex items-center justify-center min-h-screen bg-black">
        {user ? (
          <form className="flex flex-col space-y-2" onSubmit={submitOrder}>
            <select
              className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded block p-2"
              name="price"
            >
              <option value="100">$100</option>
              <option value="200">$200</option>
              <option value="300">$300</option>
            </select>
            <button
              type="submit"
              className="py-1 px-4 text-lg bg-green-400 rounded"
            >
              Place an Order
            </button>
          </form>
        ) : (
          <form className="flex flex-col space-y-2" onSubmit={sendMagicLink}>
            <input
              className="border-green-300 border rounded p-2 bg-transparent text-white"
              type="email"
              name="email"
              placeholder="Email"
            />
            <button
              type="submit"
              className="py-1 px-4 text-lg bg-green-400 rounded"
            >
              Send Magic Link
            </button>
          </form>
        )}
      </main>
    </>
)
}
export default Home
`

There is quite a bit of stuff going on here, but basically, it’s creating a simple UI for the user to sign in using the [magic link](https://supabase.com/docs/guides/auth/auth-magic-link), and once the user is signed in, will initialize OneSignal to ask the user to receive notifications on the website.

Notice that inside the `initializeOneSignal()` function, we use the Supabase user ID a to log the user into OneSignal. This allows us to later send push notifications to the user using their Supabase user ID from the backend, which is very handy.

`
await OneSignal.login(uid)
`

The front-end side of things is done here. Let’s get into the backend.

We also need to set our environment variables. Create a `.env.local` file and use the following template to set the environment variables. You can find your Supabase configuration in your dashboard under `settings > API`, and you can find the OneSignal app ID from `Settings > Keys & IDs`

`
NEXT_PUBLIC_SUPABASE_URL=YOUR_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY
NEXT_PUBLIC_ONESIGNAL_APP_ID=YOUR_ONESIGNAL_APP_ID
`

![Where to find OneSignal App ID](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/onesignal-app-id.png)

## Step 3: Create the Edge Function

Let’s create an edge function that will receive [database webhooks](https://supabase.com/docs/guides/database/webhooks) from the database and calls the OneSignal API to send the push notification.

`
supabase functions new notify
`

Replace the contents of `supabase/functions/notify/index.ts` with the following

``
import { serve } from 'https://deno.land/std@0.177.0/http/server.ts'
import * as OneSignal from 'https://esm.sh/@onesignal/node-onesignal@1.0.0-beta7'
const _OnesignalAppId_ = Deno.env.get('ONESIGNAL_APP_ID')!
const _OnesignalUserAuthKey_ = Deno.env.get('USER_AUTH_KEY')!
const _OnesignalRestApiKey_ = Deno.env.get('ONESIGNAL_REST_API_KEY')!
const configuration = OneSignal.createConfiguration({
userKey: _OnesignalUserAuthKey_,
appKey: _OnesignalRestApiKey_,
})
const onesignal = new OneSignal.DefaultApi(configuration)
serve(async (req) => {
try {
    const { record } = await req.json()
    // Build OneSignal notification object
    const notification = new OneSignal.Notification()
    notification.app_id = _OnesignalAppId_
    notification.include_external_user_ids = [record.user_id]
    notification.contents = {
      en: `You just spent $${record.price}!`,
    }
    const onesignalApiRes = await onesignal.createNotification(notification)
    return new Response(
      JSON.stringify({ onesignalResponse: onesignalApiRes }),
      {
        headers: { 'Content-Type': 'application/json' },
      }
    )
} catch (err) {
    console.error('Failed to create OneSignal notification', err)
    return new Response('Server error.', {
      headers: { 'Content-Type': 'application/json' },
      status: 400,
    })
}
})
``

If you see bunch of errors in your editor, it's because your editor is not configured to use Deno. Follow the official setup guide [here](https://deno.land/manual@v1.28.3/getting_started/setup_your_environment) to setup your IDE to use Deno.

The function receives a `record` object, which is the row inserted in your `orders` table, and constructs a notification object to then send to OneSignal to deliver the push notification.

We also need to set the environment variable for the function. Create a `.env` file under your `supabase` directory and paste the following.

`
ONESIGNAL_APP_ID=YOUR_ONESIGNAL_APP_ID
USER_AUTH_KEY=YOUR_USER_AUTH_KEY
ONESIGNAL_REST_API_KEY=YOUR_ONESIGNAL_REST_API_KEY
`

`ONESIGNAL_APP_ID` and `ONESIGNAL_REST_API_KEY` can be found under `Settings > Keys & IDs` of your OneSignal app, and `USER_AUTH_KEY` can be found by going to `Account & API Keys` page by clicking your icon in the top right corner and scrolling to the `User Auth Key` section.

![Where to find OneSignal User Auth Key](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/onesignal-api-key.png)

Once your environment variables are filled in, you can run the following command to set the environment variable.

`
supabase secrets set --env-file ./supabase/.env
`

At this point, the function should be ready to be deployed! Run the following command to deploy your functions to the edge! The `no-verify-jwt` flag is required if you plan to call the function from a webhook.

`
supabase functions deploy notify --no-verify-jwt
`

## Step 4: Setting up the Supabase database

Finally, we get to set up the database! Run the following SQL to set up the `orders` table.

`
create table
if not exists public.orders (
    id uuid not null primary key default uuid_generate_v4 (),
    created_at timestamptz not null default now (),
    user_id uuid not null default auth.uid (),
    price int8 not null
);
`

As you can see, the `orders` table has 4 columns and 3 of them have default values. That means all we need to send from the front-end app is the price. That is why our insert statement looked very simple.

`
const { error } = await supabase.from('orders').insert({
price: 100,
})
`

Let’s also set up the webhook so that whenever a new row is inserted in the `orders` table, it calls the edge function. Go to `Database > Webhooks` and create a new Database Webhook. The table should be set to `orders` and Events should be inserted. The type should be HTTP Request, the HTTP method should be POST, and the URL should be the URL of your edge function. Hit confirm to save the webhook configuration.

![Supabase Webhooks configuration](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/webhook.png)

At this point, the app should be complete! Run your app locally with `npm run dev`, or deploy your app to a hosting service and see how you receive a push notification when you place an order!
Remember that if you decide to deploy your app to a hosting service, you would need to create another OneSignal app configured for your local address.

![Ordering app UI](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/onesignal/documentation/app-ui.png)

## Resources

This particular example was using Next.js, but you can apply the same principles to implement send push notification, SMS, Emails, and in-app-notifications on other platforms as well.

- [OneSignal + Flutter + Supabase example](https://github.com/OneSignalDevelopers/onesignal-supabase-sample-integration-supabase)
- [OneSignal Mobile Quickstart](https://documentation.onesignal.com/docs/mobile-sdk-setup)
- [OneSignal Documentation](https://documentation.onesignal.com/docs/onesignal-platform)
- [OneSignal Onboarding guide](https://documentation.onesignal.com/docs/onboarding-with-onesignal)

## Details

DeveloperOneSignal

Category [Messaging](https://supabase.com/partners/integrations#messaging)

Website [onesignal.com](https://onesignal.com/)

Documentation [Learn](https://documentation.onesignal.com/docs)

Third-party integrations and docs are managed by Supabase partners.