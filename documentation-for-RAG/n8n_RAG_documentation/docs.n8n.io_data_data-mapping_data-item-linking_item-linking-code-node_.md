---
url: "https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-code-node/"
title: "Item linking in the Code node | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-code-node/#item-linking-in-the-code-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-mapping/data-item-linking/item-linking-code-node.md "Edit this page")

# Item linking in the Code node [\#](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-code-node/\#item-linking-in-the-code-node "Permanent link")

Use n8n's item linking to access data from items that precede the current item. It also has implications when using the Code node. Most nodes link every output item to an input item. This creates a chain of items that you can work back along to access previous items. For a deeper conceptual overview of this topic, refer to [Item linking concepts](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts/). This document focuses on practical usage examples.

When using the Code node, there are some scenarios where you need to manually supply item linking information if you want to be able to use `$("<node-name>").item` later in the workflow. All these scenarios only apply if you have more than one incoming item. n8n automatically handles item linking for single items.

These scenarios are when you:

- Add new items: the new items aren't linked to any input.
- Return new items.
- Want to manually control the item linking.

[n8n's automatic item linking](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts/) handles the other scenarios.

To control item linking, set `pairedItem` when returning data. For example, to link to the item at index 0:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>[<br>	{<br>		"json": {<br>			. . . <br>		},<br>		// The index of the input item that generated this output item<br>		"pairedItem": 0<br>	}<br>]<br>``` |

### `pairedItem` usage example [\#](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-code-node/\#paireditem-usage-example "Permanent link")

Take this input data:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>``` | ```<br>[<br>  {<br>    "id": "23423532",<br>    "name": "Jay Gatsby"<br>  },<br>  {<br>    "id": "23423533",<br>    "name": "José Arcadio Buendía"<br>  },<br>  {<br>    "id": "23423534",<br>    "name": "Max Sendak"<br>  },<br>  {<br>    "id": "23423535",<br>    "name": "Zaphod Beeblebrox"<br>  },<br>  {<br>    "id": "23423536",<br>    "name": "Edmund Pevensie"<br>  }<br>]<br>``` |

And use it to generate new items, containing just the name, along with a new piece of data:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>``` | ```<br>newItems = [];<br>for(let i=0; i<items.length; i++){<br>  newItems.push(<br>    {<br>    "json":<br>      {<br>        "name": items[i].json.name,<br>				"aBrandNewField": "New data for item " + i<br>      }<br>    }<br>  )<br>}<br>return newItems;<br>``` |

`newItems` is an array of items with no `pairedItem`. This means there's no way to trace back from these items to the items used to generate them.

Add the `pairedItem` object:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>``` | ```<br>newItems = [];<br>for(let i=0; i<items.length; i++){<br>  newItems.push(<br>    {<br>      "json":<br>        {<br>          "name": items[i].json.name,<br>					"aBrandNewField": "New data for item " + i<br>        },<br>      "pairedItem": i<br>    }    <br>  )<br>}<br>return newItems;<br>``` |

Each new item now links to the item used to create it.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top