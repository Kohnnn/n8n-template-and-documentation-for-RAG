---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom/"
title: "monday.com node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom/#mondaycom-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom.md "Edit this page")

# monday.com node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom/\#mondaycom-node "Permanent link")

Use the monday.com node to automate work in monday.com, and integrate monday.com with other applications. n8n has built-in support for a wide range of monday.com features, including creating a new board, and adding, deleting, and getting items on the board.

On this page, you'll find a list of operations the monday.com node supports and links to more resources.

Minimum required version

This node requires n8n version 1.22.6 or above.

Credentials

Refer to [monday.com credentials](https://docs.n8n.io/integrations/builtin/credentials/mondaycom/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom/\#operations "Permanent link")

- Board
  - Archive a board
  - Create a new board
  - Get a board
  - Get all boards
- Board Column
  - Create a new column
  - Get all columns
- Board Group
  - Delete a group in a board
  - Create a group in a board
  - Get list of groups in a board
- Board Item
  - Add an update to an item.
  - Change a column value for a board item
  - Change multiple column values for a board item
  - Create an item in a board's group
  - Delete an item
  - Get an item
  - Get all items
  - Get items by column value
  - Move item to group

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom/\#templates-and-examples "Permanent link")

**Create ticket on specific customer messages in Telegram**

by tanaypant

[View template details](https://n8n.io/workflows/368-create-ticket-on-specific-customer-messages-in-telegram/)

**Microsoft Outlook AI Email Assistant with contact support from Monday and Airtable**

by Cognitive Creators

[View template details](https://n8n.io/workflows/2809-microsoft-outlook-ai-email-assistant-with-contact-support-from-monday-and-airtable/)

**Retrieve a Monday.com row and all data in a single node**

by Joey D’Anna

[View template details](https://n8n.io/workflows/2086-retrieve-a-mondaycom-row-and-all-data-in-a-single-node/)

[Browse monday.com integration templates](https://n8n.io/integrations/mondaycom/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top