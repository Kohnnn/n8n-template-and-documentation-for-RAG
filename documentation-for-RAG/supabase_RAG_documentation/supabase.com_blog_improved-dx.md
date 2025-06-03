---
url: "https://supabase.com/blog/improved-dx"
title: "Supabase.js 1.0"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase.js 1.0

30 Oct 2020

•

4 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

**UPDATE 16/08/2022**: supabase-js v2 is out and focuses on “quality-of-life” improvements for developers. V2 includes Type support, new auth methods, realtime multiplayer sneak peek, and more: [**Read the blog post**](https://supabase.com/blog/supabase-js-v2)

### New Docs [\#](https://supabase.com/blog/improved-dx\#new-docs)

Before digging into the improvements, we're excited to point out our new [developer docs](https://supabase.com/docs/reference/javascript/installing). While they're still a work in progress, here are some things we think you'll like:

- The [Reference Docs](https://supabase.com/docs/reference/javascript/installing) are auto-generated from our TypeScript definitions and then enriched with examples. This forces us to document our code and makes it easier to keep everything in sync.
- We added placeholders for the other languages that the community is developing. They have already started with Python, C#, Dart, Rust, and Swift. Expect to see the docs filling up soon!
- We've added sections for all of the open source tools we use, including [Postgres](https://supabase.com/docs/postgres/server/about), PostgREST[1](https://supabase.com/blog/improved-dx#user-content-fn-1), [GoTrue](https://supabase.com/docs/guides/auth/architecture#auth-service), and Realtime[2](https://supabase.com/blog/improved-dx#user-content-fn-2). We'll be filling these with lots of valuable information including self-hosting, benchmarks, and simple guides.

### Errors are returned, not thrown [\#](https://supabase.com/blog/improved-dx\#errors-are-returned-not-thrown)

We attribute this improvement to community feedback. This has significantly improved the developer experience.

Previously we would throw errors:

`
try {
const { body } = supabase.from('todos').select('*')
} catch (error) {
console.log(error)
}
`

And now we simply return them:

`
const { data, error } = supabase.from('todos').select('*')
if (error) console.log(error)\n
// else, carry on ..
`

After testing this for a while we're very happy with this pattern. Errors are handled next to the offending function. Of course you can always rethrow the error if that's your preference.

### We created `gotrue-js` [\#](https://supabase.com/blog/improved-dx\#we-created-gotrue-js)

Our goal for `supabase-js` is to tie together many sub-libraries. Each sub-library is a standalone implementation for a single external system. This is one of the ways we support existing open source tools.

To maintain this philosophy, we created [`gotrue-js`](https://github.com/supabase/gotrue-js), a library for Netlify's GoTrue auth server. This library includes a number of new additions, including third-party logins.

Previously:

`
const {
body: { user },
} = await supabase.auth.signup('someone@email.com', 'password')
`

Now:

`
const { user, error } = await supabase.auth.signUp({
email: 'someone@email.com',
password: 'password',
})
`

### Enhancements and fixes [\#](https://supabase.com/blog/improved-dx\#enhancements-and-fixes)

- Native TypeScript. All of our libraries are now natively built with TypeScript: [`supabase-js`](https://github.com/supabase/supabase-js), [`postgrest-js`](https://github.com/supabase/postgrest-js), [`gotrue-js`](https://github.com/supabase/gotrue-js), and [`realtime-js`](https://github.com/supabase/realtime-js).
- Better realtime scalability: we only generate one socket connection per Supabase client. Previously we would create a connection for every subscription.
- We've added support for OAuth providers.
- 60% of minor bugs outstanding for `supabase-js` have been [solved](https://github.com/supabase/supabase-js/pull/50).
- You can use `select()` instead of `select(*)`

### Breaking changes [\#](https://supabase.com/blog/improved-dx\#breaking-changes)

We've bumped the major version because there are a number of breaking changes. We've detailed these in the [release notes](https://github.com/supabase/supabase-js/releases/tag/v1.0.1), but here are a few to be aware of:

- `signup()` is now `signUp()` and `email` / `password` is passed as an object
- `logout()` is now `signOut()`
- `login()` is now `signIn()`
- `ova()` and `ovr()` are now just `ov()`
- `body` is now `data`

Previously:

`
const { body } = supabase.from('todos').select('*')
`

Now:

`
const { data } = supabase.from('todos').select()
`

### Upgrading [\#](https://supabase.com/blog/improved-dx\#upgrading)

We have documented all of the changes in the [release notes](https://github.com/supabase/supabase-js/releases/tag/v1.0.1).

To summarise the steps:

1. Install the new version: `npm install @supabase/supabase-js@latest`
2. Update all your `body` constants to `data`
3. Update all your `supabase.auth` functions with the new [Auth interface](https://supabase.com/docs/reference/javascript/auth-signup)

### Get started [\#](https://supabase.com/blog/improved-dx\#get-started)

- Start using Supabase today: [supabase.com/dashboard](https://supabase.com/dashboard/)
- Make sure to [star us on GitHub](https://github.com/supabase/supabase)
- Follow us [on Twitter](https://twitter.com/supabase)
- Become a [sponsor](https://github.com/sponsors/supabase)

## Footnotes [\#](https://supabase.com/blog/improved-dx\#footnote-label)

1. Removed link on June 14 2022 for search optimization: page currently does not exist [↩](https://supabase.com/blog/improved-dx#user-content-fnref-1)

2. Removed link on June 14 2022 for search optimization: page currently does not exist [↩](https://supabase.com/blog/improved-dx#user-content-fnref-2)


Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&text=Supabase.js%201.0)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&text=Supabase.js%201.0)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&t=Supabase.js%201.0)

[Last post\\
\\
**Supabase Alpha October 2020** \\
\\
2 November 2020](https://supabase.com/blog/supabase-alpha-october-2020)

[Next post\\
\\
**Supabase Alpha September 2020** \\
\\
3 October 2020](https://supabase.com/blog/supabase-alpha-september-2020)

[supabase](https://supabase.com/blog/tags/supabase)

On this page

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&text=Supabase.js%201.0)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&text=Supabase.js%201.0)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fimproved-dx&t=Supabase.js%201.0)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)