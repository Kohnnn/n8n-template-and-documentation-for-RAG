---
url: "https://docs.browserless.io/baas/v1/options/api-get"
title: "Using /get API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/options/api-get#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

In recent version of browserless we've enabled special /GET handlers for our APIs. This is handy for cases where you need to directly call our services from a cache-layer like a CDN.

> Please do not call the hosted service from the browser as it will reveal your secret token!

In order to use this feature on the hosted service, you'll need to restart or update your worker(s) to do so. Simply click the "Restart Workers" button, and toggle the "Enable API GET" switch. Once restart you should be able to issue GET calls.

In docker, you'll need to set the `ENABLE_API_GET` environment variable to `true`.

## Making the request [​](https://docs.browserless.io/baas/v1/options/api-get\#making-the-request "Direct link to Making the request")

Similar to our POST APIs (/content, /screenshot, /pdf, /scrape and /stats), you'll need to send a JSON payload to browserless. However, since we're issuing a GET call instead of a POST, you'll need to stringify your JSON body and append it to the URL of the call as a query-string `body` parameter.

Here's a simple example of doing a screenshot with the example.com website.

**Before (POST)**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/screenshot?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "options": {
    "fullPage": true,
    "type": "jpeg",
    "quality": 75
  }
}'

```

**After (GET)**

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/screenshot?token=MY_API_TOKEN&body=%7B%22url%22%3A%22https%3A%2F%2Fexample.com%2F%22%2C%22options%22%3A%7B%22fullPage%22%3Atrue%2C%22type%22%3A%22jpeg%22%2C%22quality%22%3A75%7D%7D

```

You'll note that we've both stringified the JSON, and encoded it for URL transmission. Because of how much space this takes, it's generally recommended to use the POST version, however certain use-cases might benefit from this GET feature.

- [Making the request](https://docs.browserless.io/baas/v1/options/api-get#making-the-request)