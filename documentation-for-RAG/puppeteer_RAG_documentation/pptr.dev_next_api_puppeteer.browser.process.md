---
url: "https://pptr.dev/next/api/puppeteer.browser.process"
title: "Browser.process() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.process#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.process)** (24.9.0).

Version: Next

On this page

Gets the associated [ChildProcess](https://nodejs.org/api/child_process.html#class-childprocess).

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.process\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract process(): ChildProcess | null;
}

```

**Returns:**

ChildProcess \| null

`null` if this instance was connected to via [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.process#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!