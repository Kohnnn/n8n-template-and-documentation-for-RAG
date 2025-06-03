---
url: "https://docs.n8n.io/code/expressions/"
title: "Expressions | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/expressions/#expressions)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/expressions.md "Edit this page")

# Expressions [\#](https://docs.n8n.io/code/expressions/\#expressions "Permanent link")

Expressions are a powerful feature implemented in all n8n nodes. They allow node parameters to be set dynamically based on data from:

- Previous node executions
- The workflow
- Your n8n environment

You can also execute JavaScript within an expression, making this a convenient and easy way to manipulate data into useful parameter values without writing extensive extra code.

n8n created and uses a templating language called [Tournament](https://github.com/n8n-io/tournament), and extends it with [custom methods and variables](https://docs.n8n.io/code/builtin/overview/) and [data transformation functions](https://docs.n8n.io/code/builtin/data-transformation-functions/). These features make it easier to perform common tasks like getting data from other nodes or accessing workflow metadata.

n8n additionally supports two libraries:

- [Luxon](https://github.com/moment/luxon/), for working with dates and time.
- [JMESPath](https://jmespath.org/), for querying JSON.

Data in n8n

When writing expressions, it's helpful to understand data structure and behavior in n8n. Refer to [Data](https://docs.n8n.io/data/) for more information on working with data in your workflows.

## Writing expressions [\#](https://docs.n8n.io/code/expressions/\#writing-expressions "Permanent link")

To use an expression to set a parameter value:

1. Hover over the parameter where you want to use an expression.
2. Select **Expressions** in the **Fixed/Expression** toggle.
3. Write your expression in the parameter, or select **Open expression editor**![Open expressions editor icon](https://docs.n8n.io/_images/common-icons/open-expression-editor.png) to open the expressions editor. If you use the expressions editor, you can browse the available data in the **Variable selector**. All expressions have the format `{{ your expression here }}`.

### Example: Get data from webhook body [\#](https://docs.n8n.io/code/expressions/\#example-get-data-from-webhook-body "Permanent link")

Consider the following scenario: you have a webhook trigger that receives data through the webhook body. You want to extract some of that data for use in the workflow.

Your webhook data looks similar to this:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>``` | ```<br>[<br>  {<br>    "headers": {<br>      "host": "n8n.instance.address",<br>      ...<br>    },<br>    "params": {},<br>    "query": {},<br>    "body": {<br>      "name": "Jim",<br>      "age": 30,<br>      "city": "New York"<br>    }<br>  }<br>]<br>``` |

In the next node in the workflow, you want to get just the value of `city`. You can use the following expression:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>{{$json.body.city}}<br>``` |

This expression:

1. Accesses the incoming JSON-formatted data using n8n's custom `$json` variable.
2. Finds the value of `city` (in this example, "New York"). Note that this example uses JMESPath syntax to query the JSON data. You can also write this expression as `{{$json['body']['city']}}`.

### Example: Writing longer JavaScript [\#](https://docs.n8n.io/code/expressions/\#example-writing-longer-javascript "Permanent link")

An expression contains one line of JavaScript. This means you cannot do things like variable assignments or multiple standalone operations.

To understand the limitations of JavaScript in expressions, and start thinking about workarounds, look at the following two pieces of code. Both code examples use the Luxon date and time library to find the time between two dates in months, and encloses the code in handlebar brackets, like an expression.

However, the first example isn't a valid n8n expression:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>``` | ```<br>// This example is split over multiple lines for readability<br>// It's still invalid when formatted as a single line<br>{{<br>  function example() {<br>    let end = DateTime.fromISO('2017-03-13');<br>    let start = DateTime.fromISO('2017-02-13');<br>    let diffInMonths = end.diff(start, 'months');<br>    return diffInMonths.toObject();<br>  }<br>  example();<br>}}<br>``` |

While the second example is valid:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>{{DateTime.fromISO('2017-03-13').diff(DateTime.fromISO('2017-02-13'), 'months').toObject()}}<br>``` |

## Common issues [\#](https://docs.n8n.io/code/expressions/\#common-issues "Permanent link")

For common errors or issues with expressions and suggested resolution steps, refer to [Common Issues](https://docs.n8n.io/code/cookbook/expressions/common-issues/).

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top