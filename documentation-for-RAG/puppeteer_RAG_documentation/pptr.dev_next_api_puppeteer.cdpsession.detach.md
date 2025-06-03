---
url: "https://pptr.dev/next/api/puppeteer.cdpsession.detach"
title: "CDPSession.detach() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsession.detach#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsession.detach)** (24.9.0).

Version: Next

On this page

Detaches the cdpSession from the target. Once detached, the cdpSession object won't emit any events and can't be used to send messages.

### Signature [​](https://pptr.dev/next/api/puppeteer.cdpsession.detach\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class CDPSession {
  abstract detach(): Promise<void>;
}

```

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsession.detach#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!