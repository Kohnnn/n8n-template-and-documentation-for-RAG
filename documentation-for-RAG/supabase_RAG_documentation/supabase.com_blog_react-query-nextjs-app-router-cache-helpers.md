---
url: "https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers"
title: "Using React Query with Next.js App Router and Supabase Cache Helpers"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Using React Query with Next.js App Router and Supabase Cache Helpers

12 Jan 2024

•

11 minute read

[![Giancarlo Buomprisco avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2FGbuomprisco.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Giancarlo BuompriscoGuest Author](https://twitter.com/gc_psk)

[![Philipp Steinrötter avatar](https://supabase.com/_next/image?url=%2Fimages%2Fphilipp-steinrotter.jpg&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Philipp SteinrötterGuest Author](https://twitter.com/psteinroe)

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Using React Query with Next.js App Router and Supabase Cache Helpers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-01-12-react-query%2Freact-query-nextjs-supabase.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

[TanStack Query](https://tanstack.com/query/latest), also known as React Query, is an open source state management library for React which handles caching, background updates and stale data out of the box with zero-configuration, which makes it an ideal tool to pair with [supabase-js](https://supabase.com/docs/reference/javascript/introduction) and our auto-generated [REST API](https://supabase.com/docs/guides/api)!

If you prefer video guides, we've got a three-part video series for you!

React Query with Next.js App Router - YouTube

Supabase

54.4K subscribers

[React Query with Next.js App Router](https://www.youtube.com/watch?list=PL5S4mPUpp4OuCRhBFPvMTTWFHNrmAOCD_&v=Z4L_UE0hVmo)

Supabase

Search

1/3

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

[Previous (SHIFT+p)](https://www.youtube.com/watch?list=PL5S4mPUpp4OuCRhBFPvMTTWFHNrmAOCD_&v=g2k9-6Ka2QY "Previous (SHIFT+p)")[Next (SHIFT+n)](https://www.youtube.com/watch?list=PL5S4mPUpp4OuCRhBFPvMTTWFHNrmAOCD_&v=AnRshBKUApg "Next (SHIFT+n)")

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?list=PL5S4mPUpp4OuCRhBFPvMTTWFHNrmAOCD_&v=Z4L_UE0hVmo "Watch on YouTube")

If you learn better by just jumping into a demo application, you can find one in our [examples on GitHub](https://github.com/supabase/supabase/tree/master/examples/caching/with-react-query-nextjs-14).

Note: this blogpost is inspired by Giancarlo's original blogpost on using [React Query with Supabase in Remix.io](https://makerkit.dev/blog/saas/supabase-react-query)!

## Prerequisites [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#prerequisites)

This article assumes that your have some basic kowledge of building React applications with Next.js. No prior knowledge of React Query or Supabase is required.

We will use the following tools

- [Next.js](https://nextjs.org/) \- we used `14.0.3`
- [TanStack React Query](https://tanstack.com/query/latest) \- we used `5.12.2`
- [Supabase SSR helpers](https://supabase.com/docs/guides/auth/server-side/creating-a-client) \- we used `0.0.10`
- [Supabase Cache Helpers](https://github.com/psteinroe/supabase-cache-helpers) \- we used `@supabase-cache-helpers/postgrest-react-query` version `1.3.0`
- Supabase - create your account [here](https://database.new/) if you do not have one
- IDE of your choosing

### Install the required dependencies [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#install-the-required-dependencies)

After you have created your [Next.js project](https://nextjs.org/docs/pages/api-reference/create-next-app), e.g. with `npx create-next-app@latest`, you can install the required dependencies using the following command:

`
npm install @supabase/supabase-js @tanstack/react-query @supabase/ssr @supabase-cache-helpers/postgrest-react-query
`

### Creating a React Query client [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#creating-a-react-query-client)

Create a React Query client in the root of your component tree. In Next.js app router applications, this is the `layout.tsx` file in the `app` folder.

The `QueryClientProvider` can only be used in client components and can't be directly embedded in the `layout.tsx` file. Therefore make sure to create a client component first, e.g.

components/ReactQueryClientProvider.tsx

`
'use client'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { useState } from 'react'
export const ReactQueryClientProvider = ({ children }: { children: React.ReactNode }) => {
const [queryClient] = useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            // With SSR, we usually want to set some default staleTime
            // above 0 to avoid refetching immediately on the client
            staleTime: 60 * 1000,
          },
        },
      })
)
return <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
}
`

Next, wrap the root in `layout.tsx`:

app/layout.tsx

`
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import { ReactQueryClientProvider } from '@/components/ReactQueryClientProvider'
const inter = Inter({ subsets: ['latin'] })
export const metadata: Metadata = {
title: 'Create Next App',
description: 'Generated by create next app',
}
export default function RootLayout({ children }: { children: React.ReactNode }) {
return (
    <ReactQueryClientProvider>
      <html lang="en">
        <body className={inter.className}>{children}</body>
      </html>
    </ReactQueryClientProvider>
)
}
`

### Creating your Database schema and generating TypeScript types [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#creating-your-database-schema-and-generating-typescript-types)

For this example, we'll use a simple countries table where we store the id and name of countries. In your [Supabase Dashboard SQL editor](https://supabase.com/dashboard/project/_/sql/new) create the countries table and add some values:

`
create table countries (
"id" serial primary key,
"name" text
);
insert into countries
(id, name)
values
(1, 'United Kingdom'),
(2, 'United States'),
(3, 'Singapore');
`

Once you've created your schema, you can use the [Supabase CLI](https://supabase.com/docs/guides/api/rest/generating-types) to automatically generate TypeScript types for you:

`
supabase login
supabase init
supabase link
supabase gen types typescript --linked --schema=public > utils/database.types.ts
`

These generated types will allow us to get typed data returned from React Query.

### Creating supabase-js clients for client and server components [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#creating-supabase-js-clients-for-client-and-server-components)

To help you utilize the full power of supabase-js, including [Supabase Auth](https://supabase.com/auth) and [Row Level Security (RLS)](https://supabase.com/docs/guides/auth/row-level-security) policies, we provide the [Supabase SSR helper library](https://supabase.com/docs/guides/auth/server-side/creating-a-client) that allows you to conveniently create both browser Supabase clients for client components and server Supabase clients for server components.

Further reading: [detailed documentation for Supabase SSR in Next.js](https://supabase.com/docs/guides/auth/server-side/creating-a-client?framework=nextjs)

#### Create a TypedSupabaseClient type [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#create-a-typedsupabaseclient-type)

To make sure we have the proper typing available in all our components, we can create a `TypedSupabaseClient` type that we can hand to React Query:

utils/types.ts

`
import { SupabaseClient } from '@supabase/supabase-js'
import type { Database } from '@/utils/database.types'
export type TypedSupabaseClient = SupabaseClient<Database>
`

#### Creating a Browser Supabase Client [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#creating-a-browser-supabase-client)

utils/supabase-browser.ts

`
import { createBrowserClient } from '@supabase/ssr'
import type { Database } from '@/utils/database.types'
import type { TypedSupabaseClient } from '@/utils/types'
import { useMemo } from 'react'
let client: TypedSupabaseClient | undefined
function getSupabaseBrowserClient() {
if (client) {
    return client
}
client = createBrowserClient<Database>(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
)
return client
}
function useSupabaseBrowser() {
return useMemo(getSupabaseBrowserClient, [])
}
export default useSupabaseBrowser
`

#### Creating a Server Supabase Client [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#creating-a-server-supabase-client)

utils/supabase-server.ts

`
import { createServerClient } from '@supabase/ssr'
import { cookies } from 'next/headers'
import { Database } from './database.types'
export default function useSupabaseServer(cookieStore: ReturnType<typeof cookies>) {
return createServerClient<Database>(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        get(name: string) {
          return cookieStore.get(name)?.value
        },
      },
    }
)
}
`

Now we've got everything in place to get started fetching and caching data with React Query!

### Automate query key management with the Supabase Cache Helpers [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#automate-query-key-management-with-the-supabase-cache-helpers)

React Query manages query caching based on [query keys](https://tanstack.com/query/v4/docs/react/guides/query-keys). Needing to manage query keys is somewhat burdensome, luckily this is where the [Supabase Cache Helpers](https://github.com/psteinroe/supabase-cache-helpers) come into play.

Initially built during the [Launch Week 5 Hackathon](https://supabase.com/blog/launch-week-5-hackathon-winners#best-overall-project) by [Philipp Steinrötter](https://twitter.com/psteinroe), it has become a full blown open source project that automatically generates cache keys from your supabase-js queries, amongst [many other awesome features](https://github.com/psteinroe/supabase-cache-helpers?tab=readme-ov-file#features)!

### Write reusable queries [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#write-reusable-queries)

The most convenient way to use your queries across both server and client component is to define them in a central place, e.g. a `queries` folder:

queries/get-country-by-id.ts

``
import { TypedSupabaseClient } from '@/utils/types'
export function getCountryById(client: TypedSupabaseClient, countryId: number) {
return client
    .from('countries')
    .select(
      `
      id,
      name
    `
    )
    .eq('id', countryId)
    .throwOnError()
    .single()
}
``

This is a simple query function that takes in either the browser or the server Supabase client and the id of a country, and returns a supabase-js query.

### Fetch data server side [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#fetch-data-server-side)

In server components, we can now use this query with the `prefetchQuery` method:

app/ssrcountries/\[id\]/page.tsx

`
import { dehydrate, HydrationBoundary, QueryClient } from '@tanstack/react-query'
import { prefetchQuery } from '@supabase-cache-helpers/postgrest-react-query'
import useSupabaseServer from '@/utils/supabase-server'
import { cookies } from 'next/headers'
import Country from '../country'
import { getCountryById } from '@/queries/get-country-by-id'
export default async function CountryPage({ params }: { params: { id: number } }) {
const queryClient = new QueryClient()
const cookieStore = cookies()
const supabase = useSupabaseServer(cookieStore)
await prefetchQuery(queryClient, getCountryById(supabase, params.id))
return (
    // Neat! Serialization is now as easy as passing props.
    // HydrationBoundary is a Client Component, so hydration will happen there.
    <HydrationBoundary state={dehydrate(queryClient)}>
      <Country id={params.id} />
    </HydrationBoundary>
)
}
`

Our query will be executed and fetch the data on the server. This means when using our query in the corresponding `Country` client component, the data will be immediately available upon render:

app/ssrcountries/country.tsx

`
'use client'
import useSupabaseBrowser from '@/utils/supabase-browser'
import { getCountryById } from '@/queries/get-country-by-id'
import { useQuery } from '@supabase-cache-helpers/postgrest-react-query'
export default function Country({ id }: { id: number }) {
const supabase = useSupabaseBrowser()
// This useQuery could just as well happen in some deeper
// child to <Posts>, data will be available immediately either way
const { data: country } = useQuery(getCountryById(supabase, id))
return (
    <div>
      <h1>SSR: {country?.name}</h1>
    </div>
)
}
`

Since our query has them same generated cache key, React Query knows that the data was pre-fetched server side and therefore can render immediately without any loading state.

### Fetch data client side [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#fetch-data-client-side)

Of course you can still combine this with fetching data client side. React Query will check if a given query was pre-fetched server side, but if it wasn't it will then go ahead and fetch the data client side side using the browser Supabase client:

app/countries/\[id\]/page.tsx

`
'use client'
import useSupabaseBrowser from '@/utils/supabase-browser'
import { getCountryById } from '@/queries/get-country-by-id'
import { useQuery } from '@supabase-cache-helpers/postgrest-react-query'
export default function CountryPage({ params }: { params: { id: number } }) {
const supabase = useSupabaseBrowser()
const { data: country, isLoading, isError } = useQuery(getCountryById(supabase, params.id))
if (isLoading) {
    return <div>Loading...</div>
}
if (isError || !country) {
    return <div>Error</div>
}
return (
    <div>
      <h1>{country.name}</h1>
    </div>
)
}
`

## Conclusion [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#conclusion)

React Query and the Supabase Cache Helpers are fantastic tools to help you manage data fetching and caching in your Next.js applications.

Using React Query with Server Components makes most sense if:

- You have an app using React Query and want to migrate to Server Components without rewriting all the data fetching.
- You want a familiar programming paradigm, but want to still sprinkle in the benefits of Server Components where it makes most sense.
- You have some use case that React Query covers, but that your framework of choice does not cover.

It's hard to give general advice on when it makes sense to pair React Query with Server Components and not. If you are just starting out with a new Server Components app, we suggest you start out with any tools for data fetching your framework provides you with and avoid bringing in React Query until you actually need it. This might be never, and that's fine, as always: use the right tool for the job!

## More Next.js and Supabase resources [\#](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers\#more-nextjs-and-supabase-resources)

- [Supabase is now compatible with Next.js 14](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14)
- [Next.js with Supabase YouTube Playlist](https://youtube.com/playlist?list=PL5S4mPUpp4OtwG-qCxm8gA_hjaBq0OPdz&feature=shared)
- [Next.js Subscription Payments starter](https://github.com/vercel/nextjs-subscription-payments)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-query-nextjs-app-router-cache-helpers&text=Using%20React%20Query%20with%20Next.js%20App%20Router%20and%20Supabase%20Cache%20Helpers)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-query-nextjs-app-router-cache-helpers&text=Using%20React%20Query%20with%20Next.js%20App%20Router%20and%20Supabase%20Cache%20Helpers)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-query-nextjs-app-router-cache-helpers&t=Using%20React%20Query%20with%20Next.js%20App%20Router%20and%20Supabase%20Cache%20Helpers)

[Last post\\
\\
**What is SAML? A practical guide to the authentication protocol** \\
\\
17 January 2024](https://supabase.com/blog/what-is-saml-authentication)

[Next post\\
\\
**Brace yourself, IPv6 is coming** \\
\\
12 January 2024](https://supabase.com/blog/ipv6)

[react](https://supabase.com/blog/tags/react) [nextjs](https://supabase.com/blog/tags/nextjs)

On this page

- [Prerequisites](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#prerequisites)
  - [Install the required dependencies](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#install-the-required-dependencies)
  - [Creating a React Query client](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#creating-a-react-query-client)
  - [Creating your Database schema and generating TypeScript types](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#creating-your-database-schema-and-generating-typescript-types)
  - [Creating supabase-js clients for client and server components](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#creating-supabase-js-clients-for-client-and-server-components)
  - [Automate query key management with the Supabase Cache Helpers](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#automate-query-key-management-with-the-supabase-cache-helpers)
  - [Write reusable queries](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#write-reusable-queries)
  - [Fetch data server side](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#fetch-data-server-side)
  - [Fetch data client side](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#fetch-data-client-side)
- [Conclusion](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#conclusion)
- [More Next.js and Supabase resources](https://supabase.com/blog/react-query-nextjs-app-router-cache-helpers#more-nextjs-and-supabase-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-query-nextjs-app-router-cache-helpers&text=Using%20React%20Query%20with%20Next.js%20App%20Router%20and%20Supabase%20Cache%20Helpers)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-query-nextjs-app-router-cache-helpers&text=Using%20React%20Query%20with%20Next.js%20App%20Router%20and%20Supabase%20Cache%20Helpers)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-query-nextjs-app-router-cache-helpers&t=Using%20React%20Query%20with%20Next.js%20App%20Router%20and%20Supabase%20Cache%20Helpers)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)