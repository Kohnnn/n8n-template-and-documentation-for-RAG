---
url: "https://docs.n8n.io/integrations/"
title: "n8n Integrations Documentation and Guides | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/#integrations)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/index.md "Edit this page")

# Integrations [\#](https://docs.n8n.io/integrations/\#integrations "Permanent link")

n8n calls integrations nodes.

Nodes are the building blocks of workflows in n8n. They're an entry point for retrieving data, a function to process data, or an exit for sending data. The data process includes filtering, recomposing, and changing data. There can be one or several nodes for your API, service or app. You can connect multiple nodes, which allows you to create complex workflows.

## Built-in nodes [\#](https://docs.n8n.io/integrations/\#built-in-nodes "Permanent link")

n8n includes a collection of built-in integrations. Refer to [Built-in nodes](https://docs.n8n.io/integrations/builtin/node-types/) for documentation on all n8n's built-in nodes.

## Community nodes [\#](https://docs.n8n.io/integrations/\#community-nodes "Permanent link")

As well as using the built-in nodes, you can also install community-built nodes. Refer to [Community nodes](https://docs.n8n.io/integrations/community-nodes/installation/) for more information.

## Credential-only nodes and custom operations [\#](https://docs.n8n.io/integrations/\#credential-only-nodes-and-custom-operations "Permanent link")

One of the most complex parts of setting up [API](https://docs.n8n.io/glossary/#api) calls is managing authentication. n8n provides [credentials](https://docs.n8n.io/glossary/#credential-n8n) support for operations and services beyond those supported by built-in nodes.

- Custom operations for existing nodes: n8n supplies hundreds of nodes to create workflows that link multiple products. However, some nodes don't include all the possible operations supported by a product's API. You can work around this by making a custom API call using the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) node.
- Credential-only nodes: n8n includes credential-only nodes. These are integrations where n8n supports setting up credentials for use in the HTTP Request node, but doesn't provide a standalone node. You can find a credential-only node in the nodes panel, as you would for any other integration.

Refer to [Custom operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

## Generic integrations [\#](https://docs.n8n.io/integrations/\#generic-integrations "Permanent link")

If you need to connect to a service where n8n doesn't have a node, or a credential-only node, you can still use the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) node. Refer to the node page for details on how to set up authentication and create your API call.

## Where to go next [\#](https://docs.n8n.io/integrations/\#where-to-go-next "Permanent link")

- If you want to create your own node, head over to the [Creating Nodes](https://docs.n8n.io/integrations/creating-nodes/overview/) section.
- Check out [Community nodes](https://docs.n8n.io/integrations/community-nodes/usage/) to learn about installing and managing community-built nodes.
- If you'd like to learn more about the different nodes in n8n, their functionalities and example usage, check out n8n's node libraries: [Core nodes](https://docs.n8n.io/integrations/builtin/core-nodes/), [Actions](https://docs.n8n.io/integrations/builtin/app-nodes/), and [Triggers](https://docs.n8n.io/integrations/builtin/trigger-nodes/).
- If you'd like to learn how to add the credentials for the different nodes, head over to the [Credentials](https://docs.n8n.io/integrations/builtin/credentials/) section.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top