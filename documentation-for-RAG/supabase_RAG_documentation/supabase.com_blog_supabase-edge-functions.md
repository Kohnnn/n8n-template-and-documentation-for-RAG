---
url: "https://supabase.com/blog/supabase-edge-functions"
title: "Edge Functions are now available in Supabase"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Edge Functions are now available in Supabase

31 Mar 2022

•

10 minute read

[![Inian Parameshwaran avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F2155545%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Inian ParameshwaranEngineering](https://twitter.com/everConfusedGuy)

![Edge Functions are now available in Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Fthursday-functions%2Ffunctions-thumb.png&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

🆕✨ Edge Functions now natively supports npm modules and Node built-in APIs. [Learn more](https://supabase.com/blog/edge-functions-node-npm)

Today we're launching one of our [most](https://twitter.com/lau_cazanove/status/1506530181946691592) [requested](https://twitter.com/edgarasben/status/1506653203458363393) and [highly-](https://twitter.com/runjep/status/1507462077216088069) [anticipated](https://twitter.com/marcopolotwo/status/1506431782362632195) [features](https://github.com/supabase/supabase/discussions/4269) — Edge Functions. Edge Functions let you execute Typescript code close to your users, no matter where they're located.

Edge Functions are executed on the secure-by-default [Deno runtime](https://deno.land/), and deployed around the world in seconds using Deno's [hosted Deno Deploy offering](https://deno.com/deploy). However, as a user of Supabase Edge Functions, you don't need to know or worry about any of that; we handle all the gnarly details, delivering a seamless experience that allows you to focus on your business logic.

## Choosing a platform [\#](https://supabase.com/blog/supabase-edge-functions\#choosing-a-platform)

Serverless compute options can be broken down into two broad categories:

- Containers as a Service (e.g. Google Cloud Run, Fly.io)
- Functions as a Service (e.g. AWS Lambda, Cloudflare Workers, Fastly Compute @ Edge, Suborbital)

Additionally, there are self-hosted offerings within each category as well (e.g. Firecracker sort-of for the former, OpenFaaS for the latter).

Our first critical decision was to choose Functions as a Service (”FaaS”) over Containers and other alternatives. While Containers can allow for more flexible workloads, authoring and maintaining Functions allows for a substantially simpler developer experience-something Supabase has always focused on. As a Supabase user, all you need to think about is the business logic you wanted to write a Function for in the first place; you don't need to think about optimizing docker image builds, updating your system dependencies, etc.

Additionally, while a lot of work has been invested in improving container start-up times, Functions generally still enjoy significantly faster start-ups.

Our next major decision was to choose global deployments instead of a deploying to a specific geographical region.

![Functions deployment region](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Fthursday-functions%2Fwhere-functions-deploy.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
Launching Functions in a single region (e.g. close to your database) can present a lot of advantages if there are a lot of database operations being executed within your business logic.

However, Supabase already offers a flexible solution for that - [Database Functions](https://supabase.com/docs/guides/database/functions)! As such, for Supabase \[Edge\] Functions, we decided to deploy far-and-wide so that they are as close to your end-users as possible. You can even invoke a Database Function from an Edge Function, allowing you to enjoy the best of both worlds.

## The Deno runtime [\#](https://supabase.com/blog/supabase-edge-functions\#the-deno-runtime)

Deno is a modern Typescript and JavaScript runtime created with first-class support for web technologies. Here some of the reasons why we're excited about Deno:

### Open-source [\#](https://supabase.com/blog/supabase-edge-functions\#open-source)

_Deno Deploy_ is Deno's hosted service and, although it is proprietary, the Deno CLI is open source. This means that the open source offering from Deno maintains feature-parity with the proprietary service. If you use Deno to develop functions locally, its behavior will be the same as when deployed on the edge, unlocking an incredible developer experience. We couldn't achieve a similarly seamless experience with e.g. AWS Lambda, no matter how much we tried.

Deno even goes a step further than maintaining feature-parity, releasing all new APIs to open-source **first** before rolling them out to their hosted offering. This ensures that you can always develop and test bleeding-edge functionality locally, with all the tools you're used to and familiar with, before deploying to a hosted cloud environment.

### Batteries included [\#](https://supabase.com/blog/supabase-edge-functions\#batteries-included)

Deno comes with all the tools needed for a modern, productive developer experience, so you can spend less time searching through third party modules, and more time being productive. Out of the box, it includes support for Typescript, ES modules, and provides [test runners](https://deno.land/manual/testing), [formatters](https://deno.land/manual/tools/formatter), [linters](https://deno.land/manual/tools/linter), [bundlers](https://deno.land/manual/tools/bundler) and a package manager.

### Secure by default [\#](https://supabase.com/blog/supabase-edge-functions\#secure-by-default)

Like modern web browsers, the Deno runtime executes your code in a secure sandbox by default. Functions cannot access environment variables, network or filesystem unless they are explicitly allowed. Supply chain attacks have been a daunting problem in the Node ecosystem and Deno mitigates many of these attacks by having a security-first model.

## The Supa-Deno platform [\#](https://supabase.com/blog/supabase-edge-functions\#the-supa-deno-platform)

When a request comes in to an Edge Function you deploy on Supabase, it first lands at a “Relay”. The [Relay](https://github.com/supabase/functions-relay) acts as an API gateway, authenticating the JWT, and providing some additional functionality like logging and rate-limiting. Upon receiving the incoming request, the Relay retrieves the metadata for your Function, and uses it to construct a unique identifier (”Deployment ID”) for the Function. This Deployment ID then gets passed over to the Deno Deploy platform, which takes care of invoking your Function securely, and passing your output back to the Relay, which in turn passes it back to your end-user.

If a user's request comes in for your Function before it has been cached by the Deno Deploy platform (a ”cold start”), it reaches out to Supabase to retrieve your Functions code, and any associated permissions and secrets. Even though this might sound like a lot of work, we've worked to ensure that these cold starts are still pretty spiffy.

![Functions architecture](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Fthursday-functions%2Ffunctions-architecture.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

The primary goal of this architecture is to reduce the amount of work done in the hot path (marked in purple above). Each component in the hot path is globally distributed so that Edge Functions start up and respond to your users' requests fast.

### Region: Earth 🌎 [\#](https://supabase.com/blog/supabase-edge-functions\#region-earth-)

Supabase Edge Functions are deployed to one region - Earth (and we're exploring Mars as an additional region 👽). Edge Functions are deployed to over 30 data centers in a matter of seconds, ensuring fast response times no matter where your users are located.

[Database Functions](https://supabase.com/docs/guides/database/functions) (also served via our [REST and GraphQL APIs](https://supabase.com/docs/guides/database/api)) are colocated with your Postgres database, making them ideal for DB-intensive operations. These APIs can also be called seamlessly from your Supabase Edge Functions, making for a powerful combination.

### Scale to zero [\#](https://supabase.com/blog/supabase-edge-functions\#scale-to-zero)

Functions scale down to zero and you only pay for what you use. This makes them great for an extremely wide variety of workloads-whether you're starting out with extremely sporadic usage, or bursty request patterns, or using them consistently and heavily.

## A fun and efficient Developer Experience [\#](https://supabase.com/blog/supabase-edge-functions\#a-fun-and-efficient-developer-experience)

Delivering a phenomenal Developer Experience is something we care about a lot at Supabase. In the serverless functions space, we've found that local development and testing, coupled with fast deploys are critical.

We've [extended the Supabase CLI](https://supabase.com/docs/guides/local-development) to optimize the Edge Functions DX along these two dimensions. You get live-reloading, and a local Deno environment that matches the production environment, making for a great local iteration environment.

Once you've tested your Function locally (or gone straight to production cos you live _on the edge_ ... get it?) it takes just seconds to deploy a new function and see the logs streaming in your Dashboard—ensuring a tight iteration loop with your production environment.

Our observability pipeline has been built [using Logflare](https://supabase.com/blog/supabase-acquires-logflare). Structured logs from your Edge Functions get sent to Logflare, which also processes them into metrics. Your Supabase Dashboard is able to reach out to Logflare endpoints, and with some of the [(not so) secret sauce](https://supabase.com/blog/supabase-studio) from our front-end team, you get responsive charts and logs for your Edge Functions.

![new —> deploy —> invoke —> logs](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Fthursday-functions%2Ffunctions-new-deploy-invoke-logs.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)
new —> deploy —> invoke —> logs

To round off the end-to-end experience, `supabase-js` now works in Deno, making it easy to interact with the rest of your Supabase project from within your Edge Functions. Your project's URLs, API keys, and database connection strings are made available as environment variables within your Function to make this even easier. And if you want to interact with third-party APIs which require a secret key, such as Stripe, you can easily and securely make these available to your Function as environment variables via the Supabase CLI. To get an idea for what is possible, check out our examples page [here](https://github.com/supabase/supabase/tree/master/examples/edge-functions).

## Quickstart [\#](https://supabase.com/blog/supabase-edge-functions\#quickstart)

Supabase Edge Functions Quickstart - YouTube

Supabase

54.4K subscribers

[Supabase Edge Functions Quickstart](https://www.youtube.com/watch?v=5OWH9c4u68M)

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

[Watch on YouTube](https://www.youtube.com/watch?v=5OWH9c4u68M "Watch on YouTube")

Can't wait to get started? Develop, test, and deploy your first Supabase Edge Function in less than 7 minutes with our [Quickstart Video Tutorial](https://youtu.be/5OWH9c4u68M)!
Check the [Edge Functions Docs](https://supabase.com/docs/guides/functions) for the steps.

## Example apps: Mobile payments with React Native and Flutter [\#](https://supabase.com/blog/supabase-edge-functions\#example-apps-mobile-payments-with-react-native-and-flutter)

When researching use-cases with all of you, [processing payments](https://github.com/supabase/supabase/discussions/4269#discussioncomment-1748067) was being pointed out the most, so naturally, to support the launch, we've created example apps in collaboration with Stripe for [React Native](https://github.com/supabase-community/expo-stripe-payments-with-supabase-functions) and [Flutter](https://github.com/supabase-community/flutter-stripe-payments-with-supabase-functions), to allow you to get started and earn money even faster.

![functions-payment-example](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-4%2Fthursday-functions%2Ffunctions-payment.gif&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

## Can I host static sites [\#](https://supabase.com/blog/supabase-edge-functions\#can-i-host-static-sites)

Even though Deno supports [rendering `jsx` and `tsx` files](https://deno.land/manual/jsx_dom/jsx), we don't plan on becoming a website hosting provider with Edge Functions. For now, Edge Functions can only be invoked via the `POST` method. Offering secure and fast web hosting with a good developer experience is a hard problem to solve and there are [other](https://www.netlify.com/) [fantastic](https://vercel.com/) [providers](https://pages.cloudflare.com/) which do exactly that.

From our experience launching Supabase Storage last year, becoming a hosting provider is not something you want to take lightly. Malicious folks will upload their phishing sites whenever they get a chance and this can quickly spiral out of control, causing you to land on the denylist in the [Safe Browsing dataset](https://safebrowsing.google.com/). Even though we removed the project within minutes after being notified, various ISPs had already cached the information from the Safe browsing dataset and were “helping” their users by restricting access to the Supabase domain. This isn't something we're planning to repeat. But as always, we'd love to hear your use cases and feature requests, we're just one [GitHub discussion](https://github.com/supabase/supabase/discussions) away!

## Roadmap [\#](https://supabase.com/blog/supabase-edge-functions\#roadmap)

These are some of the features that are on our roadmap for functions.

- Cron functions to trigger your function on a schedule
- Studio support and self hosting multiple functions
- Optimizing cold start times
- Wasm is a great fit for running functions and companies like [Suborbital](https://suborbital.dev/) are leading the charge by making it easy to write functions that run in a Wasm-based runtime. Deno supports Wasm natively and we plan on allowing users to write their functions in languages that compile down to Wasm like Rust.
- We can expose Deno's permission model so that you can lock down your functions further by restricting outbound connections to specific domains.
- To invoke functions, you need a valid JWT signed by your project's JWT secret. We plan on making this verification optional. This enables more use cases like hooking up Supabase functions to Stripe webhooks where the function manages it's own authentication.

Give us a shout with your feedback and excited to see what you build in the hackathon!

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions&text=Edge%20Functions%20are%20now%20available%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions&text=Edge%20Functions%20are%20now%20available%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions&t=Edge%20Functions%20are%20now%20available%20in%20Supabase)

[Last post\\
\\
**Supabrew - Never Code Thirsty** \\
\\
1 April 2022](https://supabase.com/blog/supabrew)

[Next post\\
\\
**Introducing Supabase Enterprise** \\
\\
30 March 2022](https://supabase.com/blog/supabase-enterprise)

[launch-week](https://supabase.com/blog/tags/launch-week) [functions](https://supabase.com/blog/tags/functions)

On this page

- [Choosing a platform](https://supabase.com/blog/supabase-edge-functions#choosing-a-platform)
- [The Deno runtime](https://supabase.com/blog/supabase-edge-functions#the-deno-runtime)
  - [Open-source](https://supabase.com/blog/supabase-edge-functions#open-source)
  - [Batteries included](https://supabase.com/blog/supabase-edge-functions#batteries-included)
  - [Secure by default](https://supabase.com/blog/supabase-edge-functions#secure-by-default)
- [The Supa-Deno platform](https://supabase.com/blog/supabase-edge-functions#the-supa-deno-platform)
  - [Region: Earth 🌎](https://supabase.com/blog/supabase-edge-functions#region-earth-%F0%9F%8C%8E)
  - [Scale to zero](https://supabase.com/blog/supabase-edge-functions#scale-to-zero)
- [A fun and efficient Developer Experience](https://supabase.com/blog/supabase-edge-functions#a-fun-and-efficient-developer-experience)
- [Quickstart](https://supabase.com/blog/supabase-edge-functions#quickstart)
- [Example apps: Mobile payments with React Native and Flutter](https://supabase.com/blog/supabase-edge-functions#example-apps-mobile-payments-with-react-native-and-flutter)
- [Can I host static sites](https://supabase.com/blog/supabase-edge-functions#can-i-host-static-sites)
- [Roadmap](https://supabase.com/blog/supabase-edge-functions#roadmap)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions&text=Edge%20Functions%20are%20now%20available%20in%20Supabase)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions&text=Edge%20Functions%20are%20now%20available%20in%20Supabase)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-edge-functions&t=Edge%20Functions%20are%20now%20available%20in%20Supabase)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)