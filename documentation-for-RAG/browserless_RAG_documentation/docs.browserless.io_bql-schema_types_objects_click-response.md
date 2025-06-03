---
url: "https://docs.browserless.io/bql-schema/types/objects/click-response"
title: "ClickResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/click-response#__docusaurus_skipToContent_fallback)

On this page

Response returned after having clicked on an element

```codeBlockLines_p187
type ClickResponse {
  selector: String
  time: Float
  x: Float
  y: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/click-response\#fields "Direct link to Fields")

#### [`ClickResponse.selector`](https://docs.browserless.io/bql-schema/types/objects/click-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/click-response\#clickresponseselectorstring- "Direct link to clickresponseselectorstring-")

The selector text if specified

#### [`ClickResponse.time`](https://docs.browserless.io/bql-schema/types/objects/click-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/click-response\#clickresponsetimefloat- "Direct link to clickresponsetimefloat-")

The amount of time, in milliseconds, elapsed since the start of clicking to completion

#### [`ClickResponse.x`](https://docs.browserless.io/bql-schema/types/objects/click-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/click-response\#clickresponsexfloat- "Direct link to clickresponsexfloat-")

The X coordinate of the click, in pixels, on the page

#### [`ClickResponse.y`](https://docs.browserless.io/bql-schema/types/objects/click-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/click-response\#clickresponseyfloat- "Direct link to clickresponseyfloat-")

The Y coordinate of the click, in pixels, on the page

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/click-response\#returned-by "Direct link to Returned By")

[`checkbox`](https://docs.browserless.io/bql-schema/operations/mutations/checkbox) mutation ● [`click`](https://docs.browserless.io/bql-schema/operations/mutations/click) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/click-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/click-response#returned-by)