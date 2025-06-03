---
url: "https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides"
title: "BrowserContext.clearPermissionOverrides() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.clearpermissionoverrides)** (24.9.0).

Version: Next

On this page

Clears all permission overrides for this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [​](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract clearPermissionOverrides(): Promise<void>;
}

```

**Returns:**

Promise<void>

## Example [​](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides\#example "Direct link to Example")

Clearing overridden permissions in the [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext):

```codeBlockLines_RjmQ
const context = browser.defaultBrowserContext();
context.overridePermissions('https://example.com', ['clipboard-read']);
// do stuff ..
context.clearPermissionOverrides();

```

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides#signature)
- [Example](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!