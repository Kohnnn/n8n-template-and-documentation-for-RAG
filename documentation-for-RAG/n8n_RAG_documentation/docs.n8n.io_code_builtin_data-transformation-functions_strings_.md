---
url: "https://docs.n8n.io/code/builtin/data-transformation-functions/strings/"
title: "Data transformation functions for strings | n8n Docs "
---

[Skip to content](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/#strings)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/data-transformation-functions/strings.md "Edit this page")

# Strings [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#strings "Permanent link")

A reference document listing built-in convenience functions to support data transformation in [expressions](https://docs.n8n.io/glossary/#expression-n8n) for strings.

JavaScript in expressions

You can use any JavaScript in expressions. Refer to [Expressions](https://docs.n8n.io/code/expressions/) for more information.

### base64Encode():  A base64 encoded string. [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-base64Encode "Permanent link")

Encode a string as base64.

* * *

### base64Decode():  A plain string. [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-base64Decode "Permanent link")

Convert a base64 encoded string to a normal string.

* * *

### extractDomain():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-extractDomain "Permanent link")

Extracts a domain from a string containing a valid URL. Returns undefined if none is found.

* * *

### extractEmail():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-extractEmail "Permanent link")

Extracts an email from a string. Returns undefined if none is found.

* * *

### extractUrl():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-extractUrl "Permanent link")

Extracts a URL from a string. Returns undefined if none is found.

* * *

### extractUrlPath():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-extractUrlPath "Permanent link")

Extract the path but not the root domain from a URL. For example, `"https://example.com/orders/1/details".extractUrlPath()` returns `"/orders/1/details/"`.

* * *

### hash(algo?:  Algorithm):  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-hash "Permanent link")

Returns a string hashed with the given algorithm.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#function-parameters "Permanent link")

algoOptionalString enum

Which hashing algorithm to use.

Default: `md5`

One of:
`md5`,

`base64`,

`sha1`,

`sha224`,

`sha256`,

`sha384`,

`sha512`,

`sha3`,

`ripemd160`

* * *

### isDomain():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-isDomain "Permanent link")

Checks if a string is a domain.

* * *

### isEmail():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-isEmail "Permanent link")

Checks if a string is an email.

* * *

### isEmpty():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-isEmpty "Permanent link")

Checks if a string is empty.

* * *

### isNotEmpty():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-isNotEmpty "Permanent link")

Checks if a string has content.

* * *

### isNumeric():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-isNumeric "Permanent link")

Checks if a string only contains digits.

* * *

### isUrl():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-isUrl "Permanent link")

Checks if a string is a valid URL.

* * *

### parseJson():  Object [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-parseJson "Permanent link")

Equivalent of `JSON.parse()`. Parses a string as a JSON object.

* * *

### quote(mark?:  String):  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-quote "Permanent link")

Returns a string wrapped in the quotation marks. Default quotation is `"`.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#function-parameters_1 "Permanent link")

markOptionalString

Which quote mark style to use.

Default: `"
`

* * *

### removeMarkdown():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-removeMarkdown "Permanent link")

Removes Markdown formatting from a string.

* * *

### replaceSpecialChars():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-replaceSpecialChars "Permanent link")

Replaces non-ASCII characters in a string with an ASCII representation.

* * *

### removeTags():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-removeTags "Permanent link")

Remove tags, such as HTML or XML, from a string.

* * *

### toBoolean():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-toBoolean "Permanent link")

Convert a string to a boolean. `"false"`, `"0"`, `""`, and `"no"` convert to `false`.

* * *

### toDateTime():  Date [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-toDateTime "Permanent link")

Converts a string to a [Luxon date object](https://docs.n8n.io/code/cookbook/luxon/).

* * *

### toDecimalNumber():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-toDecimalNumber "Permanent link")

See [toFloat](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/#string-toFloat)

* * *

### toFloat():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-toFloat "Permanent link")

Converts a string to a decimal number.

* * *

### toInt():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-toInt "Permanent link")

Converts a string to an integer.

* * *

### toSentenceCase():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-toSentenceCase "Permanent link")

Formats a string to sentence case.

* * *

### toSnakeCase():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-toSnakeCase "Permanent link")

Formats a string to snake case.

* * *

### toTitleCase():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-toTitleCase "Permanent link")

Formats a string to title case. Will not change already uppercase letters to prevent losing information from acronyms and trademarks such as iPhone or FAANG.

* * *

### toWholeNumber():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-toWholeNumber "Permanent link")

Converts a string to a whole number.

* * *

### urlDecode(entireString?:  Boolean):  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-urlDecode "Permanent link")

Decodes a URL-encoded string. It decodes any percent-encoded characters in the input string, and replaces them with their original characters.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#function-parameters_2 "Permanent link")

entireStringOptionalBoolean

Whether to decode characters that are part of the URI syntax (true) or not (false).

* * *

### urlEncode(entireString?:  Boolean):  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#string-urlEncode "Permanent link")

Encodes a string to be used/included in a URL.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/strings/\#function-parameters_3 "Permanent link")

entireStringOptionalBoolean

Whether to encode characters that are part of the URI syntax (true) or not (false).

* * *

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top