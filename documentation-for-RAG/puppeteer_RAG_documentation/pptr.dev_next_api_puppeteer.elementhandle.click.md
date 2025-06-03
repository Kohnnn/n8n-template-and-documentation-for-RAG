---
url: "https://pptr.dev/next/api/puppeteer.elementhandle.click"
title: "ElementHandle.click() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.click#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.click)** (24.9.0).

Version: Next

On this page

This method scrolls element into view if needed, and then uses [Page.mouse](https://pptr.dev/next/api/puppeteer.page#mouse) to click in the center of the element. If the element is detached from DOM, the method throws an error.

### Signature [​](https://pptr.dev/next/api/puppeteer.elementhandle.click\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  click(
    this: ElementHandle<Element>,
    options?: Readonly<ClickOptions>,
  ): Promise<void>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.elementhandle.click\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| this | [ElementHandle](https://pptr.dev/next/api/puppeteer.elementhandle) <Element> |  |
| options | Readonly< [ClickOptions](https://pptr.dev/next/api/puppeteer.clickoptions) > | _(Optional)_ |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.click#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.click#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!