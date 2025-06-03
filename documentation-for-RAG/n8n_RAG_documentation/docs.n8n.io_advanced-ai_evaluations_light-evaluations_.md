---
url: "https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/"
title: "Light evaluations | n8n Docs "
---

[Skip to content](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/#light-evaluations)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/advanced-ai/evaluations/light-evaluations.md "Edit this page")

# Light evaluations [\#](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/\#light-evaluations "Permanent link")

Available on registered community and paid plans

Light evaluations are available to registered community users and on all paid plans.

## What are light evaluations? [\#](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/\#what-are-light-evaluations "Permanent link")

When building your workflow, you often want to test it with a handful of examples to get a sense of how it performs and make improvements. At this stage of workflow development, looking over workflow outputs for each example is often enough. The benefits of setting up more [formal scoring or metrics](https://docs.n8n.io/advanced-ai/evaluations/metric-based-evaluations/) don't yet justify the effort.

Light evaluation allows you to run the examples in a test dataset through your workflow one-by-one, writing the outputs back to your dataset. You can then examine those outputs next to each other, and visually compare them to the expected outputs (if you have them).

## How it works [\#](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/\#how-it-works "Permanent link")

Requires Google Sheets

Evaluations use Google Sheets to store the test dataset. To use evaluations, you must configure a [Google Sheets credential](https://docs.n8n.io/integrations/builtin/credentials/google/).

Light evaluations take place in the 'Editor' tab of your workflow, although you’ll find instructions on how to set it up in the 'Evaluations' tab.

Steps:

1. Create a dataset
2. Wire the dataset up to the workflow
3. Write workflow outputs back to dataset
4. Run evaluation

The following explanation will use a sample workflow that assigns a category and priority to incoming support tickets.

[![Example AI workflow ](https://docs.n8n.io/_images/advanced-ai/evaluations/example-ai-workflow.png)](https://docs.n8n.io/_images/advanced-ai/evaluations/example-ai-workflow.png)

### 1\. Create a dataset [\#](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/\#1-create-a-dataset "Permanent link")

Create a Google Sheet with a handful of examples for your workflow. Your sheet should contain column(s) for:

- The workflow input
- (Optional) The expected or correct workflow output
- The actual output

Leave the actual output column or columns blank, since you'll be filling them during the evaluation.

[![Sample dataset for a support ticket classification workflow](https://docs.n8n.io/_images/advanced-ai/evaluations/sample-dataset.png)](https://docs.n8n.io/_images/advanced-ai/evaluations/sample-dataset.png) A [sample dataset](https://docs.google.com/spreadsheets/d/1uuPS5cHtSNZ6HNLOi75A2m8nVWZrdBZ_Ivf58osDAS8/edit?gid=294497137#gid=294497137) for the support ticket classification workflow.

### 2\. Wire the dataset up to your workflow [\#](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/\#2-wire-the-dataset-up-to-your-workflow "Permanent link")

#### Insert an evaluation trigger to pull in your dataset [\#](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/\#insert-an-evaluation-trigger-to-pull-in-your-dataset "Permanent link")

Each time the evaluation trigger runs, it will output a single item representing one row of your dataset.

Clicking the 'Evaluate all' button to the left of the evaluation trigger will run your workflow multiple times in sequence, once for each row in your dataset. This is a special behavior of the evaluation trigger.

While wiring the trigger up, you often only want to run it once. You can do this by either:

- Setting the trigger's 'Max rows to process' to 1
- Clicking on the 'Execute node' button on the trigger (rather than the 'Evaluate all' button)

#### Wire the trigger up to your workflow [\#](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/\#wire-the-trigger-up-to-your-workflow "Permanent link")

You can now connect the evaluation trigger to the rest of your workflow and reference the data that it outputs. At a minimum, you need to use the dataset’s input column(s) later in the workflow.

If you have multiple triggers in your workflow you will need to [merge their branches together](https://docs.n8n.io/advanced-ai/evaluations/tips-and-common-issues/#combining-multiple-triggers).

[![Connecting the evaluation trigger](https://docs.n8n.io/_images/advanced-ai/evaluations/connecting-evaluation-trigger.png)](https://docs.n8n.io/_images/advanced-ai/evaluations/connecting-evaluation-trigger.png) The support ticket classification workflow with the evaluation trigger added in and wired up.

### 3\. Write workflow outputs back to dataset [\#](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/\#3-write-workflow-outputs-back-to-dataset "Permanent link")

To populate the output column(s) of your dataset when the evaluation runs:

- Insert the 'Set outputs' action of the evaluation node
- Wire it up to your workflow at a point after it has produced the outputs you're evaluating
- In the node's parameters, map the workflow outputs into the correct dataset column

[![Connecting the set outputs node](https://docs.n8n.io/_images/advanced-ai/evaluations/connecting-set-outputs-node.png)](https://docs.n8n.io/_images/advanced-ai/evaluations/connecting-set-outputs-node.png) The support ticket classification workflow with the 'set outputs' node added in and wired up.

### 4\. Run evaluation [\#](https://docs.n8n.io/advanced-ai/evaluations/light-evaluations/\#4-run-evaluation "Permanent link")

Click on the **Execute workflow** button to the left of the evaluation trigger. The workflow will execute multiple times, once for each row of the dataset:

[![Execute workflow button](https://docs.n8n.io/_images/advanced-ai/evaluations/execute-workflow-button.png)](https://docs.n8n.io/_images/advanced-ai/evaluations/execute-workflow-button.png)

Review the outputs of each execution in the Google Sheet, and examine the execution details using the workflow's 'executions' tab if you need to.

Once your dataset grows past a handful of examples, consider [metric-based evaluation](https://docs.n8n.io/advanced-ai/evaluations/metric-based-evaluations/) to get a numerical view of performance. See also [tips and common issues](https://docs.n8n.io/advanced-ai/evaluations/tips-and-common-issues/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top