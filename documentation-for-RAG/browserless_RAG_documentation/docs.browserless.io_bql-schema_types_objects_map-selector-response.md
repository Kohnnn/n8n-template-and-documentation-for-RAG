---
url: "https://docs.browserless.io/bql-schema/types/objects/map-selector-response"
title: "MapSelectorResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/map-selector-response#__docusaurus_skipToContent_fallback)

On this page

Response returned from a Map Selector

```codeBlockLines_p187
type MapSelectorResponse {
  innerHTML: String
  innerText: String
  id: String
  class: [String]
  attribute(
    name: String
  ): Attribute
  mapSelector(
    selector: String!
    timeout: Float
    wait: Boolean = true
  ): [MapSelectorResponse]
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#fields "Direct link to Fields")

#### [`MapSelectorResponse.innerHTML`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponseinnerhtmlstring- "Direct link to mapselectorresponseinnerhtmlstring-")

The innerHTML of the selected DOM Node

#### [`MapSelectorResponse.innerText`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponseinnertextstring- "Direct link to mapselectorresponseinnertextstring-")

The innerText of the selected DOM Node, eg, the raw textual content

#### [`MapSelectorResponse.id`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponseidstring- "Direct link to mapselectorresponseidstring-")

The ID attribute's value, if any, of the node

#### [`MapSelectorResponse.class`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`[String]`](https://docs.browserless.io/bql-schema/types/scalars/string) listscalar [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponseclassstring-- "Direct link to mapselectorresponseclassstring--")

The class attribute's value, if any, of the node represented as an array of strings

#### [`MapSelectorResponse.attribute`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`Attribute`](https://docs.browserless.io/bql-schema/types/objects/attribute) object [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponseattributeattribute- "Direct link to mapselectorresponseattributeattribute-")

Retrieve an attribute by the name of the attribute itself, eg, "data-test-id"

##### [`MapSelectorResponse.attribute.name`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponseattributenamestring- "Direct link to mapselectorresponseattributenamestring-")

#### [`MapSelectorResponse.mapSelector`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`[MapSelectorResponse]`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response) listobject [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponsemapselectormapselectorresponse-- "Direct link to mapselectorresponsemapselectormapselectorresponse--")

You can further map nested DOM nodes as well. For instance, given a parent ".product" node, you can map further nodes like ".price" or ".shipping" as examples. This will give you items appropriately nested by their parent node for better hierarchical representation of data

##### [`MapSelectorResponse.mapSelector.selector`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponsemapselectorselectorstring-- "Direct link to mapselectorresponsemapselectorselectorstring--")

A query-selector-al compatible string, or JavaScript code that returns an DOM NodeList. Examples include:

- All `<button />` Elements:
`selector: "button"`

- A JavaScript snippet that returns a button element
`selector: "document.querySelectorAll('button')"`


##### [`MapSelectorResponse.mapSelector.timeout`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponsemapselectortimeoutfloat- "Direct link to mapselectorresponsemapselectortimeoutfloat-")

How long to wait for the element to appear before timing out, overriding any defaults. Default timeout is 30 seconds, or 30000.

##### [`MapSelectorResponse.mapSelector.wait`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#mapselectorresponsemapselectorwaitboolean- "Direct link to mapselectorresponsemapselectorwaitboolean-")

Whether or not to wait for the selectors to present in the DOM

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#returned-by "Direct link to Returned By")

[`mapSelector`](https://docs.browserless.io/bql-schema/operations/mutations/map-selector) mutation

### Member Of [​](https://docs.browserless.io/bql-schema/types/objects/map-selector-response\#member-of "Direct link to Member Of")

[`MapSelectorResponse`](https://docs.browserless.io/bql-schema/types/objects/map-selector-response) object

- [Fields](https://docs.browserless.io/bql-schema/types/objects/map-selector-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/map-selector-response#returned-by)
- [Member Of](https://docs.browserless.io/bql-schema/types/objects/map-selector-response#member-of)