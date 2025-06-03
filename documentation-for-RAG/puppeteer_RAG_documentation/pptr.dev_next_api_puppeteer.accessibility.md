---
url: "https://pptr.dev/next/api/puppeteer.accessibility"
title: "Accessibility class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.accessibility#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.accessibility)** (24.9.0).

Version: Next

On this page

The Accessibility class provides methods for inspecting the browser's accessibility tree. The accessibility tree is used by assistive technology such as [screen readers](https://en.wikipedia.org/wiki/Screen_reader) or [switches](https://en.wikipedia.org/wiki/Switch_access).

### Signature [​](https://pptr.dev/next/api/puppeteer.accessibility\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class Accessibility

```

## Remarks [​](https://pptr.dev/next/api/puppeteer.accessibility\#remarks "Direct link to Remarks")

Accessibility is a very platform-specific thing. On different platforms, there are different screen readers that might have wildly different output.

Blink - Chrome's rendering engine - has a concept of "accessibility tree", which is then translated into different platform-specific APIs. Accessibility namespace gives users access to the Blink Accessibility Tree.

Most of the accessibility tree gets filtered out when converting from Blink AX Tree to Platform-specific AX-Tree or by assistive technologies themselves. By default, Puppeteer tries to approximate this filtering, exposing only the "interesting" nodes of the tree.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Accessibility` class.

## Methods [​](https://pptr.dev/next/api/puppeteer.accessibility\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [snapshot(options)](https://pptr.dev/next/api/puppeteer.accessibility.snapshot) |  | Captures the current state of the accessibility tree. The returned object represents the root accessible node of the page.<br>**Remarks:**<br>**NOTE** The Chrome accessibility tree contains nodes that go unused on most platforms and by most screen readers. Puppeteer will discard them as well for an easier to process tree, unless `interestingOnly` is set to `false`. |

- [Signature](https://pptr.dev/next/api/puppeteer.accessibility#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.accessibility#remarks)
- [Methods](https://pptr.dev/next/api/puppeteer.accessibility#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!