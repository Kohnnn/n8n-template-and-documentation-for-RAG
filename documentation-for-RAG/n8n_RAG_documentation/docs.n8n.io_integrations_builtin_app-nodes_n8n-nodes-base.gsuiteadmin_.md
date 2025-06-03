---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin/"
title: "Google Workspace Admin node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin/#google-workspace-admin-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin.md "Edit this page")

# Google Workspace Admin node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin/\#google-workspace-admin-node "Permanent link")

Use the Google Workspace Admin node to automate work in Google Workspace Admin, and integrate Google Workspace Admin with other applications. n8n has built-in support for a wide range of Google Workspace Admin features, including creating, updating, deleting, and getting users, and groups.

On this page, you'll find a list of operations the Google Workspace Admin node supports and links to more resources.

Credentials

Refer to [Google credentials](https://docs.n8n.io/integrations/builtin/credentials/google/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin/\#operations "Permanent link")

- Group
  - Create a group
  - Delete a group
  - Get a group
  - Get all groups
  - Update a group
- User
  - Create a user
  - Delete a user
  - Get a user
  - Get all users
  - Update a user

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin/\#templates-and-examples "Permanent link")

[Browse Google Workspace Admin integration templates](https://n8n.io/integrations/google-workspace-admin/), or [search all templates](https://n8n.io/workflows/)

## How to project a user's information [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin/\#how-to-project-a-users-information "Permanent link")

There are three different ways to project a user's information:

- **Basic**: Doesn't include any custom fields.
- **Custom**: Includes the custom fields from schemas in `customField`.
- **Full**: Include all the fields associated with the user.

To include custom fields, follow these steps:

1. Select **Custom** from the **Projection** dropdown list.
2. Select the **Add Options** button and select **Custom Schemas** from the dropdown list.
3. Select the schema names you want to include from the **Custom Schemas** dropdown list.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top