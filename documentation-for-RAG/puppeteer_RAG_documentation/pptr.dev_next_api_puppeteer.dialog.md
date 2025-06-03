---
url: "https://pptr.dev/next/api/puppeteer.dialog"
title: "Dialog class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.dialog#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.dialog)** (24.9.0).

Version: Next

On this page

Dialog instances are dispatched by the [Page](https://pptr.dev/next/api/puppeteer.page) via the `dialog` event.

### Signature [​](https://pptr.dev/next/api/puppeteer.dialog\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class Dialog

```

## Remarks [​](https://pptr.dev/next/api/puppeteer.dialog\#remarks "Direct link to Remarks")

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Dialog` class.

## Example [​](https://pptr.dev/next/api/puppeteer.dialog\#example "Direct link to Example")

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  page.on('dialog', async dialog => {
    console.log(dialog.message());
    await dialog.dismiss();
    await browser.close();
  });
  page.evaluate(() => alert('1'));
})();

```

## Methods [​](https://pptr.dev/next/api/puppeteer.dialog\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [accept(promptText)](https://pptr.dev/next/api/puppeteer.dialog.accept) |  | A promise that resolves when the dialog has been accepted. |
| [defaultValue()](https://pptr.dev/next/api/puppeteer.dialog.defaultvalue) |  | The default value of the prompt, or an empty string if the dialog is not a `prompt`. |
| [dismiss()](https://pptr.dev/next/api/puppeteer.dialog.dismiss) |  | A promise which will resolve once the dialog has been dismissed |
| [message()](https://pptr.dev/next/api/puppeteer.dialog.message) |  | The message displayed in the dialog. |
| [type()](https://pptr.dev/next/api/puppeteer.dialog.type) |  | The type of the dialog. |

- [Signature](https://pptr.dev/next/api/puppeteer.dialog#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.dialog#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.dialog#example)
- [Methods](https://pptr.dev/next/api/puppeteer.dialog#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!