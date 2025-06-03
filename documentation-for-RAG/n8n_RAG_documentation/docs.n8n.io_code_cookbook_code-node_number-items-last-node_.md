---
url: "https://docs.n8n.io/code/cookbook/code-node/number-items-last-node/"
title: "Get number of items returned by last node | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/cookbook/code-node/number-items-last-node/#get-number-of-items-returned-by-the-previous-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/code-node/number-items-last-node.md "Edit this page")

# Get number of items returned by the previous node [\#](https://docs.n8n.io/code/cookbook/code-node/number-items-last-node/\#get-number-of-items-returned-by-the-previous-node "Permanent link")

To get the number of items returned by the previous node:

[JavaScript](https://docs.n8n.io/code/cookbook/code-node/number-items-last-node/#__tabbed_1_1)[Python](https://docs.n8n.io/code/cookbook/code-node/number-items-last-node/#__tabbed_1_2)

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>``` | ```<br>if (Object.keys(items[0].json).length === 0) {<br>return [<br>	{<br>		json: {<br>			results: 0,<br>		}<br>	}<br>]<br>}<br>return [<br>	{<br>		json: {<br>			results: items.length,<br>		}<br>	}<br>];<br>``` |

The output will be similar to the following.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>``` | ```<br>[<br>	{<br>		"results": 8<br>	}<br>]<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>``` | ```<br>if len(items[0].json) == 0:<br>	return [<br>		{<br>			"json": {<br>				"results": 0,<br>			}<br>		}<br>	]<br>else:<br>	return [<br>		{<br>			"json": {<br>				"results": items.length,<br>			}<br>		}<br>	]<br>``` |

The output will be similar to the following.

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>``` | ```<br>[<br>	{<br>		"results": 8<br>	}<br>]<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top