---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost/"
title: "Ghost node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost/#ghost-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.ghost.md "Edit this page")

# Ghost node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost/\#ghost-node "Permanent link")

Use the Ghost node to automate work in Ghost, and integrate Ghost with other applications. n8n has built-in support for a wide range of Ghost features, including creating, updating, deleting, and getting posts for the Admin and content API.

On this page, you'll find a list of operations the Ghost node supports and links to more resources.

Credentials

Refer to [Ghost credentials](https://docs.n8n.io/integrations/builtin/credentials/ghost/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost/\#operations "Permanent link")

### Admin API [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost/\#admin-api "Permanent link")

- **Post**
  - Create a post
  - Delete a post
  - Get a post
  - Get all posts
  - Update a post

### Content API [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost/\#content-api "Permanent link")

- **Post**
  - Get a post
  - Get all posts

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost/\#templates-and-examples "Permanent link")

**Multi-Agent PDF-to-Blog Content Generation**

by Derek Cheung

[View template details](https://n8n.io/workflows/2457-multi-agent-pdf-to-blog-content-generation/)

**📄🌐PDF2Blog - Create Blog Post on Ghost CRM from PDF Document**

by Joseph LePage

[View template details](https://n8n.io/workflows/2522-pdf2blog-create-blog-post-on-ghost-crm-from-pdf-document/)

**Research AI Agent Team with auto citations using OpenRouter and Perplexity**

by Derek Cheung

[View template details](https://n8n.io/workflows/2607-research-ai-agent-team-with-auto-citations-using-openrouter-and-perplexity/)

[Browse Ghost integration templates](https://n8n.io/integrations/ghost/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.ghost/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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