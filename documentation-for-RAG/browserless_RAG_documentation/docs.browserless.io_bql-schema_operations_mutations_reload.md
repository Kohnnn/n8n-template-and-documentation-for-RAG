---
url: "https://docs.browserless.io/bql-schema/operations/mutations/reload"
title: "reload | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/reload#__docusaurus_skipToContent_fallback)

On this page

Reloads the given page with an optional waitUntil parameter and timeout parameter

Example:

```codeBlockLines_p187
mutation Reload {
  goto(url: "https://example.com") {
    status
  }
  reload(timeout: 10000) {
    status
  }
}

```

```codeBlockLines_p187
reload(
  timeout: Float
  waitUntil: WaitUntilHistory = load
): HTTPResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/reload\#arguments "Direct link to Arguments")

#### [`reload.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/reload\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/reload\#reloadtimeoutfloat- "Direct link to reloadtimeoutfloat-")

The maximum amount of time, in milliseconds, to wait for the page to load, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`reload.waitUntil`](https://docs.browserless.io/bql-schema/operations/mutations/reload\#) ● [`WaitUntilHistory`](https://docs.browserless.io/bql-schema/types/enums/wait-until-history) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/reload\#reloadwaituntilwaituntilhistory- "Direct link to reloadwaituntilwaituntilhistory-")

When to consider the page fully-loaded and proceed with further execution

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/reload\#type "Direct link to Type")

#### [`HTTPResponse`](https://docs.browserless.io/bql-schema/types/objects/httpresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/reload\#httpresponse- "Direct link to httpresponse-")

Response returned after a navigation event

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/reload#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/reload#type)