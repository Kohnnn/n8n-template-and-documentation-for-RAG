---
url: "https://pptr.dev/next/api/puppeteer.consolemessage"
title: "ConsoleMessage class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.consolemessage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.consolemessage)** (24.9.0).

Version: Next

On this page

ConsoleMessage objects are dispatched by page via the 'console' event.

### Signature [​](https://pptr.dev/next/api/puppeteer.consolemessage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class ConsoleMessage

```

## Remarks [​](https://pptr.dev/next/api/puppeteer.consolemessage\#remarks "Direct link to Remarks")

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `ConsoleMessage` class.

## Methods [​](https://pptr.dev/next/api/puppeteer.consolemessage\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [args()](https://pptr.dev/next/api/puppeteer.consolemessage.args) |  | An array of arguments passed to the console. |
| [location()](https://pptr.dev/next/api/puppeteer.consolemessage.location) |  | The location of the console message. |
| [stackTrace()](https://pptr.dev/next/api/puppeteer.consolemessage.stacktrace) |  | The array of locations on the stack of the console message. |
| [text()](https://pptr.dev/next/api/puppeteer.consolemessage.text) |  | The text of the console message. |
| [type()](https://pptr.dev/next/api/puppeteer.consolemessage.type) |  | The type of the console message. |

- [Signature](https://pptr.dev/next/api/puppeteer.consolemessage#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.consolemessage#remarks)
- [Methods](https://pptr.dev/next/api/puppeteer.consolemessage#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!