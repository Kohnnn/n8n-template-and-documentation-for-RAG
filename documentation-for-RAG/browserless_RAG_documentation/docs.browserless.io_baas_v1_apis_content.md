---
url: "https://docs.browserless.io/baas/v1/apis/content"
title: "/content API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/content#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/content) or [BrowserQL](https://docs.browserless.io/browserql/start).

The content API allows for simple navigation to a site and capturing the page's content (including the `<head>` section). browserless will respond with a `Content-Type` of `text/html`, and string of the site's HTML. This is useful for capturing the content of a page that has a lot of JavaScript or other interactivity.

If you want to see all the options check out the [schema for it here on GitHub](https://github.com/browserless/browserless/blob/v1/src/schemas.ts#L177-L192) or check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Browser%20API/post_content).

## Capture the content of example.com [​](https://docs.browserless.io/baas/v1/apis/content\#capture-the-content-of-examplecom "Direct link to Capture the content of example.com")

**JSON payload**

```codeBlockLines_p187
{
  "url": "https://example.com/"
}

```

**cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/content?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '
{
  "url": "https://example.com/"
}'

```

- [Capture the content of example.com](https://docs.browserless.io/baas/v1/apis/content#capture-the-content-of-examplecom)