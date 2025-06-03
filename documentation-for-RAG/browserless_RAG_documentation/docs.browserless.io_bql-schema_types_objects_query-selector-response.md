---
url: "https://docs.browserless.io/bql-schema/types/objects/query-selector-response"
title: "QuerySelectorResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/query-selector-response#__docusaurus_skipToContent_fallback)

On this page

The response returned after querying the page for a selector

```codeBlockLines_p187
type QuerySelectorResponse {
  childElementCount: Float
  className: String
  id: String
  innerHTML: String
  innerText: String
  localName: String
  outerHTML: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#fields "Direct link to Fields")

#### [`QuerySelectorResponse.childElementCount`](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#queryselectorresponsechildelementcountfloat- "Direct link to queryselectorresponsechildelementcountfloat-")

The Element.childElementCount read-only property returns the number of child elements of this element

#### [`QuerySelectorResponse.className`](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#queryselectorresponseclassnamestring- "Direct link to queryselectorresponseclassnamestring-")

The className property of the Element interface gets and sets the value of the class attribute of the specified element

#### [`QuerySelectorResponse.id`](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#queryselectorresponseidstring- "Direct link to queryselectorresponseidstring-")

The id property of the Element interface represents the element's identifier, reflecting the id global attribute

#### [`QuerySelectorResponse.innerHTML`](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#queryselectorresponseinnerhtmlstring- "Direct link to queryselectorresponseinnerhtmlstring-")

The Element property innerHTML gets the HTML or XML markup contained within the element

#### [`QuerySelectorResponse.innerText`](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#queryselectorresponseinnertextstring- "Direct link to queryselectorresponseinnertextstring-")

The Element property innerText gets the text contained within the element

#### [`QuerySelectorResponse.localName`](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#queryselectorresponselocalnamestring- "Direct link to queryselectorresponselocalnamestring-")

The Element.localName read-only property returns the local part of the qualified name of an element

#### [`QuerySelectorResponse.outerHTML`](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#queryselectorresponseouterhtmlstring- "Direct link to queryselectorresponseouterhtmlstring-")

The outerHTML attribute of the Element DOM interface gets the serialized HTML fragment describing the element including its descendants. It can also be set to replace the element with nodes parsed from the given string

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/query-selector-response\#returned-by "Direct link to Returned By")

[`querySelector`](https://docs.browserless.io/bql-schema/operations/mutations/query-selector) mutation ● [`querySelectorAll`](https://docs.browserless.io/bql-schema/operations/mutations/query-selector-all) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/query-selector-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/query-selector-response#returned-by)