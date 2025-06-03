---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github/"
title: "GitHub node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github/#github-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.github.md "Edit this page")

# GitHub node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github/\#github-node "Permanent link")

Use the GitHub node to automate work in GitHub, and integrate GitHub with other applications. n8n has built-in support for a wide range of GitHub features, including creating, updating, deleting, and editing files, repositories, issues, releases, and users.

On this page, you'll find a list of operations the GitHub node supports and links to more resources.

Credentials

Refer to [GitHub credentials](https://docs.n8n.io/integrations/builtin/credentials/github/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github/\#operations "Permanent link")

- File
  - Create
  - Delete
  - Edit
  - Get
  - List
- Issue
  - Create
  - Create Comment
  - Edit
  - Get
  - Lock
- Organization
  - Get Repositories
- Release
  - Create
  - Delete
  - Get
  - Get Many
  - Update
- Repository
  - Get
  - Get Issues
  - Get License
  - Get Profile
  - Get Pull Requests
  - List Popular Paths
  - List Referrers
- Review
  - Create
  - Get
  - Get Many
  - Update
- User
  - Get Repositories
  - Invite
- Workflow
  - Disable
  - Dispatch
  - Enable
  - Get
  - Get Usage
  - List

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github/\#templates-and-examples "Permanent link")

**Back Up Your n8n Workflows To Github**

by Jonathan

[View template details](https://n8n.io/workflows/1534-back-up-your-n8n-workflows-to-github/)

**Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI**

by Jenny

[View template details](https://n8n.io/workflows/2440-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-open-ai/)

**Chat with GitHub API Documentation: RAG-Powered Chatbot with Pinecone & OpenAI**

by Mihai Farcas

[View template details](https://n8n.io/workflows/2705-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-and-openai/)

[Browse GitHub integration templates](https://n8n.io/integrations/github/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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