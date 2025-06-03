---
url: "https://pptr.dev/next/api/puppeteer.connection"
title: "Connection class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.connection\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class Connection extends EventEmitter<CDPSessionEvents>

```

**Extends:** [EventEmitter](https://pptr.dev/next/api/puppeteer.eventemitter) < [CDPSessionEvents](https://pptr.dev/next/api/puppeteer.cdpsessionevents) >

## Constructors [​](https://pptr.dev/next/api/puppeteer.connection\#constructors "Direct link to Constructors")

| Constructor | Modifiers | Description |
| --- | --- | --- |
| [(constructor)(url, transport, delay, timeout, rawErrors)](https://pptr.dev/next/api/puppeteer.connection._constructor_) |  | Constructs a new instance of the `Connection` class |

## Properties [​](https://pptr.dev/next/api/puppeteer.connection\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| timeout | `readonly` | number |  |

## Methods [​](https://pptr.dev/next/api/puppeteer.connection\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [createSession(targetInfo)](https://pptr.dev/next/api/puppeteer.connection.createsession) |  |  |
| [dispose()](https://pptr.dev/next/api/puppeteer.connection.dispose) |  |  |
| [fromSession(session)](https://pptr.dev/next/api/puppeteer.connection.fromsession) | `static` |  |
| [send(method, params, options)](https://pptr.dev/next/api/puppeteer.connection.send) |  |  |
| [session(sessionId)](https://pptr.dev/next/api/puppeteer.connection.session) |  |  |
| [url()](https://pptr.dev/next/api/puppeteer.connection.url) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.connection#signature)
- [Constructors](https://pptr.dev/next/api/puppeteer.connection#constructors)
- [Properties](https://pptr.dev/next/api/puppeteer.connection#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.connection#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!