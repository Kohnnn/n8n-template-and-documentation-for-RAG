---
url: "https://docs.n8n.io/courses/level-one/chapter-1/"
title: "Navigating the editor UI | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-one/chapter-1/#navigating-the-editor-ui)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-1.md "Edit this page")

# Navigating the Editor UI [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#navigating-the-editor-ui "Permanent link")

In this lesson you will learn how to navigate the [Editor UI](https://docs.n8n.io/glossary/#editor-n8n). We will walk through the [canvas](https://docs.n8n.io/glossary/#canvas-n8n) and show you what each icon means and where to find things you will need while building workflows in n8n.

n8n version

This course is based on n8n version 1.82.1. In other versions, some user interfaces might look different, but this shouldn't impact the core functionality.

## Getting started [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#getting-started "Permanent link")

Begin by setting up n8n.

We recommend starting with [n8n Cloud](https://app.n8n.cloud/register), a hosted solution that doesn't require installation and includes a free trial.

Alternative set up

If n8n Cloud isn't a good option for you, you can [self-host with Docker](https://docs.n8n.io/hosting/installation/docker/). This is an advanced option recommended only for technical users familiar with hosting services, Docker, and the command line.

For more details on the different ways to set up n8n, see our [platforms documentation](https://docs.n8n.io/choose-n8n/#platforms).

Once you have n8n running, open the Editor UI in a browser window. Log in to your n8n instance. Select **Overview** and then **Create Workflow** to view the main canvas.

It should look like this:

[![Editor UI](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-editor-ui.png)](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-editor-ui.png) _Editor UI_

## Editor UI settings [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#editor-ui-settings "Permanent link")

The editor UI is the web interface where you build [workflows](https://docs.n8n.io/workflows/). You can access all your workflows and [credentials](https://docs.n8n.io/glossary/#credential-n8n), as well as support pages, from the Editor UI.

### Left-side panel [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#left-side-panel "Permanent link")

On the left side of the **Editor UI**, there is a panel which contains the core functionalities and settings for managing your workflows. Expand and collapse it by selecting the small arrow icon.

The panel contains the following sections:

- **Overview**: Contains all the workflows and credentials you have access to. During this course, create new workflows here.
- **Projects**: (Not available on Community edition) Projects group workflows and credentials. You can assign [roles](https://docs.n8n.io/user-management/rbac/role-types/) to users in a project to control what they can do in a project. A **Personal** project is available by default.
- **Admin Panel**: n8n Cloud only. Access your n8n instance usage, billing, and version settings.
- **Templates**: A collection of pre-made workflows. Great place to get started with common use cases.
- **Variables**: Used to store and access fixed data across your workflows. This feature is available on the Pro and Enterprise Plans.
- **All executions**: Contains information about your workflow executions.
- **Help**: Contains resources around n8n product and community.
- **Update**: (When updates are available) Indicator for any recent product updates.
- **Settings**: Under the ellipsis ( `...`) menu by your username. Manage users and access settings for a variety of features.

[![Editor UI left-side menu](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-side-panel.png)](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-side-panel.png) _Editor UI left-side menu_

### Top bar [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#top-bar "Permanent link")

The top bar of the **Editor UI** contains the following information:

- **Workflow Name**: By default, n8n names a new workflow as "My workflow", but you can edit the name at any time.
- **\+ Add Tag**: Tags help you organise your workflows by category, use case, or whatever is relevant for you. Tags are optional.
- **Inactive/active toggle**: This button activates or deactivates the current workflow. By default, workflows are deactivated.
- **Share**: You can share and collaborate with others on workflows on the Starter, Pro, and Enterprise plans.
- **Save**: This button saves the current workflow.
- **History**: Once you save your workflow, you can view previous versions here.

[![Editor UI top bar](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-top-bar.png)](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-top-bar.png) _Editor UI top bar_

### Canvas [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#canvas "Permanent link")

The **canvas** is the gray dotted grid background in the Editor UI. It displays several icons and a node with different functionalities:

- Buttons to zoom the canvas to fit the screen, zoom in or out of the canvas, and tidy up the nodes on screen.
- A button to **Execute workflow** once you add your first node. When you click on it, n8n executes all nodes on the canvas in sequence.
- A button with a **+** sign inside. This button opens the nodes panel.
- A button with a note icon inside. This button adds a [sticky note](https://docs.n8n.io/workflows/components/sticky-notes/) to the canvas (visible when hovering on the top right + icon).
- A dotted square with the text "Add first step." This is where you add your first node.

[![Workflow canvas](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-canvas.png)](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-canvas.png) _Workflow canvas_

Moving the canvas

You can move the workflow canvas around in three ways:

- Select `Ctrl` + `Left Button` on the canvas and move it around.
- Select `Middle Button` on the canvas and move it around.
- Place two fingers on your touchpad and slide.

Don't worry about workflow execution and activation for now; we'll explain these concepts later on in the course.

## Nodes [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#nodes "Permanent link")

You can think of nodes as building blocks that serve different functions that, when put together, make up a functioning machine: an automated workflow.

Node

A node is an individual step in your workflow: one that either (a) loads, (b) processes, or (c) sends data.

Based on their function, n8n classifies nodes into four types:

- **App** or **Action Nodes** add, remove, and edit data; request and send external data; and trigger events in other systems. Refer to the [Action nodes library](https://docs.n8n.io/integrations/builtin/app-nodes/) for a full list of these nodes.
- **Trigger Nodes** start a workflow and supply the initial data. Refer to the [Trigger nodes library](https://docs.n8n.io/integrations/builtin/trigger-nodes/) for a list of trigger nodes.
- **Core Nodes** can be trigger or app nodes. Whereas most nodes connect to a specific external service, core nodes provide functionality such as logic, scheduling, or generic API calls. Refer to the [Core Nodes library](https://docs.n8n.io/integrations/builtin/core-nodes/) for a full list of core nodes.
- **Cluster Nodes** are node groups that work together to provide functionality in a workflow, primarily for AI workflows. Refer to [Cluster nodes](https://docs.n8n.io/integrations/builtin/cluster-nodes/) for more information.

Learn more

Refer to [Node types](https://docs.n8n.io/integrations/builtin/node-types/) for a more detailed explanation of all node types.

### Finding nodes [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#finding-nodes "Permanent link")

You can find all available nodes in the **nodes panel** on the right side of the Editor UI. There are three ways in which you can open the nodes panel:

- Click the **+** icon in the top right corner of the canvas.
- Click the **+** icon on the right side of an existing node on the canvas (the node to which you want to add another one).
- Click the `Tab` key on your keyboard.

[![Nodes panel](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-node-menu-drilldown.gif)](https://docs.n8n.io/_images/courses/level-one/chapter-one/l1-c1-node-menu-drilldown.gif) _Nodes panel_

In the nodes panel, notice that when adding your first node, you will see the different trigger node categories. After you have added your trigger node, you'll see that the nodes panel changes to show Advanced AI, Actions in an App, Data transformation, Flow, Core, and Human in the loop nodes.

If you want to find a specific node, use the search input at the top of the nodes panel.

### Adding nodes [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#adding-nodes "Permanent link")

There are two ways to add nodes to your canvas:

- Select the node you want in the nodes panel. The new node will automatically connect to the selected node on the canvas.
- Drag and drop the node from the nodes panel to the canvas.

### Node buttons [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#node-buttons "Permanent link")

If you hover on a node, you'll notice that three icons appear on top:

- Execute the node (Play icon)
- Deactivate/Activate the node (Power icon)
- Delete the node (Trash icon)

There will also be an ellipsis icon, which opens a context menu containing other [node options](https://docs.n8n.io/workflows/components/nodes/#node-controls).

Moving a workflow

To move a workflow around the canvas, select all nodes with your mouse or `Ctrl` + `A`, select and hold on a node, then drag it to any point you want on the canvas.

## Summary [\#](https://docs.n8n.io/courses/level-one/chapter-1/\#summary "Permanent link")

In this lesson you learned how to navigate the Editor UI, what the icons mean, how to access the left-side and node panels, and how to add nodes to the canvas.

In the next lesson, you will build a mini-workflow to put into practice what you've learned so far.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top