---
url: "https://docs.browserless.io/bql-schema/operations/mutations/title"
title: "title | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/title#__docusaurus_skipToContent_fallback)

On this page

Returns the title of the page that the browser is currently at

Example:

```codeBlockLines_p187
mutation GetTitle {
  goto(url: "https://example.com") {
    status
  }

  title {
    title
  }
}

```

```codeBlockLines_p187
title: TitleResponse

```

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/title\#type "Direct link to Type")

#### [`TitleResponse`](https://docs.browserless.io/bql-schema/types/objects/title-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/title\#titleresponse- "Direct link to titleresponse-")

Response returned after the page's title has been set or get

- [Type](https://docs.browserless.io/bql-schema/operations/mutations/title#type)