---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3/"
title: "S3 node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3/#s3-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.s3.md "Edit this page")

# S3 node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3/\#s3-node "Permanent link")

Use the S3 node to automate work in non-AWS S3 storage and integrate S3 with other applications. n8n has built-in support for a wide range of S3 features, including creating, deleting, and getting buckets, files, and folders. For AWS S3, use [AWS S3](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awss3/).

Use the S3 node for non-AWS S3 solutions like:

- [MinIO](https://min.io/)
- [Wasabi](https://wasabi.com/)
- [Digital Ocean spaces](https://www.digitalocean.com/products/spaces)

On this page, you'll find a list of operations the S3 node supports and links to more resources.

Credentials

Refer to [S3 credentials](https://docs.n8n.io/integrations/builtin/credentials/s3/) for guidance on setting up authentication.

This node can be used as an AI tool

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/advanced-ai/examples/using-the-fromai-function/).

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3/\#operations "Permanent link")

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

Attach file for upload

To attach a file for upload, use another node to pass the file as a data property. Nodes like the [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/) node or the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) work well.

- Folder
  - Create a folder
  - Delete a folder
  - Get all folders

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3/\#templates-and-examples "Permanent link")

**Flux AI Image Generator**

by Max Tkacz

[View template details](https://n8n.io/workflows/2417-flux-ai-image-generator/)

**Hacker News to Video Content**

by Alex Kim

[View template details](https://n8n.io/workflows/2557-hacker-news-to-video-content/)

**Transcribe audio files from Cloud Storage**

by Lorena

[View template details](https://n8n.io/workflows/1394-transcribe-audio-files-from-cloud-storage/)

[Browse S3 integration templates](https://n8n.io/integrations/s3/), or [search all templates](https://n8n.io/workflows/)

## Node reference [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3/\#node-reference "Permanent link")

### Setting file permissions in Wasabi [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3/\#setting-file-permissions-in-wasabi "Permanent link")

When uploading files to [Wasabi](https://wasabi.com/), you must set permissions for the files using the **ACL** dropdown and not the toggles.

[![File permissions when using the S3 node with Wasabi](https://docs.n8n.io/_images/integrations/builtin/app-nodes/s3/acl_dropdown.png)](https://docs.n8n.io/_images/integrations/builtin/app-nodes/s3/acl_dropdown.png)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top