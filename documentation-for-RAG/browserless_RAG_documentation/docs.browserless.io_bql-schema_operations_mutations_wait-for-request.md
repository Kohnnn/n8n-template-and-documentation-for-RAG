---
url: "https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request"
title: "waitForRequest | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request#__docusaurus_skipToContent_fallback)

On this page

Waits for the browser to make a particular request

Example:

```codeBlockLines_p187
mutation WaitForRequest {
  goto(url: "https://browserless.io") {
    status
  }

  waitForRequest(method: GET) {
    time
  }
}

```

```codeBlockLines_p187
waitForRequest(
  method: Method
  timeout: Float
  url: String
): WaitForRequest

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request\#arguments "Direct link to Arguments")

#### [`waitForRequest.method`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request\#) ● [`Method`](https://docs.browserless.io/bql-schema/types/enums/method) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request\#waitforrequestmethodmethod- "Direct link to waitforrequestmethodmethod-")

The method of the request to wait for

#### [`waitForRequest.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request\#waitforrequesttimeoutfloat- "Direct link to waitforrequesttimeoutfloat-")

How long to wait for the request to be made before timing out, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`waitForRequest.url`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request\#waitforrequesturlstring- "Direct link to waitforrequesturlstring-")

The pattern of the request URL to wait for, using glob-style pattern-matching

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request\#type "Direct link to Type")

#### [`WaitForRequest`](https://docs.browserless.io/bql-schema/types/objects/wait-for-request) object [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request\#waitforrequest- "Direct link to waitforrequest-")

Response returned after a particular network request has been sent

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-request#type)