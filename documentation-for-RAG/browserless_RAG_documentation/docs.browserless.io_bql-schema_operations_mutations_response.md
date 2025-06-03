---
url: "https://docs.browserless.io/bql-schema/operations/mutations/response"
title: "response | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/response#__docusaurus_skipToContent_fallback)

On this page

Returns response information, filtered by the provided arguments, made by the browser. You may optionally filter the returned results by a glob-like URL-pattern, the Method of the response or the Type of response. Applying an operator to this will then change the behavior by either "and"ing the filters together, or "or"ing them. This API will automatically wait for the response to be made if none is immediately found which you can turn off by disabling the "wait" option.

**Getting all "Document" responses**

```codeBlockLines_p187
  mutation DocumentResponses{
    goto(url: "https://example.com/", waitUntil: load) {
      status
    }
    response(type:document) {
      url
      body
      headers {
        name
        value
      }
    }
  }

```

**Load all "GET" AJAX Responses**

```codeBlockLines_p187
  mutation AJAXGetCalls {
    goto(url: "https://msn.com/", waitUntil: load) {
      status
    }
    response(type: xhr, method: GET, operator: and) {
      url
      type
      method
      body
      headers {
        name
        value
      }
    }
  }

```

```codeBlockLines_p187
response(
  status: [Int]
  method: [Method]
  operator: OperatorTypes = or
  timeout: Float
  type: [ResourceType]
  url: [String]
  wait: Boolean = true
): [ResponseResponse]

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#arguments "Direct link to Arguments")

#### [`response.status`](https://docs.browserless.io/bql-schema/operations/mutations/response\#) ● [`[Int]`](https://docs.browserless.io/bql-schema/types/scalars/int) listscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#responsestatusint-- "Direct link to responsestatusint--")

The status codes response to return results for

#### [`response.method`](https://docs.browserless.io/bql-schema/operations/mutations/response\#) ● [`[Method]`](https://docs.browserless.io/bql-schema/types/enums/method) listenum [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#responsemethodmethod-- "Direct link to responsemethodmethod--")

The method of the response to return results for

#### [`response.operator`](https://docs.browserless.io/bql-schema/operations/mutations/response\#) ● [`OperatorTypes`](https://docs.browserless.io/bql-schema/types/enums/operator-types) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#responseoperatoroperatortypes- "Direct link to responseoperatoroperatortypes-")

When applying arguments like URL or method, this operator will either "and" them together, or "or" them together. Default is "or"

#### [`response.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#responsetimeoutfloat- "Direct link to responsetimeoutfloat-")

How long to wait for the response(s) to be made before timing out, overriding any defaults. Default timeout is 30 seconds, or 30000. "wait" parameter must also be "true".

#### [`response.type`](https://docs.browserless.io/bql-schema/operations/mutations/response\#) ● [`[ResourceType]`](https://docs.browserless.io/bql-schema/types/enums/resource-type) listenum [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#responsetyperesourcetype-- "Direct link to responsetyperesourcetype--")

The type content-type of the response to match against

#### [`response.url`](https://docs.browserless.io/bql-schema/operations/mutations/response\#) ● [`[String]`](https://docs.browserless.io/bql-schema/types/scalars/string) listscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#responseurlstring-- "Direct link to responseurlstring--")

The pattern of the response URL to wait for, using glob-style pattern-matching

#### [`response.wait`](https://docs.browserless.io/bql-schema/operations/mutations/response\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#responsewaitboolean- "Direct link to responsewaitboolean-")

Whether or not to wait for the response to be received. When set to `true`, generally only one response is returned since this API will wait for the first response that matches any patterns to be returned

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#type "Direct link to Type")

#### [`ResponseResponse`](https://docs.browserless.io/bql-schema/types/objects/response-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/response\#responseresponse- "Direct link to responseresponse-")

Response returned from the response API

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/response#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/response#type)