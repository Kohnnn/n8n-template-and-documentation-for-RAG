---
url: "https://docs.browserless.io/baas/v1/hosted-service/graphql-api"
title: "Browserless GraphQL API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/hosted-service/graphql-api#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/enterprise/private-deployment/graphql-api) or [BrowserQL](https://docs.browserless.io/browserql/start).

Aside from providing the default `chrome.browserless.io` domain for running sessions, browserless also exposes a GraphQL API for other operations. This document goes over some critical queries.

info

The graphql API only applies to Dedicated and Enterprise accounts.

## Pressure [​](https://docs.browserless.io/baas/v1/hosted-service/graphql-api\#pressure "Direct link to Pressure")

The `pressure` query shows how much load your instance(s) are under, and whether they can accept more traffic or not. This is real-time, so if you need to check if your instance can take more traffic you can do a request to check prior to running your `puppeteer.connect` call.

warning

The pressure queries are still in BETA and may experience breaking schema changes.

```codeBlockLines_p187
# https://api.browserless.io/graphql
{
  pressure(apiToken: "YOUR-API-TOKEN") {
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

## Metrics [​](https://docs.browserless.io/baas/v1/hosted-service/graphql-api\#metrics "Direct link to Metrics")

The `metrics` query gives you insight to how your worker(s) are performing. It details things like successful, rejected, and timed-out sessions. Eventually this will be expanded to include things like average session-time and other helpful data-points.

Below is an example of a request for `metrics` and the responding payload.

warning

The metrics queries are still in BETA and may experience breaking schema changes.

```codeBlockLines_p187
# https://api.browserless.io/graphql
{
  metrics(apiToken: "YOUR-API-TOKEN") {
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

This request returns an array of object detailing the metrics of your instance(s). If there's more than one instance stats are aggregated together in 5-minute intervals. CPU and Memory are averaged across instances.

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

## Account Status [​](https://docs.browserless.io/baas/v1/hosted-service/graphql-api\#account-status "Direct link to Account Status")

The `accountStatus` query provides information about your account's usage and worker status. This is particularly useful for:

- Checking remaining time on usage-based accounts
- Monitoring worker launch status on dedicated plans

```codeBlockLines_p187
# https://api.browserless.io/graphql
{
  accountStatus(apiToken: "YOUR-API-TOKEN") {
    launching
    secondsAvailable
  }
}

```

This request returns an object with the following information:

```codeBlockLines_p187
{
  "data": {
    "accountStatus": {
      "launching": false,
      "secondsAvailable": 3600
    }
  }
}

```

The response includes:

- `launching`: Boolean indicating if a new worker is being launched (for legacy dedicated plans)
- `secondsAvailable`: Number of seconds remaining on your account (for legacy usage-based accounts)

info

This query is specifically for legacy accounts. For current account information, please refer to the [BaaS v2 documentation](https://docs.browserless.io/enterprise/private-deployment/graphql-api).

warning

For security purposes, we limit the number of failed GraphQL request attempts. If you encounter rate limiting errors, you'll need to wait until the top of the hour before making additional requests.

## See More [​](https://docs.browserless.io/baas/v1/hosted-service/graphql-api\#see-more "Direct link to See More")

There's a lot more you can do in the GraphQL API behind browserless, so be sure to [check it out here](https://api.browserless.io/graphql/)!

- [Pressure](https://docs.browserless.io/baas/v1/hosted-service/graphql-api#pressure)
- [Metrics](https://docs.browserless.io/baas/v1/hosted-service/graphql-api#metrics)
- [Account Status](https://docs.browserless.io/baas/v1/hosted-service/graphql-api#account-status)
- [See More](https://docs.browserless.io/baas/v1/hosted-service/graphql-api#see-more)