---
url: "https://docs.n8n.io/api/api-reference/"
title: "API reference | n8n Docs  "
---

[edit.link.title](https://github.com/n8n-io/n8n-docs/edit/main/docs/api/api-reference.md "edit.link.title")

- User
  - getRetrieve all users
  - postCreate multiple users
  - getGet user by ID/Email
  - delDelete a user
  - patchChange a user's global role
- Audit
  - postGenerate an audit
- Execution
  - getRetrieve all executions
  - getRetrieve an execution
  - delDelete an execution
- Workflow
  - postCreate a workflow
  - getRetrieve all workflows
  - getRetrieves a workflow
  - delDelete a workflow
  - putUpdate a workflow
  - postActivate a workflow
  - postDeactivate a workflow
  - putTransfer a workflow to another project.
  - putTransfer a credential to another project.
  - getGet workflow tags
  - putUpdate tags of a workflow
- Credential
  - postCreate a credential
  - delDelete credential by ID
  - getShow credential data schema
- Tags
  - postCreate a tag
  - getRetrieve all tags
  - getRetrieves a tag
  - delDelete a tag
  - putUpdate a tag
- SourceControl
  - postPull changes from the remote repository
- Variables
  - postCreate a variable
  - getRetrieve variables
  - delDelete a variable
  - putUpdate a variable
- Projects
  - postCreate a project
  - getRetrieve projects
  - delDelete a project
- Project
  - putUpdate a project

[API docs by Redocly](https://redocly.com/redoc/)

# n8n Public API (1.1.1)

Download OpenAPI specification: [Download](https://docs.n8n.io/api/v1/openapi.yml)

E-mail: [hello@n8n.io](mailto:hello@n8n.io)License: [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md)[Terms of Service](https://n8n.io/legal/terms)

n8n Public API

[n8n API documentation](https://docs.n8n.io/api/)

## [tag/User](https://docs.n8n.io/api/api-reference/\#tag/User) User

Operations about users

## [tag/User/paths/~1users/get](https://docs.n8n.io/api/api-reference/\#tag/User/paths/~1users/get) Retrieve all users

Retrieve all users from your instance. Only available for the instance owner.

##### Authorizations:

_ApiKeyAuth_

##### query Parameters

|     |     |
| --- | --- |
| limit | number <= 250 <br>Default: 100<br>Example: limit=100<br>The maximum number of items to return. |
| cursor | string<br>Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail. |
| includeRole | boolean<br>Default: false<br>Example: includeRole=true<br>Whether to include the user's role or not. |
| projectId | string<br>Example: projectId=VmwOO9HeTEj20kxM |

### Responses

**200**

Operation successful.

**401**

Unauthorized

get/users

https://docs.n8n.io/api/v1/users

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"data": [\
{\
"id": "123e4567-e89b-12d3-a456-426614174000",\
"email": "john.doe@company.com",\
"firstName": "john",\
"lastName": "Doe",\
"isPending": true,\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z",\
"role": "owner"}],
"nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"}`

## [tag/User/paths/~1users/post](https://docs.n8n.io/api/api-reference/\#tag/User/paths/~1users/post) Create multiple users

Create one or more users.

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json  required

Array of users to be created.

Array

|     |     |
| --- | --- |
| email<br>required | string <email> |
| role | string<br>Enum:"global:admin""global:member" |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**403**

Forbidden

post/users

https://docs.n8n.io/api/v1/users

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`[\
{\
"email": "user@example.com",\
"role": "global:admin"}]`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"user": {
"id": "string",
"email": "string",
"inviteAcceptUrl": "string",
"emailSent": true},
"error": "string"}`

## [tag/User/paths/~1users~1{id}/get](https://docs.n8n.io/api/api-reference/\#tag/User/paths/~1users~1{id}/get) Get user by ID/Email

Retrieve a user from your instance. Only available for the instance owner.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string <identifier> <br>The ID or email of the user. |

##### query Parameters

|     |     |
| --- | --- |
| includeRole | boolean<br>Default: false<br>Example: includeRole=true<br>Whether to include the user's role or not. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

get/users/{id}

https://docs.n8n.io/api/v1/users/{id}

### Response samples

- 200

Content type

application/json

Copy

`{
"id": "123e4567-e89b-12d3-a456-426614174000",
"email": "john.doe@company.com",
"firstName": "john",
"lastName": "Doe",
"isPending": true,
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z",
"role": "owner"}`

## [tag/User/paths/~1users~1{id}/delete](https://docs.n8n.io/api/api-reference/\#tag/User/paths/~1users~1{id}/delete) Delete a user

Delete a user from your instance.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string <identifier> <br>The ID or email of the user. |

### Responses

**204**

Operation successful.

**401**

Unauthorized

**403**

Forbidden

**404**

The specified resource was not found.

delete/users/{id}

https://docs.n8n.io/api/v1/users/{id}

## [tag/User/paths/~1users~1{id}~1role/patch](https://docs.n8n.io/api/api-reference/\#tag/User/paths/~1users~1{id}~1role/patch) Change a user's global role

Change a user's global role

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string <identifier> <br>The ID or email of the user. |

##### Request Body schema: application/json  required

New role for the user

|     |     |
| --- | --- |
| newRoleName<br>required | string<br>Enum:"global:admin""global:member" |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**403**

Forbidden

**404**

The specified resource was not found.

patch/users/{id}/role

https://docs.n8n.io/api/v1/users/{id}/role

### Request samples

- Payload

Content type

application/json

Copy

`{
"newRoleName": "global:admin"}`

## [tag/Audit](https://docs.n8n.io/api/api-reference/\#tag/Audit) Audit

Operations about security audit

## [tag/Audit/paths/~1audit/post](https://docs.n8n.io/api/api-reference/\#tag/Audit/paths/~1audit/post) Generate an audit

Generate a security audit for your n8n instance.

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json  optional

|     |     |
| --- | --- |
| additionalOptions | object |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**500**

Internal server error.

post/audit

https://docs.n8n.io/api/v1/audit

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"additionalOptions": {
"daysAbandonedWorkflow": 0,
"categories": [\
"credentials"]}}`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"Credentials Risk Report": {
"risk": "credentials",
"sections": [\
{\
"title": "Credentials not used in any workflow",\
"description": "These credentials are not used in any workflow. Keeping unused credentials in your instance is an unneeded security risk.",\
"recommendation": "Consider deleting these credentials if you no longer need them.",\
"location": [\
{\
"kind": "credential",\
"id": "1",\
"name": "My Test Account"}]}]},
"Database Risk Report": {
"risk": "database",
"sections": [\
{\
"title": "Expressions in \"Execute Query\" fields in SQL nodes",\
"description": "This SQL node has an expression in the \"Query\" field of an \"Execute Query\" operation. Building a SQL query with an expression may lead to a SQL injection attack.",\
"recommendation": "Consider using the \"Query Parameters\" field to pass parameters to the query",\
"or validating the input of the expression in the "Query" field.": null,\
"location": [\
{\
"kind": "node",\
"workflowId": "1",\
"workflowName": "My Workflow",\
"nodeId": "51eb5852-ce0b-4806-b4ff-e41322a4041a",\
"nodeName": "MySQL",\
"nodeType": "n8n-nodes-base.mySql"}]}]},
"Filesystem Risk Report": {
"risk": "filesystem",
"sections": [\
{\
"title": "Nodes that interact with the filesystem",\
"description": "This node reads from and writes to any accessible file in the host filesystem. Sensitive file content may be manipulated through a node operation.",\
"recommendation": "Consider protecting any sensitive files in the host filesystem",\
"or refactoring the workflow so that it does not require host filesystem interaction.": null,\
"location": [\
{\
"kind": "node",\
"workflowId": "1",\
"workflowName": "My Workflow",\
"nodeId": "51eb5852-ce0b-4806-b4ff-e41322a4041a",\
"nodeName": "Ready Binary file",\
"nodeType": "n8n-nodes-base.readBinaryFile"}]}]},
"Nodes Risk Report": {
"risk": "nodes",
"sections": [\
{\
"title": "Community nodes",\
"description": "This node is sourced from the community. Community nodes are not vetted by the n8n team and have full access to the host system.",\
"recommendation": "Consider reviewing the source code in any community nodes installed in this n8n instance",\
"and uninstalling any community nodes no longer used.": null,\
"location": [\
{\
"kind": "community",\
"nodeType": "n8n-nodes-test.test",\
"packageUrl": "https://www.npmjs.com/package/n8n-nodes-test"}]}]},
"Instance Risk Report": {
"risk": "execution",
"sections": [\
{\
"title": "Unprotected webhooks in instance",\
"description": "These webhook nodes have the \"Authentication\" field set to \"None\" and are not directly connected to a node to validate the payload. Every unprotected webhook allows your workflow to be called by any third party who knows the webhook URL.",\
"recommendation": "Consider setting the \"Authentication\" field to an option other than \"None\"",\
"or validating the payload with one of the following nodes.": null,\
"location": [\
{\
"kind": "community",\
"nodeType": "n8n-nodes-test.test",\
"packageUrl": "https://www.npmjs.com/package/n8n-nodes-test"}]}]}}`

## [tag/Execution](https://docs.n8n.io/api/api-reference/\#tag/Execution) Execution

Operations about executions

## [tag/Execution/paths/~1executions/get](https://docs.n8n.io/api/api-reference/\#tag/Execution/paths/~1executions/get) Retrieve all executions

Retrieve all executions from your instance.

##### Authorizations:

_ApiKeyAuth_

##### query Parameters

|     |     |
| --- | --- |
| includeData | boolean<br>Whether or not to include the execution's detailed data. |
| status | string<br>Enum:"error""success""waiting"<br>Status to filter the executions by. |
| workflowId | string<br>Example: workflowId=1000<br>Workflow to filter the executions by. |
| projectId | string<br>Example: projectId=VmwOO9HeTEj20kxM |
| limit | number <= 250 <br>Default: 100<br>Example: limit=100<br>The maximum number of items to return. |
| cursor | string<br>Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**404**

The specified resource was not found.

get/executions

https://docs.n8n.io/api/v1/executions

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"data": [\
{\
"id": 1000,\
"data": { },\
"finished": true,\
"mode": "cli",\
"retryOf": 0,\
"retrySuccessId": "2",\
"startedAt": "2019-08-24T14:15:22Z",\
"stoppedAt": "2019-08-24T14:15:22Z",\
"workflowId": "1000",\
"waitTill": "2019-08-24T14:15:22Z",\
"customData": { }}],
"nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"}`

## [tag/Execution/paths/~1executions~1{id}/get](https://docs.n8n.io/api/api-reference/\#tag/Execution/paths/~1executions~1{id}/get) Retrieve an execution

Retrieve an execution from your instance.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | number<br>The ID of the execution. |

##### query Parameters

|     |     |
| --- | --- |
| includeData | boolean<br>Whether or not to include the execution's detailed data. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**404**

The specified resource was not found.

get/executions/{id}

https://docs.n8n.io/api/v1/executions/{id}

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"id": 1000,
"data": { },
"finished": true,
"mode": "cli",
"retryOf": 0,
"retrySuccessId": "2",
"startedAt": "2019-08-24T14:15:22Z",
"stoppedAt": "2019-08-24T14:15:22Z",
"workflowId": "1000",
"waitTill": "2019-08-24T14:15:22Z",
"customData": { }}`

## [tag/Execution/paths/~1executions~1{id}/delete](https://docs.n8n.io/api/api-reference/\#tag/Execution/paths/~1executions~1{id}/delete) Delete an execution

Deletes an execution from your instance.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | number<br>The ID of the execution. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**404**

The specified resource was not found.

delete/executions/{id}

https://docs.n8n.io/api/v1/executions/{id}

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"id": 1000,
"data": { },
"finished": true,
"mode": "cli",
"retryOf": 0,
"retrySuccessId": "2",
"startedAt": "2019-08-24T14:15:22Z",
"stoppedAt": "2019-08-24T14:15:22Z",
"workflowId": "1000",
"waitTill": "2019-08-24T14:15:22Z",
"customData": { }}`

## [tag/Workflow](https://docs.n8n.io/api/api-reference/\#tag/Workflow) Workflow

Operations about workflows

## [tag/Workflow/paths/~1workflows/post](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows/post) Create a workflow

Create a workflow in your instance.

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json  required

Created workflow object.

|     |     |
| --- | --- |
| name<br>required | string |
| nodes<br>required | Array of objects (node) |
| connections<br>required | object |
| settings<br>required | object (workflowSettings) |
| staticData | (string or null) or (object or null) |

### Responses

**200**

A workflow object

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

post/workflows

https://docs.n8n.io/api/v1/workflows

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"name": "Workflow 1",
"nodes": [\
{\
"id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
"name": "Jira",\
"webhookId": "string",\
"disabled": true,\
"notesInFlow": true,\
"notes": "string",\
"type": "n8n-nodes-base.Jira",\
"typeVersion": 1,\
"executeOnce": false,\
"alwaysOutputData": false,\
"retryOnFail": false,\
"maxTries": 0,\
"waitBetweenTries": 0,\
"continueOnFail": false,\
"onError": "stopWorkflow",\
"position": [\
-100,\
80],\
"parameters": {\
"additionalProperties": { }},\
"credentials": {\
"jiraSoftwareCloudApi": {\
"id": "35",\
"name": "jiraApi"}}}],
"connections": {
"main": [\
{\
"node": "Jira",\
"type": "main",\
"index": 0}]},
"settings": {
"saveExecutionProgress": true,
"saveManualExecutions": true,
"saveDataErrorExecution": "all",
"saveDataSuccessExecution": "all",
"executionTimeout": 3600,
"errorWorkflow": "VzqKEW0ShTXA5vPj",
"timezone": "America/New_York",
"executionOrder": "v1"},
"staticData": {
"lastId": 1}}`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"id": "2tUt1wbLX592XDdX",
"name": "Workflow 1",
"active": true,
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z",
"nodes": [\
{\
"id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
"name": "Jira",\
"webhookId": "string",\
"disabled": true,\
"notesInFlow": true,\
"notes": "string",\
"type": "n8n-nodes-base.Jira",\
"typeVersion": 1,\
"executeOnce": false,\
"alwaysOutputData": false,\
"retryOnFail": false,\
"maxTries": 0,\
"waitBetweenTries": 0,\
"continueOnFail": false,\
"onError": "stopWorkflow",\
"position": [\
-100,\
80],\
"parameters": {\
"additionalProperties": { }},\
"credentials": {\
"jiraSoftwareCloudApi": {\
"id": "35",\
"name": "jiraApi"}},\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}],
"connections": {
"main": [\
{\
"node": "Jira",\
"type": "main",\
"index": 0}]},
"settings": {
"saveExecutionProgress": true,
"saveManualExecutions": true,
"saveDataErrorExecution": "all",
"saveDataSuccessExecution": "all",
"executionTimeout": 3600,
"errorWorkflow": "VzqKEW0ShTXA5vPj",
"timezone": "America/New_York",
"executionOrder": "v1"},
"staticData": {
"lastId": 1},
"tags": [\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}]}`

## [tag/Workflow/paths/~1workflows/get](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows/get) Retrieve all workflows

Retrieve all workflows from your instance.

##### Authorizations:

_ApiKeyAuth_

##### query Parameters

|     |     |
| --- | --- |
| active | boolean<br>Example: active=true |
| tags | string<br>Example: tags=test,production |
| name | string<br>Example: name=My Workflow |
| projectId | string<br>Example: projectId=VmwOO9HeTEj20kxM |
| excludePinnedData | boolean<br>Example: excludePinnedData=true<br>Set this to avoid retrieving pinned data |
| limit | number <= 250 <br>Default: 100<br>Example: limit=100<br>The maximum number of items to return. |
| cursor | string<br>Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

get/workflows

https://docs.n8n.io/api/v1/workflows

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"data": [\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Workflow 1",\
"active": true,\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z",\
"nodes": [\
{\
"id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
"name": "Jira",\
"webhookId": "string",\
"disabled": true,\
"notesInFlow": true,\
"notes": "string",\
"type": "n8n-nodes-base.Jira",\
"typeVersion": 1,\
"executeOnce": false,\
"alwaysOutputData": false,\
"retryOnFail": false,\
"maxTries": 0,\
"waitBetweenTries": 0,\
"continueOnFail": false,\
"onError": "stopWorkflow",\
"position": [\
-100,\
80],\
"parameters": {\
"additionalProperties": { }},\
"credentials": {\
"jiraSoftwareCloudApi": {\
"id": "35",\
"name": "jiraApi"}},\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}],\
"connections": {\
"main": [\
{\
"node": "Jira",\
"type": "main",\
"index": 0}]},\
"settings": {\
"saveExecutionProgress": true,\
"saveManualExecutions": true,\
"saveDataErrorExecution": "all",\
"saveDataSuccessExecution": "all",\
"executionTimeout": 3600,\
"errorWorkflow": "VzqKEW0ShTXA5vPj",\
"timezone": "America/New_York",\
"executionOrder": "v1"},\
"staticData": {\
"lastId": 1},\
"tags": [\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}]}],
"nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"}`

## [tag/Workflow/paths/~1workflows~1{id}/get](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows~1{id}/get) Retrieves a workflow

Retrieves a workflow.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the workflow. |

##### query Parameters

|     |     |
| --- | --- |
| excludePinnedData | boolean<br>Example: excludePinnedData=true<br>Set this to avoid retrieving pinned data |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**404**

The specified resource was not found.

get/workflows/{id}

https://docs.n8n.io/api/v1/workflows/{id}

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"id": "2tUt1wbLX592XDdX",
"name": "Workflow 1",
"active": true,
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z",
"nodes": [\
{\
"id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
"name": "Jira",\
"webhookId": "string",\
"disabled": true,\
"notesInFlow": true,\
"notes": "string",\
"type": "n8n-nodes-base.Jira",\
"typeVersion": 1,\
"executeOnce": false,\
"alwaysOutputData": false,\
"retryOnFail": false,\
"maxTries": 0,\
"waitBetweenTries": 0,\
"continueOnFail": false,\
"onError": "stopWorkflow",\
"position": [\
-100,\
80],\
"parameters": {\
"additionalProperties": { }},\
"credentials": {\
"jiraSoftwareCloudApi": {\
"id": "35",\
"name": "jiraApi"}},\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}],
"connections": {
"main": [\
{\
"node": "Jira",\
"type": "main",\
"index": 0}]},
"settings": {
"saveExecutionProgress": true,
"saveManualExecutions": true,
"saveDataErrorExecution": "all",
"saveDataSuccessExecution": "all",
"executionTimeout": 3600,
"errorWorkflow": "VzqKEW0ShTXA5vPj",
"timezone": "America/New_York",
"executionOrder": "v1"},
"staticData": {
"lastId": 1},
"tags": [\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}]}`

## [tag/Workflow/paths/~1workflows~1{id}/delete](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows~1{id}/delete) Delete a workflow

Deletes a workflow.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the workflow. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**404**

The specified resource was not found.

delete/workflows/{id}

https://docs.n8n.io/api/v1/workflows/{id}

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"id": "2tUt1wbLX592XDdX",
"name": "Workflow 1",
"active": true,
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z",
"nodes": [\
{\
"id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
"name": "Jira",\
"webhookId": "string",\
"disabled": true,\
"notesInFlow": true,\
"notes": "string",\
"type": "n8n-nodes-base.Jira",\
"typeVersion": 1,\
"executeOnce": false,\
"alwaysOutputData": false,\
"retryOnFail": false,\
"maxTries": 0,\
"waitBetweenTries": 0,\
"continueOnFail": false,\
"onError": "stopWorkflow",\
"position": [\
-100,\
80],\
"parameters": {\
"additionalProperties": { }},\
"credentials": {\
"jiraSoftwareCloudApi": {\
"id": "35",\
"name": "jiraApi"}},\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}],
"connections": {
"main": [\
{\
"node": "Jira",\
"type": "main",\
"index": 0}]},
"settings": {
"saveExecutionProgress": true,
"saveManualExecutions": true,
"saveDataErrorExecution": "all",
"saveDataSuccessExecution": "all",
"executionTimeout": 3600,
"errorWorkflow": "VzqKEW0ShTXA5vPj",
"timezone": "America/New_York",
"executionOrder": "v1"},
"staticData": {
"lastId": 1},
"tags": [\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}]}`

