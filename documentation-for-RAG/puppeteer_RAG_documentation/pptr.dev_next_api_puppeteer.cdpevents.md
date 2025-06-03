---
url: "https://pptr.dev/next/api/puppeteer.cdpevents"
title: "CDPEvents type | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpevents#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpevents)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.cdpevents\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type CDPEvents = {
  [Property in keyof ProtocolMapping.Events]: ProtocolMapping.Events[Property][0];
};

```

- [Signature](https://pptr.dev/next/api/puppeteer.cdpevents#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!