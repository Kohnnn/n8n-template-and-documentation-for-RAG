---
url: "https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation"
title: "waitForNavigation | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation#__docusaurus_skipToContent_fallback)

On this page

Waits for a navigation even to fire, useful for clicking an element and waiting for a page load of some

Example:

```codeBlockLines_p187
mutation WaitForNavigation {
  goto(url: "https://example.com") {
    status
  }

  waitForNavigation(waitUntil: load) {
    status
  }
}

```

```codeBlockLines_p187
waitForNavigation(
  timeout: Float
  waitUntil: WaitUntilGoto = load
): HTTPResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation\#arguments "Direct link to Arguments")

#### [`waitForNavigation.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation\#waitfornavigationtimeoutfloat- "Direct link to waitfornavigationtimeoutfloat-")

The maximum amount of time, in milliseconds, to wait for the page to load, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`waitForNavigation.waitUntil`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation\#) ● [`WaitUntilGoto`](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation\#waitfornavigationwaituntilwaituntilgoto- "Direct link to waitfornavigationwaituntilwaituntilgoto-")

When to consider the page fully-loaded and proceed with further execution

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation\#type "Direct link to Type")

#### [`HTTPResponse`](https://docs.browserless.io/bql-schema/types/objects/httpresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation\#httpresponse- "Direct link to httpresponse-")

Response returned after a navigation event

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation#type)