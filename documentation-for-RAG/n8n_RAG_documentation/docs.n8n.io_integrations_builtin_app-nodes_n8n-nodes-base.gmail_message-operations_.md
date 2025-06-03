---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/"
title: "Gmail node Message Operations documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/#gmail-node-message-operations)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md "Edit this page")

# Gmail node Message Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#gmail-node-message-operations "Permanent link")

Use the Message operations to send, reply to, delete, mark read or unread, add a label to, remove a label from, or get a message or get a list of messages in Gmail. Refer to the [Gmail node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/) for more information on the Gmail node itself.

## Add Label to a message [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#add-label-to-a-message "Permanent link")

Use this operation to add one or more labels to a message.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Add Label**.
- **Message ID**: Enter the ID of the message you want to add the label to.
- **Label Names or IDs**: Select the Label names you want to add or enter an expression to specify IDs. The dropdown populates based on the **Credential** you selected.

Refer to the [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify) documentation for more information.

## Delete a message [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#delete-a-message "Permanent link")

Use this operation to immediately and permanently delete a message.

Permanent deletion

This operation can't be undone. For recoverable deletions, use the [Thread Trash operation](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations/#trash-a-thread) instead.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Delete**.
- **Message ID**: Enter the ID of the message you want to delete.

Refer to the [Gmail API Method: users.messages.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/delete) documentation for more information.

## Get a message [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#get-a-message "Permanent link")

Use this operation to get a single message.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Get**.
- **Message ID**: Enter the ID of the message you wish to retrieve.
- **Simplify**: Choose whether to return a simplified version of the response (turned on) or the raw data (turned off). Default is on.
  - This is the same as setting the `format` for the API call to `metadata`, which returns email message IDs, labels, and email headers, including: From, To, CC, BCC, and Subject.

Refer to the [Gmail API Method: users.messages.get](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get) documentation for more information.

## Get Many messages [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#get-many-messages "Permanent link")

Use this operation to get two or more messages.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Get Many**.
- **Return All**: Choose whether the node returns all messages (turned on) or only up to a set limit (turned off).
- **Limit**: Enter the maximum number of messages to return. Only used if you've turned off **Return All**.
- **Simplify**: Choose whether to return a simplified version of the response (turned on) or the raw data (turned off). Default is on.
  - This is the same as setting the `format` for the API call to `metadata`, which returns email message IDs, labels, and email headers, including: From, To, CC, BCC, and Subject.

### Get Many messages filters [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#get-many-messages-filters "Permanent link")

Use these filters to further refine the node's behavior:

- **Include Spam and Trash**: Select whether the node should get messages in the Spam and Trash folders (turned on) or not (turned off).
- **Label Names or IDs**: Only return messages with the selected labels added to them. Select the Label names you want to apply or enter an expression to specify IDs. The dropdown populates based on the **Credential** you selected.
- **Search**: Enter Gmail search refine filters, like `from:`, to filter the messages returned. Refer to [Refine searches in Gmail](https://support.google.com/mail/answer/7190?hl=en) for more information.
- **Read Status**: Choose whether to receive **Unread and read emails**, **Unread emails only** (default), or **Read emails only**.
- **Received After**: Return only those emails received after the specified date and time. Use the date picker to select the day and time or enter an expression to set a date as a string in ISO format or a timestamp in milliseconds. Refer to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) for more information on formatting the string.
- **Received Before**: Return only those emails received before the specified date and time. Use the date picker to select the day and time or enter an expression to set a date as a string in ISO format or a timestamp in milliseconds. Refer to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) for more information on formatting the string.
- **Sender**: Enter an email or a part of a sender name to return messages from only that sender.

Refer to the [Gmail API Method: users.messages.list](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list) documentation for more information.

## Mark as Read [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#mark-as-read "Permanent link")

Use this operation to mark a message as read.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Mark as Read**.
- **Message ID**: Enter the ID of the message you wish to mark as read.

Refer to the [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify) documentation for more information.

## Mark as Unread [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#mark-as-unread "Permanent link")

Use this operation to mark a message as unread.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Mark as Unread**.
- **Message ID**: Enter the ID of the message you wish to mark as unread.

Refer to the [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify) documentation for more information.

## Remove Label from a message [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#remove-label-from-a-message "Permanent link")

