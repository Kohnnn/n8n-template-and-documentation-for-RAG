---
url: "https://docs.n8n.io/code/cookbook/builtin/execution/"
title: "execution | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/cookbook/builtin/execution/#execution)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/builtin/execution.md "Edit this page")

# `execution` [\#](https://docs.n8n.io/code/cookbook/builtin/execution/\#execution "Permanent link")

## `execution.id` [\#](https://docs.n8n.io/code/cookbook/builtin/execution/\#executionid "Permanent link")

Contains the unique ID of the current workflow execution.

[JavaScript](https://docs.n8n.io/code/cookbook/builtin/execution/#__tabbed_1_1)[Python](https://docs.n8n.io/code/cookbook/builtin/execution/#__tabbed_1_2)

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>let executionId = $execution.id;<br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>executionId = _execution.id<br>``` |

## `execution.resumeUrl` [\#](https://docs.n8n.io/code/cookbook/builtin/execution/\#executionresumeurl "Permanent link")

The webhook URL to call to resume a [waiting](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/) workflow.

See the [Wait > On webhook call](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/#on-webhook-call) documentation to learn more.

## `execution.customData` [\#](https://docs.n8n.io/code/cookbook/builtin/execution/\#executioncustomdata "Permanent link")

This is only available in the Code node.

[JavaScript](https://docs.n8n.io/code/cookbook/builtin/execution/#__tabbed_2_1)[Python](https://docs.n8n.io/code/cookbook/builtin/execution/#__tabbed_2_2)

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br>// Set a single piece of custom execution data<br>$execution.customData.set("key", "value");<br>// Set the custom execution data object<br>$execution.customData.setAll({"key1": "value1", "key2": "value2"})<br>// Access the current state of the object during the execution<br>var customData = $execution.customData.getAll()<br>// Access a specific value set during this execution<br>var customData = $execution.customData.get("key")<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br># Set a single piece of custom execution data<br>_execution.customData.set("key", "value");<br># Set the custom execution data object<br>_execution.customData.setAll({"key1": "value1", "key2": "value2"})<br># Access the current state of the object during the execution<br>customData = _execution.customData.getAll()<br># Access a specific value set during this execution<br>customData = _execution.customData.get("key")<br>``` |

Refer to [Custom executions data](https://docs.n8n.io/workflows/executions/custom-executions-data/) for more information.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top