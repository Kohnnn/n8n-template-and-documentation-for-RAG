---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk/"
title: "Zendesk node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk/#zendesk-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.zendesk.md "Edit this page")

# Zendesk node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk/\#zendesk-node "Permanent link")

Use the Zendesk node to automate work in Zendesk, and integrate Zendesk with other applications. n8n has built-in support for a wide range of Zendesk features, including creating, and deleting tickets, users, and organizations.

On this page, you'll find a list of operations the Zendesk node supports and links to more resources.

Credentials

Refer to [Zendesk credentials](https://docs.n8n.io/integrations/builtin/credentials/zendesk/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk/\#operations "Permanent link")

- Ticket
  - Create a ticket
  - Delete a ticket
  - Get a ticket
  - Get all tickets
  - Recover a suspended ticket
  - Update a ticket
- Ticket Field
  - Get a ticket field
  - Get all system and custom ticket fields
- User
  - Create a user
  - Delete a user
  - Get a user
  - Get all users
  - Get a user's organizations
  - Get data related to the user
  - Search users
  - Update a user
- Organization
  - Create an organization
  - Delete an organization
  - Count organizations
  - Get an organization
  - Get all organizations
  - Get data related to the organization
  - Update a organization

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk/\#templates-and-examples "Permanent link")

**Automate SIEM Alert Enrichment with MITRE ATT&CK, Qdrant & Zendesk in n8n**

by Angel Menendez

[View template details](https://n8n.io/workflows/2840-automate-siem-alert-enrichment-with-mitre-attandck-qdrant-and-zendesk-in-n8n/)

**Sync Zendesk tickets to Slack thread**

by n8n Team

[View template details](https://n8n.io/workflows/1820-sync-zendesk-tickets-to-slack-thread/)

**Sync Zendesk tickets with subsequent comments to Jira issues**

by n8n Team

[View template details](https://n8n.io/workflows/1833-sync-zendesk-tickets-with-subsequent-comments-to-jira-issues/)

[Browse Zendesk integration templates](https://n8n.io/integrations/zendesk/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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