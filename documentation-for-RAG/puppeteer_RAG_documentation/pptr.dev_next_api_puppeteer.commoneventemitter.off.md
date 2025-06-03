---
url: "https://pptr.dev/next/api/puppeteer.commoneventemitter.off"
title: "CommonEventEmitter.off() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.off#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.off)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.commoneventemitter.off\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  off<Key extends keyof Events>(
    type: Key,
    handler?: Handler<Events[Key]>,
  ): this;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.commoneventemitter.off\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| type | Key |  |
| handler | [Handler](https://pptr.dev/next/api/puppeteer.handler) <Events\[Key\]> | _(Optional)_ |

**Returns:**

this

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.off#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.off#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!