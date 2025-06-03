---
url: "https://docs.browserless.io/browserql/recipes/mapping"
title: "Mapping | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/recipes/mapping#__docusaurus_skipToContent_fallback)

On this page

The mapping feature provides a flexible way to extract structured data from web pages by specifying DOM selectors or JavaScript snippets. This guide covers advanced tips, best practices, and sneaky strategies to help you leverage this feature fully.

The mapping feature allows you to:

- Select multiple DOM nodes simultaneously.
- Retrieve structured data (text, HTML, or attributes).
- Map nested selectors to capture hierarchical DOM structures.
- Assign aliases to make your returned JSON more meaningful.

tip

Use specific CSS selectors to avoid unnecessary data.

## Creating JSON with `mapSelector` [​](https://docs.browserless.io/browserql/recipes/mapping\#creating-json-with-mapselector "Direct link to creating-json-with-mapselector")

The `mapSelector` function offers an intuitive alternative to typical parsing, working similarly to the `map` function in functional programming, with NodeLists or `document.querySelectorAll`.

You can easily extract DOM attributes using the `attribute(name: "data-custom-attribute")` property. It returns an object with `name` and `value` properties.

The query below demonstrates how to:

1. Navigate to `https://news.ycombinator.com`.
2. Create a map named `posts` to extract all `.submission .titleline > a` elements.
3. Return an array of objects, each containing the `href` attribute as a structured JSON.

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

## Smart Use of Aliases [​](https://docs.browserless.io/browserql/recipes/mapping\#smart-use-of-aliases "Direct link to Smart Use of Aliases")

Aliases enhance readability and clarity of your mapped data.

**Example:**

```codeBlockLines_p187
mutation ProductDetails {
  goto(url: "https://example.com/products") {
    status
  }

  products: mapSelector(selector: ".product-item") {
    title: mapSelector(selector: ".product-title") { innerText }
    price: mapSelector(selector: ".product-price") { innerText }
  }
}

```

## Handling Arbitrary DOM Attributes [​](https://docs.browserless.io/browserql/recipes/mapping\#handling-arbitrary-dom-attributes "Direct link to Handling Arbitrary DOM Attributes")

Retrieve any `custom` or `data-*` attributes seamlessly:

**Example:**

```codeBlockLines_p187
mutation CustomAttributes {
  goto(url: "https://example.com") {
    status
  }

  items: mapSelector(selector: "[data-item-id]") {
    id: attribute(name: "data-item-id") {
      name
      value
    }
  }
}

```

## Nested Mapping for Hierarchical Data [​](https://docs.browserless.io/browserql/recipes/mapping\#nested-mapping-for-hierarchical-data "Direct link to Nested Mapping for Hierarchical Data")

Use nested mappings for deeply structured data. The hierarchy is preserved, making your structured JSON easier to handle:

**Example:**

```codeBlockLines_p187
mutation NestedMappingExample {
  goto(url: "https://example.com/categories") {
    status
  }

  categories: mapSelector(selector: ".category") {
    categoryName: innerText
    subcategories: mapSelector(selector: ".subcategory") {
      subcategoryName: innerText
    }
  }
}

```

### Advanced Nested Example [​](https://docs.browserless.io/browserql/recipes/mapping\#advanced-nested-example "Direct link to Advanced Nested Example")

Further illustrating nested mapping, this example retrieves metadata such as author and score:

```codeBlockLines_p187
mutation map_selector_example_with_metadata {
  goto(url: "https://news.ycombinator.com") {
    status
  }

  posts: mapSelector(selector: ".subtext .subline") {
    author: mapSelector(selector: ".hnuser") {
      authorName: innerText
    }

    score: mapSelector(selector: ".score") {
      score: innerText
    }
  }
}

```

## Conditional Wait and Timeout Adjustments [​](https://docs.browserless.io/browserql/recipes/mapping\#conditional-wait-and-timeout-adjustments "Direct link to Conditional Wait and Timeout Adjustments")

Customize wait times for dynamic content:

**Example:**

```codeBlockLines_p187
mutation TimeoutExample {
  goto(url: "https://example.com") {
    status
  }

  delayedItems: mapSelector(selector: ".async-loaded-item", timeout: 60000, wait: true) {
    content: innerText
  }
}

```

- [Creating JSON with `mapSelector`](https://docs.browserless.io/browserql/recipes/mapping#creating-json-with-mapselector)
- [Smart Use of Aliases](https://docs.browserless.io/browserql/recipes/mapping#smart-use-of-aliases)
- [Handling Arbitrary DOM Attributes](https://docs.browserless.io/browserql/recipes/mapping#handling-arbitrary-dom-attributes)
- [Nested Mapping for Hierarchical Data](https://docs.browserless.io/browserql/recipes/mapping#nested-mapping-for-hierarchical-data)
  - [Advanced Nested Example](https://docs.browserless.io/browserql/recipes/mapping#advanced-nested-example)
- [Conditional Wait and Timeout Adjustments](https://docs.browserless.io/browserql/recipes/mapping#conditional-wait-and-timeout-adjustments)