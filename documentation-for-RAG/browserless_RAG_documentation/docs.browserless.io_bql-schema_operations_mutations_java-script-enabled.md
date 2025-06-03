---
url: "https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled"
title: "javaScriptEnabled | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled#__docusaurus_skipToContent_fallback)

On this page

Sets and gets JavaScript execution on the page

**Note: changing this value won't affect scripts that have already been run. It will take full effect on the next navigation.**

Example:

```codeBlockLines_p187
mutation JavaScript {
  status: javaScriptEnabled {
    enabled
  }

  disable: javaScriptEnabled(enabled: false) {
    enabled
  }

  enable: javaScriptEnabled(enabled: true) {
    enabled
  }
}

```

```codeBlockLines_p187
javaScriptEnabled(
  enabled: Boolean
): JavaScriptResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled\#arguments "Direct link to Arguments")

#### [`javaScriptEnabled.enabled`](https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled\#javascriptenabledenabledboolean- "Direct link to javascriptenabledenabledboolean-")

Whether or not to enable JavaScript on the page

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled\#type "Direct link to Type")

#### [`JavaScriptResponse`](https://docs.browserless.io/bql-schema/types/objects/java-script-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled\#javascriptresponse- "Direct link to javascriptresponse-")

The response returned after enabling or disabling JavaScript on the page

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/java-script-enabled#type)