---
url: "https://docs.browserless.io/baas/v1/apis/config"
title: "/config API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/config#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/enterprise/utility-functions/config) or [BrowserQL](https://docs.browserless.io/browserql/start).

The config API allows you to retrieve the current configuration of your container **and is only available for dedicated and self-hosted accounts.**

Check out the [config API schema](https://chrome.browserless.io/docs/#/Management%20API/get_config) defined in our Swagger page.

## Gathering your container configuration [​](https://docs.browserless.io/baas/v1/apis/config\#gathering-your-container-configuration "Direct link to Gathering your container configuration")

To see the configuration of your container, simply issue a `GET` request to `/config`:

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/config?token=MY_API_TOKEN

```

warning

Remember that running this in the browser will expose your API key!

Running this cURL request will result in an output like:

```codeBlockLines_p187
{
  "allowFileProtocol": true,
  "chromeRefreshTime": 0,
  "connectionTimeout": 0,
  "disabledFeatures": ["string"],
  "enableAPIGet": true,
  "enableCors": true,
  "errorAlertURL": "string",
  "exitOnHealthFailure": true,
  "functionBuiltIns": ["string"],
  "functionEnableIncognitoMode": true,
  "functionExternals": ["string"],
  "healthFailureURL": "string",
  "sessionCheckFailURL": "string",
  "keepAlive": true,
  "maxCPU": 0,
  "maxConcurrentSessions": 0,
  "maxMemory": 0,
  "maxQueueLength": 0,
  "metricsJSONPath": "string",
  "port": 0,
  "prebootChrome": true,
  "queuedAlertURL": "string",
  "rejectAlertURL": "string",
  "singleRun": true,
  "timeoutAlertURL": "string",
  "token": "string",
  "workspaceDir": "string",
  "socketBehavior": "string"
}

```

- [Gathering your container configuration](https://docs.browserless.io/baas/v1/apis/config#gathering-your-container-configuration)