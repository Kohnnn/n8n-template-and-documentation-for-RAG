---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/"
title: "Jira Software node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/#jira-software-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.jira.md "Edit this page")

# Jira Software node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/\#jira-software-node "Permanent link")

Use the Jira Software node to automate work in Jira, and integrate Jira with other applications. n8n has built-in support for a wide range of Jira features, including creating, updating, deleting, and getting issues, and users.

On this page, you'll find a list of operations the Jira Software node supports and links to more resources.

Credentials

Refer to [Jira credentials](https://docs.n8n.io/integrations/builtin/credentials/jira/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/\#operations "Permanent link")

- Issue
  - Get issue changelog
  - Create a new issue
  - Delete an issue
  - Get an issue
  - Get all issues
  - Create an email notification for an issue and add it to the mail queue
  - Return either all transitions or a transition that can be performed by the user on an issue, based on the issue's status
  - Update an issue
- Issue Attachment
  - Add attachment to issue
  - Get an attachment
  - Get all attachments
  - Remove an attachment
- Issue Comment
  - Add comment to issue
  - Get a comment
  - Get all comments
  - Remove a comment
  - Update a comment
- User
  - Create a new user.
  - Delete a user.
  - Retrieve a user.

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/\#templates-and-examples "Permanent link")

**Automate Customer Support Issue Resolution using AI Text Classifier**

by Jimleuk

[View template details](https://n8n.io/workflows/2468-automate-customer-support-issue-resolution-using-ai-text-classifier/)

**Create a new issue in Jira**

by tanaypant

[View template details](https://n8n.io/workflows/459-create-a-new-issue-in-jira/)

**Analyze & Sort Suspicious Email Contents with ChatGPT**

by Angel Menendez

[View template details](https://n8n.io/workflows/2666-analyze-and-sort-suspicious-email-contents-with-chatgpt/)

[Browse Jira Software integration templates](https://n8n.io/integrations/jira-software/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/\#related-resources "Permanent link")

Refer to the [official JQL documentation](https://www.atlassian.com/software/jira/guides/expand-jira/jql) about Jira Query Language (JQL) to learn more about it.

## Fetch issues for a specific project [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira/\#fetch-issues-for-a-specific-project "Permanent link")

The **Get All** operation returns all the issues from Jira. To fetch issues for a particular project, you need to use Jira Query Language (JQL).

For example, if you want to receive all the issues of a project named `n8n`, you'd do something like this:

- Select **Get All** from the **Operation** dropdown list.
- Toggle **Return All** to true.
- Select **Add Option** and select **JQL**.
- Enter `project=n8n` in the **JQL** field.

This query will fetch all the issues in the project named `n8n`. Enter the name of your project instead of `n8n` to fetch all the issues for your project.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top