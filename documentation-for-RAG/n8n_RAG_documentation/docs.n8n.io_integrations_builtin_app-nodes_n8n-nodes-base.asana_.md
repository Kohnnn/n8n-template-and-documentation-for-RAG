---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana/"
title: "Asana node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana/#asana-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.asana.md "Edit this page")

# Asana node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana/\#asana-node "Permanent link")

Use the Asana node to automate work in Asana, and integrate Asana with other applications. n8n has built-in support for a wide range of Asana features, including creating, updating, deleting, and getting users, tasks, projects, and subtasks.

On this page, you'll find a list of operations the Asana node supports and links to more resources.

Credentials

Refer to [Asana credentials](https://docs.n8n.io/integrations/builtin/credentials/asana/) for guidance on setting up authentication.

Update to 1.22.2 or above

Due to changes in Asana's API, some operations in this node stopped working on 17th January 2023. Upgrade to n8n 1.22.2 or above.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana/\#operations "Permanent link")

- Project
  - Create a new project
  - Delete a project
  - Get a project
  - Get all projects
  - Update a project
- Subtask
  - Create a subtask
  - Get all subtasks
- Task
  - Create a task
  - Delete a task
  - Get a task
  - Get all tasks
  - Move a task
  - Search for tasks
  - Update a task
- Task Comment
  - Add a comment to a task
  - Remove a comment from a task
- Task Tag
  - Add a tag to a task
  - Remove a tag from a task
- Task Project
  - Add a task to a project
  - Remove a task from a project
- User
  - Get a user
  - Get all users

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana/\#templates-and-examples "Permanent link")

**Automated Customer Service Ticket Creation & Notifications with Asana & WhatsApp**

by Bela

[View template details](https://n8n.io/workflows/2237-automated-customer-service-ticket-creation-and-notifications-with-asana-and-whatsapp/)

**Sync tasks data between Notion and Asana**

by n8n Team

[View template details](https://n8n.io/workflows/1769-sync-tasks-data-between-notion-and-asana/)

**Receive updates when an event occurs in Asana**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/654-receive-updates-when-an-event-occurs-in-asana/)

[Browse Asana integration templates](https://n8n.io/integrations/asana/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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