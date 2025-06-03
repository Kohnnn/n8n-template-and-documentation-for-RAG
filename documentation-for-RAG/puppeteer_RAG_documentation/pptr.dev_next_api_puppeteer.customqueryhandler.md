---
url: "https://pptr.dev/next/api/puppeteer.customqueryhandler"
title: "CustomQueryHandler interface | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.customqueryhandler#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.customqueryhandler)** (24.9.0).

Version: Next

On this page

### Signature [​](https://pptr.dev/next/api/puppeteer.customqueryhandler\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CustomQueryHandler

```

## Properties [​](https://pptr.dev/next/api/puppeteer.customqueryhandler\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| queryAll | `optional` | (node: Node, selector: string) => Iterable<Node> | Searches for some [Nodes](https://developer.mozilla.org/en-US/docs/Web/API/Node) matching the given `selector` from [node](https://developer.mozilla.org/en-US/docs/Web/API/Node). |  |
| queryOne | `optional` | (node: Node, selector: string) => Node \| null | Searches for a [Node](https://developer.mozilla.org/en-US/docs/Web/API/Node) matching the given `selector` from [node](https://developer.mozilla.org/en-US/docs/Web/API/Node). |  |

- [Signature](https://pptr.dev/next/api/puppeteer.customqueryhandler#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.customqueryhandler#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!