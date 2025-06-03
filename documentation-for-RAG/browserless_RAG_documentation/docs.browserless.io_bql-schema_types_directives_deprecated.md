---
url: "https://docs.browserless.io/bql-schema/types/directives/deprecated"
title: "deprecated | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/directives/deprecated#__docusaurus_skipToContent_fallback)

On this page

Marks an element of a GraphQL schema as no longer supported.

```codeBlockLines_p187
directive @deprecated(
  reason: String = "No longer supported"
) on
  | FIELD_DEFINITION
  | ARGUMENT_DEFINITION
  | INPUT_FIELD_DEFINITION
  | ENUM_VALUE

```

### Arguments [​](https://docs.browserless.io/bql-schema/types/directives/deprecated\#arguments "Direct link to Arguments")

#### [`deprecated.reason`](https://docs.browserless.io/bql-schema/types/directives/deprecated\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/directives/deprecated\#deprecatedreasonstring- "Direct link to deprecatedreasonstring-")

Explains why this element was deprecated, usually also including a suggestion for how to access supported similar data. Formatted using the Markdown syntax, as specified by [CommonMark](https://commonmark.org/).

- [Arguments](https://docs.browserless.io/bql-schema/types/directives/deprecated#arguments)