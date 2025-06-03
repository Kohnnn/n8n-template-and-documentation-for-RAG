---
url: "https://docs.browserless.io/bql-schema/operations/mutations/reconnect"
title: "reconnect | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/reconnect#__docusaurus_skipToContent_fallback)

On this page

Returns a payload with reconnection information in order to reconnect back to the same browser session

Example:

```codeBlockLines_p187
mutation Reconnect {
  goto(url: "https://example.com") {
    status
  }

  reconnect(timeout: 30000) {
    browserQLEndpoint
    browserWSEndpoint
    devtoolsFrontendUrl
    webSocketDebuggerUrl
  }
}

```

```codeBlockLines_p187
reconnect(
  timeout: Float = 30000
): ReconnectionResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/reconnect\#arguments "Direct link to Arguments")

#### [`reconnect.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/reconnect\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/reconnect\#reconnecttimeoutfloat- "Direct link to reconnecttimeoutfloat-")

The amount of time, in milliseconds, to leave the browser open without a connection before it is manually terminated. Defaults to 30 seconds

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/reconnect\#type "Direct link to Type")

#### [`ReconnectionResponse`](https://docs.browserless.io/bql-schema/types/objects/reconnection-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/reconnect\#reconnectionresponse- "Direct link to reconnectionresponse-")

The response received after attempting to reconnect a BrowserQL session

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/reconnect#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/reconnect#type)