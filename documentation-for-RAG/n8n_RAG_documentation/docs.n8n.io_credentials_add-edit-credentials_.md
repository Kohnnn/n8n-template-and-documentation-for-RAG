---
url: "https://docs.n8n.io/credentials/add-edit-credentials/"
title: "Create and edit | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/credentials/add-edit-credentials/#create-and-edit-credentials)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/credentials/add-edit-credentials.md "Edit this page")

# Create and edit credentials [\#](https://docs.n8n.io/credentials/add-edit-credentials/\#create-and-edit-credentials "Permanent link")

Credentials are securely stored authentication information used to connect n8n workflows to external services such as APIs, or databases.

## Create a credential [\#](https://docs.n8n.io/credentials/add-edit-credentials/\#create-a-credential "Permanent link")

1. Select the ![universal create resource icon](https://docs.n8n.io/_images/common-icons/universal-resource-button.png)**button** in the upper-left corner of the side menu. Select credential.
2. If your n8n instance supports [projects](https://docs.n8n.io/glossary/#project-n8n), you'll also need to choose whether to create the credential inside your personal space or a specific project you have access to. If you're using the community version, you'll create the credential inside your personal space.
3. Select the app or service you wish to connect to.

Or:

1. Using the ![universal create resource icon](https://docs.n8n.io/_images/common-icons/universal-resource-button.png)**Create** button in the upper-right corner from either the **Overview** page or a specific project. Select Credential.
2. If you're doing this from the **Overview** page, you'll create the credential inside your personal space. If you're doing this from inside a project, you'll create the credential inside that specific project.
3. Select the app or service you wish to connect to.

You can also create new credential in the credential drop down when editing a node on the workflow editor.

Once in the credential modal, enter the details required by your service. Refer to your service's page in the [credentials library](https://docs.n8n.io/integrations/builtin/credentials/) for guidance.

When you save a credential, n8n tests it to confirm it works.

Credentials naming

n8n names new credentials " _node name_ account" by default. You can rename the credentials by clicking on the name, similarly to renaming nodes. It's good practice to give them names that identify the app or service, type, and purpose of the credential. A naming convention makes it easier to keep track of and identify your credentials.

## Expressions in credentials [\#](https://docs.n8n.io/credentials/add-edit-credentials/\#expressions-in-credentials "Permanent link")

You can use [expressions](https://docs.n8n.io/glossary/#expression-n8n) to set credentials dynamically as your workflow runs:

1. In your workflow, find the data path containing the credential. This varies depending on the exact parameter names in your data. Make sure that the data containing the credential is available in the workflow when you get to the node that needs it.
2. When creating your credential, hover over the field where you want to use an expression.
3. Toggle **Expression** on.
4. Enter your expression.

### Example workflow [\#](https://docs.n8n.io/credentials/add-edit-credentials/\#example-workflow "Permanent link")

[View workflow file](https://docs.n8n.io/_workflows/credentials/dynamic_credentials_using_expressions.json)

#### Using the example [\#](https://docs.n8n.io/credentials/add-edit-credentials/\#using-the-example "Permanent link")

To load the template into your n8n instance:

1. Download the workflow JSON file.
2. Open a new workflow in your n8n instance.
3. Copy in the JSON, or select **Workflow menu**![Workflow menu icon](https://docs.n8n.io/_images/common-icons/three-dots-horizontal.png) \> **Import from file...**.

The example workflows use Sticky Notes to guide you:

- Yellow: notes and information.
- Green: instructions to run the workflow.
- Orange: you need to change something to make the workflow work.
- Blue: draws attention to a key feature of the example.