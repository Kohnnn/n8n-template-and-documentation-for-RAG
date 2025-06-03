---
url: "https://docs.browserless.io/browserql/bot-detection/ui-automation"
title: "How to Automate UIs | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/bot-detection/ui-automation#__docusaurus_skipToContent_fallback)

On this page

For activities such as submitting forms or inputting data, Browseless recommends using **BrowserQL**, our most advanced option. BQL is our own custom library that avoids the fingerprints left by other automation tools.

## How BrowserQL Works [​](https://docs.browserless.io/browserql/bot-detection/ui-automation\#how-browserql-works "Direct link to How BrowserQL Works")

**BrowserQL** is our own browser automation language, built on GraphQL. We’ve tried to keep it simple, as just a set of queries and responses.

It’s optimized for web automation and scraping, designed to minimize complexity by making intelligent assumptions. Here’s what it does for you:

- Waits for selectors before interacting with elements.
- Handles mouse movements and clicks automatically.
- Ensures elements are visible by scrolling if needed.
- Manages page-load events, like waiting for `firstContentfulPaint`.

Instead of worrying about these technical details, you focus on queries and actions. You will:

1. Navigate to pages.
2. Perform actions (e.g., click, type).
3. Solve or verify CAPTCHAs.
4. Connect to a library if needed.

Each query follows the format of `function (arguments) {responses}` with an optional `name:` beforehand. For example, going to a site and start filling a form by typing your email, would look like:

```codeBlockLines_p187
mutation form_example {
  goto(url: "https://example.com", waitUntil: networkIdle) {
    status
  }
  typeEmail: type(text: "john@email.com", selector: "#Email"
  ) {
    time
  }
}

```

We then run this query with the browsers hosted in our cloud, which you can see run in the editor.

BrowserQL API

Find out how to export your queries and integrate it in your code by [calling the BrowserQL API](https://docs.browserless.io/browserql/using-the-ide/using-api-calls).

![](https://docs.browserless.io/img/doc/02-ui-automation/automation-01.png)

Browsers

You can run **Chrome or Chromium browsers**, which you can change in the **session settings**. Chrome is more resource-intensive but recommended for getting past CAPTCHAs.

## Humanized Interactions [​](https://docs.browserless.io/browserql/bot-detection/ui-automation\#humanized-interactions "Direct link to Humanized Interactions")

BrowserQL can **humanize** your page interactions. When `humanized` is selected in the **session settings**, it will:

- Wait until the previous action's finished.
- Scroll if needed until the field is visible.
- Mouse over to somewhere within the form field.
- Click into the field.
- Type at a realistic speed.
- Make and correct typos.

Enabling User Input

**Hybrid automations** with `liveURL` allow users to interact with automated workflows.

- [How BrowserQL Works](https://docs.browserless.io/browserql/bot-detection/ui-automation#how-browserql-works)
- [Humanized Interactions](https://docs.browserless.io/browserql/bot-detection/ui-automation#humanized-interactions)