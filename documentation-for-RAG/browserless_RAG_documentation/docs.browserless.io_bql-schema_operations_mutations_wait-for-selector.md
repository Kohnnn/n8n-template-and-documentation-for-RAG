---
url: "https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector"
title: "waitForSelector | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector#__docusaurus_skipToContent_fallback)

On this page

Waits for a given selector to be present in the DOM, with optional visibility

Example:

```codeBlockLines_p187
mutation WaitForSelector {
  goto(url: "https://example.com") {
    status
  }

  waitForSelector(selector: "h1") {
    time
  }
}

```

```codeBlockLines_p187
waitForSelector(
  selector: String!
  timeout: Float
  visible: Boolean = false
): WaitForSelector

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector\#arguments "Direct link to Arguments")

#### [`waitForSelector.selector`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector\#waitforselectorselectorstring-- "Direct link to waitforselectorselectorstring--")

The selector to wait for until present in the DOM

#### [`waitForSelector.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector\#waitforselectortimeoutfloat- "Direct link to waitforselectortimeoutfloat-")

When waiting for a selector applies a timeout to wait for in milliseconds, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`waitForSelector.visible`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector\#waitforselectorvisibleboolean- "Direct link to waitforselectorvisibleboolean-")

Whether or not to consider the element as present only if it's visible

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector\#type "Direct link to Type")

#### [`WaitForSelector`](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector) object [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector\#waitforselector- "Direct link to waitforselector-")

Response returned after a particular selector has been found in the DOM

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector#type)