---
url: "https://docs.n8n.io/hosting/securing/blocking-nodes/"
title: "Block access to nodes | n8n Docs "
---

[Skip to content](https://docs.n8n.io/hosting/securing/blocking-nodes/#block-access-to-nodes)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/hosting/securing/blocking-nodes.md "Edit this page")

# Block access to nodes [\#](https://docs.n8n.io/hosting/securing/blocking-nodes/\#block-access-to-nodes "Permanent link")

For security reasons, you may want to block your users from accessing or working with specific n8n nodes. This is helpful if your users might be untrustworthy.

Use the `NODES_EXCLUDE` environment variable to prevent your users from accessing specific nodes.

## Exclude nodes [\#](https://docs.n8n.io/hosting/securing/blocking-nodes/\#exclude-nodes "Permanent link")

Update your `NODES_EXCLUDE` environment variable to include an array of strings containing any nodes you want to block your users from using.

For example, setting the variable this way:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"<br>``` |

Blocks the [Execute Command](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/) and [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/) nodes.

Your n8n users won't be able to search for or use these nodes.

## Suggested nodes to block [\#](https://docs.n8n.io/hosting/securing/blocking-nodes/\#suggested-nodes-to-block "Permanent link")

The nodes that can pose security risks vary based on your use case and user profile. Here are some nodes you might want to start with:

- [Execute Command](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/)
- [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/)

## Related resources [\#](https://docs.n8n.io/hosting/securing/blocking-nodes/\#related-resources "Permanent link")

Refer to [Nodes environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/nodes/) for more information on this environment variable.

Refer to [Configuration](https://docs.n8n.io/hosting/configuration/configuration-methods/) for more information on setting environment variables.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top