## [tag/Workflow/paths/~1workflows~1{id}/put](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows~1{id}/put) Update a workflow

Update a workflow.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the workflow. |

##### Request Body schema: application/json  required

Updated workflow object.

|     |     |
| --- | --- |
| name<br>required | string |
| nodes<br>required | Array of objects (node) |
| connections<br>required | object |
| settings<br>required | object (workflowSettings) |
| staticData | (string or null) or (object or null) |

### Responses

**200**

Workflow object

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

**404**

The specified resource was not found.

put/workflows/{id}

https://docs.n8n.io/api/v1/workflows/{id}

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"name": "Workflow 1",
"nodes": [\
{\
"id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
"name": "Jira",\
"webhookId": "string",\
"disabled": true,\
"notesInFlow": true,\
"notes": "string",\
"type": "n8n-nodes-base.Jira",\
"typeVersion": 1,\
"executeOnce": false,\
"alwaysOutputData": false,\
"retryOnFail": false,\
"maxTries": 0,\
"waitBetweenTries": 0,\
"continueOnFail": false,\
"onError": "stopWorkflow",\
"position": [\
-100,\
80],\
"parameters": {\
"additionalProperties": { }},\
"credentials": {\
"jiraSoftwareCloudApi": {\
"id": "35",\
"name": "jiraApi"}}}],
"connections": {
"main": [\
{\
"node": "Jira",\
"type": "main",\
"index": 0}]},
"settings": {
"saveExecutionProgress": true,
"saveManualExecutions": true,
"saveDataErrorExecution": "all",
"saveDataSuccessExecution": "all",
"executionTimeout": 3600,
"errorWorkflow": "VzqKEW0ShTXA5vPj",
"timezone": "America/New_York",
"executionOrder": "v1"},
"staticData": {
"lastId": 1}}`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"id": "2tUt1wbLX592XDdX",
"name": "Workflow 1",
"active": true,
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z",
"nodes": [\
{\
"id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
"name": "Jira",\
"webhookId": "string",\
"disabled": true,\
"notesInFlow": true,\
"notes": "string",\
"type": "n8n-nodes-base.Jira",\
"typeVersion": 1,\
"executeOnce": false,\
"alwaysOutputData": false,\
"retryOnFail": false,\
"maxTries": 0,\
"waitBetweenTries": 0,\
"continueOnFail": false,\
"onError": "stopWorkflow",\
"position": [\
-100,\
80],\
"parameters": {\
"additionalProperties": { }},\
"credentials": {\
"jiraSoftwareCloudApi": {\
"id": "35",\
"name": "jiraApi"}},\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}],
"connections": {
"main": [\
{\
"node": "Jira",\
"type": "main",\
"index": 0}]},
"settings": {
"saveExecutionProgress": true,
"saveManualExecutions": true,
"saveDataErrorExecution": "all",
"saveDataSuccessExecution": "all",
"executionTimeout": 3600,
"errorWorkflow": "VzqKEW0ShTXA5vPj",
"timezone": "America/New_York",
"executionOrder": "v1"},
"staticData": {
"lastId": 1},
"tags": [\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}]}`

