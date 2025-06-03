---
url: "https://supabase.com/customers/mobbin"
title: "Mobbin | Supabase Customer Stories"
---

[Back](https://supabase.com/customers)

[Customer Stories](https://supabase.com/customers)

# How Mobbin migrated 200,000 users from Firebase for a better authentication experience.

Mobbin helps over 200,000 creators globally search and view the latest design patterns from well-known apps.

![How Mobbin migrated 200,000 users from Firebase for a better authentication experience. logo](https://supabase.com/_next/image?url=%2Fimages%2Fcustomers%2Flogos%2Fmobbin.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

About

Mobbin is a comprehensive, expert-curated library of interfaces from the best-in-class digital products that helps product designers find relevant design inspiration and references with significantly less time and effort.

[https://mobbin.design](https://mobbin.design/)

FoundedSingapore

Ready to get started?

[Contact sales](https://supabase.com/contact/enterprise)

Mobbin helps over 200,000 creators globally search and view the latest design patterns from well-known apps.
Their platform allows creators to search screenshots of mobile apps to inspire product development.
Creators use Mobbin to combine inspiration and develop new experiences.

## From Idea to 30,000 users in one Product Hunt launch [\#](https://supabase.com/customers/mobbin\#from-idea-to-30000-users-in-one-product-hunt-launch)

The initial concept for Mobbin was just a Dropbox full of screenshots. After sharing with their early users,
the team tried organizing them into folders but this quickly became unscalable. Clear interest from users encouraged them to build a full website. They used Firebase for the backend and launched on
[Product Hunt](https://www.producthunt.com/posts/mobbin-1).

Mobbin went viral, and within the first week, they had 30,000 users. They have now more than 400,000
registered users through word of mouth. Their curation continues to attract designers and creators globally.

![Mobbin cover](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fmobbin%2Fmobbin-cover.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Scaling issues put Mobbin growth at risk [\#](https://supabase.com/customers/mobbin\#scaling-issues-put-mobbin-growth-at-risk)

Firebase helped the team launch quickly, but at scale, they found Firebase lacked the functionality required for a high-quality user experience.

The first problem was duplicate user logins. Firebase Authentication doesn't automatically merge users with the same email address.
For example, users cannot log in with Google and Facebook if they share the same email address.
Users struggled to upgrade to a paid account because they couldn't remember which authentication provider they signed up with.

Next, they had issues with data integrity. While Firebase has 99.95% uptime, application code can (and does) fail.
Mobbin didn't want to implement idempotence for every mutative Firebase Function. Between a failed Function execution and a retry,
a document state might change without strict validation. The team could never be confident their data had the level of integrity they required.

Finally, the team grew concerned with their increasing Firebase bill. Because of the document-based data structure,
their API requests required several round trips. At one point, they were making 5 million API requests per month.
These round trips made their website slow and led to a notable time investment hacking together a fix.

![Mobbing screenshots](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fmobbin%2Fmobbin-screenshots.jpg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Migrating to Supabase [\#](https://supabase.com/customers/mobbin\#migrating-to-supabase)

Mobbin's initial product gave them a comprehensive understanding of customer requirements. For their second version,
they needed a better authentication experience, fairer pricing, and a relational database to deliver a quality
application sustainable for their business model.

The team found Supabase and realized it covered all the bases. Not only that, their team had experience with the
tools open source tools that Supabase is built with.

[Authentication](https://supabase.com/auth), built using [GoTrue](https://github.com/supabase/gotrue), instantly solved their users' login issues.
Under the hood, Supabase is just Postgres, and Jian Jie (co-founder and CTO of Mobbin) knows this is one of the best battle-tested
open source relational databases.

They decided that moving to Supabase was a no-brainer. The process itself was smooth - the real challenge was validating their
data integrity due to historical failures on their serverless functions.

Mobbin is now successfully running on top of Supabase, with superior performance compared to their old Firebase setup.
Because Supabase does not charge based on API requests, Mobbin significantly reduced their monthly spending without maintaining a custom backend.

> Migrating to Supabase meant that we could instantly fix our Auth problems and save money.
>
> Just being on Supabase alone gives us confidence we can deliver on whatever users need in the
> future.
>
> The cool thing is now we know under the hood it's just Postgres, it really does feel like
> anything is possible for the future of our product
>
> ![Jian Jie Liau, Co-founder and CTO at Mobbin. avatar](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Favatars%2Fjian-mobbin.jpg&w=64&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
>
> Jian Jie Liau, Co-founder and CTO at Mobbin.

## Supabase saves Mobbin time and money [\#](https://supabase.com/customers/mobbin\#supabase-saves-mobbin-time-and-money)

Migrating to Supabase helped the team at Mobbin instantly improve the end-user experience and save costs.
They now add new features with confidence, and they continue to help creators all over the globe find inspiration for their next project.
You can [check out Mobbin on their website](https://mobbin.design/browse/ios/apps).

[Sign up](https://supabase.com/dashboard/) for Supabase's Free Plan and set up a scalable backend in less than 2 minutes.

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)