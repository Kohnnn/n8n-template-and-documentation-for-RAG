---
url: "https://docs.n8n.io/code/cookbook/builtin/itemmatching/"
title: "Retrieve linked items from earlier in the workflow | n8n Docs  "
---

").itemMatching(currentNodeinputIndex)\`">



 Retrieve linked items from earlier in the workflow \| n8n Docs

[Skip to content](https://docs.n8n.io/code/cookbook/builtin/itemmatching/#retrieve-linked-items-from-earlier-in-the-workflow)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/builtin/itemmatching.md "Edit this page")

# Retrieve linked items from earlier in the workflow [\#](https://docs.n8n.io/code/cookbook/builtin/itemmatching/\#retrieve-linked-items-from-earlier-in-the-workflow "Permanent link")

Every item in a node's input data links back to the items used in previous nodes to generate it. This is useful if you need to retrieve linked items from further back than the immediate previous node.

To access the linked items from earlier in the workflow, use `("<node-name>").itemMatching(currentNodeinputIndex)`.

For example, consider a workflow that does the following:

1. The Customer Datastore node generates example data:



|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>``` | ```<br>[<br>	{<br>		"id": "23423532",<br>		"name": "Jay Gatsby",<br>		"email": "gatsby@west-egg.com",<br>		"notes": "Keeps asking about a green light??",<br>		"country": "US",<br>		"created": "1925-04-10"<br>	},<br>	{<br>		"id": "23423533",<br>		"name": "José Arcadio Buendía",<br>		"email": "jab@macondo.co",<br>		"notes": "Lots of people named after him. Very confusing",<br>		"country": "CO",<br>		"created": "1967-05-05"<br>	},<br>	...<br>]<br>``` |

2. The Edit Fields node simplifies this data:



|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>``` | ```<br>[<br>	{<br>		"name": "Jay Gatsby"<br>	},<br>	{<br>		"name": "José Arcadio Buendía"<br>	},<br>    ...<br>]<br>``` |

3. The Code node restore the email address to the correct person:



|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br>[<br>	{<br>		"name": "Jay Gatsby",<br>		"restoreEmail": "gatsby@west-egg.com"<br>	},<br>	{<br>		"name": "José Arcadio Buendía",<br>		"restoreEmail": "jab@macondo.co"<br>	},<br>	...<br>]<br>``` |


The Code node does this using the following code:

[JavaScript](https://docs.n8n.io/code/cookbook/builtin/itemmatching/#__tabbed_1_1)[Python](https://docs.n8n.io/code/cookbook/builtin/itemmatching/#__tabbed_1_2)

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>``` | ```<br>for(let i=0; i<$input.all().length; i++) {<br>	$input.all()[i].json.restoreEmail = $('Customer Datastore (n8n training)').itemMatching(i).json.email;<br>}<br>return $input.all();<br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>``` | ```<br>for i,item in enumerate(_input.all()):<br>	_input.all()[i].json.restoreEmail = _('Customer Datastore (n8n training)').itemMatching(i).json.email<br>return _input.all();<br>``` |

You can view and download the example workflow from [n8n website \| itemMatchin usage example](https://n8n.io/workflows/1966-itemmatching-usage-example/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top