---
url: "https://docs.browserless.io/browserql/scraping/scraping-responses"
title: "Scraping Responses | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/scraping/scraping-responses#__docusaurus_skipToContent_fallback)

BrowserQL can record responses made by the browser, filtered by the URL-pattern, method or type. BQL automatically waits for the response, which you can disable with the wait option.

- Getting all Document responses
- Loading all GET AJAX Response

```codeBlockLines_p187
mutation DocumentResponses{
  goto(url: "https://example.com/", waitUntil: load) {
    status
  }
  response(type:document) {
    url
    body
    headers {
      name
      value
    }
  }
}

```

```codeBlockLines_p187
mutation AJAXGetCalls {
  goto(url: "https://msn.com/", waitUntil: load) {
    status
  }
  response(type: xhr, method: GET, operator: and) {
    url
    type
    method
    body
    headers {
      name
      value
    }
  }
}

```