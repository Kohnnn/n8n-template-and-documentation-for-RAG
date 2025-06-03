---
url: "https://pptr.dev/next/api/puppeteer.browser.version"
title: "Browser.version() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.version#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.version)** (24.9.0).

Version: Next

On this page

Gets a string representing this [browser's](https://pptr.dev/next/api/puppeteer.browser) name and version.

For headless browser, this is similar to `"HeadlessChrome/61.0.3153.0"`. For non-headless or new-headless, this is similar to `"Chrome/61.0.3153.0"`. For Firefox, it is similar to `"Firefox/116.0a1"`.

The format of [Browser.version()](https://pptr.dev/next/api/puppeteer.browser.version) might change with future releases of browsers.

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.version\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract version(): Promise<string>;
}

```

**Returns:**

Promise<string>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.version#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!