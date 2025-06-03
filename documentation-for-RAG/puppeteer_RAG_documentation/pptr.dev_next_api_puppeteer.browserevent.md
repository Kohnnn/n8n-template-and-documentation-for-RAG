---
url: "https://pptr.dev/next/api/puppeteer.browserevent"
title: "BrowserEvent enum | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browserevent#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browserevent)** (24.9.0).

Version: Next

On this page

All the events a [browser instance](https://pptr.dev/next/api/puppeteer.browser) may emit.

### Signature [​](https://pptr.dev/next/api/puppeteer.browserevent\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare const enum BrowserEvent

```

## Enumeration Members [​](https://pptr.dev/next/api/puppeteer.browserevent\#enumeration-members "Direct link to Enumeration Members")

| Member | Value | Description |
| --- | --- | --- |
| Disconnected | `"disconnected"` | Emitted when Puppeteer gets disconnected from the browser instance. This might happen because either:<br>- The browser closes/crashes or - [Browser.disconnect()](https://pptr.dev/next/api/puppeteer.browser.disconnect) was called. |
| TargetChanged | `"targetchanged"` | Emitted when the URL of a target changes. Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance.<br>**Remarks:**<br>Note that this includes target changes in all browser contexts. |
| TargetCreated | `"targetcreated"` | Emitted when a target is created, for example when a new page is opened by [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) or by [browser.newPage](https://pptr.dev/next/api/puppeteer.browser.newpage)<br>Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance.<br>**Remarks:**<br>Note that this includes target creations in all browser contexts. |
| TargetDestroyed | `"targetdestroyed"` | Emitted when a target is destroyed, for example when a page is closed. Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance.<br>**Remarks:**<br>Note that this includes target destructions in all browser contexts. |

- [Signature](https://pptr.dev/next/api/puppeteer.browserevent#signature)
- [Enumeration Members](https://pptr.dev/next/api/puppeteer.browserevent#enumeration-members)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!