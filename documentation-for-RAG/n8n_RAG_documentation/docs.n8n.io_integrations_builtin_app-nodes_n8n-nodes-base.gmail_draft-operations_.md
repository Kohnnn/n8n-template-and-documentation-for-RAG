---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/"
title: "Gmail node Draft Operations documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/#gmail-node-draft-operations)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md "Edit this page")

# Gmail node Draft Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/\#gmail-node-draft-operations "Permanent link")

Use the Draft operations to create, delete, or get a draft or list drafts in Gmail. Refer to the [Gmail node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/) for more information on the Gmail node itself.

## Create a draft [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/\#create-a-draft "Permanent link")

Use this operation to create a new draft.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Draft**.
- **Operation**: Select **Create**.
- **Subject**: Enter the subject line.
- Select the **Email Type**. Choose from **Text** or **HTML**.
- **Message**: Enter the email message body.

### Create draft options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/\#create-draft-options "Permanent link")

Use these options to further refine the node's behavior:

- **Attachments**: Select **Add Attachment** to add an attachment. Enter the **Attachment Field Name (in Input)** to identify which field from the input node contains the attachment.
  - For multiple properties, enter a comma-separated list.
- **BCC**: Enter one or more email addresses for blind copy recipients. Separate multiple email addresses with a comma, for example `jay@gatsby.com, jon@smith.com`.
- **CC**: Enter one or more email addresses for carbon copy recipients. Separate multiple email addresses with a comma, for example `jay@gatsby.com, jon@smith.com`.
- **From Alias Name or ID**: Select an alias to send the draft from. This field populates based on the credential you selected in the parameters.
- **Send Replies To**: Enter an email address to set as the reply to address.
- **Thread ID**: If you want this draft attached to a thread, enter the ID for that thread.
- **To Email**: Enter one or more email addresses for recipients. Separate multiple email addresses with a comma, for example `jay@gatsby.com, jon@smith.com`.

Refer to the [Gmail API Method: users.drafts.create](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create) documentation for more information.

## Delete a draft [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/\#delete-a-draft "Permanent link")

Use this operation to delete a draft.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Draft**.
- **Operation**: Select **Delete**.
- **Draft ID**: Enter the ID of the draft you wish to delete.

Refer to the [Gmail API Method: users.drafts.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/delete) documentation for more information.

## Get a draft [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/\#get-a-draft "Permanent link")

Use this operation to get a single draft.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Draft**.
- **Operation**: Select **Get**.
- **Draft ID**: Enter the ID of the draft you wish to get information about.

### Get draft options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/\#get-draft-options "Permanent link")

Use these options to further refine the node's behavior:

- **Attachment Prefix**: Enter a prefix for the name of the binary property the node should write any attachments to. n8n adds an index starting with `0` to the prefix. For example, if you enter \`attachment\_' as the prefix, the first attachment saves to 'attachment\_0'.
- **Download Attachments**: Select whether the node should download the draft's attachments (turned on) or not (turned off).

Refer to the [Gmail API Method: users.drafts.get](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/get) documentation for more information.

## Get Many drafts [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/\#get-many-drafts "Permanent link")

Use this operation to get two or more drafts.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Draft**.
- **Operation**: Select **Get Many**.
- **Return All**: Choose whether the node returns all drafts (turned on) or only up to a set limit (turned off).
- **Limit**: Enter the maximum number of drafts to return. Only used if you've turned off **Return All**.

### Get Many drafts options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/\#get-many-drafts-options "Permanent link")

Use these options to further refine the node's behavior:

- **Attachment Prefix**: Enter a prefix for the name of the binary property the node should write any attachments to. n8n adds an index starting with `0` to the prefix. For example, if you enter \`attachment\_' as the prefix, the first attachment saves to 'attachment\_0'.
- **Download Attachments**: Select whether the node should download the draft's attachments (turned on) or not (turned off).
- **Include Spam and Trash**: Select whether the node should get drafts in the Spam and Trash folders (turned on) or not (turned off).

Refer to the [Gmail API Method: users.drafts.list](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/list) documentation for more information.

## Common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations/\#common-issues "Permanent link")

For common errors or issues and suggested resolution steps, refer to [Common Issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top