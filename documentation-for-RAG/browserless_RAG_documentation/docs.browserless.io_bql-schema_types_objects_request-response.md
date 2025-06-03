---
url: "https://docs.browserless.io/bql-schema/types/objects/request-response"
title: "RequestResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/request-response#__docusaurus_skipToContent_fallback)

On this page

Response returned from the request API

```codeBlockLines_p187
type RequestResponse {
  url: String
  method: Method
  type: ResourceType
  headers: [Headers]
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/request-response\#fields "Direct link to Fields")

#### [`RequestResponse.url`](https://docs.browserless.io/bql-schema/types/objects/request-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/request-response\#requestresponseurlstring- "Direct link to requestresponseurlstring-")

The final URL of the request

#### [`RequestResponse.method`](https://docs.browserless.io/bql-schema/types/objects/request-response\#) ● [`Method`](https://docs.browserless.io/bql-schema/types/enums/method) enum [​](https://docs.browserless.io/bql-schema/types/objects/request-response\#requestresponsemethodmethod- "Direct link to requestresponsemethodmethod-")

The HTTP method of the request

#### [`RequestResponse.type`](https://docs.browserless.io/bql-schema/types/objects/request-response\#) ● [`ResourceType`](https://docs.browserless.io/bql-schema/types/enums/resource-type) enum [​](https://docs.browserless.io/bql-schema/types/objects/request-response\#requestresponsetyperesourcetype- "Direct link to requestresponsetyperesourcetype-")

The type of request that was made

#### [`RequestResponse.headers`](https://docs.browserless.io/bql-schema/types/objects/request-response\#) ● [`[Headers]`](https://docs.browserless.io/bql-schema/types/objects/headers) listobject [​](https://docs.browserless.io/bql-schema/types/objects/request-response\#requestresponseheadersheaders-- "Direct link to requestresponseheadersheaders--")

The headers of the request

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/request-response\#returned-by "Direct link to Returned By")

[`request`](https://docs.browserless.io/bql-schema/operations/mutations/request) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/request-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/request-response#returned-by)