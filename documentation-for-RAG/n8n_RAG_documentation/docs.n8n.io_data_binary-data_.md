---
url: "https://docs.n8n.io/data/binary-data/"
title: "Binary data | n8n Docs "
---

[Skip to content](https://docs.n8n.io/data/binary-data/#binary-data)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/binary-data.md "Edit this page")

# Binary data [\#](https://docs.n8n.io/data/binary-data/\#binary-data "Permanent link")

Binary data is any file-type data, such as image files or documents.

This page collects resources relating to binary data in n8n.

## Working with binary data in your workflows [\#](https://docs.n8n.io/data/binary-data/\#working-with-binary-data-in-your-workflows "Permanent link")

You can process binary data in n8n workflows. n8n provides nodes to help you work with binary data. You can also use code.

### Nodes [\#](https://docs.n8n.io/data/binary-data/\#nodes "Permanent link")

There are three key nodes dedicated to handling binary data files:

- [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/) to read and write files from/to the machine where n8n is running.
- [Convert to File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile/) to take input data and output it as a file.
- [Extract From File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile/) to get data from a binary format and convert it to JSON.

There are separate nodes for working with XML and HTML data:

- [HTML](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html/)
- [XML](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.xml/)

And nodes for performing common tasks:

- [Compression](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression/)
- [Edit Image](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.editimage/)
- [FTP](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ftp/)

You can trigger a workflow based on changes to a local file using the [Local File trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger/).

To split or concatenate binary data items, use the [data transformation nodes](https://docs.n8n.io/data/#data-transformation-nodes).

### Code [\#](https://docs.n8n.io/data/binary-data/\#code "Permanent link")

You can use the [Code node](https://docs.n8n.io/code/code-node/) to manipulate binary data in your workflows. For example, [Get the binary data buffer](https://docs.n8n.io/code/cookbook/code-node/get-binary-data-buffer/): get the binary data available in your workflow.

## Configure binary data mode when self-hosting [\#](https://docs.n8n.io/data/binary-data/\#configure-binary-data-mode-when-self-hosting "Permanent link")

You can configure how your self-hosted n8n instance handles binary data using the [Binary data environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/binary-data/). This includes tasks such as setting the storage path and choosing how to store binary data.

Your configuration affects how well n8n scales: [Scaling \| Binary data filesystem mode](https://docs.n8n.io/hosting/scaling/binary-data/).

Reading and writing binary files can have security implications. If you want to disable reading and writing binary data, use the `NODES_EXCLUDE` environment variable. Refer to [Environment variables \| Nodes](https://docs.n8n.io/hosting/configuration/environment-variables/nodes/) for more information.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top