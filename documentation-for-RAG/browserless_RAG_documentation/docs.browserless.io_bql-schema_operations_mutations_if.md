---
url: "https://docs.browserless.io/bql-schema/operations/mutations/if"
title: "if | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/if#__docusaurus_skipToContent_fallback)

On this page

Triggers a nested branch of work when a given condition is `true`. Does not wait for these items and is a point-in-time check. Use the wait method if you're wanting to await certain behaviors to be present

Example:

```codeBlockLines_p187
mutation If {
  goto(url: "https://example.com") {
    status
  }

  # Will only trigger the screenshot if the h1 is present
  if(selector: "h1") {
    screenshot {
      base64
    }
  }
}

```

```codeBlockLines_p187
if(
  request: RequestInput
  response: ResponseInput
  selector: String
  visible: Boolean = false
): Mutation

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/if\#arguments "Direct link to Arguments")

#### [`if.request`](https://docs.browserless.io/bql-schema/operations/mutations/if\#) ● [`RequestInput`](https://docs.browserless.io/bql-schema/types/inputs/request-input) input [​](https://docs.browserless.io/bql-schema/operations/mutations/if\#ifrequestrequestinput- "Direct link to ifrequestrequestinput-")

Triggers the nested conditions if a request has been made with the following conditions

#### [`if.response`](https://docs.browserless.io/bql-schema/operations/mutations/if\#) ● [`ResponseInput`](https://docs.browserless.io/bql-schema/types/inputs/response-input) input [​](https://docs.browserless.io/bql-schema/operations/mutations/if\#ifresponseresponseinput- "Direct link to ifresponseresponseinput-")

Triggers the nested conditions if a response has been received with the following conditions

#### [`if.selector`](https://docs.browserless.io/bql-schema/operations/mutations/if\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/if\#ifselectorstring- "Direct link to ifselectorstring-")

Triggers the subsequent conditions if the selector is immediately present

#### [`if.visible`](https://docs.browserless.io/bql-schema/operations/mutations/if\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/if\#ifvisibleboolean- "Direct link to ifvisibleboolean-")

When using selectors in conditionals this options sets whether their or not to consider if they're visible to the viewport

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/if\#type "Direct link to Type")

#### [`Mutation`](https://docs.browserless.io/bql-schema/types/objects/mutation) object [​](https://docs.browserless.io/bql-schema/operations/mutations/if\#mutation- "Direct link to mutation-")

Below is a list of all available API options for the service. Click on an API for options, examples, and even argument details.

For more comprehensive examples and recipes, [see our documentation site here](https://docs.browserless.io/).

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/if#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/if#type)