---
url: "https://docs.browserless.io/bql-schema/types/objects/select-response"
title: "SelectResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/select-response#__docusaurus_skipToContent_fallback)

On this page

The response returned after selecting a value from a dropdown or multiple select element

```codeBlockLines_p187
type SelectResponse {
  selector: String
  time: Float
  value: StringOrArray
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/select-response\#fields "Direct link to Fields")

#### [`SelectResponse.selector`](https://docs.browserless.io/bql-schema/types/objects/select-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/select-response\#selectresponseselectorstring- "Direct link to selectresponseselectorstring-")

The selector of the element you selected from

#### [`SelectResponse.time`](https://docs.browserless.io/bql-schema/types/objects/select-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/select-response\#selectresponsetimefloat- "Direct link to selectresponsetimefloat-")

The amount of time, in milliseconds, elapsed since the start of selecting to completion

#### [`SelectResponse.value`](https://docs.browserless.io/bql-schema/types/objects/select-response\#) ● [`StringOrArray`](https://docs.browserless.io/bql-schema/types/scalars/string-or-array) scalar [​](https://docs.browserless.io/bql-schema/types/objects/select-response\#selectresponsevaluestringorarray- "Direct link to selectresponsevaluestringorarray-")

The value or values you selected from the select element

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/select-response\#returned-by "Direct link to Returned By")

[`select`](https://docs.browserless.io/bql-schema/operations/mutations/select) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/select-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/select-response#returned-by)