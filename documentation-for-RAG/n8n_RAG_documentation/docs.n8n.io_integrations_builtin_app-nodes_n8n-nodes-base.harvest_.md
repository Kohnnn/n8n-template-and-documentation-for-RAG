---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest/"
title: "Harvest node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest/#harvest-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.harvest.md "Edit this page")

# Harvest node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest/\#harvest-node "Permanent link")

Use the Harvest node to automate work in Harvest, and integrate Harvest with other applications. n8n has built-in support for a wide range of Harvest features, including creating, updating, deleting, and getting clients, contacts, invoices, tasks, expenses, users, and projects.

On this page, you'll find a list of operations the Harvest node supports and links to more resources.

Credentials

Refer to [Harvest credentials](https://docs.n8n.io/integrations/builtin/credentials/harvest/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest/\#operations "Permanent link")

- Client
  - Create a client
  - Delete a client
  - Get data of a client
  - Get data of all clients
  - Update a client
- Company
  - Retrieves the company for the currently authenticated user
- Contact
  - Create a contact
  - Delete a contact
  - Get data of a contact
  - Get data of all contacts
  - Update a contact
- Estimate
  - Create an estimate
  - Delete an estimate
  - Get data of an estimate
  - Get data of all estimates
  - Update an estimate
- Expense
  - Get data of an expense
  - Get data of all expenses
  - Create an expense
  - Update an expense
  - Delete an expense
- Invoice
  - Get data of an invoice
  - Get data of all invoices
  - Create an invoice
  - Update an invoice
  - Delete an invoice
- Project
  - Create a project
  - Delete a project
  - Get data of a project
  - Get data of all projects
  - Update a project
- Task
  - Create a task
  - Delete a task
  - Get data of a task
  - Get data of all tasks
  - Update a task
- Time Entries
  - Create a time entry using duration
  - Create a time entry using start and end time
  - Delete a time entry
  - Delete a time entry's external reference.
  - Get data of a time entry
  - Get data of all time entries
  - Restart a time entry
  - Stop a time entry
  - Update a time entry
- User
  - Create a user
  - Delete a user
  - Get data of a user
  - Get data of all users
  - Get data of authenticated user
  - Update a user

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest/\#templates-and-examples "Permanent link")

[Browse Harvest integration templates](https://n8n.io/integrations/harvest/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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