---
url: "https://pptr.dev/next/api/puppeteer.browser.installextension"
title: "Browser.installExtension() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.installextension#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.installextension)** (24.9.0).

Version: Next

On this page

Installs an extension and returns the ID. In Chrome, this is only available if the browser was created using `pipe: true` and the `--enable-unsafe-extension-debugging` flag is set.

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.installextension\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract installExtension(path: string): Promise<string>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.browser.installextension\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| path | string |  |

**Returns:**

Promise<string>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.installextension#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.installextension#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!