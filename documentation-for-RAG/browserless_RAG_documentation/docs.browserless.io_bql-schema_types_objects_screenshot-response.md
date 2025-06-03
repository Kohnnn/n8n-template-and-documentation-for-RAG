---
url: "https://docs.browserless.io/bql-schema/types/objects/screenshot-response"
title: "ScreenshotResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/screenshot-response#__docusaurus_skipToContent_fallback)

On this page

The response returned after generating a Screenshot

```codeBlockLines_p187
type ScreenshotResponse {
  base64: String
  format: String
  time: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/screenshot-response\#fields "Direct link to Fields")

#### [`ScreenshotResponse.base64`](https://docs.browserless.io/bql-schema/types/objects/screenshot-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/screenshot-response\#screenshotresponsebase64string- "Direct link to screenshotresponsebase64string-")

The base64 encoded image of the screenshot

#### [`ScreenshotResponse.format`](https://docs.browserless.io/bql-schema/types/objects/screenshot-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/screenshot-response\#screenshotresponseformatstring- "Direct link to screenshotresponseformatstring-")

The format of the screenshot

#### [`ScreenshotResponse.time`](https://docs.browserless.io/bql-schema/types/objects/screenshot-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/screenshot-response\#screenshotresponsetimefloat- "Direct link to screenshotresponsetimefloat-")

The time it took to take the screenshot

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/screenshot-response\#returned-by "Direct link to Returned By")

[`screenshot`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/screenshot-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/screenshot-response#returned-by)