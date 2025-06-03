---
url: "https://docs.browserless.io/bql-schema/types/inputs/response-input"
title: "ResponseInput | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/inputs/response-input#__docusaurus_skipToContent_fallback)

On this page

The specific response to perform a conditional action on

```codeBlockLines_p187
input ResponseInput {
  statuses: [Int]
  codes: [Int] @deprecated
  url: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/inputs/response-input\#fields "Direct link to Fields")

#### [`ResponseInput.statuses`](https://docs.browserless.io/bql-schema/types/inputs/response-input\#) ● [`[Int]`](https://docs.browserless.io/bql-schema/types/scalars/int) listscalar [​](https://docs.browserless.io/bql-schema/types/inputs/response-input\#responseinputstatusesint-- "Direct link to responseinputstatusesint--")

The HTTP Response code(s) of the URL to wait for. Can be a single HTTP code or a list of desired codes

#### [`ResponseInput.codes`](https://docs.browserless.io/bql-schema/types/inputs/response-input\#) ● [`[Int]`](https://docs.browserless.io/bql-schema/types/scalars/int) deprecatedlistscalar [​](https://docs.browserless.io/bql-schema/types/inputs/response-input\#responseinputcodesint--- "Direct link to responseinputcodesint---")

DEPRECATED

Use `statuses` field instead as it is more consistent in BrowserQL.

The HTTP Response code(s) of the URL to wait for. Can be a single HTTP code or a list of desired codes

#### [`ResponseInput.url`](https://docs.browserless.io/bql-schema/types/inputs/response-input\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/response-input\#responseinputurlstring- "Direct link to responseinputurlstring-")

The pattern of the response URL to wait for, using glob-style pattern-matching

### Member Of [​](https://docs.browserless.io/bql-schema/types/inputs/response-input\#member-of "Direct link to Member Of")

[`if`](https://docs.browserless.io/bql-schema/operations/mutations/if) mutation ● [`ifnot`](https://docs.browserless.io/bql-schema/operations/mutations/ifnot) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/inputs/response-input#fields)
- [Member Of](https://docs.browserless.io/bql-schema/types/inputs/response-input#member-of)