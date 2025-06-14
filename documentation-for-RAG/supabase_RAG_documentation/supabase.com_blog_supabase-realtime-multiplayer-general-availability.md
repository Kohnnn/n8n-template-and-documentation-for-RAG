---
url: "https://supabase.com/blog/supabase-realtime-multiplayer-general-availability"
title: "Realtime: Multiplayer Edition"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Realtime: Multiplayer Edition

18 Aug 2022

•

10 minute read

[![Wen Bo Xie avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fw3b6x9.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Wen Bo XieProduct](https://twitter.com/wenboxie)

[![Stanislav Muzhyk avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fabc3.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Stanislav MuzhykEngineering](https://github.com/abc3)

![Realtime: Multiplayer Edition](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-realtime%2Fthumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

During our last Launch Week, we teased our plans for "multiplayer" features. If you need a refresher,
take a glance at [Supabase Realtime, with Multiplayer Features](https://supabase.com/blog/supabase-realtime-with-multiplayer-features)
or go to [multiplayer.dev](https://multiplayer.dev/) for an interactive demo.

Today, we're excited to announce the general availability of Realtime's multiplayer features, Broadcast and Presence.

## TLDR [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#tldr)

Here are the key takeaways:

- We've added [Broadcast](https://supabase.com/docs/guides/realtime/broadcast) and [Presence](https://supabase.com/docs/guides/realtime/presence) to our Realtime server. You can use these features with the new [supabase-js](https://supabase.com/docs/reference/javascript/next) release.
- All active Supabase projects on the Free Plan have access to the these features.
- All new Supabase projects created from August 18th have access to these features.
- We will work with all other projects to migrate to the new Realtime over the next few weeks. If you want immediate access, [reach out](https://supabase.com/dashboard/support/new).
- [Chris McCord](https://twitter.com/chris_mccord), the creator of Phoenix Framework, is now a technical advisor.

## Background [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#background)

Before we discuss the new features, let's review what Realtime is and its significance to Supabase. Skip ahead if you just want to see the new features!

The first iteration of Realtime server was written by [@kiwicopple](https://twitter.com/kiwicopple), our CEO.
At his previous startup, a chat application he built was facing performance issues while broadcasting database changes from Firestore to individual subscribers.

He turned to Postgres, which has two built-in pieces of functionality for emitting database changes:

- The first, Postgres's LISTEN/NOTIFY, seems like the obvious choice because it conveniently does what its name implies, listen for changes and notify subscribers. However, this approach has a hidden limitation - NOTIFY has a payload limit of 8,000 bytes. The workaround is to send only a unique identifier and then have the client query the database for the specific change. This would have been been too slow for the chat application.
- The second, Postgres's logical replication, doesn't face the same limitations, and Paul used this approach. This required the introduction of a server to listen to a logical replication slot. Paul chose [Elixir](https://elixir-lang.org/) and the [Phoenix Framework](https://www.phoenixframework.org/) for the server as it scales exceptionally well, especially when dealing with WebSockets. He named this server " [Realtime](https://github.com/supabase/realtime)," leveraging other open source projects, [cainophile](https://github.com/cainophile/cainophile) and [pgoutput\_decoder](https://github.com/cainophile/pgoutput_decoder), to listen to the replication stream and decode changes. From there, the changes were serialized into JSON and sent on their merry way to clients.

Realtime was the very first open source project of Supabase and played a pivotal role in our founding. Over time, we've improved both the performance and security.
During Launch Week 3, we announced [Realtime RLS](https://supabase.com/blog/realtime-row-level-security-in-postgresql), which allows developers to tap into Postgres's Row Level Security to authorize changes before broadcasting them to clients. This enabled developers to use the same security framework across the entire Supabase stack.

## Realtime Channels [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#realtime-channels)

We've modified the architecture of Realtime to introduce two core features: Broadcast and Presence.

In this new version, everything is a [Channel](https://hexdocs.pm/phoenix/Phoenix.Channel.html). Channels are like “Rooms” where participants can join, and leave - very similar to Slack Channels or Discord Channels.

Broadcast and Presence are built into every Channel, and we've retro-fitted the Database change events into Channels too.

### Broadcast [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#broadcast)

Broadcast follows the classic Publisher/Subscriber pattern. A client (publisher) “broadcasts” messages using a unique identifier. For example, a user could send a message to a `#random` channel.

Other clients (subscribers) can “listen” to these messages in real-time, using the unique identifier. If they are listening to the `#random` channel, then they will receive the message.

This functionality is [baked into the Phoenix framework](https://hexdocs.pm/phoenix/Phoenix.Channel.html) and we've already been using this to [broadcast Postgres changes](https://supabase.com/docs/reference/javascript/subscribe).
With this release we're exposing the underlying primitives which unlocks a variety of use-cases for developers.

A common use-case is sharing a user's cursor position with other clients in an online game. Previously, developers were sending all the mouse movements through their Postgres database which added latency and degraded database performance. In contrast, Broadcasts are ephemeral - they bypass the database completely.

### Presence [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#presence)

Presence synchronizes shared state between users. Presence is very similar to Broadcast, except that the state is “persisted” in the Channel so that new joiners immediately receive the state without waiting for another user to broadcast it. In our Slack example, when you turn on Slack you can see who's online without each individual user sending an “I'm online” message to the new-joiner.

Presence utilizes Broadcast as the transport layer, consolidating the state in an eventually-consistent and conflict-free manner. Users are free to come-and-go as they please, and as long as they are all subscribed to the same Channel then they will all have the same Presence state as each other.

The neat thing about Presence is that if a user is suddenly disconnected (for example, they go offline), their state will be automatically removed from the shared state.
If you've ever tried to build an “I'm online” feature which handles unexpected disconnects, you'll appreciate how useful this is.

## Client Library [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#client-library)

We've introduced new functionality into the [release candidate](https://supabase.com/blog/supabase-js-v2) version of `supabase-js`.

Here's a taste of how you can start using Broadcast and Presence and continue to listen to Postgres changes.

### Broadcast Example [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#broadcast-example)

In this example we'll send and receive mouse cursor positions to anyone in `room_1`.

``
const channel = supabase.channel('room_1')
const MOUSE_EVENT = 'cursor'
// Subscribe to mouse events.
// Our second parameter filters only for mouse events.
channel
.on('broadcast', { event: MOUSE_EVENT }, (event) => {
    receivedCursorPosition(event)
})
.subscribe()
// Handle a mouse event.
const receivedCursorPosition = ({ event, payload }) => {
console.log(`
		User: ${payload.userId}
		x Position: ${payload.x}
		y Position: ${payload.y}
	`)
}
// Helper function for sending our own mouse position.
const sendMousePosition = (channel, userId, x, y) => {
return channel.send({
    type: 'broadcast',
    event: MOUSE_EVENT,
    payload: { userId, x, y },
})
}
``

### Presence Example [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#presence-example)

Let's create a contrived example where we could display a “user is typing” indicator.
In this case, we'll send the timestamp for the last time that a user hit a key.
Other clients can use this timestamp to display a “typing…” indicator.

`
const userId = 'user_1234'
const slackRoomId = '#random'
const channel = supabase.channel(slackRoomId, {
config: {
    presence: { key: userId }
}
})
// We can subscribe to all Presence changes using the 'presence' -> 'sync' event.
channel
.on('presence', { event: 'sync' }, () => presenceChanged())
.subscribe()
/*
A contrived example where we bind to all keyboard
events and send them over our channel
*/
document.addEventListener('keydown', function(event){
channel.track({ isTyping: Date.now() })
})
// Receive Presence updates
const presenceChanged = () => {
const newState = channel.presenceState()
console.log(newState)
}
// When you no longer wish to track data
channel.untrack().then(status => console.log(status)
`

### Receiving Postgres Changes [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#receiving-postgres-changes)

You can receive Postgres changes on any channel. For this example, we'll receive all messages on the `#random` channel.

``
const channelId = '#random'
// Create a filter only for new messages
const databaseFilter = {
schema: 'public',
table: 'messages',
filter: `room_id=eq.${channelId}`,
event: 'INSERT',
}
const channel = supabase
.channel(channelId)
.on('postgres_changes', databaseFilter, (payload) => receivedDatabaseEvent(payload))
.subscribe()
const receivedDatabaseEvent = (event) => {
const { payload } = event
console.log(payload)
}
``

## Future Plans [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#future-plans)

This is a big change, but it's only a small step towards the final goal. We have a few exciting plans for the future.

### Extensions [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#extensions)

Our `postgres_changes` listener is the first of many [Extensions](https://supabase.com/blog/supabase-realtime-with-multiplayer-features#extensions).
We've had requests add other integrations beyond Postgres:

- **Finance:** Listen to stock market events and broadcast them to connected users
- **Web3:** Listen to blockchain events and broadcast them to connected users
- **Authoritative clocks:** A server clock which broadcasts a timer (e.g. auction sites or ticketing systems)

### Peer to Peer [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#peer-to-peer)

A lot of users ask about using Realtime for peer to peer applications. We plan to use Realtime as a WebRTC signaling server which will enable developers to build collaborative software with even lower latency. A common example we've seen is collaborative code editors with a CRDT implementation, like Yjs.

### Realtime Inspector [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#realtime-inspector)

We're building a Realtime inspector into the Supabase Dashboard so it'll be easier to debug the messages that are getting passed through your Channels.

## Technical Overview [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#technical-overview)

Before this release, every Supabase project had a server running Realtime with the other Supabase services like Kong, GoTrue, and PostgREST.

In this release we take advantage of Elixir's strengths by running a distributed cluster of servers across the world. Each server communicates directly with the other nodes in the cluster. This improves performance by balancing the load across nodes.

Clients connect to the nearest node in the cluster, and we take advantage of the cluster's fast backbone network to improve client connection speeds, stability, and latency. This is especially useful for clients in regions with variable internet quality.

The entire cluster runs on [Fly](https://fly.io/) \- we're big fans!

Much of the new functionality leverages the [Phoenix Framework](https://www.phoenixframework.org/). This makes it relatively straightforward to offer Broadcast ( [Phoenix PubSub](https://hexdocs.pm/phoenix_pubsub/Phoenix.PubSub.html)) and Presence ( [Phoenix Presence](https://hexdocs.pm/phoenix/Phoenix.Presence.html)) in a globally-distributed cluster. Presence is built on top of [Phoenix Tracker](https://hexdocs.pm/phoenix_pubsub/Phoenix.Tracker.html), a delta-based conflict-free replicated data type (CRDT) for eventually consistent and conflict-free synced state.

In the future, we'll document the challenges we faced migrating to this new architecture as well as a few challenges we expect to face in the future.

## One More Thing [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#one-more-thing)

We have some great news! [Chris McCord](https://twitter.com/chris_mccord), the creator of the Phoenix framework, has agreed to become a Technical Advisor for Supabase.

Chris works at Fly, and will continue to work there. His role as an advisor is mostly to express our gratitude for the work he's already done (admittedly, we'll probably need his advice for some upcoming challenges). Realtime is made possible by his open source work.

We also want to thank [José Valim](https://twitter.com/josevalim), and everyone in the Erlang/Elixir ecosystem, for your open source contributions that have made our lives here on the Supabase Realtime team a lot easier.

## Announcement video and discussion [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#announcement-video-and-discussion)

Supabase Launch Week 5: Day 4 - Realtime: Multiplayer Edition - YouTube

Supabase

54.4K subscribers

[Supabase Launch Week 5: Day 4 - Realtime: Multiplayer Edition](https://www.youtube.com/watch?v=CGZr5tybW18)

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

[Watch on YouTube](https://www.youtube.com/watch?v=CGZr5tybW18 "Watch on YouTube")

## More Launch Week 5 [\#](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability\#more-launch-week-5)

- [Launch Week Page](https://supabase.com/launch-week)
- [Launch Week 5 Hackathon](https://supabase.com/blog/launch-week-5-hackathon)
- [Day 1 - Supabase CLI v1 and Management API Beta](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta)
- [Youtube video - Supabase CLI v1 and Management API Beta](https://www.youtube.com/watch?v=OpPOaJI_Z28&feature=emb_title)
- [Day 2 - supabase-js v2 Release Candidate](https://supabase.com/blog/supabase-js-v2)
- [Youtube Video - supabase-js v2 Release Candidate](https://www.youtube.com/watch?v=iqZlPtl_b-I)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-multiplayer-general-availability&text=Realtime%3A%20Multiplayer%20Edition)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-multiplayer-general-availability&text=Realtime%3A%20Multiplayer%20Edition)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-multiplayer-general-availability&t=Realtime%3A%20Multiplayer%20Edition)

[Last post\\
\\
**Supabase Vault** \\
\\
19 August 2022](https://supabase.com/blog/supabase-vault)

[Next post\\
\\
**Supabase is SOC2 compliant** \\
\\
17 August 2022](https://supabase.com/blog/supabase-soc2)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [TLDR](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#tldr)
- [Background](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#background)
- [Realtime Channels](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#realtime-channels)
  - [Broadcast](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#broadcast)
  - [Presence](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#presence)
- [Client Library](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#client-library)
  - [Broadcast Example](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#broadcast-example)
  - [Presence Example](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#presence-example)
  - [Receiving Postgres Changes](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#receiving-postgres-changes)
- [Future Plans](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#future-plans)
  - [Extensions](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#extensions)
  - [Peer to Peer](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#peer-to-peer)
  - [Realtime Inspector](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#realtime-inspector)
- [Technical Overview](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#technical-overview)
- [One More Thing](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#one-more-thing)
- [Announcement video and discussion](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#announcement-video-and-discussion)
- [More Launch Week 5](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability#more-launch-week-5)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-multiplayer-general-availability&text=Realtime%3A%20Multiplayer%20Edition)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-multiplayer-general-availability&text=Realtime%3A%20Multiplayer%20Edition)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-realtime-multiplayer-general-availability&t=Realtime%3A%20Multiplayer%20Edition)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)