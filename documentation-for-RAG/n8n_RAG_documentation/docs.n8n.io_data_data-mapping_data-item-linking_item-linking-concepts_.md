---
url: "https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts/"
title: "Item linking concepts | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts/#item-linking-concepts)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-mapping/data-item-linking/item-linking-concepts.md "Edit this page")

# Item linking concepts [\#](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts/\#item-linking-concepts "Permanent link")

Each output item created by a node includes metadata that links them to the input item (or items) that the node used to generate them. This creates a chain of items that you can work back along to access previous items. This can be complicated to understand, especially if the node splits or merges data. You need to understand item linking when building your own programmatic nodes, or in some scenarios using the Code node.

This document provides a conceptual overview of this feature. For usage details, refer to:

- [Item linking for node creators](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-node-building/), for details on how to handle item linking when building a node.
- [Item linking in the Code node](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-code-node/), to learn how to handle item linking in the Code node.
- [Item linking errors](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-errors/), to understand the errors you may encounter in the editor UI.

## n8n's automatic item linking [\#](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts/\#n8ns-automatic-item-linking "Permanent link")

If a node doesn't control how to link input items to output items, n8n tries to guess how to link the items automatically:

- Single input, single output: the output links to the input.
- Single input, multiple outputs: all outputs link to that input.
- Multiple inputs and outputs:
  - If you keep the input items, but change the order (or remove some but keep others), n8n can automatically add the correct linked item information.
  - If the number of inputs and outputs is equal, n8n links the items in order. This means that output-1 links to input-1, output-2 to input-2, and so on.
  - If the number isn't equal, or you create completely new items, n8n can't automatically link items.

If n8n can't link items automatically, and the node doesn't handle the item linking, n8n displays an error. Refer to [Item linking errors](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-errors/) for more information.

## Item linking example [\#](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts/\#item-linking-example "Permanent link")

[![A diagram showing the threads linking multiple items back through a workflow](https://docs.n8n.io/_images/data/data-mapping/data-item-linking/item-linking-multiple-lines.png)](https://docs.n8n.io/_images/data/data-mapping/data-item-linking/item-linking-multiple-lines.png)

In this example, it's possible for n8n to link an item in one node back several steps, despite the item order changing. This means the node that sorts movies alphabetically can access information about the linked item in the node that gets famous movie actors.

The methods for accessing linked items are different depending on whether you're using the UI, expressions, or the code node. Explore the following resources:

- [Mapping in the UI](https://docs.n8n.io/data/data-mapping/data-mapping-ui/)
- [Mapping in the expressions editor](https://docs.n8n.io/data/data-mapping/data-mapping-expressions/)
- [Item linking in the Code node](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-code-node/)
- [Item linking errors](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-errors/)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top