## [tag/Workflow/paths/~1workflows~1{id}~1activate/post](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows~1{id}~1activate/post) Activate a workflow

Active a workflow.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the workflow. |

### Responses

**200**

Workflow object

**401**

Unauthorized

**404**

The specified resource was not found.

post/workflows/{id}/activate

https://docs.n8n.io/api/v1/workflows/{id}/activate

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"id": "2tUt1wbLX592XDdX",
"name": "Workflow 1",
"active": true,
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z",
"nodes": [\
{\
"id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
"name": "Jira",\
"webhookId": "string",\
"disabled": true,\
"notesInFlow": true,\
"notes": "string",\
"type": "n8n-nodes-base.Jira",\
"typeVersion": 1,\
"executeOnce": false,\
"alwaysOutputData": false,\
"retryOnFail": false,\
"maxTries": 0,\
"waitBetweenTries": 0,\
"continueOnFail": false,\
"onError": "stopWorkflow",\
"position": [\
-100,\
80],\
"parameters": {\
"additionalProperties": { }},\
"credentials": {\
"jiraSoftwareCloudApi": {\
"id": "35",\
"name": "jiraApi"}},\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}],
"connections": {
"main": [\
{\
"node": "Jira",\
"type": "main",\
"index": 0}]},
"settings": {
"saveExecutionProgress": true,
"saveManualExecutions": true,
"saveDataErrorExecution": "all",
"saveDataSuccessExecution": "all",
"executionTimeout": 3600,
"errorWorkflow": "VzqKEW0ShTXA5vPj",
"timezone": "America/New_York",
"executionOrder": "v1"},
"staticData": {
"lastId": 1},
"tags": [\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}]}`

## [tag/Workflow/paths/~1workflows~1{id}~1deactivate/post](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows~1{id}~1deactivate/post) Deactivate a workflow

Deactivate a workflow.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the workflow. |

### Responses

**200**

Workflow object

**401**

Unauthorized

**404**

The specified resource was not found.

post/workflows/{id}/deactivate

https://docs.n8n.io/api/v1/workflows/{id}/deactivate

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"id": "2tUt1wbLX592XDdX",
"name": "Workflow 1",
"active": true,
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z",
"nodes": [\
{\
"id": "0f5532f9-36ba-4bef-86c7-30d607400b15",\
"name": "Jira",\
"webhookId": "string",\
"disabled": true,\
"notesInFlow": true,\
"notes": "string",\
"type": "n8n-nodes-base.Jira",\
"typeVersion": 1,\
"executeOnce": false,\
"alwaysOutputData": false,\
"retryOnFail": false,\
"maxTries": 0,\
"waitBetweenTries": 0,\
"continueOnFail": false,\
"onError": "stopWorkflow",\
"position": [\
-100,\
80],\
"parameters": {\
"additionalProperties": { }},\
"credentials": {\
"jiraSoftwareCloudApi": {\
"id": "35",\
"name": "jiraApi"}},\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}],
"connections": {
"main": [\
{\
"node": "Jira",\
"type": "main",\
"index": 0}]},
"settings": {
"saveExecutionProgress": true,
"saveManualExecutions": true,
"saveDataErrorExecution": "all",
"saveDataSuccessExecution": "all",
"executionTimeout": 3600,
"errorWorkflow": "VzqKEW0ShTXA5vPj",
"timezone": "America/New_York",
"executionOrder": "v1"},
"staticData": {
"lastId": 1},
"tags": [\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}]}`

