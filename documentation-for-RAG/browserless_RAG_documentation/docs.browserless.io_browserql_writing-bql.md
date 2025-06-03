---
url: "https://docs.browserless.io/browserql/writing-bql"
title: "Your First Query | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/writing-bql#__docusaurus_skipToContent_fallback)

On this page

BrowserQL is purely a _GraphQL_ server under the hood. This means that all of the same concepts apply to BQL that typically apply to GraphQL. Since BQL uses GraphQL as a protocol, all of the things you wish to control the browser are called _Mutations_. Here's an example first query with that in mind:

```codeBlockLines_p187
mutation ScrapeHN {
  goto(url: "https://news.ycombinator.com", waitUntil: firstMeaningfulPaint) {
    status
    time
  }
  firstHeadline: text(selector: ".titleline") {
    text
  }
}

```

Breaking this down, we're:

- Defining we want to run a `mutation` and naming our script as ScrapeHN.
- Instructing a browser to `goto` the Hacker News site, and wait for the `firstMeaningfulPaint` event to fire.
- Asking to return both the time it took and the HTTP-code's `status` once the `waitUntil` has fired.
- Giving our action an alias, in this case firstHeadline.
- Extracting the text of a specified selector.

**Click Run in the [IDE](https://account.browserless.io/bql/) to execute this mutation.**

The result will return be a JSON response that matches our query, a core part of how GraphQL works:

```codeBlockLines_p187
{
  "data": {
    "goto": {
      "status": 200,
      "time": 222
    },
    "text": {
      "text": "Hacker News new | past | comments | ask | show | jobs | submitlogin..."
    }
  }
}

```

## Exporting Your Query [​](https://docs.browserless.io/browserql/writing-bql\#exporting-your-query "Direct link to Exporting Your Query")

BrowserQL can be exported and run programmatically just like with any other kind of GraphQL server. You can export queries via two means:

**1\. Clicking the Export Query as Code button**: This option will open a tab with multiple available code languages you can select and copy the code. For more details on this feature, refer to the [Query as Code](https://docs.browserless.io/browserql/using-the-ide/ide-features#query-as-code) section of the documentation.

Keep your Token Safe

The codes copied with the Export Query as Code feature will include headers, variables and API tokens in it.
Be careful not to share your private information in public places like Github, Bitbucket, etc. This opens space for malicious API calls.

**2\. Selecting and copying the query**: Similar to other IDEs, you can select an entire query and copy it to paste wherever necessary. This is helpful if you want to store queries in a `.gql` file for further processing or fetching. Be sure to consult your library's documentation when using this approach.

note

This method does _**not**_ copy any associated variables, headers, or API tokens, so make sure to apply those correctly before executing your query.

- [Exporting Your Query](https://docs.browserless.io/browserql/writing-bql#exporting-your-query)