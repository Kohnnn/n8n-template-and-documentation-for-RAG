---
url: "https://docs.browserless.io/baas/v1/apis/kill"
title: "/kill API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/kill#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/intro) or [BrowserQL](https://docs.browserless.io/browserql/start).

The kill API allows you to kill a specific session or all the open sessions **and is only available for dedicated and self-hosted accounts.**

Check out the [kill API schema](https://chrome.browserless.io/docs/#/Management%20API/get_kill__id_) defined in our Swagger page.

danger

These actions **cannot** be undone

### Examples [​](https://docs.browserless.io/baas/v1/apis/kill\#examples "Direct link to Examples")

1. [Killing a specific session](https://docs.browserless.io/baas/v1/apis/kill#killing-a-specific-session)
2. [Killing all the sessions](https://docs.browserless.io/baas/v1/apis/kill#killing-all-the-sessions)

## Killing a specific session [​](https://docs.browserless.io/baas/v1/apis/kill\#killing-a-specific-session "Direct link to Killing a specific session")

To kill a specific session, simply issue a `GET` request to `/kill/{id}`, you can set the id with the browser ID or tracking-ID, you can find this with the help of the [sessions API](https://chrome.browserless.io/docs/#/Management%20API/get_sessions)

You can run this with a cURL request as so:

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/kill/{id}?token=MY_API_TOKEN

```

## Killing all the sessions [​](https://docs.browserless.io/baas/v1/apis/kill\#killing-all-the-sessions "Direct link to Killing all the sessions")

To kill all the open sessions, simply issue a `GET` request to `/kill/all`

You can run this with a cURL request as so:

```codeBlockLines_p187
curl -X GET \
  https://chrome.browserless.io/kill/all?token=MY_API_TOKEN

```

warning

Remember that running this in the browser will expose your API key!

- [Examples](https://docs.browserless.io/baas/v1/apis/kill#examples)
- [Killing a specific session](https://docs.browserless.io/baas/v1/apis/kill#killing-a-specific-session)
- [Killing all the sessions](https://docs.browserless.io/baas/v1/apis/kill#killing-all-the-sessions)