## [tag/Workflow/paths/~1workflows~1{id}~1transfer/put](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows~1{id}~1transfer/put) Transfer a workflow to another project.

Transfer a workflow to another project.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the workflow. |

##### Request Body schema: application/json  required

Destination project information for the workflow transfer.

|     |     |
| --- | --- |
| destinationProjectId<br>required | string<br>The ID of the project to transfer the workflow to. |

### Responses

**200**

Operation successful.

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

**404**

The specified resource was not found.

put/workflows/{id}/transfer

https://docs.n8n.io/api/v1/workflows/{id}/transfer

### Request samples

- Payload

Content type

application/json

Copy

`{
"destinationProjectId": "string"}`

## [tag/Workflow/paths/~1credentials~1{id}~1transfer/put](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1credentials~1{id}~1transfer/put) Transfer a credential to another project.

Transfer a credential to another project.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the credential. |

##### Request Body schema: application/json  required

Destination project for the credential transfer.

|     |     |
| --- | --- |
| destinationProjectId<br>required | string<br>The ID of the project to transfer the credential to. |

### Responses

**200**

Operation successful.

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

**404**

The specified resource was not found.

put/credentials/{id}/transfer

https://docs.n8n.io/api/v1/credentials/{id}/transfer

### Request samples

- Payload

