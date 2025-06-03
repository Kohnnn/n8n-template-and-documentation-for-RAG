---
url: "https://docs.browserless.io/bql-schema/types/objects/wait-for-selector"
title: "WaitForSelector | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector#__docusaurus_skipToContent_fallback)

On this page

Response returned after a particular selector has been found in the DOM

```codeBlockLines_p187
type WaitForSelector {
  height: Float
  selector: String
  time: Float
  y: Float
  x: Float
  width: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#fields "Direct link to Fields")

#### [`WaitForSelector.height`](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#waitforselectorheightfloat- "Direct link to waitforselectorheightfloat-")

The height, in pixels, of the element

#### [`WaitForSelector.selector`](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#waitforselectorselectorstring- "Direct link to waitforselectorselectorstring-")

The selector waited for

#### [`WaitForSelector.time`](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#waitforselectortimefloat- "Direct link to waitforselectortimefloat-")

The period of time elapsed, in milliseconds, waited for

#### [`WaitForSelector.y`](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#waitforselectoryfloat- "Direct link to waitforselectoryfloat-")

The position, in pixels, top of the viewport

#### [`WaitForSelector.x`](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#waitforselectorxfloat- "Direct link to waitforselectorxfloat-")

The position, in pixels, left of the viewport

#### [`WaitForSelector.width`](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#waitforselectorwidthfloat- "Direct link to waitforselectorwidthfloat-")

The width, in pixels, of the element

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector\#returned-by "Direct link to Returned By")

[`waitForSelector`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-selector) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/wait-for-selector#returned-by)