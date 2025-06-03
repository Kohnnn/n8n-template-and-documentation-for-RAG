---
url: "https://docs.n8n.io/flow-logic/subworkflows/"
title: "Sub-workflows | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/flow-logic/subworkflows/#sub-workflows)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/flow-logic/subworkflows.md "Edit this page")

# Sub-workflows [\#](https://docs.n8n.io/flow-logic/subworkflows/\#sub-workflows "Permanent link")

You can call one workflow from another workflow. This allows you to build modular, microservice-like workflows. It can also help if your workflow grows large enough to encounter [memory issues](https://docs.n8n.io/hosting/scaling/memory-errors/). Creating sub-workflows uses the [Execute Workflow](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow/) and [Execute Sub-workflow Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger/) nodes.

## Set up and use a sub-workflow [\#](https://docs.n8n.io/flow-logic/subworkflows/\#set-up-and-use-a-sub-workflow "Permanent link")

This section walks through setting up both the parent workflow and sub-workflow.

### Create the sub-workflow [\#](https://docs.n8n.io/flow-logic/subworkflows/\#create-the-sub-workflow "Permanent link")

1. Create a new workflow.



Create sub-workflows from existing workflows



You can optionally create a sub-workflow directly from an existing parent workflow using the [Execute Sub-workflow](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow/) node. In the node, select the **Database** and **From list** options and select **Create a sub-workflow** in the list.

2. **Optional**: configure which workflows can call the sub-workflow:
1. Select the **Options**![Options menu](https://docs.n8n.io/_images/common-icons/three-dot-options-menu.png) menu > **Settings**. n8n opens the **Workflow settings** modal.
2. Change the **This workflow can be called by** setting. Refer to [Workflow settings](https://docs.n8n.io/workflows/settings/) for more information on configuring your workflows.
3. Add the **Execute Sub-workflow** trigger node (if you are searching under trigger nodes, this is also titled **When Executed by Another Workflow**).
4. Set the **Input data mode** to choose how you will define the sub-workflow's input data:
   - **Define using fields below**: Choose this mode to define individual input names and data types that the calling workflow needs to provide. The [Execute Sub-workflow node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow/) or [Call n8n Workflow Tool node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/) in the calling workflow will automatically pull in the fields defined here.
   - **Define using JSON example**: Choose this mode to provide an example JSON object that demonstrates the expected input items and their types.
   - **Accept all data**: Choose this mode to accept all data unconditionally. The sub-workflow won't define any required input items. This sub-workflow must handle any input inconsistencies or missing values.
5. Add other nodes as needed to build your sub-workflow functionality.
6. Save the sub-workflow.

Sub-workflow mustn't contain errors

If there are errors in the sub-workflow, the parent workflow can't trigger it.

Load data into sub-workflow before building

This requires the ability to [load data from previous executions](https://docs.n8n.io/workflows/executions/debug/), which is available on n8n Cloud and registered Community plans.

If you want to load data into your sub-workflow to use while building it:

1. Create the sub-workflow and add the **Execute Sub-workflow Trigger**.
2. Set the node's **Input data mode** to **Accept all data** or define the input items using fields or JSON if they're already known.
3. In the sub-workflow [settings](https://docs.n8n.io/workflows/settings/), set **Save successful production executions** to **Save**.
4. Skip ahead to setting up the parent workflow, and run it.
5. Follow the steps to [load data from previous executions](https://docs.n8n.io/workflows/executions/debug/).
6. Adjust the **Input data mode** to match the input sent by the parent workflow if necessary.

You can now pin example data in the trigger node, enabling you to work with real data while configuring the rest of the workflow.

### Call the sub-workflow [\#](https://docs.n8n.io/flow-logic/subworkflows/\#call-the-sub-workflow "Permanent link")

1. Open the workflow where you want to call the sub-workflow.
2. Add the **Execute Sub-workflow** node.
3. In the **Execute Sub-workflow** node, set the sub-workflow you want to call. You can choose to call the workflow by ID, load a workflow from a local file, add workflow JSON as a parameter in the node, or target a workflow by URL.



Find your workflow ID



Your sub-workflow's ID is the alphanumeric string at the end of its URL.

4. Fill in the required input items defined by the sub-workflow.

5. Save your workflow.

When your workflow executes, it will send data to the sub-workflow, and run it.

You can follow the execution flow from the parent workflow to the sub-workflow by opening the Execute Sub-workflow node and selecting the **View sub-execution** link. Likewise, the sub-workflow's execution contains a link back to the parent workflow's execution to navigate in the other direction.

## How data passes between workflows [\#](https://docs.n8n.io/flow-logic/subworkflows/\#how-data-passes-between-workflows "Permanent link")

As an example, imagine you have an Execute Sub-workflow node in **Workflow A**. The Execute Sub-workflow node calls another workflow called **Workflow B**:

1. The Execute Sub-workflow node passes the data to the Execute Sub-workflow Trigger node (titled "When executed by another node" in the canvas) of **Workflow B**.
2. The last node of **Workflow B** sends the data back to the Execute Sub-workflow node in **Workflow A**.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top