---
url: "https://docs.browserless.io/bql-schema/operations/mutations/map-selector"
title: "mapSelector | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/map-selector#__docusaurus_skipToContent_fallback)

On this page

Specify a selector that returns multiple nodes in a document (similar to `document.querySelectorAll`), or JavaScript that returns a NodeList, and this API will respond with details about those DOM nodes. Similar to how "map" works in most functional programming languages and libraries. Useful for mapping over repetitive data in sites and pages like product listings or search results. This will automatically wait for the selector to be present on the page, and is configurable with the "wait" and "timeout" options.

For getting arbitrary DOM attributes back you can specify them via the `attribute(name: "data-custom-attribute")` property. This will return an object with `name` and `value` properties.

You may also continuously map further nested items as well, for instance this query might get all books on a page, and then a nested `mapSelector` call might list all sellers of that book, or shipping speeds. Hierarchy of data is preserved to pass through the hierarchical data modeled inside the DOM.

This API will always return a list of results back regardless if one or more items are found, or `null` if none are found.

Using aliases can also give the returned JSON more meaning and better model the data returned by this powerful API.

**Simple Example**

```codeBlockLines_p187
mutation HNLinks {
  goto(url: "https://news.ycombinator.com") {
    status
  }

  # Get all the top links HTML
  mapSelector(selector: ".athing") {
    innerHTML
  }
}

```

**Nested Example With Aliases**

```codeBlockLines_p187
mutation HNLinksWithMetaData {
  goto(url: "https://news.ycombinator.com") {
    status
  }

  # Get all textual content
  posts: mapSelector(selector: ".athing") {
    postName: innerText

    # Get the author(s)
    authors: mapSelector(selector: ".author") {
      authorName: innerText
    }

    # Get the post score
    score: mapSelector(selector: ".score") {
      score: innerText
    }
  }
}

```

```codeBlockLines_p187
mapSelector(
  selector: String!
  timeout: Float
  wait: Boolean = true
): [MapSelectorResponse]

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/map-selector\#arguments "Direct link to Arguments")

#### [`mapSelector.selector`](https://docs.browserless.io/bql-schema/operations/mutations/map-selector\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/map-selector\#mapselectorselectorstring-- "Direct link to mapselectorselectorstring--")

A `document.querySelectorAll` compatible string, or JavaScript that returns a DOM NodeList. Examples include:

- A list of `<button />` Elements:
`selector: "button"`

- A JavaScript snippet that returns a button element
`selector: "document.querySelectorAll('button')"`


#### [`mapSelector.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/map-selector\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/map-selector\#mapselectortimeoutfloat- "Direct link to mapselectortimeoutfloat-")

How long to wait for the element to appear before timing out, overriding any defaults. Default timeout is 30 seconds, or 30000.

#### [`mapSelector.wait`](https://docs.browserless.io/bql-schema/operations/mutations/map-selector\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/map-selector\#mapselectorwaitboolean- "Direct link to mapselectorwaitboolean-")

Whether or not to wait for the selectors to present in the DOM

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/map-selector\#type "Direct link to Type")

#### [`MapSelectorResponse`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/map-selector\#mapselectorresponse- "Direct link to mapselectorresponse-")

Response returned from a Map Selector

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/map-selector#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/map-selector#type)