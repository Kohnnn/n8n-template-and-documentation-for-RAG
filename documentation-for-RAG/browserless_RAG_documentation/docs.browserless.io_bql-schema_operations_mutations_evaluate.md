---
url: "https://docs.browserless.io/bql-schema/operations/mutations/evaluate"
title: "evaluate | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/evaluate#__docusaurus_skipToContent_fallback)

On this page

Evaluates JavaScript client-side, via raw content or a URL to some JavaScript code, in the browser's page environment

Example:

```codeBlockLines_p187
mutation EvaluateScript {
  byContent: evaluate(content: "2 + 2") {
    value
  }

  byUrl: evaluate(url: "https://example.com/script.js") {
    value
  }
}

```

```codeBlockLines_p187
evaluate(
  content: String
  timeout: Float
  url: String
): EvaluateResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/evaluate\#arguments "Direct link to Arguments")

#### [`evaluate.content`](https://docs.browserless.io/bql-schema/operations/mutations/evaluate\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/evaluate\#evaluatecontentstring- "Direct link to evaluatecontentstring-")

The raw script you'd like to evaluate. This code gets wrapped in an async function so you can use `return` at the end as well as `await` and other async concepts. You can return any stringified value from this function

#### [`evaluate.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/evaluate\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/evaluate\#evaluatetimeoutfloat- "Direct link to evaluatetimeoutfloat-")

A timeout to wait for the script to finish evaluating, overriding any defaults. Useful for async scripts that may be longer running. Default timeout is 30 seconds, or 30000.

#### [`evaluate.url`](https://docs.browserless.io/bql-schema/operations/mutations/evaluate\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/evaluate\#evaluateurlstring- "Direct link to evaluateurlstring-")

The URL of the script you'd like to evaluate. This code gets wrapped in an async function so you can use `return` at the end as well as `await` and other async
concepts. You can return any stringified value from this function

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/evaluate\#type "Direct link to Type")

#### [`EvaluateResponse`](https://docs.browserless.io/bql-schema/types/objects/evaluate-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/evaluate\#evaluateresponse- "Direct link to evaluateresponse-")

Response returned after evaluating a script

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/evaluate#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/evaluate#type)