---
url: "https://docs.browserless.io/baas/v1/apis/pdf"
title: "/pdf API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/pdf#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/pdf) or [BrowserQL](https://docs.browserless.io/browserql/start).

The pdf API allows for simple navigation to a site and capturing a pdf. browserless will respond with a `Content-Type` of `application/pdf`, and a Buffer of the pdf file. Similar to screenshots, this also exposes puppeteer's `pdf` options via an `options` property in the JSON body for granular control.

If you want to see all the options check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Browser%20API/post_pdf).

> This route requires either a `url` or `html` property in the JSON body. When `html` is present browserless will render the HTML for you and capture the PDF

## Basic Usage [​](https://docs.browserless.io/baas/v1/apis/pdf\#basic-usage "Direct link to Basic Usage")

```codeBlockLines_p187
// JSON body
// `options` are the options available via puppeteer's Page.pdf() method
// (see https://pptr.dev/api/puppeteer.pdfoptions)
{
  "url": "https://example.com/",
  "options": {
    "displayHeaderFooter": true,
    "printBackground": false,
    "format": "A0"
  }
}

```

**cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/pdf?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "options": {
    "displayHeaderFooter": true,
    "printBackground": false,
    "format": "A0"
  }
}'

```

> We do not allow to set a `options.path`

## Custom options [​](https://docs.browserless.io/baas/v1/apis/pdf\#custom-options "Direct link to Custom options")

The `/pdf` route has a few special custom options that make it more usable and configurable. We've added these options based on feedback from you in hope that it will help gather best-practices in a single place.

### `gotoOptions` [​](https://docs.browserless.io/baas/v1/apis/pdf\#gotooptions "Direct link to gotooptions")

The `gotoOptions` is an object that's passed directly into puppeteer's `page.goto()` call so that you can specify things like alternative loaded events. See [puppeteer's goto options](https://pptr.dev/api/puppeteer.page.goto#remarks) for more information.

**Example cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/pdf?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "gotoOptions": {
    "waitUntil": "networkidle2",
  },
  "options": {
    "displayHeaderFooter": true,
    "printBackground": false,
    "format": "A0"
  }
}'

```

## Custom styling [​](https://docs.browserless.io/baas/v1/apis/pdf\#custom-styling "Direct link to Custom styling")

If you need to inject custom CSS code to the page, you can use the `addStyleTag` property.

This property takes an array of objects, each with either a `content` property with valid CSS code, or a `url` property that loads the stylesheet from the web.

**Example**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "gotoOptions": {
    "waitUntil": "networkidle2"
  },
  "addStyleTag": [\
    {\
      "content": "body { height: 100vh;  background: linear-gradient(45deg, #da5a44, #a32784);}"\
    },\
    {\
      "url": "https://interactive-examples.mdn.mozilla.net/live-examples/css-examples/text-decoration/text-decoration-color.css"\
    }\
  ]
}

```

## safeMode [​](https://docs.browserless.io/baas/v1/apis/pdf\#safemode "Direct link to safeMode")

Because longer pages can crash trigger a "Page Crashed!" error when doing a `page.pdf` invocation, we've implemented a "safe" way to generate PDF's of bigger websites. When set to `true`, `safeMode` will:

- Capture PDF's _one_ page at a time in-memory.
- Once all pages are in memory we connect them together.
- Compress the PDF so it's more efficiently transported over the network.
- Return the resulting PDF as a binary via `application/pdf`.

> Please note that when using `safeMode` that it will likely take a while longer to process the request, and the resulting PDF file may be larger.

**Example cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/pdf?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "safeMode": true,
  "options": {
    "displayHeaderFooter": true,
    "printBackground": false,
    "format": "A0"
  }
}'

```

- [Basic Usage](https://docs.browserless.io/baas/v1/apis/pdf#basic-usage)
- [Custom options](https://docs.browserless.io/baas/v1/apis/pdf#custom-options)
  - [`gotoOptions`](https://docs.browserless.io/baas/v1/apis/pdf#gotooptions)
- [Custom styling](https://docs.browserless.io/baas/v1/apis/pdf#custom-styling)
- [safeMode](https://docs.browserless.io/baas/v1/apis/pdf#safemode)