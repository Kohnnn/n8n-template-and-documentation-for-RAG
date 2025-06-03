---
url: "https://pptr.dev/next/api/puppeteer.deletecookiesrequest"
title: "DeleteCookiesRequest interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.deletecookiesrequest#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.deletecookiesrequest)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.deletecookiesrequest\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface DeleteCookiesRequest

```

## Properties [​](https://pptr.dev/next/api/puppeteer.deletecookiesrequest\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| domain | `optional` | string | If specified, deletes only cookies with the exact domain. |  |
| name |  | string | Name of the cookies to remove. |  |
| partitionKey | `optional` | [CookiePartitionKey](https://pptr.dev/next/api/puppeteer.cookiepartitionkey) \| string | If specified, deletes cookies in the given partition key. In Chrome, partitionKey matches the top-level site the partitioned cookie is available in. In Firefox, it matches the source origin in the [PartitionKey](https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey). |  |
| path | `optional` | string | If specified, deletes only cookies with the exact path. |  |
| url | `optional` | string | If specified, deletes all the cookies with the given name where domain and path match provided URL. Otherwise, deletes only cookies related to the current page's domain. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.deletecookiesrequest#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.deletecookiesrequest#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!