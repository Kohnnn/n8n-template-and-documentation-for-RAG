---
url: "https://supabase.com/blog/supabase-js-v2"
title: "supabase-js v2"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# supabase-js v2

16 Aug 2022

•

8 minute read

[![Inian Parameshwaran avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F2155545%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Inian ParameshwaranEngineering](https://twitter.com/everConfusedGuy)

[![Alaister Young avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Falaister.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Alaister YoungEngineering](https://github.com/alaister)

![supabase-js v2](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-supabase-js%2Fthumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

⚠️ UPDATED 20/10: supabase-js v2 is fully released 🥳

[Check the updated docs](https://supabase.com/docs/reference/javascript) and [migration guide](https://supabase.com/docs/reference/javascript/v1/upgrade-guide).

Today we're publishing a release candidate for [supabase-js v2](https://github.com/supabase/supabase-js), which focuses on “quality-of-life” improvements for developers.

Try it out by running `npm i @supabase/supabase-js@rc`

Nearly 2 years ago we [released supabase-js v1](https://supabase.com/blog/improved-dx).
Since then it has been used in over [17K repositories](https://github.com/supabase/supabase-js/network/dependents?package_id=UGFja2FnZS04MjM3OTUyMDU%3D) and has grown
to [50K weekly downloads](https://www.npmjs.com/package/@supabase/supabase-js). Supabase users give a lot of great feedback and we've
learned some of the largest pain-points as a result.

## Major Updates [\#](https://supabase.com/blog/supabase-js-v2\#major-updates)

This release focuses on solving these pain-points. At the same time we want to make the upgrade path for supabase-js as easy as possible,
so we've been strategic about the changes we're making. We plan to follow this model going forward: incremental changes over huge rewrites.

### Type support [\#](https://supabase.com/blog/supabase-js-v2\#type-support)

If you followed yesterday's announcement, you will have noticed that we added
[type generators](https://supabase.com/docs/reference/cli/usage#supabase-gen-types) to the CLI.

`
supabase start
supabase gen types typescript --local > DatabaseDefinitions.ts
`

These types can now be used to enrich your development experience:

`
import type { Database } from './DatabaseDefinitions'
const supabase = createClient<Database>(SUPABASE_URL, ANON_KEY)
const { data } = await supabase.from('messages').select().match({ id: 1 })
`

ℹ️ Differences from v1

v1 also supported types, but the types were generated from the API rather than the database, so it
lost a lot of detailed information. The library also required you to specify the definition in
every method call, rather than at the client level.

`
supabase.from<Database['Message']>('messages').select('*')
`

* * *

### New Auth methods [\#](https://supabase.com/blog/supabase-js-v2\#new-auth-methods)

We're removing the `signIn()` method in favor of more explicit method signatures:
`signInWithPassword()`, and `signInWithOtp()`.

`
// v2
const { data } = await supabase.auth.signInWithPassword({
email: 'hello@example',
password: 'pass',
})
// v1
const { data } = await supabase.auth.signIn({
email: 'hello@example',
password: 'pass',
})
`

This helps with type hinting. Previously it was difficult for developers to know what they were missing.
A lot of developers didn't even realize they could use passwordless magic links.

* * *

### Data methods return minimal by default [\#](https://supabase.com/blog/supabase-js-v2\#data-methods-return-minimal-by-default)

The `insert()`, `update()`, and `upsert()` methods now require you to explicitly append `select()` if you want the data to be returned.

`
// v2
const { data } = await supabase.from('messages').insert({ id: 1, message: 'Hello world' }).select() // select is now explicitly required
// v1
const { data } = await supabase.from('messages').insert({ id: 1, message: 'Hello world' }) // insert would also "select()"
`

This was another common question in our GitHub Discussions. While the idea of automatically returning data is great,
developers often turn on Row Level Security (which is great), and then they forget to add a `select` Policy.
It is a bit surprising that you need to add a `select` policy to do an `insert`, so we opted for the “principle of least surprise”.
If you don't append `select()`, the `data` value will be an empty object: `{}`.

ℹ️ Differences from v1

Previously you could pass a `returning: 'minimal'` option to the `insert()`, `update()`, and
`upsert()` statements. We've now made this the default behaviour.

* * *

### Auth Admin methods [\#](https://supabase.com/blog/supabase-js-v2\#auth-admin-methods)

We've move all server-side Auth methods from `supabase.auth.api` to `supabase.auth.admin`:

`
// v2
const { data: user, error } = await supabase.auth.admin.listUsers()
// v1
const { data: user, error } = await supabase.auth.api.listUsers()
`

All `admin` methods expect a `SERVICE_ROLE` key.
This change makes it clear that any methods under the `admin` namespace should only be used on a trusted server-side environment.

* * *

### Async Auth overhaul [\#](https://supabase.com/blog/supabase-js-v2\#async-auth-overhaul)

We've rebuilt the Auth library, making it async for almost all methods.

`
// v2
const { data } = await supabase.auth.getSession()
// v1
const { data } = supabase.auth.session()
`

This solves the “getting logged out” issue, which has been a recurring challenge in our GitHub Discussions.

ℹ️ Improvements from v1

The previous implementation had a race condition when refreshing the auth token across multiple tabs. The async re-write forces the library to wait
for a valid/invalid session before taking any action.

* * *

### Scoped constructor config [\#](https://supabase.com/blog/supabase-js-v2\#scoped-constructor-config)

We're being much more explicit about the modular approach that `supabase-js` uses:

`
const supabase = createClient(apiURL, apiKey, {
db: {
    schema: 'public',
},
auth: {
    autoRefreshToken: true,
    persistSession: true,
},
realtime: {
    channels,
    endpoint,
},
// common across all libraries
global: {
    fetch: customFetch,
    headers: DEFAULT_HEADERS,
},
})
`

This is clearer for developers - if you're only using some parts of Supabase, you only receive the hints for those parts.

ℹ️ Improvements from v1

We noticed a lot of confusion for the variable naming between each library.
For example, Auth has a config parameter called "storageKey", which was was often confused with the `storage-js` library bundled in the `supabase-js` library.

* * *

### Better Errors [\#](https://supabase.com/blog/supabase-js-v2\#better-errors)

We've created error types for all of the sub-libraries in `supabase-js`. Here's a example for Edge Functions:

`
import { FunctionsHttpError, FunctionsRelayError, FunctionsFetchError } from '@supabase/supabase-js'
const { data: user, error } = await supabase.functions.invoke('hello')
if (error instanceof FunctionsHttpError) {
console.log('Function returned an error', error.message)
} else if (error instanceof FunctionsRelayError) {
console.log('Relay error:', error.message)
} else if (error instanceof FunctionsFetchError) {
console.log('Fetch error:', error.message)
}
`

* * *

### Improvements for Edge Functions [\#](https://supabase.com/blog/supabase-js-v2\#improvements-for-edge-functions)

`supabase-js` now automatically detects the content type for the request/response bodies for all Edge Function invocations:

`
// v2
const { data: user, error } = await supabase.functions.invoke('hello', {
body: { foo: 'bar' },
})
// v1
const { data: user, error } = await supabase.functions.invoke('hello', {
headers: { 'Content-Type': 'application/json' }
body: JSON.stringify({ foo: 'bar' }),
})
`

This improvement inspired by a Supabase community member. Thanks [@vejja](https://github.com/supabase/functions-js/pull/23)!

* * *

### Multiplayer Sneak Peek [\#](https://supabase.com/blog/supabase-js-v2\#multiplayer-sneak-peek)

There is a new `channel()` interface which are releasing in v2.
This is a "preparatory" release for our upcoming [multiplayer](https://supabase.com/blog/supabase-realtime-with-multiplayer-features) features.

`
supabase
.channel('any_string_you_want')
.on('presence', { event: 'track' }, (payload) => {
    console.log(payload)
})
.subscribe()
`

As part of this change, the old `from().on().subscribe()` method for listening to database changes will be changing:

`
// v2
supabase
.channel('any_string_you_want')
.on(
    'postgres_changes',
    {
      event: 'INSERT',
      schema: 'public',
      table: 'movies',
    },
    (payload) => {
      console.log(payload)
    }
)
.subscribe()
// v1
supabase
.from('movies')
.on('INSERT', (payload) => {
    console.log(payload)
})
.subscribe()
`

You can listen to PostgreSQL database changes on any channel you want by subscribing to the `'postgres_changes'` event.
For now, we will continue to support `from().on().subscribe()`, but in the future we will deprecate this in favor of the `channel().on().subscribe()` method.

* * *

## Community [\#](https://supabase.com/blog/supabase-js-v2\#community)

Version 2.0 is the result of the combined work of over 100 contributors to our libraries, and over 450 contributors to our docs and websites.
If you're one of those contributors, thank you.

- [`functions-js`](https://github.com/supabase/functions-js/graphs/contributors) (4)
- [`gotrue-js`](https://github.com/supabase/gotrue-js/graphs/contributors) (47)
- [`postgrest-js`](https://github.com/supabase/postgrest-js/graphs/contributors) (30)
- [`realtime-js`](https://github.com/supabase/realtime-js/graphs/contributors) (16)
- [`storage-js`](https://github.com/supabase/storage-js/graphs/contributors) (17)
- [`supabase-js`](https://github.com/supabase/supabase-js/graphs/contributors) (39)

Special shout outs to: [@vejja](https://github.com/vejja), [@pixtron](https://github.com/pixtron), [@bnjmnt4n](https://github.com/pixtron), and [@karlseguin](https://github.com/karlseguin).

## Migrating to v2 [\#](https://supabase.com/blog/supabase-js-v2\#migrating-to-v2)

Update today by running:

`
npm i @supabase/supabase-js@2
`

[Migration guide](https://supabase.com/docs/reference/javascript/v1/upgrade-guide)

We'll continuing merging security fixes to v1, with maintenance patches for the next three months.

## Announcement video and discussion [\#](https://supabase.com/blog/supabase-js-v2\#announcement-video-and-discussion)

Supabase Launch Week 5: Day 2 - supabase-js v2 Release Candidate - YouTube

Supabase

54.4K subscribers

[Supabase Launch Week 5: Day 2 - supabase-js v2 Release Candidate](https://www.youtube.com/watch?v=iqZlPtl_b-I)

Supabase

Search

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

Full screen is unavailable. [Learn More](https://support.google.com/youtube/answer/6276924)

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

[Watch on YouTube](https://www.youtube.com/watch?v=iqZlPtl_b-I "Watch on YouTube")

## supabase-js v2 resources [\#](https://supabase.com/blog/supabase-js-v2\#supabase-js-v2-resources)

- [v2 Documentation](https://supabase.com/docs/reference/javascript)
- [Migration guide](https://supabase.com/docs/reference/javascript/v1/upgrade-guide)
- [Next.js quickstart guide](https://supabase.com/docs/guides/with-nextjs)
- [Examples](https://github.com/supabase/supabase/tree/master/examples)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-v2&text=supabase-js%20v2)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-v2&text=supabase-js%20v2)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-v2&t=supabase-js%20v2)

[Last post\\
\\
**Supabase is SOC2 compliant** \\
\\
17 August 2022](https://supabase.com/blog/supabase-soc2)

[Next post\\
\\
**Supabase CLI v1 and Management API Beta** \\
\\
15 August 2022](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Major Updates](https://supabase.com/blog/supabase-js-v2#major-updates)
  - [Type support](https://supabase.com/blog/supabase-js-v2#type-support)
  - [New Auth methods](https://supabase.com/blog/supabase-js-v2#new-auth-methods)
  - [Data methods return minimal by default](https://supabase.com/blog/supabase-js-v2#data-methods-return-minimal-by-default)
  - [Auth Admin methods](https://supabase.com/blog/supabase-js-v2#auth-admin-methods)
  - [Async Auth overhaul](https://supabase.com/blog/supabase-js-v2#async-auth-overhaul)
  - [Scoped constructor config](https://supabase.com/blog/supabase-js-v2#scoped-constructor-config)
  - [Better Errors](https://supabase.com/blog/supabase-js-v2#better-errors)
  - [Improvements for Edge Functions](https://supabase.com/blog/supabase-js-v2#improvements-for-edge-functions)
  - [Multiplayer Sneak Peek](https://supabase.com/blog/supabase-js-v2#multiplayer-sneak-peek)
- [Community](https://supabase.com/blog/supabase-js-v2#community)
- [Migrating to v2](https://supabase.com/blog/supabase-js-v2#migrating-to-v2)
- [Announcement video and discussion](https://supabase.com/blog/supabase-js-v2#announcement-video-and-discussion)
- [supabase-js v2 resources](https://supabase.com/blog/supabase-js-v2#supabase-js-v2-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-v2&text=supabase-js%20v2)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-v2&text=supabase-js%20v2)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-js-v2&t=supabase-js%20v2)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)