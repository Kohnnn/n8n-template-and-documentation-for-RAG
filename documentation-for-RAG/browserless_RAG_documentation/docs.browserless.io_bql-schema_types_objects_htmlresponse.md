---
url: "https://docs.browserless.io/bql-schema/types/objects/htmlresponse"
title: "HTMLResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/htmlresponse#__docusaurus_skipToContent_fallback)

On this page

HTML content of a page

```codeBlockLines_p187
type HTMLResponse {
  html: String
  time: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/htmlresponse\#fields "Direct link to Fields")

#### [`HTMLResponse.html`](https://docs.browserless.io/bql-schema/types/objects/htmlresponse\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/htmlresponse\#htmlresponsehtmlstring- "Direct link to htmlresponsehtmlstring-")

The content of the page's HTML

#### [`HTMLResponse.time`](https://docs.browserless.io/bql-schema/types/objects/htmlresponse\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/htmlresponse\#htmlresponsetimefloat- "Direct link to htmlresponsetimefloat-")

The amount of time, in milliseconds, elapsed since the start of content retrieval to completion

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/htmlresponse\#returned-by "Direct link to Returned By")

[`html`](https://docs.browserless.io/bql-schema/operations/mutations/html) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/htmlresponse#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/htmlresponse#returned-by)