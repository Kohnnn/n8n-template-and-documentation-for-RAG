---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.reddit/"
title: "Reddit node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.reddit/#reddit-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.reddit.md "Edit this page")

# Reddit node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.reddit/\#reddit-node "Permanent link")

Use the Reddit node to automate work in Reddit, and integrate Reddit with other applications. n8n has built-in support for a wide range of Reddit features, including getting profiles, and users, retrieving post comments and subreddit, as well as submitting, getting, and deleting posts.

On this page, you'll find a list of operations the Reddit node supports and links to more resources.

Credentials

Refer to [Reddit credentials](https://docs.n8n.io/integrations/builtin/credentials/reddit/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.reddit/\#operations "Permanent link")

- Post
  - Submit a post to a subreddit
  - Delete a post from a subreddit
  - Get a post from a subreddit
  - Get all posts from a subreddit
  - Search posts in a subreddit or in all of Reddit.
- Post Comment
  - Create a top-level comment in a post
  - Retrieve all comments in a post
  - Remove a comment from a post
  - Write a reply to a comment in a post
- Profile
  - Get
- Subreddit
  - Retrieve background information about a subreddit.
  - Retrieve information about subreddits from all of Reddit.
- User
  - Get

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.reddit/\#templates-and-examples "Permanent link")

**Extract Trends, Auto-Generate Social Content with AI, Reddit, Google & Post**

by Immanuel

[View template details](https://n8n.io/workflows/3560-extract-trends-auto-generate-social-content-with-ai-reddit-google-and-post/)

**Analyze Reddit Posts with AI to Identify Business Opportunities**

by Alex Huang

[View template details](https://n8n.io/workflows/2978-analyze-reddit-posts-with-ai-to-identify-business-opportunities/)

**Reddit AI digest**

by n8n Team

[View template details](https://n8n.io/workflows/1895-reddit-ai-digest/)

[Browse Reddit integration templates](https://n8n.io/integrations/reddit/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.reddit/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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