---
url: "https://docs.browserless.io/bql-schema/operations/mutations/type"
title: "type | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/type#__docusaurus_skipToContent_fallback)

On this page

Types text into an element by scrolling to it, clicking it, then emitting key events for every character

Example:

```codeBlockLines_p187
mutation Type {
  goto(url: "https://example.com") {
    status
  }

  type(
    text: "Hello, World!"
    selector: "input[type='text']"
  ) {
    time
  }
}

```

```codeBlockLines_p187
type(
  text: String!
  selector: String!
  delay: [Int] = [50, 200]
  interactable: Boolean = true
  scroll: Boolean = true
  timeout: Float
  visible: Boolean = false
  wait: Boolean = true
): TypeResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#arguments "Direct link to Arguments")

#### [`type.text`](https://docs.browserless.io/bql-schema/operations/mutations/type\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#typetextstring-- "Direct link to typetextstring--")

The text content you want to type into the element

#### [`type.selector`](https://docs.browserless.io/bql-schema/operations/mutations/type\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#typeselectorstring-- "Direct link to typeselectorstring--")

The CSS selector of the element on the page you want to type text into

#### [`type.delay`](https://docs.browserless.io/bql-schema/operations/mutations/type\#) ● [`[Int]`](https://docs.browserless.io/bql-schema/types/scalars/int) listscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#typedelayint-- "Direct link to typedelayint--")

The amount of delay between keystrokes in milliseconds. Values are used as a range and chosen at random

#### [`type.interactable`](https://docs.browserless.io/bql-schema/operations/mutations/type\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#typeinteractableboolean- "Direct link to typeinteractableboolean-")

Whether or not to check if element can be interacted with by hovering over it and seeing if the element
is available at that x and y position

#### [`type.scroll`](https://docs.browserless.io/bql-schema/operations/mutations/type\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#typescrollboolean- "Direct link to typescrollboolean-")

Whether or not to scroll to the element prior to typing, defaults to true

#### [`type.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/type\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#typetimeoutfloat- "Direct link to typetimeoutfloat-")

How long to wait for the element to appear before timing out, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`type.visible`](https://docs.browserless.io/bql-schema/operations/mutations/type\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#typevisibleboolean- "Direct link to typevisibleboolean-")

Whether or not to type into the element only if it's visible

#### [`type.wait`](https://docs.browserless.io/bql-schema/operations/mutations/type\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#typewaitboolean- "Direct link to typewaitboolean-")

Whether or not to wait for the element to present in the DOM

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#type "Direct link to Type")

#### [`TypeResponse`](https://docs.browserless.io/bql-schema/types/objects/type-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/type\#typeresponse- "Direct link to typeresponse-")

Response returned after having typed into an element

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/type#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/type#type)