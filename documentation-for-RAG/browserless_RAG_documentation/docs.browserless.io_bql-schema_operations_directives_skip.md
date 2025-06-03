---
url: "https://docs.browserless.io/bql-schema/operations/directives/skip"
title: "skip | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/directives/skip#__docusaurus_skipToContent_fallback)

On this page

Directs the executor to skip this field or fragment when the `if` argument is true.

```codeBlockLines_p187
directive @skip(
  if: Boolean!
) on
  | FIELD
  | FRAGMENT_SPREAD
  | INLINE_FRAGMENT

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/directives/skip\#arguments "Direct link to Arguments")

#### [`skip.if`](https://docs.browserless.io/bql-schema/operations/directives/skip\#) ● [`Boolean!`](https://docs.browserless.io/bql-schema/types/scalars/boolean) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/directives/skip\#skipifboolean-- "Direct link to skipifboolean--")

Skipped when true.

- [Arguments](https://docs.browserless.io/bql-schema/operations/directives/skip#arguments)