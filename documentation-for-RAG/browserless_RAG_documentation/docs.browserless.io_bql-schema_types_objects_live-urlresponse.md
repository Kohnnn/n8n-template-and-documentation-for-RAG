---
url: "https://docs.browserless.io/bql-schema/types/objects/live-urlresponse"
title: "LiveURLResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse#__docusaurus_skipToContent_fallback)

On this page

The response from the Live-URL query

```codeBlockLines_p187
type LiveURLResponse {
  liveURLId: String
  liveURL: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse\#fields "Direct link to Fields")

#### [`LiveURLResponse.liveURLId`](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse\#liveurlresponseliveurlidstring- "Direct link to liveurlresponseliveurlidstring-")

A unique ID representing the session. Useful for storing and associations in other APIs

#### [`LiveURLResponse.liveURL`](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse\#liveurlresponseliveurlstring- "Direct link to liveurlresponseliveurlstring-")

The fully-qualified URL to share with the end-user to allow them to live-stream the browser

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse\#returned-by "Direct link to Returned By")

[`liveURL`](https://docs.browserless.io/bql-schema/operations/mutations/live-url) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse#returned-by)