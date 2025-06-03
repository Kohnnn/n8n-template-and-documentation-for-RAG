---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleslides/"
title: "Google Slides node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleslides/#google-slides-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.googleslides.md "Edit this page")

# Google Slides node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleslides/\#google-slides-node "Permanent link")

Use the Google Slides node to automate work in Google Slides, and integrate Google Slides with other applications. n8n has built-in support for a wide range of Google Slides features, including creating presentations, and getting pages.

On this page, you'll find a list of operations the Google Slides node supports and links to more resources.

Credentials

Refer to [Google credentials](https://docs.n8n.io/integrations/builtin/credentials/google/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleslides/\#operations "Permanent link")

- Page
  - Get a page
  - Get a thumbnail
- Presentation
  - Create a presentation
  - Get a presentation
  - Get presentation slides
  - Replace text in a presentation

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleslides/\#templates-and-examples "Permanent link")

**Dynamically replace images in Google Slides via API**

by Emmanuel Bernard

[View template details](https://n8n.io/workflows/2244-dynamically-replace-images-in-google-slides-via-api/)

**Get all the slides from a presentation and get thumbnails of pages**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/1035-get-all-the-slides-from-a-presentation-and-get-thumbnails-of-pages/)

**Export new deals from HubSpot to Slack and Airtable**

by Lorena

[View template details](https://n8n.io/workflows/1225-export-new-deals-from-hubspot-to-slack-and-airtable/)

[Browse Google Slides integration templates](https://n8n.io/integrations/google-slides/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googleslides/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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