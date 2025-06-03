---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan/"
title: "Wekan node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan/#wekan-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.wekan.md "Edit this page")

# Wekan node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan/\#wekan-node "Permanent link")

Use the Wekan node to automate work in Wekan, and integrate Wekan with other applications. n8n has built-in support for a wide range of Wekan features, including creating, updating, deleting, and getting boards and cards.

On this page, you'll find a list of operations the Wekan node supports and links to more resources.

Credentials

Refer to [Wekan credentials](https://docs.n8n.io/integrations/builtin/credentials/wekan/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan/\#operations "Permanent link")

- Board
  - Create a new board
  - Delete a board
  - Get the data of a board
  - Get all user boards
- Card
  - Create a new card
  - Delete a card
  - Get a card
  - Get all cards
  - Update a card
- Card Comment
  - Create a comment on a card
  - Delete a comment from a card
  - Get a card comment
  - Get all card comments
- Checklist
  - Create a new checklist
  - Delete a checklist
  - Get the data of a checklist
  - Returns all checklists for the card
- Checklist Item
  - Delete a checklist item
  - Get a checklist item
  - Update a checklist item
- List
  - Create a new list
  - Delete a list
  - Get the data of a list
  - Get all board lists

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan/\#templates-and-examples "Permanent link")

[Browse Wekan integration templates](https://n8n.io/integrations/wekan/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

## Load all the parameters for the node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan/\#load-all-the-parameters-for-the-node "Permanent link")

To load all the parameters, for example, Author ID, you need to give admin permissions to the user. Refer to the [Wekan documentation](https://github.com/wekan/wekan/wiki/Features#members-click-member-initials-or-avatar--permissions-adminnormalcomment-only) to learn how to change permissions.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top