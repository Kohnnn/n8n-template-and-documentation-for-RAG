---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3/"
title: "AWS S3 node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3/#aws-s3-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.awss3.md "Edit this page")

# AWS S3 node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3/\#aws-s3-node "Permanent link")

Use the AWS S3 node to automate work in AWS S3, and integrate AWS S3 with other applications. n8n has built-in support for a wide range of AWS S3 features, including creating and deleting buckets, copying and downloading files, as well as getting folders.

On this page, you'll find a list of operations the AWS S3 node supports and links to more resources.

Credentials

Refer to [AWS credentials](https://docs.n8n.io/integrations/builtin/credentials/aws/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3/\#operations "Permanent link")

- Bucket
  - Create a bucket
  - Delete a bucket
  - Get all buckets
  - Search within a bucket
- File
  - Copy a file
  - Delete a file
  - Download a file
  - Get all files
  - Upload a file
- Folder
  - Create a folder
  - Delete a folder
  - Get all folders

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3/\#templates-and-examples "Permanent link")

**Transcribe audio files from Cloud Storage**

by Lorena

[View template details](https://n8n.io/workflows/1394-transcribe-audio-files-from-cloud-storage/)

**Extract and store text from chat images using AWS S3**

by Lorena

[View template details](https://n8n.io/workflows/1393-extract-and-store-text-from-chat-images-using-aws-s3/)

**Sync data between Google Drive and AWS S3**

by Lorena

[View template details](https://n8n.io/workflows/1396-sync-data-between-google-drive-and-aws-s3/)

[Browse AWS S3 integration templates](https://n8n.io/integrations/aws-s3/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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