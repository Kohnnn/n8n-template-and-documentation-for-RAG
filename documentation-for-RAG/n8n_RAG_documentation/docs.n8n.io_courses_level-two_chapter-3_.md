---
url: "https://docs.n8n.io/courses/level-two/chapter-3/"
title: "Merging and splitting data | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-two/chapter-3/#merging-and-splitting-data)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-two/chapter-3.md "Edit this page")

# Merging and splitting data [\#](https://docs.n8n.io/courses/level-two/chapter-3/\#merging-and-splitting-data "Permanent link")

In this chapter, you will learn how to merge and split data, and in what cases it might be useful to perform these operations.

## Merging data [\#](https://docs.n8n.io/courses/level-two/chapter-3/\#merging-data "Permanent link")

In some cases, you might need to merge (combine) and process data from different sources.

Merging data can involve:

- Creating one data set from multiple sources.
- Synchronizing data between multiple systems. This could include removing duplicate data or updating data in one system when it changes in another.

One-way vs. two-way sync

In a one-way sync, data is synchronized in one direction. One system serves as the single source of truth. When information changes in that main system, it automatically changes in the secondary system; but if information changes in the secondary system, the changes aren't reflected in the main system.

In a two-way sync, data is synchronized in both directions (between both systems). When information changes in either of the two systems, it automatically changes in the other one as well.

