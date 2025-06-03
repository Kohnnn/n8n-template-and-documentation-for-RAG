---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive/"
title: "TheHive node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive/#thehive-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.thehive.md "Edit this page")

# TheHive node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive/\#thehive-node "Permanent link")

Use the TheHive node to automate work in TheHive, and integrate TheHive with other applications. n8n has built-in support for a wide range of TheHive features, including creating alerts, counting tasks logs, cases, and observables.

On this page, you'll find a list of operations the TheHive node supports and links to more resources.

TheHive and TheHive 5

n8n provides two nodes for TheHive. Use this node (TheHive) if you want to use TheHive's version 3 or 4 API. If you want to use version 5, use [TheHive 5](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5/).

Credentials

Refer to [TheHive credentials](https://docs.n8n.io/integrations/builtin/credentials/thehive/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive/\#operations "Permanent link")

The available operations depend on your API version. To see the operations list, create your credentials, including selecting your API version. Then return to the node, select the resource you want to use, and n8n displays the available operations for your API version.

- Alert
- Case
- Log
- Observable
- Task

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive/\#templates-and-examples "Permanent link")

**Analyze emails with S1EM**

by v1d1an

[View template details](https://n8n.io/workflows/1602-analyze-emails-with-s1em/)

**Weekly Shodan Query - Report Accidents**

by n8n Team

[View template details](https://n8n.io/workflows/1977-weekly-shodan-query-report-accidents/)

**Create, update and get a case in TheHive**

by Harshil Agrawal

[View template details](https://n8n.io/workflows/808-create-update-and-get-a-case-in-thehive/)

[Browse TheHive integration templates](https://n8n.io/integrations/thehive/), or [search all templates](https://n8n.io/workflows/)

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive/\#related-resources "Permanent link")

n8n provides a trigger node for TheHive. You can find the trigger node docs [here](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger/).

Refer to TheHive's documentation for more information about the service:

- [Version 3](https://docs.thehive-project.org/thehive/legacy/thehive3/api/)
- [Version 4](https://docs.thehive-project.org/cortex/api/api-guide/)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top