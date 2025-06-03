---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp/"
title: "Mailchimp node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp/#mailchimp-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp.md "Edit this page")

# Mailchimp node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp/\#mailchimp-node "Permanent link")

Use the Mailchimp node to automate work in Mailchimp, and integrate Mailchimp with other applications. n8n has built-in support for a wide range of Mailchimp features, including creating, updating, and deleting campaigns, as well as getting list groups.

On this page, you'll find a list of operations the Mailchimp node supports and links to more resources.

Credentials

Refer to [Mailchimp credentials](https://docs.n8n.io/integrations/builtin/credentials/mailchimp/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp/\#operations "Permanent link")

- Campaign
  - Delete a campaign
  - Get a campaign
  - Get all the campaigns
  - Replicate a campaign
  - Creates a Resend to Non-Openers version of this campaign
  - Send a campaign
- List Group
  - Get all groups
- Member
  - Create a new member on list
  - Delete a member on list
  - Get a member on list
  - Get all members on list
  - Update a new member on list
- Member Tag
  - Add tags from a list member
  - Remove tags from a list member

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp/\#templates-and-examples "Permanent link")

**Process Shopify new orders with Zoho CRM and Harvest**

by Lorena

[View template details](https://n8n.io/workflows/1206-process-shopify-new-orders-with-zoho-crm-and-harvest/)

**Add new contacts from HubSpot to the email list in Mailchimp**

by n8n Team

[View template details](https://n8n.io/workflows/1770-add-new-contacts-from-hubspot-to-the-email-list-in-mailchimp/)

**Send or update new Mailchimp subscribers in HubSpot**

by n8n Team

[View template details](https://n8n.io/workflows/1771-send-or-update-new-mailchimp-subscribers-in-hubspot/)

[Browse Mailchimp integration templates](https://n8n.io/integrations/mailchimp/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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