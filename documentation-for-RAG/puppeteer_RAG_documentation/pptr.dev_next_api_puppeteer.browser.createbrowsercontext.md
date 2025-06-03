---
url: "https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext"
title: "Browser.createBrowserContext() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.createbrowsercontext)** (24.9.0).

Version: Next

On this page

Creates a new [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).

This won't share cookies/cache with other [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract createBrowserContext(
    options?: BrowserContextOptions,
  ): Promise<BrowserContext>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [BrowserContextOptions](https://pptr.dev/next/api/puppeteer.browsercontextoptions) | _(Optional)_ |

**Returns:**

Promise< [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext) >

## Example [​](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext\#example "Direct link to Example")

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch();
// Create a new browser context.
const context = await browser.createBrowserContext();
// Create a new page in a pristine context.
const page = await context.newPage();
// Do stuff
await page.goto('https://example.com');

```

- [Signature](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!