---
url: "https://pptr.dev/next/api/puppeteer.browsercontextevent"
title: "BrowserContextEvent enum | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontextevent#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontextevent)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.browsercontextevent\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare const enum BrowserContextEvent

```

## Enumeration Members [​](https://pptr.dev/next/api/puppeteer.browsercontextevent\#enumeration-members "Direct link to Enumeration Members")

| Member | Value | Description |
| --- | --- | --- |
| TargetChanged | `"targetchanged"` | Emitted when the url of a target inside the browser context changes. Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance. |
| TargetCreated | `"targetcreated"` | Emitted when a target is created within the browser context, for example when a new page is opened by [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) or by [browserContext.newPage](https://pptr.dev/next/api/puppeteer.browsercontext.newpage)<br>Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance. |
| TargetDestroyed | `"targetdestroyed"` | Emitted when a target is destroyed within the browser context, for example when a page is closed. Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance. |

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontextevent#signature)
- [Enumeration Members](https://pptr.dev/next/api/puppeteer.browsercontextevent#enumeration-members)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!