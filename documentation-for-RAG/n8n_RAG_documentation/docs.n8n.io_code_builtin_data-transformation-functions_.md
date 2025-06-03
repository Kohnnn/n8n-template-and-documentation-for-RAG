---
url: "https://docs.n8n.io/code/builtin/data-transformation-functions/"
title: "Data transformation functions | n8n Docs "
---

[Skip to content](https://docs.n8n.io/code/builtin/data-transformation-functions/#data-transformation-functions)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/data-transformation-functions/index.md "Edit this page")

# Data transformation functions [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/\#data-transformation-functions "Permanent link")

Data transformation functions are helper functions to make data transformation easier in [expressions](https://docs.n8n.io/glossary/#expression-n8n).

JavaScript in expressions

You can use any JavaScript in expressions. Refer to [Expressions](https://docs.n8n.io/code/expressions/) for more information.

For a list of available functions, refer to the page for your data type:

- [Arrays](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/)
- [Dates](https://docs.n8n.io/code/builtin/data-transformation-functions/dates/)
- [Numbers](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/)
- [Objects](https://docs.n8n.io/code/builtin/data-transformation-functions/objects/)
- [Strings](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/)

## Usage [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/\#usage "Permanent link")

Data transformation functions are available in the expressions editor.

The syntax is:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>{{ dataItem.function() }}<br>``` |

For example, to check if a string is an email:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>``` | ```<br>{{ "example@example.com".isEmail() }}<br>// Returns true<br>``` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top