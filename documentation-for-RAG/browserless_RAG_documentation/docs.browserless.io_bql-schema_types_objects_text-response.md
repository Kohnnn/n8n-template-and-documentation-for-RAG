---
url: "https://docs.browserless.io/bql-schema/types/objects/text-response"
title: "TextResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/text-response#__docusaurus_skipToContent_fallback)

On this page

Text content of a page

```codeBlockLines_p187
type TextResponse {
  text: String
  time: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/text-response\#fields "Direct link to Fields")

#### [`TextResponse.text`](https://docs.browserless.io/bql-schema/types/objects/text-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/text-response\#textresponsetextstring- "Direct link to textresponsetextstring-")

The textual content of the page

#### [`TextResponse.time`](https://docs.browserless.io/bql-schema/types/objects/text-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/text-response\#textresponsetimefloat- "Direct link to textresponsetimefloat-")

The amount of time, in milliseconds, elapsed since the start of text retrieval to completion

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/text-response\#returned-by "Direct link to Returned By")

[`text`](https://docs.browserless.io/bql-schema/operations/mutations/text) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/text-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/text-response#returned-by)