---
url: "https://docs.browserless.io/bql-schema/operations/mutations/scroll"
title: "scroll | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/scroll#__docusaurus_skipToContent_fallback)

On this page

Waits for a selector, then scrolls to it on the page or an x,y coordinate in pixels

Example:

```codeBlockLines_p187
mutation Scroll {
  goto(url: "https://example.com") {
    status
  }

  scroll(selector: "h1") {
    time
  }
}

```

```codeBlockLines_p187
scroll(
  selector: String
  timeout: Float
  visible: Boolean = false
  wait: Boolean = true
  x: Float
  y: Float
): ScrollResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#arguments "Direct link to Arguments")

#### [`scroll.selector`](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#scrollselectorstring- "Direct link to scrollselectorstring-")

The DOM selector of the element on the page you want to scroll to

#### [`scroll.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#scrolltimeoutfloat- "Direct link to scrolltimeoutfloat-")

How long to wait for the element to appear before timing out, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`scroll.visible`](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#scrollvisibleboolean- "Direct link to scrollvisibleboolean-")

Whether or not to scroll to the element only if it's visible

#### [`scroll.wait`](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#scrollwaitboolean- "Direct link to scrollwaitboolean-")

Whether or not to wait for the element, then scroll to it

#### [`scroll.x`](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#scrollxfloat- "Direct link to scrollxfloat-")

The X coordinate, in pixels, to scroll to

#### [`scroll.y`](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#scrollyfloat- "Direct link to scrollyfloat-")

The Y coordinate, in pixels, to scroll to

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#type "Direct link to Type")

#### [`ScrollResponse`](https://docs.browserless.io/bql-schema/types/objects/scroll-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/scroll\#scrollresponse- "Direct link to scrollresponse-")

Response returned after having scrolling inside the page

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/scroll#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/scroll#type)