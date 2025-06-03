---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks/"
title: "Google Books node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks/#google-books-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks.md "Edit this page")

# Google Books node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks/\#google-books-node "Permanent link")

Use the Google Books node to automate work in Google Books, and integrate Google Books with other applications. n8n has built-in support for a wide range of Google Books features, including retrieving a specific bookshelf resource for the specified user, adding volume to a bookshelf, and getting volume.

On this page, you'll find a list of operations the Google Books node supports and links to more resources.

Credentials

Refer to [Google credentials](https://docs.n8n.io/integrations/builtin/credentials/google/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks/\#operations "Permanent link")

- Bookshelf
  - Retrieve a specific bookshelf resource for the specified user
  - Get all public bookshelf resource for the specified user
- Bookshelf Volume
  - Add a volume to a bookshelf
  - Clears all volumes from a bookshelf
  - Get all volumes in a specific bookshelf for the specified user
  - Moves a volume within a bookshelf
  - Removes a volume from a bookshelf
- Volume
  - Get a volume resource based on ID
  - Get all volumes filtered by query

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks/\#templates-and-examples "Permanent link")

[Browse Google Books integration templates](https://n8n.io/integrations/google-books/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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