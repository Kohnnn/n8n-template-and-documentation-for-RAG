---
url: "https://docs.browserless.io/enterprise/terminology"
title: "Terminology | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/terminology#__docusaurus_skipToContent_fallback)

On this page

On the main [browserless.io](https://www.browserless.io/) site, and inside this documentation site, you'll notice we use a few terms like "worker" or "session". Below is a list of commonly-used terms and what they mean.

### Worker [​](https://docs.browserless.io/enterprise/terminology\#worker "Direct link to Worker")

A worker is an instance of the Browserless container running on a virtual-machine. Our Cloud-Unit plans utilize a massive fleet of workers to handle the traffic needs of many users, and Enterprise users can engage with us and we'll provide the right size and quantity of workers in order to fulfill their needs.

### Session [​](https://docs.browserless.io/enterprise/terminology\#session "Direct link to Session")

A session is anytime Chrome is actively running and connected to. Browserless, however, automatically queues up to 2X this amount without any changes in your app's code. This allows you to set a baseline of concurrently running traffic, but allows for "bursts" of traffic without having to adjust any of your code (just keep using `puppeteer.connect`).

If more sessions are needed, you can either upgrade your worker's size or launch more instances of them to handle traffic.

### Pressure [​](https://docs.browserless.io/enterprise/terminology\#pressure "Direct link to Pressure")

Pressure indicates how much traffic is going on in your workers at any given time. Using the GraphQL API, you can fetch important details like `isAvailable` to see if your workers can handle another connection. Doing so will ensure your accout doesn't get overloaded and become unresponsive.

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

- [Worker](https://docs.browserless.io/enterprise/terminology#worker)
- [Session](https://docs.browserless.io/enterprise/terminology#session)
- [Pressure](https://docs.browserless.io/enterprise/terminology#pressure)