---
url: "https://docs.n8n.io/data/"
title: "Data | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/data/#data)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/index.md "Edit this page")

# Data [\#](https://docs.n8n.io/data/\#data "Permanent link")

Data is the information that n8n nodes receive and process. For basic usage of n8n you don't need to understand data structures and manipulation. However, it becomes important if you want to:

- Create your own node
- Write custom [expressions](https://docs.n8n.io/glossary/#expression-n8n)
- Use the Function or Function Item node

This section covers:

- [Data structure](https://docs.n8n.io/data/data-structure/)
- [Data flow within nodes](https://docs.n8n.io/data/data-flow-nodes/)
- [Transforming data](https://docs.n8n.io/data/transforming-data/)
- [Process data using code](https://docs.n8n.io/data/code/)
- [Pinning](https://docs.n8n.io/data/data-pinning/) and [editing](https://docs.n8n.io/data/data-editing/) data during workflow development.
- [Data mapping](https://docs.n8n.io/data/data-mapping/) and [Item linking](https://docs.n8n.io/data/data-mapping/data-item-linking/): how data items link to each other.

## Related resources [\#](https://docs.n8n.io/data/\#related-resources "Permanent link")

### Data transformation nodes [\#](https://docs.n8n.io/data/\#data-transformation-nodes "Permanent link")

n8n provides a collection of nodes to transform data:

- [Aggregate](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate/): take separate items, or portions of them, and group them together into individual items.
- [Limit](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate/): remove items beyond a defined maximum number.
- [Remove Duplicates](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/): identify and delete items that are identical across all fields or a subset of fields.
- [Sort](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort/): organize lists of in a desired ordering, or generate a random selection.
- [Split Out](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout/): separate a single data item containing a list into multiple items.
- [Summarize](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.summarize/): aggregate items together, in a manner similar to Excel pivot tables.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top