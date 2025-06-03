---
url: "https://pptr.dev/next/api/puppeteer.commoneventemitter.on"
title: "CommonEventEmitter.on() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.on#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.on)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.commoneventemitter.on\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  on<Key extends keyof Events>(type: Key, handler: Handler<Events[Key]>): this;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.commoneventemitter.on\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| type | Key |  |
| handler | [Handler](https://pptr.dev/next/api/puppeteer.handler) <Events\[Key\]> |  |

**Returns:**

this

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.on#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.on#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!