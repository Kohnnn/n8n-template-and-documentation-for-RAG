---
url: "https://docs.browserless.io/bql-schema/types/objects/java-script-response"
title: "JavaScriptResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/java-script-response#__docusaurus_skipToContent_fallback)

On this page

The response returned after enabling or disabling JavaScript on the page

```codeBlockLines_p187
type JavaScriptResponse {
  enabled: Boolean
  time: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/java-script-response\#fields "Direct link to Fields")

#### [`JavaScriptResponse.enabled`](https://docs.browserless.io/bql-schema/types/objects/java-script-response\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/objects/java-script-response\#javascriptresponseenabledboolean- "Direct link to javascriptresponseenabledboolean-")

Whether or not JavaScript is enabled on the page

#### [`JavaScriptResponse.time`](https://docs.browserless.io/bql-schema/types/objects/java-script-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/java-script-response\#javascriptresponsetimefloat- "Direct link to javascriptresponsetimefloat-")

The time it took to perform this action

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/java-script-response\#returned-by "Direct link to Returned By")

[`javaScriptEnabled`](https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/java-script-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/java-script-response#returned-by)