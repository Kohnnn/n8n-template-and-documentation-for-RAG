---
url: "https://docs.browserless.io/bql-schema/operations/mutations/checkbox"
title: "checkbox | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/checkbox#__docusaurus_skipToContent_fallback)

On this page

Sets or un-sets the value of a checkbox on the page

Example:

```codeBlockLines_p187
mutation ClickCheckbox {
  goto(url: "https://example.com") {
    status
  }

  checkbox(
    checked: true
    selector: "input[type='checkbox']"
  ) {
    time
  }
}

```

```codeBlockLines_p187
checkbox(
  checked: Boolean!
  selector: String!
  scroll: Boolean = true
  timeout: Float
  visible: Boolean = false
  wait: Boolean = true
): ClickResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#arguments "Direct link to Arguments")

#### [`checkbox.checked`](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#) ● [`Boolean!`](https://docs.browserless.io/bql-schema/types/scalars/boolean) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#checkboxcheckedboolean-- "Direct link to checkboxcheckedboolean--")

Whether or not the input should be checked

#### [`checkbox.selector`](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#checkboxselectorstring-- "Direct link to checkboxselectorstring--")

The CSS selector of the element on the page you want to check/uncheck

#### [`checkbox.scroll`](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#checkboxscrollboolean- "Direct link to checkboxscrollboolean-")

Whether or not to scroll to the element prior to clicking, defaults to true

#### [`checkbox.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#checkboxtimeoutfloat- "Direct link to checkboxtimeoutfloat-")

How long to wait for the element to appear before timing out on the handler, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`checkbox.visible`](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#checkboxvisibleboolean- "Direct link to checkboxvisibleboolean-")

Whether or not to check/uncheck the element only if it's visible

#### [`checkbox.wait`](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#checkboxwaitboolean- "Direct link to checkboxwaitboolean-")

Whether or not to wait for the element to present in the DOM

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#type "Direct link to Type")

#### [`ClickResponse`](https://docs.browserless.io/bql-schema/types/objects/click-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/checkbox\#clickresponse- "Direct link to clickresponse-")

Response returned after having clicked on an element

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/checkbox#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/checkbox#type)