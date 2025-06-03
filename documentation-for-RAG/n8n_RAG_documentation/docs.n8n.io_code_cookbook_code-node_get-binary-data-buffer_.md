---
url: "https://docs.n8n.io/code/cookbook/code-node/get-binary-data-buffer/"
title: "Get the binary data buffer | n8n Docs  "
---

[Skip to content](https://docs.n8n.io/code/cookbook/code-node/get-binary-data-buffer/#get-the-binary-data-buffer)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/cookbook/code-node/get-binary-data-buffer.md "Edit this page")

# Get the binary data buffer [\#](https://docs.n8n.io/code/cookbook/code-node/get-binary-data-buffer/\#get-the-binary-data-buffer "Permanent link")

The binary data buffer contains all the binary file data processed by a workflow. You need to access it if you want to perform operations on the binary data, such as:

- Manipulating the data: for example, adding column headers to a CSV file.
- Using the data in calculations: for example, calculating a hash value based on it.
- Complex HTTP requests: for example, combining file upload with sending other data formats.

Not available in Python

`getBinaryDataBuffer()` isn't supported when using Python.

You can access the buffer using n8n's `getBinaryDataBuffer()` function:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>5<br>6<br>``` | ```<br>/* <br>* itemIndex: number. The index of the item in the input data.<br>* binaryPropertyName: string. The name of the binary property. <br>* The default in the Read/Write File From Disk node is 'data'. <br>*/<br>let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(itemIndex, binaryPropertyName);<br>``` |

For example:

|     |     |
| --- | --- |
| ```<br>1<br>2<br>``` | ```<br>let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(0, 'data');<br>// Returns the data in the binary buffer for the first input item<br>``` |

You should always use the `getBinaryDataBuffer()` function, and avoid using older methods of directly accessing the buffer, such as targeting it with expressions like `items[0].binary.data.data`.

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top