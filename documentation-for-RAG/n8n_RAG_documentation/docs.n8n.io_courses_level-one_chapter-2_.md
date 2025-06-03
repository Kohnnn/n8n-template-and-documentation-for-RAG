---
url: "https://docs.n8n.io/courses/level-one/chapter-2/"
title: "Building a mini-workflow | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-one/chapter-2/#building-a-mini-workflow)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-2.md "Edit this page")

# Building a Mini-workflow [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#building-a-mini-workflow "Permanent link")

In this lesson, you will build a small [workflow](https://docs.n8n.io/glossary/#workflow-n8n) that gets 10 articles about automation from Hacker News. The process consists of five steps:

1. [Add a Manual Trigger node](https://docs.n8n.io/courses/level-one/chapter-2/#1-add-a-manual-trigger-node)
2. [Add the Hacker News node](https://docs.n8n.io/courses/level-one/chapter-2/#2-add-the-hacker-news-node)
3. [Configure the Hacker News node](https://docs.n8n.io/courses/level-one/chapter-2/#3-configure-the-hacker-news-node)
4. [Execute the node](https://docs.n8n.io/courses/level-one/chapter-2/#4-execute-the-node)
5. [Save the workflow](https://docs.n8n.io/courses/level-one/chapter-2/#5-save-the-workflow)

The finished workflow will look like this:

[View workflow file](https://docs.n8n.io/_workflows//courses/level-one/chapter-2.json)

## 1\. Add a Manual Trigger node [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#1-add-a-manual-trigger-node "Permanent link")

Open the nodes panel (reminder: you can open this by selecting the **+** icon in the top right corner of the [canvas](https://docs.n8n.io/glossary/#canvas-n8n) or selecting `Tab` on your keyboard).

Then:

1. Search for the **Manual Trigger** node.
2. Select it when it appears in the search.

This will add the [Manual Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger/) node to your canvas, which allows you to run the workflow at any time by selecting the **Execute workflow** button.

Manual triggers

For faster workflow creation, you can skip this step in the future. Adding any other node without a trigger will add the Manual Trigger node to the workflow.

In a real-world scenario, you would probably want to set up a schedule or some other [trigger](https://docs.n8n.io/glossary/#trigger-node-n8n) to run the workflow.

## 2\. Add the Hacker News node [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#2-add-the-hacker-news-node "Permanent link")

Select the **+** icon to the right of the Manual Trigger node to open the nodes panel.

Then:

1. Search for the **Hacker News** node.
2. Select it when it appears in the search.
3. In the **Actions** section, select **Get many items**.

n8n adds the node to your canvas and the node window opens to display its configuration details.

## 3\. Configure the Hacker News node [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#3-configure-the-hacker-news-node "Permanent link")

When you add a new node to the Editor UI, the node is automatically activated. The node details will open in a window with several options:

- **Parameters**: Adjust parameters to refine and control the node's functionality.
- **Settings**: Adjust settings to control the node's design and executions.
- **Docs**: Open the n8n documentation for this node in a new window.

Parameters vs. Settings

- **Parameters** are different for each node, depending on its functionality.
- **Settings** are the same for all nodes.

### Parameters [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#parameters "Permanent link")

We need to configure several parameters for the Hacker News node to make it work:

- **Resource**: All


This resource selects all data records (articles).
- **Operation**: Get Many


This operation fetches all the selected articles.
- **Limit**: 10


This parameter sets a limit to the number of results the Get Many operation returns.
- **Additional Fields** \> **Add Field** \> **Keyword**: automation

**Additional fields** are options that you can add to certain nodes to make your request more specific or filter the results. For this example, we want to get only articles that include the keyword "automation."


The configuration of the parameters for the Hacker News node should now look like this:

[![Hacker News node parameters](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c-2-hacker-news-node-parameters.png)](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c-2-hacker-news-node-parameters.png) _Hacker News node parameters_

### Settings [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#settings "Permanent link")

The **Settings** section includes several options for node design and executions. In this case, we'll configure only the final two settings, which set the node's appearance in the Editor UI canvas.

In the Hacker News node Settings, edit:

- **Notes**: Get the 10 latest articles.



Node notes



It's often helpful to add a short description in the node about what it does. This is helpful for complex or shared workflows in particular!

- **Display note in flow?**: toggle to true


This option will display the Note under the node in the canvas.


The configuration of the settings for the Hacker News node should now look like this:

[![Hacker News node settings](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-hacker-news-node-setting-configuration.png)](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-hacker-news-node-setting-configuration.png) _Hacker News node settings_

Renaming a node

You can rename the node with a name that's more descriptive for your use case. There are three ways to do this:

- Select the node you want to rename and at the same time press the F2 key on your keyboard.
- Double-click on the node to open the node window. Click on the name of the node in the top left corner of the window, rename it as you like, then click **Rename** to save the node under the new name.
- Right-click on the node and select the **Rename** option, or select the node and press F2 on your keyboard.

[![Renaming a node](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-renaming-a-node-from-the-keyboard.png)](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-renaming-a-node-from-the-keyboard.png) _Renaming a node from the keyboard_

To find the original node name (the type of node), open the node window and select **Settings**. The bottom of the page contains the node type and version.

## 4\. Execute the node [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#4-execute-the-node "Permanent link")

Select the **Execute step** button in the node details window. You should see 10 results in the Output **Table** view.

[![Results in Table view for the Hacker News node](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-results-in-table-view-for-the-hacker-news-node.png)](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-results-in-table-view-for-the-hacker-news-node.png) _Results in Table view for the Hacker News node_

### Node executions [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#node-executions "Permanent link")

Node execution

A node execution represents a run of that node to retrieve or process the specified data.

If a node executes successfully, a small green checkmark appears on top of the node in the canvas

[![Successfully executed workflow](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-successfully-executed-workflow.png)](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-successfully-executed-workflow.png) _Successfully executed workflow_

If there are no problems with the parameters and everything works fine, the requested data displays in the node window in **Table**, **JSON**, and **Schema** format. You can switch between these views by selecting the one you want from the **Table \| JSON \| Schema** button at the top of the node window.

Table vs JSON views

The **Table** view is the default. It displays the requested data in a table, where the rows are the records and the columns are the available attributes of those records.

Here's our Hacker News output in JSON view:

[![Results in JSON view for the Hacker News node](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-results-in-json-view-for-the-hacker-news-node.png)](https://docs.n8n.io/_images/courses/level-one/chapter-two/l1-c2-results-in-json-view-for-the-hacker-news-node.png) _Results in JSON view for the Hacker News node_

The node window displays more information about the node execution:

- Next to the **Output** title, notice a small icon (this will be a green checkmark if the node execution succeeded). Beside it, there is an info icon. If you hover on it, you'll get two more pieces of information that can provide insights into the performance of each individual node in a workflow:
  - **Start Time**: When the node execution started.
  - **Execution Time**: How long it took for the node to return the results from the moment it started executing.
- Just below the **Output** title, you'll notice another piece of information: **10 items**. This field displays the number of items (records) that the node request returned. In this example, it's expected to be 10, since this is the limit we set in step 2. But if you don't set a limit, it's useful to see how many records are actually returned.

Error in nodes

A red warning icon on a node means that the node has errors. This might happen if the node credentials are missing or incorrect or the node parameters aren't configured correctly.

[![Error in nodes](https://docs.n8n.io/_images/courses/level-one/chapter-one/error-node.png)](https://docs.n8n.io/_images/courses/level-one/chapter-one/error-node.png) _Error in nodes_

## 5\. Save the workflow [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#5-save-the-workflow "Permanent link")

Once you're finished editing the node, select **Back to canvas** to return to the main canvas.

By default, your workflow is automatically saved as "My workflow."

For this lesson, rename the workflow to be "Hacker News workflow."

Reminder

You can rename a workflow by clicking on the workflow's name at the top of the Editor UI.

Once you've renamed the workflow, be sure to save it.

There are two ways in which you can save a workflow:

- From the Canvas in Editor UI, click **Ctrl + S** or **Cmd + S** on your keyboard.
- Select the **Save** button in the top right corner of the Editor UI. You may need to leave the node editor first by clicking outside the dialog.

If you see a grey **Saved** text instead of the **Save** button, your workflow was automatically saved.

## Summary [\#](https://docs.n8n.io/courses/level-one/chapter-2/\#summary "Permanent link")

Congratulations, you just built your first workflow! In this lesson, you learned how to use actions in app nodes, configure their parameters and settings, and save and execute your workflow.

In the next lesson, you'll meet your new client, Nathan, who needs to automate his sales reporting work. You will build a more complex workflow for his use case, helping him become more productive at work.