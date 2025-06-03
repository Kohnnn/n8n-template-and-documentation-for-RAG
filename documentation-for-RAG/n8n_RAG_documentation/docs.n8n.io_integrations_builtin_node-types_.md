---
url: "https://docs.n8n.io/integrations/builtin/node-types/"
title: "Node types | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/node-types/#built-in-integrations)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/node-types.md "Edit this page")

# Built-in integrations [\#](https://docs.n8n.io/integrations/builtin/node-types/\#built-in-integrations "Permanent link")

This section contains the [node](https://docs.n8n.io/glossary/#node-n8n) library: reference documentation for every built-in node in n8n, and their credentials.

## Node operations: Triggers and Actions [\#](https://docs.n8n.io/integrations/builtin/node-types/\#node-operations-triggers-and-actions "Permanent link")

When you add a node to a workflow, n8n displays a list of available operations. An operation is something a node does, such as getting or sending data.

There are two types of operation:

- Triggers start a workflow in response to specific events or conditions in your services. When you select a Trigger, n8n adds a trigger node to your workflow, with the Trigger operation you chose pre-selected. When you search for a node in n8n, Trigger operations have a bolt icon ![Trigger icon](https://docs.n8n.io/_images/common-icons/trigger.png).
- Actions are operations that represent specific tasks within a workflow, which you can use to manipulate data, perform operations on external systems, and trigger events in other systems as part of your workflows. When you select an Action, n8n adds a node to your workflow, with the Action operation you chose pre-selected.

## Core nodes [\#](https://docs.n8n.io/integrations/builtin/node-types/\#core-nodes "Permanent link")

Core nodes can be actions or [triggers](https://docs.n8n.io/glossary/#trigger-node-n8n). Whereas most nodes connect to a specific external service, core nodes provide functionality such as logic, scheduling, or generic API calls.

## Cluster nodes [\#](https://docs.n8n.io/integrations/builtin/node-types/\#cluster-nodes "Permanent link")

[Cluster nodes](https://docs.n8n.io/glossary/#cluster-node-n8n) are node groups that work together to provide functionality in an n8n workflow. Instead of using a single node, you use a [root node](https://docs.n8n.io/glossary/#root-node-n8n) and one or more [sub-nodes](https://docs.n8n.io/glossary/#sub-node-n8n) that extend the functionality of the node.

[![Screenshot of a workflow with a root node and two sub-nodes](https://docs.n8n.io/_images/integrations/builtin/cluster-nodes/root-sub-nodes.png)](https://docs.n8n.io/_images/integrations/builtin/cluster-nodes/root-sub-nodes.png)

## Credentials [\#](https://docs.n8n.io/integrations/builtin/node-types/\#credentials "Permanent link")

External services need a way to identify and authenticate users. This data can range from an API key over an email/password combination to a long multi-line private key. You can save these in n8n as [credentials](https://docs.n8n.io/glossary/#credential-n8n).

Nodes in n8n can then request that credential information. As another layer of security, only node types with specific access rights can access the credentials.

To make sure that the data is secure, it gets saved to the database encrypted. n8n uses a random personal encryption key, which it automatically generates on the first run of n8n and then saved under `~/.n8n/config`.

To learn more about creating, managing, and sharing credentials, refer to [Manage credentials](https://docs.n8n.io/credentials/).

## Community nodes [\#](https://docs.n8n.io/integrations/builtin/node-types/\#community-nodes "Permanent link")

n8n supports custom nodes built by the community. Refer to [Community nodes](https://docs.n8n.io/integrations/community-nodes/installation/) for guidance on installing and using these nodes.

For help building your own custom nodes, and publish them to [npm](https://www.npmjs.com/), refer to [Creating nodes](https://docs.n8n.io/integrations/creating-nodes/overview/) for more information.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top