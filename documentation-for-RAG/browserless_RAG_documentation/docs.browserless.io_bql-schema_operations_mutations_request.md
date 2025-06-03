---
url: "https://docs.browserless.io/bql-schema/operations/mutations/request"
title: "request | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/request#__docusaurus_skipToContent_fallback)

On this page

Returns request information made by the Browser with optional filters via arguments. You may filter the returned results by a lob-like URL-pattern, the method of the request or the type of request. Applying an operator to this will then change the behavior by either "and"ing the filters together or "or"ing them. This API will automatically wait for the request to be made if none is immediately found which you can turn off by disabling the "wait" option.

**Getting all "Document" requests**

```codeBlockLines_p187
  mutation DocumentRequests {
    goto(url: "https://example.com/", waitUntil: load) {
      status
    }
    request(type:document) {
      url
      type
      method
      headers {
        name
        value
      }
    }
  }

```

**Load all "GET" AJAX Requests**

```codeBlockLines_p187
  mutation AJAXGetCalls {
    goto(url: "https://msn.com/", waitUntil: load) {
      status
    }
    request(type: xhr, method: GET, operator: and) {
      url
      type
      method
      headers {
        name
        value
      }
    }
  }

```

```codeBlockLines_p187
request(
  type: [ResourceType]
  method: [Method]
  timeout: Float
  url: [String]
  wait: Boolean = true
  operator: OperatorTypes = or
): [RequestResponse]

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/request\#arguments "Direct link to Arguments")

#### [`request.type`](https://docs.browserless.io/bql-schema/operations/mutations/request\#) ● [`[ResourceType]`](https://docs.browserless.io/bql-schema/types/enums/resource-type) listenum [​](https://docs.browserless.io/bql-schema/operations/mutations/request\#requesttyperesourcetype-- "Direct link to requesttyperesourcetype--")

The type content-type of the request to match against

#### [`request.method`](https://docs.browserless.io/bql-schema/operations/mutations/request\#) ● [`[Method]`](https://docs.browserless.io/bql-schema/types/enums/method) listenum [​](https://docs.browserless.io/bql-schema/operations/mutations/request\#requestmethodmethod-- "Direct link to requestmethodmethod--")

The method of the request to return results for

#### [`request.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/request\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/request\#requesttimeoutfloat- "Direct link to requesttimeoutfloat-")

How long to wait for the request(s) to be made before timing out, overriding any defaults. Default timeout is 30 seconds, or 30000. "wait" parameter must also be "true".

#### [`request.url`](https://docs.browserless.io/bql-schema/operations/mutations/request\#) ● [`[String]`](https://docs.browserless.io/bql-schema/types/scalars/string) listscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/request\#requesturlstring-- "Direct link to requesturlstring--")

The pattern of the request URL to wait for, using glob-style pattern-matching

#### [`request.wait`](https://docs.browserless.io/bql-schema/operations/mutations/request\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/request\#requestwaitboolean- "Direct link to requestwaitboolean-")

Whether or not to wait for the request to be made. When set to `true`, generally only one request is returned since this API will wait for the first request that matches any patterns to be returned

#### [`request.operator`](https://docs.browserless.io/bql-schema/operations/mutations/request\#) ● [`OperatorTypes`](https://docs.browserless.io/bql-schema/types/enums/operator-types) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/request\#requestoperatoroperatortypes- "Direct link to requestoperatoroperatortypes-")

When applying arguments like URL or method, this operator will either "and" them together, or "or" them together. Default is "or"

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/request\#type "Direct link to Type")

#### [`RequestResponse`](https://docs.browserless.io/bql-schema/types/objects/request-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/request\#requestresponse- "Direct link to requestresponse-")

Response returned from the request API

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/request#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/request#type)