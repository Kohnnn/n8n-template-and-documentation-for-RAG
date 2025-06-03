---
url: "https://docs.browserless.io/baas/v1/apis/metrics"
title: "/metrics API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/metrics#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/enterprise/utility-functions/metrics) or [BrowserQL](https://docs.browserless.io/browserql/start).

The metrics API allows you to retrieve an array of session statistics **and is only available for dedicated and self-hosted accounts.** This API is different to the [pressure API](https://chrome.browserless.io/docs/#/Management%20API/get_pressure) since the metrics API returns a collection of all the metrics data with one week of history whereas the pressure API only returns one object (the current metrics).

Check out the [metrics API schema](https://chrome.browserless.io/docs/#/Management%20API/get_metrics) defined in our Swagger page.

## Gathering metrics array from your workers [​](https://docs.browserless.io/baas/v1/apis/metrics\#gathering-metrics-array-from-your-workers "Direct link to Gathering metrics array from your workers")

To see statistics regarding your workers, simply issue a `GET` request to `/metrics`:

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/metrics?token=MY_API_TOKEN

```

warning

Remember that running this in the browser will expose your API key!

Running this cURL request will result in an output like:

```codeBlockLines_p187
[\
  {\
    "date": 0,\
    "successful": 0,\
    "queued": 0,\
    "rejected": 0,\
    "unhealthy": 0,\
    "memory": 0,\
    "cpu": 0,\
    "timedout": 0,\
    "totalTime": 0,\
    "meanTime": 0,\
    "maxTime": 0,\
    "minTime": 0,\
    "maxConcurrent": 0,\
    "sessionTimes": [0]\
  }\
]

```

### /metrics/all [​](https://docs.browserless.io/baas/v1/apis/metrics\#metricsall "Direct link to /metrics/all")

This route will output a similar payload, but with the total stats of all sessions.

- [Gathering metrics array from your workers](https://docs.browserless.io/baas/v1/apis/metrics#gathering-metrics-array-from-your-workers)
  - [/metrics/all](https://docs.browserless.io/baas/v1/apis/metrics#metricsall)