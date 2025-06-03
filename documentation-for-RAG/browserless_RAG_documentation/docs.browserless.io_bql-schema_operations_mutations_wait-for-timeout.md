---
url: "https://docs.browserless.io/bql-schema/operations/mutations/wait-for-timeout"
title: "waitForTimeout | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-timeout#__docusaurus_skipToContent_fallback)

On this page

Wait for a period of time, defined in milliseconds

Example:

```codeBlockLines_p187
mutation WaitForTimeout {
  waitForTimeout(time: 1000) {
    time
  }
}

```

```codeBlockLines_p187
waitForTimeout(
  time: Float!
): WaitForTimeout

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-timeout\#arguments "Direct link to Arguments")

#### [`waitForTimeout.time`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-timeout\#) ● [`Float!`](https://docs.browserless.io/bql-schema/types/scalars/float) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-timeout\#waitfortimeouttimefloat-- "Direct link to waitfortimeouttimefloat--")

The amount of time to wait for, in milliseconds

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-timeout\#type "Direct link to Type")

#### [`WaitForTimeout`](https://docs.browserless.io/bql-schema/types/objects/wait-for-timeout) object [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-timeout\#waitfortimeout- "Direct link to waitfortimeout-")

Response returned after having waited for a selector to appear in the DOM

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-timeout#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-timeout#type)