---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi/"
title: "Facebook Graph API node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi/#facebook-graph-api-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi.md "Edit this page")

# Facebook Graph API node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi/\#facebook-graph-api-node "Permanent link")

Use the Facebook Graph API node to automate work in Facebook Graph API, and integrate Facebook Graph API with other applications. n8n has built-in support for a wide range of Facebook Graph API features, including using queries GET POST DELETE for several parameters like host URL, request methods and much more.

On this page, you'll find a list of operations the Facebook Graph API node supports and links to more resources.

Credentials

Refer to [Facebook Graph API credentials](https://docs.n8n.io/integrations/builtin/credentials/facebookgraph/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi/\#operations "Permanent link")

- **Default**
  - GET
  - POST
  - DELETE
- **Video Uploads**
  - GET
  - POST
  - DELETE

### Parameters [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi/\#parameters "Permanent link")

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

- **Host URL**: The host URL for the request. The following options are available:
  - **Default**: Requests are passed to the `graph.facebook.com` host URL. Used for the majority of requests.
  - **Video**: Requests are passed to the `graph-video.facebook.com` host URL. Used for video upload requests only.
- **HTTP Request Method**: The method to be used for this request, from the following options:
  - **GET**
  - **POST**
  - **DELETE**
- **Graph API Version**: The version of the [Facebook Graph API](https://developers.facebook.com/docs/graph-api/changelog) to be used for this request.
- **Node**: The node on which to operate, for example `/<page-id>/feed`. Read more about it in the [official Facebook Developer documentation](https://developers.facebook.com/docs/graph-api/using-graph-api).
- **Edge**: Edge of the node on which to operate. Edges represent collections of objects which are attached to the node.
- **Ignore SSL Issues**: Toggle to still download the response even if SSL certificate validation isn't possible.
- **Send Binary File**: Available for `POST` operations. If enabled binary data is sent as the body. Requires setting the following:
  - **Input Binary Field**: Name of the binary property which contains the data for the file to be uploaded.

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi/\#templates-and-examples "Permanent link")

**✨🤖Automate Multi-Platform Social Media Content Creation with AI**

by Joseph LePage

[View template details](https://n8n.io/workflows/3066-automate-multi-platform-social-media-content-creation-with-ai/)

**AI-Powered Social Media Content Generator & Publisher**

by Amjid Ali

[View template details](https://n8n.io/workflows/2950-ai-powered-social-media-content-generator-and-publisher/)

**Generate Instagram Content from Top Trends with AI Image Generation**

by mustafa kendigüzel

[View template details](https://n8n.io/workflows/2803-generate-instagram-content-from-top-trends-with-ai-image-generation/)

[Browse Facebook Graph API integration templates](https://n8n.io/integrations/facebook-graph-api/), or [search all templates](https://n8n.io/workflows/)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top