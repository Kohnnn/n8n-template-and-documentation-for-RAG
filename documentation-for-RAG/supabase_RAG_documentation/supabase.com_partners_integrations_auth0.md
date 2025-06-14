---
url: "https://supabase.com/partners/integrations/auth0"
title: "Auth0 | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Auth0](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fauth0%2Fauth0_dark.png%3Ft%3D2023-07-19T19%253A13%253A04.189Z&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Auth0

## Overview

Using Auth0, developers can connect any application written in any language or stack, and define the external identity providers, as well as integrations, that they want to use. This short Auth0 product demo gives an overview of this process, touching upon Auth0’s unmatched extensibility and its applicability to B2B, B2C, and B2E use cases.

## Documentation

This guide steps through building a Next.js application with Auth0 and Supabase. We configure Auth0 to handle authenticating users and managing tokens, while writing our authorization logic in Supabase - using Row Level Security policies.

> Note: This guide is heavily inspired by the [Using Next.js and Auth0 with Supabase](https://auth0.com/blog/using-nextjs-and-auth0-with-supabase/) article on [Auth0's blog](https://auth0.com/blog/). Check it out for a practical step-by-step guide on integrating Auth0 and Supabase.

The full code example for this guide can be found [here](https://github.com/dijonmusters/supabase-auth0-example).

[Auth0](https://auth0.com/) is an authentication and authorization platform, offering numerous strategies to authenticate and manage users. It provides fine-grain control over how users sign in to your application, the token that is generated, and what data is stored about your users.

[Next.js](https://nextjs.org/) is a web application framework built on top of React. We will be using it for this example, as it allows us to write server-side logic within our application. Auth0 have also written a [very well integrated authentication library](https://www.npmjs.com/package/@auth0/nextjs-auth0) specifically for Next.js.

> Note: API routes (serverless functions) in Next.js closely resemble the structure of Node server frameworks - such as Express, Koa and Fastify. The server-side logic in this guide could easily be refactored in one of these frameworks and managed as a separate application to the front-end.

If you don’t have an Auth0 account, create one [here](https://auth0.com/signup).

You will also need a Supabase account, which can be created by signing in [here](https://supabase.com/dashboard/).

## Step 1: Creating an Auth0 tenant

From the Auth0 dashboard, click the menu to the right of the Auth0 logo, and select `Create tenant`.

![Create tenant from Auth0 dashboard](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/IYzHxeW.png)

Enter a `Domain` for your tenant - this will need to be unique.

Select a `Region` \- this should be geographically close to the majority of your users.

Select `Development` for `Environment Tag` \- this should be production when you're ready to go live.

![Auth0 tenant settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/iSA3E0J.png)

## Step 2: Setting up an Auth0 application

From the sidebar menu, select `Applications` \> `Applications` and click `Create Application`.

Give your application a name, select the `Regular Web Applications` option and click `Create`.

![Auth0 application settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/ANU4Wez.png)

Select `Settings` and navigate to the `Application URIs` section, and update the following:

`Allowed Callback URLs`: `http://localhost:3000/api/auth/callback`

`Allowed Logout URLs`: `http://localhost:3000`

Scroll to the bottom of the `Settings` section and reveal the `Advanced Settings`.

Select `OAuth` and set `JSON Web Token Signature` to `RS256`.

Confirm `OIDC Conformant` is `Enabled`.

Click `Save` to update the settings.

## Step 3: Creating a Supabase project

From your [Supabase dashboard](https://supabase.com/dashboard/), click `New project`.

Enter a `Name` for your Supabase project.

Enter a secure `Database Password`.

Select the same `Region` you selected for your Auth0 tenant.

Click `Create new project`.

![New Supabase project settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/qnmJEU7.png)

## Step 4: Creating data in Supabase

From the sidebar menu in the [Supabase dashboard](https://supabase.com/dashboard/), click `Table editor`, then `New table`.

Enter `todo` as the `Name` field.

Select `Enable Row Level Security (RLS)`.

Create two new columns:

- `title` as `text`
- `user_id` as `text`
- `is_complete` as `bool` with the default value `false`

Click `Save` to create the new table.

![Todo table](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/33kqP4K.png)

From the `Table editor` view, select the `todo` table and click `Insert row`.

Fill out the `title` field and click `Save`.

![New row settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/mEhHAWC.png)

Click `Insert row` and add a couple of extra todos.

![List of todos](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/dLOvhdq.png)

## Step 5: Building a Next.js app

Create a new Next.js project:

`
npx create-next-app <name-of-project>
`

Create a `.env.local` file and enter the following values:

`
AUTH0_SECRET=any-secure-value
AUTH0_BASE_URL=http://localhost:3000
AUTH0_ISSUER_BASE_URL=https://<name-of-your-tenant>.<region-you-selected>.auth0.com
AUTH0_CLIENT_ID=get-from-auth0-dashboard
AUTH0_CLIENT_SECRET=get-from-auth0-dashboard
NEXT_PUBLIC_SUPABASE_URL=get-from-supabase-dashboard
NEXT_PUBLIC_SUPABASE_ANON_KEY=get-from-supabase-dashboard
SUPABASE_JWT_SECRET=get-from-supabase-dashboard
`

> Note: Auth0 values can be found under `Settings > Basic Information` for your application.

![Auth0 settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/o07FaoV.png)

> Note: Supabase values can be found under `Settings > API` for your project.

![Supabase settings](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/r1GAfLo.png)

Restart your Next.js development server to read in the new values from `.env.local`.

`
npm run dev
`

## Step 6: Install Auth0 Next.js library

Install the `@auth0/nextjs-auth0` library.

`
npm i @auth0/nextjs-auth0
`

Create a new file `pages/api/auth/[...auth0].js` and add:

`
// pages/api/auth/[...auth0].js
import { handleAuth } from '@auth0/nextjs-auth0'
export default handleAuth()
`

> Note: This will create a few API routes for us. The main ones we will use are `/api/auth/login` and `/api/auth/logout` to handle signing users in and out.

Open `pages/_app.js` and wrap our `Component` with the `UserProvider` from Auth0:

`
// pages/_app.js
import React from 'react'
import { UserProvider } from '@auth0/nextjs-auth0/client'
const App = ({ Component, pageProps }) => {
return (
    <UserProvider>
      <Component {...pageProps} />
    </UserProvider>
)
}
export default App
`

Update `pages/index.js` to ensure the user is logged in to view the landing page.

`
// pages/index.js
import styles from '../styles/Home.module.css'
import { withPageAuthRequired } from '@auth0/nextjs-auth0'
import Link from 'next/link'
const Index = ({ user }) => {
return (
    <div className={styles.container}>
      <p>
        Welcome {user.name}!{' '}
        <Link href="/api/auth/logout">
          <a>Logout</a>
        </Link>
      </p>
    </div>
)
}
export const getServerSideProps = withPageAuthRequired()
export default Index
`

> Note: `withPageAuthRequired` will automatically redirect the user to `/api/auth/login` if they are not currently logged in.

Test this is working by navigating to `http://localhost:3000` which should redirect you to an Auth0 sign in screen.

![Auth0 sign in screen](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/xLRL7S7.png)

Either `Sign up` for a new account, or click `Continue with Google` to sign in.

You should now be able to view the landing page.

![Landing page](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/YdBKRy6.png)

## Step 7: Sign Auth0 token for Supabase

Currently, neither Supabase or Auth0 allow for a custom signing secret to be set for their JWT. They also use different [signing algorithms](https://auth0.com/docs/configure/applications/signing-algorithms).

Therefore, we need to extract the bits we need from Auth0's JWT, and sign our own to send to Supabase.

We can do that using Auth0's `afterCallback` function, which gets called anytime the user authenticates.

Install the `jsonwebtoken` library.

`
npm i jsonwebtoken
`

Update `pages/api/auth/[...auth0].js` with the following:

`
// pages/api/auth/[...auth0].js
import { handleAuth, handleCallback } from '@auth0/nextjs-auth0'
import jwt from 'jsonwebtoken'
const afterCallback = async (req, res, session) => {
const payload = {
    userId: session.user.sub,
    exp: Math.floor(Date.now() / 1000) + 60 * 60,
}
session.user.accessToken = jwt.sign(payload, process.env.SUPABASE_JWT_SECRET)
return session
}
export default handleAuth({
async callback(req, res) {
    try {
      await handleCallback(req, res, { afterCallback })
    } catch (error) {
      res.status(error.status || 500).end(error.message)
    }
},
})
`

Our `payload` for the JWT will contain our user's unique identifier from Auth0 - `session.user.sub` and an expiry of 1 hour.

We are signing this JWT using Supabase's signing secret, so Supabase will be able to validate it is authentic and hasn't been tampered with in transit.

> Note: We need to sign the user out and back in again to run the `afterCallback` function, and create our new token.

Now we just need to send the token along with the request to Supabase.

## Step 8: Requesting data from Supabase

Create a new file called `utils/supabase.js` and add the following:

``
// utils/supabase.js
import { createClient } from '@supabase/supabase-js'
const getSupabase = (access_token) => {
const options = {}
if (access_token) {
    options.global = {
      headers: {
        Authorization: `Bearer ${access_token}`,
      },
    }
}
const supabase = createClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY,
    options
)
return supabase
}
export { getSupabase }
``

This will be our client for talking to Supabase. We can pass it an `access_token` and it will be attached to our request.

Let's load our `todos` from Supabase in our landing page!

`
// pages/index.js
import styles from '../styles/Home.module.css'
import { withPageAuthRequired } from '@auth0/nextjs-auth0'
import { getSupabase } from '../utils/supabase'
import Link from 'next/link'
import { useEffect } from 'react'
const Index = ({ user }) => {
const [todos, setTodos] = useState([])
const supabase = getSupabase(user.accessToken)
useEffect(() => {
    const fetchTodos = async () => {
      const { data } = await supabase.from('todo').select('*')
      setTodos(data)
    }
    fetchTodos()
}, [])
return (
    <div className={styles.container}>
      <p>
        Welcome {user.name}!{' '}
        <Link href="/api/auth/logout">
          <a>Logout</a>
        </Link>
      </p>
      {todos?.length > 0 ? (
        todos.map((todo) => <p key={todo.id}>{todo.content}</p>)
      ) : (
        <p>You have completed all todos!</p>
      )}
    </div>
)
}
export const getServerSideProps = withPageAuthRequired()
export default Index
`

Alternatively, we could fetch todos on the server using the `getServerSideProps` function.

`
// pages/index.js
import styles from '../styles/Home.module.css'
import { withPageAuthRequired, getSession } from '@auth0/nextjs-auth0'
import { getSupabase } from '../utils/supabase'
import Link from 'next/link'
const Index = ({ user, todos }) => {
return (
    <div className={styles.container}>
      <p>
        Welcome {user.name}!{' '}
        <Link href="/api/auth/logout">
          <a>Logout</a>
        </Link>
      </p>
      {todos?.length > 0 ? (
        todos.map((todo) => <p key={todo.id}>{todo.content}</p>)
      ) : (
        <p>You have completed all todos!</p>
      )}
    </div>
)
}
export const getServerSideProps = withPageAuthRequired({
async getServerSideProps({ req, res }) {
    const {
      user: { accessToken },
    } = await getSession(req, res)
    const supabase = getSupabase(accessToken)
    const { data: todos } = await supabase.from('todo').select('*')
    return {
      props: { todos },
    }
},
})
export default Index
`

Either way, when we reload our application, we are still getting the empty state for todos.

![Empty todo list](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/XgEMwnN.png)

This is because we enabled Row Level Security, which blocks all requests by default. To enable our user to select their `todos` we need to write a policy.

## Step 9: Write a policy to allow select

Our policy will need to know who our currently logged in user is to determine whether or not they should have access. Let's create a PostgreSQL function to extract the current user from our new JWT.

Navigate back to the Supabase dashboard, select `SQL` from the sidebar menu, and click `New query`. This will create a new query called `new sql snippet`, which will allow us to run any SQL against our Postgres database.

Write the following and click `Run`.

`
create or replace function auth.user_id() returns text as $$
select nullif(current_setting('request.jwt.claims', true)::json->>'userId', '')::text;
$$ language sql stable;
`

This will create a function called `auth.user_id()`, which will inspect the `userId` field of our JWT payload.

> Note: To learn more about PostgreSQL functions, check out [our deep dive video](https://www.youtube.com/watch?v=MJZCCpCYEqk).

Let's create a policy that checks whether this user is the owner of the todo.

Select `Authentication` from the Supabase sidebar menu, click `Policies`, and then `New Policy` on the `todo` table.

![Create new policy](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/M7XyhHe.png)

From the modal, select `Create a policy from scratch` and add the following.

![Policy settings for SELECT](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/wuWz3am.png)

This policy is calling the function we just created to get the currently logged in user's ID `auth.user_id()` and checking whether this matches the `user_id` column for the current `todo`. If it does, then it will allow the user to select it, otherwise it will continue to deny.

Click `Review` and then `Save policy`.

> Note: To learn more about RLS and policies, check out [our deep dive video](https://www.youtube.com/watch?v=Ow_Uzedfohk).

The last thing we need to do is update the `user_id` columns for our existing `todos`.

Head back to the Supabase dashboard, and select `Table editor` from the sidebar.

![User ID null in Supabase Table Editor](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/dLOvhdq.png)

Each of our `user_id` columns are set to `NULL`!

To get the ID for our Auth0 user, head over to the Auth0 dashboard, select `User Management` from the sidebar, click `Users` and select your test user.

![List of users in Auth0 dashboard](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/GdXS013.png)

Copy their `user_id`.

![User ID in Auth0 dashboard](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/tbvd0Uj.png)

Update each row in Supabase.

![User ID set to Auth0 user](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/auth0/documentation/tPu4Tt8.png)

Now when we refresh our application, we should finally see our list of `todos`!

> Note: Check out [the repo](https://github.com/dijonmusters/supabase-auth0-example/blob/main/pages/index.js) for an example of writing new `todos` to Supabase.

## Resources

- [Auth0](https://auth0.com/) official website.
- [Auth0 blog](https://auth0.com/blog/).
- [Using Next.js and Auth0 with Supabase article](https://auth0.com/blog/using-nextjs-and-auth0-with-supabase/).
- [Auth0 community](https://community.auth0.com/).
- [Auth0 documentation](https://auth0.com/docs/).

## Details

DeveloperAuth0

Category [Auth](https://supabase.com/partners/integrations#auth)

Website [auth0.com](https://auth0.com/)

Documentation [Learn](https://auth0.com/docs)

Third-party integrations and docs are managed by Supabase partners.