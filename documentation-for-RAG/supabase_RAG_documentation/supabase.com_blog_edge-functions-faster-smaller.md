---
url: "https://supabase.com/blog/edge-functions-faster-smaller"
title: "Edge Functions are now 2x smaller and boot 3x faster"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Edge Functions are now 2x smaller and boot 3x faster

12 Sep 2024

•

7 minute read

[![Nyannyacha avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fnyannyacha.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
NyannyachaEngineering](https://github.com/nyannyacha)

![Edge Functions are now 2x smaller and boot 3x faster](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fedge-functions-faster-smaller%2Fedge-fns-faster-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We’ve rolled out some exciting updates to Edge Functions which bring significant reductions to function size and boot time. If you’re using [npm modules](https://supabase.com/blog/edge-functions-node-npm) in your functions, you should see function sizes being halved and boot time reduced by 300% in most cases.

To take advantage of these performance improvements, you can redeploy your functions using the Supabase CLI v1.192.5 or later.

Let’s compare the bundle size and boot time using some popular examples.

## Benchmarks [\#](https://supabase.com/blog/edge-functions-faster-smaller\#benchmarks)

**Supabase JavaScript Client:**

|  | **CLI 1.190.0** | **CLI 1.192.5** | **Change** |
| --- | --- | --- | --- |
| Bundle size | 1.487MB | 640.4KB | -232.34% |
| Boot time | 275ms | 25ms | -1100% |

`
import { createClient } from 'npm:@supabase/supabase-js@2'
Deno.serve(async (_req) => {
try {
    const supabase = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_ANON_KEY') ?? '',
      { global: { headers: { Authorization: req.headers.get('Authorization')! } } }
    )
    const { data, error } = await supabase.from('countries').select('*')
    if (error) {
      throw error
    }
    return new Response(JSON.stringify({ data }), {
      headers: { 'Content-Type': 'application/json' },
      status: 200,
    })
} catch (err) {
    return new Response(String(err?.message ?? err), { status: 500 })
}
})
`

**OpenAI:**

|  | **CLI 1.190.0** | **CLI 1.192.5** | **Change** |
| --- | --- | --- | --- |
| Bundle size | 2.533MB | 1.045MB | -242.39% |
| Boot time | 459ms | 57ms | -805.26% |

`
import OpenAI from 'npm:openai@4.57.3'
const client = new OpenAI({
apiKey: Deno.env.get('OPEN_AI_KEY'),
})
Deno.serve(async (req) => {
const { query } = await req.json()
const chatCompletion = await client.chat.completions.create({
    messages: [{ role: 'user', content: 'Say this is a test' }],
    model: 'gpt-3.5-turbo',
})
return new Response(chatCompletion)
})
`

**Drizzle / node-postgres:**

|  | **CLI 1.190.0** | **CLI 1.192.5** | Change |
| --- | --- | --- | --- |
| Bundle size | 929.5kB | 491.3kB | -189.19% |
| Boot time | 301ms | 83ms | -362.65% |

`
import { drizzle } from 'npm:drizzle-orm@0.33.0/node-postgres'
import pg from 'npm:pg@8.12.0'
const { Client } = pg
import { pgTable, serial, text, varchar } from 'npm:drizzle-orm@0.33.0/pg-core'
export const users = pgTable('users', {
id: serial('id').primaryKey(),
fullName: text('full_name'),
phone: varchar('phone', { length: 256 }),
})
const client = new Client({
connectionString: Deno.env.get('SUPABASE_DB_URL'),
})
await client.connect()
const db = drizzle(client)
Deno.serve(async (req) => {
const allUsers = await db.select().from(users)
console.log(allUsers)
return new Response('ok')
})
`

## How did we achieve these gains? [\#](https://supabase.com/blog/edge-functions-faster-smaller\#how-did-we-achieve-these-gains)

Let’s dive into the technical details.

### Lazy evaluating dependencies and reducing npm package section size [\#](https://supabase.com/blog/edge-functions-faster-smaller\#lazy-evaluating-dependencies-and-reducing-npm-package-section-size)

We use [eszip format](https://github.com/denoland/eszip) to bundle your function code and its dependencies when you deploy a function.

This binary format extracts the dependencies a function references from Deno's module graph and serializes them into a single file. It eliminates network requests at run time and avoids conflicts between dependencies.

This approach worked reasonably well until we added npm support. When functions started using npm modules, bundle sizes and boot times increased.

When a function is invoked, Edge Runtime loads the eszip binary for the function and passes it to a JavaScript worker (ie. isolate). The worker then loads the necessary modules from the eszip.

In the original implementation, before passing an eszip binary to the worker's module loader, we first checked the integrity of its contents. Each entry in it will have a checksum computed with the SHA-256 function immediately following the body bytes. By reading this and comparing it, we ensure that the eszip binary isn’t corrupted.

The problem is that calculating a checksum for every entry using SHA-256 is quite expensive, and we were pre-checking the integrity of all entries at a time when the worker doesn't even need that particular entry.

It is possible that some items that have been checked for integrity will not be referenced even if the worker reaches the end of its lifetime and reaches the end state.

Instead of performing the costly integrity check of all entries before passing it to the module loader, edge runtime lazily performs the integrity check whenever there is a request to load a specific entry from the eszip by the module loader.

This helped to significantly to reduce the boot times.

Another issue was that while serializing npm packages for embedding into eszip binaries, we used the JSON format. The entries in individual npm packages, which were already represented as bytes ( `Vec<u8>`), were encoded as an array representation in JSON format ( `[255, 216, 255, 224, 0, ...]`) instead of passing on as bytes, causing the outputs to bloat by up to 2x or more.

We refactored the serialization using the [`rkyv` crate](https://github.com/rkyv/rkyv) to encode this to lower to the byte level, which helped reducing the bundle sizes of eszip binaries containing npm packages.

You can find full details of the implementation in this PR [https://github.com/supabase/edge-runtime/pull/343](https://github.com/supabase/edge-runtime/pull/343)

### Using a more computationally efficient hashing function [\#](https://supabase.com/blog/edge-functions-faster-smaller\#using-a-more-computationally-efficient-hashing-function)

There was a [recent change](https://github.com/denoland/eszip/pull/181) in the eszip crate, which allowed the configuration of the source checksum.

This allowed us to switch to xxHash-3 over SHA\_256 for the source checksums. Given that the checksums are used to ensure the integrity of sources in eszip, we could rely on a non-cryptographic hash algorithm that’s more computationally efficient.

![comparison of hash functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fedge-functions-faster-smaller%2Fhash-functions.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## How to redeploy your functions [\#](https://supabase.com/blog/edge-functions-faster-smaller\#how-to-redeploy-your-functions)

To get the advantage of these optimizations, follow these steps:

- [Update Supabase CLI](https://supabase.com/docs/guides/cli/getting-started#updating-the-supabase-cli) to version is v1.195.2 or later.
- Then, redeploy your functions by running `supabase functions deploy [FUNCTION_NAME]`

## Getting Help [\#](https://supabase.com/blog/edge-functions-faster-smaller\#getting-help)

[Supabase Edge Runtime](https://github.com/supabase/edge-runtime) is fully open-source, and we value community contributions. If you would like to make any improvements, feel free to dive into the source and [create an issue](https://github.com/supabase/edge-runtime/issues).

If you have any issues with Edge Functions in your hosted project, please request support via [superbase.help](http://supabase.help/).

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&text=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&text=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&t=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)

[Last post\\
\\
**Local-first Realtime Apps with Expo and Legend-State** \\
\\
23 September 2024](https://supabase.com/blog/local-first-expo-legend-state)

[Next post\\
\\
**Building an Uber Clone with Flutter and Supabase** \\
\\
5 September 2024](https://supabase.com/blog/flutter-uber-clone)

[functions](https://supabase.com/blog/tags/functions)

On this page

- [Benchmarks](https://supabase.com/blog/edge-functions-faster-smaller#benchmarks)
- [How did we achieve these gains?](https://supabase.com/blog/edge-functions-faster-smaller#how-did-we-achieve-these-gains)
  - [Lazy evaluating dependencies and reducing npm package section size](https://supabase.com/blog/edge-functions-faster-smaller#lazy-evaluating-dependencies-and-reducing-npm-package-section-size)
  - [Using a more computationally efficient hashing function](https://supabase.com/blog/edge-functions-faster-smaller#using-a-more-computationally-efficient-hashing-function)
- [How to redeploy your functions](https://supabase.com/blog/edge-functions-faster-smaller#how-to-redeploy-your-functions)
- [Getting Help](https://supabase.com/blog/edge-functions-faster-smaller#getting-help)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&text=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&text=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-functions-faster-smaller&t=Edge%20Functions%20are%20now%202x%20smaller%20and%20boot%203x%20faster)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)