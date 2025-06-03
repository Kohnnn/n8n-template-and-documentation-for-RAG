---
url: "https://docs.n8n.io/code/"
title: "Code in n8n Documentation and Guides | n8n Docs "
---

[Skip to content](https://docs.n8n.io/code/#code-in-n8n)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/index.md "Edit this page")

# Code in n8n [\#](https://docs.n8n.io/code/\#code-in-n8n "Permanent link")

n8n is a low-code tool. This means you can do a lot without code, then add code when needed.

## Code in your workflows [\#](https://docs.n8n.io/code/\#code-in-your-workflows "Permanent link")

There are two places in your workflows where you can use code:

- **Expressions**

Use [expressions](https://docs.n8n.io/glossary/#expression-n8n) to transform [data](https://docs.n8n.io/data/) in your nodes. You can use JavaScript in expressions, as well as n8n's [Built-in methods and variables](https://docs.n8n.io/code/builtin/overview/) and [Data transformation functions](https://docs.n8n.io/code/builtin/data-transformation-functions/).

[Expressions](https://docs.n8n.io/code/expressions/)

- **Code node**

Use the Code node to add JavaScript or Python to your workflow.

[Code node](https://docs.n8n.io/code/code-node/)


## Other technical resources [\#](https://docs.n8n.io/code/\#other-technical-resources "Permanent link")

These are features that are relevant to technical users.

### Technical nodes [\#](https://docs.n8n.io/code/\#technical-nodes "Permanent link")

n8n provides core nodes, which simplify adding key functionality such as API requests, webhooks, scheduling, and file handling.

- **Write a backend**

The [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/), [Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/), and [Code](https://docs.n8n.io/code/code-node/) nodes help you make API calls, respond to webhooks, and write any JavaScript in your workflow.

Use this do things like [Create an API endpoint](https://n8n.io/workflows/1750-creating-an-api-endpoint/).

[Core nodes](https://docs.n8n.io/integrations/builtin/core-nodes/)

- **Represent complex logic**

You can build complex flows, using nodes like [If](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/), [Switch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch/), and [Merge](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/) nodes.

[Flow logic](https://docs.n8n.io/flow-logic/)


### Other developer resources [\#](https://docs.n8n.io/code/\#other-developer-resources "Permanent link")

- **The n8n API**

n8n provides an API, where you can programmatically perform many of the same tasks as you can in the GUI. There's an [n8n API node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8n/) to access the API in your workflows.

[API](https://docs.n8n.io/api/)

- **Self-host**

You can self-host n8n. This keeps your data on your own infrastructure.

[Hosting](https://docs.n8n.io/hosting/)

- **Build your own nodes**

You can build custom nodes, install them on your n8n instance, and publish them to [npm](https://www.npmjs.com/).

[Creating nodes](https://docs.n8n.io/integrations/creating-nodes/overview/)


Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top