Content type

application/json

Copy

`{
"destinationProjectId": "string"}`

## [tag/Workflow/paths/~1workflows~1{id}~1tags/get](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows~1{id}~1tags/get) Get workflow tags

Get workflow tags.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the workflow. |

### Responses

**200**

List of tags

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

**404**

The specified resource was not found.

get/workflows/{id}/tags

https://docs.n8n.io/api/v1/workflows/{id}/tags

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`[\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}]`

## [tag/Workflow/paths/~1workflows~1{id}~1tags/put](https://docs.n8n.io/api/api-reference/\#tag/Workflow/paths/~1workflows~1{id}~1tags/put) Update tags of a workflow

Update tags of a workflow.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the workflow. |

##### Request Body schema: application/json  required

List of tags

Array

|     |     |
| --- | --- |
| id<br>required | string |

### Responses

**200**

List of tags after add the tag

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

**404**

The specified resource was not found.

put/workflows/{id}/tags

https://docs.n8n.io/api/v1/workflows/{id}/tags

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`[\
{\
"id": "2tUt1wbLX592XDdX"}]`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`[\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}]`

## [tag/Credential](https://docs.n8n.io/api/api-reference/\#tag/Credential) Credential

Operations about credentials

## [tag/Credential/paths/~1credentials/post](https://docs.n8n.io/api/api-reference/\#tag/Credential/paths/~1credentials/post) Create a credential

