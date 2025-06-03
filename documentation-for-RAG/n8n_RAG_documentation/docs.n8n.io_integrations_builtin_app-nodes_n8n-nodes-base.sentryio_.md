---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio/"
title: "Sentry.io node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio/#sentryio-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.sentryio.md "Edit this page")

# Sentry.io node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio/\#sentryio-node "Permanent link")

Use the Sentry.io node to automate work in Sentry.io, and integrate Sentry.io with other applications. n8n has built-in support for a wide range of Sentry.io features, including creating, updating, deleting, and getting, issues, projects, and releases, as well as getting all events.

On this page, you'll find a list of operations the Sentry.io node supports and links to more resources.

Credentials

Refer to [Sentry.io credentials](https://docs.n8n.io/integrations/builtin/credentials/sentryio/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio/\#operations "Permanent link")

- Event
  - Get event by ID
  - Get all events
- Issue
  - Delete an issue
  - Get issue by ID
  - Get all issues
  - Update an issue
- Project
  - Create a new project
  - Delete a project
  - Get project by ID
  - Get all projects
  - Update a project
- Release
  - Create a release
  - Delete a release
  - Get release by version identifier
  - Get all releases
  - Update a release
- Organization
  - Create an organization
  - Get organization by slug
  - Get all organizations
  - Update an organization
- Team
  - Create a new team
  - Delete a team
  - Get team by slug
  - Get all teams
  - Update a team

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio/\#templates-and-examples "Permanent link")

[Browse Sentry.io integration templates](https://n8n.io/integrations/sentryio/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio/\#related-resources "Permanent link")

Refer to [Sentry.io's documentation](https://docs.sentry.io/api/) for more information about the service.

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.sentryio/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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