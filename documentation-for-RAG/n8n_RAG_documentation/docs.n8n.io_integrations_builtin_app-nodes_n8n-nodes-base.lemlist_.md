---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist/"
title: "Lemlist node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist/#lemlist-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.lemlist.md "Edit this page")

# Lemlist node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist/\#lemlist-node "Permanent link")

Use the Lemlist node to automate work in Lemlist, and integrate Lemlist with other applications. n8n has built-in support for a wide range of Lemlist features, including getting activities, teams and campaigns, as well as creating, updating, and deleting leads.

On this page, you'll find a list of operations the Lemlist node supports and links to more resources.

Credentials

Refer to [Lemlist credentials](https://docs.n8n.io/integrations/builtin/credentials/lemlist/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist/\#operations "Permanent link")

- Activity
  - Get Many: Get many activities
- Campaign
  - Get Many: Get many campaigns
  - Get Stats: Get campaign stats
- Enrichment
  - Get: Fetches a previously completed enrichment
  - Enrich Lead: Enrich a lead using an email or LinkedIn URL
  - Enrich Person: Enrich a person using an email or LinkedIn URL
- Lead
  - Create: Create a new lead
  - Delete: Delete an existing lead
  - Get: Get an existing lead
  - Unsubscribe: Unsubscribe an existing lead
- Team
  - Get: Get an existing team
  - Get Credits: Get an existing team's credits
- Unsubscribe
  - Add: Add an email to an unsubscribe list
  - Delete: Delete an email from an unsubscribe list
  - Get Many: Get many unsubscribed emails

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist/\#templates-and-examples "Permanent link")

**Create HubSpot contacts from LinkedIn post interactions**

by Pauline

[View template details](https://n8n.io/workflows/1323-create-hubspot-contacts-from-linkedin-post-interactions/)

**lemlist <> GPT-3: Supercharge your sales workflows**

by Lucas Perret

[View template details](https://n8n.io/workflows/1838-lemlist-lessgreater-gpt-3-supercharge-your-sales-workflows/)

**Classify lemlist replies using OpenAI and automate reply handling**

by Lucas Perret

[View template details](https://n8n.io/workflows/2287-classify-lemlist-replies-using-openai-and-automate-reply-handling/)

[Browse Lemlist integration templates](https://n8n.io/integrations/lemlist/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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