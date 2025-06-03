---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/"
title: "Discord node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/#discord-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md "Edit this page")

# Discord node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#discord-node "Permanent link")

Use the Discord node to automate work in Discord, and integrate Discord with other applications. n8n has built-in support for a wide range of Discord features, including sending messages in a Discord channel and managing channels.

On this page, you'll find a list of operations the Discord node supports and links to more resources.

Credentials

Refer to [Discord credentials](https://docs.n8n.io/integrations/builtin/credentials/discord/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#operations "Permanent link")

- Channel
  - Create
  - Delete
  - Get
  - Get Many
  - Update
- Message
  - Delete
  - Get
  - Get Many
  - React with Emoji
  - Send
  - Send and Wait for Response
- Member
  - Get Many
  - Role Add
  - Role Remove

## Waiting for a response [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#waiting-for-a-response "Permanent link")

By choosing the **Send and Wait for a Response** operation, you can send a message and pause the workflow execution until a person confirms the action or provides more information.

### Response Type [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#response-type "Permanent link")

You can choose between the following types of waiting and approval actions:

- **Approval**: Users can approve or disapprove from within the message.
- **Free Text**: Users can submit a response with a form.
- **Custom Form**: Users can submit a response with a custom form.

You can customize the waiting and response behavior depending on which response type you choose. You can configure these options in any of the above response types:

- **Limit Wait Time**: Whether the workflow will automatically resume execution after a specified time limit. This can be an interval or a specific wall time.
- **Append n8n Attribution**: Whether to mention in the message that it was sent automatically with n8n (turned on) or not (turned off).

### Approval response customization [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#approval-response-customization "Permanent link")

When using the Approval response type, you can choose whether to present only an approval button or both approval _and_ disapproval buttons.

You can also customize the button labels for the buttons you include.

### Free Text response customization [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#free-text-response-customization "Permanent link")

When using the Free Text response type, you can customize the message button label, the form title and description, and the response button label.

### Custom Form response customization [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#custom-form-response-customization "Permanent link")

When using the Custom Form response type, you build a form using the fields and options you want.

You can customize each form element with the settings outlined in the [n8n Form trigger's form elements](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger/#form-elements). To add more fields, select the **Add Form Element** button.

You'll also be able to customize the message button label, the form title and description, and the response button label.

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#templates-and-examples "Permanent link")

**AI-Powered Short-Form Video Generator with OpenAI, Flux, Kling, and ElevenLabs**

by Cameron Wills

[View template details](https://n8n.io/workflows/3121-ai-powered-short-form-video-generator-with-openai-flux-kling-and-elevenlabs/)

**Fully Automated AI Video Generation & Multi-Platform Publishing**

by Juan Carlos Cavero Gracia

[View template details](https://n8n.io/workflows/3442-fully-automated-ai-video-generation-and-multi-platform-publishing/)

**Discord AI-powered bot**

by Eduard

[View template details](https://n8n.io/workflows/1938-discord-ai-powered-bot/)

[Browse Discord integration templates](https://n8n.io/integrations/discord/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#related-resources "Permanent link")

Refer to [Discord's documentation](https://discord.com/developers/docs/intro) for more information about the service.

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

## Common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/\#common-issues "Permanent link")

For common errors or issues and suggested resolution steps, refer to [Common Issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top