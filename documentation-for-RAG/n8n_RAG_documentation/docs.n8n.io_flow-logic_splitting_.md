---
url: "https://docs.n8n.io/flow-logic/splitting/"
title: "Splitting with conditionals | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/flow-logic/splitting/#splitting-workflows-with-conditional-nodes)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/flow-logic/splitting.md "Edit this page")

# Splitting workflows with conditional nodes [\#](https://docs.n8n.io/flow-logic/splitting/\#splitting-workflows-with-conditional-nodes "Permanent link")

Splitting uses the [IF](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/) or [Switch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch/) nodes. It turns a single-branch workflow into a multi-branch workflow. This is a key piece of representing complex logic in n8n.

Compare these workflows:

[!["Diagram representing two workflows. One has three steps and follows a linear process, with a user submitting a bug, and the workflow emailing a support team. The second workflow starts the same way, but then splits depending on whether the user marked the issue as urgent. It then splits again depending on the user's support plan"](https://docs.n8n.io/_images/flow-logic/splitting/single-multi-branch-workflow.png)](https://docs.n8n.io/_images/flow-logic/splitting/single-multi-branch-workflow.png)

This is the power of splitting and conditional nodes in n8n.

Refer to the [IF](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/) or [Switch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch/) documentation for usage details.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top