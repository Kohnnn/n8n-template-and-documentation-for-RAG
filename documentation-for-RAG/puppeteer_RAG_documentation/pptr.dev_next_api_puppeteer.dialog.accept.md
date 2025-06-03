---
url: "https://pptr.dev/next/api/puppeteer.dialog.accept"
title: "Dialog.accept() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.dialog.accept#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.dialog.accept)** (24.9.0).

Version: Next

On this page

A promise that resolves when the dialog has been accepted.

### Signature [​](https://pptr.dev/next/api/puppeteer.dialog.accept\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Dialog {
  accept(promptText?: string): Promise<void>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.dialog.accept\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| promptText | string | _(Optional)_ optional text that will be entered in the dialog prompt. Has no effect if the dialog's type is not `prompt`. |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.dialog.accept#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.dialog.accept#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!