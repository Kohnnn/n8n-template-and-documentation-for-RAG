---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grafana/"
title: "Grafana node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grafana/#grafana-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.grafana.md "Edit this page")

# Grafana node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grafana/\#grafana-node "Permanent link")

Use the Grafana node to automate work in Grafana, and integrate Grafana with other applications. n8n has built-in support for a wide range of Grafana features, including creating, updating, deleting, and getting dashboards, teams, and users.

On this page, you'll find a list of operations the Grafana node supports and links to more resources.

Credentials

Refer to [Grafana credentials](https://docs.n8n.io/integrations/builtin/credentials/grafana/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grafana/\#operations "Permanent link")

- Dashboard
  - Create a dashboard
  - Delete a dashboard
  - Get a dashboard
  - Get all dashboards
  - Update a dashboard
- Team
  - Create a team
  - Delete a team
  - Get a team
  - Retrieve all teams
  - Update a team
- Team Member
  - Add a member to a team
  - Retrieve all team members
  - Remove a member from a team
- User
  - Delete a user from the current organization
  - Retrieve all users in the current organization
  - Update a user in the current organization

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grafana/\#templates-and-examples "Permanent link")

[Browse Grafana integration templates](https://n8n.io/integrations/grafana/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grafana/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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