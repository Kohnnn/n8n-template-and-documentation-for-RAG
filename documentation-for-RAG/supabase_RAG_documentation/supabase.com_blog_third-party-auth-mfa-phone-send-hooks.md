---
url: "https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks"
title: "Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase

14 Aug 2024

•

4 minute read

[![Stojan Dimitrovski avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fhf.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Stojan DimitrovskiEngineering](https://github.com/hf)

![Supabase Auth: Bring-your-own Auth0, Cognito, or Firebase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fthird-party-auth%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we have 3 new announcements for Supabase Auth:

1. Support for third-party Auth providers
2. Phone-based Multi-factor Authentication (SMS and Whatsapp)
3. New Auth Hooks for SMS and email

Let's dive into each new feature.

You don't need Supabase Auth - use this instead! - YouTube

Supabase

54.4K subscribers

[You don't need Supabase Auth - use this instead!](https://www.youtube.com/watch?v=BPD7kxb5N84)

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

[Watch on YouTube](https://www.youtube.com/watch?v=BPD7kxb5N84 "Watch on YouTube")

## Support for third-party Auth providers [\#](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks\#support-for-third-party-auth-providers)

The headline feature today is [third-party Authentication](https://supabase.com/docs/guides/auth/third-party/overview).

![Third-party auth](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fthird-party-auth%2Fthird-party-auth.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase is a modular platform. We've been designing it so that you can choose which products you use with Postgres. You can use our own products (like Supabase Auth) or external products (like Auth0), and _in theory_ the experience should be just-as-delightful.

Until today, using third-party auth products required developers to translate JWTs into a format compatible with Supabase Auth. This is difficult and unmaintainable.

So we fixed it. Today we're adding first-class support for the following third-party authentication products:

1. [Auth0](https://supabase.com/docs/guides/auth/third-party/firebase-auth)
2. [AWS Cognito](https://supabase.com/docs/guides/auth/third-party/aws-cognito) (standalone or via AWS Amplify)
3. [Firebase Auth](https://supabase.com/docs/guides/auth/third-party/firebase-auth)

Firebase Auth is currently under a private-alpha release stage, as we're still improving the security developer experience when using it. [Register your interest](https://forms.supabase.com/third-party-auth-with-firebase) and someone from the team will reach out.

Migrating auth providers can be costly and technically challenging, especially for applications with large user bases. You can use Supabase's native auth offering alongside your third-party authentication provider to achieve a disruption-free migration.

All of the third-party providers are supported in the Supabase CLI, so you can evaluate, test, and develop your integration for free.

The Supabase client supports third-party auth like this:

`
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
accessToken: async () => {
    const accessToken = await auth0.getTokenSilently()
    return accessToken
},
})
`

## Phone-based multi-factor authentication [\#](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks\#phone-based-multi-factor-authentication)

We've extended MFA to [support SMS and WhatsApp](https://supabase.com/docs/guides/auth/auth-mfa).

![Phone MFA](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fthird-party-auth%2Fphone-mfa.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We have a strong conviction that all applications should have access to an open and secure authentication provider. Secure-by-default should not be a luxury: developers should have affordable access to security best-practices.

[Almost two years ago](https://supabase.com/blog/mfa-auth-via-rls) we launched [MFA with TOTP (app authenticator)](https://supabase.com/docs/guides/auth/auth-mfa) free of charge. Since then, we've heard a common complaint from developers: app authenticators can be hard to adopt for non-techies. Phone-based MFA is for those developers who want to provide a more accessible MFA experience for their users.

No security product is infallible! MFA with SMS can come with some hidden security drawbacks - please evaluate your application's risk tolerance for SIM-swapping attacks.

The code looks like this:

``
// Send an SMS or WhatsApp message to the user
const { data: { challengeId } } = await supabase.auth.mfa.challenge({
factorId,
})
// To verify the code received by the user
await supabase.auth.mfa.verify({
factorId,
challengeId,
code: '123456',
})
// The user's `aal` claim in the JWT
// will be upgraded to aal2
``

## Auth Hooks for SMS and Email [\#](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks\#auth-hooks-for-sms-and-email)

We've added a few new [Auth Hooks](https://supabase.com/docs/guides/auth/auth-hooks), which supports HTTP endpoints as a webhook now.

**Email Hooks**

We've heard the (rather loud) feedback that the built-in email templates (based on the Go templating language) can be limiting. There's been a lot of development in email rendering libraries like [Resend's React Email](https://resend.com/blog/react-email-2). To help make this available for developers, we've added a ["Send Email" Auth Hook](https://supabase.com/docs/guides/auth/auth-hooks/send-email-hook), which you can use to customize your emails and how they are sent.

**SMS Hooks**

Supabase Auth has built-in support for popular SMS sending providers like Twilio, Messagebird, Textlocal and Vonage, but we realize this choice can be limiting.

Today we're launching a new ["Send SMS" Auth Hook](https://supabase.com/docs/guides/auth/auth-hooks/send-sms-hook). You no longer need to use the built-in provider - you can implement your own by specifying a HTTP endpoint that receives a POST request when a message needs to be sent.

## Getting started [\#](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks\#getting-started)

Check out the docs for more details on how to get started:

- [Third-party Authentication](https://supabase.com/docs/guides/auth/third-party/overview)
- [Multi-factor Authentication](https://supabase.com/docs/guides/auth/auth-mfa)
- [Auth Hooks](https://supabase.com/docs/guides/auth/auth-hooks)

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fthird-party-auth-mfa-phone-send-hooks&text=Supabase%20Auth%3A%20Bring-your-own%20Auth0%2C%20Cognito%2C%20or%20Firebase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fthird-party-auth-mfa-phone-send-hooks&text=Supabase%20Auth%3A%20Bring-your-own%20Auth0%2C%20Cognito%2C%20or%20Firebase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fthird-party-auth-mfa-phone-send-hooks&t=Supabase%20Auth%3A%20Bring-your-own%20Auth0%2C%20Cognito%2C%20or%20Firebase)

[Last post\\
\\
**Snaplet is now open source** \\
\\
14 August 2024](https://supabase.com/blog/snaplet-is-now-open-source)

[Next post\\
\\
**Supabase Realtime: Broadcast and Presence Authorization** \\
\\
13 August 2024](https://supabase.com/blog/supabase-realtime-broadcast-and-presence-authorization)

[auth](https://supabase.com/blog/tags/auth) [engineering](https://supabase.com/blog/tags/engineering)

On this page

- [Support for third-party Auth providers](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks#support-for-third-party-auth-providers)
- [Phone-based multi-factor authentication](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks#phone-based-multi-factor-authentication)
- [Auth Hooks for SMS and Email](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks#auth-hooks-for-sms-and-email)
- [Getting started](https://supabase.com/blog/third-party-auth-mfa-phone-send-hooks#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fthird-party-auth-mfa-phone-send-hooks&text=Supabase%20Auth%3A%20Bring-your-own%20Auth0%2C%20Cognito%2C%20or%20Firebase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fthird-party-auth-mfa-phone-send-hooks&text=Supabase%20Auth%3A%20Bring-your-own%20Auth0%2C%20Cognito%2C%20or%20Firebase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fthird-party-auth-mfa-phone-send-hooks&t=Supabase%20Auth%3A%20Bring-your-own%20Auth0%2C%20Cognito%2C%20or%20Firebase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)