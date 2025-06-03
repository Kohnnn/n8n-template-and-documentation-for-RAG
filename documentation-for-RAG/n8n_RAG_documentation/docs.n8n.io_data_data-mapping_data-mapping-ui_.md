---
url: "https://docs.n8n.io/data/data-mapping/data-mapping-ui/"
title: "Data mapping in the UI | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/data/data-mapping/data-mapping-ui/#mapping-in-the-ui)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/data/data-mapping/data-mapping-ui.md "Edit this page")

# Mapping in the UI [\#](https://docs.n8n.io/data/data-mapping/data-mapping-ui/\#mapping-in-the-ui "Permanent link")

Data mapping means referencing data from previous nodes. It doesn't include changing (transforming) data, just referencing it.

You can map data in the following ways:

- Using the expressions editor.
- By dragging and dropping data from the **INPUT** into parameters. This generates the expression for you.

For information on errors with mapping and linking items, refer to [Item linking errors](https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-errors/).

## How to drag and drop data [\#](https://docs.n8n.io/data/data-mapping/data-mapping-ui/\#how-to-drag-and-drop-data "Permanent link")

1. Run your workflow to load data.
2. Open the node where you need to map data.
3. You can map in table, JSON, and schema view:
   - In table view: click and hold a table heading to map top level data, or a field in the table to map nested data.
   - In JSON view: click and hold a key.
   - In schema view: click and hold a key.
4. Drag the item into the field where you want to use the data.

### Understand what you're mapping with drag and drop [\#](https://docs.n8n.io/data/data-mapping/data-mapping-ui/\#understand-what-youre-mapping-with-drag-and-drop "Permanent link")

Data mapping maps the key path, and loads the key's value into the field. For example, given the following data:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>``` | ```<br>[<br>	{<br>		"fruit": "apples",<br>		"color": "green"<br>	}<br>]<br>``` |

You can map `fruit` by dragging and dropping **fruit** from the **INPUT** into the field where you want to use its value. This creates an expression, `{{ $json.fruit }}`. When the node iterates over input items, the value of the field becomes the value of `fruit` for each item.

### Understand nested data [\#](https://docs.n8n.io/data/data-mapping/data-mapping-ui/\#understand-nested-data "Permanent link")

Given the following data:

|     |     |
| --- | --- |
| ```<br> 1<br> 2<br> 3<br> 4<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>``` | ```<br>[<br>  {<br>    "name": "First item",<br>    "nested": {<br>      "example-number-field": 1,<br>      "example-string-field": "apples"<br>    }<br>  },<br>  {<br>    "name": "Second item",<br>    "nested": {<br>      "example-number-field": 2,<br>      "example-string-field": "oranges"<br>    }<br>  }<br>]<br>``` |

n8n displays it in table form like this:

[!["Screenshot of a table in the INPUT panel. It includes a top level field named "nested." This field contains nested data, which is indicated in bold."](https://docs.n8n.io/_images/data/data-mapping/nested-data.png)](https://docs.n8n.io/_images/data/data-mapping/nested-data.png)

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top