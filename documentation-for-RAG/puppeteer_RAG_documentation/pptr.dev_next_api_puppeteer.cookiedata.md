---
url: "https://pptr.dev/next/api/puppeteer.cookiedata"
title: "CookieData interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookiedata#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookiedata)** (24.9.0).

Version: Next

On this page

Cookie parameter object used to set cookies in the browser-level cookies API.

### Signature [​](https://pptr.dev/next/api/puppeteer.cookiedata\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CookieData

```

## Properties [​](https://pptr.dev/next/api/puppeteer.cookiedata\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| domain |  | string | Cookie domain. |  |
| expires | `optional` | number | Cookie expiration date, session cookie if not set |  |
| httpOnly | `optional` | boolean | True if cookie is http-only. |  |
| name |  | string | Cookie name. |  |
| partitionKey | `optional` | [CookiePartitionKey](https://pptr.dev/next/api/puppeteer.cookiepartitionkey) \| string | Cookie partition key. In Chrome, it matches the top-level site the partitioned cookie is available in. In Firefox, it matches the source origin in the [PartitionKey](https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey). |  |
| path | `optional` | string | Cookie path. |  |
| priority | `optional` | [CookiePriority](https://pptr.dev/next/api/puppeteer.cookiepriority) | Cookie Priority. Supported only in Chrome. |  |
| sameParty | `optional` | boolean | True if cookie is SameParty. Supported only in Chrome. |  |
| sameSite | `optional` | [CookieSameSite](https://pptr.dev/next/api/puppeteer.cookiesamesite) | Cookie SameSite type. |  |
| secure | `optional` | boolean | True if cookie is secure. |  |
| sourceScheme | `optional` | [CookieSourceScheme](https://pptr.dev/next/api/puppeteer.cookiesourcescheme) | Cookie source scheme type. Supported only in Chrome. |  |
| value |  | string | Cookie value. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cookiedata#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.cookiedata#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!