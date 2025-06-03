---
url: "https://docs.browserless.io/bql-schema/types/objects/verify-response"
title: "VerifyResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/verify-response#__docusaurus_skipToContent_fallback)

On this page

Response returned after a verification method has been bypassed

```codeBlockLines_p187
type VerifyResponse {
  found: Boolean
  solved: Boolean
  time: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/verify-response\#fields "Direct link to Fields")

#### [`VerifyResponse.found`](https://docs.browserless.io/bql-schema/types/objects/verify-response\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/objects/verify-response\#verifyresponsefoundboolean- "Direct link to verifyresponsefoundboolean-")

If a verification was found or not

#### [`VerifyResponse.solved`](https://docs.browserless.io/bql-schema/types/objects/verify-response\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/objects/verify-response\#verifyresponsesolvedboolean- "Direct link to verifyresponsesolvedboolean-")

If a verification was found, whether or not it was clicked

#### [`VerifyResponse.time`](https://docs.browserless.io/bql-schema/types/objects/verify-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/verify-response\#verifyresponsetimefloat- "Direct link to verifyresponsetimefloat-")

The total time it took to find, and click, the verification

- [Fields](https://docs.browserless.io/bql-schema/types/objects/verify-response#fields)