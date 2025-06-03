---
url: "https://supabase.com/blog/alpha-launch-postmortem"
title: "Alpha Launch Postmortem"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Alpha Launch Postmortem

10 Jul 2020

•

6 minute read

[![Paul Copplestone avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fkiwicopple.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Paul CopplestoneCEO and Co-Founder](https://github.com/kiwicopple)

On May 27 Supabase hit the [top of Hacker News](https://news.ycombinator.com/item?id=23319901) and stayed on the front page for more than 24 hours.

Since then, Supabase has been featured on the [Stack Overflow podcast](https://stackoverflow.blog/2020/06/05/podcast-241-new-tools-for-new-times/), hit the [trending page](https://twitter.com/supabase/status/1268062559023685633) on GitHub, and scaled to over 1000 databases.

Here is everything that went wrong along the way.

## Quick stats - launch week [\#](https://supabase.com/blog/alpha-launch-postmortem\#quick-stats---launch-week)

Before we get into the details, here are some high-level numbers for the week following the launch.

We had 30,000 new website visitors to [supabase.io](https://supabase.com/):

![This graph shows the traffic to our website, that peaks at 15,000 the first day and tails off throughout the week. We had a total of 30,000 visitors to our site. That's according to Google Analytics though, and everyone on HN blocks GA so who knows what the real number is.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupabase-traffic-may.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We had over 1400 signups in 7 days:

![This graph shows our signups. Before the launch we had around 100 signups. After the launch it sky-rocketed to 600 in the first day, 900 by the second, and 1000 by the third day. By the end of the week we had over 1400 signups.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fhn-launch.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

GitHub stars rocketed for our two main repos, [supabase](https://github.com/supabase/supabase) and [realtime](https://github.com/supabase/realtime).

![This graph shows our github stars. It's basically a vertical line. Our main repo went from 300 stars to 1300 overnight.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupabase-github-stars-june.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## The good [\#](https://supabase.com/blog/alpha-launch-postmortem\#the-good)

Here are the things that survived well.

### Middleware: docker compose up [\#](https://supabase.com/blog/alpha-launch-postmortem\#middleware-docker-compose-up)

This was the most surprising survivor. Our middleware was served from a single Ubuntu server with 4 CPUs and 8GB of RAM. This server was running our middleware using `docker compose up`:

![This image shows in middleware architecture. We used docker compose to pull up 5 open source tools: Kong, Realtime, PostgREST, PG-API, and PG-BOSS.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsupabase-middleware-docker.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

In case you're wondering why any sane company would use that in production, it's because we weren't planning to launch - the HackerNews post was created by an early GitHub follower, while we were alpha testing, and it was too scary to migrate the middleware while it was servicing the thundering herd. All Supabase projects use the same middleware stack (without docker compose), so I guess this counts as a successful load test.

We have since migrated our middleware to multiple ECS clusters, globally load-balanced using AWS's [Global Accelerator](https://aws.amazon.com/global-accelerator/).

### Frontend: Netlify, Vercel, Auth0 [\#](https://supabase.com/blog/alpha-launch-postmortem\#frontend-netlify-vercel-auth0)

We serve our marketing site ( [supabase.io](https://supabase.com/)) from Netlify. It's a static-build [Docusaurus (v2)](https://v2.docusaurus.io/) site, so it had no problems (apart from one developer in Russia who couldn't access the site - it looks like some of Netlify's IP addresses are blocked there).

We serve our app ( [supabase.com/dashboard](https://supabase.com/dashboard)) using Vercel, and the login system uses Auth0. These were both rock-solid. Before the launch we noticed that Vercel was extremely slow on their Free Plan, and once we upgraded to their Pro Plan for multi-region deploys it solved performance issues. It looks like they are changing their plans again so buyer beware.

## The Bad [\#](https://supabase.com/blog/alpha-launch-postmortem\#the-bad)

### Digital Ocean cloud limits [\#](https://supabase.com/blog/alpha-launch-postmortem\#digital-ocean-cloud-limits)

In May we were using Digital Ocean to serve all of our customer databases. We hit the first server limit (400 servers) in the space of a few hours. They bumped our limit up to 1000 and we hit that again a few hours later.

Digital Ocean were very responsive when we asked for increases, each time responding in 30 minutes or less.

### Cloudflare cloud limits [\#](https://supabase.com/blog/alpha-launch-postmortem\#cloudflare-cloud-limits)

Each Supabase project gets a unique URL for their API and database. This is set up using Cloudflare's API. This was a seamless process until we hit the 1000-subdomain limit, at 4am in the morning. My cofounder was awake, managed to identify the problem early, and reached out to the support to increase the limit.

Cloudflare support advised him to upgrade the account to increase the limit, but the upgrade could only be done by the owner (me). Unfortunately my phone was on silent, so for 3 hours our systems were down. Ideally any one of our team could have upgraded our account, but I imagine that Cloudflare have their reasons for this restriction.

## The Ugly - migrating 1800 servers [\#](https://supabase.com/blog/alpha-launch-postmortem\#the-ugly---migrating-1800-servers)

Let me start by saying that Digital Ocean have been great for getting up and running. The experience was simple to start with, but ended painfully.

### Digital Ocean production errors [\#](https://supabase.com/blog/alpha-launch-postmortem\#digital-ocean-production-errors)

The first sign of problems were the frequent production errors. This is a screenshot of emails from Digital ocean for the month of June.

![This image shows all the emails I was receiving from Digital Ocean. I was receiving an email every other day about servers which needed to be migrated.](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fdigital-ocean-emails-errors.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Each of these emails represents one or more servers that has a critical issue:

> We have identified an issue on the physical machine hosting one or more of your Droplets. In the event that we are not able to perform a live migration of a Droplet, we will perform an offline migration during which the Droplet will be powered off and migrated offline during the window.

Luckily we are in alpha, and our community has been extremely patient.

### Credit limits [\#](https://supabase.com/blog/alpha-launch-postmortem\#credit-limits)

Most of our frustration was due to their internal policy around credits program. We were generously granted $10,000 Digital Ocean credits in February through Stripe Atlas, and so they became our primary cloud provider.

Digital Ocean have another (more generous) credits package for YC companies. Unfortunately when we applied for this we were told we weren't eligible because it was a "Partner switch" from Stripe to YC. This was frustrating because a "Partner switch" is completely arbitrary to us as a customer.

Also we had conveniently just run out of credits. We don’t expect cloud providers to fund our inefficiencies, but we needed time to optimize our infrastructure after our surprise launch. We had assumed that the more generous credits package was guaranteed - an assumption which cost us several thousand dollars. After swift deliberation, we decided to migrate away from Digital Ocean.

## Going Forward: AWS t3a [\#](https://supabase.com/blog/alpha-launch-postmortem\#going-forward-aws-t3a)

In the past 3 weeks we have migrated 1800 servers over to AWS.

We are on the AWS "Activate" program, which grants us $100,000 credits. Since Firebase has a very generous free-tier, and we want to be able to offer Supabase developers a similar experience, this is ultimately a huge benefit to our community.

The AWS team were helpful, suggesting their new `t3a` instances. We're already seeing improvements, with database startup times almost halved from ~90s to ~50s. From our research, this is the fastest Postgres setup in the market.

We will release a detailed write-up on these instances in the next few weeks. Sign up to our newsletter if you want to be notified when we release the post.

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Falpha-launch-postmortem&text=Alpha%20Launch%20Postmortem)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Falpha-launch-postmortem&text=Alpha%20Launch%20Postmortem)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Falpha-launch-postmortem&t=Alpha%20Launch%20Postmortem)

[Last post\\
\\
**Supabase Alpha July 2020** \\
\\
2 August 2020](https://supabase.com/blog/supabase-alpha-july-2020)

[Next post\\
\\
**What are PostgreSQL Templates?** \\
\\
9 July 2020](https://supabase.com/blog/postgresql-templates)

[supabase](https://supabase.com/blog/tags/supabase)

On this page

- [Quick stats - launch week](https://supabase.com/blog/alpha-launch-postmortem#quick-stats---launch-week)
- [The good](https://supabase.com/blog/alpha-launch-postmortem#the-good)
- [The Bad](https://supabase.com/blog/alpha-launch-postmortem#the-bad)
- [The Ugly - migrating 1800 servers](https://supabase.com/blog/alpha-launch-postmortem#the-ugly---migrating-1800-servers)
- [Going Forward: AWS t3a](https://supabase.com/blog/alpha-launch-postmortem#going-forward-aws-t3a)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Falpha-launch-postmortem&text=Alpha%20Launch%20Postmortem)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Falpha-launch-postmortem&text=Alpha%20Launch%20Postmortem)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Falpha-launch-postmortem&t=Alpha%20Launch%20Postmortem)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)