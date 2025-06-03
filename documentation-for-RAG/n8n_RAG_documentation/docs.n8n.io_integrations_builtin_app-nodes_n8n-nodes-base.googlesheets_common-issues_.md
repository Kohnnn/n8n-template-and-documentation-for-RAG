---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues/"
title: "Google Sheets node common issues | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues/#google-sheets-node-common-issues)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues.md "Edit this page")

# Google Sheets node common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues/\#google-sheets-node-common-issues "Permanent link")

Here are some common errors and issues with the [Google Sheets node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/) and steps to resolve or troubleshoot them.

## Append an array [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues/\#append-an-array "Permanent link")

To insert an array of data into Google Sheets, you must convert the array into a valid JSON (key, value) format.

To do so, consider using:

1. The [Split Out](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout/) node.
2. The [AI Transform](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aitransform/) node. For example, try entering something like:



|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>Convert 'languages' array to JSON (key, value) pairs.<br>``` |

3. The [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/).

## Column names were updated after the node's setup [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues/\#column-names-were-updated-after-the-nodes-setup "Permanent link")

You'll receive this error if the Google Sheet's column names have changed since you set up the node.

To refresh the column names, re-select **Mapping Column Mode**. This should prompt the node to fetch the column names again.

Once the column names refresh, update the node parameters.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top