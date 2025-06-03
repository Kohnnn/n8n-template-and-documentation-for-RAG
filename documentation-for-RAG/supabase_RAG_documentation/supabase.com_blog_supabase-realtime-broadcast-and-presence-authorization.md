---
url: "https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization"
title: "Supabase Realtime: Broadcast and Presence Authorization"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Realtime: Broadcast and Presence Authorization

13 Aug 2024

•

8 minute read

[![Filipe Cabaço avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Ffilipecabaco.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Filipe CabaçoEngineering](https://twitter.com/filipecabaco)

![Supabase Realtime: Broadcast and Presence Authorization](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-08-13-supabase-realtime-broadcast-and-presence-authorization%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we're releasing Authorization for Realtime's Broadcast and Presence.

For context, Supabase includes three useful extensions for building real-time applications.

1. [Broadcast](https://supabase.com/docs/guides/realtime/broadcast): Send ephemeral, low-latency messages between users.
2. [Presence](https://supabase.com/docs/guides/realtime/presence): Show when users are online and share state between users.
3. [Postgres Changes](https://supabase.com/docs/guides/realtime/postgres-changes): Listen to Postgres database changes.

This release introduces authorization for Broadcast and Presence using Row Level Security policies:

Securing your Broadcast and Presence messages on Supabase Realtime with RLS - YouTube

Supabase

54.4K subscribers

[Securing your Broadcast and Presence messages on Supabase Realtime with RLS](https://www.youtube.com/watch?v=IXRrU9MpA8Q)

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

Watch on

0:00

/
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=IXRrU9MpA8Q "Watch on YouTube")

To facilitate this, Realtime creates and manages a `messages` table in your Database's `realtime` schema:

![The table that is used to check policies.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-08-13-supabase-realtime-broadcast-and-presence-authorization%2Fschema--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

You can then write RLS Policies for this table and Realtime will then allow or deny clients' access to your Broadcast and Presence Channels:

- `SELECT` Policies - Allow/Deny receiving messages
- `INSERT` Policies - Allow/Deny sending messages

## How Realtime works without Authorization [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#how-realtime-works-without-authorization)

When you want to connect to a Realtime Channel, you can do the following:

`
import { createClient } from '@supabase/supabase-js'
// Prepare client with authenticated user
const client = createClient('<url>', '<anon_key>')
client.realtime.setAuth(token)
// Prepare the realtime channel
const channel = client.channel('topic')
channel
.subscribe((status: string, err: any) => {
if (status === 'SUBSCRIBED') {
    console.log('Connected')
}
})
`

Without Authorization, any authenticated client can subscribe to any _public_ Channel, to send and receive any messages.

## Adding Authorization to Realtime Channels [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#adding-authorization-to-realtime-channels)

You can convert this into an _authorized_ Channel (one that verifies RLS policies) in two steps:

1. [Create RLS Policies](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#create-rls-policies)
2. [Enabling Authorization on Channels](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#enabling-authorization-on-channels)

### 1\. Create RLS Policies [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#1-create-rls-policies)

We'll keep it simple with this example. Let's allow authenticated users to:

- Broadcast: send and receive messages (full access)
- Presence: sync, track, and untrack (full access)

`
create policy "authenticated user listen to all"
on "realtime"."messages"
as permissive
for select -- receive
to authenticated
using ( true );
create policy "authenticated user write to all"
on "realtime"."messages"
as permissive
for insert -- send
to authenticated
with check ( true );
`

We also have a new database function called `realtime.topic()`. You can use this to access the name of the Channel inside your Policies:

`
create policy "authenticated users can only read from 'locked' topic"
on "realtime"."messages"
as permissive
for select   -- read only
to authenticated
using (
realtime.topic() = 'locked'  -- access the topic name
);
`

You can use the `extension` column in the `messages` table to allow/deny specify the Realtime extension:

`
create policy "read access to broadcast and presence"
on "realtime"."messages"
as permissive
for select
to authenticated
using (
realtime.messages.extension in ('broadcast', 'presence') -- specify the topic name
);
`

Reference our [Github Discussion](https://github.com/orgs/supabase/discussions/22484) for more complex use cases.

### 2\. Enabling Authorization on Channels [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#2-enabling-authorization-on-channels)

We've introduced a new configuration parameter `private` to signal to Realtime servers that you want to check authorization on the channel.

If you try to subscribe with an unauthorized user you will get a new error message informing the user that they do not have permission to access the topic.

`
// With anon user
supabase.realtime
.channel('locked', { config: { private: true } })
.subscribe((status: string, err: any) => {
    if (status === 'SUBSCRIBED') {
      console.log('Connected!')
    } else {
      console.error(err.message)
    }
})
// Outputs the following code:
// "You do not have permissions to read from this Topic"
`

But if you connect with an authorized user you will be able to listen to all messages from the “locked” topic

`
// With an authenticated user
supabase.realtime.setAuth(token)
supabase.realtime
.channel('locked', { config: { private: true } })
.subscribe((status: string, err: any) => {
    if (status === 'SUBSCRIBED') {
      console.log('Connected!')
    } else {
      console.error(err.message)
    }
})
// Outputs the following code:
// "Connected!"
`

### Advanced examples [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#advanced-examples)

You can find a more complex example in the [Next.js Authorization Demo](https://github.com/supabase/supabase/tree/master/examples/realtime/nextjs-authorization-demo) where we are using this feature to build chat rooms with restricted access or you could check the [Flutter Figma Clone](https://github.com/supabase/supabase/tree/master/examples/realtime/flutter-figma-clone) to see how you can secure realtime communication between users.

## How does it work? [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#how-does-it-work)

We decided on an approach that keeps your database and RLS policies at the heart of this new authorization strategy.

### Database as a source of security [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#database-as-a-source-of-security)

To achieve Realtime authorization, we looked into our current solutions, namely how [Storage](https://supabase.com/docs/guides/storage/security/access-control) handles Access Control. Due to the nature of Realtime, our primitives are different as we have no assets stored in the database. So how did we achieve it?

On Channel subscription you are able to inform Realtime to use a private Channel and we will do the required checks.

The checks are done by running SELECT and INSERT queries on the new `realtime.messages` table which are then rolled backed so nothing is persisted. Then, based on the query result, we can determine the policies the user has for a given extension.

As a result, in the server, we create a map of policies per connected socket so we can keep them in memory associated with the user's connection.

`
%Policies{
broadcast: %BroadcastPolicies{read: false, write: false},
presence: %PresencePolicies{read: false, write: false}
}
`

### One user, one context, one connection [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#one-user-one-context-one-connection)

Now that we have set up everything on the database side, let's understand how it works and how we can verify authorization via RLS policies.

Realtime uses the private flag client's define when creating channel, takes the headers used to upgrade to the WebSocket connection, claims from your verified JSON Web Token (JWT), loads them into a Postgres transaction using `set_config`, verifies them by querying the `realtime.messages` table, and stores the output as a group of policies within the context of the user's channel on the server.

![Flow of checks done against the database to determine the policies for a user connection.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-08-13-supabase-realtime-broadcast-and-presence-authorization%2Fone-user-connection--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## How is this approach performant? [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#how-is-this-approach-performant)

Realtime checks RLS policies against your database on Channel subscription, so expect a small latency increase initially, but will be cached on the server so all messages will pass from client to server to clients with minimal latency.

Latency between geographically close users is very important for a product like Realtime. To deliver messages as fast as possible between users on our global network, we cache the policies.

We can maintain high throughput and low latency on a Realtime Channel with Broadcast and Presence authorization because:

- the policy is only generated when a user connects to a Channel
- the policy cached in memory is close to your users
- the policy is cached for the duration of the connection, until the JWT expires, or when the user sends a new refresh token

If a user does not have access to a given Channel they won't be able to connect at all and their connections will be rejected.

### Refreshing your Policies [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#refreshing-your-policies)

Realtime will check RLS policies against your database whenever the user connects or there's a new refresh token to make sure that it continues to be authorized despite any changes to its claims. Be aware of your token expiration time to ensure users policies are checked regularly.

### Postgres Changes Support [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#postgres-changes-support)

This method for Realtime Authorization currently only supports Broadcast and Presence. Postgres Changes already adheres to RLS policies on the tables you're listening to so you can continue using that authorization scheme for getting changes from your database.

## Availability [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#availability)

Broadcast and Presence Authorization is available in Public Beta. We are looking for feedback so please do share it in the [GitHub discussion](https://github.com/orgs/supabase/discussions/22484).

## Future Work [\#](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization\#future-work)

We're excited to make Realtime more secure, performant, and stable.

We'll take your feedback, expand this approach, and continue to improve the developer experience as you implement Realtime Authorization for your use cases.

[Launch Week12](https://supabase.com/launch-week/12)

12-16 August

[Day 1 -postgres.new: In-browser Postgres with an AI interface](https://supabase.com/blog/postgres-new)

[Day 2 -Realtime Broadcast and Presence Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)

[Day 3 -Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)

[Day 4 -Introducing Log Drains](https://supabase.com/blog/log-drains)

[Day 5 -Postgres Foreign Data Wrappers with Wasm](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

Build Stage

[01 -GitHub Copilot](https://supabase.com/blog/github-copilot-extension-for-vs-code)

[02 -pg\_replicate](https://news.ycombinator.com/item?id=41209994)

[03 -Snaplet is now open source](https://supabase.com/blog/snaplet-is-now-open-source)

[04 -Supabase Book](https://supabase.com/blog/supabase-book-by-david-lorenz)

[05 -PostgREST](https://supabase.com/blog/postgrest-12-2)

[06 -vec2pg](https://supabase.com/blog/vec2pg)

[07 -pg\_graphql](https://supabase.com/blog/pg-graphql-1-5-7)

[08 -Platform Access Control](https://supabase.com/blog/platform-access-control)

[09 -python-support](https://supabase.com/blog/python-support)

[10 -Launch Week Summary](https://supabase.com/blog/launch-week-12-top-10)

[Community Meetups](https://supabase.com/launch-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-broadcast-and-presence-authorization&text=Supabase%20Realtime%3A%20Broadcast%20and%20Presence%20Authorization)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-broadcast-and-presence-authorization&text=Supabase%20Realtime%3A%20Broadcast%20and%20Presence%20Authorization)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-broadcast-and-presence-authorization&t=Supabase%20Realtime%3A%20Broadcast%20and%20Presence%20Authorization)

[Last post\\
\\
**Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase** \\
\\
14 August 2024](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks)

[Next post\\
\\
**Official Supabase extension for VS Code and GitHub Copilot** \\
\\
12 August 2024](https://supabase.com/blog/github-copilot-extension-for-vs-code)

[realtime](https://supabase.com/blog/tags/realtime) [engineering](https://supabase.com/blog/tags/engineering)

On this page

- [How Realtime works without Authorization](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#how-realtime-works-without-authorization)
- [Adding Authorization to Realtime Channels](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#adding-authorization-to-realtime-channels)
  - [1\. Create RLS Policies](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#1-create-rls-policies)
  - [2\. Enabling Authorization on Channels](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#2-enabling-authorization-on-channels)
  - [Advanced examples](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#advanced-examples)
- [How does it work?](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#how-does-it-work)
  - [Database as a source of security](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#database-as-a-source-of-security)
  - [One user, one context, one connection](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#one-user-one-context-one-connection)
- [How is this approach performant?](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#how-is-this-approach-performant)
  - [Refreshing your Policies](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#refreshing-your-policies)
  - [Postgres Changes Support](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#postgres-changes-support)
- [Availability](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#availability)
- [Future Work](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization#future-work)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-broadcast-and-presence-authorization&text=Supabase%20Realtime%3A%20Broadcast%20and%20Presence%20Authorization)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-broadcast-and-presence-authorization&text=Supabase%20Realtime%3A%20Broadcast%20and%20Presence%20Authorization)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-broadcast-and-presence-authorization&t=Supabase%20Realtime%3A%20Broadcast%20and%20Presence%20Authorization)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![The table that is used to check policies.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-08-13-supabase-realtime-broadcast-and-presence-authorization%2Fschema--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![Flow of checks done against the database to determine the policies for a user connection.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-08-13-supabase-realtime-broadcast-and-presence-authorization%2Fone-user-connection--dark.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)