---
url: "https://docs.n8n.io/data/data-structure/"
title: "Data structure | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/data/data-structure/#data-structure)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-structure.md "Edit this page")

# Data structure [\#](https://docs.n8n.io/data/data-structure/\#data-structure "Permanent link")

In n8n, all data passed between nodes is an array of objects. It has the following structure:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>``` | ```<br>[<br>	{<br>		// For most data:<br>		// Wrap each item in another object, with the key 'json'<br>		"json": {<br>			// Example data<br>			"apple": "beets",<br>			"carrot": {<br>				"dill": 1<br>			}<br>		},<br>		// For binary data:<br>		// Wrap each item in another object, with the key 'binary'<br>		"binary": {<br>			// Example data<br>			"apple-picture": {<br>				"data": "....", // Base64 encoded binary data (required)<br>				"mimeType": "image/png", // Best practice to set if possible (optional)<br>				"fileExtension": "png", // Best practice to set if possible (optional)<br>				"fileName": "example.png", // Best practice to set if possible (optional)<br>			}<br>		}<br>	},<br>]<br>``` |

Skipping the `json` key and array syntax

From 0.166.0 on, when using the Function node or Code node, n8n automatically adds the `json` key if it's missing. It also automatically wraps your items in an array ( `[]`) if needed. This is only the case when using the Function or Code nodes. When building your own nodes, you must still make sure the node returns data with the `json` key.

## Data item processing [\#](https://docs.n8n.io/data/data-structure/\#data-item-processing "Permanent link")

Nodes can process multiple items.

For example, if you set the Trello node to `Create-Card`, and create an expression that sets `Name` using a property called `name-input-value` from the incoming data, the node creates a card for each item, always choosing the `name-input-value` of the current item.

For example, this input will create two cards. One named `test1` the other one named `test2`:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>``` | ```<br>[<br>	{<br>		name-input-value: "test1"<br>	},<br>	{<br>		name-input-value: "test2"<br>	}<br>]<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top