---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot/"
title: "HubSpot node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot/#hubspot-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md "Edit this page")

# HubSpot node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot/\#hubspot-node "Permanent link")

Use the HubSpot node to automate work in HubSpot, and integrate HubSpot with other applications. n8n has built-in support for a wide range of HubSpot features, including creating, updating, deleting, and getting contacts, deals, lists, engagements and companies.

On this page, you'll find a list of operations the HubSpot node supports and links to more resources.

Credentials

Refer to [HubSpot credentials](https://docs.n8n.io/integrations/builtin/credentials/hubspot/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot/\#operations "Permanent link")

- Contact
  - Create/Update a contact
  - Delete a contact
  - Get a contact
  - Get all contacts
  - Get recently created/updated contacts
  - Search contacts
- Contact List
  - Add contact to a list
  - Remove a contact from a list
- Company
  - Create a company
  - Delete a company
  - Get a company
  - Get all companies
  - Get recently created companies
  - Get recently modified companies
  - Search companies by domain
  - Update a company
- Deal
  - Create a deal
  - Delete a deal
  - Get a deal
  - Get all deals
  - Get recently created deals
  - Get recently modified deals
  - Search deals
  - Update a deal
- Engagement
  - Create an engagement
  - Delete an engagement
  - Get an engagement
  - Get all engagements
- Form
  - Get all fields from a form
  - Submit data to a form
- Ticket
  - Create a ticket
  - Delete a ticket
  - Get a ticket
  - Get all tickets
  - Update a ticket

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot/\#templates-and-examples "Permanent link")

**Create HubSpot contacts from LinkedIn post interactions**

by Pauline

[View template details](https://n8n.io/workflows/1323-create-hubspot-contacts-from-linkedin-post-interactions/)

**Update HubSpot when a new invoice is registered in Stripe**

by Jonathan

[View template details](https://n8n.io/workflows/1468-update-hubspot-when-a-new-invoice-is-registered-in-stripe/)

**Real Estate Lead Generation with BatchData Skip Tracing & CRM Integration**

by Preston Zeller

[View template details](https://n8n.io/workflows/3666-real-estate-lead-generation-with-batchdata-skip-tracing-and-crm-integration/)

[Browse HubSpot integration templates](https://n8n.io/integrations/hubspot/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.hubspot/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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