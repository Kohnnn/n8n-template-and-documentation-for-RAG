---
url: "https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions"
title: "BrowserContext.overridePermissions() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.overridepermissions)** (24.9.0).

Version: Next

On this page

Grants this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) the given `permissions` within the given `origin`.

### Signature [​](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract overridePermissions(
    origin: string,
    permissions: Permission[],
  ): Promise<void>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| origin | string | The origin to grant permissions to, e.g. " [https://example.com](https://example.com/)". |
| permissions | [Permission](https://pptr.dev/next/api/puppeteer.permission)\[\] | An array of permissions to grant. All permissions that are not listed here will be automatically denied. |

**Returns:**

Promise<void>

## Example [​](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions\#example "Direct link to Example")

Overriding permissions in the [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext):

```codeBlockLines_RjmQ
const context = browser.defaultBrowserContext();
await context.overridePermissions('https://html5demos.com', ['geolocation']);

```

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!