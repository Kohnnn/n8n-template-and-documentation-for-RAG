---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/"
title: "Microsoft Entra ID node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/#microsoft-entra-id-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra.md "Edit this page")

# Microsoft Entra ID node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/\#microsoft-entra-id-node "Permanent link")

Use the Microsoft Entra ID node to automate work in Microsoft Entra ID and integrate Microsoft Entra ID with other applications. n8n has built-in support for a wide range of Microsoft Entra ID features, which includes creating, getting, updating, and deleting users and groups, as well as adding users to and removing them from groups.

On this page, you'll find a list of operations the Microsoft Entra ID node supports, and links to more resources.

Credentials

You can find authentication information for this node [here](https://docs.n8n.io/integrations/builtin/credentials/microsoftentra/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/\#operations "Permanent link")

- **Group**
  - **Create**: Create a new group
  - **Delete**: Delete an existing group
  - **Get**: Retrieve data for a specific group
  - **Get Many**: Retrieve a list of groups
  - **Update**: Update a group
- **User**
  - **Create**: Create a new user
  - **Delete**: Delete an existing user
  - **Get**: Retrieve data for a specific user
  - **Get Many**: Retrieve a list of users
  - **Update**: Update a user
  - **Add to Group**: Add user to a group
  - **Remove from Group**: Remove user from a group

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/\#templates-and-examples "Permanent link")

**Automated Web Scraping: email a CSV, save to Google Sheets & Microsoft Excel**

by Mihai Farcas

[View template details](https://n8n.io/workflows/2275-automated-web-scraping-email-a-csv-save-to-google-sheets-and-microsoft-excel/)

**Create a Branded AI-Powered Website Chatbot**

by Wayne Simpson

[View template details](https://n8n.io/workflows/2786-create-a-branded-ai-powered-website-chatbot/)

**Hacker News to Video Content**

by Alex Kim

[View template details](https://n8n.io/workflows/2557-hacker-news-to-video-content/)

[Browse Microsoft Entra ID integration templates](https://n8n.io/integrations/microsoft-entra-id-azure-active-directory/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/\#related-resources "Permanent link")

Refer to [Microsoft Entra ID's documentation](https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview?view=graph-rest-1.0) for more information about the service.

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

## Common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/\#common-issues "Permanent link")

Here are some common errors and issues with the Microsoft Entra ID node and steps to resolve or troubleshoot them.

### Updating the Allow External Senders and Auto Subscribe New Members options fails [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra/\#updating-the-allow-external-senders-and-auto-subscribe-new-members-options-fails "Permanent link")

You can't update the **Allow External Senders** and **Auto Subscribe New Members** options directly after creating a new group. You must wait after creating a group before you can change the values of these options.

When designing workflows that use multiple Microsoft Entra ID nodes to first create groups and then update these options, add a [Wait](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/) node between the two operations. A Wait node configured to pause for at least two seconds allows time for the group to fully initialize. After the wait, the update operation can complete without erroring.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top