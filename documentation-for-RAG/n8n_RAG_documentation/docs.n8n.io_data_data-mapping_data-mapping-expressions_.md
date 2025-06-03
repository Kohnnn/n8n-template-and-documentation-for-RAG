---
url: "https://docs.n8n.io/data/data-mapping/data-mapping-expressions/"
title: "Data mapping in the expressions editor | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/data/data-mapping/data-mapping-expressions/#mapping-in-the-expressions-editor)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-mapping/data-mapping-expressions.md "Edit this page")

# Mapping in the expressions editor [\#](https://docs.n8n.io/data/data-mapping/data-mapping-expressions/\#mapping-in-the-expressions-editor "Permanent link")

These examples show how to access linked items in the expressions editor. Refer to [expressions](https://docs.n8n.io/code/expressions/) for more information on expressions, including built in variables and methods.

For information on errors with mapping and linking items, refer to [Item linking errors](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-errors/).

## Access the linked item in a previous node's output [\#](https://docs.n8n.io/data/data-mapping/data-mapping-expressions/\#access-the-linked-item-in-a-previous-nodes-output "Permanent link")

When you use this, n8n works back up the item linking chain, to find the parent item in the given node.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>// Returns the linked item<br>{{$("<node-name>").item}}<br>``` |

As a longer example, consider a scenario where a node earlier in the workflow has the following output data:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>``` | ```<br>[<br>  {<br>    "id": "23423532",<br>    "name": "Jay Gatsby",<br>  },<br>  {<br>    "id": "23423533",<br>    "name": "José Arcadio Buendía",<br>  },<br>  {<br>    "id": "23423534",<br>    "name": "Max Sendak",<br>  },<br>  {<br>    "id": "23423535",<br>    "name": "Zaphod Beeblebrox",<br>  },<br>  {<br>    "id": "23423536",<br>    "name": "Edmund Pevensie",<br>  }<br>]<br>``` |

To extract the name, use the following expression:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>{{$("<node-name>").item.json.name}}<br>``` |

### Access the linked item in the current node's input [\#](https://docs.n8n.io/data/data-mapping/data-mapping-expressions/\#access-the-linked-item-in-the-current-nodes-input "Permanent link")

In this case, the item linking is within the node: find the input item that the node links to an output item.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>// Returns the linked item<br>{{$input.item}}<br>``` |

As a longer example, consider a scenario where the current node has the following input data:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>``` | ```<br>[<br>  {<br>    "id": "23423532",<br>    "name": "Jay Gatsby",<br>  },<br>  {<br>    "id": "23423533",<br>    "name": "José Arcadio Buendía",<br>  },<br>  {<br>    "id": "23423534",<br>    "name": "Max Sendak",<br>  },<br>  {<br>    "id": "23423535",<br>    "name": "Zaphod Beeblebrox",<br>  },<br>  {<br>    "id": "23423536",<br>    "name": "Edmund Pevensie",<br>  }<br>]<br>``` |

To extract the name, you'd normally use drag-and-drop [Data mapping](https://docs.n8n.io/data/data-mapping/), but you could also write the following expression:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>{{$input.item.json.name}}<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top