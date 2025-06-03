---
url: "https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all"
title: "querySelectorAll | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all#__docusaurus_skipToContent_fallback)

On this page

Passes through certain properties of the browsers' own `document.querySelectorAll` API

Example:

````codeBlockLines_p187
mutation QuerySelectorAll &#x007B;
  goto(url: "https://example.com") &#x007B;
    status
  &#x007D;

  query: querySelectorAll(selector: "h1") &#x007B;
    innerHTML
  &#x007D;
&#x007D;

```graphql
querySelectorAll(
selector: String!
timeout: Float
visible: Boolean = false
): [QuerySelectorResponse]

````

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all\#arguments "Direct link to Arguments")

#### [`querySelectorAll.selector`](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all\#queryselectorallselectorstring-- "Direct link to queryselectorallselectorstring--")

#### [`querySelectorAll.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all\#queryselectoralltimeoutfloat- "Direct link to queryselectoralltimeoutfloat-")

#### [`querySelectorAll.visible`](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all\#queryselectorallvisibleboolean- "Direct link to queryselectorallvisibleboolean-")

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all\#type "Direct link to Type")

#### [`QuerySelectorResponse`](https://docs.browserless.io/bql-schema/types/objects/query-selector-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all\#queryselectorresponse- "Direct link to queryselectorresponse-")

The response returned after querying the page for a selector

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all#type)