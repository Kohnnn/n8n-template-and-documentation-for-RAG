---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage/"
title: "Google Cloud Storage node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage/#google-cloud-storage-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage.md "Edit this page")

# Google Cloud Storage node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage/\#google-cloud-storage-node "Permanent link")

Use the Google Cloud Storage node to automate work in Google Cloud Storage, and integrate Google Cloud Storage with other applications. n8n has built-in support for a wide range of Google Cloud Storage features, including creating, updating, deleting, and getting buckets and objects.

On this page, you'll find a list of operations the Google Cloud Storage node supports and links to more resources.

Credentials

Refer to [Google Cloud Storage credentials](https://docs.n8n.io/integrations/builtin/credentials/google/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage/\#operations "Permanent link")

- Bucket
  - Create
  - Delete
  - Get
  - Get Many
  - Update
- Object
  - Create
  - Delete
  - Get
  - Get Many
  - Update

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage/\#templates-and-examples "Permanent link")

**Transcribe audio files from Cloud Storage**

by Lorena

[View template details](https://n8n.io/workflows/1394-transcribe-audio-files-from-cloud-storage/)

**Automatic Youtube Shorts Generator**

by Samautomation.work

[View template details](https://n8n.io/workflows/2856-automatic-youtube-shorts-generator/)

**Vector Database as a Big Data Analysis Tool for AI Agents \[1/3 anomaly\]\[1/2 KNN\]**

by Jenny

[View template details](https://n8n.io/workflows/2654-vector-database-as-a-big-data-analysis-tool-for-ai-agents-13-anomaly12-knn/)

[Browse Google Cloud Storage integration templates](https://n8n.io/integrations/google-cloud-storage/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage/\#related-resources "Permanent link")

Refer to Google's [Cloud Storage API documentation](https://cloud.google.com/storage/docs/apis) for detailed information about the API that this node integrates with.

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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