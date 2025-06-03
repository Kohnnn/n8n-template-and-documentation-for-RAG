---
url: "https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/"
title: "Data transformation functions for numbers | n8n Docs "
---

[Skip to content](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/#numbers)

[Edit this page](https://github.com/n8n-io/n8n-docs/edit/main/docs/code/builtin/data-transformation-functions/numbers.md "Edit this page")

# Numbers [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#numbers "Permanent link")

A reference document listing built-in convenience functions to support data transformation in [expressions](https://docs.n8n.io/glossary/#expression-n8n) for numbers.

JavaScript in expressions

You can use any JavaScript in expressions. Refer to [Expressions](https://docs.n8n.io/code/expressions/) for more information.

### ceil():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#number-ceil "Permanent link")

Rounds up a number to a whole number.

* * *

### floor():  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#number-floor "Permanent link")

Rounds down a number to a whole number.

* * *

### format(locales?:  LanguageCode, options?:  FormatOptions):  String [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#number-format "Permanent link")

This is a wrapper around [Intl.NumberFormat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat). Returns a formatted string of a number based on the given LanguageCode and FormatOptions. When no arguments are given, transforms the number in a like format 1.234.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#function-parameters "Permanent link")

localesOptionalString

An IETF BCP 47 language tag.

Default: `en-US`

optionsOptionalObject

Configure options for number formatting. Refer to [MDN \| Intl.NumberFormat()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat) for more information.

* * *

### isEven():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#number-isEven "Permanent link")

Returns true if the number is even. Only works on whole numbers.

* * *

### isOdd():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#number-isOdd "Permanent link")

Returns true if the number is odd. Only works on whole numbers.

* * *

### round(decimalPlaces?:  Number):  Number [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#number-round "Permanent link")

Returns the value of a number rounded to the nearest whole number, unless a decimal place is specified.

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#function-parameters_1 "Permanent link")

decimalPlacesOptionalNumber

How many decimal places to round to.

Default: `0`

* * *

### toBoolean():  Boolean [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#number-toBoolean "Permanent link")

Converts a number to a boolean. `0` converts to `false`. All other values convert to `true`.

* * *

### toDateTime(format?:  String):  Date [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#number-toDateTime "Permanent link")

Converts a number to a [Luxon date object](https://docs.n8n.io/code/cookbook/luxon/).

#### Function parameters [\#](https://docs.n8n.io/code/builtin/data-transformation-functions/numbers/\#function-parameters_2 "Permanent link")

formatOptionalString enum

Can be `ms` (milliseconds), `s` (seconds), or `excel` (Excel 1900). Defaults to milliseconds.

* * *

Was this page helpful?






Thanks for your feedback!






Thanks for your feedback! Help us improve this page by submitting an issue or a fix in our [GitHub repo](https://github.com/n8n-io/n8n-docs).


Back to top