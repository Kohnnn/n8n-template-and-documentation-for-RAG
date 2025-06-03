---
url: "https://docs.browserless.io/bql-schema/types/objects/evaluate-response"
title: "EvaluateResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/evaluate-response#__docusaurus_skipToContent_fallback)

On this page

Response returned after evaluating a script

```codeBlockLines_p187
type EvaluateResponse {
  time: Float
  value: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/evaluate-response\#fields "Direct link to Fields")

#### [`EvaluateResponse.time`](https://docs.browserless.io/bql-schema/types/objects/evaluate-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/evaluate-response\#evaluateresponsetimefloat- "Direct link to evaluateresponsetimefloat-")

The time it took for the evaluate call to happen

#### [`EvaluateResponse.value`](https://docs.browserless.io/bql-schema/types/objects/evaluate-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/evaluate-response\#evaluateresponsevaluestring- "Direct link to evaluateresponsevaluestring-")

The returned value of the script, if any

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/evaluate-response\#returned-by "Direct link to Returned By")

[`evaluate`](https://docs.browserless.io/bql-schema/operations/mutations/evaluate) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/evaluate-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/evaluate-response#returned-by)