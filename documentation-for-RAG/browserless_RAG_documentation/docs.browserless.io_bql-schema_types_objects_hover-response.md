---
url: "https://docs.browserless.io/bql-schema/types/objects/hover-response"
title: "HoverResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/hover-response#__docusaurus_skipToContent_fallback)

On this page

Response returned after having hovered over an element

```codeBlockLines_p187
type HoverResponse {
  selector: String
  time: Float
  x: Float
  y: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/hover-response\#fields "Direct link to Fields")

#### [`HoverResponse.selector`](https://docs.browserless.io/bql-schema/types/objects/hover-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/hover-response\#hoverresponseselectorstring- "Direct link to hoverresponseselectorstring-")

The selector text

#### [`HoverResponse.time`](https://docs.browserless.io/bql-schema/types/objects/hover-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/hover-response\#hoverresponsetimefloat- "Direct link to hoverresponsetimefloat-")

The amount of time, in milliseconds, elapsed since the start to completion

#### [`HoverResponse.x`](https://docs.browserless.io/bql-schema/types/objects/hover-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/hover-response\#hoverresponsexfloat- "Direct link to hoverresponsexfloat-")

The X coordinate in pixels, on the page

#### [`HoverResponse.y`](https://docs.browserless.io/bql-schema/types/objects/hover-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/hover-response\#hoverresponseyfloat- "Direct link to hoverresponseyfloat-")

The Y coordinate in pixels, on the page

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/hover-response\#returned-by "Direct link to Returned By")

[`hover`](https://docs.browserless.io/bql-schema/operations/mutations/hover) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/hover-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/hover-response#returned-by)