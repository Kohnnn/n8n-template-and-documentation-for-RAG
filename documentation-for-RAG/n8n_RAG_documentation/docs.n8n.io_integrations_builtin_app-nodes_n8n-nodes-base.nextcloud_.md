---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud/"
title: "Nextcloud node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud/#nextcloud-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud.md "Edit this page")

# Nextcloud node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud/\#nextcloud-node "Permanent link")

Use the Nextcloud node to automate work in Nextcloud, and integrate Nextcloud with other applications. n8n has built-in support for a wide range of Nextcloud features, including creating, updating, deleting, and getting files, and folders as well as retrieving, and inviting users.

On this page, you'll find a list of operations the Nextcloud node supports and links to more resources.

Credentials

Refer to [Nextcloud credentials](https://docs.n8n.io/integrations/builtin/credentials/nextcloud/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud/\#operations "Permanent link")

- File
  - Copy a file
  - Delete a file
  - Download a file
  - Move a file
  - Share a file
  - Upload a file
- Folder
  - Copy a folder
  - Create a folder
  - Delete a folder
  - Return the contents of a given folder
  - Move a folder
  - Share a folder
- User
  - Invite a user to a Nextcloud organization
  - Delete a user.
  - Retrieve information about a single user.
  - Retrieve a list of users.
  - Edit attributes related to a user.

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud/\#templates-and-examples "Permanent link")

**Save email attachments to Nextcloud**

by Manu

[View template details](https://n8n.io/workflows/1344-save-email-attachments-to-nextcloud/)

**Backs up n8n Workflows to NextCloud**

by dave

[View template details](https://n8n.io/workflows/175-backs-up-n8n-workflows-to-nextcloud/)

**Move a nextcloud folder file by file**

by Nico Kowalczyk

[View template details](https://n8n.io/workflows/1994-move-a-nextcloud-folder-file-by-file/)

[Browse Nextcloud integration templates](https://n8n.io/integrations/nextcloud/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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