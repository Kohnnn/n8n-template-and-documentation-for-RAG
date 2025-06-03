---
url: "https://pptr.dev/next/api/puppeteer.elementhandle.__"
title: "ElementHandle.$$() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.__#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.__)** (24.9.0).

Version: Next

On this page

Queries the current element for all elements matching the given selector.

### Signature [​](https://pptr.dev/next/api/puppeteer.elementhandle.__\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  $$<Selector extends string>(
    selector: Selector,
    options?: QueryOptions,
  ): Promise<Array<ElementHandle<NodeFor<Selector>>>>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.elementhandle.__\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| selector | Selector | [selector](https://pptr.dev/guides/page-interactions#selectors) to query the page for. [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) can be passed as-is and a [Puppeteer-specific selector syntax](https://pptr.dev/guides/page-interactions#non-css-selectors) allows querying by [text](https://pptr.dev/guides/page-interactions#text-selectors--p-text), [a11y role and name](https://pptr.dev/guides/page-interactions#aria-selectors--p-aria), and [xpath](https://pptr.dev/guides/page-interactions#xpath-selectors--p-xpath) and [combining these queries across shadow roots](https://pptr.dev/guides/page-interactions#querying-elements-in-shadow-dom). Alternatively, you can specify the selector type using a [prefix](https://pptr.dev/guides/page-interactions#prefixed-selector-syntax). |
| options | [QueryOptions](https://pptr.dev/next/api/puppeteer.queryoptions) | _(Optional)_ |

**Returns:**

Promise<Array< [ElementHandle](https://pptr.dev/next/api/puppeteer.elementhandle) < [NodeFor](https://pptr.dev/next/api/puppeteer.nodefor) <Selector>>>>

An array of [element handles](https://pptr.dev/next/api/puppeteer.elementhandle) that point to elements matching the given selector.

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.__#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.__#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!