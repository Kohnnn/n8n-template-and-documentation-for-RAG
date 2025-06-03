---
url: "https://docs.browserless.io/bql-schema/operations/mutations/preferences"
title: "preferences | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/preferences#__docusaurus_skipToContent_fallback)

On this page

Sets configuration for the entirety of the session, replacing defaults like the 30 second timeout default

Example:

```codeBlockLines_p187
mutation Preferences {
  preferences(timeout: 10000) {
    timeout
  }
}

```

```codeBlockLines_p187
preferences(
  timeout: Float = 30000
): DefaultResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/preferences\#arguments "Direct link to Arguments")

#### [`preferences.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/preferences\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/preferences\#preferencestimeoutfloat- "Direct link to preferencestimeoutfloat-")

Sets a default timeout for all methods, including 'goto', 'type', 'wait', etc. Default timeout is 30 seconds, or 30000.

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/preferences\#type "Direct link to Type")

#### [`DefaultResponse`](https://docs.browserless.io/bql-schema/types/objects/default-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/preferences\#defaultresponse- "Direct link to defaultresponse-")

Default response for all methods

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/preferences#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/preferences#type)