---
url: "https://docs.browserless.io/bql-schema/operations/mutations/back"
title: "back | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/back#__docusaurus_skipToContent_fallback)

On this page

Goes back in browser history, optionally accepting waitUntil and timeout arguments. Returns null if no back is possible

Example:

```codeBlockLines_p187
mutation GoBack {
  firstNav: goto(url: "https://example.com") {
    time
  }

  secondNav: goto(url: "https://browserless.com") {
    time
  }

  back(waitUntil: domContentLoaded) {
    status
  }
}

```

```codeBlockLines_p187
back(
  timeout: Float
  waitUntil: WaitUntilHistory = load
): HTTPResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/back\#arguments "Direct link to Arguments")

#### [`back.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/back\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/back\#backtimeoutfloat- "Direct link to backtimeoutfloat-")

The maximum amount of time, in milliseconds, to wait for the page to load, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`back.waitUntil`](https://docs.browserless.io/bql-schema/operations/mutations/back\#) ● [`WaitUntilHistory`](https://docs.browserless.io/bql-schema/types/enums/wait-until-history) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/back\#backwaituntilwaituntilhistory- "Direct link to backwaituntilwaituntilhistory-")

When to consider the page fully-loaded and proceed with further execution

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/back\#type "Direct link to Type")

#### [`HTTPResponse`](https://docs.browserless.io/bql-schema/types/objects/httpresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/back\#httpresponse- "Direct link to httpresponse-")

Response returned after a navigation event

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/back#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/back#type)