---
url: "https://docs.n8n.io/data/data-editing/"
title: "Data editing | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/data/data-editing/#data-editing)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-editing.md "Edit this page")

# Data editing [\#](https://docs.n8n.io/data/data-editing/\#data-editing "Permanent link")

n8n allows you to edit [pinned data](https://docs.n8n.io/data/data-pinning/). This means you can check different scenarios without setting up each scenario and sending the relevant data from your external system. It makes it easier to test edge cases.

For development only

Data editing isn't available for production workflow executions. It's a feature to help test workflows during development.

## Edit output data [\#](https://docs.n8n.io/data/data-editing/\#edit-output-data "Permanent link")

To edit output data:

1. Run the node to load data.
2. In the **OUTPUT** view, select **JSON** to switch to JSON view.
3. Select **Edit**![Edit data icon](https://docs.n8n.io/_images/data/data-pinning/edit-data.png).
4. Edit your data.
5. Select **Save**. n8n saves your data changes and pins your data.

## Use data from previous executions [\#](https://docs.n8n.io/data/data-editing/\#use-data-from-previous-executions "Permanent link")

You can copy data from nodes in previous workflow executions:

01. Open the left menu.
02. Select **Executions**.
03. Browse the workflow executions list to find the one with the data you want to copy.
04. Select **Open Past Execution**![Open past execution icon](https://docs.n8n.io/_images/data/data-pinning/open-execution.png).
05. Double click the node whose data you want to copy.
06. If it's table layout, select **JSON** to switch to JSON view.
07. There are two ways to copy the JSON:
08. Select the JSON you want by highlighting it, like selecting text. Then use `ctrl` \+ `c` to copy it.
09. Select the JSON you want to copy by clicking on a parameter. Then:
    1. Hover over the JSON. n8n displays the **Copy**![Copy data icon](https://docs.n8n.io/_images/data/data-pinning/copy-data.png) button.
    2. Select **Copy**![Copy data icon](https://docs.n8n.io/_images/data/data-pinning/copy-data.png).
    3. You can choose what to copy:
       - **Copy Item Path** and **Copy Parameter Path** gives you expressions that access parts of the JSON.
       - **Copy Value**: copies the entire selected JSON.
10. Return to the workflow you're working on:
    1. Open the left menu.
    2. Select **Workflows**.
    3. Select **Open**.
    4. Select the workflow you want to open.
11. Open the node where you want to use the copied data.
12. If there is no data, run the node to load data.
13. In the **OUTPUT** view, select **JSON** to switch to JSON view.
14. Select **Edit**![Edit data icon](https://docs.n8n.io/_images/data/data-pinning/edit-data.png).
15. Paste in the data from the previous execution.
16. Select **Save**. n8n saves your data changes and pins your data.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top