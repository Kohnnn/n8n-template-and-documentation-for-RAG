---
url: "https://docs.n8n.io/code/cookbook/jmespath/"
title: "Query JSON with JMESPath | n8n Docs "
---

[Skip to content](https://docs.n8n.io/code/cookbook/jmespath/#query-json-with-jmespath)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/jmespath.md "Edit this page")

# Query JSON with JMESPath [\#](https://docs.n8n.io/code/cookbook/jmespath/\#query-json-with-jmespath "Permanent link")

[JMESPath](https://jmespath.org/) is a query language for JSON that you can use to extract and transform elements from a JSON document. For full details of how to use JMESPath, refer to the [JMESPath documentation](https://jmespath.org/tutorial.html).

## The `jmespath()` method [\#](https://docs.n8n.io/code/cookbook/jmespath/\#the-jmespath-method "Permanent link")

n8n provides a custom method, `jmespath()`. Use this method to perform a search on a JSON object using the JMESPath query language.

The basic syntax is:

[JavaScript](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_1_1)[Python](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_1_2)

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>$jmespath(object, searchString)<br>``` |

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>_jmespath(object, searchString)<br>``` |

To help understand what the method does, here is the equivalent longer JavaScript:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>var jmespath = require('jmespath');<br>jmespath.search(object, searchString);<br>``` |

Expressions must be single-line

The longer code example doesn't work in Expressions, as they must be single-line.

`object` is a JSON object, such as the output of a previous node. `searchString` is an expression written in the JMESPath query language. The [JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification) provides a list of supported expressions, while their [Tutorial](https://jmespath.org/tutorial.html) and [Examples](https://jmespath.org/examples.html) provide interactive examples.

Search parameter order

The examples in the [JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification) follow the pattern `search(searchString, object)`. The [JMESPath JavaScript library](https://github.com/jmespath/jmespath.js/), which n8n uses, supports `search(object, searchString)` instead. This means that when using examples from the JMESPath documentation, you may need to change the order of the search function parameters.

## Common tasks [\#](https://docs.n8n.io/code/cookbook/jmespath/\#common-tasks "Permanent link")

This section provides examples for some common operations. More examples, and detailed guidance, are available in [JMESPath's own documentation](https://jmespath.org/tutorial.html).

When trying out these examples, you need to set the Code node **Mode** to **Run Once for Each Item**.

### Apply a JMESPath expression to a collection of elements with projections [\#](https://docs.n8n.io/code/cookbook/jmespath/\#apply-a-jmespath-expression-to-a-collection-of-elements-with-projections "Permanent link")

From the [JMESPath projections documentation](https://jmespath.org/tutorial.html#projections):

> Projections are one of the key features of JMESPath. Use it to apply an expression to a collection of elements. JMESPath supports five kinds of projections:
>
> - List Projections
> - Slice Projections
> - Object Projections
> - Flatten Projections
> - Filter Projections

The following example shows basic usage of list, slice, and object projections. Refer to the [JMESPath projections documentation](https://jmespath.org/tutorial.html#projections) for detailed explanations of each projection type, and more examples.

Given this JSON from a webhook node:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>``` | ```<br>[<br>  {<br>    "headers": {<br>      "host": "n8n.instance.address",<br>      ...<br>    },<br>    "params": {},<br>    "query": {},<br>    "body": {<br>      "people": [<br>        {<br>          "first": "James",<br>          "last": "Green"<br>        },<br>        {<br>          "first": "Jacob",<br>          "last": "Jones"<br>        },<br>        {<br>          "first": "Jayden",<br>          "last": "Smith"<br>        }<br>      ],<br>      "dogs": {<br>        "Fido": {<br>          "color": "brown",<br>          "age": 7<br>        },<br>        "Spot": {<br>          "color": "black and white",<br>          "age": 5<br>        }<br>      }<br>    }<br>  }<br>]<br>``` |

Retrieve a [list](https://jmespath.org/tutorial.html#list-and-slice-projections) of all the people's first names:

[Expressions (JavaScript)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_2_1)[Code node (JavaScript)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_2_2)[Code node (Python)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_2_3)

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>{{$jmespath($json.body.people, "[*].first" )}}<br>// Returns ["James", "Jacob", "Jayden"]<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>``` | ```<br>let firstNames = $jmespath($json.body.people, "[*].first" )<br>return {firstNames};<br>/* Returns:<br>[<br>	{<br>		"firstNames": [<br>			"James",<br>			"Jacob",<br>			"Jayden"<br>		]<br>	}<br>]<br>*/<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>``` | ```<br>firstNames = _jmespath(_json.body.people, "[*].first" )<br>return {"firstNames":firstNames}<br>"""<br>Returns:<br>[<br> 	{<br>		"firstNames": [<br>			"James",<br>			"Jacob",<br>			"Jayden"<br>		]<br>	}<br>]<br>"""<br>``` |

Get a [slice](https://jmespath.org/tutorial.html#list-and-slice-projections) of the first names:

[Expressions (JavaScript)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_3_1)[Code node (JavaScript)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_3_2)[Code node (Python)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_3_3)

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>{{$jmespath($json.body.people, "[:2].first")}}<br>// Returns ["James", "Jacob"]<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>``` | ```<br>let firstTwoNames = $jmespath($json.body.people, "[:2].first");<br>return {firstTwoNames};<br>/* Returns:<br>[<br>	{<br>		"firstNames": [<br>			"James",<br>			"Jacob",<br>			"Jayden"<br>		]<br>	}<br>]<br>*/<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>``` | ```<br>firstTwoNames = _jmespath(_json.body.people, "[:2].first" )<br>return {"firstTwoNames":firstTwoNames}<br>"""<br>Returns:<br>[<br>	{<br>		"firstTwoNames": [<br>		"James",<br>		"Jacob"<br>		]<br>	}<br>]<br>"""<br>``` |

Get a list of the dogs' ages using [object projections](https://jmespath.org/tutorial.html#object-projections):

[Expressions (JavaScript)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_4_1)[Code node (JavaScript)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_4_2)[Code node (Python)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_4_3)

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>{{$jmespath($json.body.dogs, "*.age")}}<br>// Returns [7,5]<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>``` | ```<br>let dogsAges = $jmespath($json.body.dogs, "*.age");<br>return {dogsAges};<br>/* Returns:<br>[<br>	{<br>		"dogsAges": [<br>			7,<br>			5<br>		]<br>	}<br>]<br>*/<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>``` | ```<br>dogsAges = _jmespath(_json.body.dogs, "*.age")<br>return {"dogsAges": dogsAges}<br>"""<br>Returns:<br>[<br>	{<br>		"dogsAges": [<br>			7,<br>			5<br>		]<br>	}<br>]<br>"""<br>``` |

### Select multiple elements and create a new list or object [\#](https://docs.n8n.io/code/cookbook/jmespath/\#select-multiple-elements-and-create-a-new-list-or-object "Permanent link")

Use [Multiselect](https://jmespath.org/tutorial.html#multiselect) to select elements from a JSON object and combine them into a new list or object.

Given this JSON from a webhook node:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>``` | ```<br>[<br>  {<br>    "headers": {<br>      "host": "n8n.instance.address",<br>      ...<br>    },<br>    "params": {},<br>    "query": {},<br>    "body": {<br>      "people": [<br>        {<br>          "first": "James",<br>          "last": "Green"<br>        },<br>        {<br>          "first": "Jacob",<br>          "last": "Jones"<br>        },<br>        {<br>          "first": "Jayden",<br>          "last": "Smith"<br>        }<br>      ],<br>      "dogs": {<br>        "Fido": {<br>          "color": "brown",<br>          "age": 7<br>        },<br>        "Spot": {<br>          "color": "black and white",<br>          "age": 5<br>        }<br>      }<br>    }<br>  }<br>]<br>``` |

Use multiselect list to get the first and last names and create new lists containing both names:

[Expressions (JavaScript)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_5_1)[Code node (JavaScript)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_5_2)[Code node (Python)](https://docs.n8n.io/code/cookbook/jmespath/#__tabbed_5_3)

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>{{$jmespath($json.body.people, "[].[first, last]")}}<br>// Returns [["James","Green"],["Jacob","Jones"],["Jayden","Smith"]]<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>``` | ```<br>let newList = $jmespath($json.body.people, "[].[first, last]");<br>return {newList};<br>/* Returns:<br>[<br>	{<br>		"newList": [<br>			[<br>				"James",<br>				"Green"<br>			],<br>			[<br>				"Jacob",<br>				"Jones"<br>			],<br>			[<br>				"Jayden",<br>				"Smith"<br>			]<br>		]<br>	}<br>]<br>*/<br>``` |

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>``` | ```<br>newList = _jmespath(_json.body.people, "[].[first, last]")<br>return {"newList":newList}<br>"""<br>Returns:<br>[<br>	{<br>		"newList": [<br>			[<br>				"James",<br>				"Green"<br>			],<br>			[<br>				"Jacob",<br>				"Jones"<br>			],<br>			[<br>				"Jayden",<br>				"Smith"<br>			]<br>		]<br>	}<br>]<br>"""<br>``` |

### An alternative to arrow functions in expressions [\#](https://docs.n8n.io/code/cookbook/jmespath/\#an-alternative-to-arrow-functions-in-expressions "Permanent link")

For example, generate some input data by returning the below code from the Code node:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>``` | ```<br>return[<br>  {<br>    "json": {      <br>      "num_categories": "0",<br>      "num_products": "45",<br>      "category_id": 5529735,<br>      "parent_id": 1407340,<br>      "pos_enabled": 1,<br>      "pos_favorite": 0,<br>      "name": "HP",<br>      "description": "",<br>      "image": ""<br>    }<br>  },<br>  {<br>    "json": {<br>      "num_categories": "0",<br>      "num_products": "86",<br>      "category_id": 5529740,<br>      "parent_id": 1407340,<br>      "pos_enabled": 1,<br>      "pos_favorite": 0,<br>      "name": "Lenovo",<br>      "description": "",<br>      "image": ""<br>    }<br>  }  <br>]<br>``` |

You could do a search like "find the item with the name Lenovo and tell me their category ID."

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>{{ $jmespath($("Code").all(), "[?json.name=='Lenovo'].json.category_id") }}<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top