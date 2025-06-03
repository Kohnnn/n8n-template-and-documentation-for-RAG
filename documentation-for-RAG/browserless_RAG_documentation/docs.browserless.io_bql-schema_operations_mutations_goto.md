---
url: "https://docs.browserless.io/bql-schema/operations/mutations/goto"
title: "goto | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/goto#__docusaurus_skipToContent_fallback)

On this page

Navigates to a URL with an optional waitUntil parameter and timeout parameter

Example:

```codeBlockLines_p187
mutation Goto {
  goto(url: "https://example.com") {
    status
  }
}

```

```codeBlockLines_p187
goto(
  url: String!
  timeout: Float
  waitUntil: WaitUntilGoto = load
): HTTPResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/goto\#arguments "Direct link to Arguments")

#### [`goto.url`](https://docs.browserless.io/bql-schema/operations/mutations/goto\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/goto\#gotourlstring-- "Direct link to gotourlstring--")

The fully-qualified URL of the page you'd like to navigate to

#### [`goto.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/goto\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/goto\#gototimeoutfloat- "Direct link to gototimeoutfloat-")

The maximum amount of time, in milliseconds, to wait for the page to load, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`goto.waitUntil`](https://docs.browserless.io/bql-schema/operations/mutations/goto\#) ● [`WaitUntilGoto`](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/goto\#gotowaituntilwaituntilgoto- "Direct link to gotowaituntilwaituntilgoto-")

When to consider the page fully-loaded and proceed with further execution

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/goto\#type "Direct link to Type")

#### [`HTTPResponse`](https://docs.browserless.io/bql-schema/types/objects/httpresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/goto\#httpresponse- "Direct link to httpresponse-")

Response returned after a navigation event

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/goto#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/goto#type)