---
url: "https://docs.n8n.io/embed/workflow-templates/"
title: "Workflows templates | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/embed/workflow-templates/#workflow-templates)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/embed/workflow-templates.md "Edit this page")

# Workflow templates [\#](https://docs.n8n.io/embed/workflow-templates/\#workflow-templates "Permanent link")

Feature availability

Embed requires an embed license. For more information about when to use Embed, as well as costs and licensing processes, refer to [Embed](https://n8n.io/embed/) on the n8n website.

n8n provides a library of workflow [templates](https://docs.n8n.io/glossary/#template-n8n). When embedding n8n, you can:

- Continue to use n8n's workflow templates library (this is the default behavior)
- Disable workflow templates
- Create your own workflow templates library

## Disable workflow templates [\#](https://docs.n8n.io/embed/workflow-templates/\#disable-workflow-templates "Permanent link")

In your environment variables, set `N8N_TEMPLATES_ENABLED` to false.

## Use your own workflow templates library [\#](https://docs.n8n.io/embed/workflow-templates/\#use-your-own-workflow-templates-library "Permanent link")

In your environment variables, set `N8N_TEMPLATES_HOST` to the base URL of your API.

### Endpoints [\#](https://docs.n8n.io/embed/workflow-templates/\#endpoints "Permanent link")

Your API must provide the same endpoints and data structure as n8n's.

The endpoints are:

| Method | Path |
| --- | --- |
| GET | /templates/workflows/ `<id>` |
| GET | /templates/search |
| GET | /templates/collections/ `<id>` |
| GET | /templates/collections |
| GET | /templates/categories |
| GET | /health |

### Query parameters [\#](https://docs.n8n.io/embed/workflow-templates/\#query-parameters "Permanent link")

The `/templates/search` endpoint accepts the following query parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `page` | integer | The page of results to return |
| `rows` | integer | The maximum number of results to return per page |
| `category` | comma-separated list of strings (categories) | The categories to search within |
| `search` | string | The search query |

The `/templates/collections` endpoint accepts the following query parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `category` | comma-separated list of strings (categories) | The categories to search within |
| `search` | string | The search query |

### Data schema [\#](https://docs.n8n.io/embed/workflow-templates/\#data-schema "Permanent link")

You can explore the data structure of the items in the response object returned by endpoints here:

Show `workflow` item data schema

| Workflow item data schema |
| --- |
| ```<br>  1<br>  2<br>  3<br>  4<br>  5<br>  6<br>  7<br>  8<br>  9<br> 10<br> 11<br> 12<br> 13<br> 14<br> 15<br> 16<br> 17<br> 18<br> 19<br> 20<br> 21<br> 22<br> 23<br> 24<br> 25<br> 26<br> 27<br> 28<br> 29<br> 30<br> 31<br> 32<br> 33<br> 34<br> 35<br> 36<br> 37<br> 38<br> 39<br> 40<br> 41<br> 42<br> 43<br> 44<br> 45<br> 46<br> 47<br> 48<br> 49<br> 50<br> 51<br> 52<br> 53<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>``` | ```<br>{<br>  "$schema": "http://json-schema.org/draft-07/schema#",<br>  "title": "Generated schema for Root",<br>  "type": "object",<br>  "properties": {<br>    "id": {<br>      "type": "number"<br>    },<br>    "name": {<br>      "type": "string"<br>    },<br>    "totalViews": {<br>      "type": "number"<br>    },<br>    "price": {},<br>    "purchaseUrl": {},<br>    "recentViews": {<br>      "type": "number"<br>    },<br>    "createdAt": {<br>      "type": "string"<br>    },<br>    "user": {<br>      "type": "object",<br>      "properties": {<br>        "username": {<br>          "type": "string"<br>        },<br>        "verified": {<br>          "type": "boolean"<br>        }<br>      },<br>      "required": [<br>        "username",<br>        "verified"<br>      ]<br>    },<br>    "nodes": {<br>      "type": "array",<br>      "items": {<br>        "type": "object",<br>        "properties": {<br>          "id": {<br>            "type": "number"<br>          },<br>          "icon": {<br>            "type": "string"<br>          },<br>          "name": {<br>            "type": "string"<br>          },<br>          "codex": {<br>            "type": "object",<br>            "properties": {<br>              "data": {<br>                "type": "object",<br>                "properties": {<br>                  "details": {<br>                    "type": "string"<br>                  },<br>                  "resources": {<br>                    "type": "object",<br>                    "properties": {<br>                      "generic": {<br>                        "type": "array",<br>                        "items": {<br>                          "type": "object",<br>                          "properties": {<br>                            "url": {<br>                              "type": "string"<br>                            },<br>                            "icon": {<br>                              "type": "string"<br>                            },<br>                            "label": {<br>                              "type": "string"<br>                            }<br>                          },<br>                          "required": [<br>                            "url",<br>                            "label"<br>                          ]<br>                        }<br>                      },<br>                      "primaryDocumentation": {<br>                        "type": "array",<br>                        "items": {<br>                          "type": "object",<br>                          "properties": {<br>                            "url": {<br>                              "type": "string"<br>                            }<br>                          },<br>                          "required": [<br>                            "url"<br>                          ]<br>                        }<br>                      }<br>                    },<br>                    "required": [<br>                      "primaryDocumentation"<br>                    ]<br>                  },<br>                  "categories": {<br>                    "type": "array",<br>                    "items": {<br>                      "type": "string"<br>                    }<br>                  },<br>                  "nodeVersion": {<br>                    "type": "string"<br>                  },<br>                  "codexVersion": {<br>                    "type": "string"<br>                  }<br>                },<br>                "required": [<br>                  "categories"<br>                ]<br>              }<br>            }<br>          },<br>          "group": {<br>            "type": "string"<br>          },<br>          "defaults": {<br>            "type": "object",<br>            "properties": {<br>              "name": {<br>                "type": "string"<br>              },<br>              "color": {<br>                "type": "string"<br>              }<br>            },<br>            "required": [<br>              "name"<br>            ]<br>          },<br>          "iconData": {<br>            "type": "object",<br>            "properties": {<br>              "icon": {<br>                "type": "string"<br>              },<br>              "type": {<br>                "type": "string"<br>              },<br>              "fileBuffer": {<br>                "type": "string"<br>              }<br>            },<br>            "required": [<br>              "type"<br>            ]<br>          },<br>          "displayName": {<br>            "type": "string"<br>          },<br>          "typeVersion": {<br>            "type": "number"<br>          },<br>          "nodeCategories": {<br>            "type": "array",<br>            "items": {<br>              "type": "object",<br>              "properties": {<br>                "id": {<br>                  "type": "number"<br>                },<br>                "name": {<br>                  "type": "string"<br>                }<br>              },<br>              "required": [<br>                "id",<br>                "name"<br>              ]<br>            }<br>          }<br>        },<br>        "required": [<br>          "id",<br>          "icon",<br>          "name",<br>          "codex",<br>          "group",<br>          "defaults",<br>          "iconData",<br>          "displayName",<br>          "typeVersion"<br>        ]<br>      }<br>    }<br>  },<br>  "required": [<br>    "id",<br>    "name",<br>    "totalViews",<br>    "price",<br>    "purchaseUrl",<br>    "recentViews",<br>    "createdAt",<br>    "user",<br>    "nodes"<br>  ]<br>}<br>``` |

Show `category` item data schema

| Category item data schema |
| --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>``` | ```<br>{<br>  "$schema": "http://json-schema.org/draft-07/schema#",<br>  "type": "object",<br>  "properties": {<br>    "id": {<br>      "type": "number"<br>    },<br>    "name": {<br>      "type": "string"<br>    }<br>  },<br>  "required": [<br>    "id",<br>    "name"<br>  ]<br>}<br>``` |

Show `collection` item data schema

| Collection item data schema |
| --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>``` | ```<br>{<br>  "$schema": "http://json-schema.org/draft-07/schema#",<br>  "type": "object",<br>  "properties": {<br>    "id": {<br>      "type": "number"<br>    },<br>    "rank": {<br>      "type": "number"<br>    },<br>    "name": {<br>      "type": "string"<br>    },<br>    "totalViews": {},<br>    "createdAt": {<br>      "type": "string"<br>    },<br>    "workflows": {<br>      "type": "array",<br>      "items": {<br>        "type": "object",<br>        "properties": {<br>          "id": {<br>            "type": "number"<br>          }<br>        },<br>        "required": [<br>          "id"<br>        ]<br>      }<br>    },<br>    "nodes": {<br>      "type": "array",<br>      "items": {}<br>    }<br>  },<br>  "required": [<br>    "id",<br>    "rank",<br>    "name",<br>    "totalViews",<br>    "createdAt",<br>    "workflows",<br>    "nodes"<br>  ]<br>}<br>``` |

You can also interactively explore n8n's API endpoints:

[https://api.n8n.io/templates/categories](https://api.n8n.io/templates/categories)

[https://api.n8n.io/templates/collections](https://api.n8n.io/templates/collections)

[https://api.n8n.io/templates/search](https://api.n8n.io/templates/search)

[https://api.n8n.io/health](https://api.n8n.io/health)

You can [contact us](mailto:help@n8n.io) for more support.

## Add your workflows to the n8n library [\#](https://docs.n8n.io/embed/workflow-templates/\#add-your-workflows-to-the-n8n-library "Permanent link")

You can submit your workflows to n8n's template library.

n8n is working on a creator program, and developing a marketplace of templates. This is an ongoing project, and details are likely to change.

Refer to [n8n Creator hub](https://www.notion.so/n8n/n8n-Creator-hub-7bd2cbe0fce0449198ecb23ff4a2f76f) for information on how to submit templates and become a creator.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top