[This blog tutorial](https://blog.n8n.io/how-to-sync-data-between-two-systems/) explains how to sync data one-way and two-way between two CRMs.

In n8n, you can merge data from two different nodes using the [Merge node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/), which provides several merging options:

- [Append](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/#append)
- [Combine](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/#combine)
  - [Merge by Fields](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/#combine-by-matching-fields): requires input fields to match on
  - [Merge by Position](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/#combine-by-position)
  - [Combine all possible combinations](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/#combine-by-all-possible-combinations)
- [Choose Branch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge/#choose-branch)

Notice that Combine > Merge by Fields requires you enter input fields to match on. These fields should contain identical values between the data sources so n8n can properly match data together. In the **Merge node**, they're called `Input 1 Field` and `Input 2 Field`.

[![Property Input fields in the Merge node](https://docs.n8n.io/_images/courses/level-two/chapter-three/explanation_mergepropertyinput.png)](https://docs.n8n.io/_images/courses/level-two/chapter-three/explanation_mergepropertyinput.png) _Property Input fields in the Merge node_

Property Input in dot notation

If you want to reference nested values in the **Merge node** parameters `Input 1 Field` and `Input 2 Field`, you need to enter the property key in dot-notation format (as text, not as an expression).

Note

You can also find the **Merge node** under the alias Join. This might be more intuitive if you're familiar with SQL joins.

### Merge Exercise [\#](https://docs.n8n.io/courses/level-two/chapter-3/\#merge-exercise "Permanent link")

Build a workflow that merges data from the Customer Datastore node and Code node.

1. Add a **Merge node** that takes `Input 1` from a **Customer Datastore node** and `Input 2` from a **Code node**.
2. In the **Customer Datastore node**, run the operation **Get All People**.
3. In the **Code node**, create an array of two objects with three properties: `name`, `language`, and `country`, where the property `country` has two sub-properties `code` and `name`.
   - Fill out the values of these properties with the information of two characters from the Customer Database.
   - For example, Jay Gatsby's language is English and country name is United States.
4. In the **Merge node**, try out different merge options.

Show me the solution

The workflow for this exercise looks like this:

[![Workflow exercise for merging data](https://docs.n8n.io/_images/courses/level-two/chapter-three/exercise_merge.png)](https://docs.n8n.io/_images/courses/level-two/chapter-three/exercise_merge.png) _Workflow exercise for merging data_

If you merge data with the option **Keep Matches** using the name as the input fields to match, the result should look like this (note this example only contains Jay Gatsby; yours might look different depending on which characters you selected):

[![Output of Merge node with option to keep matches](https://docs.n8n.io/_images/courses/level-two/chapter-three/exercise_merge_kkm.png)](https://docs.n8n.io/_images/courses/level-two/chapter-three/exercise_merge_kkm.png) _Output of Merge node with option to keep matches_

To check the configuration of the nodes, you can copy the JSON workflow code below and paste it into your Editor UI:

|     |     |
| --- | --- |
| ```<br>  1<br>  2<br>  3<br>  4<br>  5<br>  6<br>  7<br>  8<br>  9<br> 10<br> 11<br> 12<br> 13<br> 14<br> 15<br> 16<br> 17<br> 18<br> 19<br> 20<br> 21<br> 22<br> 23<br> 24<br> 25<br> 26<br> 27<br> 28<br> 29<br> 30<br> 31<br> 32<br> 33<br> 34<br> 35<br> 36<br> 37<br> 38<br> 39<br> 40<br> 41<br> 42<br> 43<br> 44<br> 45<br> 46<br> 47<br> 48<br> 49<br> 50<br> 51<br> 52<br> 53<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>``` | ```<br>{<br>"meta": {<br>	"templateCredsSetupCompleted": true,<br>	"instanceId": "cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7"<br>},<br>"nodes": [<br>	{<br>	"parameters": {<br>		"mode": "combine",<br>		"mergeByFields": {<br>		"values": [<br>			{<br>			"field1": "name",<br>			"field2": "name"<br>			}<br>		]<br>		},<br>		"options": {}<br>	},<br>	"id": "578365f3-26dd-4fa6-9858-f0a5fdfc413b",<br>	"name": "Merge",<br>	"type": "n8n-nodes-base.merge",<br>	"typeVersion": 2.1,<br>	"position": [<br>		720,<br>		580<br>	]<br>	},<br>	{<br>	"parameters": {},<br>	"id": "71aa5aad-afdf-4f8a-bca0-34450eee8acc",<br>	"name": "When clicking \"Execute workflow\"",<br>	"type": "n8n-nodes-base.manualTrigger",<br>	"typeVersion": 1,<br>	"position": [<br>		260,<br>		560<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"operation": "getAllPeople"<br>	},<br>	"id": "497174fe-3cab-4160-8103-78b44efd038d",<br>	"name": "Customer Datastore (n8n training)",<br>	"type": "n8n-nodes-base.n8nTrainingCustomerDatastore",<br>	"typeVersion": 1,<br>	"position": [<br>		500,<br>		460<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"jsCode": "return [\n  {\n    'name': 'Jay Gatsby',\n    'language': 'English',\n    'country': {\n      'code': 'US',\n      'name': 'United States'\n    }\n    \n  }\n  \n];"<br>	},<br>	"id": "387e8a1e-e796-4f05-8e75-7ce25c786c5f",<br>	"name": "Code",<br>	"type": "n8n-nodes-base.code",<br>	"typeVersion": 2,<br>	"position": [<br>		500,<br>		720<br>	]<br>	}<br>],<br>"connections": {<br>	"When clicking \"Execute workflow\"": {<br>	"main": [<br>		[<br>		{<br>			"node": "Customer Datastore (n8n training)",<br>			"type": "main",<br>			"index": 0<br>		},<br>		{<br>			"node": "Code",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"Customer Datastore (n8n training)": {<br>	"main": [<br>		[<br>		{<br>			"node": "Merge",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"Code": {<br>	"main": [<br>		[<br>		{<br>			"node": "Merge",<br>			"type": "main",<br>			"index": 1<br>		}<br>		]<br>	]<br>	}<br>},<br>"pinData": {}<br>}<br>``` |

## Looping [\#](https://docs.n8n.io/courses/level-two/chapter-3/\#looping "Permanent link")

In some cases, you might need to perform the same operation on each element of an array or each data item (for example sending a message to every contact in your address book). In technical terms, you need to iterate through the data (with loops).

n8n generally handles this repetitive processing automatically, as the nodes run once for each item, so you don't need to build loops into your workflows.

However, there are some [exceptions of nodes and operations](https://docs.n8n.io/flow-logic/looping/#node-exceptions) that will require you to build a loop into your workflow.

To [create a loop in an n8n workflow](https://docs.n8n.io/flow-logic/looping/#using-loops-in-n8n), you need to connect the output of one node to the input of a previous node, and add an **If node** to check when to stop the loop.

## Splitting data in batches [\#](https://docs.n8n.io/courses/level-two/chapter-3/\#splitting-data-in-batches "Permanent link")

If you need to process large volumes of incoming data, execute the **Code node** multiple times, or avoid API rate limits, it's best to split the data into batches (groups) and process these batches.

For these processes, use the [**Loop Over Items node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches/). This node splits input data into a specified batch size and, with each iteration, returns a predefined amount of data.

Execution of Loop Over Items node

The **Loop Over Items node** stops executing after all the incoming items get divided into batches and passed on to the next node in the workflow, so it's not necessary to add an **If node** to stop the loop.

### Loop/Batch Exercise [\#](https://docs.n8n.io/courses/level-two/chapter-3/\#loopbatch-exercise "Permanent link")

Build a workflow that reads the RSS feed from Medium and dev.to. The workflow should consist of three nodes:

1. A **Code node** that returns the URLs of the RSS feeds of Medium ( `https://medium.com/feed/n8n-io`) and dev.to ( `https://dev.to/feed/n8n`).
2. A **Loop Over Items node** with `Batch Size: 1`, that takes in the inputs from the **Code node** and **RSS Read node** and iterates over the items.
3. An **RSS Read node** that gets the URL of the Medium RSS feed, passed as an expression: `{{ $json.url }}`.
   - The **RSS Read node** is one of the [exception nodes](https://docs.n8n.io/flow-logic/looping/#node-exceptions) which processes only the first item it receives, so the **Loop Over Items node** is necessary for iterating over multiple items.

Show me the solution

1. Add a **Code Node**. You can format the code in several ways, one way is:
   - Set **Mode** to `Run Once for All Items`.
   - Set **Language** to `JavaScript`.
   - Copy the code below and paste it into the JavaScript Code editor:



     |     |     |
     | --- | --- |
     | ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>``` | ```<br>let urls = [<br>	{<br>		json: {<br>		url: 'https://medium.com/feed/n8n-io'<br>		}<br>	},<br>	{<br>	json: {<br>		url: 'https://dev.to/feed/n8n'<br>		} <br>	}<br>]<br>return urls;<br>``` |
2. Add a **Loop Over Items node** connected to the **Code node**.
   - Set **Batch Size** to `1`.
3. The **Loop Over Items node** automatically adds a node called "Replace Me". Replace that node with an **RSS Read node**.
   - Set the **URL** to use the url from the Code Node: `{{ $json.url }}`.

The workflow for this exercise looks like this:

[![Workflow for getting RSS feeds from two blogs](https://docs.n8n.io/_images/courses/level-two/chapter-three/exercise_splitinbatches.png)](https://docs.n8n.io/_images/courses/level-two/chapter-three/exercise_splitinbatches.png) _Workflow for getting RSS feeds from two blogs_

To check the configuration of the nodes, you can copy the JSON workflow code below and paste it into your Editor UI:

|     |     |
| --- | --- |
| ```<br>  1<br>  2<br>  3<br>  4<br>  5<br>  6<br>  7<br>  8<br>  9<br> 10<br> 11<br> 12<br> 13<br> 14<br> 15<br> 16<br> 17<br> 18<br> 19<br> 20<br> 21<br> 22<br> 23<br> 24<br> 25<br> 26<br> 27<br> 28<br> 29<br> 30<br> 31<br> 32<br> 33<br> 34<br> 35<br> 36<br> 37<br> 38<br> 39<br> 40<br> 41<br> 42<br> 43<br> 44<br> 45<br> 46<br> 47<br> 48<br> 49<br> 50<br> 51<br> 52<br> 53<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>``` | ```<br>{<br>"meta": {<br>	"templateCredsSetupCompleted": true,<br>	"instanceId": "cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7"<br>},<br>"nodes": [<br>	{<br>	"parameters": {},<br>	"id": "ed8dc090-ae8c-4db6-a93b-0fa873015c25",<br>	"name": "When clicking \"Execute workflow\"",<br>	"type": "n8n-nodes-base.manualTrigger",<br>	"typeVersion": 1,<br>	"position": [<br>		460,<br>		460<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"jsCode": "let urls = [\n  {\n    json: {\n      url: 'https://medium.com/feed/n8n-io'\n    }\n  },\n  {\n   json: {\n     url: 'https://dev.to/feed/n8n'\n   } \n  }\n]\n\nreturn urls;"<br>	},<br>	"id": "1df2a9bf-f970-4e04-b906-92dbbc9e8d3a",<br>	"name": "Code",<br>	"type": "n8n-nodes-base.code",<br>	"typeVersion": 2,<br>	"position": [<br>		680,<br>		460<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"options": {}<br>	},<br>	"id": "3cce249a-0eab-42e2-90e3-dbdf3684e012",<br>	"name": "Loop Over Items",<br>	"type": "n8n-nodes-base.splitInBatches",<br>	"typeVersion": 3,<br>	"position": [<br>		900,<br>		460<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"url": "={{ $json.url }}",<br>		"options": {}<br>	},<br>	"id": "50e1c1dc-9a5d-42d3-b7c0-accc31636aa6",<br>	"name": "RSS Read",<br>	"type": "n8n-nodes-base.rssFeedRead",<br>	"typeVersion": 1,<br>	"position": [<br>		1120,<br>		460<br>	]<br>	}<br>],<br>"connections": {<br>	"When clicking \"Execute workflow\"": {<br>	"main": [<br>		[<br>		{<br>			"node": "Code",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"Code": {<br>	"main": [<br>		[<br>		{<br>			"node": "Loop Over Items",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"Loop Over Items": {<br>	"main": [<br>		null,<br>		[<br>		{<br>			"node": "RSS Read",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"RSS Read": {<br>	"main": [<br>		[<br>		{<br>			"node": "Loop Over Items",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	}<br>},<br>"pinData": {}<br>}<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top