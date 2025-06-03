---
url: "https://pptr.dev/next/api/puppeteer.elementhandle.contentframe"
title: "ElementHandle.contentFrame() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.contentframe)** (24.9.0).

Version: Next

On this page

## contentFrame(): Promise<Frame>

Resolves the frame associated with the element, if any. Always exists for HTMLIFrameElements.

### Signature [​](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  abstract contentFrame(this: ElementHandle<HTMLIFrameElement>): Promise<Frame>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| this | [ElementHandle](https://pptr.dev/next/api/puppeteer.elementhandle) <HTMLIFrameElement> |  |

**Returns:**

Promise< [Frame](https://pptr.dev/next/api/puppeteer.frame) >

## contentFrame(): Promise<Frame \| null>

### Signature [​](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe\#signature-1 "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  abstract contentFrame(): Promise<Frame | null>;
}

```

**Returns:**

Promise< [Frame](https://pptr.dev/next/api/puppeteer.frame) \| null>

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe#parameters)
  - [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe#signature-1)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!