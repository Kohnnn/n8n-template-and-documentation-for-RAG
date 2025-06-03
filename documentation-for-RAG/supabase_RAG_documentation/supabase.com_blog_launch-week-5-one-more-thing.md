---
url: "https://supabase.com/blog/launch-week-5-one-more-thing"
title: "One more thing"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# One more thing

19 Aug 2022

•

3 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![One more thing](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-one-more%2Flw5-one-more-thumb.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Let's be honest, it's never just one more thing.
Here are six more things that you need to know this Launch Week.

* * *

## Supabase Vault [\#](https://supabase.com/blog/launch-week-5-one-more-thing\#supabase-vault)

![Supabase Vault](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-one-more%2Flw5-vault.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Today we're announcing [Supabase Vault](https://supabase.com/blog/supabase-vault), a Postgres extension for managing secrets and encryption inside your database.
Vault is a thin usability-layer on top of [pgsodium](https://github.com/michelp/pgsodium).

Vault is not available on the Supabase Platform yet. This release is intended to gather user feedback.

[Read more](https://supabase.com/blog/supabase-vault).

* * *

## Auth UI [\#](https://supabase.com/blog/launch-week-5-one-more-thing\#auth-ui)

Auth UI was previously released as a single `<Auth/>` component in the [`@supabase/ui`](http://github.com/supabase/ui) library.
We recognized it was one of the most popular aspects of the library and developers were installing the library to use the Auth component alone.

From today, you can install it [from its own NPM package](https://github.com/supabase-community/auth-ui):

`
npm install @supabase/auth-ui-react
`

We've decoupled this library from our own styling system and you are now able to ( _deep breath..._): create your own theme, use a pre-existing Supabase theme, extend a theme using token variables, create multiple variations of themes (and then also extend them with variables), use CSS classes and also use any inline CSS styles.

This is all done with [stitches.js](https://stitches.dev/) (or more specifically, the [framework agnostic API](https://stitches.dev/docs/framework-agnostic)) to handle variants of components and the CSS properties.

A new feature in Auth UI is custom labels. You can now override any of the text labels—very useful for multiple language support.

Our initial release supports React, but we have prepared the repo for other frameworks. This release is a small step towards a larger feature—“ _Hosted Auth Pages_”. The wide range of customization will become useful for developers to tweak their Hosted Auth pages to reflect their brand personality.

[View the docs](https://supabase.com/docs/guides/auth/auth-helpers/auth-ui).

* * *

## Dashboard permissions [\#](https://supabase.com/blog/launch-week-5-one-more-thing\#dashboard-permissions)

![Dashboard permissions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-one-more%2Flw5-permissions.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've released granular permissions for the Supabase Dashboard. Dashboard permissions allow you assign roles to your team and to restrict what they can do.

We're starting with 3 roles—Owner, Administrator, and Developer—which you can edit in the Org settings of the Dashboard.
There's a tooltip in the header of the members table, which elaborates on the individual permissions available for each role.

[Read more](https://supabase.com/docs/guides/platform/access-control#manage-team-members).

* * *

## JSON schema validation [\#](https://supabase.com/blog/launch-week-5-one-more-thing\#json-schema-validation)

![JSON schema validation](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-one-more%2Flw5-jsonschema.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've released [`pg_jsonschema`](https://github.com/supabase/pg_jsonschema), a new Postgres extension for the Supabase Platform.

`pg_jsonschema` adds support for [JSON Schema](https://json-schema.org/) validation for `json` and `jsonb` data types, built with Rust.
You can read the blog post, which explains some of the scenarios where this is useful.

[Read more](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation).

* * *

## pg\_graphql v0.4.0 [\#](https://supabase.com/blog/launch-week-5-one-more-thing\#pg_graphql-v040)

![graphql.png](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-one-more%2Flw5-graphql.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've released a new version of `pg_graphql`, our GraphQL extension for Postgres.
This release adds support for `json` / `jsonb` types, the `in` filter, and introspection for much larger schemas (10x larger than before). We've fixed a few bugs too.

You can read the [release notes](https://github.com/supabase/pg_graphql/releases/tag/v0.4.0) and [documentation](https://supabase.github.io/pg_graphql/), and start using `pg_graphql` on Supabase today.

[Read more](https://supabase.com/blog/graphql-now-available).

* * *

## Multi-Factor Authentication [\#](https://supabase.com/blog/launch-week-5-one-more-thing\#multi-factor-authentication)

![Multi-Factor Authentication](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-one-more%2Flw5-mfa.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We've opened early-access signups for Multi-Factor Authentication (MFA). To be clear—this is for MFA for [Supabase Auth](https://supabase.com/auth),
which you can use to build additional layers of security in your applications (and not MFA for our Dashboard, which we will also release soon).

If you're interested, sign up and we'll grant your projects early access to the MFA API endpoints.

[Sign up](https://airtable.com/shrjcc9zi0RduHLIx).

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-5-one-more-thing&text=One%20more%20thing)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-5-one-more-thing&text=One%20more%20thing)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-5-one-more-thing&t=One%20more%20thing)

[Last post\\
\\
**Community Day** \\
\\
19 August 2022](https://supabase.com/blog/launch-week-5-community-day)

[Next post\\
\\
**pg\_jsonschema: JSON Schema support for Postgres** \\
\\
19 August 2022](https://supabase.com/blog/pg-jsonschema-a-postgres-extension-for-json-validation)

[launch-week](https://supabase.com/blog/tags/launch-week)

On this page

- [Supabase Vault](https://supabase.com/blog/launch-week-5-one-more-thing#supabase-vault)
- [Auth UI](https://supabase.com/blog/launch-week-5-one-more-thing#auth-ui)
- [Dashboard permissions](https://supabase.com/blog/launch-week-5-one-more-thing#dashboard-permissions)
- [JSON schema validation](https://supabase.com/blog/launch-week-5-one-more-thing#json-schema-validation)
- [pg\_graphql v0.4.0](https://supabase.com/blog/launch-week-5-one-more-thing#pg_graphql-v040)
- [Multi-Factor Authentication](https://supabase.com/blog/launch-week-5-one-more-thing#multi-factor-authentication)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-5-one-more-thing&text=One%20more%20thing)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-5-one-more-thing&text=One%20more%20thing)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Flaunch-week-5-one-more-thing&t=One%20more%20thing)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)