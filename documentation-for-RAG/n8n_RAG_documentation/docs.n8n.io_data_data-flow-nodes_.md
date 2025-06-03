---
url: "https://docs.n8n.io/data/data-flow-nodes/"
title: "Data flow within nodes | n8n Docs "
---

[Skip to content](https://docs.n8n.io/data/data-flow-nodes/#data-flow-within-nodes)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-flow-nodes.md "Edit this page")

# Data flow within nodes [\#](https://docs.n8n.io/data/data-flow-nodes/\#data-flow-within-nodes "Permanent link")

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