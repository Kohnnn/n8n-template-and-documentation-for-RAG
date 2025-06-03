---
url: "https://pptr.dev/next/api/puppeteer.cdpsession"
title: "CDPSession class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsession#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsession)** (24.9.0).

Version: Next

On this page

The `CDPSession` instances are used to talk raw Chrome Devtools Protocol.

### Signature [​](https://pptr.dev/next/api/puppeteer.cdpsession\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class CDPSession extends EventEmitter<CDPSessionEvents>

```

**Extends:** [EventEmitter](https://pptr.dev/next/api/puppeteer.eventemitter) < [CDPSessionEvents](https://pptr.dev/next/api/puppeteer.cdpsessionevents) >

## Remarks [​](https://pptr.dev/next/api/puppeteer.cdpsession\#remarks "Direct link to Remarks")

Protocol methods can be called with [CDPSession.send()](https://pptr.dev/next/api/puppeteer.cdpsession.send) method and protocol events can be subscribed to with `CDPSession.on` method.

Useful links: [DevTools Protocol Viewer](https://chromedevtools.github.io/devtools-protocol/) and [Getting Started with DevTools Protocol](https://github.com/aslushnikov/getting-started-with-cdp/blob/HEAD/README.md).

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `CDPSession` class.

## Example [​](https://pptr.dev/next/api/puppeteer.cdpsession\#example "Direct link to Example")

```codeBlockLines_RjmQ
const client = await page.createCDPSession();
await client.send('Animation.enable');
client.on('Animation.animationCreated', () =>
  console.log('Animation created!'),
);
const response = await client.send('Animation.getPlaybackRate');
console.log('playback rate is ' + response.playbackRate);
await client.send('Animation.setPlaybackRate', {
  playbackRate: response.playbackRate / 2,
});

```

## Properties [​](https://pptr.dev/next/api/puppeteer.cdpsession\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| detached | `readonly` | boolean | True if the session has been detached, false otherwise. |

## Methods [​](https://pptr.dev/next/api/puppeteer.cdpsession\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [connection()](https://pptr.dev/next/api/puppeteer.cdpsession.connection) |  | The underlying connection for this session, if any. |
| [detach()](https://pptr.dev/next/api/puppeteer.cdpsession.detach) |  | Detaches the cdpSession from the target. Once detached, the cdpSession object won't emit any events and can't be used to send messages. |
| [id()](https://pptr.dev/next/api/puppeteer.cdpsession.id) |  | Returns the session's id. |
| [send(method, params, options)](https://pptr.dev/next/api/puppeteer.cdpsession.send) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsession#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.cdpsession#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.cdpsession#example)
- [Properties](https://pptr.dev/next/api/puppeteer.cdpsession#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.cdpsession#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!