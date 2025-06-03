## Explore n8n Docs: Your Resource for Workflow Automation and Integrations | n8n Docs
Original URL: https://docs.n8n.io/

# Welcome to n8n Docs

This is the documentation for [n8n](https://n8n.io/), a [fair-code](https://faircode.io/) licensed workflow automation tool that combines AI capabilities with business process automation.

It covers everything from setup to usage and development. It's a work in progress and all [contributions](https://docs.n8n.io/help-community/contributing/) are welcome.

## Where to start

- **Quickstarts**

Jump in with n8n's quickstart guides.

[Try it out](https://docs.n8n.io/try-it-out/)

- **Choose the right n8n for you**

Cloud, npm, self-host . . .

[Options](https://docs.n8n.io/choose-n8n/)

- **Explore integrations**

Browse n8n's integrations library.

[Find your apps](https://docs.n8n.io/integrations/)

- **Build AI functionality**

n8n supports building AI functionality and tools.

[Advanced AI](https://docs.n8n.io/advanced-ai/)

## About n8n

n8n (pronounced n-eight-n) helps you to connect any app with an API with any other, and manipulate its data with little or no code.

- Customizable: highly flexible workflows and the option to build custom nodes.
- Convenient: use the npm or Docker to try out n8n, or the Cloud hosting option if you want us to handle the infrastructure.
- Privacy-focused: self-host n8n for privacy and security.

## n8n v1.0 migration guide | n8n Docs
Original URL: https://docs.n8n.io/1-0-migration-checklist/

# n8n v1.0 migration guide

This document provides a summary of what you should be aware of before updating to version 1.0 of n8n.

The release of n8n 1.0 marks a milestone in n8n's journey to make n8n available for demanding production environments. Version 1.0 represents the hard work invested over the last four years to make n8n the most accessible, powerful, and versatile automation tool. n8n 1.0 is now ready for use in production.

## New features

### Python support in the Code node

Although JavaScript remains the default language, you can now also select Python as an option in the [Code node](https://docs.n8n.io/code/code-node/) and even make use of [many Python modules](https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide). Note that Python is unavailable in Code nodes added to a workflow before v1.0.

[PR #4295](https://github.com/n8n-io/n8n/pull/4295), [PR #6209](https://github.com/n8n-io/n8n/pull/6209)

### Execution order

n8n 1.0 introduces a new execution order for multi-branch workflows:

In multi-branch workflows, n8n needs to determine the order in which to execute nodes on branches. Previously, n8n executed the first node of each branch, then the second of each branch, and so on (breadth-first). The new execution order ensures that each branch executes completely before starting the next one (depth-first). Branches execute based on their position on the canvas, from top to bottom. If two branches are at the same height, the leftmost one executes first.

n8n used to execute multi-input nodes as long as they received data on their first input. Nodes connected to the second input of multi-input nodes automatically executed regardless of whether they received data. The new execution order introduced in n8n 1.0 simplifies this behavior: Nodes are now executed only when they receive data, and multi-input nodes require data on at least one of their inputs to execute.

Your existing workflows will use the legacy order, while new workflows will execute using the v1 order. You can configure the execution order for each workflow in [workflow settings](https://docs.n8n.io/workflows/settings/).

[PR #4238](https://github.com/n8n-io/n8n/pull/4238), [PR #6246](https://github.com/n8n-io/n8n/pull/6246), [PR #6507](https://github.com/n8n-io/n8n/pull/6507)

## Deprecations

### MySQL and MariaDB

n8n has removed support for MySQL and MariaDB as storage backends for n8n. These database systems are used by only a few users, yet they require continuous development and maintenance efforts. n8n recommends migrating to PostgreSQL for better compatibility and long-term support.

[PR #6189](https://github.com/n8n-io/n8n/pull/6189)

### EXECUTIONS_PROCESS and "own" mode

Previously, you could use the `EXECUTIONS_PROCESS` environment variable to specify whether executions should run in the `main` process or in their `own` processes. This option and `own` mode are now deprecated and will be removed in a future version of n8n. This is because it led to increased code complexity while offering marginal benefits. Starting from n8n 1.0, `main` will be the new default.

Note that executions start much faster in `main` mode than in `own` mode. However, if a workflow consumes more memory than is available, it might crash the entire n8n application instead of just the worker thread. To mitigate this, make sure to allocate enough system resources or configure [queue mode](https://docs.n8n.io/hosting/scaling/queue-mode/) to distribute executions among multiple workers.

[PR #6196](https://github.com/n8n-io/n8n/pull/6196)

## Breaking changes

### Docker

#### Permissions change

When using Docker-based deployments, the n8n process is now run by the user `node` instead of `root`. This change increases security.

If permission errors appear in your n8n container logs when starting n8n, you may need to update the permissions by executing the following command on the Docker host:

|     |     |
| --- | --- |
| ```
1
``` | ```
docker run --rm -it --user root -v ~/.n8n:/home/node/.n8n --entrypoint chown n8nio/base:16 -R node:node /home/node/.n8n
``` |

#### Image removal

We've removed the Debian and RHEL images. If you were using these you need to change the image you use. This shouldn't result in any errors unless you were making a custom image based on one of those images.

#### Entrypoint change

The entrypoint for the container has changed and you no longer need to specify the n8n command. If you were previously running `n8n worker --concurrency=5` it's now `worker --concurrency=5`

[PR #6365](https://github.com/n8n-io/n8n/pull/6365)

### Workflow failures due to expression errors

Workflow executions may fail due to syntax or runtime errors in expressions, such as those that reference non-existent nodes. While expressions already throw errors on the frontend, this change ensures that n8n also throws errors on the backend, where they were previously silently ignored. To receive notifications of failing workflows, n8n recommends setting up an "error workflow" under workflow settings.

[PR #6352](https://github.com/n8n-io/n8n/pull/6352)

### Mandatory owner account

This change makes [User Management](https://docs.n8n.io/user-management/) mandatory and removes support for other authentication methods, such as BasicAuth and External JWT. Note that the number of permitted users on [n8n.cloud](https://n8n.cloud/) or custom plans still varies depending on your subscription.

[PR #6362](https://github.com/n8n-io/n8n/pull/6362)

### Directory for installing custom nodes

n8n will no longer load custom nodes from its global `node_modules` directory. Instead, you must install (or link) them to `~/.n8n/custom` (or a directory defined by `N8N_CUSTOM_EXTENSIONS`). Custom nodes that are npm packages will be located in `~/.n8n/nodes`.
If you have custom nodes that were linked using `npm link` into the global `node_modules` directory, you need to link them again, into `~/.n8n/nodes` instead.

[PR #6396](https://github.com/n8n-io/n8n/pull/6396)

### WebSockets

The `N8N_PUSH_BACKEND` environment variable can be used to configure one of two available methods for pushing updates to the user interface: `sse` and `websocket`. Starting with n8n 1.0, `websocket` is the default method.

[PR #6196](https://github.com/n8n-io/n8n/pull/6196)

### Date transformation functions

n8n provides various transformation functions that operate on dates. These functions may return either a JavaScript `Date` or a Luxon `DateTime` object. With the new behavior, the return type always matches the input. If you call a date transformation function on a `Date`, it returns a `Date`. Similarly, if you call it on a `DateTime` object, it returns a `DateTime` object.

To identify any workflows and nodes that might be impacted by this change, you can use this [utility workflow](https://n8n.io/workflows/1929-v1-helper-find-params-with-affected-expressions/).

For more information about date transformation functions, please refer to the [official documentation](https://docs.n8n.io/code/builtin/data-transformation-functions/dates/).

[PR #6435](https://github.com/n8n-io/n8n/pull/6435)

### Execution data retention

Starting from n8n 1.0, all successful, failed, and manual workflow executions will be saved by default. These settings can be modified for each workflow under "Workflow Settings," or globally using the respective environment variables. Additionally, the `EXECUTIONS_DATA_PRUNE` setting will be enabled by default, with `EXECUTIONS_DATA_PRUNE_MAX_COUNT` set to 10,000. These default settings are designed to prevent performance degradation when using SQLite. Make sure to configure them according to your individual requirements and system capacity.

[PR #6577](https://github.com/n8n-io/n8n/pull/6577)

### Removed N8N_USE_DEPRECATED_REQUEST_LIB

The legacy `request` library has been deprecated for some time now. As of n8n 1.0, the ability to fall back to it in the HTTP Request node by setting the `N8N_USE_DEPRECATED_REQUEST_LIB` environment variable has been fully removed. The HTTP Request node will now always use the new `HttpRequest` interface.

If you build custom nodes, refer to [HTTP request helpers](https://docs.n8n.io/integrations/creating-nodes/build/reference/http-helpers/) for more information on migrating to the new interface.

[PR #6413](https://github.com/n8n-io/n8n/pull/6413)

### Removed WEBHOOK_TUNNEL_URL

As of version 0.227.0, n8n has renamed the `WEBHOOK_TUNNEL_URL` configuration option to `WEBHOOK_URL`. In n8n 1.0, `WEBHOOK_TUNNEL_URL` has been removed. Update your setup to reflect the new name. For more information about this configuration option, refer to [the docs](https://docs.n8n.io/hosting/configuration/configuration-examples/webhook-url/).

[PR #1408](https://github.com/n8n-io/n8n/pull/1408)

### Remove Node 16 support

n8n now requires Node 18.17.0 or above.

## Updating to n8n 1.0

1. Create a full backup of n8n.
2. n8n recommends updating to the latest n8n 0.x release before updating to n8n 1.x. This will allow you to pinpoint any potential issues to the correct release. Once you have verified that n8n 0.x starts up without any issues, proceed to the next step.
3. Carefully read the [Deprecations](https://docs.n8n.io/1-0-migration-checklist/#deprecations) and [Breaking Changes](https://docs.n8n.io/1-0-migration-checklist/#breaking-changes) sections above to assess how they may affect your setup.
4. Update to n8n 1.0:
   - During beta (before July 24th 2023): If using Docker, pull the `next` Docker image.
   - After July 24th 2023: If using Docker, pull the `latest` Docker image.
5. If you encounter any issues, redeploy the previous n8n version and restore the backup.

## Reporting issues

If you encounter any issues during the process of updating to n8n 1.0, please seek help in the community [forum](https://community.n8n.io/).

## Thank you

We would like to take a moment to express our gratitude to all of our users for their continued support and feedback. Your contributions are invaluable in helping us make n8n the best possible automation tool. We're excited to continue working with you as we move forward with the release of version 1.0 and beyond. Thank you for being a part of our journey!

## n8n Advanced AI Documentation and Guides | n8n Docs
Original URL: https://docs.n8n.io/advanced-ai/

# Advanced AI

Build AI functionality using n8n: from creating your own chat bot, to using AI to process documents and data from other sources.

Feature availability

This feature is available on Cloud and self-hosted n8n, in version 1.19.4 and above.

- **Get started**

Work through the short tutorial to learn the basics of building AI workflows in n8n.

[Tutorial](https://docs.n8n.io/advanced-ai/intro-tutorial/)

- **Use a Starter Kit**

Try n8n's Self-hosted AI Starter Kit to quickly start building AI workflows.

[Self-hosted AI Starter Kit](https://docs.n8n.io/hosting/starter-kits/ai-starter-kit/)

- **Explore examples and concepts**

Browse examples and workflow templates to help you build. Includes explanations of important AI concepts.

[Examples](https://docs.n8n.io/advanced-ai/examples/introduction/)

- **How n8n uses LangChain**

Learn more about how n8n builds on LangChain.

[LangChain in n8n](https://docs.n8n.io/advanced-ai/langchain/overview/)

- **Browse AI templates**

Explore a wide range of AI workflow templates on the n8n website.

[AI workflows on n8n.io](https://n8n.io/workflows/?categories=25)

## Related resources

Related documentation and tools.

### Node types

This feature uses [Cluster nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/): groups of [root](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/) and [sub](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/) nodes that work together.

[Cluster nodes](https://docs.n8n.io/glossary/#cluster-node-n8n) are node groups that work together to provide functionality in an n8n workflow. Instead of using a single node, you use a [root node](https://docs.n8n.io/glossary/#root-node-n8n) and one or more [sub-nodes](https://docs.n8n.io/glossary/#sub-node-n8n) that extend the functionality of the node.

[![Screenshot of a workflow with a root node and two sub-nodes](https://docs.n8n.io/_images/integrations/builtin/cluster-nodes/root-sub-nodes.png)](https://docs.n8n.io/_images/integrations/builtin/cluster-nodes/root-sub-nodes.png)

### Workflow templates

You can browse [workflow templates](https://docs.n8n.io/glossary/#template-n8n) in-app or on the n8n website [Workflows](https://n8n.io/workflows/?categories=25,26) page.

Refer to [Templates](https://docs.n8n.io/workflows/templates/) for information on accessing templates in-app.

### Chat trigger

Use the [n8n Chat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/) to trigger a workflow based on chat interactions.

### Chatbot widget

n8n provides a chatbot widget that you can use as a frontend for AI-powered chat workflows. Refer to the [@n8n/chat npm page](https://www.npmjs.com/package/@n8n/chat) for usage information.

## Node types | n8n Docs
Original URL: https://docs.n8n.io/integrations/builtin/node-types/

# Built-in integrations

This section contains the [node](https://docs.n8n.io/glossary/#node-n8n) library: reference documentation for every built-in node in n8n, and their credentials.

## Node operations: Triggers and Actions

When you add a node to a workflow, n8n displays a list of available operations. An operation is something a node does, such as getting or sending data.

There are two types of operation:

- Triggers start a workflow in response to specific events or conditions in your services. When you select a Trigger, n8n adds a trigger node to your workflow, with the Trigger operation you chose pre-selected. When you search for a node in n8n, Trigger operations have a bolt icon ![Trigger icon](https://docs.n8n.io/_images/common-icons/trigger.png).
- Actions are operations that represent specific tasks within a workflow, which you can use to manipulate data, perform operations on external systems, and trigger events in other systems as part of your workflows. When you select an Action, n8n adds a node to your workflow, with the Action operation you chose pre-selected.

## Core nodes

Core nodes can be actions or [triggers](https://docs.n8n.io/glossary/#trigger-node-n8n). Whereas most nodes connect to a specific external service, core nodes provide functionality such as logic, scheduling, or generic API calls.

## Cluster nodes

[Cluster nodes](https://docs.n8n.io/glossary/#cluster-node-n8n) are node groups that work together to provide functionality in an n8n workflow. Instead of using a single node, you use a [root node](https://docs.n8n.io/glossary/#root-node-n8n) and one or more [sub-nodes](https://docs.n8n.io/glossary/#sub-node-n8n) that extend the functionality of the node.

[![Screenshot of a workflow with a root node and two sub-nodes](https://docs.n8n.io/_images/integrations/builtin/cluster-nodes/root-sub-nodes.png)](https://docs.n8n.io/_images/integrations/builtin/cluster-nodes/root-sub-nodes.png)

## Credentials

External services need a way to identify and authenticate users. This data can range from an API key over an email/password combination to a long multi-line private key. You can save these in n8n as [credentials](https://docs.n8n.io/glossary/#credential-n8n).

Nodes in n8n can then request that credential information. As another layer of security, only node types with specific access rights can access the credentials.

To make sure that the data is secure, it gets saved to the database encrypted. n8n uses a random personal encryption key, which it automatically generates on the first run of n8n and then saved under `~/.n8n/config`.

To learn more about creating, managing, and sharing credentials, refer to [Manage credentials](https://docs.n8n.io/credentials/).

## Community nodes

n8n supports custom nodes built by the community. Refer to [Community nodes](https://docs.n8n.io/integrations/community-nodes/installation/) for guidance on installing and using these nodes.

For help building your own custom nodes, and publish them to [npm](https://www.npmjs.com/), refer to [Creating nodes](https://docs.n8n.io/integrations/creating-nodes/overview/) for more information.

## Integrations: Built-in App Nodes
Original Context: Files related to docs.n8n.io/integrations/builtin/app-nodes/*

### Trello node documentation | n8n Docs
Original URL: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.trello/

# Trello node

Use the Trello node to automate work in Trello, and integrate Trello with other applications. n8n has built-in support for a wide range of Trello features, including creating and updating cards, and adding and removing members.

On this page, you'll find a list of operations the Trello node supports and links to more resources.

Credentials

Refer to [Trello credentials](https://docs.n8n.io/integrations/builtin/credentials/trello/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations

- Attachment
  - Create a new attachment for a card
  - Delete an attachment
  - Get the data of an attachment
  - Returns all attachments for the card
- Board
  - Create a new board
  - Delete a board
  - Get the data of a board
  - Update a board
- Board Member
  - Add
  - Get All
  - Invite
  - Remove
- Card
  - Create a new card
  - Delete a card
  - Get the data of a card
  - Update a card
- Card Comment
  - Create a comment on a card
  - Delete a comment from a card
  - Update a comment on a card
- Checklist
  - Create a checklist item
  - Create a new checklist
  - Delete a checklist
  - Delete a checklist item
  - Get the data of a checklist
  - Returns all checklists for the card
  - Get a specific checklist on a card
  - Get the completed checklist items on a card
  - Update an item in a checklist on a card
- Label
  - Add a label to a card.
  - Create a new label
  - Delete a label
  - Get the data of a label
  - Returns all labels for the board
  - Remove a label from a card.
  - Update a label.
- List
  - Archive/Unarchive a list
  - Create a new list
  - Get the data of a list
  - Get all the lists
  - Get all the cards in a list
  - Update a list

## Templates and examples

**RSS Feed News Processing and Distribution Workflow**

by PollupAI

[View template details](https://n8n.io/workflows/2785-rss-feed-news-processing-and-distribution-workflow/)

**Process Shopify new orders with Zoho CRM and Harvest**

by Lorena

[View template details](https://n8n.io/workflows/1206-process-shopify-new-orders-with-zoho-crm-and-harvest/)

**Sync Google Calendar tasks to Trello every day**

by Angel Menendez

[View template details](https://n8n.io/workflows/1118-sync-google-calendar-tasks-to-trello-every-day/)

[Browse Trello integration templates](https://n8n.io/integrations/trello/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

## Find the List ID

1. Open the Trello board that contains the list.
2. If the list doesn't have any cards, add a card to the list.
3. Open the card, add `.json` at the end of the URL, and press enter.
4. In the JSON file, you will see a field called `idList`.
5. Copy the contents of the `idList` field and paste it in the **\*List ID** field in n8n. 