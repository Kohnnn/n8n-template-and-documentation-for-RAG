---
url: "https://docs.n8n.io/data/transforming-data/"
title: "Transforming data | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/data/transforming-data/#transforming-data)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/transforming-data.md "Edit this page")

# Transforming data [\#](https://docs.n8n.io/data/transforming-data/\#transforming-data "Permanent link")

n8n uses a predefined [data structure](https://docs.n8n.io/data/data-structure/) that allows all nodes to process incoming data correctly.

Your incoming data may have a different data structure, in which case you will need to transform it to allow each item to be processed individually.

For example, the image below shows the output of an [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) node that returns data incompatible with n8n's data structure. The node returns the data and displays that only one item was returned.

[![HTTP Request node output](https://docs.n8n.io/_images/data/transforming-data/HTTPRequest_output.png)](https://docs.n8n.io/_images/data/transforming-data/HTTPRequest_output.png)

To transform this kind of structure into the n8n data structure you can use the data transformation nodes:

- [Aggregate](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate/): take separate items, or portions of them, and group them together into individual items.
- [Limit](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit/): remove items beyond a defined maximum number.
- [Remove Duplicates](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/): identify and delete items that are identical across all fields or a subset of fields.
- [Sort](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort/): organize lists of in a desired ordering, or generate a random selection.
- [Split Out](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout/): separate a single data item containing a list into multiple items.
- [Summarize](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.summarize/): aggregate items together, in a manner similar to Excel pivot tables.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top