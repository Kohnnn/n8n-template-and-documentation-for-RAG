---
url: "https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.5/"
title: "Calculating booked orders | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.5/#5-calculating-booked-orders)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-one/chapter-5/chapter-5.5.md "Edit this page")

# 5\. Calculating Booked Orders [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.5/\#5-calculating-booked-orders "Permanent link")

In this step of the workflow you will learn how n8n structures data and how to add custom JavaScript code to perform calculations using the Code node. After this step, your workflow should look like this:

[View workflow file](https://docs.n8n.io/_workflows//courses/level-one/chapter-5/chapter-5.5.json)

The next step in Nathan's workflow is to calculate two values from the booked orders:

- The total number of booked orders
- The total value of all booked orders

To calculate data and add more functionality to your workflows you can use the Code node, which lets you write custom JavaScript code.

## About the Code node [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.5/\#about-the-code-node "Permanent link")

Code node modes

The Code node has two operational **modes**, depending on how you want to process items:

- **Run Once for All Items** allows you to write code to process all input items at once, as a group.
- **Run Once for Each Item** executes your code once for each input item.

Learn more about how to use the [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code/).

In n8n, the data that's passed between nodes is an array of objects with the following JSON structure:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>``` | ```<br>[<br>    {<br>   	 "json": { <br>   		 "apple": "beets",<br>   		 "carrot": {<br>   			 "dill": 1<br>   		 }<br>   	 },<br>   	 "binary": { <br>   		 "apple-picture": { <br>   			 "data": "....", <br>   			 "mimeType": "image/png", <br>   			 "fileExtension": "png", <br>   			 "fileName": "example.png", <br>   		 }<br>   	 }<br>    },<br>    ...<br>]<br>``` |

You can learn more about the expected format on the [n8n data structure](https://docs.n8n.io/data/data-structure/) page.

## Configure the Code node [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.5/\#configure-the-code-node "Permanent link")

Now let's see how to accomplish Nathan's task using the Code node.

In your workflow, add a **Code node** connected to the `false` branch of the **If node**.

With the Code node window open, configure these parameters:

- **Mode**: Select **Run Once for All Items**.
- **Language**: Select **JavaScript**.



Using Python in code nodes



While we use JavaScript below, you can also use Python in the Code node. To learn more, refer to the [Code node](https://docs.n8n.io/code/code-node/) documentation.

- Copy the Code below and paste it into the **Code** box to replace the existing code:



|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>let items = $input.all();<br>let totalBooked = items.length;<br>let bookedSum = 0;<br>for (let i=0; i < items.length; i++) {<br>  bookedSum = bookedSum + items[i].json.orderPrice;<br>}<br>return [{ json: {totalBooked, bookedSum} }];<br>``` |


Notice the format in which we return the results of the calculation:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>return [{ json: {totalBooked, bookedSum} }]<br>``` |

Data structure error

If you don't use the correct data structure, you will get an error message: `Error: Always an Array of items has to be returned!`

Now select **Execute step** and you should see the following results:

[![Code node output](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-5-code-node.png)](https://docs.n8n.io/_images/courses/level-one/chapter-five/l1-c5-5-5-code-node.png) _Code node output_

## What's next? [\#](https://docs.n8n.io/courses/level-one/chapter-5/chapter-5.5/\#whats-next "Permanent link")

**Nathan 🙋**: Wow, the Code node is powerful! This means that if I have some basic JavaScript skills I can power up my workflows.

**You 👩‍🔧**: Yes! You can progress from no-code to low-code!

**Nathan 🙋**: Now, how do I send the calculations for the booked orders to my team's Discord channel?

**You 👩‍🔧**: There's an n8n node for that. I'll set it up in the next step.