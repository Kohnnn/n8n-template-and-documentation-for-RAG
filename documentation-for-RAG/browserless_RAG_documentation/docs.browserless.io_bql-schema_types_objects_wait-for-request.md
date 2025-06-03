---
url: "https://docs.browserless.io/bql-schema/types/objects/wait-for-request"
title: "WaitForRequest | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/wait-for-request#__docusaurus_skipToContent_fallback)

On this page

Response returned after a particular network request has been sent

```codeBlockLines_p187
type WaitForRequest {
  time: Float
  url: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-request\#fields "Direct link to Fields")

#### [`WaitForRequest.time`](https://docs.browserless.io/bql-schema/types/objects/wait-for-request\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-request\#waitforrequesttimefloat- "Direct link to waitforrequesttimefloat-")

The period of time elapsed, in milliseconds, waited for

#### [`WaitForRequest.url`](https://docs.browserless.io/bql-schema/types/objects/wait-for-request\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-request\#waitforrequesturlstring- "Direct link to waitforrequesturlstring-")

The URL parameter used to match the response with

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-request\#returned-by "Direct link to Returned By")

[`waitForRequest`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/wait-for-request#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/wait-for-request#returned-by)