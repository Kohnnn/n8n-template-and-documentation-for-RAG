---
url: "https://pptr.dev/next/api/puppeteer.cookie"
title: "Cookie interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookie#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookie)** (24.9.0).

Version: Next

On this page

Represents a cookie object.

### Signature [​](https://pptr.dev/next/api/puppeteer.cookie\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface Cookie extends CookieData

```

**Extends:** [CookieData](https://pptr.dev/next/api/puppeteer.cookiedata)

## Properties [​](https://pptr.dev/next/api/puppeteer.cookie\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| domain |  | string | Cookie domain. |  |
| expires |  | number | Cookie expiration date as the number of seconds since the UNIX epoch. Set to `-1` for session cookies |  |
| httpOnly |  | boolean | True if cookie is http-only. |  |
| name |  | string | Cookie name. |  |
| partitionKey | `optional` | [CookiePartitionKey](https://pptr.dev/next/api/puppeteer.cookiepartitionkey) \| string | Cookie partition key. In Chrome, it is the top-level site the partitioned cookie is available in. In Firefox, it matches the source origin in the [PartitionKey](https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey). |  |
| partitionKeyOpaque | `optional` | boolean | True if cookie partition key is opaque. Supported only in Chrome. |  |
| path |  | string | Cookie path. |  |
| priority | `optional` | [CookiePriority](https://pptr.dev/next/api/puppeteer.cookiepriority) | Cookie Priority. Supported only in Chrome. |  |
| sameParty | `optional` | boolean | True if cookie is SameParty. Supported only in Chrome. |  |
| sameSite | `optional` | [CookieSameSite](https://pptr.dev/next/api/puppeteer.cookiesamesite) | Cookie SameSite type. |  |
| secure |  | boolean | True if cookie is secure. |  |
| session |  | boolean | True in case of session cookie. |  |
| size |  | number | Cookie size. |  |
| sourceScheme | `optional` | [CookieSourceScheme](https://pptr.dev/next/api/puppeteer.cookiesourcescheme) | Cookie source scheme type. Supported only in Chrome. |  |
| value |  | string | Cookie value. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cookie#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.cookie#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!