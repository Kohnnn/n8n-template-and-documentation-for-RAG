---
url: "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues/"
title: "Notion node common issues | n8n Docs "
---

[Skip to content](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues/#notion-node-common-issues)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues.md "Edit this page")

# Notion node common issues [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues/\#notion-node-common-issues "Permanent link")

Here are some common errors and issues with the [Notion node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/) and steps to resolve or troubleshoot them.

## Relation property not displaying [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues/\#relation-property-not-displaying "Permanent link")

The Notion node only supports displaying the data relation property for [two-way relations](https://www.notion.com/help/relations-and-rollups). When you connect two Notion databases with a two-way relationship, you can select or filter by the relation property when working with the Notion node's **Database Page** resource.

To enable two-way relations, edit the relation property in Notion and enable the **Show on \[name of related database\]** option to create a reverse relation. Select a name to use for the relation in the new context. The relation is now accessible in n8n when filtering or selecting.

If you need to work with Notion databases with one-way relationship, you can use the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) with your existing Notion credentials. For example, to update a one-way relationship, you can send a `PATCH` request to the following URL:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>https://api.notion.com/v1/pages/<page_id><br>``` |

Enable **Send Body**, set the **Body Content Type** to **JSON**, and set **Specify Body** to **Using JSON**. Afterward, you can enter a JSON object like the following into the **JSON** field:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br>{<br>	"properties": {<br>		"Account": {<br>			"relation": [<br>				{<br>					"id": "<your_relation_ID>"<br>				}<br>			]<br>		}<br>	}<br>}<br>``` |

## Create toggle heading [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues/\#create-toggle-heading "Permanent link")

The Notion node allows you to create headings and toggles when adding blocks to **Page**, **Database Page**, or **Block** resources. Creating toggleable headings isn't yet supported by the Notion node itself.

You can work around this be creating a regular heading and then modifying it to enable the [`is_toggleable` property](https://developers.notion.com/reference/block#headings):

01. Add a heading with Notion node.
02. Select the resource you want to add a heading to:
    - To add a new page with a heading, select the **Page** or **Database Page** resources with the **Create** operation.
    - To add a heading to an existing page, select the **Block** resource with the **Append After** operation.
03. Select **Add Block** and set the **Type Name or ID** to either **Heading 1**, **Heading 2**, or **Heading 3**.
04. Add an [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/) node connected to the Notion node and select the `GET` method.
05. Set the **URL** to `https://api.notion.com/v1/blocks/<block_ID>`. For example, if your added the heading to an existing page, you could use the following URL: `https://api.notion.com/v1/blocks/{{ $json.results[0].id }}`. If you created a new page instead of appending a block, you may need to discover the block ID by querying the page contents first.
06. Select **Predefined Credential Type** and connect your existing Notion credentials.
07. Add an [Edit Fields (Set)](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/) node after the HTTP Request node.
08. Add `heading_1.is_toggleable` as a new **Boolean** field set to `true`. Swap `heading_1` for a different heading number as necessary.
09. Add a second HTTP Request node after the Edit Fields (Set) node.
10. Set the **Method** to `PATCH` and use `https://api.notion.com/v1/blocks/{{ $json.id }}` as the **URL** value.
11. Select **Predefined Credential Type** and connect your existing Notion credentials.
12. Enable **Send Body** and set a parameter.
13. Set the parameter **Name** to `heading_1` (substitute `heading_1` for the heading level you are using).
14. Set the parameter **Value** to `{{ $json.heading_1 }}` (substitute `heading_1` for the heading level you are using).

The above sequence will create a regular heading block. It will query the newly created header, add the `is_toggleable` property, and update the heading block.

## Handle null and empty values [\#](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues/\#handle-null-and-empty-values "Permanent link")

You may receive a validation error when working with the Notion node if you submit fields with empty or null values. This can occur any time you populate fields from previous nodes when that data is missing.

To work around this, check for the existence of the field data before sending it to Notion or use a default value.

To check for the data before executing the Notion node, use an [If](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if/) node to check whether the field is unset. This allows you to use the [Edit Fields (Set)](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/) node to conditionally remove the field when it doesn't have a valid value.

As an alternative, you can set a [default value](https://docs.n8n.io/code/cookbook/expressions/check-incoming-data/) if the incoming data doesn't provide one.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top