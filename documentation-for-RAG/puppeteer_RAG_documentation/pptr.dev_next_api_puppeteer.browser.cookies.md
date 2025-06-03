---
url: "https://pptr.dev/next/api/puppeteer.browser.cookies"
title: "Browser.cookies() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.cookies#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.cookies)** (24.9.0).

Version: Next

On this page

Returns all cookies in the default [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.cookies\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  cookies(): Promise<Cookie[]>;
}

```

**Returns:**

Promise< [Cookie](https://pptr.dev/next/api/puppeteer.cookie)\[\]>

## Remarks [​](https://pptr.dev/next/api/puppeteer.browser.cookies\#remarks "Direct link to Remarks")

Shortcut for [browser.defaultBrowserContext().cookies()](https://pptr.dev/next/api/puppeteer.browsercontext.cookies).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.cookies#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.cookies#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!