---
url: "https://docs.browserless.io/baas/v1/hosted-service/how-it-works"
title: "How it works | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/hosted-service/how-it-works#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/session-management/reconnect) or [BrowserQL](https://docs.browserless.io/browserql/start).

warning

Libraries that only allow a `host` and `port` option are not well supported by the Browserless service since you cannot properly send in API tokens. If you're looking to integrate into the hosted service, read more about our REST API's and the `/function` [endpoint here](https://www.browserless.io/blog/2018/05/26/browserless-functions/#browserless-functions).

Browserless works almost identically to how most libraries and web-drivers work when ran locally. There's no additional software you need to install on your production machines or complicated setup steps. As a matter of fact, the only thing you really need to when using the Browserless service is merely change where your code references Chrome.

Browserless runs Chrome in a cloud environment, and exposes most of the [Chrome remote protocol](https://chromedevtools.github.io/devtools-protocol/) to you. On top of exposing these commands, it also:

- Isolates your session from all others.
- Can run concurrent requests without interfering with others.
- Cleans up sessions after 30 seconds.
- Starts a clean copy of Chrome for each session.
- Restarts automatically if anything crashes.
- Queues requests if thresholds are met.

## How sessions work [​](https://docs.browserless.io/baas/v1/hosted-service/how-it-works\#how-sessions-work "Direct link to How sessions work")

### Via `browserWSEndpoint` [​](https://docs.browserless.io/baas/v1/hosted-service/how-it-works\#via-browserwsendpoint "Direct link to via-browserwsendpoint")

Libraries like puppeteer and chrome-remote-interface can hook into an existing Chrome instance by WebSocket. The hosted Browserless service only supports this type of interface since you can pass in tokens and other query-params. Typically you only need to replace how you start Chrome with a connect-like statement:

```codeBlockLines_p187
// Connecting to Chrome locally
const browser = await puppeteer.launch();

// Connecting to browserless
const browser = await puppeteer.connect({
  browserWSEndpoint: 'wss://chrome.browserless.io/?token=YOUR_API_TOKEN',
});

```

After that your code should remain exactly the same.

### Via `host` and `port` [​](https://docs.browserless.io/baas/v1/hosted-service/how-it-works\#via-host-and-port "Direct link to via-host-and-port")

Many libraries will issue an HTTP request to one of the `/json` endpoints exposed by Chrome's dev protocol. When this request happens, Browserless will respond with the resulting payload to allow remote programs to interact with it.

If you're looking to use the Browserless service with non-Node language, it's better to use the REST API's and `/function` endpoint as Browserless _can_ run puppeteer code for you. Take a look at our blog post about this interface [here](https://www.browserless.io/blog/2018/05/26/browserless-functions/#browserless-functions).

**Introspection Request**

```codeBlockLines_p187
# curl https://chrome.browserless.io/json?token=YOUR_API_TOKEN_HERE
[\
   {\
      "description":"",\
      "devtoolsFrontendUrl":"/devtools/inspector.html?ws=138.197.93.72:3000/devtools/page/da78a5e7-1db5-4d47-a2a5-07885088ad07",\
      "id":"da78a5e7-1db5-4d47-a2a5-07885088ad07",\
      "title":"about:blank",\
      "type":"page",\
      "url":"about:blank",\
      "webSocketDebuggerUrl":"ws://138.197.93.72:3000/devtools/page/da78a5e7-1db5-4d47-a2a5-07885088ad07"\
   }\
]

```

The WebSocket endpoints are where commands from the protocol are emitted into, and Chrome will then emit responses back. Browserless does not modify or alter any of these messages. Once your session and underlying websocket are closed, Browserless will automatically clear that Target and session data.

- [How sessions work](https://docs.browserless.io/baas/v1/hosted-service/how-it-works#how-sessions-work)
  - [Via `browserWSEndpoint`](https://docs.browserless.io/baas/v1/hosted-service/how-it-works#via-browserwsendpoint)
  - [Via `host` and `port`](https://docs.browserless.io/baas/v1/hosted-service/how-it-works#via-host-and-port)