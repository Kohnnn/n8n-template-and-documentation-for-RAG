---
url: "https://docs.n8n.io/flow-logic/error-handling/"
title: "Error handling | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/flow-logic/error-handling/#error-handling)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/flow-logic/error-handling.md "Edit this page")

# Error handling [\#](https://docs.n8n.io/flow-logic/error-handling/\#error-handling "Permanent link")

When designing your flow logic, it's a good practice to consider potential errors, and set up methods to handle them gracefully. With an error workflow, you can control how n8n responds to a workflow execution failure.

Investigating errors

To investigate failed executions, you can:

- Review your [Executions](https://docs.n8n.io/workflows/executions/), for a [single workflow](https://docs.n8n.io/workflows/executions/single-workflow-executions/) or [all workflows you have access to](https://docs.n8n.io/workflows/executions/all-executions/). You can [load data from previous execution](https://docs.n8n.io/workflows/executions/debug/) into your current workflow.
- Enable [Log streaming](https://docs.n8n.io/log-streaming/).

## Create and set an error workflow [\#](https://docs.n8n.io/flow-logic/error-handling/\#create-and-set-an-error-workflow "Permanent link")

For each workflow, you can set an error workflow in **Workflow Settings**. It runs if an execution fails. This means you can, for example, send email or Slack alerts when a workflow execution errors. The error workflow must start with the [Error Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger/).

You can use the same error workflow for multiple workflows.

1. Create a new workflow, with the Error Trigger as the first node.
2. Give the workflow a name, for example `Error Handler`.
3. Select **Save**.
4. In the workflow where you want to use this error workflow:
1. Select **Options**![Options menu icon](https://docs.n8n.io/_images/common-icons/three-dot-options-menu.png) \> **Settings**.
2. In **Error workflow**, select the workflow you just created. For example, if you used the name Error Handler, select **Error handler**.
3. Select **Save**.
      Now, when this workflow errors, the related error workflow runs.

## Error data [\#](https://docs.n8n.io/flow-logic/error-handling/\#error-data "Permanent link")

The default error data received by the Error Trigger is:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>``` | ```<br>[<br>	{<br>		"execution": {<br>			"id": "231",<br>			"url": "https://n8n.example.com/execution/231",<br>			"retryOf": "34",<br>			"error": {<br>				"message": "Example Error Message",<br>				"stack": "Stacktrace"<br>			},<br>			"lastNodeExecuted": "Node With Error",<br>			"mode": "manual"<br>		},<br>		"workflow": {<br>			"id": "1",<br>			"name": "Example Workflow"<br>		}<br>	}<br>]<br>``` |

All information is always present, except:

- `execution.id`: requires the execution to be saved in the database. Not present if the error is in the trigger node of the main workflow, as the workflow doesn't execute.
- `execution.url`: requires the execution to be saved in the database. Not present if the error is in the trigger node of the main workflow, as the workflow doesn't execute.
- `execution.retryOf`: only present when the execution is a retry of a failed execution.

If the error is caused by the trigger node of the main workflow, rather than a later stage, the data sent to the error workflow is different. There's less information in `execution{}` and more in `trigger{}`:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>``` | ```<br>{<br>  "trigger": {<br>    "error": {<br>      "context": {},<br>      "name": "WorkflowActivationError",<br>      "cause": {<br>        "message": "",<br>        "stack": ""<br>      },<br>      "timestamp": 1654609328787,<br>      "message": "",<br>      "node": {<br>        . . . <br>      }<br>    },<br>    "mode": "trigger"<br>  },<br>  "workflow": {<br>    "id": "",<br>    "name": ""<br>  }<br>}<br>``` |

## Cause a workflow execution failure using Stop And Error [\#](https://docs.n8n.io/flow-logic/error-handling/\#cause-a-workflow-execution-failure-using-stop-and-error "Permanent link")

When you create and set an error workflow, n8n runs it when an execution fails. Usually, this is due to things like errors in node settings, or the workflow running out of memory.

You can add the [Stop And Error](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror/) node to your workflow to force executions to fail under your chosen circumstances, and trigger the error workflow.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top