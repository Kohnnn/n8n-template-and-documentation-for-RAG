---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup/"
title: "ClickUp node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup/#clickup-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.clickup.md "Edit this page")

# ClickUp node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup/\#clickup-node "Permanent link")

Use the ClickUp node to automate work in ClickUp, and integrate ClickUp with other applications. n8n has built-in support for a wide range of ClickUp features, including creating, getting, deleting, and updating folders, checklists, tags, comments, and goals.

On this page, you'll find a list of operations the ClickUp node supports and links to more resources.

Credentials

Refer to [ClickUp credentials](https://docs.n8n.io/integrations/builtin/credentials/clickup/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup/\#operations "Permanent link")

- Checklist
  - Create a checklist
  - Delete a checklist
  - Update a checklist
- Checklist Item
  - Create a checklist item
  - Delete a checklist item
  - Update a checklist item
- Comment
  - Create a comment
  - Delete a comment
  - Get all comments
  - Update a comment
- Folder
  - Create a folder
  - Delete a folder
  - Get a folder
  - Get all folders
  - Update a folder
- Goal
  - Create a goal
  - Delete a goal
  - Get a goal
  - Get all goals
  - Update a goal
- Goal Key Result
  - Create a key result
  - Delete a key result
  - Update a key result
- List
  - Create a list
  - Retrieve list's custom fields
  - Delete a list
  - Get a list
  - Get all lists
  - Get list members
  - Update a list
- Space Tag
  - Create a space tag
  - Delete a space tag
  - Get all space tags
  - Update a space tag
- Task
  - Create a task
  - Delete a task
  - Get a task
  - Get all tasks
  - Get task members
  - Set a custom field
  - Update a task
- Task List
  - Add a task to a list
  - Remove a task from a list
- Task Tag
  - Add a tag to a task
  - Remove a tag from a task
- Task Dependency
  - Create a task dependency
  - Delete a task dependency
- Time Entry
  - Create a time entry
  - Delete a time entry
  - Get a time entry
  - Get all time entries
  - Start a time entry
  - Stop the current running timer
  - Update a time Entry
- Time Entry Tag
  - Add tag to time entry
  - Get all time entry tags
  - Remove tag from time entry

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup/\#templates-and-examples "Permanent link")

**Zoom AI Meeting Assistant creates mail summary, ClickUp tasks and follow-up call**

by Friedemann Schuetz

[View template details](https://n8n.io/workflows/2800-zoom-ai-meeting-assistant-creates-mail-summary-clickup-tasks-and-follow-up-call/)

**Create a task in ClickUp**

by tanaypant

[View template details](https://n8n.io/workflows/485-create-a-task-in-clickup/)

**Sync Notion database pages as ClickUp tasks**

by n8n Team

[View template details](https://n8n.io/workflows/1835-sync-notion-database-pages-as-clickup-tasks/)

[Browse ClickUp integration templates](https://n8n.io/integrations/clickup/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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