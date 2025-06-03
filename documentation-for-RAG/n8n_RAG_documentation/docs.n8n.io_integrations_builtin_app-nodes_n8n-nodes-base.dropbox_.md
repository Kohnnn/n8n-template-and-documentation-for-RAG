---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dropbox/"
title: "Dropbox node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dropbox/#dropbox-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.dropbox.md "Edit this page")

# Dropbox node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dropbox/\#dropbox-node "Permanent link")

Use the Dropbox node to automate work in Dropbox, and integrate Dropbox with other applications. n8n has built-in support for a wide range of Dropbox features, including creating, downloading, moving, and copying files and folders.

On this page, you'll find a list of operations the Dropbox node supports and links to more resources.

Credentials

Refer to [Dropbox credentials](https://docs.n8n.io/integrations/builtin/credentials/dropbox/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dropbox/\#operations "Permanent link")

- File
  - Copy a file
  - Delete a file
  - Download a file
  - Move a file
  - Upload a file
- Folder
  - Copy a folder
  - Create a folder
  - Delete a folder
  - Return the files and folders in a given folder
  - Move a folder
- Search
  - Query

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dropbox/\#templates-and-examples "Permanent link")

**Hacker News to Video Content**

by Alex Kim

[View template details](https://n8n.io/workflows/2557-hacker-news-to-video-content/)

**Nightly n8n backup to Dropbox**

by Joey D’Anna

[View template details](https://n8n.io/workflows/2075-nightly-n8n-backup-to-dropbox/)

**Manipulate PDF with Adobe developer API**

by digi-stud.io

[View template details](https://n8n.io/workflows/2424-manipulate-pdf-with-adobe-developer-api/)

[Browse Dropbox integration templates](https://n8n.io/integrations/dropbox/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.dropbox/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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