---
url: "https://supabase.com/blog/platform-access-control"
title: "Introducing New Platform Access Control"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Introducing New Platform Access Control

16 Aug 2024

•

2 minute read

[![Hieu Pham avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fphamhieu.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Hieu PhamEngineering](https://github.com/phamhieu)

[![Joshen Lim avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fjoshenlim.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Joshen LimEngineering](https://github.com/joshenlim)

![Introducing New Platform Access Control](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Fthumb_platform-access-control.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

At Supabase, we're constantly striving to provide the tools developers need to build secure, reliable applications. Our latest update focuses on an area that's critical to both security and reliability: Platform Access Control.

We're excited to announce the rollout of our new granular access control features which allows giving users access to specific projects instead of the entire organization.

![Configuring project roles for a user](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw12%2Fday-5%2Faccess-control.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Why Platform Access Control matters [\#](https://supabase.com/blog/platform-access-control\#why-platform-access-control-matters)

Managing who can access what within your project isn't just a convenience — it's essential for maintaining security and ensuring that your software development lifecycle (SDLC) is followed and availability guarantees are met. While Supabase already provides a robust data security framework through Row-Level Security (RLS), we recognized a gap when it came to managing platform-level access. Our new Platform Access Control feature fills that gap by offering Role-Based Access Control (RBAC) to the Supabase platform and management APIs.

### Granular control at your fingertips [\#](https://supabase.com/blog/platform-access-control\#granular-control-at-your-fingertips)

With Platform Access Control, Supabase now offers a way to manage permissions at the both the organization and project levels.

A user can either have permissions assigned for the whole organization or for specific projects. The roles remain the same as before:

- **Owner:** Full control over everything
- **Administrator:** Similar to the Owner role with some restrictions on update organization settings, transferring projects and modifying owners.
- **Developer:** Cannot modify any settings but has full access to modifying the content like updating the database, uploading storage objects, etc.
- **Read-Only:** Ideal for stakeholders or team members who need visibility into the project without the ability to make changes.

For a more exhaustive list of actions allowed for each role, check out the [access control docs](https://supabase.com/docs/guides/platform/access-control#organization-scoped-roles-vs-project-scoped-roles).

### Unlocking the full potential of your team [\#](https://supabase.com/blog/platform-access-control\#unlocking-the-full-potential-of-your-team)

With these new features, Supabase is making it easier than ever to ensure that every team member has the right level of access. By assigning specific roles, you can reduce the risk of accidental changes, streamline workflows, and maintain a high level of security across your projects. If you're part of a growing team, consider upgrading to an Enterprise Plan to take full advantage of these powerful new tools.

### Get started [\#](https://supabase.com/blog/platform-access-control\#get-started)

To start using the new Platform Access Control features, check out our updated documentation [here](https://supabase.com/docs/guides/platform/access-control).

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fplatform-access-control&text=Introducing%20New%20Platform%20Access%20Control)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fplatform-access-control&text=Introducing%20New%20Platform%20Access%20Control)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fplatform-access-control&t=Introducing%20New%20Platform%20Access%20Control)

[Last post\\
\\
**Top 10 Launches of Launch Week 12** \\
\\
16 August 2024](https://supabase.com/blog/launch-week-12-top-10)

[Next post\\
\\
**Postgres Foreign Data Wrappers with Wasm** \\
\\
16 August 2024](https://supabase.com/blog/postgres-foreign-data-wrappers-with-wasm)

[launch-week](https://supabase.com/blog/tags/launch-week) [tech](https://supabase.com/blog/tags/tech)

On this page

- [Why Platform Access Control matters](https://supabase.com/blog/platform-access-control#why-platform-access-control-matters)
- [Granular control at your fingertips](https://supabase.com/blog/platform-access-control#granular-control-at-your-fingertips)
- [Unlocking the full potential of your team](https://supabase.com/blog/platform-access-control#unlocking-the-full-potential-of-your-team)
- [Get started](https://supabase.com/blog/platform-access-control#get-started)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fplatform-access-control&text=Introducing%20New%20Platform%20Access%20Control)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fplatform-access-control&text=Introducing%20New%20Platform%20Access%20Control)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fplatform-access-control&t=Introducing%20New%20Platform%20Access%20Control)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)