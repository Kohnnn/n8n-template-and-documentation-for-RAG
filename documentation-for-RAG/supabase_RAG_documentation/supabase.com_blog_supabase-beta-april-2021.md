---
url: "https://supabase.com/blog/supabase-beta-april-2021"
title: "Supabase Beta April 2021"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta April 2021

05 May 2021

•

5 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Supabase Beta April 2021](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fapril-2021%2Frelease-apr-2021.jpg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

This month was a "gardening" month for Supabase. The team focused on stability, security, and community support.
Check out what we were working on below, as well as some incredible Community contributions.

### Quick demo [\#](https://supabase.com/blog/supabase-beta-april-2021\#quick-demo)

Watch a full demo:

Supabase Beta \| April 2021 - YouTube

Supabase

54.4K subscribers

[Supabase Beta \| April 2021](https://www.youtube.com/watch?v=uWJmUTCFdak)

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

[Watch on YouTube](https://www.youtube.com/watch?v=uWJmUTCFdak "Watch on YouTube")

## Light Mode [\#](https://supabase.com/blog/supabase-beta-april-2021\#light-mode)

We're a developer tool, which means that Dark Mode is [extremely popular](https://twitter.com/supabase/status/1388131942919376904).

![This poll on twitter shows that 78.5% of our developer base use Dark Mode for the IDE](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fapril-2021%2Ftwitter-darkmode.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

While Dark mode is great, for some people it's not an option. Dark Mode is difficult to use for developers with astigmatisms,
or even just working in brightly-lit environments.

So today we're shipping Light Mode. Access it in the settings of your [Dashboard](https://supabase.com/dashboard).

## Translations [\#](https://supabase.com/blog/supabase-beta-april-2021\#translations)

With the help of the community, we [started internationalizing](https://github.com/supabase/supabase/issues/1341) our main repository:

- [Arabic \| العربية](https://github.com/supabase/supabase/blob/master/i18n/README.ar.md)
- [Chinese / 中文](https://github.com/supabase/supabase/blob/master/i18n/README.zh-cn.md)
- [Dutch / Nederlands](https://github.com/supabase/supabase/blob/master/i18n/README.nl.md)
- [English](https://github.com/supabase/supabase)
- [French / Français](https://github.com/supabase/supabase/blob/master/i18n/README.fr.md)
- [German / Deutsch](https://github.com/supabase/supabase/blob/master/i18n/README.de.md)
- [Hindi / हिंदी](https://github.com/supabase/supabase/blob/master/i18n/README.hi.md)
- [Nepali / नेपाली](https://github.com/supabase/supabase/blob/master/i18n/README.ne.md)
- [Italiano / Italian](https://github.com/supabase/supabase/blob/master/i18n/README.it.md)
- [Japanese / 日本語](https://github.com/supabase/supabase/blob/master/i18n/README.jp.md)
- [Norwegian (Bokmål) / Norsk (Bokmål)](https://github.com/supabase/supabase/blob/master/i18n/README.nb-no.md)
- [Polish / Polski](https://github.com/supabase/supabase/blob/master/i18n/README.pl.md)
- [Portuguese / Portuguese](https://github.com/supabase/supabase/blob/master/i18n/README.pt.md)
- [Portuguese (Brazilian) / Português Brasileiro](https://github.com/supabase/supabase/blob/master/i18n/README.pt-br.md)
- [Russian / Pусский](https://github.com/supabase/supabase/blob/master/i18n/README.ru.md)
- [Spanish / Español](https://github.com/supabase/supabase/blob/master/i18n/README.es.md)
- [Traditional Chinese / 正體中文](https://github.com/supabase/supabase/blob/master/i18n/README.zh-tw.md)
- [Turkish / Türkçe](https://github.com/supabase/supabase/blob/master/i18n/README.tr.md)
- [Ukrainian / Українська](https://github.com/supabase/supabase/blob/master/i18n/README.uk.md)

![Map of the world](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fapril-2021%2Fmap.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## OpenAPI spec for Storage [\#](https://supabase.com/blog/supabase-beta-april-2021\#openapi-spec-for-storage)

We released [Storage Api docs](https://supabase.github.io/storage) built using OpenAPI (swagger).

![Storage API documentation](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fapril-2021%2Fstorage-openapi.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Stripe Sync Engine (Experimental) [\#](https://supabase.com/blog/supabase-beta-april-2021\#stripe-sync-engine-experimental)

We [open-sourced a server](https://github.com/supabase/stripe-sync-engine) which keeps any Postgres database in sync with Stripe.
This is experimental only. We're evaluating other tools such as [Singer](https://www.singer.io/tap/stripe/postgresql/),
which provide a more general solution (but are less "realtime"), and we're opening it up here to gather feedback.

![Stripe sync engine](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fapril-2021%2Fstripe-sync-engine.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Community spotlight: Threaded comments [\#](https://supabase.com/blog/supabase-beta-april-2021\#community-spotlight-threaded-comments)

One of the most powerful Postgres features is "recursive CTEs" which can be used for nested items (comments, pages, friend-graphs). [@lawrencecchen](https://twitter.com/lawrencecchen) has built a full [Threaded Comments demo](https://github.com/lawrencecchen/threaded-comments) which you can [Deploy with a single click](https://github.com/lawrencecchen/threaded-comments#instant-deploy). Want to add comments to your blog with [Full Text Search](https://supabase.com/docs/reference/javascript/textsearch)? Just use Postgres.

## Community spotlight: SupaScript [\#](https://supabase.com/blog/supabase-beta-april-2021\#community-spotlight-supascript)

It looks like [@burggraf2](https://twitter.com/burggraf2) got tired of waiting for us to ship Functions, and decided to
build a whole JS ecosystem within his Supabase database. If you want to write PG functions in JS, import remote libraries
from the web, and console log to your browser, check out this [SupaScript repo](https://github.com/burggraf/SupaScript).

`
// After installing:
// https://github.com/burggraf/SupaScript#installation
/**
* Get all users who logged in this week.
* Use in the database:  select * from users_this_week();
* Use in the browser:   supabase.rpc('users_this_week');
*/
create or replace function users_this_week()
returns json as $$
const moment = require('https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.1/moment.js', false);
const lastWeek = moment().subtract(7, 'days');
const query = 'select * from auth.users where created_at > $1'
const users = sql(query, lastWeek);
return users;
$$ language plv8;
`

## Community spotlight: Fireship [\#](https://supabase.com/blog/supabase-beta-april-2021\#community-spotlight-fireship)

Fireship reviewed Supabase last week, and despite being a (self-proclaimed) Firebase fan-boy, the review was very impartial.

Is Supabase Legit? Firebase Alternative Breakdown - YouTube

Fireship

3.89M subscribers

[Is Supabase Legit? Firebase Alternative Breakdown](https://www.youtube.com/watch?v=WiwfiVdfRIc)

Fireship

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

[Watch on YouTube](https://www.youtube.com/watch?v=WiwfiVdfRIc "Watch on YouTube")

## Community [\#](https://supabase.com/blog/supabase-beta-april-2021\#community)

- Watch [@everConfusedGuy](https://twitter.com/everConfusedGuy)'s talk at DevX conf - Building Supabase Storage: [YouTube video](https://www.youtube.com/watch?v=YsUYOsq_o7g)
- DuckDuckAbdaal by [@Nutlope](https://twitter.com/Nutlope) \- a personalized search engine: [Twitter](https://twitter.com/Nutlope/status/1389082406477463557)
- Supabase in 6 minutes by [Georges Duverger](https://www.youtube.com/channel/UCNERPJ-vs61KEsD_dRNWFIw): [YouTube video](https://www.youtube.com/watch?v=c8DNV9yl0mg)
- Build a SaaS Platform with Stripe by [@\_\_dijonmusters:](https://twitter.com/_dijonmusters) [DEV blog](https://dev.to/dijonmusters/series/12346)
- Supabase & Sveltekit by Svelte Mastery: [YouTube video](https://www.youtube.com/watch?v=j4AV2Liojk0)
- Firebase vs. Supabase - Draftbit Office Hours: [YouTube Livestream](https://www.youtube.com/watch?v=9Yg6i_zCuiM)

**Supabase GitHub Star Growth**

- Our [main GitHub repo](https://github.com/supabase/supabase) grew 60% (by stars) and we saw a flood of new contributors.
- Our [UI Library](https://github.com/supabase/ui) grew 175%
- Our [Realtime Server](https://github.com/supabase/realtime) grew 39% after landing on the [front page of Hacker News](https://news.ycombinator.com/item?id=26968449).

![Stars from github](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fapril-2021%2Fstars-all.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Source: [repository.surf/supabase](https://repository.surf/supabase)

If you want to keep up to date, make sure you [subscribe to our YouTube channel](https://www.youtube.com/c/supabase) or [follow us on Twitter](https://twitter.com/supabase).

## Coming Next [\#](https://supabase.com/blog/supabase-beta-april-2021\#coming-next)

You might have noticed our Dashboard slowly changing (improving), as we migrate the components out to our [open source UI Library](https://github.com/supabase/ui). This progression is an important step towards offering a UI for [Local Development](https://supabase.com/docs/guides/local-development) and [Self Hosting](https://supabase.com/docs/guides/self-hosting).

We're also working on our [Workflows engine](https://supabase.com/blog/supabase-workflows). This is quite a large task, but we're making progress and aiming to ship sometime in July.

## One more thing [\#](https://supabase.com/blog/supabase-beta-april-2021\#one-more-thing)

[We started hiring](https://supabase.com/docs/careers).

![screenshot of our hiring page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fapril-2021%2Fhiring.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Get started [\#](https://supabase.com/blog/supabase-beta-april-2021\#get-started)

- Start using Supabase today: [supabase.com/dashboard](https://supabase.com/dashboard/)
- Make sure to [star us on GitHub](https://github.com/supabase/supabase)
- Follow us [on Twitter](https://twitter.com/supabase)
- Subscribe to our [YouTube channel](https://www.youtube.com/c/supabase)
- Become a [sponsor](https://github.com/sponsors/supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-april-2021&text=Supabase%20Beta%20April%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-april-2021&text=Supabase%20Beta%20April%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-april-2021&t=Supabase%20Beta%20April%202021)

[Last post\\
\\
**Supabase Beta June 2021** \\
\\
2 June 2021](https://supabase.com/blog/supabase-beta-june-2021)

[Next post\\
\\
**Supabase Beta March 2021** \\
\\
6 April 2021](https://supabase.com/blog/supabase-beta-march-2021)

[release-notes](https://supabase.com/blog/tags/release-notes)

On this page

- [Light Mode](https://supabase.com/blog/supabase-beta-april-2021#light-mode)
- [Translations](https://supabase.com/blog/supabase-beta-april-2021#translations)
- [OpenAPI spec for Storage](https://supabase.com/blog/supabase-beta-april-2021#openapi-spec-for-storage)
- [Stripe Sync Engine (Experimental)](https://supabase.com/blog/supabase-beta-april-2021#stripe-sync-engine-experimental)
- [Community spotlight: Threaded comments](https://supabase.com/blog/supabase-beta-april-2021#community-spotlight-threaded-comments)
- [Community spotlight: SupaScript](https://supabase.com/blog/supabase-beta-april-2021#community-spotlight-supascript)
- [Community spotlight: Fireship](https://supabase.com/blog/supabase-beta-april-2021#community-spotlight-fireship)
- [Community](https://supabase.com/blog/supabase-beta-april-2021#community)
- [Coming Next](https://supabase.com/blog/supabase-beta-april-2021#coming-next)
- [One more thing](https://supabase.com/blog/supabase-beta-april-2021#one-more-thing)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-april-2021&text=Supabase%20Beta%20April%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-april-2021&text=Supabase%20Beta%20April%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-april-2021&t=Supabase%20Beta%20April%202021)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)