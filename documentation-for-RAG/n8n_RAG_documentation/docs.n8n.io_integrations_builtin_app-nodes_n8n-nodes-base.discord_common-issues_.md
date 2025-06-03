---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues/"
title: "Discord node common issues | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues/#discord-node-common-issues)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues.md "Edit this page")

# Discord node common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues/\#discord-node-common-issues "Permanent link")

Here are some common errors and issues with the [Discord node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/) and steps to resolve or troubleshoot them.

## Add extra fields to embeds [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues/\#add-extra-fields-to-embeds "Permanent link")

Discord messages can optionally include embeds, a rich preview component that can include a title, description, image, link, and more.

The Discord node supports embeds when using the **Send** operation on the **Message** resource. Select **Add Embeds** to set extra fields including Description, Author, Title, URL, and URL Image.

To add fields that aren't included by default, set **Input Method** to **Raw JSON**. From here, add a JSON object to the **Value** parameter defining the [field names](https://discord.com/developers/docs/resources/message#embed-object) and values you want to include.

For example, to include `footer` and `fields`, neither of which are available using the **Enter Fields** Input Method, you could use a JSON object like this:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>``` | ```<br>{<br>    "author": "My Name",<br>	"url": "https://discord.js.org",<br>	"fields": [<br>		{<br>			"name": "Regular field title",<br>			"value": "Some value here"<br>		}<br>	],<br>	"footer": {<br>		"text": "Some footer text here",<br>		"icon_url": "https://i.imgur.com/AfFp7pu.png"<br>	}<br>}<br>``` |

You can learn more about embeds in [Using Webhooks and Embeds \| Discord](https://discord.com/safety/using-webhooks-and-embeds).

If you experience issues when working with embeds with the Discord node, you can use the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) with your existing Discord credentials to `POST` to the following URL:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>https://discord.com/api/v10/channels/<CHANNEL_ID>/messages<br>``` |

In the body, include your embed information in the message content like this:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>``` | ```<br>{<br>	"content": "Test",<br>	"embeds": [<br>		{<br>			"author": "My Name",<br>			"url": "https://discord.js.org",<br>			"fields": [<br>				{<br>					"name": "Regular field title",<br>					"value": "Some value here"<br>				}<br>			],<br>			"footer": {<br>				"text": "Some footer text here",<br>				"icon_url": "https://i.imgur.com/AfFp7pu.png"<br>			}<br>		}<br>	]<br>}<br>``` |

## Mention users and channels [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues/\#mention-users-and-channels "Permanent link")

To mention users and channels in Discord messages, you need to format your message according to [Discord's message formatting guidelines](https://discord.com/developers/docs/reference#message-formatting).

To mention a user, you need to know the Discord user's user ID. Keep in mind that the user ID is different from the user's display name. Similarly, you need a channel ID to link to a specific channel.

You can learn how to enable developer mode and copy the user or channel IDs in [Discord's documentation on finding User/Server/Message IDs](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID).

Once you have the user or channel ID, you can format your message with the following syntax:

- **User**: `<@USER_ID>`
- **Channel**: `<#CHANNEL_ID>`
- **Role**: `<@&ROLE_ID>`

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top