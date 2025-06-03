---
url: "https://pptr.dev/next/api/puppeteer.commoneventemitter.emit"
title: "CommonEventEmitter.emit() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.emit)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  emit<Key extends keyof Events>(type: Key, event: Events[Key]): boolean;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| type | Key |  |
| event | Events\[Key\] |  |

**Returns:**

boolean

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!