Creates a credential that can be used by nodes of the specified type.

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json  required

Credential to be created.

|     |     |
| --- | --- |
| name<br>required | string |
| type<br>required | string |
| data<br>required | object |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**415**

Unsupported media type.

post/credentials

https://docs.n8n.io/api/v1/credentials

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"name": "Joe's Github Credentials",
"type": "github",
"data": {
"token": "ada612vad6fa5df4adf5a5dsf4389adsf76da7s"}}`

### Response samples

- 200

Content type

application/json

Copy

`{
"id": "vHxaz5UaCghVYl9C",
"name": "John's Github account",
"type": "github",
"createdAt": "2022-04-29T11:02:29.842Z",
"updatedAt": "2022-04-29T11:02:29.842Z"}`

## [tag/Credential/operation/deleteCredential](https://docs.n8n.io/api/api-reference/\#tag/Credential/operation/deleteCredential) Delete credential by ID

Deletes a credential from your instance. You must be the owner of the credentials

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The credential ID that needs to be deleted |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**404**

The specified resource was not found.

delete/credentials/{id}

https://docs.n8n.io/api/v1/credentials/{id}

### Response samples

- 200

Content type

application/json

Copy

`{
"id": "R2DjclaysHbqn778",
"name": "Joe's Github Credentials",
"type": "github",
"createdAt": "2022-04-29T11:02:29.842Z",
"updatedAt": "2022-04-29T11:02:29.842Z"}`

## [tag/Credential/paths/~1credentials~1schema~1{credentialTypeName}/get](https://docs.n8n.io/api/api-reference/\#tag/Credential/paths/~1credentials~1schema~1{credentialTypeName}/get) Show credential data schema

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| credentialTypeName<br>required | string<br>The credential type name that you want to get the schema for |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**404**

The specified resource was not found.

get/credentials/schema/{credentialTypeName}

https://docs.n8n.io/api/v1/credentials/schema/{credentialTypeName}

### Response samples

- 200

Content type

application/json

Example

freshdeskApislackOAuth2ApifreshdeskApi

Copy
Expand all  Collapse all

`{
"additionalProperties": false,
"type": "object",
"properties": {
"apiKey": {
"type": "string"},
"domain": {
"type": "string"}},
"required": [\
"apiKey",\
"domain"]}`

## [tag/Tags](https://docs.n8n.io/api/api-reference/\#tag/Tags) Tags

Operations about tags

## [tag/Tags/paths/~1tags/post](https://docs.n8n.io/api/api-reference/\#tag/Tags/paths/~1tags/post) Create a tag

Create a tag in your instance.

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json  required

Created tag object.

|     |     |
| --- | --- |
| name<br>required | string |

### Responses

**201**

A tag object

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

**409**

Conflict

post/tags

https://docs.n8n.io/api/v1/tags

### Request samples

- Payload

Content type

application/json

Copy

`{
"name": "Production"}`

### Response samples

- 201

Content type

application/json

Copy

`{
"id": "2tUt1wbLX592XDdX",
"name": "Production",
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z"}`

## [tag/Tags/paths/~1tags/get](https://docs.n8n.io/api/api-reference/\#tag/Tags/paths/~1tags/get) Retrieve all tags

Retrieve all tags from your instance.

##### Authorizations:

_ApiKeyAuth_

##### query Parameters

|     |     |
| --- | --- |
| limit | number <= 250 <br>Default: 100<br>Example: limit=100<br>The maximum number of items to return. |
| cursor | string<br>Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

get/tags

https://docs.n8n.io/api/v1/tags

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"data": [\
{\
"id": "2tUt1wbLX592XDdX",\
"name": "Production",\
"createdAt": "2019-08-24T14:15:22Z",\
"updatedAt": "2019-08-24T14:15:22Z"}],
"nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"}`

## [tag/Tags/paths/~1tags~1{id}/get](https://docs.n8n.io/api/api-reference/\#tag/Tags/paths/~1tags~1{id}/get) Retrieves a tag

Retrieves a tag.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the tag. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**404**

The specified resource was not found.

get/tags/{id}

https://docs.n8n.io/api/v1/tags/{id}

### Response samples

- 200

Content type

application/json

Copy

`{
"id": "2tUt1wbLX592XDdX",
"name": "Production",
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z"}`

## [tag/Tags/paths/~1tags~1{id}/delete](https://docs.n8n.io/api/api-reference/\#tag/Tags/paths/~1tags~1{id}/delete) Delete a tag

Deletes a tag.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the tag. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

**403**

Forbidden

**404**

The specified resource was not found.

delete/tags/{id}

https://docs.n8n.io/api/v1/tags/{id}

### Response samples

- 200

Content type

application/json

Copy

`{
"id": "2tUt1wbLX592XDdX",
"name": "Production",
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z"}`

## [tag/Tags/paths/~1tags~1{id}/put](https://docs.n8n.io/api/api-reference/\#tag/Tags/paths/~1tags~1{id}/put) Update a tag

Update a tag.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the tag. |

##### Request Body schema: application/json  required

Updated tag object.

|     |     |
| --- | --- |
| name<br>required | string |

### Responses

**200**

Tag object

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

**404**

The specified resource was not found.

**409**

Conflict

put/tags/{id}

https://docs.n8n.io/api/v1/tags/{id}

### Request samples

- Payload

Content type

application/json

Copy

`{
"name": "Production"}`

### Response samples

- 200

Content type

application/json

Copy

`{
"id": "2tUt1wbLX592XDdX",
"name": "Production",
"createdAt": "2019-08-24T14:15:22Z",
"updatedAt": "2019-08-24T14:15:22Z"}`

## [tag/SourceControl](https://docs.n8n.io/api/api-reference/\#tag/SourceControl) SourceControl

Operations about source control

## [tag/SourceControl/paths/~1source-control~1pull/post](https://docs.n8n.io/api/api-reference/\#tag/SourceControl/paths/~1source-control~1pull/post) Pull changes from the remote repository

Requires the Source Control feature to be licensed and connected to a repository.

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json  required

Pull options

|     |     |
| --- | --- |
| force | boolean |
| variables | object |

### Responses

**200**

Import result

**400**

The request is invalid or provides malformed data.

**409**

Conflict

post/source-control/pull

https://docs.n8n.io/api/v1/source-control/pull

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"force": true,
"variables": {
"foo": "bar"}}`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"variables": {
"added": [\
"string"],
"changed": [\
"string"]},
"credentials": [\
{\
"id": "string",\
"name": "string",\
"type": "string"}],
"workflows": [\
{\
"id": "string",\
"name": "string"}],
"tags": {
"tags": [\
{\
"id": "string",\
"name": "string"}],
"mappings": [\
{\
"workflowId": "string",\
"tagId": "string"}]}}`

