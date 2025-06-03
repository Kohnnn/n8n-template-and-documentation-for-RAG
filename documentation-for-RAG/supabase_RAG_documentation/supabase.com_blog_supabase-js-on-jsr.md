---
url: "https://supabase.com/blog/supabase-js-on-jsr"
title: "Announcing Supabase on JSR"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Announcing Supabase on JSR

16 Jul 2024

•

2 minute read

[![Bobbie Soedirgo avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsoedirgo.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Bobbie SoedirgoEngineering](https://github.com/soedirgo)

[![Thor Schaeff avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fthorwebdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Thor SchaeffDevRel & DX](https://twitter.com/thorwebdev)

![Announcing Supabase on JSR](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fjsr_supabase%2Fjsr_supabase.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Prefer Deno's awesome visuals? Read the announcement on [Deno's blog](https://deno.com/blog/supabase-on-jsr).

[JSR](https://jsr.io/) is a modern [open source](https://github.com/jsr-io/jsr) JavaScript registry that simplifies publishing and importing JavaScript and TypeScript modules. JSR supports publishing TypeScript source code, auto-generating documentation and type definition files, provenance attestation for more security, and can be used with npm-like package managers. Since its launch, over 250 new packages are being published each week.

We're thrilled to announce that our [JavaScript client library](https://jsr.io/@supabase/supabase-js) is now available on JSR.

As many of you know, our JavaScript library, `supabase-js`, is composed of [many sub-clients](https://github.com/supabase-community#client-libraries) that let you query your Supabase [database](https://supabase.com/database), subscribe to [real-time events](https://supabase.com/realtime), upload and download [files](https://supabase.com/storage), manage [auth](https://supabase.com/auth), invoke Deno powered [Edge Functions](https://supabase.com/edge-functions), and [more](https://supabase.com/vector). It's fully isomorphic and can be used across any environment that speaks JavaScript and HTTPS, such as browsers, servers, and [the edge](https://deno.com/blog/the-future-of-web-is-on-the-edge)!

Using supabase-js via JSR offers an excellent developer experience, with first class TypeScript support, auto-generated documentation accessible in your code editor, and more.

## Installing Supabase [\#](https://supabase.com/blog/supabase-js-on-jsr\#installing-supabase)

You can get started with Supabase using the `deno add` command:

`
deno add @supabase/supabase-js
`

Or using npm:

`
npx jsr add @supabase/supabase-js
`

The above commands will generate a `deno.json` file, listing all your project dependencies.

deno.json

`
{
"imports": {
    "@supabase/supabase-js": "jsr:@supabase/supabase-js@2"
}
}
`

You can then import the client library to your `main.ts` file:

main.ts

`
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('https://xyzcompany.supabase.co', 'public-anon-key')
console.log('Supabase Instance: ', supabase)
`

Finally, you can run the following command to execute:

`
deno run -A main.ts
`

Check out the [`supabase-js` README](https://jsr.io/@supabase/supabase-js) to see how to use it in other environments.

## What's next? [\#](https://supabase.com/blog/supabase-js-on-jsr\#whats-next)

With the Supabase client on JSR, you can easily and quickly add authentication or persistent storage to your projects, which can run in any JavaScript environment!

- [Check out JSR](https://jsr.io/) the JavaScript registry built for the modern web.
- Read the announcement on [Deno's blog](https://deno.com/blog/supabase-on-jsr).

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-on-jsr&text=Announcing%20Supabase%20on%20JSR)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-on-jsr&text=Announcing%20Supabase%20on%20JSR)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-on-jsr&t=Announcing%20Supabase%20on%20JSR)

[Last post\\
\\
**postgres.new: In-browser Postgres with an AI interface** \\
\\
12 August 2024](https://supabase.com/blog/postgres-new)

[Next post\\
\\
**Supabase Security Suite** \\
\\
11 July 2024](https://supabase.com/blog/hardening-supabase)

[javascript](https://supabase.com/blog/tags/javascript) [deno](https://supabase.com/blog/tags/deno)

On this page

- [Installing Supabase](https://supabase.com/blog/supabase-js-on-jsr#installing-supabase)
- [What's next?](https://supabase.com/blog/supabase-js-on-jsr#whats-next)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-on-jsr&text=Announcing%20Supabase%20on%20JSR)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-on-jsr&text=Announcing%20Supabase%20on%20JSR)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-on-jsr&t=Announcing%20Supabase%20on%20JSR)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)