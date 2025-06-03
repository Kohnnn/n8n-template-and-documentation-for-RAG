---
url: "https://docs.browserless.io/bql-schema/types/inputs/request-input"
title: "RequestInput | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/inputs/request-input#__docusaurus_skipToContent_fallback)

On this page

The specific request to perform a conditional action on

```codeBlockLines_p187
input RequestInput {
  method: Method
  url: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/inputs/request-input\#fields "Direct link to Fields")

#### [`RequestInput.method`](https://docs.browserless.io/bql-schema/types/inputs/request-input\#) ● [`Method`](https://docs.browserless.io/bql-schema/types/enums/method) enum [​](https://docs.browserless.io/bql-schema/types/inputs/request-input\#requestinputmethodmethod- "Direct link to requestinputmethodmethod-")

The HTTP Method of the request

#### [`RequestInput.url`](https://docs.browserless.io/bql-schema/types/inputs/request-input\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/request-input\#requestinputurlstring- "Direct link to requestinputurlstring-")

The pattern of the request URL to wait for, using glob-style pattern-matching

### Member Of [​](https://docs.browserless.io/bql-schema/types/inputs/request-input\#member-of "Direct link to Member Of")

[`if`](https://docs.browserless.io/bql-schema/operations/mutations/if) mutation ● [`ifnot`](https://docs.browserless.io/bql-schema/operations/mutations/ifnot) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/inputs/request-input#fields)
- [Member Of](https://docs.browserless.io/bql-schema/types/inputs/request-input#member-of)