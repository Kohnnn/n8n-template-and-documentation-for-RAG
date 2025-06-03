---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/"
title: "Google Chat node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/#google-chat-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.googlechat.md "Edit this page")

# Google Chat node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/\#google-chat-node "Permanent link")

Use the Google Chat node to automate work in Google Chat, and integrate Google Chat with other applications. n8n has built-in support for a wide range of Google Chat features, including getting membership and spaces, as well as creating and deleting messages.

On this page, you'll find a list of operations the Google Chat node supports and links to more resources.

Credentials

Refer to [Google credentials](https://docs.n8n.io/integrations/builtin/credentials/google/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/\#operations "Permanent link")

- Member
  - Get a membership
  - Get all memberships in a space
- Message
  - Create a message
  - Delete a message
  - Get a message
  - Send and Wait for Response
  - Update a message
- Space
  - Get a space
  - Get all spaces the caller is a member of

## Waiting for a response [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/\#waiting-for-a-response "Permanent link")

By choosing the **Send and Wait for a Response** operation, you can send a message and pause the workflow execution until a person confirms the action or provides more information.

### Response Type [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/\#response-type "Permanent link")

You can choose between the following types of waiting and approval actions:

- **Approval**: Users can approve or disapprove from within the message.
- **Free Text**: Users can submit a response with a form.
- **Custom Form**: Users can submit a response with a custom form.

You can customize the waiting and response behavior depending on which response type you choose. You can configure these options in any of the above response types:

- **Limit Wait Time**: Whether the workflow will automatically resume execution after a specified time limit. This can be an interval or a specific wall time.
- **Append n8n Attribution**: Whether to mention in the message that it was sent automatically with n8n (turned on) or not (turned off).

### Approval response customization [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/\#approval-response-customization "Permanent link")

When using the Approval response type, you can choose whether to present only an approval button or both approval _and_ disapproval buttons.

You can also customize the button labels for the buttons you include.

### Free Text response customization [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/\#free-text-response-customization "Permanent link")

When using the Free Text response type, you can customize the message button label, the form title and description, and the response button label.

### Custom Form response customization [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/\#custom-form-response-customization "Permanent link")

When using the Custom Form response type, you build a form using the fields and options you want.

You can customize each form element with the settings outlined in the [n8n Form trigger's form elements](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger/#form-elements). To add more fields, select the **Add Form Element** button.

You'll also be able to customize the message button label, the form title and description, and the response button label.

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlechat/\#templates-and-examples "Permanent link")

**AI agent chat**

by n8n Team

[View template details](https://n8n.io/workflows/1954-ai-agent-chat/)

**✨🤖Automate Multi-Platform Social Media Content Creation with AI**

by Joseph LePage

[View template details](https://n8n.io/workflows/3066-automate-multi-platform-social-media-content-creation-with-ai/)

**Ask questions about a PDF using AI**

by David Roberts

[View template details](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)

[Browse Google Chat integration templates](https://n8n.io/integrations/google-chat/), or [search all templates](https://n8n.io/workflows/)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top