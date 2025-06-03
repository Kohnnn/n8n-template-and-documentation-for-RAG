---
url: "https://docs.browserless.io/bql-schema/operations/mutations/reject"
title: "reject | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/reject#__docusaurus_skipToContent_fallback)

On this page

Rejects requests by a specified URL pattern, method, or type and operator. You may supply a single pattern, or a list (array) of them. This mutation, by default, will reject any requests that match _any_ pattern, which we call an "or" operator. To reject requests where conditions must all match, specify an "and" operator in the mutation. Note that this only has an effect when the query is executing, so scripts that return quickly will likely see assets loading in the editor as these rejections only happen when mutations are executing.

* * *

**Rejecting images or media**

```codeBlockLines_p187
mutation RejectImages {
  reject(type: [image, media]) {
    enabled
    time
  }
  goto(url: "https://cnn.com"
  waitUntil: firstContentfulPaint) {
    status
    time
  }
}

```

* * *

**Rejecting media when coming from google.com domain**

```codeBlockLines_p187
mutation Reject {
  reject(
    operator: and
    type: image
    url: "*google.com*"
  ) {
    enabled
    time
  }
  goto(url: "https://cnn.com"
  waitUntil: firstContentfulPaint) {
    status
    time
  }
}

```

```codeBlockLines_p187
reject(
  enabled: Boolean = true
  method: [Method]
  operator: OperatorTypes = or
  type: [ResourceType]
  url: [String]
): RejectResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/reject\#arguments "Direct link to Arguments")

#### [`reject.enabled`](https://docs.browserless.io/bql-schema/operations/mutations/reject\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/reject\#rejectenabledboolean- "Direct link to rejectenabledboolean-")

Whether or not to enable request rejections

#### [`reject.method`](https://docs.browserless.io/bql-schema/operations/mutations/reject\#) ● [`[Method]`](https://docs.browserless.io/bql-schema/types/enums/method) listenum [​](https://docs.browserless.io/bql-schema/operations/mutations/reject\#rejectmethodmethod-- "Direct link to rejectmethodmethod--")

The Method of the request you'd like to reject

#### [`reject.operator`](https://docs.browserless.io/bql-schema/operations/mutations/reject\#) ● [`OperatorTypes`](https://docs.browserless.io/bql-schema/types/enums/operator-types) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/reject\#rejectoperatoroperatortypes- "Direct link to rejectoperatoroperatortypes-")

Whether to "or" conditions together, meaning any condition that matches will be rejected, or "and" them together meaning every condition must match to reject the request.

#### [`reject.type`](https://docs.browserless.io/bql-schema/operations/mutations/reject\#) ● [`[ResourceType]`](https://docs.browserless.io/bql-schema/types/enums/resource-type) listenum [​](https://docs.browserless.io/bql-schema/operations/mutations/reject\#rejecttyperesourcetype-- "Direct link to rejecttyperesourcetype--")

The type of resource you'd like to reject request to

#### [`reject.url`](https://docs.browserless.io/bql-schema/operations/mutations/reject\#) ● [`[String]`](https://docs.browserless.io/bql-schema/types/scalars/string) listscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/reject\#rejecturlstring-- "Direct link to rejecturlstring--")

The glob-style URL pattern you'd like to reject requests to

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/reject\#type "Direct link to Type")

#### [`RejectResponse`](https://docs.browserless.io/bql-schema/types/objects/reject-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/reject\#rejectresponse- "Direct link to rejectresponse-")

The response parameters for the reject mutation

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/reject#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/reject#type)