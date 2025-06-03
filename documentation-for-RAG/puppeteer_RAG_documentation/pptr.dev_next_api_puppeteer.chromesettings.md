---
url: "https://pptr.dev/next/api/puppeteer.chromesettings"
title: "ChromeSettings interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.chromesettings#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.chromesettings)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.chromesettings\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ChromeSettings

```

## Properties [​](https://pptr.dev/next/api/puppeteer.chromesettings\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| downloadBaseUrl | `optional` | string | Specifies the URL prefix that is used to download the browser.<br>Can be overridden by `PUPPETEER_CHROME_DOWNLOAD_BASE_URL`.<br>**Remarks:**<br>This must include the protocol and may even need a path prefix. This must **not** include a trailing slash similar to the default. | [https://storage.googleapis.com/chrome-for-testing-public](https://storage.googleapis.com/chrome-for-testing-public) |
| skipDownload | `optional` | boolean | Tells Puppeteer to not download the browser during installation.<br>Can be overridden by `PUPPETEER_CHROME_SKIP_DOWNLOAD`. | false |
| version | `optional` | string | Specifies a certain version of the browser you'd like Puppeteer to use.<br>Can be overridden by `PUPPETEER_CHROME_VERSION` or `PUPPETEER_SKIP_CHROME_DOWNLOAD`.<br>See [puppeteer.launch](https://pptr.dev/next/api/puppeteer.puppeteernode.launch) on how executable path is inferred. | The pinned browser version supported by the current Puppeteer version. |

- [Signature](https://pptr.dev/next/api/puppeteer.chromesettings#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.chromesettings#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!