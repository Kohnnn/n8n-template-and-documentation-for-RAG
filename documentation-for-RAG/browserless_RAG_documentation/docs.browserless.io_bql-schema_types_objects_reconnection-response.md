---
url: "https://docs.browserless.io/bql-schema/types/objects/reconnection-response"
title: "ReconnectionResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/reconnection-response#__docusaurus_skipToContent_fallback)

On this page

The response received after attempting to reconnect a BrowserQL session

```codeBlockLines_p187
type ReconnectionResponse {
  browserQLEndpoint: String
  browserWSEndpoint: String
  devtoolsFrontendUrl: String
  webSocketDebuggerUrl: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#fields "Direct link to Fields")

#### [`ReconnectionResponse.browserQLEndpoint`](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#reconnectionresponsebrowserqlendpointstring- "Direct link to reconnectionresponsebrowserqlendpointstring-")

The fully-qualified URL to reconnect future BrowserQL sessions, eg: [https://chrome.browserless.io/bql/$id](https://chrome.browserless.io/bql/$id). Please note that token information is not returned by this API and might be required

#### [`ReconnectionResponse.browserWSEndpoint`](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#reconnectionresponsebrowserwsendpointstring- "Direct link to reconnectionresponsebrowserwsendpointstring-")

The fully-qualified URL of the browserWSEndpoint which can be used with other libraries like playwright or puppeteer. Please note that token information is not returned by this API and might be required

#### [`ReconnectionResponse.devtoolsFrontendUrl`](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#reconnectionresponsedevtoolsfrontendurlstring- "Direct link to reconnectionresponsedevtoolsfrontendurlstring-")

The fully-qualified URL of the devtools resources for loading Chrome's developer tools remotely

#### [`ReconnectionResponse.webSocketDebuggerUrl`](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#reconnectionresponsewebsocketdebuggerurlstring- "Direct link to reconnectionresponsewebsocketdebuggerurlstring-")

The underlying page's webSocketDebuggerUrl, useful for hooking libraries that operate on a page and not a browser object

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/reconnection-response\#returned-by "Direct link to Returned By")

[`reconnect`](https://docs.browserless.io/bql-schema/operations/mutations/reconnect) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/reconnection-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/reconnection-response#returned-by)