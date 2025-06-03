---
url: "https://docs.browserless.io/bql-schema/types/objects/httpresponse"
title: "HTTPResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/httpresponse#__docusaurus_skipToContent_fallback)

On this page

Response returned after a navigation event

```codeBlockLines_p187
type HTTPResponse {
  status: Int
  time: Float
  text: String
  url: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#fields "Direct link to Fields")

#### [`HTTPResponse.status`](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#) ● [`Int`](https://docs.browserless.io/bql-schema/types/scalars/int) scalar [​](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#httpresponsestatusint- "Direct link to httpresponsestatusint-")

The status code response of the initial page-load

#### [`HTTPResponse.time`](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#httpresponsetimefloat- "Direct link to httpresponsetimefloat-")

The amount of time, in milliseconds, elapsed since the start of navigation to completion

#### [`HTTPResponse.text`](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#httpresponsetextstring- "Direct link to httpresponsetextstring-")

The status text of the response from the initial page-load. Generally 'ok'

#### [`HTTPResponse.url`](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#httpresponseurlstring- "Direct link to httpresponseurlstring-")

The final URL of the page after any potential redirects or URL rewrites

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/httpresponse\#returned-by "Direct link to Returned By")

[`back`](https://docs.browserless.io/bql-schema/operations/mutations/back) mutation ● [`content`](https://docs.browserless.io/bql-schema/operations/mutations/content) mutation ● [`forward`](https://docs.browserless.io/bql-schema/operations/mutations/forward) mutation ● [`goto`](https://docs.browserless.io/bql-schema/operations/mutations/goto) mutation ● [`reload`](https://docs.browserless.io/bql-schema/operations/mutations/reload) mutation ● [`waitForNavigation`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/httpresponse#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/httpresponse#returned-by)