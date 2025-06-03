---
url: "https://docs.n8n.io/code/builtin/convenience/"
title: "Convenience methods | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/builtin/convenience/#convenience-methods)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/convenience.md "Edit this page")

# Convenience methods [\#](https://docs.n8n.io/code/builtin/convenience/\#convenience-methods "Permanent link")

n8n provides these methods to make it easier to perform common tasks in [expressions](https://docs.n8n.io/glossary/#expression-n8n).

Python support

You can use Python in the Code node. It isn't available in expressions.

[JavaScript](https://docs.n8n.io/code/builtin/convenience/#__tabbed_1_1)[Python](https://docs.n8n.io/code/builtin/convenience/#__tabbed_1_2)

| Method | Description | Available in Code node? |
| --- | --- | --- |
| `$evaluateExpression(expression: string, itemIndex?: number)` | Evaluates a string as an expression. If you don't provide `itemIndex`, n8n uses the data from item 0 in the Code node. | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) |
| `$ifEmpty(value, defaultValue)` | The `$ifEmpty()` function takes two parameters, tests the first to check if it's empty, then returns either the parameter (if not empty) or the second parameter (if the first is empty). The first parameter is empty if it's:<br>- `undefined`<br>- `null`<br>- An empty string `''`<br>- An array where `value.length` returns `false`<br>- An object where `Object.keys(value).length` returns `false` | ![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) |
| `$if()` | The `$if()` function takes three parameters: a condition, the value to return if true, and the value to return if false. | ![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) |
| `$max()` | Returns the highest of the provided numbers. | ![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) |
| `$min()` | Returns the lowest of the provided numbers. | ![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) |

| Method | Description |
| --- | --- |
| `_evaluateExpression(expression: string, itemIndex?: number)` | Evaluates a string as an expression. If you don't provide `itemIndex`, n8n uses the data from item 0 in the Code node. |
| `_ifEmpty(value, defaultValue)` | The `_ifEmpty()` function takes two parameters, tests the first to check if it's empty, then returns either the parameter (if not empty) or the second parameter (if the first is empty). The first parameter is empty if it's:<br>- `undefined`<br>- `null`<br>- An empty string `''`<br>- An array where `value.length` returns `false`<br>- An object where `Object.keys(value).length` returns `false` |

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top