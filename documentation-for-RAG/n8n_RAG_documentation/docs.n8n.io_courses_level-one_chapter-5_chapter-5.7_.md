---
url: "https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.7/"
title: "Scheduling the workflow | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.7/#7-scheduling-the-workflow)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-5/chapter-5.7.md "Edit this page")

# 7\. Scheduling the Workflow [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.7/\#7-scheduling-the-workflow "Permanent link")

In this step of the workflow, you will learn how to schedule your workflow so that it runs automatically at a set time/interval using the Schedule Trigger node. After this step, your workflow should look like this:

[View workflow file](https://docs.n8n.io/_workflows//courses/level-one/finished.json)

The workflow you've built so far executes only when you click on **Test Workflow**. But Nathan needs it to run automatically every Monday morning. You can do this with the [Schedule Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/), which allows you to schedule workflows to run periodically at fixed dates, times, or intervals.

To achieve this, we'll remove the Manual Trigger node we started with and replace it with a Schedule Trigger node instead.

## Remove the Manual Trigger node [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.7/\#remove-the-manual-trigger-node "Permanent link")

First, let's remove the Manual Trigger node:

1. Select the Manual Trigger node connected to your HTTP Request node.
2. Select the trash can icon to delete.

This removes the Manual Trigger node and you'll see an "Add first step" option.

## Add the Schedule Trigger node [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.7/\#add-the-schedule-trigger-node "Permanent link")

1. Open the nodes panel and search for **Schedule Trigger**.
2. Select it when it appears in the search results.

In the Schedule Trigger node window, configure these parameters:

- **Trigger Interval**: Select **Weeks**.
- **Weeks Between Triggers**: Enter `1`.
- **Trigger on weekdays**: Select **Monday** (and remove **Sunday** if added by default).
- **Trigger at Hour**: Select **9am**.
- **Trigger at Minute**: Enter `0`.

Your Schedule Trigger node should look like this:

[![Schedule Trigger Node](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-7-schedule-trigger-node.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-7-schedule-trigger-node.png) _Schedule Trigger Node_

Keep in mind

To ensure accurate scheduling with the Schedule Trigger node, be sure to set the correct timezone for your [n8n instance](https://docs.n8n.io/manage-cloud/set-cloud-timezone/) or the [workflow's settings](https://docs.n8n.io/workflows/settings/). The Schedule Trigger node will use the workflow's timezone if it's set; it will fall back to the n8n instance's timezone if it's not.

## Connect the Schedule Trigger node [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.7/\#connect-the-schedule-trigger-node "Permanent link")

Return to the canvas and connect your Schedule Trigger node to the HTTP Request node by dragging the arrow from it to the HTTP Request node.

Your full workflow should look like this:

[View workflow file](https://docs.n8n.io/_workflows//courses/level-one/finished.json)

## What's next? [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.7/\#whats-next "Permanent link")

**You 👩‍🔧**: That was it for the workflow! I've added and configured all necessary nodes. Now every time you click on **Execute workflow**, n8n will execute all the nodes: getting, filtering, calculating, and transferring the sales data.

**Nathan 🙋**: This is just what I needed! My workflow will run automatically every Monday morning, correct?

**You 👩‍🔧**: Not so fast. To do that, you need to activate your workflow. I'll do this in the next step and show you how to interpret the execution log.