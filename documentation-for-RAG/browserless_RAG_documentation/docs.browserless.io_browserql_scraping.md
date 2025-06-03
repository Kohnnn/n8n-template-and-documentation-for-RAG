---
url: "https://docs.browserless.io/browserql/scraping"
title: "How to scrape websites | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/scraping#__docusaurus_skipToContent_fallback)

On this page

For web scraping, Browseless recommends using **BrowserQL**, our most advanced option. BQL is our own custom library that avoids the fingerprints left by other automation tools.

In this section you'll go through the following:

- [How BrowserQL works](https://docs.browserless.io/browserql/scraping#how-browserql-works)
- [Bypassing bot detectors](https://docs.browserless.io/scraping/bot-detectors)
- [Performing searches](https://docs.browserless.io/scraping/performing-searches)
- [Extracting HTML or a JSON](https://docs.browserless.io/scraping/extracting-data)
- [Scraping responses](https://docs.browserless.io/scraping/scraping-responses)

## How BrowserQL works [​](https://docs.browserless.io/browserql/scraping\#how-browserql-works "Direct link to How BrowserQL works")

BrowserQL is our own browser automation language, built on GraphQL. We’ve kept it simple, as a set of queries and responses.

BQL is optimized for web automation and scraping, designed to minimize complexity by making intelligent assumptions. Here’s what it does for you:

- Loads a browser with human-like fingerprints.
- Manages page-load events, like `firstContentfulPaint`.
- Handles proxies and request filtering.
- Waits for any mentioned selectors.

Instead of worrying about these technical details, you can focus on queries and actions. You will:

1. Navigate to pages.
2. Perform actions (e.g., click, type).
3. Extract data (e.g., text, HTML).

Each query follows the format of `function (arguments) {responses}` with an optional `name:` beforehand For example, going to a site and grabbing a product name would be:

```codeBlockLines_p187
mutation scrape_example {
  goto(url: "https://example.com", waitUntil: networkIdle) {
    status
  }
 productName: text(
    selector: "span#productTitle"
    visible: true
  ) {
    text
  }
}

```

We then run this query with the browsers hosted in our cloud, which you can see run in the [editor](https://bql.browserless.io/).

BrowserQL API

Find out how to export your queries and integrate it in your code by [calling the BrowserQL API](https://docs.browserless.io/browserql/using-the-ide/using-api-calls).

![](https://docs.browserless.io/img/doc/01-scraping/scraping-1.png)

- [How BrowserQL works](https://docs.browserless.io/browserql/scraping#how-browserql-works)