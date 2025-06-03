---
url: "https://docs.n8n.io/hosting/scaling/binary-data/"
title: "Scaling binary data in n8n | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/scaling/binary-data/#binary-data)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/scaling/binary-data.md "Edit this page")

# Binary data [\#](https://docs.n8n.io/hosting/scaling/binary-data/\#binary-data "Permanent link")

Binary data is any file-type data, such as image files or documents generated or processed during the execution of a workflow.

## Enable filesystem mode [\#](https://docs.n8n.io/hosting/scaling/binary-data/\#enable-filesystem-mode "Permanent link")

When handling binary data, n8n keeps the data in memory by default. This can cause crashes when working with large files.

To avoid this, change the `N8N_DEFAULT_BINARY_DATA_MODE` [environment variable](https://docs.n8n.io/hosting/configuration/environment-variables/binary-data/) to `filesystem`. This causes n8n to save data to disk, instead of using memory.

If you're using queue mode, keep this to `default`. n8n doesn't support filesystem mode with queue mode.

## Binary data pruning [\#](https://docs.n8n.io/hosting/scaling/binary-data/\#binary-data-pruning "Permanent link")

n8n executes binary data pruning as part of execution data pruning. Refer to [Execution data \| Enable data pruning](https://docs.n8n.io/hosting/scaling/execution-data/#enable-data-pruning) for details.

If you configure multiple binary data modes, binary data pruning operates on the active binary data mode. For example, if your instance stored data in S3, and you later switched to filesystem mode, n8n only prunes binary data in the filesystem. Refer to [External storage](https://docs.n8n.io/hosting/scaling/external-storage/#usage) for details.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top