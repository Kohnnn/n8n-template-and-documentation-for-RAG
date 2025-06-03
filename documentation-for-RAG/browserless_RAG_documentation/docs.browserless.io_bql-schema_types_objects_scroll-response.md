---
url: "https://docs.browserless.io/bql-schema/types/objects/scroll-response"
title: "ScrollResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/scroll-response#__docusaurus_skipToContent_fallback)

On this page

Response returned after having scrolling inside the page

```codeBlockLines_p187
type ScrollResponse {
  selector: String
  time: Float
  x: Float
  y: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#fields "Direct link to Fields")

#### [`ScrollResponse.selector`](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#scrollresponseselectorstring- "Direct link to scrollresponseselectorstring-")

The CSS selector of the element on the page you want to scroll to

#### [`ScrollResponse.time`](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#scrollresponsetimefloat- "Direct link to scrollresponsetimefloat-")

The amount of time, in milliseconds, elapsed since the start of scrolling to completion

#### [`ScrollResponse.x`](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#scrollresponsexfloat- "Direct link to scrollresponsexfloat-")

The X coordinate, in pixels, to scroll to

#### [`ScrollResponse.y`](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#scrollresponseyfloat- "Direct link to scrollresponseyfloat-")

The Y coordinate, in pixels, to scroll to

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/scroll-response\#returned-by "Direct link to Returned By")

[`scroll`](https://docs.browserless.io/bql-schema/operations/mutations/scroll) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/scroll-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/scroll-response#returned-by)