---
url: "https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.2/"
title: "Inserting data into airtable | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.2/#2-inserting-data-into-airtable)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-5/chapter-5.2.md "Edit this page")

# 2\. Inserting data into Airtable [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.2/\#2-inserting-data-into-airtable "Permanent link")

In this step of the workflow, you will learn how to insert the data received from the HTTP Request node into Airtable using the [Airtable node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/).

Spreadsheet nodes

You can replace the Airtable node with another spreadsheet app/service. For example, n8n also has a node for [**Google Sheets**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/).

After this step, your workflow should look like this:

[View workflow file](https://docs.n8n.io/_workflows//courses/level-one/chapter-5/chapter-5.2.json)

## Configure your table [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.2/\#configure-your-table "Permanent link")

If we're going to insert data into Airtable, we first need to set up a table there. To do this:

1. [Create an Airtable account](https://airtable.com/signup).
2. In your Airtable workspace add a new base from scratch and name it, for example, _beginner course_.


[![Create an Airtable base](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-2-create-airtable-base.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-2-create-airtable-base.png) _Create an Airtable base_

3. In the beginner course base, by default, you have a table called **Table 1** with four fields: `Name`, `Notes`, `Assignee`, and `Status`. These fields aren't relevant for us since they aren't in our "orders" data set. This brings us to the next point: the names of the fields in Airtable have to match the names of the columns in the node result. Prepare the table by doing the following:


   - Rename the table from **Table 1** to **orders** to make it easier to identify.
   - Delete the 3 blank records created by default.
   - Delete the `Notes`, `Assignee`, and `Status` fields.
   - Edit the `Name` field (the primary field) to read `orderID`, with the **Number** field type.
   - Add the rest of the fields, and their field types, using the table below as a reference:

| Field name | Field type |
| --- | --- |
| `orderID` | Number |
| `customerID` | Number |
| `employeeName` | Single line text |
| `orderPrice` | Number |
| `orderStatus` | Single line text |

Now your table should look like this:

[![Orders table in Airtable](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-2-orders-table.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-2-orders-table.png) _Orders table in Airtable_

Now that the table is ready, let's return to the workflow in the n8n Editor UI.

## Add an Airtable node to the HTTP Request node [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.2/\#add-an-airtable-node-to-the-http-request-node "Permanent link")

Add an Airtable node connected to the HTTP Request node.

Remember

You can add a node connected to an existing node by selecting the **+** icon next to the existing node.

In the node panel:

1. Search for Airtable.
2. Select **Create a record** from the **Record Actions** search results.

This will add the Airtable node to your canvas and open the node details window.

In the Airtable node window, configure the following parameters:

- **Credential to connect with**:
  - Select **Create new credential**.
  - Keep the default option **Connect using: Access Token** selected.
  - **Access token**: Follow the instructions from the [Airtable credential](https://docs.n8n.io/integrations/builtin/credentials/airtable/) page to create your token. Use the recommended scopes and add access to your beginners course base. Save the credential and close the Credential window when you're finished.
- **Resource**: Record.
- **Operation**: Create. This operation will create new records in the table.
- **Base**: You can pick your base from a list (for example, beginner course).
- **Table**: orders.
- **Mapping Column Mode**: Map automatically. In this mode, the incoming data fields must have the same as the columns in Airtable.

## Test the Airtable node [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.2/\#test-the-airtable-node "Permanent link")

Once you've finished configuring the Airtable node, execute it by selecting **Execute step**. This might take a moment to process, but you can follow the progress by viewing the base in Airtable.

Your results should look like this:

[![Airtable node results](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-2-airtable-node.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-2-airtable-node.png) _Airtable node results_

All 30 data records will now appear in the orders table in Airtable:

[![Imported records in the orders table](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-2-airtable-records.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-2-airtable-records.png) _Imported records in the orders table_

## What's next? [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.2/\#whats-next "Permanent link")

**Nathan 🙋**: Wow, this automation is already so useful! But this inserts all collected data from the HTTP Request node into Airtable. Remember that I actually need to insert only processing orders in the table and calculate the price of booked orders?

**You 👩‍🔧**: Sure, no problem. As a next step, I'll use a new node to filter the orders based on their status.