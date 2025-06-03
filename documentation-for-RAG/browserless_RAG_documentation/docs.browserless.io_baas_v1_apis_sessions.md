---
url: "https://docs.browserless.io/baas/v1/apis/sessions"
title: "/sessions API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/sessions#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/enterprise/utility-functions/sessions) or [BrowserQL](https://docs.browserless.io/browserql/start).

The sessions API allows you to gather information about the currently running sessions **and is only available for dedicated and self-hosted accounts**

Check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Management%20API/get_sessions).

## Gathering information from your running sessions [​](https://docs.browserless.io/baas/v1/apis/sessions\#gathering-information-from-your-running-sessions "Direct link to Gathering information from your running sessions")

To see information regarding the running sessions, simply issue a `GET` request to `/sessions`:

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/sessions?token=MY_API_TOKEN

```

warning

Remember that running this in the browser will expose your API key!

Running this cURL request will result in an output like:

```codeBlockLines_p187
[\
  {\
    "description": "",\
    "devtoolsFrontendUrl": "/devtools/inspector.html?ws=0.0.0.0:3000/devtools/page/7B491986CD0B6408DF15A339A7621226",\
    "id": "7B491986CD0B6408DF15A339A7621226",\
    "title": "Example Domain",\
    "type": "page",\
    "url": "https://www.example.com",\
    "webSocketDebuggerUrl": "ws://0.0.0.0:3000/devtools/page/7B491986CD0B6408DF15A339A7621226",\
    "port": "41685",\
    "browserId": "b95cd82a-76b1-495e-8092-b040de780d0f",\
    "trackingId": null,\
    "browserWSEndpoint": "ws://0.0.0.0:3000/devtools/browser/b95cd82a-76b1-495e-8092-b040de780d0f"\
  }\
]

```

- [Gathering information from your running sessions](https://docs.browserless.io/baas/v1/apis/sessions#gathering-information-from-your-running-sessions)