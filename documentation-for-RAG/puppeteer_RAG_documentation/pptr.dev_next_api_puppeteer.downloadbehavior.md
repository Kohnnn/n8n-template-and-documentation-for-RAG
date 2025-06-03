---
url: "https://pptr.dev/next/api/puppeteer.downloadbehavior"
title: "DownloadBehavior interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.downloadbehavior#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.downloadbehavior)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.downloadbehavior\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface DownloadBehavior

```

## Properties [​](https://pptr.dev/next/api/puppeteer.downloadbehavior\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| downloadPath | `optional` | string | The default path to save downloaded files to.<br>**Remarks:**<br>Setting this is required if behavior is set to `allow` or `allowAndName`. |  |
| policy |  | [DownloadPolicy](https://pptr.dev/next/api/puppeteer.downloadpolicy) | Whether to allow all or deny all download requests, or use default behavior if available.<br>**Remarks:**<br>Setting this to `allowAndName` will name all files according to their download guids. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.downloadbehavior#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.downloadbehavior#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!