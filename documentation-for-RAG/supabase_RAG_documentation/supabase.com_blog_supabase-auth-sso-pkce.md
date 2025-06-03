---
url: "https://supabase.com/blog/supabase-auth-sso-pkce"
title: "Supabase Auth: SSO,  Mobile, and Server-side support"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Auth: SSO, Mobile, and Server-side support

13 Apr 2023

•

10 minute read

[![Stojan Dimitrovski avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fhf.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Stojan DimitrovskiEngineering](https://github.com/hf)

[![Joel Lee avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fj0.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Joel LeeEngineering](https://github.com/j0)

[![Kang Ming Tay avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkangmingtay.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Kang Ming TayEngineering](https://github.com/kangmingtay)

![Supabase Auth: SSO,  Mobile, and Server-side support](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-4-supabase-auth-sso-pkce%2Fsupabase-auth-sso-pkce-og.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we're excited to announce a few new features for Supabase Auth:

1. [Easily add Single Sign-On support to your projects using SAML 2.0](https://supabase.com/blog/supabase-auth-sso-pkce#single-sign-on-support-using-saml-20)
2. [Better support for server-side rendering and mobile apps using PKCE](https://supabase.com/blog/supabase-auth-sso-pkce#server-side-and-mobile-auth)
3. [Native Apple login on iOS](https://supabase.com/blog/supabase-auth-sso-pkce#native-apple-login-on-ios)

## Single Sign-On Support using SAML 2.0 [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#single-sign-on-support-using-saml-20)

With Single Sign-On (SSO), your users can login with their company's identity provider (IDP), a critical feature when you're building applications for Enterprises.

Every developer building a B2B application eventually needs the SSO authentication flow to onboard enterprise customers. SSO is a requirement for larger Enterprise customers because it's a standard request in Enterprise Security Policies. Over the past few months, we've been [dogfooding SSO for our own Enterprise customers](https://supabase.com/docs/guides/platform/sso), and today we're releasing it for you to do the same.

Building SSO into your application isn't necessarily hard, but does come with some complexity. A lot of time can be spent understanding the nuances and details of the protocol - from dissecting the jargon to testing the implementation heavily. It took us months to build it for ourselves. With this release, you will have SSO set up and running in less than an hour so that you can focus on shipping the core features of your product. This feature is available for the [Pro Plan and above](https://supabase.com/pricing), starting today. This will also be available on the self-hosted version.

Single Sign-On with SAML 2.0 and Okta - YouTube

Supabase

54.4K subscribers

[Single Sign-On with SAML 2.0 and Okta](https://www.youtube.com/watch?v=hAwJeR6mhB0)

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

[Watch on YouTube](https://www.youtube.com/watch?v=hAwJeR6mhB0 "Watch on YouTube")

### Getting Started with SAML 2.0 [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#getting-started-with-saml-20)

To get started, enable the [“SAML 2.0“](https://supabase.com/dashboard/project/phcnitosaawbzytgyznx/auth/providers) [authentication method in the dashboard](https://supabase.com/dashboard/project/_/auth/providers). We've added new commands to the [Supabase CLI](https://supabase.com/docs/guides/cli) to help with the configuration process:

`
$ supabase sso --help
Manage Single Sign-On (SSO) authentication for projects
Usage:
supabase sso [command]
Available Commands:
add         Add a new SSO identity provider
info        Returns the SAML SSO settings required for the identity provider
list        List all SSO identity providers for a project
remove      Remove an existing SSO identity provider
show        Show information about an SSO identity provider
update      Update information about an SSO identity provider
`

Once you've added a new SSO identity provider to your project, it's as simple as calling the `signInWithSSO()` from the `supabase-js` library:

`
const { data } = await supabase.auth.signInWithSSO({ domain: 'acme.corp' })
if (data.url) window.location.href = data.url
`

### SSO with Row Level Security and multi-tenancy [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#sso-with-row-level-security-and-multi-tenancy)

As usual, we've engineered this feature around the excellent capabilities of PostgreSQL.

For example, you can use Row Level Security (RLS) to build multi-tenant applications, simply by using the provider's unique identifier in the user's JWT:

`
create policy "Only allow read-write access to tenants" on tablename as restrictive to authenticated using (
tenant_id = (select auth.jwt() -> 'app_metadata' ->> 'provider')
);
`

The journey to enterprise readiness isn't an end goal, it is a continuous process that demands constant attention and maintenance. With Supabase Auth, your team can offload this engineering burden to us and prioritize the features that matter.

## Server-Side and Mobile Auth [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#server-side-and-mobile-auth)

Many developers today are using Supabase to build mobile apps, and server-side rendering is becoming popular (again!). This release will add support for these use cases by introducing the _Proof Key for Code Exchange flow (PKCE)_ authentication flow. This improves security for mobile apps and makes building server-first apps simple. Since this is a major update that touches many of the authentication routes, we will be rolling it out gradually over the next few weeks.

### A brief history of Supabase Auth [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#a-brief-history-of-supabase-auth)

When we [launched](https://news.ycombinator.com/item?id=24072051) Supabase Auth, our target was JAMstack developers. In these cases, the protocol used between the user's application and Supabase Auth is known as the [Implicit Grant Flow](https://www.rfc-editor.org/rfc/rfc6749#section-4.2):

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-4-supabase-auth-sso-pkce%2Fsupabase-auth-implicit-grant-flow--dark.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

As developers built more complex apps, they encountered two problems with this authentication flow:

- **Server-Side Email Verification Links**
Data provided in a URL fragment is only accessible in a browser environment, not on the server. This is problematic for email verification links that redirect users to a server-side route.
- **Challenges with Mobile App Authentication**
The implicit grant flow raised security concerns for mobile use cases since [malicious apps could potentially obtain the user session](https://www.rfc-editor.org/rfc/rfc7636#section-1).

Server-side auth unlocks a number of benefits. Developers can:

- Set cookies on the same domain as the application.
- Enable server-side rendering for protected pages.
- Perform downstream actions after user authentication, such as adding the user to a CRM or sending analytics.

### Introducing PKCE [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#introducing-pkce)

To solve these problems, we're introducing support for the _Proof Key for Code Exchange_ flow (PKCE, pronounced “pixy”).

The PKCE flow introduces a _code verifier_ (a randomly generated secret) and a _code challenge_ (the hash of the _code verifier_). The authorization code is returned as a query parameter so it's accessible on the server. During the PKCE flow:

1. The _code challenge_ is sent to Supabase Auth, which returns an _authorization code._
2. The client sends the _authorization code_ together with the _code verifier_ to obtain the user's session.
3. Supabase Auth checks if the _code verifier_ matches the _code challenge_ sent earlier by computing the hash. This renders a malicious attacker's attempt to intercept the authorization code useless, since they need to know the value of the _code verifier_ as well.

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-4-supabase-auth-sso-pkce%2Fsupabase-auth-pkce-flow--dark.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Migrating to PKCE on the client [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#migrating-to-pkce-on-the-client)

Over the next few weeks, you'll be able to use it with the Supabase libraries. We've already added PKCE to the [JavaScript](https://supabase.com/docs/reference/javascript/installing) client library and our [auth-helpers](https://supabase.com/docs/guides/auth/auth-helpers) library. If you're using `supabase-js` , you can switch to PKCE by initializing your client with the following option:

`
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
auth: {
    flowType: 'pkce',
},
})
`

For client-side auth, that's all you need to do to switch over. `supabase-js` will handle the generation and storage for the code verifier, as well as exchanging the authorization code for the user's session.

### Migrating to PKCE on the server [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#migrating-to-pkce-on-the-server)

Server-side authentication is now a lot easier. Let's look at an example using Next.js.

Install the `next` version of auth-helpers (lets use the `nextjs` version for this example)

`
npm install @supabase/auth-helpers-nextjs@next
`

Then prepare an endpoint for the sign in process. The redirect URL is set to `/api/auth/callback`, which will be implemented next.

`
// api/auth/login
import { NextApiRequest, NextApiResponse } from 'next'
import { createServerSupabaseClient } from '@supabase/auth-helpers-nextjs'
export default async function handler(req: NextApiRequest, res: NextApiResponse) {
// Create the Supabase Client
const supabase = createServerSupabaseClient(
    { req, res },
    {
      supabaseUrl: process.env.SUPABASE_URL,
      supabaseKey: process.env.SUPABASE_ANON_KEY,
    }
)
// Start sign in with one-time password
const { error } = await supabase.auth.signInWithOtp({
    email: 'foo@example.com',
    options: {
      emailRedirectTo: 'http://localhost:3000/api/auth/callback',
    },
})
if (error) {
    res.json(JSON.stringify(error))
}
res.redirect('/')
}
`

Now we can set up the callback API endpoint:

`
// api/auth/callback
import { NextApiRequest, NextApiResponse } from 'next'
import { createServerSupabaseClient } from '@supabase/auth-helpers-nextjs'
export default async function handler(req: NextApiRequest, res: NextApiResponse) {
// Create authenticated Supabase Client
const supabase = createServerSupabaseClient(
    { req, res },
    {
      supabaseUrl: SUPABASE_URL,
      supabaseKey: SUPABASE_ANON_KEY,
    }
)
// check for code in url querystring
const code = req.query.code
if (typeof code === 'string') {
    // exchange the auth code for user session
    await supabase.auth.exchangeCodeForSession(code)
}
// redirect the user to a server-side protected area in your app
res.redirect('/')
}
`

### Roll out [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#roll-out)

Since this is a major update that touches many of the authentication routes, we will roll it out gradually over the next few weeks. You will receive a notification in your dashboard when the feature is available for your project. Reach out to us if you want early access to this feature.

**Update**: Server-Side Auth (PKCE) is now available on all projects. Please refer to our [Server Side Auth Guide](https://supabase.com/docs/guides/auth/server-side-rendering) for further details on how to add PKCE to your project.

## Native Apple login on iOS [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#native-apple-login-on-ios)

While PKCE support is great, that is not the only news for you mobile app developers out there.

Building apps for iOS requires [1](https://supabase.com/blog/supabase-auth-sso-pkce#user-content-fn-1) support for native _Sign in with Apple_. We heard the community's requests for native sign-in. We hope you join our excitement to officially announce support for native _Sign in with Apple_.

Your app's iOS Bundle ID can now be configured in the Apple provider section of your project's dashboard.

![native-apple-login-on-iOS.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-4-supabase-auth-sso-pkce%2Fnative-apple-login-on-iOS.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This is the only prerequisite for triggering a native _Sign in with Apple._ With [supabase-flutter](https://pub.dev/packages/supabase_flutter#native-sign-in-with-apple-example), this is as easy as:

`
final AuthResponse response = await supabase.auth.signInWithApple();
`

It's that easy! No need to set up deep links, no need to pass any parameters.

We're just starting with Apple login, and soon add support for Google login.

## Wrapping Up [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#wrapping-up)

Supabase Auth aims to continue developing auth features that are secure by default yet simple to implement. We use Supabase Auth for our hosted platform and continuously dogfood the latest version on it. If you are interested to migrate to Supabase Auth, you can check out this blog post on how [Parqet migrated 125,000 users from Auth0 to Supabase Auth](https://kevcodez.medium.com/migrating-125-000-users-from-auth0-to-supabase-81c0568de307).

## Footnotes [\#](https://supabase.com/blog/supabase-auth-sso-pkce\#footnote-label)

1. [App store review guidelines](https://developer.apple.com/app-store/review/guidelines/#sign-in-with-apple) [↩](https://supabase.com/blog/supabase-auth-sso-pkce#user-content-fnref-1)


### More Launch Week 7

[Designing with AI\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fai-images%2F00-ai-images-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/designing-with-ai-midjourney)

[Supavisor\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday0%2Fsupavisor%2Fsupavisor-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://github.com/supabase/supavisor)

[Open Source Logging\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday1%2Fself-hosted-logs-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-logs-self-hosted)

[Self-hosted Deno Edge Functions\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday2%2Fself-hosted-edge-functions-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions)

[Storage v3: Resumable Uploads with support for 50GB files\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday3%2Fstorage-v3-thumb.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/storage-v3-resumable-uploads)

[Supabase Auth: SSO, Mobile, and Server-side support\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday4%2Fsso-support-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-auth-sso-pkce)

[Community Highlight\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fcommunity%2Fcommunity-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/launch-week-7-community-highlights)

[Studio Updates\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fstudio%2Fstudio-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/supabase-studio-2.0)

[dbdev\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2Fdbdev-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/dbdev)

[Postgres TLE\\
\\
![](https://supabase.com/_next/image?url=%2Fimages%2Flaunchweek%2Fseven%2Fday5%2Fone-more-thing%2FpgTLE-thumb.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)](https://supabase.com/blog/pg-tle)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-sso-pkce&text=Supabase%20Auth%3A%20SSO%2C%20%20Mobile%2C%20and%20Server-side%20support)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-sso-pkce&text=Supabase%20Auth%3A%20SSO%2C%20%20Mobile%2C%20and%20Server-side%20support)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-sso-pkce&t=Supabase%20Auth%3A%20SSO%2C%20%20Mobile%2C%20and%20Server-side%20support)

[Last post\\
\\
**Supabase Studio 2.0: help when you need it most** \\
\\
14 April 2023](https://supabase.com/blog/supabase-studio-2.0)

[Next post\\
\\
**Supabase Storage v3: Resumable Uploads with support for 50GB files** \\
\\
12 April 2023](https://supabase.com/blog/storage-v3-resumable-uploads)

[launch-week](https://supabase.com/blog/tags/launch-week) [auth](https://supabase.com/blog/tags/auth)

On this page

- [Single Sign-On Support using SAML 2.0](https://supabase.com/blog/supabase-auth-sso-pkce#single-sign-on-support-using-saml-20)
  - [Getting Started with SAML 2.0](https://supabase.com/blog/supabase-auth-sso-pkce#getting-started-with-saml-20)
  - [SSO with Row Level Security and multi-tenancy](https://supabase.com/blog/supabase-auth-sso-pkce#sso-with-row-level-security-and-multi-tenancy)
- [Server-Side and Mobile Auth](https://supabase.com/blog/supabase-auth-sso-pkce#server-side-and-mobile-auth)
  - [A brief history of Supabase Auth](https://supabase.com/blog/supabase-auth-sso-pkce#a-brief-history-of-supabase-auth)
  - [Introducing PKCE](https://supabase.com/blog/supabase-auth-sso-pkce#introducing-pkce)
  - [Migrating to PKCE on the client](https://supabase.com/blog/supabase-auth-sso-pkce#migrating-to-pkce-on-the-client)
  - [Migrating to PKCE on the server](https://supabase.com/blog/supabase-auth-sso-pkce#migrating-to-pkce-on-the-server)
  - [Roll out](https://supabase.com/blog/supabase-auth-sso-pkce#roll-out)
- [Native Apple login on iOS](https://supabase.com/blog/supabase-auth-sso-pkce#native-apple-login-on-ios)
- [Wrapping Up](https://supabase.com/blog/supabase-auth-sso-pkce#wrapping-up)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-sso-pkce&text=Supabase%20Auth%3A%20SSO%2C%20%20Mobile%2C%20and%20Server-side%20support)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-sso-pkce&text=Supabase%20Auth%3A%20SSO%2C%20%20Mobile%2C%20and%20Server-side%20support)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-auth-sso-pkce&t=Supabase%20Auth%3A%20SSO%2C%20%20Mobile%2C%20and%20Server-side%20support)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-4-supabase-auth-sso-pkce%2Fsupabase-auth-implicit-grant-flow--dark.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-4-supabase-auth-sso-pkce%2Fsupabase-auth-pkce-flow--dark.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)