---
url: "https://pptr.dev/next/api/puppeteer.browsercontextoptions"
title: "BrowserContextOptions interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontextoptions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontextoptions)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.browsercontextoptions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface BrowserContextOptions

```

## Properties [​](https://pptr.dev/next/api/puppeteer.browsercontextoptions\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| downloadBehavior | `optional` | [DownloadBehavior](https://pptr.dev/next/api/puppeteer.downloadbehavior) | Behavior definition for when downloading a file.<br>**Remarks:**<br>If not set, the default behavior will be used. |  |
| proxyBypassList | `optional` | string\[\] | Bypass the proxy for the given list of hosts. |  |
| proxyServer | `optional` | string | Proxy server with optional port to use for all requests. Username and password can be set in `Page.authenticate`. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontextoptions#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.browsercontextoptions#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!