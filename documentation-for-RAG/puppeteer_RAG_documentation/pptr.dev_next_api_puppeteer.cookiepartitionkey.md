---
url: "https://pptr.dev/next/api/puppeteer.cookiepartitionkey"
title: "CookiePartitionKey interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookiepartitionkey#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookiepartitionkey)** (24.9.0).

Version: Next

On this page

Represents a cookie partition key in Chrome.

### Signature [​](https://pptr.dev/next/api/puppeteer.cookiepartitionkey\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CookiePartitionKey

```

## Properties [​](https://pptr.dev/next/api/puppeteer.cookiepartitionkey\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| hasCrossSiteAncestor | `optional` | boolean | Indicates if the cookie has any ancestors that are cross-site to the topLevelSite.<br>Supported only in Chrome. |  |
| sourceOrigin |  | string | The site of the top-level URL the browser was visiting at the start of the request to the endpoint that set the cookie.<br>In Chrome, maps to the CDP's `topLevelSite` partition key. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cookiepartitionkey#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.cookiepartitionkey#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!