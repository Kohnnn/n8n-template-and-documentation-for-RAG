---
url: "https://pptr.dev/next/api/puppeteer.connectoptions"
title: "ConnectOptions interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.connectoptions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connectoptions)** (24.9.0).

Version: Next

On this page

Generic browser options that can be passed when launching any browser or when connecting to an existing browser instance.

### Signature [​](https://pptr.dev/next/api/puppeteer.connectoptions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ConnectOptions

```

## Properties [​](https://pptr.dev/next/api/puppeteer.connectoptions\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| acceptInsecureCerts | `optional` | boolean | Whether to ignore HTTPS errors during navigation. | `false` |
| browserURL | `optional` | string |  |  |
| browserWSEndpoint | `optional` | string |  |  |
| capabilities | `optional` | [SupportedWebDriverCapabilities](https://pptr.dev/next/api/puppeteer.supportedwebdrivercapabilities) | WebDriver BiDi capabilities passed to BiDi `session.new`.<br>**Remarks:**<br>Only works for `protocol="webDriverBiDi"` and [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect). |  |
| defaultViewport | `optional` | [Viewport](https://pptr.dev/next/api/puppeteer.viewport) \| null | Sets the viewport for each page. | '{width: 800, height: 600}' |
| downloadBehavior | `optional` | [DownloadBehavior](https://pptr.dev/next/api/puppeteer.downloadbehavior) | Sets the download behavior for the context. |  |
| headers | `optional` | Record<string, string> | Headers to use for the web socket connection.<br>**Remarks:**<br>Only works in the Node.js environment. |  |
| protocol | `optional` | [ProtocolType](https://pptr.dev/next/api/puppeteer.protocoltype) |  | Determined at run time:<br>- Launching Chrome - 'cdp'.<br>  <br>- Launching Firefox - 'webDriverBiDi'.<br>  <br>- Connecting to a browser - 'cdp'. |
| protocolTimeout | `optional` | number | Timeout setting for individual protocol (CDP) calls. | `180_000` |
| slowMo | `optional` | number | Slows down Puppeteer operations by the specified amount of milliseconds to aid debugging. |  |
| targetFilter | `optional` | [TargetFilterCallback](https://pptr.dev/next/api/puppeteer.targetfiltercallback) | Callback to decide if Puppeteer should connect to a given target or not. |  |
| transport | `optional` | [ConnectionTransport](https://pptr.dev/next/api/puppeteer.connectiontransport) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.connectoptions#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.connectoptions#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!