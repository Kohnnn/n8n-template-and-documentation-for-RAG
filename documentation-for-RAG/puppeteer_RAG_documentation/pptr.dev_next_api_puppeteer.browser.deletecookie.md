---
url: "https://pptr.dev/next/api/puppeteer.browser.deletecookie"
title: "Browser.deleteCookie() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.deletecookie#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.deletecookie)** (24.9.0).

Version: Next

On this page

Removes cookies from the default [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.deletecookie\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  deleteCookie(...cookies: Cookie[]): Promise<void>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.browser.deletecookie\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| cookies | [Cookie](https://pptr.dev/next/api/puppeteer.cookie)\[\] |  |

**Returns:**

Promise<void>

## Remarks [​](https://pptr.dev/next/api/puppeteer.browser.deletecookie\#remarks "Direct link to Remarks")

Shortcut for [browser.defaultBrowserContext().deleteCookie()](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.deletecookie#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.deletecookie#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.deletecookie#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!