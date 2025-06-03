---
url: "https://docs.browserless.io/browserql/scraping/extracting-data"
title: "Extracting Data | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/scraping/extracting-data#__docusaurus_skipToContent_fallback)

On this page

You have three main options for extracting data:

- Grab the full or cleaned HTML to parse externally
- Use the mapping function to generate a JSON
- Use requests to grab an API response

## Responding with HTML [​](https://docs.browserless.io/browserql/scraping/extracting-data\#responding-with-html "Direct link to Responding with HTML")

If you already have a parser set up, then you can grab the HTML. You can include selectors such as `body` or use our cleaning options. For example:

- Cleaned HTML
- HTML of a selector

```codeBlockLines_p187
mutation clean_example {
  goto(url: "https://www.browserless.io/") {
    status
  }
html(clean: {
    removeAttributes: true,
    removeNonTextNodes: true
  }) {
    html
  }
}

```

```codeBlockLines_p187
mutation clean_example {
  goto(url: "https://www.browserless.io/") {
    status
  }
html(
  selector: ".navbar_container"
  clean: {
    removeAttributes: true,
    removeNonTextNodes: true
  }) {
    html
  }
}

```

Clean Features

Features of the "clean" argument include removal of non-text nodes, removal of DOM attributes, as well as removal of excessive whitespace and newlines. Using "clean" can save nearly 1,000 times the payload size.

## Creating a JSON with `mapSelector` [​](https://docs.browserless.io/browserql/scraping/extracting-data\#creating-a-json-with-mapselector "Direct link to creating-a-json-with-mapselector")

We have created an alternative to typical parsing, with our `mapSelector` mutation. It is similar to how “map” works in most functional programming languages, where you might use a NodeList or `document.querySelectorAll`.

For getting arbitrary DOM attributes back you can specify them via the `attribute(name: "data-custom-attribute")` property. This will return an object with `name` and `value` properties.

To exemplify this feature, the query below does the following:

1. Navigates to `https://news.ycombinator.com`.
2. Creates a map called `posts`, finding all elements with the `.submission .titleline > a` selector.
3. Returns an array of objects, with an object for each element found. This object will present the name given to the attribute searched as key ( `link`), and inside it, a `value` key with the actual value searched, in the example below, the `href` of each element.

- Mutation
- Example response

```codeBlockLines_p187
mutation scraping_example {
  goto(
    url: "https://news.ycombinator.com",
    waitUntil: firstContentfulPaint
  ) {
    status
  }

  posts: mapSelector(selector: ".submission .titleline > a", wait: true) {
    link: attribute(name: "href") {
      value
    }
  }
}

```

```codeBlockLines_p187
{
  "data": {
    "goto": {
      "status": 200
    },
    "posts": [\
      {\
        "link": {\
          "value": "https://churchofturing.github.io/landscapeoflisp.html"\
        }\
      },\
      {\
        "link": {\
          "value": "https://www.jjj.de/fxt/fxtbook.pdf"\
        }\
      },\
      ...\
      {\
        "link": {\
          "value": "https://ereader-swedish.fly.dev/"\
        }\
      }\
    ]
  }
}

```

You may also continuously map further nested items, for instance this query might get all posts on a page, and then a nested `mapSelector` call might list each author, and post score. Hierarchy of data is preserved to pass through the hierarchical data modeled inside the DOM.

```codeBlockLines_p187
mutation map_selector_example_with_metadata {
  goto(url: "https://news.ycombinator.com") {
    status
  }

  # Get all textual content
  posts: mapSelector(selector: ".subtext .subline") {
    # Get the author(s)
    author: mapSelector(selector: ".hnuser") {
      authorName: innerText
    }

    # Get the post score
    score: mapSelector(selector: ".score") {
      score: innerText
    }
  }
}

```

This API will always return a list of results back regardless if one or more items are found, or null if none are found.

For more details, check out the [advanced mapping guide](https://docs.browserless.io/browserql/recipes/mapping).

- [Responding with HTML](https://docs.browserless.io/browserql/scraping/extracting-data#responding-with-html)
- [Creating a JSON with `mapSelector`](https://docs.browserless.io/browserql/scraping/extracting-data#creating-a-json-with-mapselector)