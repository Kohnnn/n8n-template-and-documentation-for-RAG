---
url: "https://docs.browserless.io/bql-schema/operations/mutations/query-selector"
title: "querySelector | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/query-selector#__docusaurus_skipToContent_fallback)

On this page

Passes through certain properties of the browsers' own `document.querySelector` API

Example:

```codeBlockLines_p187
mutation QuerySelector {
  goto(url: "https://example.com") {
    status
  }

  query: querySelector(selector: "h1") {
    innerHTML
  }
}

```

```codeBlockLines_p187
querySelector(
  selector: String!
  timeout: Float
  visible: Boolean = false
): QuerySelectorResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector\#arguments "Direct link to Arguments")

#### [`querySelector.selector`](https://docs.browserless.io/bql-schema/operations/mutations/query-selector\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector\#queryselectorselectorstring-- "Direct link to queryselectorselectorstring--")

#### [`querySelector.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/query-selector\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector\#queryselectortimeoutfloat- "Direct link to queryselectortimeoutfloat-")

#### [`querySelector.visible`](https://docs.browserless.io/bql-schema/operations/mutations/query-selector\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector\#queryselectorvisibleboolean- "Direct link to queryselectorvisibleboolean-")

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector\#type "Direct link to Type")

#### [`QuerySelectorResponse`](https://docs.browserless.io/bql-schema/types/objects/query-selector-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector\#queryselectorresponse- "Direct link to queryselectorresponse-")

The response returned after querying the page for a selector

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/query-selector#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/query-selector#type)