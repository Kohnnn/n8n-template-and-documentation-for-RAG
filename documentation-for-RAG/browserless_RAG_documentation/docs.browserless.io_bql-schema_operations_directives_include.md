---
url: "https://docs.browserless.io/bql-schema/operations/directives/include"
title: "include | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/directives/include#__docusaurus_skipToContent_fallback)

On this page

Directs the executor to include this field or fragment only when the `if` argument is true.

```codeBlockLines_p187
directive @include(
  if: Boolean!
) on
  | FIELD
  | FRAGMENT_SPREAD
  | INLINE_FRAGMENT

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/directives/include\#arguments "Direct link to Arguments")

#### [`include.if`](https://docs.browserless.io/bql-schema/operations/directives/include\#) ● [`Boolean!`](https://docs.browserless.io/bql-schema/types/scalars/boolean) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/directives/include\#includeifboolean-- "Direct link to includeifboolean--")

Included when true.

- [Arguments](https://docs.browserless.io/bql-schema/operations/directives/include#arguments)