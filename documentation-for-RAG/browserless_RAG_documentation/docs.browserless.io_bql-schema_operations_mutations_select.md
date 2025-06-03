---
url: "https://docs.browserless.io/bql-schema/operations/mutations/select"
title: "select | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/select#__docusaurus_skipToContent_fallback)

On this page

Selects a value from a dropdown or multiple select element

Example:

```codeBlockLines_p187
mutation Select {
  goto(url: "https://example.com") {
    status
  }

  single: select(
    selector: "select"
    value: "option1"
  ) {
    time
  }

  multi: select(
    selector: "select"
    value: ["option1", "option2"]
  ) {
    time
  }
}

```

```codeBlockLines_p187
select(
  timeout: Float
  scroll: Boolean = true
  selector: String!
  value: StringOrArray!
  visible: Boolean = false
  wait: Boolean = true
): SelectResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/select\#arguments "Direct link to Arguments")

#### [`select.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/select\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/select\#selecttimeoutfloat- "Direct link to selecttimeoutfloat-")

How long to wait for the element to appear before timing out on the handler, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`select.scroll`](https://docs.browserless.io/bql-schema/operations/mutations/select\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/select\#selectscrollboolean- "Direct link to selectscrollboolean-")

Whether or not to scroll to the select element prior to selecting, defaults to true

#### [`select.selector`](https://docs.browserless.io/bql-schema/operations/mutations/select\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/select\#selectselectorstring-- "Direct link to selectselectorstring--")

The CSS selector of the element on the page you want to select a value from

#### [`select.value`](https://docs.browserless.io/bql-schema/operations/mutations/select\#) ● [`StringOrArray!`](https://docs.browserless.io/bql-schema/types/scalars/string-or-array) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/select\#selectvaluestringorarray-- "Direct link to selectvaluestringorarray--")

The value or values to select from the dropdown or multiple select element

#### [`select.visible`](https://docs.browserless.io/bql-schema/operations/mutations/select\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/select\#selectvisibleboolean- "Direct link to selectvisibleboolean-")

Whether or not to select the element only if it's visible

#### [`select.wait`](https://docs.browserless.io/bql-schema/operations/mutations/select\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/select\#selectwaitboolean- "Direct link to selectwaitboolean-")

Whether or not to wait for the select to present in the DOM

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/select\#type "Direct link to Type")

#### [`SelectResponse`](https://docs.browserless.io/bql-schema/types/objects/select-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/select\#selectresponse- "Direct link to selectresponse-")

The response returned after selecting a value from a dropdown or multiple select element

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/select#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/select#type)