---
url: "https://pptr.dev/next/api/puppeteer.commoneventemitter.once"
title: "CommonEventEmitter.once() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.once#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.once)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.commoneventemitter.once\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  once<Key extends keyof Events>(
    type: Key,
    handler: Handler<Events[Key]>,
  ): this;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.commoneventemitter.once\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| type | Key |  |
| handler | [Handler](https://pptr.dev/next/api/puppeteer.handler) <Events\[Key\]> |  |

**Returns:**

this

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.once#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.once#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!