---
url: "https://docs.browserless.io/bql-schema/types/enums/wait-until-history"
title: "WaitUntilHistory | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/enums/wait-until-history#__docusaurus_skipToContent_fallback)

On this page

The different stages of the browser's loading process

```codeBlockLines_p187
enum WaitUntilHistory {
  commit
  domContentLoaded
  load
  networkIdle
}

```

### Values [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#values "Direct link to Values")

#### [`WaitUntilHistory.commit`](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#waituntilhistorycommit "Direct link to waituntilhistorycommit")

Fired when network response is received and the document started loading

#### [`WaitUntilHistory.domContentLoaded`](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#waituntilhistorydomcontentloaded "Direct link to waituntilhistorydomcontentloaded")

Fired when the DOMContentLoaded event is fired

#### [`WaitUntilHistory.load`](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#waituntilhistoryload "Direct link to waituntilhistoryload")

Fired when the 'load' event occurs

#### [`WaitUntilHistory.networkIdle`](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#waituntilhistorynetworkidle "Direct link to waituntilhistorynetworkidle")

Use with caution: Fired when there are no network connections for at least 500 ms

### Member Of [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-history\#member-of "Direct link to Member Of")

[`back`](https://docs.browserless.io/bql-schema/operations/mutations/back) mutation ● [`content`](https://docs.browserless.io/bql-schema/operations/mutations/content) mutation ● [`forward`](https://docs.browserless.io/bql-schema/operations/mutations/forward) mutation ● [`reload`](https://docs.browserless.io/bql-schema/operations/mutations/reload) mutation

- [Values](https://docs.browserless.io/bql-schema/types/enums/wait-until-history#values)
- [Member Of](https://docs.browserless.io/bql-schema/types/enums/wait-until-history#member-of)