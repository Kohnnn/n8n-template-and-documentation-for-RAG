---
url: "https://pptr.dev/next/api/puppeteer.browser.uninstallextension"
title: "Browser.uninstallExtension() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.uninstallextension#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.uninstallextension)** (24.9.0).

Version: Next

On this page

Uninstalls an extension. In Chrome, this is only available if the browser was created using `pipe: true` and the `--enable-unsafe-extension-debugging` flag is set.

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.uninstallextension\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract uninstallExtension(id: string): Promise<void>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.browser.uninstallextension\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| id | string |  |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.uninstallextension#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.uninstallextension#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!