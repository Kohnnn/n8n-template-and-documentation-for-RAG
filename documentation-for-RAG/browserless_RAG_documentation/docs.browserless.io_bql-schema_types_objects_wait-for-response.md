---
url: "https://docs.browserless.io/bql-schema/types/objects/wait-for-response"
title: "WaitForResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/wait-for-response#__docusaurus_skipToContent_fallback)

On this page

Response returned after a particular network response has been received

```codeBlockLines_p187
type WaitForResponse {
  time: Float
  status: Int
  url: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-response\#fields "Direct link to Fields")

#### [`WaitForResponse.time`](https://docs.browserless.io/bql-schema/types/objects/wait-for-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-response\#waitforresponsetimefloat- "Direct link to waitforresponsetimefloat-")

The period of time elapsed, in milliseconds, waited for

#### [`WaitForResponse.status`](https://docs.browserless.io/bql-schema/types/objects/wait-for-response\#) ● [`Int`](https://docs.browserless.io/bql-schema/types/scalars/int) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-response\#waitforresponsestatusint- "Direct link to waitforresponsestatusint-")

The status code response of the response

#### [`WaitForResponse.url`](https://docs.browserless.io/bql-schema/types/objects/wait-for-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-response\#waitforresponseurlstring- "Direct link to waitforresponseurlstring-")

The URL parameter used to match the response with

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-response\#returned-by "Direct link to Returned By")

[`waitForResponse`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/wait-for-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/wait-for-response#returned-by)