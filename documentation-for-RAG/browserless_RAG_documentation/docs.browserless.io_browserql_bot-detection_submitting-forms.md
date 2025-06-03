---
url: "https://docs.browserless.io/browserql/bot-detection/submitting-forms"
title: "Submitting Forms | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/bot-detection/submitting-forms#__docusaurus_skipToContent_fallback)

On this page

Modern websites often employ sophisticated techniques such as CAPTCHAs, iframes, and closed-shadow DOM trees to block automated tools. **BrowserQL** presents you with tools to automate challenging scenarios such as handling CAPTCHAs, submitting forms, and navigating deeply nested elements. The combination of **deep selectors** and **humanized actions** ensures that your automation scripts are both effective and resilient.

## Submitting Forms [​](https://docs.browserless.io/browserql/bot-detection/submitting-forms\#submitting-forms "Direct link to Submitting Forms")

BrowserQL simplifies form submission by automating the process in a human-like manner. It handles tasks like filling input fields, selecting dropdowns, and clicking buttons with minimal configuration. Here’s how you can fill out a form and submit it:

Solving CAPTCHAs

BQL can solve CAPTCHAs with the `solve` and `verify` mutations. Refer to the [Solving CAPTCHAs](https://docs.browserless.io/browserql/bot-detection/solving-captchas) page for more details.

```codeBlockLines_p187
mutation SubmitForm {
  goto(url: "https://example.com/form", waitUntil: firstContentfulPaint) {
    status
  }

  fillName: type(
    selector: "input#name"
    text: "John Doe"
  ) {
    time
  }

  fillEmail: type(
    selector: "input#email"
    text: "johndoe@example.com"
  ) {
    time
  }

  submitForm: click(
    selector: "button#submit"
  ) {
    time
  }
}

```

Humanized Behavior

BrowserQL ensures that the input values are typed with randomized delays, mimicking human behavior to avoid detection. Refer to the following pages for more details:

- **[Session Settings](https://docs.browserless.io/browserql/using-the-ide/session-settings#configuring-session-settings)**: Learn to activate human-like behavior on your queries.
- **[Writing BrowserQL](https://docs.browserless.io/browserql/writing-bql/language-basics#performing-actions)**: Understand how to change delay time in your mutations.

## Clicking within Iframes [​](https://docs.browserless.io/browserql/bot-detection/submitting-forms\#clicking-within-iframes "Direct link to Clicking within Iframes")

Deep selectors lets you target elements nested inside iframes or hidden within shadow DOMs. These selectors extend the standard query syntax, allowing precise targeting even on complex web pages.

### How to Click within Iframes [​](https://docs.browserless.io/browserql/bot-detection/submitting-forms\#how-to-click-within-iframes "Direct link to How to Click within Iframes")

To target an element inside an iframe, you need to specify the iframe URL pattern and the DOM selector, following the format shown below:

```codeBlockLines_p187
selector: "< [optional URL pattern] selector"

```

1. **`<` Character**: Indicates that you’re using a deep selector.
2. **Optional URL Pattern**: Matches iframe URLs using glob-style patterns.
3. **DOM Selector**: Identifies the target element within the matched iframe.

Below you can see multiple deep selector examples:

- Example 1
- Example 2
- Example 3
- Example 4

Target an iframe of cnn.com and look for a button with an ID of "submit"

```codeBlockLines_p187
selector: "< *cnn.com* button#submit"

```

Target an iframe of google.com/api/verify and click an anchor element with a classname that includes "now":

```codeBlockLines_p187
selector: "< *google.com/api/verify* a[class*='now']"

```

Find any element on any iframe (or top-level page) with an attribute of price:

```codeBlockLines_p187
selector: "< [price]"

```

Find an iframe with an exact URL of " [https://amazon.com/](https://amazon.com/) and a span with classname of "submit" and "order":

```codeBlockLines_p187
selector: "< https://amazon.com/ span.submit.order"

```

Restrictions

- **Parent-child relationships** are not supported (e.g., `div > span`).
- Each selector must refer to a **single node**.

- [Submitting Forms](https://docs.browserless.io/browserql/bot-detection/submitting-forms#submitting-forms)
- [Clicking within Iframes](https://docs.browserless.io/browserql/bot-detection/submitting-forms#clicking-within-iframes)
  - [How to Click within Iframes](https://docs.browserless.io/browserql/bot-detection/submitting-forms#how-to-click-within-iframes)