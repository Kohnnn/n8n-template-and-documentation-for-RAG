---
url: "https://docs.browserless.io/baas/v1/apis/screenshot"
title: "/screenshot API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/screenshot#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/screenshot) or [BrowserQL](https://docs.browserless.io/browserql/start).

The screenshot API allows for simple navigation to a site and capturing a screenshot. browserless will respond with either a binary or base64 encode of a `png` or `jpg` (depending on parameters). This API exposes most of puppeteer's screenshot API through the posted JSON payload.

If you want to see all the options check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Browser%20API/post_screenshot).

## Basic Usage [​](https://docs.browserless.io/baas/v1/apis/screenshot\#basic-usage "Direct link to Basic Usage")

```codeBlockLines_p187
// JSON body
// `options` are the options available via puppeteer's Page.screenshot() method
// (see https://pptr.dev/api/puppeteer.screenshotoptions)
{
  "url": "https://example.com/",
  "options": {
    "fullPage": true,
    "type": "jpeg",
    "quality": 75
  }
}

```

**cURL request**

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

## Screenshot options [​](https://docs.browserless.io/baas/v1/apis/screenshot\#screenshot-options "Direct link to Screenshot options")

We support Puppeteer's [screenshot options](https://pptr.dev/api/puppeteer.screenshotoptions/#properties) almost in its entirety, and you can easily pass options to the JSON payload using the `options` property.

**Example**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "options": {
    "type": "jpeg",
    "clip": {
      "height": 200,
      "width": 600,
      "x": 90,
      "y": 100
    },
    "fullPage": false,
    "encoding": "binary"
  }
}

```

> We do not allow to set a `options.path` nor to return a `webp`

## Custom options [​](https://docs.browserless.io/baas/v1/apis/screenshot\#custom-options "Direct link to Custom options")

The `/screenshot` route has a few special custom options that make it more usable and configurable. We've added these options based on feedback from you in hope that it will help gather best-practices in a single place.

### `gotoOptions` [​](https://docs.browserless.io/baas/v1/apis/screenshot\#gotooptions "Direct link to gotooptions")

The `gotoOptions` is an object that's passed directly into puppeteer's `page.goto()` call so that you can specify things like alternative loaded events. See [puppeteer's goto options](https://pptr.dev/api/puppeteer.page.goto#remarks) for more information.

**cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/screenshot?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "gotoOptions": {
    "waitUntil": "networkidle2",
  }
}'

```

## Custom styling [​](https://docs.browserless.io/baas/v1/apis/screenshot\#custom-styling "Direct link to Custom styling")

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

## Custom behavior with `waitFor` [​](https://docs.browserless.io/baas/v1/apis/screenshot\#custom-behavior-with-waitfor "Direct link to custom-behavior-with-waitfor")

If you need to wait for a selector to appear in the DOM, to wait for a timeout to happen, or to execute a custom function before screenshotting, you can use the `waitFor` property in your JSON payload.

We closely follow [puppeteer's `waitFor()` method](https://github.com/puppeteer/puppeteer/blob/7b768838023bcb79051f5d34c96949ef253ad9a2/docs/api.md#pagewaitforselectororfunctionortimeout-options-args).

This property can accept one of three options:

- A valid CSS selector to wait for.
- A `number` indicating the time in milliseconds to wait.
- A function to be ran within the page's context.

**Waiting for a selector**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "waitFor": "h1"
}

```

**Waiting for a timeout**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "waitFor": 5000
}

```

**Waiting for a function**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "waitFor": "() => document.querySelector(`h1`).innerText = `Hello World!`"
}

```

- [Basic Usage](https://docs.browserless.io/baas/v1/apis/screenshot#basic-usage)
- [Screenshot options](https://docs.browserless.io/baas/v1/apis/screenshot#screenshot-options)
- [Custom options](https://docs.browserless.io/baas/v1/apis/screenshot#custom-options)
  - [`gotoOptions`](https://docs.browserless.io/baas/v1/apis/screenshot#gotooptions)
- [Custom styling](https://docs.browserless.io/baas/v1/apis/screenshot#custom-styling)
- [Custom behavior with `waitFor`](https://docs.browserless.io/baas/v1/apis/screenshot#custom-behavior-with-waitfor)