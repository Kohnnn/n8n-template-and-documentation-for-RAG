---
url: "https://docs.browserless.io/bql-schema/operations/mutations/content"
title: "content | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/content#__docusaurus_skipToContent_fallback)

On this page

Sets the given HTML content on the page with an optional waitUntil parameter

Example:

```codeBlockLines_p187
mutation SetContent {
  content(html: "<h1>Hello, World!</h1>") {
    status
  }
}

```

```codeBlockLines_p187
content(
  html: String!
  waitUntil: WaitUntilHistory
): HTTPResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/content\#arguments "Direct link to Arguments")

#### [`content.html`](https://docs.browserless.io/bql-schema/operations/mutations/content\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/content\#contenthtmlstring-- "Direct link to contenthtmlstring--")

When present, sets the content of page to the value passed, then returns the pages content

#### [`content.waitUntil`](https://docs.browserless.io/bql-schema/operations/mutations/content\#) ● [`WaitUntilHistory`](https://docs.browserless.io/bql-schema/types/enums/wait-until-history) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/content\#contentwaituntilwaituntilhistory- "Direct link to contentwaituntilwaituntilhistory-")

When to consider the page fully-loaded and proceed with further execution, used in conjunction with the value parameter

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/content\#type "Direct link to Type")

#### [`HTTPResponse`](https://docs.browserless.io/bql-schema/types/objects/httpresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/content\#httpresponse- "Direct link to httpresponse-")

Response returned after a navigation event

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/content#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/content#type)