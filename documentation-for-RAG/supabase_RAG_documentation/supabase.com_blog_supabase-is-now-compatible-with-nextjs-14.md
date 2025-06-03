---
url: "https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14"
title: "Supabase is now compatible with Next.js 14"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase is now compatible with Next.js 14

01 Nov 2023

•

7 minute read

[![Jon Meyers avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdijonmusters.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Jon MeyersDeveloper Advocate](https://twitter.com/jonmeyers_io)

![Supabase is now compatible with Next.js 14](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Fnextjs-compatible.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

As part of [Next.js Conf 2023](https://nextjs.org/conf), the team at Vercel released [Next.js 14](https://nextjs.org/blog/next-14). The huge headline feature was...

[![Tweet from Lee Robinson about Next.js 14 containing no new APIs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Flee-tweet-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://x.com/leeerob/status/1717596944623649198?s=20)

That's right, the headline feature is no new features!

This may sound underwhelming at first, but is incredibly good news for the stability of Next.js. This release comes with a huge number of performance and stability improvements—such as [Server Actions](https://nextjs.org/docs/app/api-reference/functions/server-actions) being marked as stable. This means we can finally start promoting this fantastically simple way of authenticating users—entirely server-side!

`
export default async function Page() {
const signIn = async () => {
    'use server'
    supabase.auth.signInWithOAuth({...})
}
return (
    <form action={signIn}>
      <button>Sign in with GitHub</button>
    </form>
)
}
`

With [Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components), fetching data in Next.js became as simple as:

`
export default async function Page() {
const { data } = await supabase.from('...').select()
return ...
}
`

With Server Actions, you can now place mutation logic alongside the Server Components responsible for fetching data and rendering the page:

`
export default async function Page() {
const { data } = await supabase.from('...').select()
const createNote = async () => {
    'use server'
    await supabase.from('...').insert({...})
}
return ...
}
`

> To hear more about our thoughts on Next.js Conf and the release of Next.js 14, check out our [Twitter space](https://twitter.com/i/spaces/1yoKMwNWbRjJQ?s=20). [Yuri](https://twitter.com/yuricodesbot), [Alaister](https://twitter.com/alaisteryoung), [Terry](https://twitter.com/saltcod) and [myself](https://twitter.com/jonmeyers_io) talk through how we use Next.js at Supabase and what we personally found most exciting about Next.js Conf and the release of Next.js 14.

## Is Supabase compatible with Next.js 14? [\#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14\#is-supabase-compatible-with-nextjs-14)

Yes, it is! So much so that [Guillermo Rauch](https://twitter.com/rauchg) shouted us out in the keynote!

[![Tweet showing Guillermo Rauch mentioning Supabase as one of the companies compatible with the Next.js App Router](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Fguillermo-tweet-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://x.com/supabase/status/1717658742743761239?s=20)

Since the release of the [App Router](https://nextjs.org/docs/app)—launched as beta with Next.js 13—we have been working closely with the team at Vercel to ensure that Supabase is fully compatible with every part of Next.js.

So for the [App Router](https://nextjs.org/docs/app), that's:

- [Client Components](https://nextjs.org/docs/app/building-your-application/rendering/client-components)
- [Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components)
- [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)
- [Server Actions](https://nextjs.org/docs/app/api-reference/functions/server-actions)
- [Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware)

And for the [Pages Router](https://nextjs.org/docs/pages):

- [`getServerSideProps` function](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)
- [`getStaticProps` function](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
- [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
- [Page Components](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)

So why does it require work on the Supabase side to make it compatible with Next.js?

## Configuring Supabase to use Cookies [\#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14\#configuring-supabase-to-use-cookies)

By default, [`supabase-js`](https://supabase.com/docs/reference/javascript/introduction) uses `localStorage` to store the user's session. This works well for client-side apps, but will fail when you try to use [`supabase-js`](https://supabase.com/docs/reference/javascript/introduction) in a Server Component, as there is no concept of 'localStorage' on the server.

To do this, we need to configure `supabase-js` to use cookies instead of `localStorage` when running on the server. But this code is a little verbose to ask people to duplicate across every app they build with Supabase:

`
const supabase = createClient(supabaseUrl, supabaseAnonKey, {
auth: {
    flowType: 'pkce',
    autoRefreshToken: false,
    detectSessionInUrl: false,
    persistSession: true,
    storage: {
      getItem: async (key: string) => {
        cookieStore.get(key)
      },
      setItem: async (key: string, value: string) => {
        cookieStore.set(key, value)
      },
      removeItem: async (key: string) => {
        cookieStore.remove(key)
      },
    },
},
})
`

That takes care of the server-side pieces of Next.js, but since we recommend securing your apps with [Row Level Security (RLS) policies](https://www.youtube.com/watch?v=Ow_Uzedfohk), you can safely access your user's session client-side too. Therefore, we need to tell the browser how access that cookie too:

`
const supabase = createClient(supabaseUrl, supabaseAnonKey, {
auth: {
    flowType: 'pkce',
    autoRefreshToken: true,
    detectSessionInUrl: true,
    persistSession: true,
    storage: {
      getItem: async (key: string) => {
        return parse(document.cookie[key])
      },
      setItem: async (key: string, value: string) => {
        document.cookie = serialize(key, value)
      },
    },
    removeItem: async (key: string) => {
      document.cookie = serialize(key, '', {
        maxAge: 0,
      })
    },
},
})
`

That is a lot of very confusing code! So we decided to [create a package called `@supabase/ssr`](https://supabase.com/docs/guides/auth/server-side/overview) that does all of this for you. Then we took it one step further and created a [Next.js and Supabase Starter Template](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs), so you can just focus on building your awesome app! 🚀

> Check out my [Next.js Conf talk](https://www.youtube.com/watch?t=3880&v=FdiX5rHS_0Y) to see this starter template in action!

## How do I get started? [\#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14\#how-do-i-get-started)

One command:

`
npx create-next-app@latest -e with-supabase
`

The landing page will guide you through the process of creating a Supabase project and configuring your environment variables.

Build ~~in a weekend~~ on a Friday night! Scale to millions!

## Meme zone [\#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14\#meme-zone)

As you probably know, we love memes, so we are signing off with one about the least controversial commands coming out of Next.js Conf:

[![Tweet from Terry Sutton running the `with-supabase` command](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Fterry-tweet-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://x.com/saltcod/status/1718959967955275843?s=20)

## More Supabase and Next.js resources [\#](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14\#more-supabase-and-nextjs-resources)

- [Next.js Quickstart](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)
- [Build a User Management App with Next.js](https://supabase.com/docs/guides/getting-started/tutorials/with-nextjs)
- [Server-Side Auth Overview](https://supabase.com/docs/guides/auth/server-side/overview)
- [Fetching and caching Supabase data in Next.js 13 Server Components](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components)
- [Infinite scroll with Next.js, Framer Motion, and Supabase](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&text=Supabase%20is%20now%20compatible%20with%20Next.js%2014)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&text=Supabase%20is%20now%20compatible%20with%20Next.js%2014)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&t=Supabase%20is%20now%20compatible%20with%20Next.js%2014)

[Last post\\
\\
**Supabase Beta October 2023** \\
\\
6 November 2023](https://supabase.com/blog/beta-update-october-2023)

[Next post\\
\\
**pgvector vs Pinecone: cost and performance** \\
\\
10 October 2023](https://supabase.com/blog/pgvector-vs-pinecone)

[nextjs](https://supabase.com/blog/tags/nextjs) [intgrations](https://supabase.com/blog/tags/intgrations)

On this page

- [Is Supabase compatible with Next.js 14?](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#is-supabase-compatible-with-nextjs-14)
- [Configuring Supabase to use Cookies](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#configuring-supabase-to-use-cookies)
- [How do I get started?](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#how-do-i-get-started)
- [Meme zone](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#meme-zone)
- [More Supabase and Next.js resources](https://supabase.com/blog/supabase-is-now-compatible-with-nextjs-14#more-supabase-and-nextjs-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&text=Supabase%20is%20now%20compatible%20with%20Next.js%2014)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&text=Supabase%20is%20now%20compatible%20with%20Next.js%2014)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-is-now-compatible-with-nextjs-14&t=Supabase%20is%20now%20compatible%20with%20Next.js%2014)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Tweet from Lee Robinson about Next.js 14 containing no new APIs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Flee-tweet-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Tweet showing Guillermo Rauch mentioning Supabase as one of the companies compatible with the Next.js App Router](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Fguillermo-tweet-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Tweet from Terry Sutton running the `with-supabase` command](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-11-01-supabase-is-now-compatible-with-nextjs-14%2Fterry-tweet-dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)