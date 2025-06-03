---
url: "https://pptr.dev/next/api/puppeteer.browser.useragent"
title: "Browser.userAgent() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.useragent#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.useragent)** (24.9.0).

Version: Next

On this page

Gets this [browser's](https://pptr.dev/next/api/puppeteer.browser) original user agent.

[Pages](https://pptr.dev/next/api/puppeteer.page) can override the user agent with [Page.setUserAgent()](https://pptr.dev/next/api/puppeteer.page.setuseragent).

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.useragent\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract userAgent(): Promise<string>;
}

```

**Returns:**

Promise<string>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.useragent#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!