---
url: "https://docs.browserless.io/enterprise/private-deployment/graphql-api"
title: "Browserless GraphQL API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/private-deployment/graphql-api#__docusaurus_skipToContent_fallback)

On this page

Aside from providing the default `production-sfo.browserless.io` domain for running sessions, Browserless also exposes a GraphQL API for other operations. This document goes over some critical queries, however there's more information and descriptions at the interactive GraphiQL interface [located here](https://api.browserless.io/graphql/).

note

This GraphQL API is specifically for monitoring and managing private Browserless deployments (checking session pressure, metrics, etc). If you are looking for browser automation capabilities, you should use [BrowserQL](https://docs.browserless.io/browserql/start) instead, which is our dedicated browser automation API.

## Pressure [​](https://docs.browserless.io/enterprise/private-deployment/graphql-api\#pressure "Direct link to Pressure")

The `pressure` query shows how much load your instance(s) are under, and whether they can accept more traffic or not. This is real-time, so if you need to check if your instance can take more traffic you can do a request to check prior to running your `puppeteer.connect` call.

warning

The pressure queries are still in BETA and may experience breaking schema changes.

```codeBlockLines_p187
# https://api.browserless.io/graphql
{
  pressure(apiToken: "YOUR_API_TOKEN_HERE") {
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

## Metrics [​](https://docs.browserless.io/enterprise/private-deployment/graphql-api\#metrics "Direct link to Metrics")

The `metrics` query gives you insight to how your worker(s) are performing. It details things like successful, rejected, and timed-out sessions. Eventually this will be expanded to include things like average session-time and other helpful data-points.

Below is an example of a request for `metrics` and the responding payload.

warning

The metrics queries are still in BETA and may experience breaking schema changes.

```codeBlockLines_p187
# https://api.browserless.io/graphql
{
  metrics(apiToken: "YOUR_API_TOKEN_HERE") {
    successful
    rejected
    timedout
    queued
    cpu
    memory
    date
  }
}

```

This request returns an array of object detailing the metrics of your instance(s). If there's more than one instance stats are aggregated together in 5-minute intervals. CPU and Memory are averaged accross instances.

```codeBlockLines_p187
{
  "data": {
    "metrics": [\
      {\
        "successful": 0,\
        "rejected": 0,\
        "timedout": 0,\
        "queued": 0,\
        "cpu": 0.002734375,\
        "memory": 0.9055320561641963,\
        "date": 1524227700000\
      },\
      //...\
    ]
  }
}

```

## Sessions [​](https://docs.browserless.io/enterprise/private-deployment/graphql-api\#sessions "Direct link to Sessions")

The `sessions` query shows what browsers you have instantiated and running. This will only work for customers who have their dedicated fleet, for security purposes.

```codeBlockLines_p187
# https://api.browserless.io/graphql
{
  sessions(apiToken: "YOUR_API_TOKEN_HERE") {
     description
    devtoolsFrontendUrl
    live
    kill
    title
    type
    url
    trackingId
    browserId
    browserWSEndpoint
    browserWSEndpointClient
  }
}

```

warning

For security purposes, we limit the number of failed GraphQL request attempts. If you encounter rate limiting errors, you'll need to wait until the top of the hour before making additional requests.

## Pre-Session Checks [​](https://docs.browserless.io/enterprise/private-deployment/graphql-api\#pre-session-checks "Direct link to Pre-Session Checks")

If you've been getting rejections or queued, be sure to use the GraphQL API to do pre-session checks. This allows your workers to remain up and healthy, allowing sessions to go smoothly.

```codeBlockLines_p187
# https://api.browserless.io/graphql
{
  pressure(apiToken: "YOUR_API_TOKEN_HERE") {
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

You can use the `isAvailable` boolean to check to see if the instance can handle more connections. Otherwise you're free to write any sort of custom check with the provided JSON response.

## See More [​](https://docs.browserless.io/enterprise/private-deployment/graphql-api\#see-more "Direct link to See More")

There's a lot more you can do in the GraphQL API behind browserless, so be sure to [check it out here](https://api.browserless.io/graphql/)!

- [Pressure](https://docs.browserless.io/enterprise/private-deployment/graphql-api#pressure)
- [Metrics](https://docs.browserless.io/enterprise/private-deployment/graphql-api#metrics)
- [Sessions](https://docs.browserless.io/enterprise/private-deployment/graphql-api#sessions)
- [Pre-Session Checks](https://docs.browserless.io/enterprise/private-deployment/graphql-api#pre-session-checks)
- [See More](https://docs.browserless.io/enterprise/private-deployment/graphql-api#see-more)