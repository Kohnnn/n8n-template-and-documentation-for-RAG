---
url: "https://docs.browserless.io/browserql/writing-bql/language-basics"
title: "Language Basics | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/writing-bql/language-basics#__docusaurus_skipToContent_fallback)

On this page

Learning a new language can be intimidating, but mastering BQL doesn't have to be difficult. This guide provides a straightforward overview of how to write BQL with a clear.

## What You Won't Write [​](https://docs.browserless.io/browserql/writing-bql/language-basics\#what-you-wont-write "Direct link to What You Won't Write")

BrowserQL is optimized for web automation and scraping, designed to minimize complexity by making intelligent assumptions. Here’s what it does **for you**:

- **Waits for selectors** before interacting with elements.
- Handles **mouse movements** and clicks automatically.
- Ensures **elements are visible** by scrolling as needed.
- Manages **page-load events**, like waiting for `firstContentfulPaint`.

Instead of worrying about these technical details, you focus on **queries and actions**.

## What You’ll Write [​](https://docs.browserless.io/browserql/writing-bql/language-basics\#what-youll-write "Direct link to What You’ll Write")

BQL is a query language where you:

1. Navigate to pages.
2. Perform actions (e.g., click, type).
3. Extract data (e.g., text, HTML).

With just a handful of commands ( [`goto`](https://docs.browserless.io/bql-schema/operations/mutations/goto), [`text`](https://docs.browserless.io/bql-schema/operations/mutations/text), [`html`](https://docs.browserless.io/bql-schema/operations/mutations/html), [`click`](https://docs.browserless.io/bql-schema/operations/mutations/click), [`type`](https://docs.browserless.io/bql-schema/operations/mutations/type) and [more](https://docs.browserless.io/bql-schema/operations/mutations)), you can achieve complex automation in a fraction of the usual code.

For example, the script below demonstrates how easy it is to automate a logging into Cloudflare in 30 lines:

```codeBlockLines_p187
mutation Cloudflare {
  goto(
    url: "https://dash.cloudflare.com/login?lang=en-gb"
    waitUntil: firstContentfulPaint
  ) {
    status
  }

  acceptCookies: click(
    selector: "#onetrust-accept-btn-handler"
  ) {
    time
  }

  typeEmail: type(
    selector: "form [data-testid='login-input-email']"
    text: "test@browserless.io"
  ) {
    selector
  }

  typePassword: type(
    selector: "form [data-testid='login-input-password']"
    text: "super-cool-password"
  ) {
    selector
  }

  clickCaptcha: verify(
    type: cloudflare
  ) {
    solved
  }
}

```

## Creating a BQL Script [​](https://docs.browserless.io/browserql/writing-bql/language-basics\#creating-a-bql-script "Direct link to Creating a BQL Script")

Below are steps into creating a BQL script, guiding you into navigating to a page, retrieving data, performing actions, and, finally, generating an endpoint to connect to external libraries.

### Navigating to a Page [​](https://docs.browserless.io/browserql/writing-bql/language-basics\#navigating-to-a-page "Direct link to Navigating to a Page")

Every script starts with a **mutation**, specifying actions and the responses you expect:

```codeBlockLines_p187
mutation ExampleName {
  goto(
    url: "https://example.com"
    waitUntil: firstMeaningfulPaint
  ) {
    status
    time
  }
}

```

This standard format is composed of the following:

1. **Action**: `goto` specifies the page to navigate to.
2. **Arguments**: Provide the `url` and a `waitUntil` condition.
3. **Response**: Request useful outputs, like `status` or `time`.

Mutations

You can find detailed information on all mutations, their arguments, and responses in the [Mutations Reference page](https://docs.browserless.io/bql-schema/schema) and also in the [Built-in Documentation](https://docs.browserless.io/browserql/using-the-ide/ide-features#built-in-documentation) in our IDE.

### Retrieving Data [​](https://docs.browserless.io/browserql/writing-bql/language-basics\#retrieving-data "Direct link to Retrieving Data")

Extracting information is just as simple. Use `text` or `html` commands depending on the format you need:

- Text
- HTML

```codeBlockLines_p187
mutation ExampleName {
  ...
  productName: text(
    selector: "span#productTitle"
    visible: true
  ) {
    text
  }
}

```

Where:

- **Alias**: `productName` is the name for this interaction. You can define names for each interaction in the script.
- **Action**: `text` extracts visible text.
- **Arguments**: Include a `selector` and optional conditions like `visible`.
- **Output**: The desired response (e.g., text content).

Example JSON response:

```codeBlockLines_p187
"productName": {
  "text": "Coffee and Espresso Maker"
}

```

Pro Tip

Omit the `selector` to retrieve the entire page’s content.

```codeBlockLines_p187
mutation ExampleName {
  ...
  elementHTML: html(
    selector: "div"
    visible: true
  ) {
    html
  }
}

```

Where:

- **Alias**: `elementHTML` is the name for this interaction. You can define names for each interaction in the script.
- **Action**: `html` extracts the element's HTML content.
- **Arguments**: Include a `selector` and optional conditions like `visible`.
- **Output**: The desired response (e.g., html content).

Example JSON response:

```codeBlockLines_p187
"productName": {
  "html": "\n    <h1 xmlns=\"http://www.w3.org/1999/xhtml\">Example Domain</h1>\n    <p xmlns=\"http://www.w3.org/1999/xhtml\">This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p xmlns=\"http://www.w3.org/1999/xhtml\"><a href=\"https://www.iana.org/domains/example\">More information...</a></p>\n"
}

```

Pro Tip

Omit the `selector` to retrieve the entire page’s html content.

### Performing Actions [​](https://docs.browserless.io/browserql/writing-bql/language-basics\#performing-actions "Direct link to Performing Actions")

Many cases for gathering data or normalizing data across systems require you click, type and submit forms. All of these are staples of any web automation library and are supported by BrowserQL.

By default, BrowserQL takes care of waiting for these elements to be present in the document, visible to an end user, and scrolls to them in the viewport. You won't have to worry about writing code to handle those small nuanced situations.

- Clicking a Button
- Keyboard Typing
- HTML Content
- Retrieving Text

To click the **Free Trial** link at the Browserless.io website, you need to navigate to the website with the `goto` mutation, and then use the `click` to select the `<a>` element. In the example below, we'll use the element's href to find the correct element on screen. Also, the visible flag specifies that this element must be visible to the user.

- Clicking
- Setting a Timeout

```codeBlockLines_p187
mutation ClickButton {
  goto(url: "https://www.browserless.io/" waitUntil: firstContentfulPaint) {
    status
  }

  click(selector: "a[href=\"https://account.browserless.io/signup/email/?plan=starter\"]", visible: true) {
    x
    y
  }
}

```

By default BrowserQL will automatically wait for elements to be present before interacting with them. You can limit the amount of time it will wait by setting a `timeout` argument. The following will limit the `timeout` to 10 seconds versus the default of 30 seconds:

```codeBlockLines_p187

mutation ClickButton {
  goto(url: "https://www.browserless.io/" waitUntil: firstContentfulPaint) {
    status
  }

  click(
    selector: "a[href=\"https://account.browserless.io/signup/email/?plan=starter\"]",
    visible: true
    timeout: 10000
  ) {
    x
    y
  }
}

```

Typing is also supported, and works similarly to how the `click` query does. After navigating to a website, you need to specify the text you want to be typed, along with the selector, telling the query where it should type the content.

- Typing
- Setting a Delay

```codeBlockLines_p187
mutation TypeInteraction {
  goto(url: "https://www.google.com/" waitUntil: firstContentfulPaint) {
    status
  }

  type(
    text: "I'm a little teapot!"
    selector: "form textarea"
  ) {
    x
    y
  }
}

```

By default, BrowserQL will type a character at a time with a random interval of space between similar to a real user. If you wish to change this delay you can specify a `delay` argument which receives an array with a minimum and maximum delay time ( `[min, max]`) in milliseconds.

```codeBlockLines_p187
mutation TypeInteraction {
  goto(url: "https://www.google.com/" waitUntil: firstContentfulPaint) {
    status
  }

  type(
    text: "I'm a little teapot!"
    selector: "form textarea"
    delay: [10, 50]
  ) {
    x
    y
  }
}

```

This means a delay between `10` and `50` milliseconds is chosen at random between keystrokes.

You can retrieve HTML content from any website with BrowserQL as well. Use the `html` mutation after navigating to the website.

- HTML
- With Selector

```codeBlockLines_p187
mutation HTMLInteraction {
  goto(url: "https://www.browserless.io/" waitUntil: firstContentfulPaint) {
    status
  }

  html(
    visible: true
  ) {
    time
    html
  }
}

```

You can set a selector to the `html` mutation to define what content you want to retrieve from the page. In the case below, we return the content from the `h1` element with `.heading-style-h1.margin-bottom.margin-large` classes.

```codeBlockLines_p187
mutation HTMLInteraction {
  goto(url: "https://www.browserless.io/" waitUntil: firstContentfulPaint) {
    status
  }

  html(
    selector: "h1.heading-style-h1.margin-bottom.margin-large"
    visible: true
  ) {
    time
    html
  }
}

```

To retrieve the text from an element in any website, you can use the `text` mutation, and add a `selector` argument to define which element to search for the text content.

- Text
- Last element of its kind

```codeBlockLines_p187
mutation TextInteraction {
  goto(url: "https://www.example.com/" waitUntil: firstContentfulPaint) {
    status
  }

  text(
    selector: "p"
    visible: true
  ) {
    time
    text
  }
}

```

```codeBlockLines_p187
mutation TextInteraction {
  goto(url: "https://www.example.com/" waitUntil: firstContentfulPaint) {
    status
  }

  text(
    selector: "p:last-of-type"
    visible: true
  ) {
    time
    text
  }
}

```

For actions such as the need to get past a captcha, BQL takes humanized actions, such as moving the mouse to a selector and randomized typing delays. By default, BrowserQL will type a character at a time with a random time between strokes similar to a real user.

Delay Change

If you wish to change this delay you can specify a `min` and `max` delay. Below, typing delays are randomized between 10–50 milliseconds, mimicking natural input:

```codeBlockLines_p187
teapotTyping: type(
  text: "I'm a little teapot!"
  selector: "form textarea"
  delay: [10, 50]
) {
  time
}

```

### Handling CAPTCHA [​](https://docs.browserless.io/browserql/writing-bql/language-basics\#handling-captcha "Direct link to Handling CAPTCHA")

If you know that a page is going to have a captcha, such as for a login or form submission, you can use the [verification mutation](https://docs.browserless.io/bql-schema/operations/mutations/verify). This will click on the captcha, even if it’s hidden away in iframe and shadow DOMs. Just specify the CAPTCHA type (e.g., `hcaptcha` or `cloudflare`), and BQL takes care of the rest:

```codeBlockLines_p187
verifyCaptcha: verify(type: hcaptcha) {
  time
  found
  solved
}

```

### Connecting Libraries with Endpoints [​](https://docs.browserless.io/browserql/writing-bql/language-basics\#connecting-libraries-with-endpoints "Direct link to Connecting Libraries with Endpoints")

We also know that you might want to connect other libraries, like Puppeteer or Playwright, to these browsers once they’ve got past the bot detectors. You can create an endpoint with the `reconnect` action, and use this endpoint to connect to the browser:

```codeBlockLines_p187
reconnect(timeout: 30000) {
  browserWSEndpoint
}

```

## Next Steps [​](https://docs.browserless.io/browserql/writing-bql/language-basics\#next-steps "Direct link to Next Steps")

BrowserQL simplifies web automation with intuitive commands and a structure that’s easy to learn. Start by focusing on the following:

- [Advanced Options](https://docs.browserless.io/browserql/writing-bql/advanced-options)
- [Extracting Scripts](https://docs.browserless.io/browserql/writing-bql/exporting-scripts)

- [What You Won't Write](https://docs.browserless.io/browserql/writing-bql/language-basics#what-you-wont-write)
- [What You’ll Write](https://docs.browserless.io/browserql/writing-bql/language-basics#what-youll-write)
- [Creating a BQL Script](https://docs.browserless.io/browserql/writing-bql/language-basics#creating-a-bql-script)
  - [Navigating to a Page](https://docs.browserless.io/browserql/writing-bql/language-basics#navigating-to-a-page)
  - [Retrieving Data](https://docs.browserless.io/browserql/writing-bql/language-basics#retrieving-data)
  - [Performing Actions](https://docs.browserless.io/browserql/writing-bql/language-basics#performing-actions)
  - [Handling CAPTCHA](https://docs.browserless.io/browserql/writing-bql/language-basics#handling-captcha)
  - [Connecting Libraries with Endpoints](https://docs.browserless.io/browserql/writing-bql/language-basics#connecting-libraries-with-endpoints)
- [Next Steps](https://docs.browserless.io/browserql/writing-bql/language-basics#next-steps)