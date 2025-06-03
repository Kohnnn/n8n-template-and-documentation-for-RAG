---
url: "https://docs.n8n.io/embed/managing-workflows/"
title: "Workflow management | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/embed/managing-workflows/#workflow-management-in-embed)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/embed/managing-workflows.md "Edit this page")

# Workflow management in Embed [\#](https://docs.n8n.io/embed/managing-workflows/\#workflow-management-in-embed "Permanent link")

Feature availability

Embed requires an embed license. For more information about when to use Embed, as well as costs and licensing processes, refer to [Embed](https://n8n.io/embed/) on the n8n website.

When managing an embedded n8n deployment, spanning across teams or organizations, you will likely need to run the same (or similar) workflows for multiple users. There are two available options for doing so:

| Solution | Pros | Cons |
| --- | --- | --- |
| Create a workflow for each user | No limitation on how workflow starts (can use any trigger) | Requires managing multiple workflows. |
| Create a single workflow, and pass it user credentials when executing | Simplified workflow management (only need to change one workflow). | To run the workflow, your product must call it |

Warning

The APIs referenced in this document are subject to change at any time. Be sure the check for continued functionality with each version upgrade.

## Workflow per user [\#](https://docs.n8n.io/embed/managing-workflows/\#workflow-per-user "Permanent link")

There are three general steps to follow:

- Obtain the credentials for each user, and any additional parameters that may be required based on the workflow.
- Create the [n8n credentials](https://docs.n8n.io/glossary/#credential-n8n) for this user.
- Create the workflow.

### 1\. Obtain user credentials [\#](https://docs.n8n.io/embed/managing-workflows/\#1-obtain-user-credentials "Permanent link")

Here you need to capture all credentials for any node/service this user must authenticate with, along with any additional parameters required for the particular workflow. The credentials and any parameters needed will depend on your workflow and what you are trying to do.

### 2\. Create user credentials [\#](https://docs.n8n.io/embed/managing-workflows/\#2-create-user-credentials "Permanent link")

After all relevant credential details have been obtained, you can proceed to create the relevant service credentials in n8n. This can be done using the Editor UI or API call.

#### Using the Editor UI [\#](https://docs.n8n.io/embed/managing-workflows/\#using-the-editor-ui "Permanent link")

1. From the menu select **Credentials** \> **New**.
2. Use the drop-down to select the **Credential type** to create, for example _Airtable_.
    [![Create New Credentials drop-down](https://docs.n8n.io/_images/embed/managing-workflows/create_new_credentials.png)](https://docs.n8n.io/_images/embed/managing-workflows/create_new_credentials.png)
3. In the **Create New Credentials** modal, enter the corresponding credentials details for the user, and select the nodes that will have access to these credentials.
    [![Create New Credentials modal](https://docs.n8n.io/_images/embed/managing-workflows/create_new_credentials2.png)](https://docs.n8n.io/_images/embed/managing-workflows/create_new_credentials2.png)
4. Click **Create** to finish and save.

#### Using the API [\#](https://docs.n8n.io/embed/managing-workflows/\#using-the-api "Permanent link")

The frontend API used by the Editor UI can also be called to achieve the same result. The API endpoint is in the format: `https://<n8n-domain>/rest/credentials`.

For example, to create the credentials in the Editor UI example above, the request would be:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>POST https://<n8n-domain>/rest/credentials<br>``` |

With the request body:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>``` | ```<br>{<br>   "name":"MyAirtable",<br>   "type":"airtableApi",<br>   "nodesAccess":[<br>      {<br>         "nodeType":"n8n-nodes-base.airtable"<br>      }<br>   ],<br>   "data":{<br>      "apiKey":"q12we34r5t67yu"<br>   }<br>}<br>``` |

The response will contain the ID of the new credentials, which you will use when creating the workflow for this user:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>``` | ```<br>{<br>   "data":{<br>      "name":"MyAirtable",<br>      "type":"airtableApi",<br>      "data":{<br>         "apiKey":"q12we34r5t67yu"<br>      },<br>      "nodesAccess":[<br>         {<br>            "nodeType":"n8n-nodes-base.airtable",<br>            "date":"2021-09-10T07:41:27.770Z"<br>         }<br>      ],<br>      "id":"29",<br>      "createdAt":"2021-09-10T07:41:27.777Z",<br>      "updatedAt":"2021-09-10T07:41:27.777Z"<br>   }<br>}<br>``` |

### 3\. Create the workflow [\#](https://docs.n8n.io/embed/managing-workflows/\#3-create-the-workflow "Permanent link")

Best practice is to have a “base” workflow that you then duplicate and customize for each new user with their credentials (and any other details).

You can duplicate and customize your template workflow using either the Editor UI or API call.

#### Using the Editor UI [\#](https://docs.n8n.io/embed/managing-workflows/\#using-the-editor-ui_1 "Permanent link")

1. From the menu select **Workflows** \> **Open** to open the template workflow to be duplicated.

2. Select **Workflows** \> **Duplicate**, then enter a name for this new workflow and click **Save**.
    [![Duplicate workflow](https://docs.n8n.io/_images/embed/managing-workflows/duplicate_workflow.png)](https://docs.n8n.io/_images/embed/managing-workflows/duplicate_workflow.png)

3. Update all relevant nodes to use the credentials for this user (created above).

4. **Save** this workflow set it to **Active** using the toggle in the top-right corner.


#### Using the API [\#](https://docs.n8n.io/embed/managing-workflows/\#using-the-api_1 "Permanent link")

1. Fetch the JSON of the template workflow using the endpoint: `https://<n8n-domain>/rest/workflows/<workflow_id>`


|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>GET https://<n8n-domain>/rest/workflows/1012<br>``` |


The response will contain the JSON data of the selected workflow:

|     |     |
| --- | --- |
| ```<br>  1<br>  2<br>  3<br>  4<br>  5<br>  6<br>  7<br>  8<br>  9<br> 10<br> 11<br> 12<br> 13<br> 14<br> 15<br> 16<br> 17<br> 18<br> 19<br> 20<br> 21<br> 22<br> 23<br> 24<br> 25<br> 26<br> 27<br> 28<br> 29<br> 30<br> 31<br> 32<br> 33<br> 34<br> 35<br> 36<br> 37<br> 38<br> 39<br> 40<br> 41<br> 42<br> 43<br> 44<br> 45<br> 46<br> 47<br> 48<br> 49<br> 50<br> 51<br> 52<br> 53<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>208<br>209<br>210<br>211<br>212<br>213<br>214<br>215<br>216<br>217<br>218<br>219<br>220<br>221<br>222<br>223<br>224<br>225<br>226<br>227<br>228<br>``` | ```<br>{<br>  "data": {<br>    "id": "1012",<br>    "name": "Nathan's Workflow",<br>    "active": false,<br>    "nodes": [<br>      {<br>        "parameters": {},<br>        "name": "Start",<br>        "type": "n8n-nodes-base.start",<br>        "typeVersion": 1,<br>        "position": [<br>          130,<br>          640<br>        ]<br>      },<br>      {<br>        "parameters": {<br>          "authentication": "headerAuth",<br>          "url": "https://internal.users.n8n.cloud/webhook/custom-erp",<br>          "options": {<br>            "splitIntoItems": true<br>          },<br>          "headerParametersUi": {<br>            "parameter": [<br>              {<br>                "name": "unique_id",<br>                "value": "recLhLYQbzNSFtHNq"<br>              }<br>            ]<br>          }<br>        },<br>        "name": "HTTP Request",<br>        "type": "n8n-nodes-base.httpRequest",<br>        "typeVersion": 1,<br>        "position": [<br>          430,<br>          300<br>        ],<br>        "credentials": {<br>          "httpHeaderAuth": "beginner_course"<br>        }<br>      },<br>      {<br>        "parameters": {<br>          "operation": "append",<br>          "application": "appKBGQfbm6NfW6bv",<br>          "table": "processingOrders",<br>          "options": {}<br>        },<br>        "name": "Airtable",<br>        "type": "n8n-nodes-base.airtable",<br>        "typeVersion": 1,<br>        "position": [<br>          990,<br>          210<br>        ],<br>        "credentials": {<br>          "airtableApi": "Airtable"<br>        }<br>      },<br>      {<br>        "parameters": {<br>          "conditions": {<br>            "string": [<br>              {<br>                "value1": "={{$json[\"orderStatus\"]}}",<br>                "value2": "processing"<br>              }<br>            ]<br>          }<br>        },<br>        "name": "IF",<br>        "type": "n8n-nodes-base.if",<br>        "typeVersion": 1,<br>        "position": [<br>          630,<br>          300<br>        ]<br>      },<br>      {<br>        "parameters": {<br>          "keepOnlySet": true,<br>          "values": {<br>            "number": [<br>              {<br>                "name": "=orderId",<br>                "value": "={{$json[\"orderID\"]}}"<br>              }<br>            ],<br>            "string": [<br>              {<br>                "name": "employeeName",<br>                "value": "={{$json[\"employeeName\"]}}"<br>              }<br>            ]<br>          },<br>          "options": {}<br>        },<br>        "name": "Set",<br>        "type": "n8n-nodes-base.set",<br>        "typeVersion": 1,<br>        "position": [<br>          800,<br>          210<br>        ]<br>      },<br>      {<br>        "parameters": {<br>          "functionCode": "let totalBooked = items.length;\nlet bookedSum = 0;\n\nfor(let i=0; i < items.length; i++) {\n  bookedSum = bookedSum + items[i].json.orderPrice;\n}\nreturn [{json:{totalBooked, bookedSum}}]\n"<br>        },<br>        "name": "Function",<br>        "type": "n8n-nodes-base.function",<br>        "typeVersion": 1,<br>        "position": [<br>          800,<br>          400<br>        ]<br>      },<br>      {<br>        "parameters": {<br>          "webhookUri": "https://discord.com/api/webhooks/865213348202151968/oD5_WPDQwtr22Vjd_82QP3-_4b_lGhAeM7RynQ8Js5DzyXrQEnj0zeAQIA6fki1JLtXE",<br>          "text": "=This week we have {{$json[\"totalBooked\"]}} booked orders with a total value of {{$json[\"bookedSum\"]}}. My Unique ID: {{$node[\"HTTP Request\"].parameter[\"headerParametersUi\"][\"parameter\"][0][\"value\"]}}"<br>        },<br>        "name": "Discord",<br>        "type": "n8n-nodes-base.discord",<br>        "typeVersion": 1,<br>        "position": [<br>          1000,<br>          400<br>        ]<br>      },<br>      {<br>        "parameters": {<br>          "triggerTimes": {<br>            "item": [<br>              {<br>                "mode": "everyWeek",<br>                "hour": 9<br>              }<br>            ]<br>          }<br>        },<br>        "name": "Cron",<br>        "type": "n8n-nodes-base.cron",<br>        "typeVersion": 1,<br>        "position": [<br>          220,<br>          300<br>        ]<br>      }<br>    ],<br>    "connections": {<br>      "HTTP Request": {<br>        "main": [<br>          [<br>            {<br>              "node": "IF",<br>              "type": "main",<br>              "index": 0<br>            }<br>          ]<br>        ]<br>      },<br>      "Start": {<br>        "main": [<br>          []<br>        ]<br>      },<br>      "IF": {<br>        "main": [<br>          [<br>            {<br>              "node": "Set",<br>              "type": "main",<br>              "index": 0<br>            }<br>          ],<br>          [<br>            {<br>              "node": "Function",<br>              "type": "main",<br>              "index": 0<br>            }<br>          ]<br>        ]<br>      },<br>      "Set": {<br>        "main": [<br>          [<br>            {<br>              "node": "Airtable",<br>              "type": "main",<br>              "index": 0<br>            }<br>          ]<br>        ]<br>      },<br>      "Function": {<br>        "main": [<br>          [<br>            {<br>              "node": "Discord",<br>              "type": "main",<br>              "index": 0<br>            }<br>          ]<br>        ]<br>      },<br>      "Cron": {<br>        "main": [<br>          [<br>            {<br>              "node": "HTTP Request",<br>              "type": "main",<br>              "index": 0<br>            }<br>          ]<br>        ]<br>      }<br>    },<br>    "createdAt": "2021-07-16T11:15:46.066Z",<br>    "updatedAt": "2021-07-16T12:05:44.045Z",<br>    "settings": {},<br>    "staticData": null,<br>    "tags": []<br>  }<br>}<br>``` |

1. Save the returned JSON data and update any relevant credentials and fields for the new user.

2. Create a new workflow using the updated JSON as the request body at endpoint: `https://<n8n-domain>/rest/workflows`



|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>POST https://<n8n-domain>/rest/workflows/<br>``` |


The response will contain the ID of the new workflow, which you will use in the next step.

1. Lastly, activate the new workflow:



|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>PATCH https://<n8n-domain>/rest/workflows/1012<br>``` |


Passing the additional value `active` in your JSON payload:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>``` | ```<br>// ...<br>"active":true,<br>"settings": {},<br>"staticData": null,<br>"tags": []<br>``` |

## Single workflow [\#](https://docs.n8n.io/embed/managing-workflows/\#single-workflow "Permanent link")

There are four steps to follow to implement this method:

- Obtain the credentials for each user, and any additional parameters that may be required based on the workflow. See [Obtain user credentials](https://docs.n8n.io/embed/managing-workflows/#1-obtain-user-credentials) above.
- Create the n8n credentials for this user. See [Create user credentials](https://docs.n8n.io/embed/managing-workflows/#2-create-user-credentials) above.
- Create the workflow.
- Call the workflow as needed.

### Create the workflow [\#](https://docs.n8n.io/embed/managing-workflows/\#create-the-workflow "Permanent link")

The details and scope of this workflow will vary greatly according to the individual use case, however there are a few design implementations to keep in mind:

- This workflow must be triggered by a [Webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/) node.
- The incoming webhook call must contain the user’s credentials and any other workflow parameters required.
- Each node where the user’s credentials are needed should use an [expression](https://docs.n8n.io/code/expressions/) so that the node’s credential field reads the credential provided in the webhook call.
- Save and activate the workflow, ensuring the production URL is selected for the Webhook node. Refer to [webhook node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/) for more information.

### Call the workflow [\#](https://docs.n8n.io/embed/managing-workflows/\#call-the-workflow "Permanent link")

For each new user, or for any existing user as may be needed, call the webhook defined as the workflow trigger and provide the necessary credentials (and any other workflow parameters).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top