---
url: "https://docs.browserless.io/bql-schema/operations/mutations/text"
title: "text | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/text#__docusaurus_skipToContent_fallback)

On this page

Returns the text content on the given page or by selector when specified

Example:

```codeBlockLines_p187
mutation GetText {
  goto(url: "https://example.com") {
    status
  }

  selector: text(selector: "h1") {
      text
  }

  fullPage: text {
    text
  }
}

```

```codeBlockLines_p187
text(
  timeout: Float
  selector: String
  visible: Boolean = false
  clean: CleanInput
): TextResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/text\#arguments "Direct link to Arguments")

#### [`text.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/text\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/text\#texttimeoutfloat- "Direct link to texttimeoutfloat-")

The maximum amount of time, in milliseconds, to wait for the selector to appear, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`text.selector`](https://docs.browserless.io/bql-schema/operations/mutations/text\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/text\#textselectorstring- "Direct link to textselectorstring-")

The DOM selector of the given element you want to return the text of

#### [`text.visible`](https://docs.browserless.io/bql-schema/operations/mutations/text\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/text\#textvisibleboolean- "Direct link to textvisibleboolean-")

Whether or not to return the text content of the element only if it's visible

#### [`text.clean`](https://docs.browserless.io/bql-schema/operations/mutations/text\#) ● [`CleanInput`](https://docs.browserless.io/bql-schema/types/inputs/clean-input) input [​](https://docs.browserless.io/bql-schema/operations/mutations/text\#textcleancleaninput- "Direct link to textcleancleaninput-")

Specifies conditions for "cleaning" the returned text, useful for minimizing the amount of markup returned for cases like LLMs and more. See nested options for parameters.

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/text\#type "Direct link to Type")

#### [`TextResponse`](https://docs.browserless.io/bql-schema/types/objects/text-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/text\#textresponse- "Direct link to textresponse-")

Text content of a page

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/text#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/text#type)