---
url: "https://docs.n8n.io/code/builtin/current-node-input/"
title: "Current node input | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/builtin/current-node-input/#current-node-input)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/current-node-input.md "Edit this page")

# Current node input [\#](https://docs.n8n.io/code/builtin/current-node-input/\#current-node-input "Permanent link")

Methods for working with the input of the current node. Some methods and variables aren't available in the Code node.

Python support

You can use Python in the Code node. It isn't available in expressions.

[JavaScript](https://docs.n8n.io/code/builtin/current-node-input/#__tabbed_1_1)[Python](https://docs.n8n.io/code/builtin/current-node-input/#__tabbed_1_2)

| Method | Description | Available in Code node? |
| --- | --- | --- |
| `$binary` | Shorthand for `$input.item.binary`. Incoming binary data from a node | ![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) |
| `$input.item` | The input item of the current node that's being processed. Refer to [Item linking](https://docs.n8n.io/data/data-mapping/data-item-linking/) for more information on paired items and item linking. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) |
| `$input.all()` | All input items in current node. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) |
| `$input.first()` | First input item in current node. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) |
| `$input.last()` | Last input item in current node. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) |
| `$input.params` | Object containing the query settings of the previous node. This includes data such as the operation it ran, result limits, and so on. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) |
| `$json` | Shorthand for `$input.item.json`. Incoming JSON data from a node. Refer to [Data structure](https://docs.n8n.io/data/data-structure/) for information on item structure. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) (when running once for each item) |
| `$input.context.noItemsLeft` | Boolean. Only available when working with the Loop Over Items node. Provides information about what's happening in the node. Use this to determine whether the node is still processing items. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) |

| Method | Description |
| --- | --- |
| `_input.item` | The input item of the current node that's being processed. Refer to [Item linking](https://docs.n8n.io/data/data-mapping/data-item-linking/) for more information on paired items and item linking. |
| `_input.all()` | All input items in current node. |
| `_input.first()` | First input item in current node. |
| `_input.last()` | Last input item in current node. |
| `_input.params` | Object containing the query settings of the previous node. This includes data such as the operation it ran, result limits, and so on. |
| `_json` | Shorthand for `_input.item.json`. Incoming JSON data from a node. Refer to [Data structure](https://docs.n8n.io/data/data-structure/) for information on item structure. Available when you set **Mode** to **Run Once for Each Item**. |
| `_input.context.noItemsLeft` | Boolean. Only available when working with the Loop Over Items node. Provides information about what's happening in the node. Use this to determine whether the node is still processing items. |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top