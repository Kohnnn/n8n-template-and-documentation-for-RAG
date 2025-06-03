---
url: "https://docs.n8n.io/code/cookbook/expressions/check-incoming-data/"
title: "Check incoming data | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/cookbook/expressions/check-incoming-data/#check-incoming-data)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/expressions/check-incoming-data.md "Edit this page")

# Check incoming data [\#](https://docs.n8n.io/code/cookbook/expressions/check-incoming-data/\#check-incoming-data "Permanent link")

At times, you may want to check the incoming data. If the incoming data doesn't match a condition, you may want to return a different value. For example, you want to check if a variable from the previous node is empty and return a string if it's empty. Use the following code snippet to return `not found` if the variable is empty.

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>{{$json["variable_name"]? $json["variable_name"] :"not found"}}<br>``` |

The above expression uses the ternary operator. You can learn more about the ternary operator [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator).

As an alternative, you can use the [nullish coalescing operator (??)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) or the [logical or operator (\|\|)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR):

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>{{ $x ?? "default value" }}<br>{{ $x || "default value" }}<br>``` |

In either of the above two cases, the value of `$x` will be used if it's set to a non-null, non-false value. The string `default value` is the fallback value.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top