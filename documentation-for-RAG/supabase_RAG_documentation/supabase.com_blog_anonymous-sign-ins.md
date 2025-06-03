---
url: "https://supabase.com/blog/anonymous-sign-ins"
title: "Supabase Auth now supports Anonymous Sign-ins"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Auth now supports Anonymous Sign-ins

17 Apr 2024

•

7 minute read

[![Kang Ming Tay avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkangmingtay.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Kang Ming TayEngineering](https://github.com/kangmingtay)

![Supabase Auth now supports Anonymous Sign-ins](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fanonymous-sign-ins%2Fthumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Supabase Auth now supports [anonymous sign-ins](https://supabase.com/docs/guides/auth/auth-anonymous), one of our [most-requested features](https://github.com/supabase/auth/issues/68) by the community.

Anonymous sign-ins can be used to create **temporary users** who haven’t signed up for your application yet. This lowers the friction for new users to try out your product since they don’t have to provide any signup credentials.

Improve UX with Anonymous Sign-Ins - YouTube

Supabase

54.4K subscribers

[Improve UX with Anonymous Sign-Ins](https://www.youtube.com/watch?v=WNN7Pp5Ftk4)

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

[Watch on YouTube](https://www.youtube.com/watch?v=WNN7Pp5Ftk4 "Watch on YouTube")

## Enabling Anonymous sign-ins [\#](https://supabase.com/blog/anonymous-sign-ins\#enabling-anonymous-sign-ins)

You can [enable anonymous sign-ins](https://supabase.com/dashboard/project/_/settings/auth) for your project today from the dashboard:

![Allow anonymous sign ins](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fanonymous-sign-ins%2Fallow-anon-sign-ins.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

For local development, upgrade your Supabase CLI and add the config to the `config.toml` file:

`
[auth]
enable_anonymous_sign_ins = true
`

You can create an anonymous user through the [Javascript](https://supabase.com/docs/reference/javascript/auth-signinanonymously), [Flutter](https://supabase.com/docs/reference/dart/auth-signinanonymously) or [Swift](https://supabase.com/docs/reference/swift/auth-signinanonymously) SDKs today. Here’s how you can create an anonymous user using `supabase-js` .

`
const { data, error } = await supabase
.auth
.signInAnonymously()
`

## Terminology [\#](https://supabase.com/blog/anonymous-sign-ins\#terminology)

Profiles created with anonymous sign-ins are also `authenticated`!

Once you call `.signInAnonymously()` you have moved the user into an authentication flow, and we treat them like a signed in user:

![Integrated pgvector experience](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fanonymous-sign-ins%2Fanonymous-user-lifecycle.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Restricting access for anonymous users [\#](https://supabase.com/blog/anonymous-sign-ins\#restricting-access-for-anonymous-users)

Like a permanent user, anonymous users are persisted in the `auth.users` table:

| id | role | email | is\_anonymous |
| --- | --- | --- | --- |
| e053e470-afa1-4625-8963-37adb862fd11 | authenticated | NULL | true |
| 5563108e-ac81-4063-9288-4f3db068efa1 | authenticated | [luke@starwars.com](mailto:luke@starwars.com) | false |

An anonymous user can be identified by the `is_anonymous` claim returned in the user’s JWT, which is accessible from your Row Level Security policies (RLS). This is helpful if you want to limit access to certain features in your application.

For example, let’s say that we have an online forum where users can create and read posts.

Given this table to store the posts:

`
create table public.posts (
id serial primary key,
name text not null,
description text
);
`

If we only want to allow permanent users to create posts, we can check if the user is anonymous by inspecting the JWT `select auth.jwt() ->> 'is_anonymous'`.

Using this function in an RLS policy:

`
create policy "Only permanent users can create posts"
on public.posts
for insert
to authenticated -- Note: user is still authenticated
with check (
(select auth.jwt() ->> 'is_anonymous')::boolean is false
);
`

RLS gives us full flexibility to create a variety of rules.

For example, to allow read access for permanent users for all posts and limit anonymous users to posts created today:

`
create policy "Limit access to anonymous users"
on public.posts
for select
to authenticated -- Note: user is still authenticated
using (
case
    when (select (auth.jwt() ->> 'is_anonymous'))::boolean is true
    then (created_at >= current_date)
else
    true
end
);
`

## Convert an anonymous user to a permanent user [\#](https://supabase.com/blog/anonymous-sign-ins\#convert-an-anonymous-user-to-a-permanent-user)

At some point, an anonymous user may decide they want to create a post. This is where we prompt them to sign up for an account which converts them to a permanent user.

##### An anonymous user is considered a permanent user when they have an identity associated to them.

After they have been converted, the user id remains the same, which means that any data associated with the user’s id would be carried over.

Supabase Auth provides 2 ways to achieve this:

1. Link an email or phone identity
2. Link an OAuth identity

### Link an email or phone identity [\#](https://supabase.com/blog/anonymous-sign-ins\#link-an-email-or-phone-identity)

To link an email or phone identity:

`
const { data, error } = await supabase
.auth
.updateUser({ email })
`

### Link an OAuth identity [\#](https://supabase.com/blog/anonymous-sign-ins\#link-an-oauth-identity)

To link an OAuth identity to an anonymous user, you need to [enable manual linking](https://supabase.com/dashboard/project/_/settings/auth) for your project. Learn about how [identity linking](https://supabase.com/docs/guides/auth/auth-identity-linking) works with Supabase Auth.

![Allow anonymous sign ins](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fanonymous-sign-ins%2Fallow-manual-linking.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Once enabled, you can call the `linkIdentity()` method:

`
const { data, error } = await supabase
.auth
.linkIdentity({ provider: 'google' })
`

## Impersonating an anonymous user [\#](https://supabase.com/blog/anonymous-sign-ins\#impersonating-an-anonymous-user)

When creating RLS policies to differentiate access for an anonymous user, you can leverage the [user impersonation feature](https://supabase.com/blog/studio-introducing-assistant) in the SQL editor to test out your policies:

![Allow anonymous sign ins](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fanonymous-sign-ins%2Fimpersonation-role-settings.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)Database role settings in the SQL editor. You can impersonate an anonymous user by selecting the user from the dropdown.

The [user management screen](https://supabase.com/dashboard/project/_/auth/users) provides an option to filter by anonymous users, which can help to know how many anonymous users have been created.

![Allow anonymous sign ins](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fanonymous-sign-ins%2Fanon-user-filtering.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)Filtering by anonymous users on the Users page.

## What’s next [\#](https://supabase.com/blog/anonymous-sign-ins\#whats-next)

Managing anonymous users can be tricky, especially when you have a lot of visitors to your site. We’re working on an “automatic clean-up” option to delete anonymous users that have been inactive for more than 30 days. In the meantime, since anonymous users are stored in the auth schema in your database, you can clean up orphaned anonymous users by running the following query:

`
-- deletes anonymous users created more than 30 days ago
delete from auth.users
where is_anonymous is true and created_at < now() - interval '30 days';
`

We are also working on a [linter](https://github.com/supabase/splinter/pull/28) to check your RLS policies and highlight those that allow anonymous users access - stay tuned for updates later this month!

## Getting started [\#](https://supabase.com/blog/anonymous-sign-ins\#getting-started)

- Docs: [Anonymous sign-ins](https://supabase.com/docs/guides/auth/auth-anonymous)
- API method references: [Javascript](https://supabase.com/docs/reference/javascript/auth-signinanonymously), [Flutter](https://supabase.com/docs/reference/dart/auth-signinanonymously), [Swift](https://supabase.com/docs/reference/swift/auth-signinanonymously)

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fanonymous-sign-ins&text=Supabase%20Auth%20now%20supports%20Anonymous%20Sign-ins)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fanonymous-sign-ins&text=Supabase%20Auth%20now%20supports%20Anonymous%20Sign-ins)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fanonymous-sign-ins&t=Supabase%20Auth%20now%20supports%20Anonymous%20Sign-ins)

[Last post\\
\\
**Supabase Security Advisor & Performance Advisor** \\
\\
18 April 2024](https://supabase.com/blog/security-performance-advisor)

[Next post\\
\\
**AI Inference now available in Supabase Edge Functions** \\
\\
16 April 2024](https://supabase.com/blog/ai-inference-now-available-in-supabase-edge-functions)

[launch-week](https://supabase.com/blog/tags/launch-week) [database](https://supabase.com/blog/tags/database)

On this page

- [Enabling Anonymous sign-ins](https://supabase.com/blog/anonymous-sign-ins#enabling-anonymous-sign-ins)
- [Terminology](https://supabase.com/blog/anonymous-sign-ins#terminology)
- [Restricting access for anonymous users](https://supabase.com/blog/anonymous-sign-ins#restricting-access-for-anonymous-users)
- [Convert an anonymous user to a permanent user](https://supabase.com/blog/anonymous-sign-ins#convert-an-anonymous-user-to-a-permanent-user)
  - [Link an email or phone identity](https://supabase.com/blog/anonymous-sign-ins#link-an-email-or-phone-identity)
  - [Link an OAuth identity](https://supabase.com/blog/anonymous-sign-ins#link-an-oauth-identity)
- [Impersonating an anonymous user](https://supabase.com/blog/anonymous-sign-ins#impersonating-an-anonymous-user)
- [What’s next](https://supabase.com/blog/anonymous-sign-ins#whats-next)
- [Getting started](https://supabase.com/blog/anonymous-sign-ins#getting-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fanonymous-sign-ins&text=Supabase%20Auth%20now%20supports%20Anonymous%20Sign-ins)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fanonymous-sign-ins&text=Supabase%20Auth%20now%20supports%20Anonymous%20Sign-ins)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fanonymous-sign-ins&t=Supabase%20Auth%20now%20supports%20Anonymous%20Sign-ins)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![Integrated pgvector experience](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fga-week%2Fanonymous-sign-ins%2Fanonymous-user-lifecycle.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)