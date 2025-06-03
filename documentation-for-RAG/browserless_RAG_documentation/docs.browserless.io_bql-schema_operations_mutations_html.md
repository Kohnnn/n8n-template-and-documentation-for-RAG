---
url: "https://docs.browserless.io/bql-schema/operations/mutations/html"
title: "html | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/html#__docusaurus_skipToContent_fallback)

On this page

Returns the HTML content of the page or selector when specified. This API can also "clean" HTML markup returned by specifying a "clean" argument with numerous options. Features of the "clean" argument include removal of non-text nodes, removal of DOM attributes, as well as removal of excessive whitespace and newlines. Using "clean" can save nearly 1,000 times the payload size. Useful for LLM's and other scenarios

Example:

```codeBlockLines_p187
mutation GetHTML {
  goto(url: "https://example.com") {
    status
  }
  html(selector: "h1") {
    html
  }
}

```

Remove non-text DOM nodes and all Node attributes, but preserve the DOM tree

```codeBlockLines_p187
mutation GetHTML {
  goto(url: "https://example.com") {
    status
  }

  html(clean: {
    removeAttributes: true
    removeNonTextNodes: true
  }) {
    html
  }
}

```

```codeBlockLines_p187
html(
  selector: String
  timeout: Float
  visible: Boolean = false
  clean: CleanInput
): HTMLResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/html\#arguments "Direct link to Arguments")

#### [`html.selector`](https://docs.browserless.io/bql-schema/operations/mutations/html\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/html\#htmlselectorstring- "Direct link to htmlselectorstring-")

The DOM selector of the given element you want to return the HTML of

#### [`html.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/html\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/html\#htmltimeoutfloat- "Direct link to htmltimeoutfloat-")

The maximum amount of time, in milliseconds, to wait for the selector to appear, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`html.visible`](https://docs.browserless.io/bql-schema/operations/mutations/html\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/html\#htmlvisibleboolean- "Direct link to htmlvisibleboolean-")

Whether or not to return the HTMLπ content of the element only if it's visible

#### [`html.clean`](https://docs.browserless.io/bql-schema/operations/mutations/html\#) ● [`CleanInput`](https://docs.browserless.io/bql-schema/types/inputs/clean-input) input [​](https://docs.browserless.io/bql-schema/operations/mutations/html\#htmlcleancleaninput- "Direct link to htmlcleancleaninput-")

Specifies conditions for "cleaning" HTML, useful for minimizing the amount of markup returned for cases like LLMs and more. See nested options for parameters.

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/html\#type "Direct link to Type")

#### [`HTMLResponse`](https://docs.browserless.io/bql-schema/types/objects/htmlresponse) object [​](https://docs.browserless.io/bql-schema/operations/mutations/html\#htmlresponse- "Direct link to htmlresponse-")

HTML content of a page

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/html#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/html#type)