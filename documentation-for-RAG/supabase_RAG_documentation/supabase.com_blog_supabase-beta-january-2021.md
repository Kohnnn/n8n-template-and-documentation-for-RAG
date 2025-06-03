---
url: "https://supabase.com/blog/supabase-beta-january-2021"
title: "Supabase Beta January 2021"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Beta January 2021

02 Feb 2021

•

4 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

![Supabase Beta January 2021](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupabase-january-2021.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

New year, new features. We've been busy at Supabase during January and our community has been even busier. Here's a few things you'll find interesting.

### Quick demo [\#](https://supabase.com/blog/supabase-beta-january-2021\#quick-demo)

Watch a full demo:

Supabase Beta \| January 2021 - YouTube

Supabase

54.4K subscribers

[Supabase Beta \| January 2021](https://www.youtube.com/watch?v=DlybOLANG4s)

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

[Watch on YouTube](https://www.youtube.com/watch?v=DlybOLANG4s "Watch on YouTube")

### Count functionality [\#](https://supabase.com/blog/supabase-beta-january-2021\#count-functionality)

Anyone who has worked with Firebase long enough has become frustrated over the [lack](https://stackoverflow.com/questions/49979714/how-to-get-count-of-documents-in-a-collection) of `count` functionality. This isn't a problem with PostgreSQL! Our libraries now have support for PostgREST's [exact](https://postgrest.org/en/v7.0.0/api.html?highlight=count#exact-count), [planned](https://postgrest.org/en/v7.0.0/api.html?highlight=count#planned-count), and [estimated](https://postgrest.org/en/v7.0.0/api.html?highlight=count#estimated-count) counts. A massive thanks to [@dshukertjr](https://github.com/supabase/postgrest-js/issues/94#event-4210564301) for this adding support to our client library.

![Supabase now supports count functionality](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fpostgres-count.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### New Auth Providers [\#](https://supabase.com/blog/supabase-beta-january-2021\#new-auth-providers)

We enabled 2 new Auth providers - Facebook and Azure. Thanks to [@Levet](https://github.com/supabase/gotrue/pull/54) for the Azure plugin, and once again to [Netlify's amazing work](https://github.com/netlify/gotrue/issues/107) with GoTrue to implement Facebook.

![Supabase now supports Azure and Facebook Oauth providers](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fauth-azure-and-facebook.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Auth Audit Trail [\#](https://supabase.com/blog/supabase-beta-january-2021\#auth-audit-trail)

We have exposed the audit trail directly in the dashboard, as well as the GoTrue logs. Great for security and debugging.

![Supabase exposes the Auth Audit trail on the dashboard](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fauth-audit.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Auth UI widget [\#](https://supabase.com/blog/supabase-beta-january-2021\#auth-ui-widget)

In case our Auth endpoints aren't easy enough already, we've built a React [Auth Widget](https://ui.supabase.com/?path=/story/auth-auth--default) for you to drop into your app and to get up-and-running in minutes.

![Supabase has released a React Auth widget](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fauth-widget.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### New `auth.email()` function [\#](https://supabase.com/blog/supabase-beta-january-2021\#new-authemail-function)

We added a helper function for extracting the logged in user's email address.

![Supabase added an email function for using with Policies](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fpolicies-email.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### New Regions [\#](https://supabase.com/blog/supabase-beta-january-2021\#new-regions)

Launch your database in London or Sydney!

![Launch your database in London or Sydney](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fregions-london-sydney.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Copy rows as Markdown [\#](https://supabase.com/blog/supabase-beta-january-2021\#copy-rows-as-markdown)

You can now copy SQL results as Markdown - super useful for adding to blogs and issues.

![Copy query results as markdown](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fcountries.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### React server components [\#](https://supabase.com/blog/supabase-beta-january-2021\#react-server-components)

If you're excited by React Server components then check out the Supabase + Server Components experimental repo. [https://github.com/supabase/next-server-components](https://github.com/supabase/next-server-components)

![Use supabase with React Server components](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Freact-server-components-supabase.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Learn [\#](https://supabase.com/blog/supabase-beta-january-2021\#learn)

We know that Auth can be a bit daunting when you're just starting out, so we have created some intro videos to get you up to speed in no time:

- [Supabase Auth Deep Dive Part 1: JWTs](https://youtu.be/v3Exg5YpJvE)
- [Supabase Auth Deep Dive Part 2: Restrict Table Access](https://youtu.be/qY_iQ10IUhs)
- [Supabase Auth Deep Dive Part 3: User Based Access Policies](https://youtu.be/0LvCOlELs5U)

![We released a Auth Video Series](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fsupabase-auth-series.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

### Kaizen [\#](https://supabase.com/blog/supabase-beta-january-2021\#kaizen)

- Performance: We migrated all of our subdomains to Route53, implementing custom Let's Encrypt certs for your APIs. As a result, our read benchmarks are measuring up 12% faster.
- Performance: We upgrade your databases to the new [GP3](https://aws.amazon.com/about-aws/whats-new/2020/12/introducing-new-amazon-ebs-general-purpose-volumes-gp3/) storage for faster and more consistent throughput.

### Community [\#](https://supabase.com/blog/supabase-beta-january-2021\#community)

- @kiwicopple chats to @bdougie on HeavyBit's Jamstack Radio: [Link](https://www.heavybit.com/library/podcasts/jamstack-radio/ep-71-open-source-firebase-alternative-with-paul-copplestone-of-supabase)
- Watch @leerob from Vercel deploy a full Next.js app with Supabase in just 2 minutes:
[Link](https://twitter.com/leeerob/status/1351576575888797696)
- Redwood now supports Supabase:
[Link](https://twitter.com/redwoodjs/status/1347311574415863811)
- Deploy a full analytics solution using Umami:
[Link](https://twitter.com/mkalvas/status/1353880637506260994)
- Check out this open source Trello Clone:
[Link](https://twitter.com/joshnuss/status/1352094804335857664)
- Get started with Expo + Supabase using this starter template from Kiki:
[Link](https://twitter.com/kikiding/status/1352086899242856449)
- Use Supabase Auth with NestJS:
[Link](https://twitter.com/atsuhio/status/1348516650144780288?s=21)
- The community has made some serious advances on the [Dart](https://github.com/supabase?q=dart&type=&language=), [C#](https://github.com/supabase?q=csharp&type=&language=), [Python](https://github.com/supabase?q=python&type=&language=), and [Kotlin](https://github.com/supabase?q=kotlin&type=&language=) libraries.
- We were one of the fastest growing open source startups in Q4 last year: [Link](https://twitter.com/RunaCapital/status/1351122231791910916)

![This image shows the Supabase GitHub star growth.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fblog%2Fjan-21-starcount.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Source: [repository.surf/supabase](https://repository.surf/supabase)

### Coming next [\#](https://supabase.com/blog/supabase-beta-january-2021\#coming-next)

We're ramping up to "Launch week" at the end of Q1, where we will be giving you some very exciting new features (including Storage!).

### Get started [\#](https://supabase.com/blog/supabase-beta-january-2021\#get-started)

- Start using Supabase today: [supabase.com/dashboard](https://supabase.com/dashboard/)
- Make sure to [star us on GitHub](https://github.com/supabase/supabase)
- Follow us [on Twitter](https://twitter.com/supabase)
- Subscribe to our [YouTube channel](https://www.youtube.com/c/supabase)
- Become a [sponsor](https://github.com/sponsors/supabase)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2021&text=Supabase%20Beta%20January%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2021&text=Supabase%20Beta%20January%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2021&t=Supabase%20Beta%20January%202021)

[Last post\\
\\
**Roboflow.com choose Supabase to power Paint.wtf leaderboard** \\
\\
9 February 2021](https://supabase.com/blog/case-study-roboflow)

[Next post\\
\\
**Supabase Beta December 2020** \\
\\
2 January 2021](https://supabase.com/blog/supabase-beta-december-2020)

[supabase](https://supabase.com/blog/tags/supabase)

On this page

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2021&text=Supabase%20Beta%20January%202021)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2021&text=Supabase%20Beta%20January%202021)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-beta-january-2021&t=Supabase%20Beta%20January%202021)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)