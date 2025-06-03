---
url: "https://pptr.dev/next/api/puppeteer.elementhandle.autofill"
title: "ElementHandle.autofill() method | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.autofill#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.autofill)** (24.9.0).

Version: Next

On this page

If the element is a form input, you can use [ElementHandle.autofill()](https://pptr.dev/next/api/puppeteer.elementhandle.autofill) to test if the form is compatible with the browser's autofill implementation. Throws an error if the form cannot be autofilled.

### Signature [​](https://pptr.dev/next/api/puppeteer.elementhandle.autofill\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  abstract autofill(data: AutofillData): Promise<void>;
}

```

## Parameters [​](https://pptr.dev/next/api/puppeteer.elementhandle.autofill\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| data | [AutofillData](https://pptr.dev/next/api/puppeteer.autofilldata) |  |

**Returns:**

Promise<void>

## Remarks [​](https://pptr.dev/next/api/puppeteer.elementhandle.autofill\#remarks "Direct link to Remarks")

Currently, Puppeteer supports auto-filling credit card information only and in Chrome in the new headless and headful modes only.

```codeBlockLines_RjmQ
// Select an input on the credit card form.
const name = await page.waitForSelector('form #name');
// Trigger autofill with the desired data.
await name.autofill({
  creditCard: {
    number: '4444444444444444',
    name: 'John Smith',
    expiryMonth: '01',
    expiryYear: '2030',
    cvc: '123',
  },
});

```

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.autofill#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.autofill#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.elementhandle.autofill#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!