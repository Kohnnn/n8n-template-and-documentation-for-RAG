---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/"
title: "Airtop node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/#airtop-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.airtop.md "Edit this page")

# Airtop node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#airtop-node "Permanent link")

Use the Airtop node to automate work in Airtop, and integrate Airtop with other applications. n8n has built-in support for a wide range of Airtop features, enabling you to control a cloud-based web browser for tasks like querying, scraping, and interacting with web pages.

On this page, you'll find a list of operations the Airtop node supports, and links to more resources.

Credentials

Refer to [Airtop credentials](https://docs.n8n.io/integrations/builtin/credentials/airtop/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#operations "Permanent link")

- Session
  - Create session
  - Save profile on termination
  - Terminate session
- Window
  - Create a new browser window
  - Load URL
  - Take screenshot
  - Close window
- Extraction
  - Query page
  - Query page with pagination
  - Smart scrape page
- Interaction
  - Click an element
  - Hover on an element
  - Type

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#templates-and-examples "Permanent link")

**Automated LinkedIn Profile Discovery with Airtop and Google Search**

by Airtop

[View template details](https://n8n.io/workflows/3477-automated-linkedin-profile-discovery-with-airtop-and-google-search/)

**Automate Web Interactions with Claude 3.5 Haiku and Airtop Browser Agent**

by Airtop

[View template details](https://n8n.io/workflows/3592-automate-web-interactions-with-claude-35-haiku-and-airtop-browser-agent/)

**Build Lists of Profiles from Any Platform using Airtop and Google Sheets**

by Airtop

[View template details](https://n8n.io/workflows/3479-build-lists-of-profiles-from-any-platform-using-airtop-and-google-sheets/)

[Browse Airtop integration templates](https://n8n.io/integrations/airtop/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#related-resources "Permanent link")

Refer to [Airtop's documentation](https://docs.airtop.ai/api-reference/airtop-api) for more information about the service.

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

Contact [Airtop's Support](https://docs.airtop.ai/guides/misc/support) for assistance or to create a feature request.

## Node reference [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#node-reference "Permanent link")

### Create a session and window [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#create-a-session-and-window "Permanent link")

Create an Airtop browser session to get a **Session ID**, then use it to create a new browser window. After this, you can use any extraction or interaction operation.

### Extract content [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#extract-content "Permanent link")

Extract content from a web browser using these operations:

- **Query page**: Extract information from the current window.
- **Query page with pagination**: Extract information from pages with pagination or infinite scrolling.
- **Smart scrape page**: Get the window content as markdown.

Get JSON responses by using the **JSON Output Schema** parameter in query operations.

### Interacting with pages [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#interacting-with-pages "Permanent link")

Click, hover, or type on elements by describing the element you want to interact with.

### Terminate a session [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop/\#terminate-a-session "Permanent link")

End your session to save resources. Sessions are automatically terminated based on the **Idle Timeout** set in the **Create Session** operation or can be manually terminated using the **Terminate Session** operation.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top