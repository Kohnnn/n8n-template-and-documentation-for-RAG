---
url: "https://docs.browserless.io/bql-schema/operations/mutations/ifnot"
title: "ifnot | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/ifnot#__docusaurus_skipToContent_fallback)

On this page

Triggers a nested branch of work when a given condition is `false`. This method does not wait for these items and is a point-in-time check. Use the wait method if you're wanting to await certain behaviors to be present

Example:

```codeBlockLines_p187
mutation IfNot {
  goto(url: "https://example.com") {
    status
  }

  # Will only trigger the screenshot if the h2 is not present
  ifnot(selector: "h2") {
    screenshot {
      base64
    }
  }
}

```

```codeBlockLines_p187
ifnot(
  request: RequestInput
  response: ResponseInput
  selector: String
): Mutation

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/ifnot\#arguments "Direct link to Arguments")

#### [`ifnot.request`](https://docs.browserless.io/bql-schema/operations/mutations/ifnot\#) ● [`RequestInput`](https://docs.browserless.io/bql-schema/types/inputs/request-input) input [​](https://docs.browserless.io/bql-schema/operations/mutations/ifnot\#ifnotrequestrequestinput- "Direct link to ifnotrequestrequestinput-")

Triggers the nested conditions if a request has been made with the following conditions

#### [`ifnot.response`](https://docs.browserless.io/bql-schema/operations/mutations/ifnot\#) ● [`ResponseInput`](https://docs.browserless.io/bql-schema/types/inputs/response-input) input [​](https://docs.browserless.io/bql-schema/operations/mutations/ifnot\#ifnotresponseresponseinput- "Direct link to ifnotresponseresponseinput-")

Triggers the nested conditions if a response has been received with the following conditions

#### [`ifnot.selector`](https://docs.browserless.io/bql-schema/operations/mutations/ifnot\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/ifnot\#ifnotselectorstring- "Direct link to ifnotselectorstring-")

Triggers the subsequent conditions if the selector is immediately present

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/ifnot\#type "Direct link to Type")

#### [`Mutation`](https://docs.browserless.io/bql-schema/types/objects/mutation) object [​](https://docs.browserless.io/bql-schema/operations/mutations/ifnot\#mutation- "Direct link to mutation-")

Below is a list of all available API options for the service. Click on an API for options, examples, and even argument details.

For more comprehensive examples and recipes, [see our documentation site here](https://docs.browserless.io/).

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/ifnot#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/ifnot#type)