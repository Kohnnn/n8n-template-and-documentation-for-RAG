---
url: "https://docs.browserless.io/bql-schema/operations/mutations/click"
title: "click | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/click#__docusaurus_skipToContent_fallback)

On this page

Waits for the element to be visible, scrolls to it, then clicks on it with native events

Example:

```codeBlockLines_p187
mutation ClickButton {
  goto(url: "https://example.com") {
    status
  }

  click(selector: "a") {
    time
  }
}

```

```codeBlockLines_p187
click(
  selector: String!
  scroll: Boolean = true
  timeout: Float
  visible: Boolean = false
  wait: Boolean = true
): ClickResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/click\#arguments "Direct link to Arguments")

#### [`click.selector`](https://docs.browserless.io/bql-schema/operations/mutations/click\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/click\#clickselectorstring-- "Direct link to clickselectorstring--")

A query-selector compatible string, JavaScript that returns an HTML Node, OR a Browserless-deep query. Examples include:

- A simple `<button />` Element:
`selector: "button"`

- A JavaScript snippet that returns a button element
`selector: "document.querySelector('button')"`

- A Browserless Deep query. These queries must start with a "<" character.
Deep queries will traverse all iframes, shadow-doms (open or closed), and more.
`selector: "< button"`


Here's a deep query that filters by iframes with a url of "example.com" and a button with a class of active
`selector: "< https://example.com/* button.active"`

#### [`click.scroll`](https://docs.browserless.io/bql-schema/operations/mutations/click\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/click\#clickscrollboolean- "Direct link to clickscrollboolean-")

Whether or not to scroll to the element prior to clicking, defaults to true

#### [`click.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/click\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/click\#clicktimeoutfloat- "Direct link to clicktimeoutfloat-")

How long to wait for the element to appear before timing out on the click handler, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`click.visible`](https://docs.browserless.io/bql-schema/operations/mutations/click\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/click\#clickvisibleboolean- "Direct link to clickvisibleboolean-")

Whether or not to click the element only if it's visible

#### [`click.wait`](https://docs.browserless.io/bql-schema/operations/mutations/click\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/click\#clickwaitboolean- "Direct link to clickwaitboolean-")

Whether or not to wait for the element to present in the DOM

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/click\#type "Direct link to Type")

#### [`ClickResponse`](https://docs.browserless.io/bql-schema/types/objects/click-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/click\#clickresponse- "Direct link to clickresponse-")

Response returned after having clicked on an element

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/click#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/click#type)