---
url: "https://supabase.com/blog/supabase-flutter-sdk-v1-released"
title: "supabase-flutter v1 Released"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# supabase-flutter v1 Released

21 Oct 2022

•

3 minute read

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![supabase-flutter v1 Released](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-v1-release%2Fflutter_v1_official_release.jpeg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

A few months ago, we announced a [developer preview version of supabase-flutter SDK](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview). Since then, we have heard a lot of amazing feedback from the community, and have been improving it. Today, we are happy to announce the stable v1 of [supabase-flutter](https://pub.dev/packages/supabase_flutter). You can also find the updated [quick start guide](https://supabase.com/docs/guides/with-flutter), [documentation](https://supabase.com/docs/reference/dart) and a [migration guide from v0](https://supabase.com/docs/reference/dart/v0/upgrade-guide).

## What is new in v1? [\#](https://supabase.com/blog/supabase-flutter-sdk-v1-released\#what-is-new-in-v1)

supabase-flutter v1 focuses on improved developer experience. The new version requires far less boiler plate code as well as it provides more intuitive APIs. Here are some highlights of the update.

### No more `.execute()` [\#](https://supabase.com/blog/supabase-flutter-sdk-v1-released\#no-more-execute)

Previously, for `.select()`, `.insert()`, `.update()`, `.delete()` and `.stream()` required `execute()` to be called at the end. On top of that, errors are thrown, not returned, so you can be sure that you have the query results in the returned value.

`
// Before
final response = await supabase.from('messages').select().execute();
final data = response.data;
// After
final data = await supabase.from('messages').select();
`

### More predictable auth methods [\#](https://supabase.com/blog/supabase-flutter-sdk-v1-released\#more-predictable-auth-methods)

Names of the auth methods are more descriptive about what they do. Here are some examples of the new methods:

`
await supabase.auth.signInWithPassword(email: email, password: password);
await supabase.auth.signInWithOAuth(Provider.github)
`

Also, `onAuthStateChange` returns stream, which feels more natural for anyone coding in Dart.

`
supabase.auth.onAuthStateChange.listen((data) {
final AuthChangeEvent event = data.event;
final Session? session = data.session;
});
`

### Realtime Multiplayer edition support [\#](https://supabase.com/blog/supabase-flutter-sdk-v1-released\#realtime-multiplayer-edition-support)

During the last launch week, we announced the [general availability of Realtime Multiplayer](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability). supabase-flutter now has first class support for the two newly introduced realtime methods, broadcast and presence. Broadcast can be used to share realtime data to all connected clients with low latency. Presence is a way to let other connected clients know the status of the client. You can visit [multiplayer.dev](http://multiplayer.dev/) to see a quick demo of the feature.

``
final channel = Supabase.instance.client.channel('my_channel');
// listen to `location` broadcast events
channel.on(
    RealtimeListenTypes.broadcast,
    ChannelFilter(
      event: 'location',
    ), (payload, [ref]) {
	// Do something exciting with the broadcast event
});
// send `location` broadcast events
channel.send(
type: RealtimeListenTypes.broadcast,
event: 'location',
payload: {'lat': 1.3521, 'lng': 103.8198},
);
// listen to presence states
channel.on(RealtimeListenTypes.presence, ChannelFilter(event: 'sync'),
    (payload, [ref]) {
	// Do something exciting with the presence state
});
// subscribe to the above changes
channel.subscribe((status) async {
if (status == 'SUBSCRIBED') {
    // if subscribed successfully, send presence event
    final status = await channel.track({'user_id': myUserId});
}
});
``

These are just tip of the iceberg of all the updates that we shipped in v1. Check out the [documentation](https://supabase.com/docs/reference/dart/) to see the full list.

## Acknowledgements [\#](https://supabase.com/blog/supabase-flutter-sdk-v1-released\#acknowledgements)

It required massive support from the community to bring the supabase-flutter to where it is today. I would like to thank everyone who has contributed to the library, and a special thanks to [Bruno](https://github.com/bdlukaa) and [Vinzent](https://github.com/Vinzent03), who have been key for this release. We really could not have done it without you!

## Resources [\#](https://supabase.com/blog/supabase-flutter-sdk-v1-released\#resources)

- [Install supabase-flutter v1.0](https://pub.dev/packages/supabase_flutter)
- [supabase-flutter documentation](https://supabase.com/docs/reference/dart/)
- [v0 to v1 migration guide](https://supabase.com/docs/reference/dart/v0/upgrade-guide)
- [Flutter Tutorial: building a Flutter chat app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)
- [Flutter Tutorial - Part 2: Authentication and Authorization with RLS](https://supabase.com/blog/flutter-authentication-and-authorization-with-rls)
- [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)
- [Build a Flutter app with Very Good CLI and Supabase](https://verygood.ventures/blog/flutter-app-very-good-cli-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-v1-released&text=supabase-flutter%20v1%20Released)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-v1-released&text=supabase-flutter%20v1%20Released)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-v1-released&t=supabase-flutter%20v1%20Released)

[Last post\\
\\
**What is PostgreSQL commitfest and how to contribute** \\
\\
27 October 2022](https://supabase.com/blog/postgresql-commitfest)

[Next post\\
\\
**supabase-js v2 Released** \\
\\
20 October 2022](https://supabase.com/blog/supabase-js-v2-released)

[flutter](https://supabase.com/blog/tags/flutter) [mobile](https://supabase.com/blog/tags/mobile)

On this page

- [What is new in v1?](https://supabase.com/blog/supabase-flutter-sdk-v1-released#what-is-new-in-v1)
  - [No more `.execute()`](https://supabase.com/blog/supabase-flutter-sdk-v1-released#no-more-execute)
  - [More predictable auth methods](https://supabase.com/blog/supabase-flutter-sdk-v1-released#more-predictable-auth-methods)
  - [Realtime Multiplayer edition support](https://supabase.com/blog/supabase-flutter-sdk-v1-released#realtime-multiplayer-edition-support)
- [Acknowledgements](https://supabase.com/blog/supabase-flutter-sdk-v1-released#acknowledgements)
- [Resources](https://supabase.com/blog/supabase-flutter-sdk-v1-released#resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-v1-released&text=supabase-flutter%20v1%20Released)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-v1-released&text=supabase-flutter%20v1%20Released)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-v1-released&t=supabase-flutter%20v1%20Released)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)