---
url: "https://docs.browserless.io/bql-schema/types/objects/response-response"
title: "ResponseResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/response-response#__docusaurus_skipToContent_fallback)

On this page

Response returned from the response API

```codeBlockLines_p187
type ResponseResponse {
  status: Int
  url: String
  method: Method
  type: ResourceType
  headers: [Headers]
  body: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/response-response\#fields "Direct link to Fields")

#### [`ResponseResponse.status`](https://docs.browserless.io/bql-schema/types/objects/response-response\#) ● [`Int`](https://docs.browserless.io/bql-schema/types/scalars/int) scalar [​](https://docs.browserless.io/bql-schema/types/objects/response-response\#responseresponsestatusint- "Direct link to responseresponsestatusint-")

The HTTP status code of the response

#### [`ResponseResponse.url`](https://docs.browserless.io/bql-schema/types/objects/response-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/response-response\#responseresponseurlstring- "Direct link to responseresponseurlstring-")

The final URL of the response

#### [`ResponseResponse.method`](https://docs.browserless.io/bql-schema/types/objects/response-response\#) ● [`Method`](https://docs.browserless.io/bql-schema/types/enums/method) enum [​](https://docs.browserless.io/bql-schema/types/objects/response-response\#responseresponsemethodmethod- "Direct link to responseresponsemethodmethod-")

The HTTP method of the request that facilitated the response

#### [`ResponseResponse.type`](https://docs.browserless.io/bql-schema/types/objects/response-response\#) ● [`ResourceType`](https://docs.browserless.io/bql-schema/types/enums/resource-type) enum [​](https://docs.browserless.io/bql-schema/types/objects/response-response\#responseresponsetyperesourcetype- "Direct link to responseresponsetyperesourcetype-")

The type of response that was received

#### [`ResponseResponse.headers`](https://docs.browserless.io/bql-schema/types/objects/response-response\#) ● [`[Headers]`](https://docs.browserless.io/bql-schema/types/objects/headers) listobject [​](https://docs.browserless.io/bql-schema/types/objects/response-response\#responseresponseheadersheaders-- "Direct link to responseresponseheadersheaders--")

The response headers returned

#### [`ResponseResponse.body`](https://docs.browserless.io/bql-schema/types/objects/response-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/response-response\#responseresponsebodystring- "Direct link to responseresponsebodystring-")

The body of the response, represented as a string when possible or base64 for binary-type requests like images

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/response-response\#returned-by "Direct link to Returned By")

[`response`](https://docs.browserless.io/bql-schema/operations/mutations/response) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/response-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/response-response#returned-by)