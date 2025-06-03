---
url: "https://docs.browserless.io/bql-schema/types/objects/type-response"
title: "TypeResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/type-response#__docusaurus_skipToContent_fallback)

On this page

Response returned after having typed into an element

```codeBlockLines_p187
type TypeResponse {
  selector: String
  text: String
  time: Float
  x: Float
  y: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/type-response\#fields "Direct link to Fields")

#### [`TypeResponse.selector`](https://docs.browserless.io/bql-schema/types/objects/type-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/type-response\#typeresponseselectorstring- "Direct link to typeresponseselectorstring-")

The selector of the element you typed into

#### [`TypeResponse.text`](https://docs.browserless.io/bql-schema/types/objects/type-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/type-response\#typeresponsetextstring- "Direct link to typeresponsetextstring-")

The textual content that was typed

#### [`TypeResponse.time`](https://docs.browserless.io/bql-schema/types/objects/type-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/type-response\#typeresponsetimefloat- "Direct link to typeresponsetimefloat-")

The amount of time, in milliseconds, elapsed since the start of typing to completion

#### [`TypeResponse.x`](https://docs.browserless.io/bql-schema/types/objects/type-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/type-response\#typeresponsexfloat- "Direct link to typeresponsexfloat-")

The X coordinate of the element, in pixels, on the page

#### [`TypeResponse.y`](https://docs.browserless.io/bql-schema/types/objects/type-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/type-response\#typeresponseyfloat- "Direct link to typeresponseyfloat-")

The Y coordinate of the element, in pixels, on the page

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/type-response\#returned-by "Direct link to Returned By")

[`type`](https://docs.browserless.io/bql-schema/operations/mutations/type) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/type-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/type-response#returned-by)