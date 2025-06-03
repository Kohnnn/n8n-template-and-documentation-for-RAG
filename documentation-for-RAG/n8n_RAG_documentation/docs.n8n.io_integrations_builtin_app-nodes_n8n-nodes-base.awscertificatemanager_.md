---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager/"
title: "AWS Certificate Manager node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager/#aws-certificate-manager-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager.md "Edit this page")

# AWS Certificate Manager node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager/\#aws-certificate-manager-node "Permanent link")

Use the AWS Certificate Manager node to automate work in AWS Certificate Manager, and integrate AWS Certificate Manager with other applications. n8n has built-in support for a wide range of AWS Certificate Manager features, including creating, deleting, getting, and renewing SSL certificates.

On this page, you'll find a list of operations the AWS Certificate Manager node supports and links to more resources.

Credentials

Refer to [AWS Certificate Manager credentials](https://docs.n8n.io/integrations/builtin/credentials/aws/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager/\#operations "Permanent link")

- Certificate
  - Delete
  - Get
  - Get Many
  - Get Metadata
  - Renew

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager/\#templates-and-examples "Permanent link")

**Transcribe audio files from Cloud Storage**

by Lorena

[View template details](https://n8n.io/workflows/1394-transcribe-audio-files-from-cloud-storage/)

**Extract and store text from chat images using AWS S3**

by Lorena

[View template details](https://n8n.io/workflows/1393-extract-and-store-text-from-chat-images-using-aws-s3/)

**Sync data between Google Drive and AWS S3**

by Lorena

[View template details](https://n8n.io/workflows/1396-sync-data-between-google-drive-and-aws-s3/)

[Browse AWS Certificate Manager integration templates](https://n8n.io/integrations/aws-certificate-manager/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager/\#related-resources "Permanent link")

Refer to [AWS Certificate Manager's documentation](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) for more information on this service.

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

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