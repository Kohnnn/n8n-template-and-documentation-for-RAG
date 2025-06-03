---
url: "https://docs.n8n.io/integrations/custom-operations/"
title: "Custom API actions for existing nodes | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/integrations/custom-operations/#custom-api-operations)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/custom-operations.md "Edit this page")

# Custom API operations [\#](https://docs.n8n.io/integrations/custom-operations/\#custom-api-operations "Permanent link")

One of the most complex parts of setting up [API](https://docs.n8n.io/glossary/#api) calls is managing authentication. n8n provides [credentials](https://docs.n8n.io/glossary/#credential-n8n) support for operations and services beyond those supported by built-in nodes.

- Custom operations for existing nodes: n8n supplies hundreds of nodes to create workflows that link multiple products. However, some nodes don't include all the possible operations supported by a product's API. You can work around this by making a custom API call using the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) node.
- Credential-only nodes: n8n includes credential-only nodes. These are integrations where n8n supports setting up credentials for use in the HTTP Request node, but doesn't provide a standalone node. You can find a credential-only node in the nodes panel, as you would for any other integration.

## Predefined credential types [\#](https://docs.n8n.io/integrations/custom-operations/\#predefined-credential-types "Permanent link")

A predefined credential type is a credential that already exists in n8n. You can use predefined credential types instead of generic credentials in the HTTP Request node.

For example: you create an Asana credential, for use with the Asana node. Later, you want to perform an operation that isn't supported by the Asana node, using Asana's API. You can use your existing Asana credential in the HTTP Request node to perform the operation, without additional authentication setup.

### Using predefined credential types [\#](https://docs.n8n.io/integrations/custom-operations/\#using-predefined-credential-types "Permanent link")

To use a predefined credential type:

1. Open your HTTP Request node, or add a new one to your workflow.
2. In **Authentication**, select **Predefined Credential Type**.
3. In **Credential Type**, select the API you want to use.
4. In **Credential for `<API name>`**, you can:
1. Select an existing credential for that platform, if available.
2. Select **Create New** to create a new credential.

### Credential scopes [\#](https://docs.n8n.io/integrations/custom-operations/\#credential-scopes "Permanent link")

Some existing credential types have specific scopes: endpoints that they work with. n8n warns you about this when you select the credential type.

For example, follow the steps in [Using predefined credential types](https://docs.n8n.io/integrations/custom-operations/#using-predefined-credential-types), and select **Google Calendar OAuth2 API** as your **Credential Type**. n8n displays a box listing the two endpoints you can use this credential type with:

[![The scopes box](https://docs.n8n.io/_images/integrations/custom-operations/scopes.png)](https://docs.n8n.io/_images/integrations/custom-operations/scopes.png)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top