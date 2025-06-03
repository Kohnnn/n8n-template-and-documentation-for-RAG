---
url: "https://docs.n8n.io/flow-logic/"
title: "Flow logic | n8n Docs "
---

[Skip to content](https://docs.n8n.io/flow-logic/#flow-logic)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/flow-logic/index.md "Edit this page")

# Flow logic [\#](https://docs.n8n.io/flow-logic/\#flow-logic "Permanent link")

n8n allows you to represent complex logic in your workflows.

This section covers:

- [Splitting with conditionals](https://docs.n8n.io/flow-logic/splitting/)
- [Merging data](https://docs.n8n.io/flow-logic/merging/)
- [Looping](https://docs.n8n.io/flow-logic/looping/)
- [Waiting](https://docs.n8n.io/flow-logic/waiting/)
- [Sub-workflows](https://docs.n8n.io/flow-logic/subworkflows/)
- [Error handling](https://docs.n8n.io/flow-logic/error-handling/)
- [Execution order in multi-branch workflows](https://docs.n8n.io/flow-logic/execution-order/)

## Related sections [\#](https://docs.n8n.io/flow-logic/\#related-sections "Permanent link")

You need some understanding of [Data](https://docs.n8n.io/data/) in n8n, including [Data structure](https://docs.n8n.io/data/data-structure/) and [Data flow within nodes](https://docs.n8n.io/data/data-flow-nodes/).

When building your logic, you'll use n8n's [Core nodes](https://docs.n8n.io/integrations/builtin/core-nodes/), including:

- Splitting: [IF](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/) and [Switch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch/).
- Merging: [Merge](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/), [Compare Datasets](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets/), and [Code](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/).
- Looping: [IF](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/) and [Loop Over Items](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches/).
- Waiting: [Wait](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/).
- Creating sub-workflows: [Execute Workflow](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow/) and [Execute Workflow Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger/).
- Error handling: [Stop And Error](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror/) and [Error Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top