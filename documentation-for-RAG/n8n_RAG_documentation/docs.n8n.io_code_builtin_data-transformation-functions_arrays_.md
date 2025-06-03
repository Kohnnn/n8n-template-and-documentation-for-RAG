---
url: "https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/"
title: "Data transformation functions for arrays | n8n Docs "
---

[Skip to content](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/#arrays)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/data-transformation-functions/arrays.md "Edit this page")

# Arrays [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#arrays "Permanent link")

A reference document listing built-in convenience functions to support data transformation in [expressions](https://docs.n8n.io/glossary/#expression-n8n) for arrays.

JavaScript in expressions

You can use any JavaScript in expressions. Refer to [Expressions](https://docs.n8n.io/code/expressions/) for more information.

### average():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-average "Permanent link")

Returns the value of elements in an array

* * *

### chunk(size:  Number):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-chunk "Permanent link")

Splits arrays into chunks with a length of size

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters "Permanent link")

sizeRequiredNumber

The size of each chunk.

* * *

### compact():  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-compact "Permanent link")

Removes empty values from the array.

* * *

### difference(arr:  Array):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-difference "Permanent link")

Compares two arrays. Returns all elements in the base array that aren't present in arr.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters_1 "Permanent link")

arrRequiredArray

The array to compare to the base array.

* * *

### intersection(arr:  Array):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-intersection "Permanent link")

Compares two arrays. Returns all elements in the base array that are present in arr.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters_2 "Permanent link")

arrRequiredArray

The array to compare to the base array.

* * *

### first():  Array item [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-first "Permanent link")

Returns the first element of the array.

* * *

### isEmpty():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-isEmpty "Permanent link")

Checks if the array doesn't have any elements.

* * *

### isNotEmpty():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-isNotEmpty "Permanent link")

Checks if the array has elements.

* * *

### last():  Array item [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-last "Permanent link")

Returns the last element of the array.

* * *

### max():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-max "Permanent link")

Returns the highest value in an array.

* * *

### merge(arr:  Array):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-merge "Permanent link")

Merges two Object-arrays into one array by merging the key-value pairs of each element.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters_3 "Permanent link")

arrRequiredArray

The array to merge into the base array.

* * *

### min():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-min "Permanent link")

Gets the minimum value from a number-only array.

* * *

### pluck(fieldName?:  String):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-pluck "Permanent link")

Returns an array of Objects where keys equal the given field names.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters_4 "Permanent link")

fieldNameOptionalString

The key(s) you want to retrieve. You can enter as many keys as you want, as comma-separated strings.

* * *

### randomItem():  Array item [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-randomItem "Permanent link")

Returns a random element from an array.

* * *

### removeDuplicates(key?:  String):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-removeDuplicates "Permanent link")

Removes duplicates from an array.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters_5 "Permanent link")

keyOptionalString

A key, or comma-separated list of keys, to check for duplicates.

* * *

### renameKeys(from:  String, to:  String):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-renameKeys "Permanent link")

Renames all matching keys in the array. You can rename more than one key by entering a series of comma separated strings, in the pattern oldKeyName, newKeyName.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters_6 "Permanent link")

fromRequiredString

The key you want to rename.

toRequiredString

The new name.

* * *

### smartJoin(keyField:  String, nameField:  String):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-smartJoin "Permanent link")

Operates on an array of objects where each object contains key-value pairs. Creates a new object containing key-value pairs, where the key is the value of the first pair, and the value is the value of the second pair. Removes non-matching and empty values and trims any whitespace before joining.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters_7 "Permanent link")

keyFieldRequiredString

The key to join.

nameFieldRequiredString

The value to join.

#### Example

##### Basic usage

|     |     |
| --- | --- |
| ```<br>1<br>2<br>3<br>4<br>``` | ```<br>// Input<br>{{ [{"type":"fruit", "name":"apple"},{"type":"vegetable", "name":"carrot"} ].smartJoin("type","name") }}<br>// Output<br>[Object: {"fruit":"apple","vegetable":"carrot"}]<br>``` |

* * *

### sum():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-sum "Permanent link")

Returns the total sum all the values in an array of parsable numbers.

* * *

### toJsonString():  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-toJsonString "Permanent link")

Convert an array to a JSON string. Equivalent of `JSON.stringify`.

* * *

### union(arr:  Array):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-union "Permanent link")

Concatenates two arrays and then removes duplicate.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters_8 "Permanent link")

arrRequiredArray

The array to compare to the base array.

* * *

### unique(key?:  String):  Array [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#array-unique "Permanent link")

Remove duplicates from an array.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/arrays/\#function-parameters_9 "Permanent link")

keyOptionalString

A key, or comma-separated list of keys, to check for duplicates.

* * *

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top