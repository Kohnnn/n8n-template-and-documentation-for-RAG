---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/"
title: "KoboToolbox node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/#kobotoolbox-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox.md "Edit this page")

# KoboToolbox node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/\#kobotoolbox-node "Permanent link")

Use the KoboToolbox node to automate work in KoboToolbox, and integrate KoboToolbox with other applications. n8n has built-in support for a wide range of KoboToolbox features, including creating, updating, deleting, and getting files, forms, hooks, and submissions.

On this page, you'll find a list of operations the KoboToolbox node supports and links to more resources.

Credentials

Refer to [KoboToolbox credentials](https://docs.n8n.io/integrations/builtin/credentials/kobotoolbox/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/\#operations "Permanent link")

- File
  - Create
  - Delete
  - Get
  - Get Many
- Form
  - Get
  - Get Many
    - Redeploy
- Hook
  - Get
  - Get Many
  - Logs
  - Retry All
  - Retry One
- Submission
  - Delete
  - Get
  - Get Many
  - Get Validation Status
  - Update Validation Status

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/\#templates-and-examples "Permanent link")

[Browse KoboToolbox integration templates](https://n8n.io/integrations/kobotoolbox/), or [search all templates](https://n8n.io/workflows/)

## Options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/\#options "Permanent link")

### Query Options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/\#query-options "Permanent link")

The Query Submission operation supports query options:

- In the main section of the **Parameters** panel:
  - **Start** controls the index offset to start the query from (to use the API pagination logic).
  - **Limit** sets the maximum number of records to return. Note that the API always has a limit of 30,000 returned records, whatever value you provide.
- In the **Query Options** section, you can activate the following parameters:
  - **Query** lets you specify filter predicates in MongoDB's JSON query format. For example: `{"status": "success", "_submission_time": {"$lt": "2021-11-01T01:02:03"}}` queries for all submissions with the value `success` for the field `status`, and submitted before November 1st, 2021, 01:02:03.
  - **Fields** lets you specify the list of fields you want to fetch, to make the response lighter.
  - **Sort** lets you provide a list of sorting criteria in MongoDB JSON format. For example, `{"status": 1, "_submission_time": -1}` specifies a sort order by ascending status, and then descending submission time.

More details about these options can be found in the [Formhub API docs](https://github.com/SEL-Columbia/formhub/wiki/Formhub-Access-Points-(API)#api-parameters)

### Submission options [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/\#submission-options "Permanent link")

All operations that return form submission data offer options to tweak the response. These include:

- Download options lets you download any attachment linked to each particular form submissions, such as pictures and videos. It also lets you select the naming pattern, and the file size to download (if available - typically for images).
- Formatting options perform some reformatting as described in [About reformatting](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/#about-reformatting).

#### About reformatting [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/\#about-reformatting "Permanent link")

The default JSON format for KoboToolbox submission data is sometimes hard to deal with, because it's not schema-aware, and all fields are therefore returned as strings.

This node provides a lightweight opinionated reformatting logic, enabled with the **Reformat?** parameter, available on all operations that return form submissions: the submission query, get, and the attachment download operations.

When enabled, the reformatting:

- Reorganizes the JSON into a multi-level hierarchy following the form's groups. By default, question grouping hierarchy is materialized by a `/` character in the field names, for example `Group1/Question1`. With reformatting enabled, n8n reorganizes these into `Group1.Question1`, as nested JSON objects.
- Renames fields to trim `_` (not supported by many downstream systems).
- Parses all geospatial fields (Point, Line, and Area question types) into their standard GeoJSON equivalent.
- Splits all fields matching any of the **Multiselect Mask** wildcard masks into an array. Since the multi-select fields appear as space-separated strings, they can't be guessed algorithmically, so you must provide a field naming mask. Format the masks as a comma-separated list. Lists support the `*` wildcard.
- Converts all fields matching any of the **Number Mask** wildcard masks into a JSON float.

Here's a detailed example in JSON:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>``` | ```<br>{<br>  "_id": 471987,<br>  "formhub/uuid": "189436bb09a54957bfcc798e338b54d6",<br>  "start": "2021-12-05T16:13:38.527+02:00",<br>  "end": "2021-12-05T16:15:33.407+02:00",<br>  "Field_Details/Field_Name": "Test Fields",<br>  "Field_Details/Field_Location": "-1.932914 30.078211 1421 165",<br>  "Field_Details/Field_Shape": "-1.932914 30.078211 1421 165;-1.933011 30.078085 0 0;-1.933257 30.078004 0 0;-1.933338 30.078197 0 0;-1.933107 30.078299 0 0;-1.932914 30.078211 1421 165",<br>  "Field_Details/Crops_Grown": "maize beans avocado",<br>  "Field_Details/Field_Size_sqm": "2300",<br>  "__version__": "veGcULpqP6JNFKRJbbMvMs",<br>  "meta/instanceID": "uuid:2356cbbe-c1fd-414d-85c8-84f33e92618a",<br>  "_xform_id_string": "ajXVJpBkTD5tB4Nu9QXpgm",<br>  "_uuid": "2356cbbe-c1fd-414d-85c8-84f33e92618a",<br>  "_attachments": [],<br>  "_status": "submitted_via_web",<br>  "_geolocation": [<br>    -1.932914,<br>    30.078211<br>  ],<br>  "_submission_time": "2021-12-05T14:15:44",<br>  "_tags": [],<br>  "_notes": [],<br>  "_validation_status": {},<br>  "_submitted_by": null<br>}<br>``` |

With reformatting enabled, and the appropriate masks for multi-select and number formatting (for example, `Crops_*` and `*_sqm` respectively), n8n parses it into:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>``` | ```<br>{<br>  "id": 471987,<br>  "formhub": {<br>    "uuid": "189436bb09a54957bfcc798e338b54d6"<br>  },<br>  "start": "2021-12-05T16:13:38.527+02:00",<br>  "end": "2021-12-05T16:15:33.407+02:00",<br>  "Field_Details": {<br>    "Field_Name": "Test Fields",<br>    "Field_Location": {<br>      "lat": -1.932914,<br>      "lon": 30.078211<br>    },<br>    "Field_Shape": {<br>      "type": "polygon",<br>      "coordinates": [<br>        {<br>          "lat": -1.932914,<br>          "lon": 30.078211<br>        },<br>        {<br>          "lat": -1.933011,<br>          "lon": 30.078085<br>        },<br>        {<br>          "lat": -1.933257,<br>          "lon": 30.078004<br>        },<br>        {<br>          "lat": -1.933338,<br>          "lon": 30.078197<br>        },<br>        {<br>          "lat": -1.933107,<br>          "lon": 30.078299<br>        },<br>        {<br>          "lat": -1.932914,<br>          "lon": 30.078211<br>        }<br>      ]<br>    },<br>    "Crops_Grown": [<br>      "maize",<br>      "beans",<br>      "avocado"<br>    ],<br>    "Field_Size_sqm": 2300<br>  },<br>  "version": "veGcULpqP6JNFKRJbbMvMs",<br>  "meta": {<br>    "instanceID": "uuid:2356cbbe-c1fd-414d-85c8-84f33e92618a"<br>  },<br>  "xform_id_string": "ajXVJpBkTD5tB4Nu9QXpgm",<br>  "uuid": "2356cbbe-c1fd-414d-85c8-84f33e92618a",<br>  "attachments": [],<br>  "status": "submitted_via_web",<br>  "geolocation": {<br>    "lat": -1.932914,<br>    "lon": 30.078211<br>  },<br>  "submission_time": "2021-12-05T14:15:44",<br>  "tags": [],<br>  "notes": [],<br>  "validation_status": {},<br>  "submitted_by": null<br>}<br>``` |

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top