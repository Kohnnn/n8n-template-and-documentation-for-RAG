---
url: "https://docs.n8n.io/flow-logic/execution-order/"
title: "Execution order in multi-branch workflows | n8n Docs "
---

[Skip to content](https://docs.n8n.io/flow-logic/execution-order/#execution-order-in-multi-branch-workflows)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/flow-logic/execution-order.md "Edit this page")

# Execution order in multi-branch workflows [\#](https://docs.n8n.io/flow-logic/execution-order/\#execution-order-in-multi-branch-workflows "Permanent link")

n8n's node execution order depends on the version of n8n you're using:

- For workflows created before version 1.0: n8n executes the first node of each branch, then the second node of each branch, and so on.
- For workflows created in version 1.0 and above: executes each branch in turn, completing one branch before starting another. n8n orders the branches based on their position on the [canvas](https://docs.n8n.io/glossary/#canvas-n8n), from topmost to bottommost. If two branches are at the same height, the leftmost branch executes first.

You can change the execution order in your [workflow settings](https://docs.n8n.io/workflows/settings/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top