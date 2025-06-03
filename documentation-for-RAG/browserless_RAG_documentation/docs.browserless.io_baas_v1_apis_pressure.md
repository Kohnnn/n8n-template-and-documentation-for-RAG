---
url: "https://docs.browserless.io/baas/v1/apis/pressure"
title: "/pressure API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/pressure#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/intro) or [BrowserQL](https://docs.browserless.io/browserql/start).

The pressure API allows you to retrieve the current metrics of your worker(s) **and is only available for dedicated and self-hosted accounts.** This API is different to the [metrics API](https://chrome.browserless.io/docs/#/Management%20API/get_metrics) since the pressure API only returns one object (the current metrics) whereas the metrics API returns a collection of all the metrics data with one week of history.

Check out the [pressure API schema](https://chrome.browserless.io/docs/#/Management%20API/get_pressure) defined in our Swagger page.

## Gathering metrics from your workers [​](https://docs.browserless.io/baas/v1/apis/pressure\#gathering-metrics-from-your-workers "Direct link to Gathering metrics from your workers")

To see statistics regarding your workers, simply issue a `GET` request to `/pressure`:

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/pressure?token=MY_API_TOKEN

```

warning

Remember that running this in the browser will expose your API key!

Running this cURL request will result in an output like:

```codeBlockLines_p187
{
  "date": 0,
  "successful": 0,
  "queued": 0,
  "rejected": 0,
  "unhealthy": 0,
  "memory": 0,
  "cpu": 0,
  "timedout": 0,
  "totalTime": 0,
  "meanTime": 0,
  "maxTime": 0,
  "minTime": 0,
  "maxConcurrent": 0,
  "sessionTimes": [0]
}

```

- [Gathering metrics from your workers](https://docs.browserless.io/baas/v1/apis/pressure#gathering-metrics-from-your-workers)