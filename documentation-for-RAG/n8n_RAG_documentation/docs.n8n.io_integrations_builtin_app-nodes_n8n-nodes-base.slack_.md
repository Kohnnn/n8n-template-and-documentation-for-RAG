---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/"
title: "Slack node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/#slack-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.slack.md "Edit this page")

# Slack node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/\#slack-node "Permanent link")

Use the Slack node to automate work in Slack, and integrate Slack with other applications. n8n has built-in support for a wide range of Slack features, including creating, archiving, and closing channels, getting users and files, as well as deleting messages.

On this page, you'll find a list of operations the Slack node supports and links to more resources.

Credentials

Refer to [Slack credentials](https://docs.n8n.io/integrations/builtin/credentials/slack/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/\#operations "Permanent link")

- **Channel**
  - **Archive** a channel.
  - **Close** a direct message or multi-person direct message.
  - **Create** a public or private channel-based conversation.
  - **Get** information about a channel.
  - **Get Many**: Get a list of channels in Slack.
  - **History**: Get a channel's history of messages and events.
  - **Invite** a user to a channel.
  - **Join** an existing channel.
  - **Kick**: Remove a user from a channel.
  - **Leave** a channel.
  - **Member**: List the members of a channel.
  - **Open** or resume a direct message or multi-person direct message.
  - **Rename** a channel.
  - **Replies**: Get a thread of messages posted to a channel.
  - **Sets purpose** of a channel.
  - **Sets topic** of a channel.
  - **Unarchive** a channel.
- **File**
  - **Get** a file.
  - **Get Many**: Get and filter team files.
  - **Upload**: Create or upload an existing file.
- **Message**
  - **Delete** a message
  - **Get permalink**: Get a message's permalink.
  - **Search** for messages
  - **Send** a message
  - **Send and Wait for Approval**: Send a message and wait for approval from the recipient before continuing.
  - **Update** a message
- **Reaction**
  - **Add** a reaction to a message.
  - **Get** a message's reactions.
  - **Remove** a reaction from a message.
- **Star**
  - **Add** a star to an item.
  - **Delete** a star from an item.
  - **Get Many**: Get a list of an authenticated user's stars.
- **User**
  - **Get** information about a user.
  - **Get Many**: Get a list of users.
  - **Get User's Profile**.
  - **Get User's Status**.
  - **Update User's Profile**.
- **User Group**
  - **Create** a user group.
  - **Disable** a user group.
  - **Enable** a user group.
  - **Get Many**: Get a list of user groups.
  - **Update** a user group.

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/\#templates-and-examples "Permanent link")

**Back Up Your n8n Workflows To Github**

by Jonathan

[View template details](https://n8n.io/workflows/1534-back-up-your-n8n-workflows-to-github/)

**Slack chatbot powered by AI**

by n8n Team

[View template details](https://n8n.io/workflows/1961-slack-chatbot-powered-by-ai/)

**Advanced AI Demo (Presented at AI Developers #14 meetup)**

by Max Tkacz

[View template details](https://n8n.io/workflows/2358-advanced-ai-demo-presented-at-ai-developers-14-meetup/)

[Browse Slack integration templates](https://n8n.io/integrations/slack/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/\#related-resources "Permanent link")

Refer to [Slack's documentation](https://api.slack.com/) for more information about the service.

## Required scopes [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/\#required-scopes "Permanent link")

Once you create a Slack app for your [Slack credentials](https://docs.n8n.io/integrations/builtin/credentials/slack/), you must add the appropriate scopes to your Slack app for this node to work. Start with the scopes listed in the [Scopes \| Slack credentials](https://docs.n8n.io/integrations/builtin/credentials/slack/#scopes) page.

If those aren't enough, use the table below to look up the resource and operation you want to use, then follow the link to Slack's API documentation to find the correct scopes.

| **Resource** | **Operation** | **Slack API method** |
| --- | --- | --- |
| Channel | Archive | [conversations.archive](https://api.slack.com/methods/conversations.archive) |
| Channel | Close | [conversations.close](https://api.slack.com/methods/conversations.close) |
| Channel | Create | [conversations.create](https://api.slack.com/methods/conversations.create) |
| Channel | Get | [conversations.info](https://api.slack.com/methods/conversations.info) |
| Channel | Get Many | [conversations.list](https://api.slack.com/methods/conversations.list) |
| Channel | History | [conversations.history](https://api.slack.com/methods/conversations.history) |
| Channel | Invite | [conversations.invite](https://api.slack.com/methods/conversations.invite) |
| Channel | Join | [conversations.join](https://api.slack.com/methods/conversations.join) |
| Channel | Kick | [conversations.kick](https://api.slack.com/methods/conversations.kick) |
| Channel | Leave | [conversations.leave](https://api.slack.com/methods/conversations.leave) |
| Channel | Member | [conversations.members](https://api.slack.com/methods/conversations.members) |
| Channel | Open | [conversations.open](https://api.slack.com/methods/conversations.open) |
| Channel | Rename | [conversations.rename](https://api.slack.com/methods/conversations.rename) |
| Channel | Replies | [conversations.replies](https://api.slack.com/methods/conversations.replies) |
| Channel | Set Purpose | [conversations.setPurpose](https://api.slack.com/methods/conversations.setPurpose) |
| Channel | Set Topic | [conversations.setTopic](https://api.slack.com/methods/conversations.setTopic) |
| Channel | Unarchive | [conversations.unarchive](https://api.slack.com/methods/conversations.unarchive) |
| File | Get | [files.info](https://api.slack.com/methods/files.info) |
| File | Get Many | [files.list](https://api.slack.com/methods/files.list) |
| File | Upload | [files.upload](https://api.slack.com/methods/files.upload) |
| Message | Delete | [chat.delete](https://api.slack.com/methods/chat.delete) |
| Message | Get Permalink | [chat.getPermalink](https://api.slack.com/methods/chat.getPermalink) |
| Message | Search | [search.messages](https://api.slack.com/methods/search.messages) |
| Message | Send | [chat.postMessage](https://api.slack.com/methods/chat.postMessage) |
| Message | Send and Wait for Approval | [chat.postMessage](https://api.slack.com/methods/chat.postMessage) |
| Message | Update | [chat.update](https://api.slack.com/methods/chat.update) |
| Reaction | Add | [reactions.add](https://api.slack.com/methods/reactions.add) |
| Reaction | Get | [reactions.get](https://api.slack.com/methods/reactions.get) |
| Reaction | Remove | [reactions.remove](https://api.slack.com/methods/reactions.remove) |
| Star | Add | [stars.add](https://api.slack.com/methods/stars.add) |
| Star | Delete | [stars.remove](https://api.slack.com/methods/stars.remove) |
| Star | Get Many | [stars.list](https://api.slack.com/methods/stars.list) |
| User | Get | [users.info](https://api.slack.com/methods/users.info) |
| User | Get Many | [users.list](https://api.slack.com/methods/users.list) |
| User | Get User's Profile | [users.profile.get](https://api.slack.com/methods/users.profile.get) |
| User | Get User's Status | [users.getPresence](https://api.slack.com/methods/users.getPresence) |
| User | Update User's Profile | [users.profile.set](https://api.slack.com/methods/users.profile.set) |
| User Group | Create | [usergroups.create](https://api.slack.com/methods/usergroups.create) |
| User Group | Disable | [usergroups.disable](https://api.slack.com/methods/usergroups.disable) |
| User Group | Enable | [usergroups.enable](https://api.slack.com/methods/usergroups.enable) |
| User Group | Get Many | [usergroups.list](https://api.slack.com/methods/usergroups.list) |
| User Group | Update | [usergroups.update](https://api.slack.com/methods/usergroups.update) |

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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