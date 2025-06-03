---
url: "https://docs.browserless.io/bql-schema/operations/mutations/hover"
title: "hover | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/hover#__docusaurus_skipToContent_fallback)

On this page

Waits for the element to be visible, scrolls to it, then hover on it with native events

Example:

```codeBlockLines_p187
mutation HoverElement {
  goto(url: "https://example.com") {
    status
  }

  hover(selector: "a") {
    time
  }
}

```

```codeBlockLines_p187
hover(
  scroll: Boolean = true
  selector: String
  timeout: Float
  visible: Boolean = false
  wait: Boolean = true
  x: Float
  y: Float
): HoverResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#arguments "Direct link to Arguments")

#### [`hover.scroll`](https://docs.browserless.io/bql-schema/operations/mutations/hover\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#hoverscrollboolean- "Direct link to hoverscrollboolean-")

Whether or not to scroll to the element, defaults to true

#### [`hover.selector`](https://docs.browserless.io/bql-schema/operations/mutations/hover\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#hoverselectorstring- "Direct link to hoverselectorstring-")

The CSS selector of the element on the page you want to hover on

#### [`hover.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/hover\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#hovertimeoutfloat- "Direct link to hovertimeoutfloat-")

How long to wait for the element to appear before timing out, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`hover.visible`](https://docs.browserless.io/bql-schema/operations/mutations/hover\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#hovervisibleboolean- "Direct link to hovervisibleboolean-")

Whether or not to hover on the element only if it's visible

#### [`hover.wait`](https://docs.browserless.io/bql-schema/operations/mutations/hover\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#hoverwaitboolean- "Direct link to hoverwaitboolean-")

Whether or not to wait for the element to present in the DOM

#### [`hover.x`](https://docs.browserless.io/bql-schema/operations/mutations/hover\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#hoverxfloat- "Direct link to hoverxfloat-")

The X coordinate, in pixels, to hover on the page

#### [`hover.y`](https://docs.browserless.io/bql-schema/operations/mutations/hover\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#hoveryfloat- "Direct link to hoveryfloat-")

The Y coordinate, in pixels, to hover on the page

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#type "Direct link to Type")

#### [`HoverResponse`](https://docs.browserless.io/bql-schema/types/objects/hover-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/hover\#hoverresponse- "Direct link to hoverresponse-")

Response returned after having hovered over an element

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/hover#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/hover#type)