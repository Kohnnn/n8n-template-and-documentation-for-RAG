---
url: "https://supabase.com/blog/supabase-swift"
title: "Supabase Swift"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Swift

15 Apr 2024

•

2 minute read

[![Guilherme Souza avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fgrdsdev.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Guilherme SouzaEngineering](https://github.com/grdsdev)

![Supabase Swift](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-11%2Fswift%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We are excited to announce that Supabase Swift libraries are now officially supported by Supabase.

This makes it simple to interact with Supabase from applications on Apple's platforms, including iOS, macOS, watchOS, tvOS, and visionOS:

`
let url = URL(string: "...")!
let anonKey = "public-anon-key"
let client = SupabaseClient(supabaseURL: url, supabaseKey: anonKey)
struct Country: Decodable {
let id: Int
let name: String
}
let countries: [Country] = try await supabase.from("countries")
.select()
.execute()
.value
`

## New features [\#](https://supabase.com/blog/supabase-swift\#new-features)

This release includes the following new features:

- WhatsApp OTP: [https://github.com/supabase/supabase-swift/pull/287](https://github.com/supabase/supabase-swift/pull/287)
- Captcha support: [https://github.com/supabase/supabase-swift/pull/276](https://github.com/supabase/supabase-swift/pull/276)
- SSO: [https://github.com/supabase/supabase-swift/pull/289](https://github.com/supabase/supabase-swift/pull/289)
- Simplified Storage uploads: [https://github.com/supabase/supabase-swift/pull/290](https://github.com/supabase/supabase-swift/pull/290)
- Anonymous sign-ins: [https://github.com/supabase-community/supabase-swift/releases/tag/v2.6.0](https://github.com/supabase-community/supabase-swift/releases/tag/v2.6.0)
- Simplified OAuth: [https://github.com/supabase/supabase-swift/pull/299](https://github.com/supabase/supabase-swift/pull/299)

## What does official support mean? [\#](https://supabase.com/blog/supabase-swift\#what-does-official-support-mean)

Swift developers can now integrate Supabase services seamlessly with official support. This means:

- **Direct assistance from the Supabase team**: Get timely and effective help directly from the developers who build and maintain your tools.
- **Continuously updated libraries**: Stay up-to-date with the latest features and optimizations that are fully tested and endorsed by Supabase.
- **Community and collaboration**: Engage with a broader community of Swift developers using Supabase, share knowledge, and contribute to the library's growth.

## Contributors [\#](https://supabase.com/blog/supabase-swift\#contributors)

We want to give a shout out to the community members who have contributed to the development of the Supabase Swift libraries:

[grdsdev](https://github.com/grdsdev), [satishbabariya](https://github.com/satishbabariya), [AngCosmin](https://github.com/AngCosmin), [thecoolwinter](https://github.com/thecoolwinter), [maail](https://github.com/maail), [gentilijuanmanuel](https://github.com/gentilijuanmanuel), [mbarnach](https://github.com/mbarnach), [mdloucks](https://github.com/mdloucks), [mpross512](https://github.com/mpross512), [SaurabhJamadagni](https://github.com/SaurabhJamadagni), [theolampert](https://github.com/theolampert), [tyirenkyi](https://github.com/tyirenkyi), [tmn](https://github.com/tmn), [multimokia](https://github.com/multimokia), [zunda-pixel](https://github.com/zunda-pixel), [iamlouislab](https://github.com/iamlouislab), [jxhug](https://github.com/jxhug), [james-william-r](https://github.com/james-william-r), [jknlsn](https://github.com/jknlsn), [jknlsn](https://github.com/glowcap), [Colgates](https://github.com/Colgates), [ChristophePRAT](https://github.com/ChristophePRAT), [brianmichel](https://github.com/brianmichel), [junjielu](https://github.com/junjielu).

## Getting started [\#](https://supabase.com/blog/supabase-swift\#getting-started)

We've released a [new guide](https://supabase.com/docs/guides/getting-started/tutorials/with-swift) to help you get started with the key features available in Supabase Swift.

Or you can jump into our deep dive to use iOS Swift with Postgres & Supabase Auth:

iOS Swift Database & Auth - YouTube

Supabase

54.4K subscribers

[iOS Swift Database & Auth](https://www.youtube.com/watch?v=enVDRqzmudo)

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

[Watch on YouTube](https://www.youtube.com/watch?v=enVDRqzmudo "Watch on YouTube")

[![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-black.svg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)![GA logo](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fga%2Fga-white.svg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)Week](https://supabase.com/ga-week)

15-19 April

[Day 1 -Supabase is officially launching into General Availability](https://supabase.com/ga)

[Day 2 -Supabase Functions now supports AI models](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions)

[Day 3 -Supabase Auth now supports Anonymous sign-ins](https://supabase.com/blog/anonymous-sign-ins)

[Day 4 -Supabase Storage: now supports the S3 protocol](https://supabase.com/blog/s3-compatible-storage)

[Day 5 -Supabase Security Advisor & Performance Advisor](https://supabase.com/blog/security-performance-advisor)

Build Stage

[01 -PostgreSQL Index Advisor](https://github.com/supabase/index_advisor)

[02 -Branching now Publicly Available](https://supabase.com/blog/branching-publicly-available)

[03 -Oriole joins Supabase](https://supabase.com/blog/supabase-acquires-oriole)

[04 -Supabase on AWS Marketplace](https://supabase.com/blog/supabase-aws-marketplace)

[05 -Supabase Bootstrap](https://supabase.com/blog/supabase-bootstrap)

[06 -Supabase Swift](https://supabase.com/blog/supabase-swift)

[07 -Top 10 Launches from Supabase GA Week](https://supabase.com/blog/ga-week-summary)

[Open Source Hackathon 2024](https://supabase.com/blog/supabase-oss-hackathon)

[Community Meetups](https://supabase.com/ga-week#meetups)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&text=Supabase%20Swift)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&text=Supabase%20Swift)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&t=Supabase%20Swift)

[Last post\\
\\
**Supabase Bootstrap: the fastest way to launch a new project** \\
\\
15 April 2024](https://supabase.com/blog/supabase-bootstrap)

[Next post\\
\\
**Supabase Open Source Hackathon 2024** \\
\\
12 April 2024](https://supabase.com/blog/supabase-oss-hackathon)

[launch-week](https://supabase.com/blog/tags/launch-week) [database](https://supabase.com/blog/tags/database)

On this page

- [New features](https://supabase.com/blog/supabase-swift#new-features)
- [What does official support mean?](https://supabase.com/blog/supabase-swift#what-does-official-support-mean)
- [Contributors](https://supabase.com/blog/supabase-swift#contributors)
- [Getting started](https://supabase.com/blog/supabase-swift#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&text=Supabase%20Swift)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&text=Supabase%20Swift)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-swift&t=Supabase%20Swift)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)