---
url: "https://pptr.dev/next/api/puppeteer.connection.createsession"
title: "Connection.createSession() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection.createsession#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection.createsession)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.connection.createsession\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Connection {
  createSession(targetInfo: Protocol.Target.TargetInfo): Promise<CDPSession>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.connection.createsession\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| targetInfo | Protocol.Target.TargetInfo | The target info |

**Returns:**

Promise< [CDPSession](https://pptr.dev/next/api/puppeteer.cdpsession) >

The CDP session that is created

- [Signature](https://pptr.dev/next/api/puppeteer.connection.createsession#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.connection.createsession#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!