## [tag/Variables](https://docs.n8n.io/api/api-reference/\#tag/Variables) Variables

Operations about variables

## [tag/Variables/paths/~1variables/post](https://docs.n8n.io/api/api-reference/\#tag/Variables/paths/~1variables/post) Create a variable

Create a variable in your instance.

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json  required

Payload for variable to create.

|     |     |
| --- | --- |
| key<br>required | string |
| value<br>required | string |

### Responses

**201**

Operation successful.

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

post/variables

https://docs.n8n.io/api/v1/variables

### Request samples

- Payload

Content type

application/json

Copy

`{
"key": "string",
"value": "test"}`

## [tag/Variables/paths/~1variables/get](https://docs.n8n.io/api/api-reference/\#tag/Variables/paths/~1variables/get) Retrieve variables

Retrieve variables from your instance.

##### Authorizations:

_ApiKeyAuth_

##### query Parameters

|     |     |
| --- | --- |
| limit | number <= 250 <br>Default: 100<br>Example: limit=100<br>The maximum number of items to return. |
| cursor | string<br>Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

get/variables

https://docs.n8n.io/api/v1/variables

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"data": [\
{\
"id": "string",\
"key": "string",\
"value": "test",\
"type": "string"}],
"nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"}`

## [tag/Variables/paths/~1variables~1{id}/delete](https://docs.n8n.io/api/api-reference/\#tag/Variables/paths/~1variables~1{id}/delete) Delete a variable

Delete a variable from your instance.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the variable. |

### Responses

**204**

Operation successful.

**401**

Unauthorized

**404**

The specified resource was not found.

delete/variables/{id}

https://docs.n8n.io/api/v1/variables/{id}

## [tag/Variables/paths/~1variables~1{id}/put](https://docs.n8n.io/api/api-reference/\#tag/Variables/paths/~1variables~1{id}/put) Update a variable

Update a variable from your instance.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| id<br>required | string<br>The ID of the variable. |

##### Request Body schema: application/json  required

Updated variable object.

|     |     |
| --- | --- |
| key<br>required | string |
| value<br>required | string |

### Responses

**204**

Operation successful.

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

**403**

Forbidden

**404**

The specified resource was not found.

put/variables/{id}

https://docs.n8n.io/api/v1/variables/{id}

### Request samples

- Payload

Content type

application/json

Copy

`{
"key": "string",
"value": "test"}`

## [tag/Projects](https://docs.n8n.io/api/api-reference/\#tag/Projects) Projects

Operations about projects

## [tag/Projects/paths/~1projects/post](https://docs.n8n.io/api/api-reference/\#tag/Projects/paths/~1projects/post) Create a project

Create a project in your instance.

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json  required

Payload for project to create.

|     |     |
| --- | --- |
| name<br>required | string |

### Responses

**201**

Operation successful.

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

post/projects

https://docs.n8n.io/api/v1/projects

### Request samples

- Payload

Content type

application/json

Copy

`{
"name": "string"}`

## [tag/Projects/paths/~1projects/get](https://docs.n8n.io/api/api-reference/\#tag/Projects/paths/~1projects/get) Retrieve projects

Retrieve projects from your instance.

##### Authorizations:

_ApiKeyAuth_

##### query Parameters

|     |     |
| --- | --- |
| limit | number <= 250 <br>Default: 100<br>Example: limit=100<br>The maximum number of items to return. |
| cursor | string<br>Paginate by setting the cursor parameter to the nextCursor attribute returned by the previous request's response. Default value fetches the first "page" of the collection. See pagination for more detail. |

### Responses

**200**

Operation successful.

**401**

Unauthorized

get/projects

https://docs.n8n.io/api/v1/projects

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"data": [\
{\
"id": "string",\
"name": "string",\
"type": "string"}],
"nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"}`

