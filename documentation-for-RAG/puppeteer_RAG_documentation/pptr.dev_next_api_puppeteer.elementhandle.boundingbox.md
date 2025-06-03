---
url: "https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox"
title: "ElementHandle.boundingBox() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.boundingbox)** (24.9.0).

Version: Next

On this page

This method returns the bounding box of the element (relative to the main frame), or `null` if the element is [not part of the layout](https://drafts.csswg.org/css-display-4/#box-generation) (example: `display: none`).

### Signature [​](https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  boundingBox(): Promise<BoundingBox | null>;
}

```

**Returns:**

Promise< [BoundingBox](https://pptr.dev/next/api/puppeteer.boundingbox) \| null>

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!