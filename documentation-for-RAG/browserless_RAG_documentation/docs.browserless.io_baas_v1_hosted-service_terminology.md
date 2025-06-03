---
url: "https://docs.browserless.io/baas/v1/hosted-service/terminology"
title: "Browserless Terminology | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/hosted-service/terminology#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/enterprise/terminology) or [BrowserQL](https://docs.browserless.io/browserql/start).

On the main browserless.io site, and inside this documentation site, you'll notice we use a few terms like "worker" or "session". Below is a list of commonly-used terms and what they mean.

## Worker [​](https://docs.browserless.io/baas/v1/hosted-service/terminology\#worker "Direct link to Worker")

A worker is an instance of the Browserless container, running on a virtual-machine. The size of the worker will dictate what types of sites and interactions you can do. For Browserless Enterprise customers, we go through an onboarding process where we help pick the right size and class of machine in order to properly support your workloads.

## Session [​](https://docs.browserless.io/baas/v1/hosted-service/terminology\#session "Direct link to Session")

A session is anytime Chrome is actively running and connected to. Browserless, however, automatically queues up to 2X this amount without any changes in your app's code for _Enterprise plans_ only. Our cloud-unit fleet is provisioned such that you shouldn't ever encounter a sluggish connection. This allows you to set a baseline of traffic throughput, but allows for "bursts" of traffic without having to adjust any of your code (just keep using `puppeteer.connect`).

If more sessions are needed, [please reach out to us](https://www.browserless.io/contact).

## Pressure [​](https://docs.browserless.io/baas/v1/hosted-service/terminology\#pressure "Direct link to Pressure")

info

The Pressure API is only available for Enterprise plans that run on a dedicated fleet of machines.

Pressure indicates how much traffic is going on in your workers at any given time. Using the GraphQL API, you can fetch important details like `isAvailable` to see if your workers can handle another connection. Doing so will ensure your account doesn't get overloaded and become unresponsive.

```codeBlockLines_p187
# https://api.browserless.io/graphql
{
  pressure(apiToken: "YOUR_API_KEY") {
    running
    recentlyRejected
    queued
    isAvailable
    date
  }
}

```

This request will return a JSON object with the following payload:

```codeBlockLines_p187
// JSON returned
{
  "data": {
    "pressure": {
      "running": 0,
      "recentlyRejected": 0,
      "queued": 0,
      "isAvailable": true,
      "date": 1524762532204
    }
  }
}

```

## More Coming [​](https://docs.browserless.io/baas/v1/hosted-service/terminology\#more-coming "Direct link to More Coming")

Did we miss something? [Send us an email and let us know!](https://www.browserless.io/contact)

- [Worker](https://docs.browserless.io/baas/v1/hosted-service/terminology#worker)
- [Session](https://docs.browserless.io/baas/v1/hosted-service/terminology#session)
- [Pressure](https://docs.browserless.io/baas/v1/hosted-service/terminology#pressure)
- [More Coming](https://docs.browserless.io/baas/v1/hosted-service/terminology#more-coming)