## [tag/Projects/paths/~1projects~1{projectId}/delete](https://docs.n8n.io/api/api-reference/\#tag/Projects/paths/~1projects~1{projectId}/delete) Delete a project

Delete a project from your instance.

##### Authorizations:

_ApiKeyAuth_

##### path Parameters

|     |     |
| --- | --- |
| projectId<br>required | string<br>The ID of the project. |

### Responses

**204**

Operation successful.

**401**

Unauthorized

**403**

Forbidden

**404**

The specified resource was not found.

delete/projects/{projectId}

https://docs.n8n.io/api/v1/projects/{projectId}

## [tag/Project](https://docs.n8n.io/api/api-reference/\#tag/Project) Project

## [tag/Project/paths/~1projects~1{projectId}/put](https://docs.n8n.io/api/api-reference/\#tag/Project/paths/~1projects~1{projectId}/put) Update a project

Update a project.

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json  required

Updated project object.

|     |     |
| --- | --- |
| name<br>required | string |

### Responses

**204**

Operation successful.

**400**

The request is invalid or provides malformed data.

**401**

Unauthorized

**403**

Forbidden

**404**

The specified resource was not found.

put/projects/{projectId}

https://docs.n8n.io/api/v1/projects/{projectId}

### Request samples

- Payload

Content type

application/json

Copy

`{
"name": "string"}`

Back to top