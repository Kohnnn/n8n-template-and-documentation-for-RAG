---
url: "https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.3/"
title: "Filtering orders | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.3/#3-filtering-orders)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-5/chapter-5.3.md "Edit this page")

# 3\. Filtering Orders [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.3/\#3-filtering-orders "Permanent link")

In this step of the workflow, you will learn how to filter data using conditional logic and how to use expressions in nodes using the [If node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/).

After this step, your workflow should look like this:

[View workflow file](https://docs.n8n.io/_workflows//courses/level-one/chapter-5/chapter-5.3.json)

To insert only processing orders into Airtable we need to filter our data by `orderStatus`. Basically, we want to tell the program that _if_ the `orderStatus` is processing, _then_ insert all records with this status into Airtable; _else_, for example, if the `orderStatus` isn't _processing_, calculate the sum of all orders with the other `orderStatus` ( `booked`).

This if-then-else command is conditional logic. In n8n workflows, you can add conditional logic with the [If node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/), which splits a workflow conditionally based on comparison operations.

If vs. Switch

If you need to filter data on more than boolean values (true and false), use the [Switch node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch/). The Switch node is similar to the If node, but supports multiple output connectors.

## Add If node before the Airtable node [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.3/\#add-if-node-before-the-airtable-node "Permanent link")

First, let's add an If node between the connection from the HTTP Request node to the Airtable node:

1. Hover over the arrow connection the **HTTP Request** node and the **Airtable** node.
2. Select the **+** sign between the HTTP Request node and the Airtable node.

## Configure the If node [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.3/\#configure-the-if-node "Permanent link")

Selecting the plus removes the connection to the Airtable node to the HTTP request. Now, let's add an If node connected to the HTTP Request node:

1. Search for the If node.
2. Select it when it appears in the search.

For the If node, we'll use an expression.

Expressions

An [expression](https://docs.n8n.io/glossary/#expression-n8n) is a string of characters and symbols in a programming language that can be evaluated to get a value, often according to its input. In n8n workflows, you can use expressions in a node to refer to another node for input data. In our example, the If node references the data output by the HTTP Request node.

In the If node window, configure the parameters:

- Set the `value1` placeholder to `{{ $json.orderStatus }}` with the following steps:
1. Hover over the value1 field.
2. Select the **Expression** tab on the right side of the `value1` field.
3. Next, open the expression editor by selecting the link icon:
     [![Opening the Expression Editor](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-3-if-node-open-editor.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-3-if-node-open-editor.png) _Opening the Expression Editor_
4. Use the left-side panel to select **HTTP Request** \> **orderStatus** and drag it into the **Expression** field in the center of the window.
     [![Expression Editor in the IF node](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-3-if-node-expression-editor.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-3-if-node-expression-editor.png) _Expression Editor in the If node_
5. Once you add the expression, close the **Edit Expression** dialog.
- **Operation**: Select **String** \> **is equal to**

- Set the `value2` placeholder to `processing`.

Data Type

Make sure to select the correct data type (boolean, date & time, number, or string) when you select the **Operation**.

Select **Execute step** to test the If node.

Your results should look like this:

[![If node output](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-3-if-node-output.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-3-if-node-output.png) _If node output_

Note that the orders with a `processing` order status should show for the **True Branch** output, while the orders with a `booked` order status should show in the **False Branch** output.

Close the If node detail view when you're finished.

## Insert data into Airtable [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.3/\#insert-data-into-airtable "Permanent link")

Next, we want to insert this data into Airtable. Remember what Nathan said at the end of the [Inserting data into Airtable](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.2/) lesson?

> I actually need to insert only processing orders in the table...

Since Nathan only needs the `processing` orders in the table, we'll connect the Airtable node to the If node's `true` connector.

In this case, since the Airtable node is already on our canvas, select the **If node** `true` connector and drag it to the Airtable node.

It's a good idea at this point to retest the Airtable node. Before you do, open your table in Airtable and delete all existing rows. Then open the Airtable node window in n8n and select **Execute step**.

Review your data in Airtable to be sure your workflow only added the correct orders (those with `orderStatus` of `processing`). There should be 14 records now instead of 30.

At this stage, your workflow should look like this:

[View workflow file](https://docs.n8n.io/_workflows//courses/level-one/chapter-5/chapter-5.3.json)

## What's next? [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.3/\#whats-next "Permanent link")

**Nathan 🙋**: This If node is so useful for filtering data! Now I have all the information about processing orders. I actually only need the `employeeName` and `orderID`, but I guess I can keep all the other fields just in case.

**You 👩‍🔧**: Actually, I wouldn't recommend doing that. Inserting more data requires more computational power, the data transfer is slower and takes longer, and takes up more storage resources in your table. In this particular case, 14 records with 5 fields might not seem like it'd make a significant difference, but if your business grows to thousands of records and dozens of fields, things add up and even one extra column can affect performance.

**Nathan 🙋**: Oh, that's good to know. Can you select only two fields from the processing orders?

**You 👩‍🔧**: Sure, I'll do that in the next step.