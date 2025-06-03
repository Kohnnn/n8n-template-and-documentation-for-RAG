---
url: "https://pptr.dev/next/api/puppeteer.browser.pages"
title: "Browser.pages() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.pages#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.pages)** (24.9.0).

Version: Next

On this page

Gets a list of all open [pages](https://pptr.dev/next/api/puppeteer.page) inside this [Browser](https://pptr.dev/next/api/puppeteer.browser).

If there are multiple [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext), this returns all [pages](https://pptr.dev/next/api/puppeteer.page) in all [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.pages\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  pages(): Promise<Page[]>;
}

```

**Returns:**

Promise< [Page](https://pptr.dev/next/api/puppeteer.page)\[\]>

## Remarks [​](https://pptr.dev/next/api/puppeteer.browser.pages\#remarks "Direct link to Remarks")

Non-visible [pages](https://pptr.dev/next/api/puppeteer.page), such as `"background_page"`, will not be listed here. You can find them using [Target.page()](https://pptr.dev/next/api/puppeteer.target.page).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.pages#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.pages#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!