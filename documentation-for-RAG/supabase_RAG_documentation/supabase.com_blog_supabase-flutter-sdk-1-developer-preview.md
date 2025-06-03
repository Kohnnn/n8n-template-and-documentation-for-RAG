---
url: "https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview"
title: "Supabase Flutter SDK 1.0 Developer Preview"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Flutter SDK 1.0 Developer Preview

02 Aug 2022

•

6 minute read

[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Tyler ShukertDevRel](https://twitter.com/dshukertjr)

![Supabase Flutter SDK 1.0 Developer Preview](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-1%2Fsupabase-flutter-1.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today, we are releasing of Developer Preview version of v1.0 of [Supabase Flutter SDK](https://pub.dev/packages/supabase_flutter/versions/1.0.0-dev.1). Flutter has quickly become one of the most popular frameworks for developers to build cross-platform mobile apps. We can attest to that growth, our Flutter SDK is one of the most popular libraries and each day we see more Flutter devs choosing Supabase.

For this release, our main focus is developer experiences. We would love for you to try the SDK and provide your feedback so that we can continue to improve!

Before we dive into the actual updates, I would like to thank all the community contributors who have helped the library to be where it is today.

## Better developer experience [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#better-developer-experience)

Until now, there were some disputable implementations in the Flutter SDK. We've made several improvements:

### Automatically handling auth state persistence [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#automatically-handling-auth-state-persistence)

Previously, `supabase-flutter` required a class that extends `SupabaseAuthState` or `SupabaseAuthRequiredState` to persist auth state. With `supabase-flutter` 1.0, you no longer need to include these classes.

All you need to persist the auth state is initialize Supabase and everything else will be automatically taken care of. `SupabaseAuthState` and `SupabaseAuthRequiredState` have been removed from the code base.

`
// Before
await Supabase.initialize(
url: 'SUPABASE_URL',
anonKey: 'SUPABASE_ANON_KEY',
);
...
class AuthState<T extends StatefulWidget> extends SupabaseAuthState<T> {
...
}
// After
await Supabase.initialize(
url: 'SUPABASE_URL',
anonKey: 'SUPABASE_ANON_KEY',
);
`

### Automatically handling deep links [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#automatically-handling-deep-links)

Deep link handling had similar issues previously, requiring you to implement `SupabaseAuthState` or `SupabaseAuthRequiredState` classes.

With the 1.0 update, you no longer need to use these classes, and deep links will be automatically handled. You can listen to `onAuthStateChange` to handle when a deep link is received to redirect users to a new screen.

`
// Before
void onReceivedAuthDeeplink(Uri uri) {
Supabase.instance.log('onReceivedAuthDeeplink uri: $uri');
}
// After
await Supabase.instance.initialize(
url: 'SUPABASE_URL',
anonKey: 'SUPABASE_ANON_KEY',
);
`

### Throwing errors instead of returning them [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#throwing-errors-instead-of-returning-them)

When `supabase-dart` and `supabase-flutter` were created, we wanted to mirror the JavaScript library as much as possible. We soon realized that some syntax does not fit well when written in Dart. Throwing vs returning error is a good example of that. Since Dart does not have object destruction, the code becomes a bit tedious when errors are returned.

With `supabase-flutter` 1.0, we are throwing errors instead of returning them. This is consistent across all features from `auth`, `postgrest`, and `storage`.

`
// Before
final response = await Supabase.instance.from('messages').select().execute();
final data = response.data;
final error = response.error;
// After
try {
final data = await Supabase.instance.from('messages').select();
} catch(error) {
// Handle error here
}
`

### No more `.execute()` to get the data [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#no-more-execute-to-get-the-data)

We want this SDK to be as close as possible to the JavaScript SDK to provide consistent developer experience no matter what programming language you are using. Prior to the 1.0 update, whenever you called the `postgrest` endpoints, you had to call `.execute()` at the end of each query.

`.execute()` is now deprecated. You no longer needed it to query data from your Supabase database. This update, along with many many other improvements across the whole library, has been done by [Bruno D'Luka](https://github.com/bdlukaa), and I would love to give him a special shout out here!

`
// Before
final response = await Supabase.instance.from('messages').select().execute();
final data = response.data;
// After
final data = await Supabase.instance.from('messages').select();
`

## Desktop support for deeplinks [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#desktop-support-for-deeplinks)

Ever since `supabase-flutter` was born, it supported only iOS, Android and Web for deep linking. This was a limitation of the deep link library that we were using.

With the 1.0 launch, we are moving to use [app\_links](https://pub.dev/packages/app_links), which will enable us to support MacOS and Windows applications as well! Linux support is being worked on - follow the repo to keep updated.

![Supabase Flutter desktop support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-1%2Fsupported-platforms-table.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Multiplayer support [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#multiplayer-support)

[Multiplayer](https://supabase.com/blog/supabase-realtime-with-multiplayer-features) is the next generation Supabase Realtime engine that was announced at the previous launch week.

We want our Flutter developers to experience this new multiplayer feature as well, so are working hard at bringing it to our Flutter SDK. It is not yet included in the developer preview of Supabase Flutter 1.0, but will be part of it when stable launch has been released.

## Supabase Auth UI for Flutter [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#supabase-auth-ui-for-flutter)

![Supabase Auth UI for Flutter](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-1%2Fsupabase-flutter-auth-ui.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Last but not least, we are bringing you another library, the Supabase Auth UI for Supabase! When released, this library will enable you to implement a basic authentication screen without building it yourself. You can just load the library and display a nice looking Auth UI. The library takes your theme settings automatically to match the look and feel of your application.

You can get started with it on [pub.dev](https://pub.dev/packages/supabase_auth_ui).

I would like to thank [Fatuma](https://twitter.com/XquisiteDreamer) for single-handedly working on bringing us an easier authentication experience.

`
// Email and password signin form
SupaEmailAuth(
authAction: AuthAction.signIn,
redirectUrl: '/home',
),
// Magic Link signin form
SupaMagicAuth(),
// Social Login Buttons
SupaSocialsAuth(
socialProviders: [\
SocialProviders.apple,\
SocialProviders.google,\
],
colored: true,
),
`

## Final thoughts [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#final-thoughts)

These updates are just the tip of the iceberg for 1.0. There are been many bug fixes and features constantly being added to the Supabase Flutter SDK. This could not have been possible without the help from the open source community. Here, I would also like to give a shout out to two other developers who have been a major part of the journey of this SDK: [Vinzent](https://twitter.com/Vinzent03_) and [Daniel Mossaband](https://github.com/DanMossa). They have been a huge part of the Supabase Flutter SDK - not just for the 1.0 release, but throughout the lifetime of the library.
For those of you who want to try out the new SDK, you can get the developer preview version from [supabase-flutter](https://pub.dev/packages/supabase_flutter/versions/1.0.0-dev.1) pub.dev page or can simply copy and paste the following into your pubspec.yaml file.

`
supabase_flutter: ^1.0.0-dev.1
`

If you have any feedbacks, please let us know in the issues of the [supabase-flutter](https://github.com/supabase-community/supabase-flutter/issues) repository.

## Flutter Resources [\#](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview\#flutter-resources)

- [supabase-flutter 1.0 developer preview](https://pub.dev/packages/supabase_flutter)
- [Flutter Tutorial: building a Flutter chat app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)
- [Flutter Tutorial - Part 2: Authentication and Authorization with RLS](https://supabase.com/blog/flutter-authentication-and-authorization-with-rls)
- [How to build a real-time multiplayer game with Flutter Flame](https://supabase.com/blog/flutter-real-time-multiplayer-game)
- [Build a Flutter app with Very Good CLI and Supabase](https://verygood.ventures/blog/flutter-app-very-good-cli-supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&text=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&text=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&t=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)

[Last post\\
\\
**Supabase Beta July 2022** \\
\\
3 August 2022](https://supabase.com/blog/supabase-beta-update-july-2022)

[Next post\\
\\
**Implementing "seen by" functionality with Postgres** \\
\\
18 July 2022](https://supabase.com/blog/seen-by-in-postgresql)

[flutter](https://supabase.com/blog/tags/flutter) [mobile](https://supabase.com/blog/tags/mobile)

On this page

- [Better developer experience](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#better-developer-experience)
  - [Automatically handling auth state persistence](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#automatically-handling-auth-state-persistence)
  - [Automatically handling deep links](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#automatically-handling-deep-links)
  - [Throwing errors instead of returning them](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#throwing-errors-instead-of-returning-them)
  - [No more `.execute()` to get the data](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#no-more-execute-to-get-the-data)
- [Desktop support for deeplinks](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#desktop-support-for-deeplinks)
- [Multiplayer support](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#multiplayer-support)
- [Supabase Auth UI for Flutter](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#supabase-auth-ui-for-flutter)
- [Final thoughts](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#final-thoughts)
- [Flutter Resources](https://supabase.com/blog/supabase-flutter-sdk-1-developer-preview#flutter-resources)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&text=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&text=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-flutter-sdk-1-developer-preview&t=Supabase%20Flutter%20SDK%201.0%20Developer%20Preview)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)