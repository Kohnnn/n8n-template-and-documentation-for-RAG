---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube/"
title: "YouTube node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube/#youtube-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.youtube.md "Edit this page")

# YouTube node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube/\#youtube-node "Permanent link")

Use the YouTube node to automate work in YouTube, and integrate YouTube with other applications. n8n has built-in support for a wide range of YouTube features, including retrieving and updating channels, as well as creating and deleting playlists.

On this page, you'll find a list of operations the YouTube node supports and links to more resources.

Credentials

Refer to [YouTube credentials](https://docs.n8n.io/integrations/builtin/credentials/google/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube/\#operations "Permanent link")

- Channel
  - Retrieve a channel
  - Retrieve all channels
  - Update a channel
  - Upload a channel banner
- Playlist
  - Create a playlist
  - Delete a playlist
  - Get a playlist
  - Retrieve all playlists
  - Update a playlist
- Playlist Item
  - Add an item to a playlist
  - Delete a item from a playlist
  - Get a playlist's item
  - Retrieve all playlist items
- Video
  - Delete a video
  - Get a video
  - Retrieve all videos
  - Rate a video
  - Update a video
  - Upload a video
- Video Category
  - Retrieve all video categories

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube/\#templates-and-examples "Permanent link")

**⚡AI-Powered YouTube Video Summarization & Analysis**

by Joseph LePage

[View template details](https://n8n.io/workflows/2679-ai-powered-youtube-video-summarization-and-analysis/)

**AI Youtube Trend Finder Based On Niche**

by Leonardo Grigorio

[View template details](https://n8n.io/workflows/2606-ai-youtube-trend-finder-based-on-niche/)

**Hacker News to Video Content**

by Alex Kim

[View template details](https://n8n.io/workflows/2557-hacker-news-to-video-content/)

[Browse YouTube integration templates](https://n8n.io/integrations/youtube/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.youtube/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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