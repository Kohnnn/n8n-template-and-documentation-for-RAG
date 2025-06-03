---
url: "https://docs.n8n.io/courses/level-two/chapter-4/"
title: "Dealing with errors in workflows | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-two/chapter-4/#dealing-with-errors-in-workflows)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-two/chapter-4.md "Edit this page")

# Dealing with errors in workflows [\#](https://docs.n8n.io/courses/level-two/chapter-4/\#dealing-with-errors-in-workflows "Permanent link")

Sometimes you build a nice workflow, but it fails when you try to execute it. Workflow executions may fail for a variety of reasons, ranging from straightforward problems with incorrectly configuring a node or a failure in a third-party service to more mysterious errors.

But don't panic. In this lesson, you'll learn how you can troubleshoot errors so you can get your workflow up and running as soon as possible.

## Checking failed workflows [\#](https://docs.n8n.io/courses/level-two/chapter-4/\#checking-failed-workflows "Permanent link")

n8n tracks executions of your workflows.

When one of your workflows fails, you can check the Executions log to see what went wrong. The Executions log shows you a list of the latest execution time, status, mode, and running time of your saved workflows.

Open the Executions log by selecting [**Executions**](https://docs.n8n.io/workflows/executions/#execution-modes) in the left-side panel.

To investigate a specific failed execution from the list, select the name or the **View** button that appears when you hover over the row of the respective execution.

[![Executions log](https://docs.n8n.io/_images/courses/level-two/chapter-four/explanation_workflowexecutions.png)](https://docs.n8n.io/_images/courses/level-two/chapter-four/explanation_workflowexecutions.png) _Executions log_

This will open the workflow in read-only mode, where you can see the execution of each node. This representation can help you identify at what point the workflow ran into issues.

To toggle between viewing the execution and the editor, select the **Editor \| Executions** button at the top of the page.

[![Workflow execution view](https://docs.n8n.io/_images/courses/level-two/chapter-four/explanation_workflowexecutions_readonly.png)](https://docs.n8n.io/_images/courses/level-two/chapter-four/explanation_workflowexecutions_readonly.png) _Workflow execution view_

## Catching erroring workflows [\#](https://docs.n8n.io/courses/level-two/chapter-4/\#catching-erroring-workflows "Permanent link")

To catch failed workflows, create a separate [**Error Workflow**](https://docs.n8n.io/flow-logic/error-handling/) with the [**Error Trigger node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger/). This workflow will only execute if the main workflow execution fails.

Use additional nodes in your **Error Workflow** that make sense, like sending notifications about the failed workflow and its errors using email or Slack.

To receive error messages for a failed workflow, set the **Error Workflow** in the [Workflow Settings](https://docs.n8n.io/workflows/settings/) to an Error Workflow that uses an **Error Trigger node**.

The only difference between a regular workflow and an Error Workflow is that the latter contains an **Error Trigger node**. Make sure to create this node before you set this as another workflow's designated Error Workflow.

Error workflows

- If a workflow uses the Error Trigger node, you don't have to activate the workflow.
- If a workflow contains the Error Trigger node, by default, the workflow uses itself as the error workflow.
- You can't test error workflows when running workflows manually. The Error trigger only runs when an automatic workflow errors.
- You can set the same Error Workflow for multiple workflows.

### Exercise [\#](https://docs.n8n.io/courses/level-two/chapter-4/\#exercise "Permanent link")

In the previous chapters, you've built several small workflows. Now, pick one of them that you want to monitor and create an Error Workflow for it:

1. Create a new Error Workflow.
2. Add the **Error Trigger node**.
3. Connect a node for the communication platform of your choice to the Error Trigger node, like [Slack](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/), [Discord](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/), [Telegram](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/), or even [Gmail](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/) or a more generic [Send Email](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail/).
4. In the workflow you want to monitor, open the [Workflow Settings](https://docs.n8n.io/workflows/settings/) and select the new Error Workflow you just created. Note that this workflow needs to run automatically to trigger the error workflow.

Show me the solution

The workflow for this exercise looks like this:

[![](https://docs.n8n.io/_images/courses/level-two/chapter-four/exercise_errors_errortriggernode_workflow.png)](https://docs.n8n.io/_images/courses/level-two/chapter-four/exercise_errors_errortriggernode_workflow.png) _Error workflow_

To check the configuration of the nodes, you can copy the JSON workflow code below and paste it into your Editor UI:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>``` | ```<br>{<br>	"nodes": [<br>		{<br>			"parameters": {},<br>			"name": "Error Trigger",<br>			"type": "n8n-nodes-base.errorTrigger",<br>			"typeVersion": 1,<br>			"position": [<br>				720,<br>				-380<br>			]<br>		},<br>		{<br>			"parameters": {<br>				"channel": "channelname",<br>				"text": "=This workflow {{$node[\"Error Trigger\"].json[\"workflow\"][\"name\"]}}failed.\nHave a look at it here: {{$node[\"Error Trigger\"].json[\"execution\"][\"url\"]}}",<br>				"attachments": [],<br>				"otherOptions": {}<br>			},<br>			"name": "Slack",<br>			"type": "n8n-nodes-base.slack",<br>			"position": [<br>				900,<br>				-380<br>			],<br>			"typeVersion": 1,<br>			"credentials": {<br>				"slackApi": {<br>					"id": "17",<br>					"name": "slack_credentials"<br>				}<br>			}<br>		}<br>	],<br>	"connections": {<br>		"Error Trigger": {<br>			"main": [<br>				[<br>					{<br>						"node": "Slack",<br>						"type": "main",<br>						"index": 0<br>					}<br>				]<br>			]<br>		}<br>	}<br>}<br>``` |

## Throwing exceptions in workflows [\#](https://docs.n8n.io/courses/level-two/chapter-4/\#throwing-exceptions-in-workflows "Permanent link")

Another way of troubleshooting workflows is to include a [**Stop and Error node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror/) in your workflow. This node throws an error. You can specify the error type:

- **Error Message**: returns a custom message about the error
- **Error Object**: returns the type of error

You can only use the **Stop and Error node** as the last node in a workflow.

When to throw errors

Throwing exceptions with the **Stop and Error node** is useful for verifying the data (or assumptions about the data) from a node and returning custom error messages.

If you are working with data from a third-party service, you may come across problems such as:

- Wrongly formatted JSON output
- Data with the wrong type (for example, numeric data that has a non-numeric value)
- Missing values
- Errors from remote servers

Though this kind of invalid data might not cause the workflow to fail right away, it could cause problems later on, and then it can become difficult to track the source error. This is why it's better to throw an error at the time you know there might be a problem.

[![Stop and Error node with error message](https://docs.n8n.io/_images/courses/level-two/chapter-four/exercise_errors_stopanderror.png)](https://docs.n8n.io/_images/courses/level-two/chapter-four/exercise_errors_stopanderror.png) _Stop and Error node with error message_

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top