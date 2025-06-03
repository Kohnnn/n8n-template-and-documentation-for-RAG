---
url: "https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget"
title: "BrowserContext.waitForTarget() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.waitfortarget)** (24.9.0).

Version: Next

On this page

Waits until a [target](https://pptr.dev/next/api/puppeteer.target) matching the given `predicate` appears and returns it.

This will look all open [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [​](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  waitForTarget(
    predicate: (x: Target) => boolean | Promise<boolean>,
    options?: WaitForTargetOptions,
  ): Promise<Target>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| predicate | (x: [Target](https://pptr.dev/next/api/puppeteer.target)) =\> boolean \| Promise<boolean> |  |
| options | [WaitForTargetOptions](https://pptr.dev/next/api/puppeteer.waitfortargetoptions) | _(Optional)_ |

**Returns:**

Promise< [Target](https://pptr.dev/next/api/puppeteer.target) >

## Example [​](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget\#example "Direct link to Example")

Finding a target for a page opened via `window.open`:

```codeBlockLines_RjmQ
await page.evaluate(() => window.open('https://www.example.com/'));
const newWindowTarget = await browserContext.waitForTarget(
  target => target.url() === 'https://www.example.com/',
);

```

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!