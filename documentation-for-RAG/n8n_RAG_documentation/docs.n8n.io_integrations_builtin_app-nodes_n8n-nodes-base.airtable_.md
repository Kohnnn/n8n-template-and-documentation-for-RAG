---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/"
title: "Airtable node documentation | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/#airtable-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.airtable/index.md "Edit this page")

# Airtable node [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#airtable-node "Permanent link")

Use the Airtable node to automate work in Airtable, and integrate Airtable with other applications. n8n has built-in support for a wide range of Airtable features, including creating, reading, listing, updating and deleting tables.

On this page, you'll find a list of operations the Airtable node supports and links to more resources.

Credentials

Refer to [Airtable credentials](https://docs.n8n.io/integrations/builtin/credentials/airtable/) for guidance on setting up authentication.

## Operations [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#operations "Permanent link")

- Append the data to a table
- Delete data from a table
- List data from a table
- Read data from a table
- Update data in a table

## Templates and examples [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#templates-and-examples "Permanent link")

**Handling Appointment Leads and Follow-up With Twilio, Cal.com and AI**

by Jimleuk

[View template details](https://n8n.io/workflows/2342-handling-appointment-leads-and-follow-up-with-twilio-calcom-and-ai/)

**AI-Powered Social Media Amplifier**

by Mudit Juneja

[View template details](https://n8n.io/workflows/2681-ai-powered-social-media-amplifier/)

**Technical stock analysis with Telegram, Airtable and a GPT-powered AI Agent**

by Mark Shcherbakov

[View template details](https://n8n.io/workflows/3053-technical-stock-analysis-with-telegram-airtable-and-a-gpt-powered-ai-agent/)

[Browse Airtable integration templates](https://n8n.io/integrations/airtable/), or [search all templates](https://n8n.io/workflows/)

## Related resources [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#related-resources "Permanent link")

n8n provides a trigger node for Airtable. You can find the trigger node docs [here](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger/).

Refer to [Airtable's documentation](https://airtable.com/developers/web/api/introduction) for more information about the service.

## What to do if your operation isn't supported [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#what-to-do-if-your-operation-isnt-supported "Permanent link")

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1. In the HTTP Request node, select **Authentication** \> **Predefined Credential Type**.
2. Select the service you want to connect to.
3. Select your credential.

Refer to [Custom API operations](https://docs.n8n.io/integrations/custom-operations/) for more information.

## Node reference [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#node-reference "Permanent link")

### Get the Record ID [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#get-the-record-id "Permanent link")

To fetch data for a particular record, you need the Record ID. There are two ways to get the Record ID.

### Create a Record ID column in Airtable [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#create-a-record-id-column-in-airtable "Permanent link")

To create a `Record ID` column in your table, refer to this [article](https://support.airtable.com/docs/finding-airtable-ids). You can then use this Record ID in your Airtable node.

### Use the List operation [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#use-the-list-operation "Permanent link")

To get the Record ID of your record, you can use the **List** operation of the Airtable node. This operation will return the Record ID along with the fields. You can then use this Record ID in your Airtable node.

### Filter records when using the List operation [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#filter-records-when-using-the-list-operation "Permanent link")

To filter records from your Airtable base, use the **Filter By Formula** option. For example, if you want to return all the users that belong to the organization `n8n`, follow the steps mentioned below:

1. Select 'List' from the **Operation** dropdown list.
2. Enter the base ID and the table name in the **Base ID** and **Table** field, respectively.
3. Click on **Add Option** and select 'Filter By Formula' from the dropdown list.
4. Enter the following formula in the **Filter By Formula** field: `{Organization}='n8n'`.

Similarly, if you want to return all the users that don't belong to the organization `n8n`, use the following formula: `NOT({Organization}='n8n')`.

Refer to the Airtable [documentation](https://support.airtable.com/hc/en-us/articles/203255215-Formula-Field-Reference) to learn more about the formulas.

## Common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/\#common-issues "Permanent link")

For common errors or issues and suggested resolution steps, refer to [Common Issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top