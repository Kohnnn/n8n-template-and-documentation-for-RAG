---
url: "https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response"
title: "waitForResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response#__docusaurus_skipToContent_fallback)

On this page

Waits for a particular network response to be made back to the browser

Example:

```codeBlockLines_p187
mutation WaitForResponse {
  goto(url: "https://browserless.io") {
    status
  }

  waitForResponse(codes: [200]) {
    time
  }
}

```

```codeBlockLines_p187
waitForResponse(
  codes: [Int]
  statuses: [Int]
  url: String
): WaitForResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response\#arguments "Direct link to Arguments")

#### [`waitForResponse.codes`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response\#) ● [`[Int]`](https://docs.browserless.io/bql-schema/types/scalars/int) deprecatedlistscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response\#waitforresponsecodesint--- "Direct link to waitforresponsecodesint---")

DEPRECATED

Use `statuses` field instead as it is more consistent in BrowserQL.

The HTTP Response code(s) of the URL to wait for. Can be a single HTTP code or a list of desired codes

#### [`waitForResponse.statuses`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response\#) ● [`[Int]`](https://docs.browserless.io/bql-schema/types/scalars/int) listscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response\#waitforresponsestatusesint-- "Direct link to waitforresponsestatusesint--")

The HTTP Response code(s) of the URL to wait for. Can be a single HTTP code or a list of desired codes

#### [`waitForResponse.url`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response\#waitforresponseurlstring- "Direct link to waitforresponseurlstring-")

The pattern of the response URL to wait for, using glob-style pattern-matching

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response\#type "Direct link to Type")

#### [`WaitForResponse`](https://docs.browserless.io/bql-schema/types/objects/wait-for-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response\#waitforresponse- "Direct link to waitforresponse-")

Response returned after a particular network response has been received

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-response#type)