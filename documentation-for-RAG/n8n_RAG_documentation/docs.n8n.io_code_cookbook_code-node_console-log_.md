---
url: "https://docs.n8n.io/code/cookbook/code-node/console-log/"
title: "Output to the browser console | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/cookbook/code-node/console-log/#output-to-the-browser-console-with-consolelog-or-print-in-the-code-node)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/code-node/console-log.md "Edit this page")

# Output to the browser console with `console.log()` or `print()` in the Code node [\#](https://docs.n8n.io/code/cookbook/code-node/console-log/\#output-to-the-browser-console-with-consolelog-or-print-in-the-code-node "Permanent link")

You can use `console.log()` or `print()` in the Code node to help when writing and debugging your code.

For help opening your browser console, refer to [this guide by Balsamiq](https://balsamiq.com/support/faqs/browserconsole/).

## console.log (JavaScript) [\#](https://docs.n8n.io/code/cookbook/code-node/console-log/\#consolelog-javascript "Permanent link")

For technical information on `console.log()`, refer to the [MDN developer docs](https://developer.mozilla.org/en-US/docs/Web/API/Console/log).

For example, copy the following code into a Code node, then open your console and run the node:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>let a = "apple";<br>console.log(a);<br>``` |

## print (Python) [\#](https://docs.n8n.io/code/cookbook/code-node/console-log/\#print-python "Permanent link")

For technical information on `print()`, refer to the [Real Python's guide](https://realpython.com/python-print/).

For example, set your Code node **Language** to **Python**, copy the following code into the node, then open your console and run the node:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>a = "apple"<br>print(a)<br>``` |

### Handling an output of `[object Object]` [\#](https://docs.n8n.io/code/cookbook/code-node/console-log/\#handling-an-output-of-object-object "Permanent link")

If the console displays `[object Object]` when you print, check the data type, then convert it as needed.

To check the data type:

|     |     |
| --- | --- |
| ```<br>1<br>``` | ```<br>print(type(myData))<br>``` |

#### JsProxy [\#](https://docs.n8n.io/code/cookbook/code-node/console-log/\#jsproxy "Permanent link")

If `type()` outputs `<class 'pyodide.ffi.JsProxy'>`, you need to convert the JsProxy to a native Python object using `to_py()`. This occurs when working with data in the n8n node data structure, such as node inputs and outputs. For example, if you want to print the data from a previous node in the workflow:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>``` | ```<br>previousNodeData = _("<node-name>").all();<br>for item in previousNodeData:<br>	# item is of type <class 'pyodide.ffi.JsProxy'><br>	# You need to convert it to a Dict<br>	itemDict = item.json.to_py()<br>	print(itemDict)<br>``` |

Refer to the Pyodide documentation on [JsProxy](https://pyodide.org/en/stable/usage/api/python-api/ffi.html#pyodide.ffi.JsProxy) for more information on this class.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top