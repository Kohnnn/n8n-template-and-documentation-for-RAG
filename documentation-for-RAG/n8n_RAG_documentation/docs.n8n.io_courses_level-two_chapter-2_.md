---
url: "https://docs.n8n.io/courses/level-two/chapter-2/"
title: "Processing different data types | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/courses/level-two/chapter-2/#processing-different-data-types)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/courses/level-two/chapter-2.md "Edit this page")

# Processing different data types [\#](https://docs.n8n.io/courses/level-two/chapter-2/\#processing-different-data-types "Permanent link")

In this chapter, you will learn how to process different types of data using [n8n core nodes](https://docs.n8n.io/workflows/components/nodes/).

## HTML and XML data [\#](https://docs.n8n.io/courses/level-two/chapter-2/\#html-and-xml-data "Permanent link")

You're most likely familiar with HTML and XML.

HTML vs. XML

HTML is a markup language used to describe the structure and semantics of a web page. XML looks similar to HTML, but the tag names are different, as they describe the kind of data they hold.

If you need to process HTML or XML data in your n8n workflows, use the [**HTML node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html/) or the [**XML node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.xml/).

Use the **HTML node** to extract HTML content of a webpage by referencing CSS selectors. This is useful if you want to collect structured information from a website (web-scraping).

### HTML Exercise [\#](https://docs.n8n.io/courses/level-two/chapter-2/\#html-exercise "Permanent link")

Let's get the title of the latest n8n blog post:

1. Use the **HTTP Request node** to make a GET request to the URL `https://blog.n8n.io/` (this endpoint requires no authentication).
2. Connect an **HTML node** and configure it to extract the title of the first blog post on the page.
   - Hint: If you're not familiar with CSS selectors or reading HTML, the CSS selector `.post .item-title  a` should help!

Show me the solution

1. Configure the HTTP Request node with the following parameters:
   - **Authentication**: None
   - **Request Method**: GET
   - **URL**: https://blog.n8n.io/
     The result should look like this:

[![Result of HTTP Request node](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_html_httprequestnode.png)](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_html_httprequestnode.png) _Result of HTTP Request node_

2. Connect an **HTML node** to the **HTTP Request node** and configure the former's parameters:
   - **Operation**: Extract HTML Content
   - **Source Data**: JSON
   - **JSON Property**: data
   - **Extraction Values**:
     - **Key**: title
     - **CSS Selector**: `.post .item-title  a`
     - **Return Value**: HTML

You can add more values to extract more data.

The result should look like this:

[![Result of HTML Extract node](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_html_htmlextractnode.png)](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_html_htmlextractnode.png) _Result of HTML Extract node_

Use the **XML node** to convert XML to JSON and JSON to XML. This operation is useful if you work with different web services that use either XML or JSON and need to get and submit data between them in the two formats.

### XML Exercise [\#](https://docs.n8n.io/courses/level-two/chapter-2/\#xml-exercise "Permanent link")

In the [final exercise of Chapter 1](https://docs.n8n.io/courses/level-two/chapter-1/#exercise_2), you used an **HTTP Request node** to make a request to the PokéAPI. In this exercise, we'll return to that same API but we'll convert the output to XML:

1. Add an **HTTP Request node** that makes the same request to the PokéAPI at `https://pokeapi.co/api/v2/pokemon`.
2. Use the XML node to convert the JSON output to XML.

Show me the solution

1. To get the pokemon from the PokéAPI, execute the **HTTP Request node** with the following parameters:
   - **Authentication**: None
   - **Request Method**: GET
   - **URL**: https://pokeapi.co/api/v2/pokemon
2. Connect an **XML node** to it with the following parameters:
   - **Mode**: JSON to XML
   - **Property name**: data

The result should look like this:

[![Table view of XML Node (JSON to XML)](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_html_xmlnode_table.png)](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_html_xmlnode_table.png) _XML node (JSON to XML) – Table View_

To transform data the other way around, select the mode **XML to JSON**.

## Date, time, and interval data [\#](https://docs.n8n.io/courses/level-two/chapter-2/\#date-time-and-interval-data "Permanent link")

Date and time data types include `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, and `YEAR`. The dates and times can be passed in different formats, for example:

- `DATE`: March 29 2022, 29-03-2022, 2022/03/29
- `TIME`: 08:30:00, 8:30, 20:30
- `DATETIME`: 2022/03/29 08:30:00
- `TIMESTAMP`: 1616108400 (Unix timestamp), 1616108400000 (Unix ms timestamp)
- `YEAR`: 2022, 22

There are a few ways you can work with dates and times:

- Use the [**Date & Time node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datetime/) to convert date and time data to different formats and calculate dates.
- Use [**Schedule Trigger node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/) to schedule workflows to run at a specific time, interval, or duration.

Sometimes, you might need to pause the workflow execution. This might be necessary if you know that a service doesn't process the data instantly or it's slow to return all the results. In these cases, you don't want n8n to pass incomplete data to the next node.

If you run into situations like this, use the [**Wait node**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait/) after the node that you want to delay. The **Wait node** pauses the workflow execution and will resume execution:

- At a specific time.
- After a specified time interval.
- On a webhook call.

### Date Exercise [\#](https://docs.n8n.io/courses/level-two/chapter-2/\#date-exercise "Permanent link")

Build a workflow that adds five days to an input date from the Customer Datastore node that you used before. Then, if the calculated date occurred after 1959, the workflow waits 1 minute before [setting](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/) the calculated date as a value. The workflow should be triggered every 30 minutes.

To begin:

1. Add the **Customer Datastore (n8n training) node** with the **Get All People** action selected. Return All.
2. Add the **Date & Time node** to Round Up the created Date from the datastore to End of Month. Output this to field new-date. Include all input fields.
3. Add the **If node** to check if that new rounded date is after `1960-01-01 00:00:00`.
4. Add the **Wait node** to the True output of that node and set it to wait for one minute.
5. Add the **Edit Fields (Set) node** to set a new field called outputValue to a String containing new-date. Include all input fields.
6. Add the **Schedule Trigger node** at the beginning of the workflow to trigger it every 30 minutes. (You can keep the [Manual Trigger node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger/) for testing!)

Show me the solution

1. Add the **Customer Datastore (n8n training) node** with the **Get All People** action selected.
   - Select the option to **Return All**.
2. Add a **Date & Time node** connected to the Customer Datastore node. Select the option to **Round a Date**.
   - Add the `created` date as the **Date** to round.
   - Select `Round Up` as the **Mode** and `End of Month` as the **To**.
   - Set the **Output Field Name** as `new-date`.
   - In **Options**, select **Add Option** and use the control to **Include Input Fields**
3. Add an **If node** connected to the **Date & Time node**.
   - Add the new-date field as the first part of the condition.
   - Set the comparison to **Date &Time > is after**
   - Add `1960-01-01 00:00:00` as the second part of the expression. (This should produce 3 items in the True Branch and 2 items in the False Branch)
4. Add a **Wait node** to the True output of the **If node**.
   - Set **Resume** to `After Time interval`.
   - Set **Wait Amount** to `1.00`.
   - Set **Wait Unit** to `Minutes`.
5. Add an **Edit Fields (Set) node** to the **Wait node**.
   - Use either JSON or Manual Mapping **Mode**.
   - Set a new field called `outputValue` to be the value of the new-date field.
   - Select the option to **Include Other Input Fields** and include **All** fields.
6. Add a **Schedule Trigger node** at the beginning of the workflow.
   - Set the **Trigger Interval** to use `Minutes`.
   - Set the **Minutes Between Triggers** to 30.
   - To test your schedule, be sure to activate the workflow.
   - Be sure to connect this node to the **Customer Datastore (n8n training) node** you began with!

The workflow should look like this:

[![Workflow for transforming dates](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_datetime.png)](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_datetime.png) _Workflow for transforming dates_

To check the configuration of each node, you can copy the JSON code of this workflow and either paste it into the Editor UI or save it as a file and import from file into a new workflow. See [Export and import workflows](https://docs.n8n.io/workflows/export-import/) for more information.

|     |     |
| --- | --- |
| ```<br>  1<br>  2<br>  3<br>  4<br>  5<br>  6<br>  7<br>  8<br>  9<br> 10<br> 11<br> 12<br> 13<br> 14<br> 15<br> 16<br> 17<br> 18<br> 19<br> 20<br> 21<br> 22<br> 23<br> 24<br> 25<br> 26<br> 27<br> 28<br> 29<br> 30<br> 31<br> 32<br> 33<br> 34<br> 35<br> 36<br> 37<br> 38<br> 39<br> 40<br> 41<br> 42<br> 43<br> 44<br> 45<br> 46<br> 47<br> 48<br> 49<br> 50<br> 51<br> 52<br> 53<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>208<br>209<br>``` | ```<br>{<br>"name": "Course 2, Ch 2, Date exercise",<br>"nodes": [<br>	{<br>	"parameters": {},<br>	"id": "6bf64d5c-4b00-43cf-8439-3cbf5e5f203b",<br>	"name": "When clicking \"Execute workflow\"",<br>	"type": "n8n-nodes-base.manualTrigger",<br>	"typeVersion": 1,<br>	"position": [<br>		620,<br>		280<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"operation": "getAllPeople",<br>		"returnAll": true<br>	},<br>	"id": "a08a8157-99ee-4d50-8fe4-b6d7e16e858e",<br>	"name": "Customer Datastore (n8n training)",<br>	"type": "n8n-nodes-base.n8nTrainingCustomerDatastore",<br>	"typeVersion": 1,<br>	"position": [<br>		840,<br>		360<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"operation": "roundDate",<br>		"date": "={{ $json.created }}",<br>		"mode": "roundUp",<br>		"outputFieldName": "new-date",<br>		"options": {<br>		"includeInputFields": true<br>		}<br>	},<br>	"id": "f66a4356-2584-44b6-a4e9-1e3b5de53e71",<br>	"name": "Date & Time",<br>	"type": "n8n-nodes-base.dateTime",<br>	"typeVersion": 2,<br>	"position": [<br>		1080,<br>		360<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"conditions": {<br>		"options": {<br>			"caseSensitive": true,<br>			"leftValue": "",<br>			"typeValidation": "strict"<br>		},<br>		"conditions": [<br>			{<br>			"id": "7c82823a-e603-4166-8866-493f643ba354",<br>			"leftValue": "={{ $json['new-date'] }}",<br>			"rightValue": "1960-01-01T00:00:00",<br>			"operator": {<br>				"type": "dateTime",<br>				"operation": "after"<br>			}<br>			}<br>		],<br>		"combinator": "and"<br>		},<br>		"options": {}<br>	},<br>	"id": "cea39877-6183-4ea0-9400-e80523636912",<br>	"name": "If",<br>	"type": "n8n-nodes-base.if",<br>	"typeVersion": 2,<br>	"position": [<br>		1280,<br>		360<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"amount": 1,<br>		"unit": "minutes"<br>	},<br>	"id": "5aa860b7-c73c-4df0-ad63-215850166f13",<br>	"name": "Wait",<br>	"type": "n8n-nodes-base.wait",<br>	"typeVersion": 1.1,<br>	"position": [<br>		1480,<br>		260<br>	],<br>	"webhookId": "be78732e-787d-463e-9210-2c7e8239761e"<br>	},<br>	{<br>	"parameters": {<br>		"assignments": {<br>		"assignments": [<br>			{<br>			"id": "e058832a-2461-4c6d-b584-043ecc036427",<br>			"name": "outputValue",<br>			"value": "={{ $json['new-date'] }}",<br>			"type": "string"<br>			}<br>		]<br>		},<br>		"includeOtherFields": true,<br>		"options": {}<br>	},<br>	"id": "be034e9e-3cf1-4264-9d15-b6760ce28f91",<br>	"name": "Edit Fields",<br>	"type": "n8n-nodes-base.set",<br>	"typeVersion": 3.3,<br>	"position": [<br>		1700,<br>		260<br>	]<br>	},<br>	{<br>	"parameters": {<br>		"rule": {<br>		"interval": [<br>			{<br>			"field": "minutes",<br>			"minutesInterval": 30<br>			}<br>		]<br>		}<br>	},<br>	"id": "6e8e4308-d0e0-4d0d-bc29-5131b57cf061",<br>	"name": "Schedule Trigger",<br>	"type": "n8n-nodes-base.scheduleTrigger",<br>	"typeVersion": 1.1,<br>	"position": [<br>		620,<br>		480<br>	]<br>	}<br>],<br>"pinData": {},<br>"connections": {<br>	"When clicking \"Execute workflow\"": {<br>	"main": [<br>		[<br>		{<br>			"node": "Customer Datastore (n8n training)",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"Customer Datastore (n8n training)": {<br>	"main": [<br>		[<br>		{<br>			"node": "Date & Time",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"Date & Time": {<br>	"main": [<br>		[<br>		{<br>			"node": "If",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"If": {<br>	"main": [<br>		[<br>		{<br>			"node": "Wait",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"Wait": {<br>	"main": [<br>		[<br>		{<br>			"node": "Edit Fields",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	},<br>	"Schedule Trigger": {<br>	"main": [<br>		[<br>		{<br>			"node": "Customer Datastore (n8n training)",<br>			"type": "main",<br>			"index": 0<br>		}<br>		]<br>	]<br>	}<br>}<br>}<br>``` |

## Binary data [\#](https://docs.n8n.io/courses/level-two/chapter-2/\#binary-data "Permanent link")

Up to now, you have mainly worked with text data. But what if you want to process data that's not text, like images or PDF files? These types of files are represented in the binary numeral system, so they're considered binary data. In this form, binary data doesn't offer you useful information, so you'll need to convert it into a readable form.

In n8n, you can process binary data with the following nodes:

- [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to request and send files from/to web resources and APIs.
- [Read/Write Files from Disk](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile/) to read and write files from/to the machine where n8n is running.
- [Convert to File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile/) to take input data and output it as a file.
- [Extract From File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile/) to get data from a binary format and convert it to JSON.

Reading and writing files is only available on self-hosted n8n

Reading and writing files to disk isn't available on n8n Cloud. You'll read and write to the machine where you installed n8n. If you run n8n in Docker, your command runs in the n8n container and not the Docker host. The Read/Write Files From Disk node looks for files relative to the n8n install path. n8n recommends using absolute file paths to prevent any errors.

To read or write a binary file, you need to write the path (location) of the file in the node's `File(s) Selector` parameter (for the Read operation) or in the node's `File Path and Name` parameter (for the Write operation).

Naming the right path

The file path looks slightly different depending on how you are running n8n:

- npm: `~/my_file.json`
- n8n cloud / Docker: `/tmp/my_file.json`

### Binary Exercise 1 [\#](https://docs.n8n.io/courses/level-two/chapter-2/\#binary-exercise-1 "Permanent link")

For our first binary exercise, let's convert a PDF file to JSON:

1. Make an HTTP request to get this PDF file: `https://media.kaspersky.com/pdf/Kaspersky_Lab_Whitepaper_Anti_blocker.pdf.`
2. Use the **Extract From File node** to convert the file from binary to JSON.

Show me the solution

In the **HTTP Request node**, you should see the PDF file, like this:

[![HTTP Request node to get PDF](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_binarydata_httprequest_file.png)](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_binarydata_httprequest_file.png) _HTTP Request node to get PDF_

When you convert the PDF from binary to JSON using the **Extract From File node**, the result should look like this:

[![Extract From File node](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_binarydata_movedata_btoj.png)](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_binarydata_movedata_btoj.png) _Extract From File node_

To check the configuration of the nodes, you can copy the JSON workflow code below and paste it into your Editor UI:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>``` | ```<br>{<br>	"name": "Binary to JSON",<br>	"nodes": [<br>		{<br>		"parameters": {},<br>		"id": "78639a25-b69a-4b9c-84e0-69e045bed1a3",<br>		"name": "When clicking \"Execute Workflow\"",<br>		"type": "n8n-nodes-base.manualTrigger",<br>		"typeVersion": 1,<br>		"position": [<br>			480,<br>			520<br>		]<br>		},<br>		{<br>		"parameters": {<br>			"url": "https://media.kaspersky.com/pdf/Kaspersky_Lab_Whitepaper_Anti_blocker.pdf",<br>			"options": {}<br>		},<br>		"id": "a11310df-1287-4e9a-b993-baa6bd4265a6",<br>		"name": "HTTP Request",<br>		"type": "n8n-nodes-base.httpRequest",<br>		"typeVersion": 4.1,<br>		"position": [<br>			700,<br>			520<br>		]<br>		},<br>		{<br>		"parameters": {<br>			"operation": "pdf",<br>			"options": {}<br>		},<br>		"id": "88697b6b-fb02-4c3d-a715-750d60413e9f",<br>		"name": "Extract From File",<br>		"type": "n8n-nodes-base.extractFromFile",<br>		"typeVersion": 1,<br>		"position": [<br>			920,<br>			520<br>		]<br>		}<br>	],<br>	"pinData": {},<br>	"connections": {<br>		"When clicking \"Execute Workflow\"": {<br>		"main": [<br>			[<br>			{<br>				"node": "HTTP Request",<br>				"type": "main",<br>				"index": 0<br>			}<br>			]<br>		]<br>		},<br>		"HTTP Request": {<br>		"main": [<br>			[<br>			{<br>				"node": "Extract From File",<br>				"type": "main",<br>				"index": 0<br>			}<br>			]<br>		]<br>		}<br>	}<br>}<br>``` |

### Binary Exercise 2 [\#](https://docs.n8n.io/courses/level-two/chapter-2/\#binary-exercise-2 "Permanent link")

For our second binary exercise, let's convert some JSON data to binary:

1. Make an HTTP request to the Poetry DB API `https://poetrydb.org/random/1`.
2. Convert the returned data from JSON to binary using the **Convert to File node**.
3. Write the new binary file data to the machine where n8n is running using the **Read/Write Files From Disk node**.
4. To check that it worked out, use the **Read/Write Files From Disk node** to read the generated binary file.

Show me the solution

The workflow for this exercise looks like this:

[![Workflow for moving JSON to binary data](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_binarydata.png)](https://docs.n8n.io/_images/courses/level-two/chapter-two/exercise_binarydata.png) _Workflow for moving JSON to binary data_

To check the configuration of the nodes, you can copy the JSON workflow code below and paste it into your Editor UI:

|     |     |
| --- | --- |
| ```<br>  1<br>  2<br>  3<br>  4<br>  5<br>  6<br>  7<br>  8<br>  9<br> 10<br> 11<br> 12<br> 13<br> 14<br> 15<br> 16<br> 17<br> 18<br> 19<br> 20<br> 21<br> 22<br> 23<br> 24<br> 25<br> 26<br> 27<br> 28<br> 29<br> 30<br> 31<br> 32<br> 33<br> 34<br> 35<br> 36<br> 37<br> 38<br> 39<br> 40<br> 41<br> 42<br> 43<br> 44<br> 45<br> 46<br> 47<br> 48<br> 49<br> 50<br> 51<br> 52<br> 53<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>``` | ```<br>{<br>	"name": "JSON to file and Read-Write",<br>	"nodes": [<br>		{<br>		"parameters": {},<br>		"id": "78639a25-b69a-4b9c-84e0-69e045bed1a3",<br>		"name": "When clicking \"Execute Workflow\"",<br>		"type": "n8n-nodes-base.manualTrigger",<br>		"typeVersion": 1,<br>		"position": [<br>			480,<br>			520<br>		]<br>		},<br>		{<br>		"parameters": {<br>			"url": "https://poetrydb.org/random/1",<br>			"options": {}<br>		},<br>		"id": "a11310df-1287-4e9a-b993-baa6bd4265a6",<br>		"name": "HTTP Request",<br>		"type": "n8n-nodes-base.httpRequest",<br>		"typeVersion": 4.1,<br>		"position": [<br>			680,<br>			520<br>		]<br>		},<br>		{<br>		"parameters": {<br>			"operation": "toJson",<br>			"options": {}<br>		},<br>		"id": "06be18f6-f193-48e2-a8d9-35f4779d8324",<br>		"name": "Convert to File",<br>		"type": "n8n-nodes-base.convertToFile",<br>		"typeVersion": 1,<br>		"position": [<br>			880,<br>			520<br>		]<br>		},<br>		{<br>		"parameters": {<br>			"operation": "write",<br>			"fileName": "/tmp/poetrydb.json",<br>			"options": {}<br>		},<br>		"id": "f2048e5d-fa8f-4708-b15a-d07de359f2e5",<br>		"name": "Read/Write Files from Disk",<br>		"type": "n8n-nodes-base.readWriteFile",<br>		"typeVersion": 1,<br>		"position": [<br>			1080,<br>			520<br>		]<br>		},<br>		{<br>		"parameters": {<br>			"fileSelector": "={{ $json.fileName }}",<br>			"options": {}<br>		},<br>		"id": "d630906c-09d4-49f4-ba14-416c0f4de1c8",<br>		"name": "Read/Write Files from Disk1",<br>		"type": "n8n-nodes-base.readWriteFile",<br>		"typeVersion": 1,<br>		"position": [<br>			1280,<br>			520<br>		]<br>		}<br>	],<br>	"pinData": {},<br>	"connections": {<br>		"When clicking \"Execute Workflow\"": {<br>		"main": [<br>			[<br>			{<br>				"node": "HTTP Request",<br>				"type": "main",<br>				"index": 0<br>			}<br>			]<br>		]<br>		},<br>		"HTTP Request": {<br>		"main": [<br>			[<br>			{<br>				"node": "Convert to File",<br>				"type": "main",<br>				"index": 0<br>			}<br>			]<br>		]<br>		},<br>		"Convert to File": {<br>		"main": [<br>			[<br>			{<br>				"node": "Read/Write Files from Disk",<br>				"type": "main",<br>				"index": 0<br>			}<br>			]<br>		]<br>		},<br>		"Read/Write Files from Disk": {<br>		"main": [<br>			[<br>			{<br>				"node": "Read/Write Files from Disk1",<br>				"type": "main",<br>				"index": 0<br>			}<br>			]<br>		]<br>		}<br>	}<br>}<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top