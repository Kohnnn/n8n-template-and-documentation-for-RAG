---
url: "https://docs.n8n.io/code/cookbook/expressions/common-issues/"
title: "Expressions common issues | n8n Docs "
---

[Skip to content](https://docs.n8n.io/code/cookbook/expressions/common-issues/#expressions-common-issues)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/expressions/common-issues.md "Edit this page")

# Expressions common issues [\#](https://docs.n8n.io/code/cookbook/expressions/common-issues/\#expressions-common-issues "Permanent link")

Here are some common errors and issues related to [expressions](https://docs.n8n.io/code/expressions/) and steps to resolve or troubleshoot them.

## The 'JSON Output' in item 0 contains invalid JSON [\#](https://docs.n8n.io/code/cookbook/expressions/common-issues/\#the-json-output-in-item-0-contains-invalid-json "Permanent link")

This error occurs when you use JSON mode but don't provide a valid JSON object. Depending on the problem with the JSON object, the error sometimes display as `The 'JSON Output' in item 0 does not contain a valid JSON object`.

To resolve this, make sure that the code you provide is valid JSON:

- Check the JSON with a [JSON validator](https://jsonlint.com/).
- Check that your JSON object doesn't reference undefined input data. This may occur if the incoming data doesn't always include the same fields.

## Can't get data for expression [\#](https://docs.n8n.io/code/cookbook/expressions/common-issues/\#cant-get-data-for-expression "Permanent link")

This error occurs when n8n can't retrieve the data referenced by an expression. Often, this happens when the preceding node hasn't been run yet.

Another variation of this may appear as `Referenced node is unexecuted`. In that case, the full text of this error will tell you the exact node that isn't executing in this format:

> An expression references the node '<node-name>', but it hasn’t been executed yet. Either change the expression, or re-wire your workflow to make sure that node executes first.

To begin troubleshooting, test the workflow up to the named node.

For nodes that use JavaScript or other custom code, you can check if a previous node has executed before trying to use its value by checking the following:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>$("<node-name>").isExecuted<br>``` |

As an example, this JSON references the parameters of the input data. This error will display if you test this step without connecting it to another node:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>{<br>  "my_field_1": {{ $input.params }}<br>}<br>``` |

## Invalid syntax [\#](https://docs.n8n.io/code/cookbook/expressions/common-issues/\#invalid-syntax "Permanent link")

This error occurs when you use an expression that has a syntax error.

For example, the expression in this JSON includes a trailing period, which results in an invalid syntax error:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>``` | ```<br>{<br>  "my_field_1": "value",<br>  "my_field_2": {{ $('If').item.json. }}<br>}<br>``` |

To resolve this error, check your [expression syntax](https://www.notion.so/code/expressions/) to make sure they follow the expected format.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top