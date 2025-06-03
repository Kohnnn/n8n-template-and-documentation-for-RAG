---
url: "https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion"
title: "Infinite scroll with Next.js, Framer Motion, and Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Infinite scroll with Next.js, Framer Motion, and Supabase

04 Apr 2023

•

13 minute read

[![Francesco Sansalvadore avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ffsansalvadore.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Francesco SansalvadoreEngineering](https://github.com/fsansalvadore)

![Infinite scroll with Next.js, Framer Motion, and Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Finfinite-scroll-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Imagine you generated a bunch of tickets for the Supabase [Launch Week](https://www.supabase.com/launch-week/7) and you wanted to display them all on [one page](https://supabase.com/launch-week/7/tickets). It might take a while to load them all in one go, so a great solution to this would be to lazy load smaller subsets while the user scrolls, with a technique called infinite scrolling.

An infinite scroll allows you to scroll through your content endlessly while only loading the data you need as you need it. This improves performance while also creating a smooth and delightful user experience.

In this post, we'll go through the steps of how to create an infinite scroll using NextJs, Supabase, and Framer Motion.

## What is infinite scroll? [\#](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion\#what-is-infinite-scroll)

Infinite scroll is a web design technique that automatically loads and displays new content as a user scrolls down a web page. This creates an endless scrolling experience that eliminates the need for pagination and provides a seamless and uninterrupted browsing experience.

Infinite scroll can enhance user experience and engagement by providing a fluid and intuitive browsing experience. It also allows for faster content delivery. By dynamically loading and displaying content as needed, infinite scroll can reduce the time and effort required to load pages and deliver content, improving overall performance and user satisfaction.

Next.js is a great choice for implementing infinite scroll in a web application. It provides server-side rendering and automatic code splitting, which can improve performance and optimize the loading of content as the user scrolls down the page. It also includes built-in support for dynamic imports and lazy loading, which can be useful for fetching and displaying content as needed.

Plus, incremental static regeneration (ISR) and pre-fetching of data can further improve performance by enabling the server to generate and cache pages in advance, and to pre-fetch data as the user scrolls down the page.

Now, onto the code!

## Step 0. Load the first batch [\#](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion\#step-0-load-the-first-batch)

First things first, let's install the dependencies we'll need.

`
npm install @supabase/supabase-js lodash framer-motion
`

Set up the supabase-js client and fetch the first 20 tickets through `getServerSideProps` so we don't start with an empty screen.

We'll assume our table in the db is called `my_tickets_table`.

`
import { useEffect, useState } from 'react'
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('supabase-url', 'supabase-key')
export default function TicketsPage({ tickets }) {
const [loadedTickets, setLoadedTickets] = useState(tickets)
return (
    <div>
      {loadedTickets.map((ticket, index) => (
        {/* We'll get to this part later */}
      ))}
    </div>
)
export const getServerSideProps: GetServerSideProps = async ({ req, res }) => {
const { data: tickets } = await supabase!
    .from('my_tickets_table')
    .select('*')
    .order('createdAt', { ascending: false })
    .limit(20)
return {
    props: {
      tickets,
    },
}
}
`

## Step 1. Listen to the scroll [\#](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion\#step-1-listen-to-the-scroll)

To detect if the user is scrolling we can listen to the window `scroll` event.

If you try to `console.log()` the event returned in the listener callback, you'll notice that it fires on every single pixel scrolled. We want to avoid triggering like crazy, so we'll use a [lodash debounce function](https://www.geeksforgeeks.org/lodash-_-debounce-method/) to limit how often we call this event to once every 200 milliseconds.

Here's what it looks like:

`
import { useEffect } from 'react'
import { debounce } from 'lodash'
const handleScroll = () => {
// Do stuff when scrolling
}
useEffect(() => {
const handleDebouncedScroll = debounce(() => handleScroll(), 200)
window.addEventListener('scroll', handleDebouncedScroll)
return () => {
    window.removeEventListener('scroll', handleDebouncedScroll)
}
}, [])
`

## Step 2. Check if the container intersects the viewport [\#](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion\#step-2-check-if-the-container-intersects-the-viewport)

Next, we want to check if the bottom of the tickets container intersects with the bottom of the viewport. We can use the `getBoundingClientRect` method to get the position of the container and then compare it with the height of the viewport.

`
import { useRef, useState } from 'react'
// ...
const containerRef = useRef(null)
const [offset, setOffset] = useState(1)
const [isInView, setIsInView] = useState(false)
const handleScroll = (container) => {
if (containerRef.current && typeof window !== 'undefined') {
    const container = containerRef.current
    const { bottom } = container.getBoundingClientRect()
    const { innerHeight } = window
    setIsInView((prev) => bottom <= innerHeight)
}
}
useEffect(() => {
if (isInView) {
    loadMoreUsers(offset)
}
}, [isInView])
return <div ref={containerRef}>{/* List of loaded tickets */}</div>
`

## Step 3. Load tickets based on the offset [\#](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion\#step-3-load-tickets-based-on-the-offset)

Now we can load more tickets based on the current offset. We'll use the [range](https://supabase.com/docs/reference/javascript/range) method from the supabase-js library to easily work with the pagination logic.

`
export default function TicketsPage() {
const PAGE_COUNT = 20
const [offset, setOffset] = useState(1)
const [isLoading, setIsLoading] = useState(false)
const [isInView, setIsInView] = useState(false)
useEffect(() => {
    if (isInView) {
      loadMoreTickets(offset)
    }
}, [isInView])
const loadMoreTickets = async (offset: number) => {
    setIsLoading(true)
    // Every time we fetch, we want to increase
    // the offset to load fresh tickets
    setOffset((prev) => prev + 1)
    const { data: newTickets } = await fetchTickets(offset, PAGE_COUNT)
    // Merge new tickets with all previously loaded
    setLoadedTickets((prevTickets) => [...prevTickets, ...newTickets])
    setIsLoading(false)
}
const fetchTickets = async (offset, limit) => {
    const from = offset * PAGE_COUNT
    const to = from + PAGE_COUNT - 1
    const { data } = await supabase!
        .from('my_tickets_table')
        .select('*')
        .range(from, to)
        .order('createdAt', { ascending: false })
    return data
}
}
`

## Step 4. Animate the tickets [\#](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion\#step-4-animate-the-tickets)

Now that we have our tickets loaded, we want to add some animation to make them pop like dominos as they appear on the screen. For this, we're going to use the [Framer Motion](https://www.framer.com/motion/) library.

We'll wrap each ticket in a motion component and add a transition effect to stagger their appearance on the screen:

`
import { motion } from 'framer-motion'
// ...
{
loadedTickets.map((ticket, index) => {
    // each ticket will be delayed based on it's index
    // but we need to subtract the delay from all the previously loaded tickets
    const recalculatedDelay = i >= PAGE_COUNT * 2 ? (i - PAGE_COUNT * (offset - 1)) / 15 : i / 15
    return (
      <motion.div
        key={ticket.id}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{
          duration: 0.4,
          ease: [0.25, 0.25, 0, 1],
          delay: recalculatedDelay,
        }}
      >
        {/* Actual ticket component */}
      </motion.div>
    )
})
}
`

With this code, each ticket will start with an opacity of 0 and a y position of 20. As it animates into view, it will fade in and move up to its final position. The delay for each ticket will be based on its index in the array, creating a nice staggered effect.

## Step 5. Stop listening when finished [\#](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion\#step-5-stop-listening-when-finished)

Once all the tickets have been loaded, we want to stop listening to the scroll event to avoid unnecessary requests. We can do this by setting a state variable called `isLast` to true whenever the length of the response will be less than `PAGE_COUNT`:

`
if (newTickets.length < PAGE_COUNT) {
setIsLast(true)
}
`

We'll use this code to conditionally remove the event listener:

`
useEffect(() => {
const handleDebouncedScroll = debounce(() => !isLast && handleScroll(), 200)
window.addEventListener('scroll', handleScroll)
return () => {
    window.removeEventListener('scroll', handleScroll)
}
}, [])
`

Now, when the `isLast` state variable is true, the event listener will be removed and the component will stop listening to the scroll event.

## Wrap up [\#](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion\#wrap-up)

That's it! We hope this post enabled you to build the next awesome infinite scroll.

Here's the complete code:

`
import { useEffect, useState, useRef } from 'react'
import { createClient } from '@supabase/supabase-js'
import { debounce } from 'lodash'
import { motion } from 'framer-motion'
const supabase = createClient('supabase-url', 'supabase-key')
export default function TicketsPage({ tickets }) {
const PAGE_COUNT = 20
const containerRef = useRef(null)
const [loadedTickets, setLoadedTickets] = useState(tickets)
const [offset, setOffset] = useState(1)
const [isLoading, setIsLoading] = useState(false)
const [isInView, setIsInView] = useState(false)
const handleScroll = (container) => {
    if (containerRef.current && typeof window !== 'undefined') {
      const container = containerRef.current
      const { bottom } = container.getBoundingClientRect()
      const { innerHeight } = window
      setIsInView((prev) => bottom <= innerHeight)
    }
}
useEffect(() => {
    const handleDebouncedScroll = debounce(() => !isLast && handleScroll(), 200)
    window.addEventListener('scroll', handleScroll)
    return () => {
      window.removeEventListener('scroll', handleScroll)
    }
}, [])
useEffect(() => {
    if (isInView) {
      loadMoreTickets(offset)
    }
}, [isInView])
const loadMoreTickets = async (offset: number) => {
    setIsLoading(true)
    setOffset((prev) => prev + 1)
    const { data: newTickets } = await fetchTickets(offset, PAGE_COUNT)
    setLoadedTickets((prevTickets) => [...prevTickets, ...newTickets])
    setIsLoading(false)
}
const fetchTickets = async (offset) => {
    const from = offset * PAGE_COUNT
    const to = from + PAGE_COUNT - 1
    const { data } = await supabase!
        .from('my_tickets_table')
        .select('*')
        .range(from, to)
        .order('createdAt', { ascending: false })
    return data
}
return (
    <div ref={containerRef}>
      {
        loadedTickets.map((ticket, index) => {
          const recalculatedDelay =
            i >= PAGE_COUNT * 2 ? (i - PAGE_COUNT * (offset - 1)) / 15 : i / 15
          return (
            <motion.div
              key={ticket.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{
                duration: 0.4,
                ease: [0.25, 0.25, 0, 1],
                delay: recalculatedDelay,
              }}
            >
              {/* Actual ticket component */}
            </motion.div>
          )
        })
      }
    </div>
)
export const getServerSideProps: GetServerSideProps = async ({ req, res }) => {
const { data: tickets } = await supabase!
    .from('my_tickets_table')
    .select('*')
    .order('createdAt', { ascending: false })
    .limit(20)
return {
    props: {
      tickets,
    },
}
}
`

If you also want to feature in the endless tickets page and have a chance to win cool swag, you're invited to [generate your unique ticket](https://www.supabase.com/launch-week) until April 16th.

See you at Launch Week! 👋

### More Launch Week 7

[Designing with AI\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fai-images%2F00-ai-images-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/designing-with-ai-midjourney)

[Supavisor\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fsupavisor%2Fsupavisor-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://github.com/supabase/supavisor)

[Open Source Logging\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday1%2Fself-hosted-logs-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-logs-self-hosted)

[Self-hosted Deno Edge Functions\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday2%2Fself-hosted-edge-functions-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)

[Storage v3: Resumable Uploads with support for 50GB files\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday3%2Fstorage-v3-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/storage-v3-resumable-uploads)

[Supabase Auth: SSO, Mobile, and Server-side support\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday4%2Fsso-support-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-auth-sso-pkce)

[Community Highlight\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fcommunity%2Fcommunity-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/launch-week-7-community-highlights)

[Studio Updates\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fstudio%2Fstudio-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-studio-2.0)

[dbdev\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2Fdbdev-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/dbdev)

[Postgres TLE\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2FpgTLE-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/pg-tle)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finfinite-scroll-with-nextjs-framer-motion&text=Infinite%20scroll%20with%20Next.js%2C%20Framer%20Motion%2C%20and%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finfinite-scroll-with-nextjs-framer-motion&text=Infinite%20scroll%20with%20Next.js%2C%20Framer%20Motion%2C%20and%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Finfinite-scroll-with-nextjs-framer-motion&t=Infinite%20scroll%20with%20Next.js%2C%20Framer%20Motion%2C%20and%20Supabase)

[Last post\\
\\
**The Supabase AI Hackathon** \\
\\
7 April 2023](https://supabase.com/blog/launch-week-7-hackathon)

[Next post\\
\\
**SupaClub** \\
\\
1 April 2023](https://supabase.com/blog/supaclub)

[tutorial](https://supabase.com/blog/tags/tutorial) [launch-week](https://supabase.com/blog/tags/launch-week) [Next.js](https://supabase.com/blog/tags/Next.js)

On this page

- [What is infinite scroll?](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion#what-is-infinite-scroll)
- [Step 0. Load the first batch](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion#step-0-load-the-first-batch)
- [Step 1. Listen to the scroll](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion#step-1-listen-to-the-scroll)
- [Step 2. Check if the container intersects the viewport](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion#step-2-check-if-the-container-intersects-the-viewport)
- [Step 3. Load tickets based on the offset](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion#step-3-load-tickets-based-on-the-offset)
- [Step 4. Animate the tickets](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion#step-4-animate-the-tickets)
- [Step 5. Stop listening when finished](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion#step-5-stop-listening-when-finished)
- [Wrap up](https://supabase.com/blog/infinite-scroll-with-nextjs-framer-motion#wrap-up)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finfinite-scroll-with-nextjs-framer-motion&text=Infinite%20scroll%20with%20Next.js%2C%20Framer%20Motion%2C%20and%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Finfinite-scroll-with-nextjs-framer-motion&text=Infinite%20scroll%20with%20Next.js%2C%20Framer%20Motion%2C%20and%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Finfinite-scroll-with-nextjs-framer-motion&t=Infinite%20scroll%20with%20Next.js%2C%20Framer%20Motion%2C%20and%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)