---
url: "https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-node-building/"
title: "Item linking for node creators | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-node-building/#item-linking-for-node-creators)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-mapping/data-item-linking/item-linking-node-building.md "Edit this page")

# Item linking for node creators [\#](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-node-building/\#item-linking-for-node-creators "Permanent link")

Programmatic-style nodes only

This guidance applies to programmatic-style nodes. If you're using declarative style, n8n handles paired items for you automatically.

Use n8n's item linking to access data from items that precede the current item. n8n needs to know which input item a given output item comes from. If this information is missing, expressions in other nodes may break. As a node developer, you must ensure any items returned by your node support this.

This applies to programmatic nodes (including trigger nodes). You don't need to consider item linking when building a declarative-style node. Refer to [Choose your node building approach](https://docs.n8n.io/integrations/creating-nodes/plan/choose-node-method/) for more information on node styles.

Start by reading [Item linking concepts](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts/), which provides a conceptual overview of item linking, and details of the scenarios where n8n can handle the linking automatically.

If you need to handle item linking manually, do this by setting `pairedItem` on each item your node returns:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>``` | ```<br>// Use the pairedItem information of the incoming item<br>newItem = {<br>	"json": { . . . },<br>	"pairedItem": {<br>		"item": item.pairedItem,<br>		// Optional: choose the input to use<br>		// Set this if your node combines multiple inputs<br>		"input": 0<br>};<br>// Or set the index manually<br>newItem = {<br>		"json": { . . . }<br>		"pairedItem": {<br>			"item": i,<br>			// Optional: choose the input to use<br>			// Set this if your node combines multiple inputs<br>			"input": 0<br>		},<br>};<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top