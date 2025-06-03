---
url: "https://docs.browserless.io/bql-schema/operations/mutations/url"
title: "url | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/url#__docusaurus_skipToContent_fallback)

On this page

Returns the URL of the page that the browser is currently at

Example:

```codeBlockLines_p187
mutation GetURL {
  goto(url: "https://example.com") {
    status
  }

  url {
    url
  }
}

```

```codeBlockLines_p187
url: URLResponse

```

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/url\#type "Direct link to Type")

#### [`URLResponse`](https://docs.browserless.io/bql-schema/types/objects/urlresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/url\#urlresponse- "Direct link to urlresponse-")

Response returned after the URL of the page has been set or get

- [Type](https://docs.browserless.io/bql-schema/operations/mutations/url#type)