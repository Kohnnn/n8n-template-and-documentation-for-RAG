---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab/"
title: "GitLab node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab/#gitlab-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md "Edit this page")

# GitLab node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab/\#gitlab-node "Permanent link")

Use the GitLab node to automate work in GitLab, and integrate GitLab with other applications. n8n has built-in support for a wide range of GitLab features, including creating, updating, deleting, and editing issues, repositories, releases and users.

On this page, you'll find a list of operations the GitLab node supports and links to more resources.

Credentials

Refer to [GitLab credentials](https://docs.n8n.io/integrations/builtin/credentials/gitlab/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab/\#operations "Permanent link")

- File
  - Create
  - Delete
  - Edit
  - Get
  - List
- Issue
  - Create a new issue
  - Create a new comment on an issue
  - Edit an issue
  - Get the data of a single issue
  - Lock an issue
- Release
  - Create a new release
  - Delete a new release
  - Get a new release
  - Get all releases
  - Update a new release
- Repository
  - Get the data of a single repository
  - Returns issues of a repository
- User
  - Returns the repositories of a user

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab/\#templates-and-examples "Permanent link")

**ChatGPT Automatic Code Review in Gitlab MR**

by assert

[View template details](https://n8n.io/workflows/2167-chatgpt-automatic-code-review-in-gitlab-mr/)

**Save your workflows into a Gitlab repository**

by Julien DEL RIO

[View template details](https://n8n.io/workflows/2385-save-your-workflows-into-a-gitlab-repository/)

**Automate GitLab Merge Requests Using APIs with n8n**

by Aditya Gaur

[View template details](https://n8n.io/workflows/2858-automate-gitlab-merge-requests-using-apis-with-n8n/)

[Browse GitLab integration templates](https://n8n.io/integrations/gitlab/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab/\#related-resources "Permanent link")

Refer to [GitLab's documentation](https://docs.gitlab.com/ee/api/rest/) for more information about the service.

n8n provides a trigger node for GitLab. You can find the trigger node docs [here](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger/).

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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