Use this operation to remove one or more labels from a message.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Remove Label**.
- **Message ID**: Enter the ID of the message you want to remove the label from.
- **Label Names or IDs**: Select the Label names you want to remove or enter an expression to specify IDs. The dropdown populates based on the **Credential** you selected.

Refer to the [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify) documentation for more information.

## Reply to a message [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#reply-to-a-message "Permanent link")

Use this operation to send a message as a reply to an existing message.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Reply**.
- **Message ID**: Enter the ID of the message you want to reply to.
- Select the **Email Type**. Choose from **Text** or **HTML**.
- **Message**: Enter the email message body.

### Reply options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#reply-options "Permanent link")

Use these options to further refine the node's behavior:

- **Append n8n attribution**: By default, the node appends the statement `This email was sent automatically with n8n` to the end of the email. To remove this statement, turn this option off.
- **Attachments**: Select **Add Attachment** to add an attachment. Enter the **Attachment Field Name (in Input)** to identify which field from the input node contains the attachment.
  - For multiple properties, enter a comma-separated list.
- **BCC**: Enter one or more email addresses for blind copy recipients. Separate multiple email addresses with a comma, for example `jay@gatsby.com, jon@smith.com`.
- **CC**: Enter one or more email addresses for carbon copy recipients. Separate multiple email addresses with a comma, for example `jay@gatsby.com, jon@smith.com`.
- **Sender Name**: Enter the name you want displayed in your recipients' email as the sender.
- **Reply to Sender Only**: Choose whether to reply all (turned off) or reply to the sender only (turned on).

Refer to the [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) documentation for more information.

## Send a message [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#send-a-message "Permanent link")

Use this operation to send a message.

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Send**.
- **To**: Enter the email address you want the email sent to.
- **Subject**: Enter the subject line.
- Select the **Email Type**. Choose from **Text** or **HTML**.
- **Message**: Enter the email message body.

### Send options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#send-options "Permanent link")

Use these options to further refine the node's behavior:

- **Append n8n attribution**: By default, the node appends the statement `This email was sent automatically with n8n` to the end of the email. To remove this statement, turn this option off.
- **Attachments**: Select **Add Attachment** to add an attachment. Enter the **Attachment Field Name (in Input)** to identify which field from the input node contains the attachment.
  - For multiple properties, enter a comma-separated list.
- **BCC**: Enter one or more email addresses for blind copy recipients. Separate multiple email addresses with a comma, for example `jay@gatsby.com, jon@smith.com`.
- **CC**: Enter one or more email addresses for carbon copy recipients. Separate multiple email addresses with a comma, for example `jay@gatsby.com, jon@smith.com`.
- **Sender Name**: Enter the name you want displayed in your recipients' email as the sender.
- **Send Replies To**: Enter an email address to set as the reply to address.
- **Reply to Sender Only**: Choose whether to reply all (turned off) or reply to the sender only (turned on).

Refer to the [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) documentation for more information.

## Send a message and wait for approval [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#send-a-message-and-wait-for-approval "Permanent link")

Use this operation to send a message and wait for approval from the recipient before continuing the workflow execution.

Use Wait for complex approvals

The **Send and Wait for Approval** operation is well-suited for simple approval processes. For more complex approvals, consider using the [Wait node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/).

Enter these parameters:

- Select the **Credential to connect with** or create a new one.
- **Resource**: Select **Message**.
- **Operation**: Select **Send and Wait for Approval**.
- **To**: Enter the email address you want the email sent to.
- **Subject**: Enter the subject line.
- **Message**: Enter the email message body.

### Send and wait for approval options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#send-and-wait-for-approval-options "Permanent link")

Use these options to further refine the node's behavior:

- **Type of Approval**: Choose **Approve Only** (default) to include only an approval button or **Approve and Disapprove** to also include a disapproval option.
- **Approve Button Label**: The label to use for the approval button ( **Approve** by default).
- **Approve Button Style**: Whether to style the approval button as a **Primary** (default) or **Secondary** button.
- **Disapprove Button Label**: The label to use for the disapproval button ( **Decline** by default). Only visible when you set **Type of Approval** to **Approve and Disapprove**.
- **Disapprove Button Style**: Whether to style the disapproval button as a **Primary** or **Secondary** (default) button. Only visible when you set **Type of Approval** to **Approve and Disapprove**.

Refer to the [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) documentation for more information.

## Common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/\#common-issues "Permanent link")

For common errors or issues and suggested resolution steps, refer to [Common Issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top