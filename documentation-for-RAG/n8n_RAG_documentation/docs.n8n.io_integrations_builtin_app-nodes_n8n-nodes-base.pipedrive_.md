---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive/"
title: "Pipedrive node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive/#pipedrive-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive.md "Edit this page")

# Pipedrive node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive/\#pipedrive-node "Permanent link")

Use the Pipedrive node to automate work in Pipedrive, and integrate Pipedrive with other applications. n8n has built-in support for a wide range of Pipedrive features, including creating, updating, deleting, and getting activity, files, notes, organizations, and leads.

On this page, you'll find a list of operations the Pipedrive node supports and links to more resources.

Credentials

Refer to [Pipedrive credentials](https://docs.n8n.io/integrations/builtin/credentials/pipedrive/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive/\#operations "Permanent link")

- Activity
  - Create an activity
  - Delete an activity
  - Get data of an activity
  - Get data of all activities
  - Update an activity
- Deal
  - Create a deal
  - Delete a deal
  - Duplicate a deal
  - Get data of a deal
  - Get data of all deals
  - Search a deal
  - Update a deal
- Deal Activity
  - Get all activities of a deal
- Deal Product
  - Add a product to a deal
  - Get all products in a deal
  - Remove a product from a deal
  - Update a product in a deal
- File
  - Create a file
  - Delete a file
  - Download a file
  - Get data of a file
- Lead
  - Create a lead
  - Delete a lead
  - Get data of a lead
  - Get data of all leads
  - Update a lead
- Note
  - Create a note
  - Delete a note
  - Get data of a note
  - Get data of all notes
  - Update a note
- Organization
  - Create an organization
  - Delete an organization
  - Get data of an organization
  - Get data of all organizations
  - Update an organization
  - Search organizations
- Person
  - Create a person
  - Delete a person
  - Get data of a person
  - Get data of all persons
  - Search all persons
  - Update a person
- Product
  - Get data of all products

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive/\#templates-and-examples "Permanent link")

**Two way sync Pipedrive and MySQL**

by n8n Team

[View template details](https://n8n.io/workflows/1822-two-way-sync-pipedrive-and-mysql/)

**Upload leads from a CSV file to Pipedrive CRM**

by n8n Team

[View template details](https://n8n.io/workflows/1787-upload-leads-from-a-csv-file-to-pipedrive-crm/)

**Enrich new leads in Pipedrive and send an alert to Slack for high-quality ones**

by Niklas Hatje

[View template details](https://n8n.io/workflows/2135-enrich-new-leads-in-pipedrive-and-send-an-alert-to-slack-for-high-quality-ones/)

[Browse Pipedrive integration templates](https://n8n.io/integrations/pipedrive/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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