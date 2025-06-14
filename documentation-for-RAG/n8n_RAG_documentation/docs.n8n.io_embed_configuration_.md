---
url: "https://docs.n8n.io/embed/configuration/"
title: "n8n Embed Configuration | n8n Docs "
---

[Skip to content](https://docs.n8n.io/embed/configuration/#configuration)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/embed/configuration.md "Edit this page")

# Configuration [\#](https://docs.n8n.io/embed/configuration/\#configuration "Permanent link")

Feature availability

Embed requires an embed license. For more information about when to use Embed, as well as costs and licensing processes, refer to [Embed](https://n8n.io/embed/) on the n8n website.

## Authentication [\#](https://docs.n8n.io/embed/configuration/\#authentication "Permanent link")

You can secure n8n by setting up [User management](https://docs.n8n.io/user-management/), n8n's built-in authentication feature.

n8n supports [LDAP](https://docs.n8n.io/user-management/ldap/) and [SAML](https://docs.n8n.io/user-management/saml/).

### Credential overwrites [\#](https://docs.n8n.io/embed/configuration/\#credential-overwrites "Permanent link")

To offer OAuth login to users, it's possible to overwrite [credentials](https://docs.n8n.io/glossary/#credential-n8n) on a global basis. This credential data isn't visible to users but the backend uses it automatically.

In the Editor UI, n8n hides all overwritten fields by default. This means that users are able to authenticate using OAuth by pressing the "connect" button on the credentials.

n8n offers two ways to apply credential overwrites: using Environment Variable and using the REST API.

#### Using environment variables [\#](https://docs.n8n.io/embed/configuration/\#using-environment-variables "Permanent link")

You can set credential overwrites using environment variable by setting the `CREDENTIALS_OVERWRITE_DATA` to `{ CREDENTIAL_NAME: { PARAMETER: VALUE }}`.

Warning

Even though this is possible, it isn't recommended. Environment variables aren't protected in n8n, so the data can leak to users.

#### Using REST APIs [\#](https://docs.n8n.io/embed/configuration/\#using-rest-apis "Permanent link")

The recommended way is to load the data using a custom REST endpoint. Set the `CREDENTIALS_OVERWRITE_ENDPOINT` to a path under which this endpoint should be made available.

Note

The endpoints can be called just one at a time for security reasons.

For example:

1. Activate the endpoint by setting the environment variable in the environment n8n runs under:



|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>export CREDENTIALS_OVERWRITE_ENDPOINT=send-credentials<br>``` |

2. A JSON file with the credentials to overwrite is then needed. For example, a `oauth-credentials.json` file to overwrite credentials for Asana and GitHub could look like this:



|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>``` | ```<br>{<br>    "asanaOAuth2Api": {<br>        "clientId": "<id>",<br>        "clientSecret": "<secret>"<br>    },<br>    "githubOAuth2Api": {<br>        "clientId": "<id>",<br>        "clientSecret": "<secret>"<br>    }<br>}<br>``` |

3. Then apply it to the instance by sending it using curl:



|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>curl -H "Content-Type: application/json" --data @oauth-credentials.json http://localhost:5678/send-credentials<br>``` |


Note

There are cases when credentials are based on others. For example, the `googleSheetsOAuth2Api` extends the `googleOAuth2Api`.
In this case, you can set parameters on the parent credentials ( `googleOAuth2Api`) for all child-credentials ( `googleSheetsOAuth2Api`) to use.

## Environment variables [\#](https://docs.n8n.io/embed/configuration/\#environment-variables "Permanent link")

n8n has many [environment variables](https://docs.n8n.io/hosting/configuration/environment-variables/) you can configure. Here are the most relevant environment variables for your hosted solution:

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `EXECUTIONS_TIMEOUT` | Number | `-1` | Sets a default timeout (in seconds) to all workflows after which n8n stops their execution. Users can override this for individual workflows up to the duration set in `EXECUTIONS_TIMEOUT_MAX`. Set `EXECUTIONS_TIMEOUT` to `-1` to disable. |
| `EXECUTIONS_DATA_PRUNE` | Boolean | `true` | Whether to delete data of past executions on a rolling basis. |
| `EXECUTIONS_DATA_MAX_AGE` | Number | `336` | The execution age (in hours) before it's deleted. |
| `EXECUTIONS_DATA_PRUNE_MAX_COUNT` | Number | `10000` | Maximum number of executions to keep in the database. 0 = no limit |
| `NODES_EXCLUDE` | Array of strings | - | Specify which nodes not to load. For example, to block nodes that can be a security risk if users aren't trustworthy: `NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"` |
| `NODES_INCLUDE` | Array of strings | - | Specify which nodes to load. |
| `N8N_TEMPLATES_ENABLED` | Boolean | `true` | Enable [workflow templates](https://docs.n8n.io/glossary/#template-n8n) (true) or disable (false). |
| `N8N_TEMPLATES_HOST` | String | `https://api.n8n.io` | Change this if creating your own workflow template library. Note that to use your own workflow templates library, your API must provide the same endpoints and response structure as n8n's. Refer to [Workflow templates](https://docs.n8n.io/workflows/templates/) for more information. |

## Backend hooks [\#](https://docs.n8n.io/embed/configuration/\#backend-hooks "Permanent link")

It's possible to define external hooks that n8n executes whenever a specific operation runs. You can use these, for example, to log data, change data, or forbid an action by throwing an error.

### Available hooks [\#](https://docs.n8n.io/embed/configuration/\#available-hooks "Permanent link")

| Hook | Arguments | Description |
| --- | --- | --- |
| `credentials.create` | `[credentialData: ICredentialsDb]` | Called before new credentials get created. Use to restrict the number of credentials. |
| `credentials.delete` | `[id: credentialId]` | Called before credentials get deleted. |
| `credentials.update` | `[credentialData: ICredentialsDb]` | Called before existing credentials are saved. |
| `frontend.settings` | `[frontendSettings: IN8nUISettings]` | Gets called on n8n startup. Allows you to, for example, overwrite frontend data like the displayed OAuth URL. |
| `n8n.ready` | `[app: App]` | Called once n8n is ready. Use to, for example, register custom API endpoints. |
| `n8n.stop` |  | Called when an n8n process gets stopped. Allows you to save some process data. |
| `oauth1.authenticate` | `[oAuthOptions: clientOAuth1.Options, oauthRequestData: {oauth_callback: string}]` | Called before an OAuth1 authentication. Use to overwrite an OAuth callback URL. |
| `oauth2.callback` | `[oAuth2Parameters: {clientId: string, clientSecret: string \| undefined, accessTokenUri: string, authorizationUri: string, redirectUri: string, scopes: string[]}]` | Called in an OAuth2 callback. Use to overwrite an OAuth callback URL. |
| `workflow.activate` | `[workflowData: IWorkflowDb]` | Called before a workflow gets activated. Use to restrict the number of active workflows. |
| `workflow.afterDelete` | `[workflowId: string]` | Called after a workflow gets deleted. |
| `workflow.afterUpdate` | `[workflowData: IWorkflowBase]` | Called after an existing workflow gets saved. |
| `workflow.create` | `[workflowData: IWorkflowBase]` | Called before a workflow gets created. Use to restrict the number of saved workflows. |
| `workflow.delete` | `[workflowId: string]` | Called before a workflow gets delete. |
| `workflow.postExecute` | `[run: IRun, workflowData: IWorkflowBase]` | Called after a workflow gets executed. |
| `workflow.preExecute` | `[workflow: Workflow: mode: WorkflowExecuteMode]` | Called before a workflow gets executed. Allows you to count or limit the number of workflow executions. |
| `workflow.update` | `[workflowData: IWorkflowBase]` | Called before an existing workflow gets saved. |

### Registering hooks [\#](https://docs.n8n.io/embed/configuration/\#registering-hooks "Permanent link")

Set hooks by registering a hook file that contains the hook functions.
To register a hook, set the environment variable `EXTERNAL_HOOK_FILES`.

You can set the variable to a single file:

`EXTERNAL_HOOK_FILES=/data/hook.js`

Or to contain multiple files separated by a semicolon:

`EXTERNAL_HOOK_FILES=/data/hook1.js;/data/hook2.js`

### Backend hook files [\#](https://docs.n8n.io/embed/configuration/\#backend-hook-files "Permanent link")

Hook files are regular JavaScript files that have the following format:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>``` | ```<br>module.exports = {<br>    "frontend": {<br>        "settings": [<br>            async function (settings) {<br>                settings.oauthCallbackUrls.oauth1 = 'https://n8n.example.com/oauth1/callback';<br>                settings.oauthCallbackUrls.oauth2 = 'https://n8n.example.com/oauth2/callback';<br>            }<br>        ]<br>    },<br>    "workflow": {<br>        "activate": [<br>            async function (workflowData) {<br>                const activeWorkflows = await this.dbCollections.Workflow.count({ active: true });<br>                if (activeWorkflows > 1) {<br>                    throw new Error(<br>                        'Active workflow limit reached.'<br>                    );<br>                }<br>            }<br>        ]<br>    }<br>}<br>``` |

### Backend hook functions [\#](https://docs.n8n.io/embed/configuration/\#backend-hook-functions "Permanent link")

A hook or a hook file can contain multiple hook functions, with all functions executed one after another.

If the parameters of the hook function are objects, it's possible to change the data of that parameter to change the behavior of n8n.

You can also access the database in any hook function using `this.dbCollections` (refer to the code sample in [Backend hook files](https://docs.n8n.io/embed/configuration/#backend-hook-files).

## Frontend external hooks [\#](https://docs.n8n.io/embed/configuration/\#frontend-external-hooks "Permanent link")

Like backend external hooks, it's possible to define external hooks in the frontend code that get executed by n8n whenever a user performs a specific operation. You can use them, for example, to log data and change data.

### Available hooks [\#](https://docs.n8n.io/embed/configuration/\#available-hooks_1 "Permanent link")

| Hook | Description |
| --- | --- |
| `credentialsEdit.credentialTypeChanged` | Called when an existing credential's type changes. |
| `credentials.create` | Called when someone creates a new credential. |
| `credentialsList.dialogVisibleChanged` |  |
| `dataDisplay.nodeTypeChanged` |  |
| `dataDisplay.onDocumentationUrlClick` | Called when someone selects the help documentation link. |
| `execution.open` | Called when an existing execution opens. |
| `executionsList.openDialog` | Called when someone selects an execution from existing Workflow Executions. |
| `expressionEdit.itemSelected` |  |
| `expressionEdit.dialogVisibleChanged` |  |
| `nodeCreateList.filteredNodeTypesComputed` |  |
| `nodeCreateList.nodeFilterChanged` | Called when someone makes any changes to the node panel filter. |
| `nodeCreateList.selectedTypeChanged` |  |
| `nodeCreateList.mounted` |  |
| `nodeCreateList.destroyed` |  |
| `nodeSettings.credentialSelected` |  |
| `nodeSettings.valueChanged` |  |
| `nodeView.createNodeActiveChanged` |  |
| `nodeView.addNodeButton` |  |
| `nodeView.createNodeActiveChanged` |  |
| `nodeView.mount` |  |
| `pushConnection.executionFinished` |  |
| `showMessage.showError` |  |
| `runData.displayModeChanged` |  |
| `workflow.activeChange` |  |
| `workflow.activeChangeCurrent` |  |
| `workflow.afterUpdate` | Called when someone updates an existing workflow. |
| `workflow.open` |  |
| `workflowRun.runError` |  |
| `workflowRun.runWorkflow` | Called when a workflow executes. |
| `workflowSettings.dialogVisibleChanged` |  |
| `workflowSettings.saveSettings` | Called when someone saves the settings of a workflow. |

### Registering hooks [\#](https://docs.n8n.io/embed/configuration/\#registering-hooks_1 "Permanent link")

You can set hooks by loading the hooks script on the page. One way to do this is by creating a hooks file in the project and adding a script tag in your `editor-ui/public/index.html` file:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br><script src="frontend-hooks.js"></script><br>``` |

### Frontend hook files [\#](https://docs.n8n.io/embed/configuration/\#frontend-hook-files "Permanent link")

Frontend external hook files are regular JavaScript files which have the following format:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>``` | ```<br>window.n8nExternalHooks = {<br>  nodeView: {<br>    mount: [<br>      function (store, meta) {<br>        // do something<br>      },<br>    ],<br>    createNodeActiveChanged: [<br>      function (store, meta) {<br>        // do something<br>      },<br>      function (store, meta) {<br>        // do something else<br>      },<br>    ],<br>    addNodeButton: [<br>      function (store, meta) {<br>        // do something<br>      },<br>    ],<br>  },<br>};<br>``` |

### Frontend hook functions [\#](https://docs.n8n.io/embed/configuration/\#frontend-hook-functions "Permanent link")

You can define multiple hook functions per hook. Each hook function is invoked with the following arguments arguments:

- `store`: The Vuex store object. You can use this to change or get data from the store.
- `metadata`: The object that contains any data provided by the hook. To see what's passed, search for the hook in the `editor-ui` package.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top