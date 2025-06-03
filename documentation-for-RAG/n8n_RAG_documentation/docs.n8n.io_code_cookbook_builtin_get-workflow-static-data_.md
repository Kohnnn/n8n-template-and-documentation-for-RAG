---
url: "https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data/"
title: "getWorkflowStaticData | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data/#getworkflowstaticdatatype)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/builtin/get-workflow-static-data.md "Edit this page")

# `getWorkflowStaticData(type)` [\#](https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data/\#getworkflowstaticdatatype "Permanent link")

This gives access to the static workflow data.

Experimental feature

- Static data isn't available when testing workflows. The workflow must be active and called by a [trigger](https://docs.n8n.io/glossary/#trigger-node-n8n) or webhook to save static data.
- This feature may behave unreliably under high-frequency workflow executions.

You can save data directly in the workflow. This data should be small.

As an example: you can save a timestamp of the last item processed from
an RSS feed or database. It will always return an object. Properties can then read, delete or
set on that object. When the workflow execution succeeds, n8n checks automatically if the data
has changed and saves it, if necessary.

There are two types of static data, global and node. Global static data is the
same in the whole workflow. Every node in the workflow can access it. The node static data is unique to the node. Only the node that set it can retrieve it again.

Example with global data:

[JavaScript](https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data/#__tabbed_1_1)[Python](https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data/#__tabbed_1_2)

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br>// Get the global workflow static data<br>const workflowStaticData = $getWorkflowStaticData('global');<br>// Access its data<br>const lastExecution = workflowStaticData.lastExecution;<br>// Update its data<br>workflowStaticData.lastExecution = new Date().getTime();<br>// Delete data<br>delete workflowStaticData.lastExecution;<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br># Get the global workflow static data<br>workflowStaticData = _getWorkflowStaticData('global')<br># Access its data<br>lastExecution = workflowStaticData.lastExecution<br># Update its data<br>workflowStaticData.lastExecution = new Date().getTime()<br># Delete data<br>delete workflowStaticData.lastExecution<br>``` |

Example with node data:

[JavaScript](https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data/#__tabbed_2_1)[Python](https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data/#__tabbed_2_2)

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br>// Get the static data of the node<br>const nodeStaticData = $getWorkflowStaticData('node');<br>// Access its data<br>const lastExecution = nodeStaticData.lastExecution;<br>// Update its data<br>nodeStaticData.lastExecution = new Date().getTime();<br>// Delete data<br>delete nodeStaticData.lastExecution;<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br># Get the static data of the node<br>nodeStaticData = _getWorkflowStaticData('node')<br># Access its data<br>lastExecution = nodeStaticData.lastExecution<br># Update its data<br>nodeStaticData.lastExecution = new Date().getTime()<br># Delete data<br>delete nodeStaticData.lastExecution<br>``` |

## Templates and examples [\#](https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data/\#templates-and-examples "Permanent link")

[View template details](https://n8n.io/workflows/2538-demo-workflow-how-to-use-workflowstaticdata/)