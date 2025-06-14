---
url: "https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components"
title: "Fetching and caching Supabase data in Next.js 13 Server Components"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Fetching and caching Supabase data in Next.js 13 Server Components

17 Nov 2022

•

15 minute read

[![Jon Meyers avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdijonmusters.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jon MeyersDeveloper Advocate](https://twitter.com/jonmeyers_io)

![Fetching and caching Supabase data in Next.js 13 Server Components](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2022-11-17-supabase-nextjs-13%2Fnextjs-supabase.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The biggest announcement from Next.js Conf 2022 was the [release of Next.js 13](https://nextjs.org/blog/next-13), which introduces a collection of improvements, most exciting of which is Server Components. The combination of Server Components and Suspense allow for a more streamlined, reimagined way to fetch and cache data in Next.js applications. This provides excellent DX improvements — such as async components — and aligns the Next framework even closer with the future of React.

This article is going to look at how we can use these brand new async components to simplify fetching and caching data from Supabase. We will look all things auth in a separate article. Check out the [Server Components example in the Auth Helpers repo](https://github.com/supabase/auth-helpers/tree/main/examples/nextjs-server-components) if you just can't wait!

> To learn more about any of the concepts covered in this article, check out the [Next.js beta docs](https://beta.nextjs.org/docs).

A good distinction to understand at this point, is that Next.js 13 is stable and ready for production, however, the `app` directory is still in beta and likely to change. This article will be focusing on the app directory, Server Components and Suspense so let's get experimental!

> For an example of the code covered in this tutorial, check out [this repo](https://github.com/dijonmusters/fetching-and-caching-supabase-data-in-next-js-13-server-components).

If you prefer video, check out our recent live stream where we stepped through a similar example.

Data fetching and caching with Next.js 13 - Supabase Happy Hour #26 - YouTube

Supabase

54.4K subscribers

[Data fetching and caching with Next.js 13 - Supabase Happy Hour #26](https://www.youtube.com/watch?v=QH0P5xZt5wY)

Supabase

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

[Watch on](https://www.youtube.com/watch?v=QH0P5xZt5wY&embeds_referring_euri=https%3A%2F%2Fsupabase.com%2F)

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=QH0P5xZt5wY "Watch on YouTube")

Let’s get started by creating a brand new Next.js 13 app using the `create-next-app` package:

`
npx create-next-app@latest --experimental-app next13
`

Now we can run our app in development mode:

`
npm run dev
`

And navigate to [http://localhost:3000](http://localhost:3000/).

This should look pretty familiar, and scanning the folder structure for the app, it should look almost identical to Next.js 12, but with a new folder called `app`. This is where the new data fetching and caching magic takes place. 🪄

Each folder within the `app` directory represents a route in our application. Each folder must have a `page` component, which is rendered when the user navigates to the route, and optional `layout`, `loading` and `error` components.

> Learn more about [Page](https://beta.nextjs.org/docs/api-reference/file-conventions/page), [Layout](https://beta.nextjs.org/docs/api-reference/file-conventions/layout), [Loading](https://beta.nextjs.org/docs/api-reference/file-conventions/loading) and [Error](https://beta.nextjs.org/docs/api-reference/file-conventions/error) components in the [Next.js beta docs](https://beta.nextjs.org/docs).

Before we jump into fetching data, we need some data to fetch. Let’s [create a new Supabase project](https://supabase.com/dashboard).

Once your instance is up and running, head over to the [SQL Editor](https://supabase.com/dashboard/project/_/sql), paste in the following snippet and click `RUN`.

`
create table if not exists posts (
id uuid default gen_random_uuid() primary key,
created_at timestamp with time zone default timezone('utc'::text, now()) not null,
title text,
content text
);
insert into posts(title, content)
values
('My first post', 'Wow! What a great post.'),
('My second post', 'This one needs a little work!');
`

This will create a table called `posts`, and populate it with some example data.

Let’s install the [supabase-js library](https://www.npmjs.com/package/@supabase/supabase-js) to fetch our `posts`.

`
npm install @supabase/supabase-js
`

And add a `.env.local` file with the following environment variables:

`
NEXT_PUBLIC_SUPABASE_URL=your-supabase-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
`

> The values for these can be found in [your project’s API settings](https://supabase.com/dashboard/project/_/settings/api).

Lastly, we need to create a Supabase client. Create a file at `utils/supabase.ts` with the following content:

`
import { createClient } from '@supabase/supabase-js'
export default createClient(
process.env.NEXT_PUBLIC_SUPABASE_URL!,
process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)
`

> For automatically adding types to the Supabase client, check out [how to generate types](https://supabase.com/docs/reference/javascript/typescript-support).

Okay, let’s look at some different data fetching and caching strategies.

# Static [\#](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components\#static)

By default any page component in the `app` folder is a Server Component, and its data is fetched and cached by Next.js every time we build a new version of our application. This is equivalent to exporting a `getStaticProps` function from a component in the `pages` directory.

Let’s create a new file at `app/static/page.tsx` and populate with the following:

`
import supabase from '../../utils/supabase'
export default async function Posts() {
const { data: posts } = await supabase.from('posts').select()
return <pre>{JSON.stringify(posts, null, 2)}</pre>
}
`

Server Components support async/await by default, and suspend the rendering of the component until the data has been fetched. This means we don’t need to handle error or loading states in our component, keeping our rendering logic clean.

> To learn more about displaying `loading` and `error` states, check out [the documentation](https://beta.nextjs.org/docs/api-reference/file-conventions/loading).

Let’s modify this component to render out a collection of `<Link />` components, that navigate to a dedicated page for each post.

``
import Link from 'next/link'
import supabase from '../../utils/supabase'
export default async function Posts() {
const { data: posts } = await supabase.from('posts').select('id, title')
if (!posts) {
    return <p>No posts found.</p>
}
return posts.map((post) => (
    <p key={post.id}>
      <Link href={`/static/${post.id}`}>{post.title}</Link>
    </p>
))
}
``

> Since we are only using `id` and `title` in our component, we can scope our query down to only return these two columns for each post.

Let’s create a dynamic route to handle displaying an individual post. Create a new file at `app/static/[id]/page.tsx` and populate with the following:

`
import supabase from '../../../utils/supabase'
import { notFound } from 'next/navigation'
export default async function Post({ params: { id } }: { params: { id: string } }) {
const { data } = await supabase.from('posts').select().match({ id }).single()
if (!data) {
    notFound()
}
return <pre>{JSON.stringify(data, null, 2)}</pre>
}
`

Currently, this page is generated on-demand and then cached. This means the first person who visits the page will need to wait for the server to get the post data from Supabase. This won’t take long at all, because Supabase is Supa awesome! But, we can still make this _slightly_ more efficient by telling Next.js a finite collection of paths that we want to generate at build time.

We do this by exporting out a `generateStaticParams` function from our dynamic page.

`
export async function generateStaticParams() {
const { data: posts } = await supabase.from('posts').select('id')
return posts?.map(({ id }) => ({
    id,
}))
}
`

> This is similar to `getStaticPaths` in a pages component. Learn more [here](https://beta.nextjs.org/docs/data-fetching/generating-static-params).

The full component should look something like this:

`
import supabase from '../../../utils/supabase'
import { notFound } from 'next/navigation'
export async function generateStaticParams() {
const { data: posts } = await supabase.from('posts').select('id')
return posts?.map(({ id }) => ({
    id,
}))
}
export default async function Post({ params: { id } }: { params: { id: string } }) {
const { data: post } = await supabase.from('posts').select().match({ id }).single()
if (!post) {
    notFound()
}
return <pre>{JSON.stringify(post, null, 2)}</pre>
}
`

Awesome! We now have a Supa snappy blog! The user never needs to wait for data to be fetched. All pages are statically generated at build time, and cached at CDN nodes close to our users! 🎉

Unfortunately, this means any changes we make in Supabase — adding, updating or deleting posts etc — will not be reflected in our blog. If we want to refresh this data on a regular basis, we need to tell Next.js when to _revalidate_.

# Static with Revalidation [\#](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components\#static-with-revalidation)

By exporting a `revalidate` variable from our component, we can specify how many seconds we consider this data to be “fresh”.

`
export const revalidate = 60
`

> This is similar to returning a `revalidate` key from the `getStaticProps` function in a component from the `pages` directory.

So, for 60 seconds Next.js will continue to respond with the static version of our page. After 60 seconds, it will fetch fresh data from Supabase and generate a new static page. However, there is no downtime while this happens, as the previous static page will continue to be served until the “fresh” one has been successfully generated.

The `Posts` component should now look like this:

``
import Link from 'next/link'
import supabase from '../../utils/supabase'
export const revalidate = 60
export default async function Posts() {
const { data: posts } = await supabase.from('posts').select('id, title')
if (!posts) {
    return <p>No posts found.</p>
}
return posts.map((post) => (
    <p key={post.id}>
      <Link href={`/static/${post.id}`}>{post.title}</Link>
    </p>
))
}
``

And the `Post` component should look like this:

`
import supabase from '../../../utils/supabase'
import { notFound } from 'next/navigation'
export const revalidate = 60
export async function generateStaticParams() {
const { data: posts } = await supabase.from('posts').select('id')
return posts?.map(({ id }) => ({
    id,
}))
}
export default async function Post({ params: { id } }: { params: { id: string } }) {
const { data: post } = await supabase.from('posts').select().match({ id }).single()
if (!post) {
    notFound()
}
return <pre>{JSON.stringify(post, null, 2)}</pre>
}
`

We now get all the benefits of static — users not waiting around while data is fetched at request time — but we also get the benefits of dynamic data, as it is being refreshed on a regular basis.

Very cool! 😎

# Dynamic [\#](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components\#dynamic)

If we want fresh data to be fetched on every single request, we can simply set our `revalidate` value to `0`.

**Posts Component**

``
import Link from 'next/link'
import supabase from '../../utils/supabase'
export const revalidate = 0
export default async function Posts() {
const { data: posts } = await supabase.from('posts').select('id, title')
if (!posts) {
    return <p>No posts found.</p>
}
return posts.map((post) => (
    <p key={post.id}>
      <Link href={`/static/${post.id}`}>{post.title}</Link>
    </p>
))
}
``

**Single Post Component**

`
import supabase from '../../../utils/supabase'
import { notFound } from 'next/navigation'
export const revalidate = 0
export async function generateStaticParams() {
const { data: posts } = await supabase.from('posts').select('id')
return posts?.map(({ id }) => ({
    id,
}))
}
export default async function Post({ params: { id } }: { params: { id: string } }) {
const { data: post } = await supabase.from('posts').select().match({ id }).single()
if (!post) {
    notFound()
}
return <pre>{JSON.stringify(post, null, 2)}</pre>
}
`

This is similar to exporting a `getServerSideProps` function from a component in the `pages` directory.

All this server stuff is great, but what if you want to use Supabase client-side? 🤔

# Client-side [\#](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components\#client-side)

There are many use-cases where you need to use Supabase client-side:

1. Authentication

Supabase Auth does a bunch of stuff behind the scenes — handling 3rd party OAuth flows, for example. This will break if you try to sign users in and out on the server.

2. Realtime

Supabase manages the awesome power of websockets on your behalf — something that is not yet solved in this serverless world.

3. You prefer it

There is nothing wrong with this! You do you!


To use Supabase client-side, we need to tell Next.js that this is a [Client Component](https://beta.nextjs.org/docs/rendering/server-and-client-components#client-components). We do this by specifying the `use client` directive at the top of our component. This opts into a similar flow to the `pages` directory — the component is rendered on the server and hydrated client-side.

> The React team is [working on an awesome new hook called "use"](https://github.com/acdlite/rfcs/blob/first-class-promises/text/0000-first-class-support-for-promises.md#example-use-in-client-components-and-hooks), which will drastically simplify fetching data client-side, but for now, we still need to rely on the combination of `useState` and `useEffect`.

Let’s implement client-side data fetching.

`
'use client'
import { useEffect, useState } from 'react'
import supabase from '../../utils/supabase'
export default function ClientPosts() {
const [isLoading, setIsLoading] = useState(true)
const [posts, setPosts] = useState<any>([])
useEffect(() => {
    const fetchPosts = async () => {
      const { data } = await supabase.from('posts').select()
      setPosts(data)
      setIsLoading(false)
    }
    fetchPosts()
}, [])
return isLoading ? <p>Loading</p> : <pre>{JSON.stringify(posts, null, 2)}</pre>
}
`

> Again, check out [how to generate types](https://supabase.com/docs/reference/javascript/typescript-support) to add proper typing for Post.

But now we have loading spinners! Yuck!

# Realtime [\#](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components\#realtime)

Realtime allows us to subscribe to changes in Supabase — inserted, updated or deleted posts — and update our UI dynamically. In order to receive realtime events, we need to [enable replication](https://supabase.com/dashboard/project/_/database/publications) on the posts table.

Let’s merge the two previous concepts and fetch the initial state of our posts in a Server Component, and then render a Client Component to do client-y things — like subscribe to changes in the DB and update the UI dynamically:

**Server Component**

`
import supabase from '../../utils/supabase'
import RealtimePosts from './realtime-posts'
export const revalidate = 0
export default async function Realtime() {
const { data } = await supabase.from('posts').select('*')
return <RealtimePosts serverPosts={data} />
}
`

**Client Component**

`
'use client'
import { useEffect, useState } from 'react'
import supabase from '../../utils/supabase'
export default function RealtimePosts({ serverPosts }: { serverPosts: any }) {
const [posts, setPosts] = useState(serverPosts)
useEffect(() => {
    setPosts(serverPosts)
}, [serverPosts])
useEffect(() => {
    const channel = supabase
      .channel('*')
      .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'posts' }, (payload) =>
        setPosts((posts: any) => [...posts, payload.new])
      )
      .subscribe()
    return () => {
      supabase.removeChannel(channel)
    }
}, [serverPosts])
return <pre>{JSON.stringify(posts, null, 2)}</pre>
}
`

> `useEffect` is used to subscribe to changes to the `serverPosts` prop. Without this, our component would not display fresh server-side results when the parent component is re-rendered, only on the first render.

This is a great pattern for fetching initial data server-side and subscribing to realtime changes client-side. This will likely be replaced by the `use` hook once it is stable with Next.js — it also uses suspense to _suspend_ the rendering of a component while fetching data, and cleans up those loading and error states.

# Conclusion [\#](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components\#conclusion)

Next.js 13 Server Components are awesome! Suspense is awesome! Async components are awesome!

The combination of these concepts allow us to think about data fetching and caching as separate concerns, rather than specifying completely different data fetching functions like `getStaticProps` and `getServerSideProps`. If our caching requirements for a component change, we simply update the caching value, rather than refactoring our data fetching logic.

Additionally, by allowing any component in the tree to be either a server or client component — that is responsible for its own data and suspends rendering until it is ready — drastically simplifies our code, and provides much more flexible patterns for creating maintainable applications as complexity grows.

# More Next.js 13 Resources [\#](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components\#more-nextjs-13-resources)

- [Next.js Quickstart](https://supabase.com/docs/guides/with-nextjs)
- [Next.js 13 Beta Docs](https://beta.nextjs.org/docs)
- [Creating an authenticated Supabase client in Next.js 13 Server Component](https://github.com/supabase/auth-helpers/tree/main/examples/nextjs-server-components)
- [Data fetching and caching with Next.js 13 - Supabase Happy Hour #26](https://www.youtube.com/watch?v=QH0P5xZt5wY)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ffetching-and-caching-supabase-data-in-next-js-server-components&text=Fetching%20and%20caching%20Supabase%20data%20in%20Next.js%2013%20Server%20Components)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ffetching-and-caching-supabase-data-in-next-js-server-components&text=Fetching%20and%20caching%20Supabase%20data%20in%20Next.js%2013%20Server%20Components)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Ffetching-and-caching-supabase-data-in-next-js-server-components&t=Fetching%20and%20caching%20Supabase%20data%20in%20Next.js%2013%20Server%20Components)

[Last post\\
\\
**Flutter Authorization with RLS** \\
\\
22 November 2022](https://supabase.com/blog/flutter-authorization-with-rls)

[Next post\\
\\
**Authentication in Ionic Angular with Supabase** \\
\\
8 November 2022](https://supabase.com/blog/authentication-in-ionic-angular)

[Next.js](https://supabase.com/blog/tags/Next.js)

On this page

- [Static](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components#static)
- [Static with Revalidation](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components#static-with-revalidation)
- [Dynamic](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components#dynamic)
- [Client-side](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components#client-side)
- [Realtime](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components#realtime)
- [Conclusion](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components#conclusion)
- [More Next.js 13 Resources](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components#more-nextjs-13-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ffetching-and-caching-supabase-data-in-next-js-server-components&text=Fetching%20and%20caching%20Supabase%20data%20in%20Next.js%2013%20Server%20Components)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Ffetching-and-caching-supabase-data-in-next-js-server-components&text=Fetching%20and%20caching%20Supabase%20data%20in%20Next.js%2013%20Server%20Components)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Ffetching-and-caching-supabase-data-in-next-js-server-components&t=Fetching%20and%20caching%20Supabase%20data%20in%20Next.js%2013%20Server%20Components)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)