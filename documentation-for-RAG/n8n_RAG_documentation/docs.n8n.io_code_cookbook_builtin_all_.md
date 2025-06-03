---
url: "https://docs.n8n.io/code/cookbook/builtin/all/"
title: "(node-name).all | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/cookbook/builtin/all/#node-nameallbranchindex-number-runindex-number)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/builtin/all.md "Edit this page")

# `("<node-name>").all(branchIndex?: number, runIndex?: number)` [\#](https://docs.n8n.io/code/cookbook/builtin/all/\#node-nameallbranchindex-number-runindex-number "Permanent link")

This gives access to all the items of the current or parent nodes. If you don't supply any parameters, it returns all the items of the current node.

## Getting items [\#](https://docs.n8n.io/code/cookbook/builtin/all/\#getting-items "Permanent link")

[JavaScript](https://docs.n8n.io/code/cookbook/builtin/all/#__tabbed_1_1)[Python](https://docs.n8n.io/code/cookbook/builtin/all/#__tabbed_1_2)

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br>// Returns all the items of the given node and current run<br>let allItems = $("<node-name>").all();<br>// Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)<br>let allItems = $("IF").all();<br>// Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)<br>let allItems = $("IF").all(0, $runIndex);<br>// Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)<br>let allItems = $("IF").all(1, 0);<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br># Returns all the items of the given node and current run<br>allItems = _("<node-name>").all();<br># Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)<br>allItems = _("IF").all();<br># Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)<br>allItems = _("IF").all(0, _runIndex);<br># Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)<br>allItems = _("IF").all(1, 0);<br>``` |

## Accessing item data [\#](https://docs.n8n.io/code/cookbook/builtin/all/\#accessing-item-data "Permanent link")

Get all items output by a previous node, and log out the data they contain:

[JavaScript](https://docs.n8n.io/code/cookbook/builtin/all/#__tabbed_2_1)[Python](https://docs.n8n.io/code/cookbook/builtin/all/#__tabbed_2_2)

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>``` | ```<br>previousNodeData = $("<node-name>").all();<br>for(let i=0; i<previousNodeData.length; i++) {<br>	console.log(previousNodeData[i].json);<br>}<br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>``` | ```<br>previousNodeData = _("<node-name>").all();<br>for item in previousNodeData:<br>	# item is of type <class 'pyodide.ffi.JsProxy'><br>	# You need to convert it to a Dict<br>	itemDict = item.json.to_py()<br>	print(itemDict)<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top