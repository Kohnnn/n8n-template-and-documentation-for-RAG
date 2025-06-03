---
url: "https://docs.browserless.io/bql-schema/operations/mutations/forward"
title: "forward | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/forward#__docusaurus_skipToContent_fallback)

On this page

Goes forward in browser history, optionally accepting waitUntil and timeout arguments. Returns null if no forward is possible

Example:

```codeBlockLines_p187
mutation GoForward {
  firstNav: goto(url: "https://example.com", waitUntil: load) {
    time
  }

  secondNav: goto(url: "https://browserless.io", waitUntil: load) {
    time
  }

  back(waitUntil: domContentLoaded) {
    status
  }

  forward(waitUntil: domContentLoaded) {
    status
  }
}

```

```codeBlockLines_p187
forward(
  timeout: Float
  waitUntil: WaitUntilHistory = load
): HTTPResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/forward\#arguments "Direct link to Arguments")

#### [`forward.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/forward\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/forward\#forwardtimeoutfloat- "Direct link to forwardtimeoutfloat-")

The maximum amount of time, in milliseconds, to wait for the page to load, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`forward.waitUntil`](https://docs.browserless.io/bql-schema/operations/mutations/forward\#) ● [`WaitUntilHistory`](https://docs.browserless.io/bql-schema/types/enums/wait-until-history) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/forward\#forwardwaituntilwaituntilhistory- "Direct link to forwardwaituntilwaituntilhistory-")

When to consider the page fully-loaded and proceed with further execution

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/forward\#type "Direct link to Type")

#### [`HTTPResponse`](https://docs.browserless.io/bql-schema/types/objects/httpresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/forward\#httpresponse- "Direct link to httpresponse-")

Response returned after a navigation event

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/forward#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/forward#type)