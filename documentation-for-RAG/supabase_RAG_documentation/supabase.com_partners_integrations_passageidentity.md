---
url: "https://supabase.com/partners/integrations/passageidentity"
title: "Passage by 1Password | Works With Supabase"
---

[Back](https://supabase.com/partners/integrations)

![Passage by 1Password](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fpassageidentity%2Fpassage_logo.jpeg&w=128&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

# Passage by 1Password

![Passage by 1Password](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fpassageidentity%2F1Password-Passage-header.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Passage by 1Password](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fpassageidentity%2FPassage_Passkey-Complete_Login.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Passage by 1Password](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fpassageidentity%2FPassage_Passkey-Complete_User%2520Details.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Passage by 1Password](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fpassageidentity%2FPassage-App-Dashboard.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Overview

Passage is a passwordless authentication service that enables you to add passkey sign-in experiences to your apps and websites with just two lines of code. As a full stack solution, Passage comes with robust backend infrastructure and pre-built UI elements, letting you implement secure and frictionless logins in minutes.

[Check out this guide](https://docs.passage.id/helpful-guides/supabase-integration-guide) to learn how to add Passage to your Supabase powered site and plug into RLS.

## Documentation

This guide steps through building a Next.js application with Passage and Supabase. We will use Passage to authenticate users and manage tokens, while using Supabase for storing data and enforcing authorization logic using Row Level Security policies.

The full code example for this guide can be found [here](https://github.com/passageidentity/supabase-passage-example).

[Passage](https://passage.id/) is a passwordless authentication platform that makes it simple for developers to add passkey authentication to their apps and websites, providing better security and simpler sign in for your users. They provide simple frontend components that handle all of the complexity of passwordless login for developers in just two lines of codes. Passage also provides session management, user management, and in-depth customization capabilities.

Next.js is a web application framework built on top of React. We will be using it for this example, as it allows us to write server-side logic within our application. Passage’s [frontend elements](https://docs.passage.id/frontend/passage-element) and [Node.js SDK](https://docs.passage.id/backend/overview/node) are designed to work for Next.js.

For this guide, you will need a Passage account which can be created [here](https://console.passage.id/register), and a Supabase account which can be created [here](https://supabase.com/dashboard/).

## 1\. Create a Passage application

In the [Passage Console](https://console.passage.id/), create a new application with the following configuration:

- Application name: Todo Application
- Authentication origin: [http://localhost:3000](http://localhost:3000/)
- Redirect URL: /dashboard

![Passage Console dashboard](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/01.png)

![Fill out the required fields to create a new application](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/02.png)

## 2\. Create and configure a Supabase project

#### Create a new project

In the [Supabase dashboard](https://supabase.com/dashboard/), click `New Project`.
Enter a name for your project and create a secure database password.

#### Create a table schema

We are building Todo list application, similar to the [Supabase demo application](https://github.com/supabase/supabase/tree/master/examples/todo-list/nextjs-todo-list) so we will need a table for the todo list items.

Create a new table in the Table Editor view.

Set the Name field to `todo`.

Select Enable Row Level Security (RLS).

Create the following new columns.

- `title` as `text`
- `user_id` as `text` with a default value of `auth.user_id()`
- `is_complete` as `bool` with a default value of `false`

Click `Save` to create the table.

![Table schema.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/03.png)

#### Add initial data to the table

From the Table editor, select the `todo` table and click `Insert row`. Fill out the required fields with an example todo item, leaving the `user_id` as NULL and click `Save`.

![Example todo item.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/04.png)

After adding a few todo items, the table editor view will look like this:

![Table with multiple todo items.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/05.png)

## 3\. Build a Next.js app

#### Create Next.js app

Create a new Next.js project on the command line. You can choose your settings through the setup wizard - for this guide we will use JavaScript instead of TypeScript. This example uses the create script in Next v13.2.

`
npx create-next-app <name-of-project>
cd <name-of-project>/
`

You should be able to use the default settings for the project, but here are the settings used for the example app.

![Settings for Next.js application.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/06.png)

#### Configure your ENV

Create a `.env` file and enter the following values.

`
NEXT_PUBLIC_PASSAGE_APP_ID=get-from-passage-settings
PASSAGE_API_KEY=get-from-passage-settings
NEXT_PUBLIC_SUPABASE_URL=get-from-supabase-dashboard
NEXT_PUBLIC_SUPABASE_ANON_KEY=get-from-supabase-dashboard
SUPABASE_JWT_SECRET=get-from-supabase-dashboard
`

The Supabase values can be found under `Project->Settings->API Settings`.

![Supabase environment variables.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/07.png)

The Passage values can be found under `General->Settings` and `General->API Keys`.

![Passage environment variables.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/08.png)

![Passage environment variables.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/09.png)

> The `PASSAGE_API_KEY` and `SUPABASE_JWT_SECRET` are secret values and should never be shared publicly. They will only be used in the server-side code of the Next.js application.

Restart your Next.js development server to read in the environment variables.

`
npm run dev
`

## 4\. Add Passage login to your app

#### Add Passage Element

Install the `@passageidentity/passage-elements` package.

`
npm install @passageidentity/passage-elements
`

Create a new folder called components with a new login file `components/login.js` and add the following content.

`
// components/login.js
import { useEffect } from 'react'
const PassageLogin = () => {
useEffect(() => {
    require('@passageidentity/passage-elements/passage-auth')
}, [])
return (
    <>
      <passage-auth app-id={process.env.NEXT_PUBLIC_PASSAGE_APP_ID}></passage-auth>
    </>
)
}
export default PassageLogin
`

Then update `pages/index.js` to include the login component.

`
// pages/index.js
import styles from '@/styles/Home.module.css'
import PassageLogin from '@/components/login'
export default function Home(props) {
return (
    <div className={styles.main}>
      <PassageLogin />
    </div>
)
}
`

When we have a successful registration the Passage element will request a redirect to `/dashboard` per the redirect URL we set during app creation.

Create a new file `pages/dashboard.js` for this new route with the following content:

`
// pages/dashboard.js
import styles from '@/styles/Home.module.css'
export default function Dashboard({ isAuthorized, userID, todos }) {
return (
    <div className={styles.main}>
      <div className={styles.container}>
        <p>You've logged in!</p>
      </div>
    </div>
)
}
`

Now when you visit `http://localhost:3000` in a browser you will have a fully functioning and passwordless login page!

![Simple app with Passage login page.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/10.png)

Go ahead and go through the registration process. You will be able to register an account with either a passkey or a magic link. Once you've logged in, you will notice that you just get redirected to `/dashboard` page.
The login was successful, but we need to build in the functionality to know when a user is authenticated and show them the appropriate view.

#### Use Passage to verify the JWT

Now we will need to use a Passage SDK to verify the JWT from Passage.

Install the Passage Node.js library.

`
npm install @passageidentity/passage-node
`

Create a utils folder and a file called `utils/passage.js` with the following content.

`
// utils/passage.js
import Passage from '@passageidentity/passage-node'
const passage = new Passage({
appID: process.env.NEXT_PUBLIC_PASSAGE_APP_ID,
apiKey: process.env.PASSAGE_API_KEY,
})
export const getAuthenticatedUserFromSession = async (req, res) => {
try {
    const userID = await passage.authenticateRequest(req)
    if (userID) {
      return { isAuthorized: true, userID: userID }
    }
} catch (error) {
    // authentication failed
    return { isAuthorized: false, userID: '' }
}
}
`

This will be used in the `getServerSideProps()` function to check authentication status for a user. Add this function to `index.js` then update the `Home` function to use the props.

`
// pages/index.js
import styles from '@/styles/Home.module.css'
import PassageLogin from '@/components/login'
import { getAuthenticatedUserFromSession } from '@/utils/passage'
import { useEffect } from 'react'
import Router from 'next/router'
export default function Home({ isAuthorized }) {
useEffect(() => {
    if (isAuthorized) {
      Router.push('/dashboard')
    }
})
return (
    <div className={styles.main}>
      <PassageLogin />
    </div>
)
}
export const getServerSideProps = async (context) => {
const loginProps = await getAuthenticatedUserFromSession(context.req, context.res)
return {
    props: {
      isAuthorized: loginProps.isAuthorized ?? false,
      userID: loginProps.userID ?? '',
    },
}
}
`

We will also use this logic on the dashboard page to check if a user is authenticated. If not we should redirect them to the login page. We will also add a quick sign out button using Passage while we are at it.

`
// pages/dashboard.js
import styles from '@/styles/Home.module.css'
import { useEffect } from 'react'
import Router from 'next/router'
import { getAuthenticatedUserFromSession } from '@/utils/passage'
import { PassageUser } from '@passageidentity/passage-elements/passage-user'
export default function Dashboard({ isAuthorized, userID }) {
useEffect(() => {
    if (!isAuthorized) {
      Router.push('/')
    }
})
const signOut = async () => {
    new PassageUser().signOut()
    Router.push('/')
}
return (
    <div className={styles.main}>
      <h1>Welcome {userID}! </h1>
      <br></br>
      <button onClick={signOut}>Sign Out</button>
    </div>
)
}
export const getServerSideProps = async (context) => {
const loginProps = await getAuthenticatedUserFromSession(context.req, context.res)
return {
    props: {
      isAuthorized: loginProps.isAuthorized ?? false,
      userID: loginProps.userID ?? '',
    },
}
}
`

The app can now tell the difference between an authenticated and unauthenticated user. When you log into the application, you will be redirected to the dashboard and see this message.

![Authenticated users can see their user ID.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/11.png)

## 5\. Integrate Supabase into Next.js app

Passage and Supabase do not currently allow for custom signing secrets. Therefore, we will need to extract the necessary claims from the Passage JWT and sign a new JWT to send to Supabase.

Because of the sensitive nature of this functionality, we will handle the authentication and JWT exchange in Next.js’s server-side rendering function `getServerSideProps()`. Imports used in this function will not be bundled client-side. Additionally, the JWT provided by Passage is stored in a cookie which is automatically passed to `getServerSideProps()`.

#### Sign Passage token for Supabase

Install the Supabase client SDK and the popular Node package `jsonwebtoken`, which allows us to easily work with JWTs.

`
npm install @supabase/supabase-js jsonwebtoken
`

Create a new file called `utils/supabase.js` and add the following content. This function accepts a Passage user ID and then creates and signs a Supabase JWT for that user. This allows Supabase to verify the token and authenticate the user when making Supabase calls.

``
// utils/supabase.js
import { createClient } from '@supabase/supabase-js'
import jwt from 'jsonwebtoken'
const getSupabase = (userId) => {
const options = {}
if (userId) {
    const payload = {
      userId,
      exp: Math.floor(Date.now() / 1000) + 60 * 60,
    }
    const token = jwt.sign(payload, process.env.SUPABASE_JWT_SECRET)
    options.global = {
      headers: {
        Authorization: `Bearer ${token}`,
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

#### Enable Row Level Security (RLS) in Supabase

To enable users to view and create their own todo items we need to write a RLS policy. Our policy will check the currently logged in user is to determine whether or not they should have access. Let's create a PostgreSQL function to extract the current user from our new JWT.

Navigate back to the Supabase dashboard, select `SQL Editor` from the sidebar menu, and click `New query`. This will create a new query called `new sql snippet`, which will allow us to run any SQL against our Postgres database.

Write the following and click `Run`.

`
create or replace function auth.user_id() returns text as $$
select nullif(current_setting('request.jwt.claims', true)::json->>'userId', '')::text;
$$ language sql stable;
`

You should see the output `Success, no rows returned`. This created a function called `auth.user_id()` which will return the `userId` field of our JWT payload.

> To learn more about PostgresSQL functions, check out this [deep dive video](https://www.youtube.com/watch?v=MJZCCpCYEqk).

Now we can create a policy that checks whether the current user is the owner of a todo item. From the `Authentication` sidebar menu in Supabase, click `Policies` then create a new policy.

![RLS policies for a table.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/12.png)

Choose `For full customization create a policy from scratch` and add the following.

![Policy to restrict access to todo items.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/13.png)

This policy is calling the function we just created to get the currently logged in user's ID `auth.user_id() ` and checking whether this matches the `user_id` column for the current todo. If it does, then it will allow the user to select it, otherwise it will deny access.

Click `Review` and then `Save policy`.

> Note: To learn more about RLS and policies, check out this [deep dive video](https://www.youtube.com/watch?v=Ow_Uzedfohk).

#### Fetch data from Supabase

Now we can fetch data from Supabase specific to that user. We will update `pages/dashboard.js` to do the following:

1. authenticate the user using Passage
2. create and sign a JWT for the user with the Supabase secret
3. query Supabase to fetch a user’s todo list items

`
// pages/dashboard.js
import styles from '@/styles/Home.module.css'
import { useEffect } from 'react'
import Router from 'next/router'
import { getAuthenticatedUserFromSession } from '@/utils/passage'
import { getSupabase } from '../utils/supabase'
export default function Dashboard({ isAuthorized, userID, todos }) {
useEffect(() => {
    if (!isAuthorized) {
      Router.push('/')
    }
})
return (
    <div className={styles.main}>
      <div className={styles.container}>
        <h1>Welcome {userID}! </h1>
        <br></br>
        <button onClick={signOut}>Sign Out</button>
        <br></br>
        <div className={styles.list}>
          {todos?.length > 0 ? (
            todos.map((todo) => <li key={todo.id}>{todo.title}</li>)
          ) : (
            <p>You have completed all todos!</p>
          )}
        </div>
      </div>
    </div>
)
}
export const getServerSideProps = async (context) => {
const loginProps = await getAuthenticatedUserFromSession(context.req, context.res)
if (loginProps.isAuthorized) {
    const supabase = getSupabase(loginProps.userID)
    const { data } = await supabase.from('todo').select()
    return {
      props: {
        isAuthorized: loginProps.isAuthorized ?? false,
        userID: loginProps.userID ?? '',
        todos: data ?? [],
      },
    }
} else {
    return {
      props: {
        isAuthorized: loginProps.isAuthorized ?? false,
        userID: loginProps.userID ?? '',
      },
    }
}
}
`

When we reload our application, we are still getting the empty state for todos.

This is because we enabled Row Level Security, which blocks all requests by default and lets you granularly control access to the data in your database.

#### Update the UserID data

The last thing we need to do is update the `user_id` columns for our existing todos. Head back to the Supabase dashboard, and select `Table editor` from the sidebar. You will see that the `user_id` field is NULL for all of our todo items.

![User ID is NULL for all todo items.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/14.png)

To get the user ID for our Passage user, go back to the Passage Console and check the `Users` tab.

![Get User ID from Passage.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/15.png)

Copy this user ID and update two of the three rows in the Supabase database to match this user ID. When you are done, the database table will look like this.

![Updated User ID in Supabase.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/16.png)

Now when we refresh the application, we will see the todo items for our user!

![Authenticated users can see their todo items.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/17.png)

## Bonus: Add todo items

To build out a bit more functionality in our application, we can now let users add items to their to do list. Create a file `pages/api/addTodo.js` with the following content.

`
// pages/api/addTodo.js
import { getSupabase } from '../../utils/supabase'
export default async function handler(req, res) {
const { userID, todo } = req.body
const supabase = getSupabase(userID)
const { data, error } = await supabase.from('todo').insert({ title: todo }).select().single()
if (error) return res.status(400).json(error)
res.status(200).json(data)
}
`

Then update `pages/dashboard.js` to include a form for submitting new to do items. The complete file will look like this.

`
//pages/dashboard.js
import styles from '@/styles/Home.module.css'
import { useEffect, useState } from 'react'
import Router from 'next/router'
import { getAuthenticatedUserFromSession } from '@/utils/passage'
import { getSupabase } from '../utils/supabase'
import { PassageUser } from '@passageidentity/passage-elements/passage-user'
export default function Dashboard({ isAuthorized, userID, initialTodos }) {
const [todos, setTodos] = useState(initialTodos)
useEffect(() => {
    if (!isAuthorized) {
      Router.push('/')
    }
})
const handleSubmit = async (e) => {
    e.preventDefault()
    const data = new FormData(e.target)
    const todo = data.get('todo')
    const res = await fetch('/api/addTodo', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ todo, userID }),
    }).then((res) => res.json())
    setTodos([...todos, res])
}
const signOut = async () => {
    new PassageUser().signOut()
    Router.push('/')
}
return (
    <div className={styles.main}>
      <div className={styles.container}>
        <h1>Welcome {userID}! </h1>
        <br></br>
        <button onClick={signOut}>Sign Out</button>
        <br></br>
        <div className={styles.list}>
          {todos?.length > 0 ? (
            todos.map((todo) => <li key={todo.id}>{todo.title}</li>)
          ) : (
            <p>You have completed all todos!</p>
          )}
        </div>
        <form onSubmit={handleSubmit}>
          <label>
            Todo: <input type="text" name="todo" />
          </label>
          <button>Submit</button>
        </form>
      </div>
    </div>
)
}
export const getServerSideProps = async (context) => {
const loginProps = await getAuthenticatedUserFromSession(context.req, context.res)
if (loginProps.isAuthorized) {
    const supabase = getSupabase(loginProps.userID)
    const { data } = await supabase.from('todo').select().is('is_complete', false)
    return {
      props: {
        isAuthorized: loginProps.isAuthorized ?? false,
        userID: loginProps.userID ?? '',
        initialTodos: data ?? [],
      },
    }
} else {
    return {
      props: {
        isAuthorized: loginProps.isAuthorized ?? false,
        userID: loginProps.userID ?? '',
      },
    }
}
}
`

Finally, we need to add a new RLS policy in Supabase to allow users to insert their own todo items.

![RLS policy for inserting todo items.](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/18.png)

That's it! Now the website has form for submitting new items for the to do list.

![Authenticated users can create todo items](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/passageidentity/documentation/19.png)

## Resources

- [Passage website](https://passage.id/)
- [Complete developer documentation](https://docs.passage.id/)
- [Passage Github](https://github.com/passageidentity), including SDKs and example apps for Next.js
- [Developer community](https://discord.com/invite/445QpyEDXh) on Discord

## Details

Watch an introductory video

![Video guide preview](https://supabase.com/_next/image?url=%2Fimages%2Fblur.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

DeveloperPassage Identity

Category [Auth](https://supabase.com/partners/integrations#auth)

Website [passage.1password.com](https://passage.1password.com/)

Documentation [Learn](https://docs.passage.id/helpful-guides/supabase-integration-guide)

Third-party integrations and docs are managed by Supabase partners.