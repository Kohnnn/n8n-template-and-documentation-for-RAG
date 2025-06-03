---
url: "https://supabase.com/blog/edge-runtime-self-hosted-deno-functions"
title: "Supabase Edge Runtime: Self-hosted Deno Functions"
---

[Back](https://supabase.com/blog)

[Blog](https://supabase.com/blog)

# Supabase Edge Runtime: Self-hosted Deno Functions

11 Apr 2023

•

10 minute read

[![Lakshan Perera avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Flaktek.png&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Lakshan PereraEngineering](https://github.com/laktek)

[![Inian Parameshwaran avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F2155545%3Fv%3D4&w=96&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)\\
\\
Inian ParameshwaranEngineering](https://twitter.com/everConfusedGuy)

![Supabase Edge Runtime: Self-hosted Deno Functions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-2-edge-runtime%2Fedge-runtime-thumb.jpeg&w=3840&q=100&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

🆕✨ Edge Functions now natively supports npm modules and Node built-in APIs. [Learn more](https://supabase.com/blog/edge-functions-node-npm)

Today we’re open-sourcing [Supabase Edge Runtime](https://github.com/supabase/edge-runtime) for self-hosting Deno Edge Functions.

Edge Runtime is MIT licensed, written in Rust, and based on the latest Deno Runtime (1.32+). If you’ve been using the Supabase CLI to serve functions then you’re already one of our Beta testers (thanks!).

Self-Host Supabase Edge Functions - YouTube

Supabase

54.4K subscribers

[Self-Host Supabase Edge Functions](https://www.youtube.com/watch?v=cPGxPl1lx4Y)

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

[Watch on YouTube](https://www.youtube.com/watch?v=cPGxPl1lx4Y "Watch on YouTube")

## Host your Edge Functions anywhere [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#host-your-edge-functions-anywhere)

![Self-hosted functions tweet](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-2-edge-runtime%2Fself-hosted-functions-tweet.png&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

We [launched](https://supabase.com/blog/supabase-edge-functions) Supabase Edge Functions a little more than a year ago. We use [Deno Deploy](https://deno.com/deploy) to host your edge functions globally across 30+ data centers, so your users get super fast responses. This setup works great for us! We didn’t have an easy solution for self-hosting Edge Functions. We’re releasing Edge Runtime to address this.

One of our core principles is “ [Everything is portable](https://supabase.com/docs/guides/getting-started/architecture#everything-is-portable)”, meaning you should be able to take any part of the Supabase stack and host it yourself.

Supabase Edge Runtime is a web server written in Rust that uses a custom Deno runtime. It can serve TypeScript, JavaScript, and WASM functions. All your existing Edge Functions run on Edge Runtime without changing a single line of code.

## Better local development experience [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#better-local-development-experience)

Self-hosting is not the only benefit of Edge Runtime. It will improve the local development experience of Edge Functions.

### Serve all functions [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#serve-all-functions)

Supabase CLI can now serve all local Edge Functions by running `supabase functions serve`. Previously, you could only serve a single Edge Function at a time. This was not a great experience for local development. Some of you even devised [clever hacks](https://github.com/orgs/supabase/discussions/6786) to get around this limitation.

When you run `supabase functions serve`, the CLI uses Edge Runtime to serve all functions. It supports JWT verification, import maps, and passing custom environment variables. It hot-reloads local changes, giving you a seamless development experience.

### Dev/Prod parity [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#devprod-parity)

Edge Runtime improves Dev/Prod parity for Edge Functions. You may have encountered issues where an Edge Function works locally but fails when deployed. The main cause for this is Deno Deploy Runtime is more restrictive and [only supports](https://deno.com/deploy/docs/runtime-api) a subset of Deno APIs. Edge Runtime exposes the same APIs available in the Deno Deploy Runtime. This will help you spot issues faster while developing and avoid surprises when deploying.

### Enforcing memory/duration limits [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#enforcing-memoryduration-limits)

Another neat feature we built into Edge Runtime is the option to enforce limits on memory and wall-clock durations. Currently, we are setting them to sensible defaults (memory set to 150 MB and execution duration set to 60s). This will allow you to simulate your functions’ resource usage and handle the behavior if they run into the limits. Soon we will allow configuring these limits via CLI config so that you can match them with the real limits of the deployment platform.

## How to self-host Edge Functions [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#how-to-self-host-edge-functions)

We have put together a demo on how to self-host edge functions on [Fly.io](http://fly.io/) (you can also use other providers like Digital Ocean or AWS).

To try it yourself:

1. Sign up for an [Fly.io](http://fly.io/) account and install [flyctl](https://fly.io/docs/hands-on/install-flyctl/)

2. Clone the [demo repository](https://github.com/supabase/self-hosted-edge-functions-demo) to your machine

3. Copy your Edge Function into the `./functions` directory in the demo repo.

4. Update the Dockerfile to pull the latest edge-runtime image (check [releases](https://github.com/supabase/edge-runtime/pkgs/container/edge-runtime))

5. Optionally edit `./functions/main/index.ts`, adding any other request preprocessing logic (for example, you can enable JWT validation, handle CORS requests)

6. Run `fly launch` to create a new app to serve your Edge Functions

7. Access your Edge Function by visiting:

`https://{your-app-name}.fly.dev/{your-function-name}`


View the logs for the Edge Runtime by visiting Fly.io’s Dashboard > Your App > Metrics. You can serve Edge Runtime from multiple regions by running `fly regions add [REGION]`.

## Standing on the shoulders of Deno [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#standing-on-the-shoulders-of-deno)

You may wonder why we cannot use Deno Runtime to self-host functions. Isn’t it open-source and available as a Docker container?

[Deno Runtime](https://deno.com/runtime), by default, includes a wide array of built-in APIs, making it easy to use for multiple use cases out of the box. However, this makes it difficult to use for serving web requests. You need the runtime embedded within a web server that can boot fast and, for security, has a more restricted API.

However, Deno’s architecture makes it easy to extend its core capabilities and create a customized runtime to match our needs. Deno provides a Rust crate called `deno_core`, which abstracts the interactions with V8 JavaScript engine. Using `deno_core` we can create a JS context (known as a V8 Isolate). A V8 isolate has minimal overhead to boot up and a single process can host multiple V8 isolates. When you load a web page that contains scripts from multiple domains in a browser, each of them runs in a separate v8 isolate.

Deno team has a detailed 2-part blog post on [how to create a custom runtime](https://deno.com/blog/roll-your-own-javascript-runtime).

Edge Runtime implements an HTTP server (using [hyper](https://github.com/hyperium/hyper)) that listens to incoming requests. When Edge Runtime is booted, it spins up a JS context (V8 isolate), which we call the `Main Worker`. Main Worker runs in a separate thread, executing the provided main module. When a new HTTP request is received, the Rust runtime will forward it to the Main Worker.

You can write a main module to handle all incoming requests. This would look like a typical Deno Edge Function. The main difference is that it has access to a global object called “ `EdgeRuntime`”.

`EdgeRuntime` global provides methods to create and access `UserWorkers`. `Main Worker` can optionally delegate a request to a UserWorker to handle and respond.

User Workers are separate JS contexts (V8 isolates) that can run a given Edge Function. They have a restricted API (for example, they don’t get access to the host machine’s environment variables). You can also control the memory and duration a User Worker can run.

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-2-edge-runtime%2Fedge-runtime-dark-mode.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)

Here’s a simple implementation of a Main Worker that receives a request, then creates a User Worker and passes the handling of request to the worker.

`
serve(async (req: Request) => {
const memoryLimitMb = 150
const workerTimeoutMs = 1 * 60 * 1000
const noModuleCache = false
const importMapPath = null
const envVars = [\
    ['USER', 'foo'],\
    ['PASSWORD', 'BAR'],\
]
try {
    const worker = await EdgeRuntime.userWorkers.create({
      servicePath,
      memoryLimitMb,
      workerTimeoutMs,
      noModuleCache,
      importMapPath,
      envVars,
    })
    return await worker.fetch(req)
} catch (e) {
    const error = { msg: e.toString() }
    return new Response(JSON.stringify(error), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
}
})
`

## What’s Next? [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#whats-next)

Open-sourcing Edge Runtime is the first step of an exciting roadmap we have planned for Edge Functions. In the coming months, you will see tighter integrations with the rest of the Supabase ecosystem. Here are some sneak peeks at what is to come next.

### API Gateway to other Supabase services [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#api-gateway-to-other-supabase-services)

We plan to use Edge Runtime as a replacement for Kong, acting as an API gateway to other Supabase services. This will not only simplify the self-hosting setup but also give you the option to do Request pre/post-processing using JavaScript.

Here’s a simple example of re-routing a request to a different endpoint using Edge Runtime.

`
serve(async (req) => {
try {
    if (req.url.endsWith('/rest/v1/old_table')) {
      return await fetch('http://rest:3000/rest/v1/new_table', {
        headers: req.headers,
        method: req.method,
        body: req.body,
      })
    }
} catch (e) {
    const error = { msg: e.toString() }
    return new Response(JSON.stringify(error), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
}
})
`

### Scheduled Functions [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#scheduled-functions)

Since Edge Runtime’s Main Worker runs in the background as long as the server is running, we can utilize it to run periodic tasks.

For example, here’s a naive implementation of how it can be used to trigger a function every 2 minutes. In production, you need to account for server restarts and timer resetting.

`
const interval = 2 * 60 * 1000 // 2 minutes
try {
const worker = await EdgeRuntime.userWorkers.create({
    servicePath,
    memoryLimitMb,
    workerTimeoutMs,
    noModuleCache,
    importMapPath,
    envVars,
})
const req = new Request('http://localhost/scheduled-job')
setInterval(() => worker.fetch(req), interval)
} catch (e) {
console.error(e)
}
`

### Custom Global Objects [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#custom-global-objects)

Another exciting thing about shipping a custom JavaScript runtime is that we can control the available global objects in the runtime. In previous examples, you may noticed we used `EdgeRuntime` without importing a specific module to our function, this was possible because we exposed it as a global object in the runtime.

We can introduce a `Supabase` global object that can provide platform specific features. For example, similar to `Deno.writeTextFile` , we can expose a `Supabase.writeTextFile` which can directly write a file to Supabase Storage.

## We 💚 Contributions [\#](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions\#we-contributions)

We are excited to build Edge Runtime in public and involve the Supabase community in the process. As an initial beta release, there are still bugs and performance quirks to be ironed out. Don’t shy away from trying it though.

You can report any issues you encounter in repo’s [GitHub issues](https://github.com/supabase/edge-runtime/issues). If you have ideas on how to make edge-runtime better, reach out via [Twitter](https://twitter.com/supabase) or [Discord](http://discord.supabase.com/).

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

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-runtime-self-hosted-deno-functions&text=Supabase%20Edge%20Runtime%3A%20Self-hosted%20Deno%20Functions)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-runtime-self-hosted-deno-functions&text=Supabase%20Edge%20Runtime%3A%20Self-hosted%20Deno%20Functions)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-runtime-self-hosted-deno-functions&t=Supabase%20Edge%20Runtime%3A%20Self-hosted%20Deno%20Functions)

[Last post\\
\\
**Supabase Storage v3: Resumable Uploads with support for 50GB files** \\
\\
12 April 2023](https://supabase.com/blog/storage-v3-resumable-uploads)

[Next post\\
\\
**Supabase Logs: open source logging server** \\
\\
10 April 2023](https://supabase.com/blog/supabase-logs-self-hosted)

[launch-week](https://supabase.com/blog/tags/launch-week) [functions](https://supabase.com/blog/tags/functions)

On this page

- [Host your Edge Functions anywhere](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#host-your-edge-functions-anywhere)
- [Better local development experience](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#better-local-development-experience)
  - [Serve all functions](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#serve-all-functions)
  - [Dev/Prod parity](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#devprod-parity)
  - [Enforcing memory/duration limits](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#enforcing-memoryduration-limits)
- [How to self-host Edge Functions](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#how-to-self-host-edge-functions)
- [Standing on the shoulders of Deno](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#standing-on-the-shoulders-of-deno)
- [What’s Next?](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#whats-next)
  - [API Gateway to other Supabase services](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#api-gateway-to-other-supabase-services)
  - [Scheduled Functions](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#scheduled-functions)
  - [Custom Global Objects](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#custom-global-objects)
- [We 💚 Contributions](https://supabase.com/blog/edge-runtime-self-hosted-deno-functions#we-%F0%9F%92%9A-contributions)

Share this article

[Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-runtime-self-hosted-deno-functions&text=Supabase%20Edge%20Runtime%3A%20Self-hosted%20Deno%20Functions)[Share on Linkedin](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-runtime-self-hosted-deno-functions&text=Supabase%20Edge%20Runtime%3A%20Self-hosted%20Deno%20Functions)[Share on Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fedge-runtime-self-hosted-deno-functions&t=Supabase%20Edge%20Runtime%3A%20Self-hosted%20Deno%20Functions)

## Build in a weekend, scale to millions

[Start your project](https://supabase.com/dashboard) [Request a demo](https://supabase.com/contact/sales)

![diagram reference](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-7%2Fday-2-edge-runtime%2Fedge-runtime-dark-mode.svg&w=3840&q=75&dpl=dpl_7FY8EmFQ6G3YqautJ4Fvh1viLnvu)