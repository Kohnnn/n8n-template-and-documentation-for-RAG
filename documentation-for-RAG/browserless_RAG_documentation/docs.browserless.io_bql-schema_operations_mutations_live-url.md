---
url: "https://docs.browserless.io/bql-schema/operations/mutations/live-url"
title: "liveURL | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/live-url#__docusaurus_skipToContent_fallback)

On this page

Returns a fully-qualified, user-shareable live-URL for streaming the web-browser to an end-user, optionally interactive.

**Set 30 second timer for interaction**

```codeBlockLines_p187
mutation LiveURL {
  goto(url: "https://example.com") {
    status
  }
  liveURL {
    liveURL
  }
}

```

**Don't allow interaction at all**

```codeBlockLines_p187
mutation LiveURL {
  goto(url: "https://example.com") {
    status
  }
  liveURL(interactable: false) {
    liveURL
  }
}

```

**Low quality for better bandwidth**

```codeBlockLines_p187
mutation LiveURL {
  goto(url: "https://example.com") {
    status
  }
  liveURL(quality: 20 type: jpeg) {
    liveURL
  }
}

```

```codeBlockLines_p187
liveURL(
  timeout: Float
  interactable: Boolean = true
  type: LiveURLStreamType = jpeg
  quality: Int = 100
): LiveURLResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#arguments "Direct link to Arguments")

#### [`liveURL.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#liveurltimeoutfloat- "Direct link to liveurltimeoutfloat-")

The maximum time allowed for the browser to remain alive. Once the time is reached, the end-user will receive a prompt that the session has closed

#### [`liveURL.interactable`](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#liveurlinteractableboolean- "Direct link to liveurlinteractableboolean-")

Whether the session is interactable or not. Set to "false" to not allow click and mouse events to be forwarded through to the end-user

#### [`liveURL.type`](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#) ● [`LiveURLStreamType`](https://docs.browserless.io/bql-schema/types/enums/live-urlstream-type) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#liveurltypeliveurlstreamtype- "Direct link to liveurltypeliveurlstreamtype-")

The binary-type of the streamed imaged. "jpeg" will consumer lower bandwidth and useful low bandwidth networks and devices. "png" is a much higher quality but will consume considerably more bandwidth.

Use "jpeg" when setting a custom quality

#### [`liveURL.quality`](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#) ● [`Int`](https://docs.browserless.io/bql-schema/types/scalars/int) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#liveurlqualityint- "Direct link to liveurlqualityint-")

The quality of the stream, represented as number from 1 - 100. Only used when "type" is "jpeg"

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#type "Direct link to Type")

#### [`LiveURLResponse`](https://docs.browserless.io/bql-schema/types/objects/live-urlresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/live-url\#liveurlresponse- "Direct link to liveurlresponse-")

The response from the Live-URL query

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/live-url#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/live-url#type)