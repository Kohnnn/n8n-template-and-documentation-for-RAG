---
url: "https://docs.browserless.io/bql-schema/types/inputs/clean-input"
title: "CleanInput | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/inputs/clean-input#__docusaurus_skipToContent_fallback)

On this page

Options for cleaning up the DOM prior to exporting its content. Many options are available, and this query can destructively remove non-text DOM nodes, DOM attributes, and gratuitous whitespace characters. Since these operations are destructive in their nature it's recommended to run them at the very end of your query in order to preserve page functionality

```codeBlockLines_p187
input CleanInput {
  removeNonTextNodes: Boolean
  removeAttributes: Boolean
  removeRegex: Boolean
  selectors: [String!]
  attributes: [String]
  regexes: [String!]
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#fields "Direct link to Fields")

#### [`CleanInput.removeNonTextNodes`](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#cleaninputremovenontextnodesboolean- "Direct link to cleaninputremovenontextnodesboolean-")

When true (default is true) this will remove non-textual nodes from the DOM like scripts, links, video, canvas, etc. You may override this by specifying a `selectors` argument for DOM selectors to remove.

#### [`CleanInput.removeAttributes`](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#cleaninputremoveattributesboolean- "Direct link to cleaninputremoveattributesboolean-")

When true (default is false) this will remove all attributes on all DOM nodes. Useful for "cleaning" up all HTML markup but preserving the structure overall. You can specify specific attributes to remove with `attributes` argument

#### [`CleanInput.removeRegex`](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#cleaninputremoveregexboolean- "Direct link to cleaninputremoveregexboolean-")

Removes any characters in the HTML by a regex pattern and arn in order. By default this is true and removes newlines, returns, tabs, multi-spaces and HTML comments in that order. You may supply your own regex by using the `regexes` argument

#### [`CleanInput.selectors`](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#) ● [`[String!]`](https://docs.browserless.io/bql-schema/types/scalars/string) listscalar [​](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#cleaninputselectorsstring-- "Direct link to cleaninputselectorsstring--")

A list of selectors to remove from the page when `removeNonTextNodes` is set to true ( `true` by default).

#### [`CleanInput.attributes`](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#) ● [`[String]`](https://docs.browserless.io/bql-schema/types/scalars/string) listscalar [​](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#cleaninputattributesstring-- "Direct link to cleaninputattributesstring--")

A list of attributes to remove from all DOM nodes. When this isn't specified, and `removeAttributes` is true, all attributes on all DOM nodes are removed. `removeNonTextNodes` must be set to `true` for this to take effect

#### [`CleanInput.regexes`](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#) ● [`[String!]`](https://docs.browserless.io/bql-schema/types/scalars/string) listscalar [​](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#cleaninputregexesstring-- "Direct link to cleaninputregexesstring--")

When `removeRegex` is set to "true" this list of regex items, without the beginning and ending `/`, are removed from the page. These are each run in order and replaced with a single space character to preserve some of their contents

### Member Of [​](https://docs.browserless.io/bql-schema/types/inputs/clean-input\#member-of "Direct link to Member Of")

[`html`](https://docs.browserless.io/bql-schema/operations/mutations/html) mutation ● [`text`](https://docs.browserless.io/bql-schema/operations/mutations/text) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/inputs/clean-input#fields)
- [Member Of](https://docs.browserless.io/bql-schema/types/inputs/clean-input#member-of)