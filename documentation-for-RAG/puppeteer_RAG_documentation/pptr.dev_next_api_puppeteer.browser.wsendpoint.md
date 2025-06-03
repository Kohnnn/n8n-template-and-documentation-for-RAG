---
url: "https://pptr.dev/next/api/puppeteer.browser.wsendpoint"
title: "Browser.wsEndpoint() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.wsendpoint#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.wsendpoint)** (24.9.0).

Version: Next

On this page

Gets the WebSocket URL to connect to this [browser](https://pptr.dev/next/api/puppeteer.browser).

This is usually used with [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect).

You can find the debugger URL ( `webSocketDebuggerUrl`) from `http://HOST:PORT/json/version`.

See [browser endpoint](https://chromedevtools.github.io/devtools-protocol/#how-do-i-access-the-browser-target) for more information.

### Signature [​](https://pptr.dev/next/api/puppeteer.browser.wsendpoint\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract wsEndpoint(): string;
}

```

**Returns:**

string

## Remarks [​](https://pptr.dev/next/api/puppeteer.browser.wsendpoint\#remarks "Direct link to Remarks")

The format is always `ws://HOST:PORT/devtools/browser/<id>`.

- [Signature](https://pptr.dev/next/api/puppeteer.browser.wsendpoint#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.wsendpoint#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!