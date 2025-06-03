---
url: "https://pptr.dev/next/api/puppeteer.connection.send"
title: "Connection.send() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection.send#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection.send)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.connection.send\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Connection {
  send<T extends keyof ProtocolMapping.Commands>(
    method: T,
    params?: ProtocolMapping.Commands[T]['paramsType'][0],
    options?: CommandOptions,
  ): Promise<ProtocolMapping.Commands[T]['returnType']>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.connection.send\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| method | T |  |
| params | ProtocolMapping.Commands\[T\]\['paramsType'\]\[0\] | _(Optional)_ |
| options | [CommandOptions](https://pptr.dev/next/api/puppeteer.commandoptions) | _(Optional)_ |

**Returns:**

Promise<ProtocolMapping.Commands\[T\]\['returnType'\]>

- [Signature](https://pptr.dev/next/api/puppeteer.connection.send#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.connection.send#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!