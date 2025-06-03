---
url: "https://pptr.dev/next/api/puppeteer.browser.setcookie"
title: "Browser.setCookie() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.setcookie#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.setcookie)** (24.9.0).

Version: Next

On this page

Sets cookies in the default [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.setcookie\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  setCookie(...cookies: CookieData[]): Promise<void>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.browser.setcookie\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| cookies | [CookieData](https://pptr.dev/next/api/puppeteer.cookiedata)\[\] |  |

**Returns:**

Promise<void>

## Remarks [​](https://pptr.dev/next/api/puppeteer.browser.setcookie\#remarks "Direct link to Remarks")

Shortcut for [browser.defaultBrowserContext().setCookie()](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.setcookie#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.setcookie#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.setcookie#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!