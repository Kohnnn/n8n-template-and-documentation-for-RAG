---
url: "https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel"
title: "ElementHandle.boxModel() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.boxmodel)** (24.9.0).

Version: Next

On this page

This method returns boxes of the element, or `null` if the element is [not part of the layout](https://drafts.csswg.org/css-display-4/#box-generation) (example: `display: none`).

### Signature [​](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  boxModel(): Promise<BoxModel | null>;
}

```

**Returns:**

Promise< [BoxModel](https://pptr.dev/next/api/puppeteer.boxmodel) \| null>

## Remarks [​](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel\#remarks "Direct link to Remarks")

Boxes are represented as an array of points; Each Point is an object `{x, y}`. Box points are sorted clock-wise.

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!