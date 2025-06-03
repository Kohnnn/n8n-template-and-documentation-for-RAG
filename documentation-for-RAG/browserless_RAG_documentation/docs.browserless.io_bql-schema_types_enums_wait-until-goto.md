---
url: "https://docs.browserless.io/bql-schema/types/enums/wait-until-goto"
title: "WaitUntilGoto | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto#__docusaurus_skipToContent_fallback)

On this page

Options for when to consider the page has loaded and proceed with further execution

```codeBlockLines_p187
enum WaitUntilGoto {
  domContentLoaded
  load
  commit
  firstMeaningfulPaint
  firstContentfulPaint
  interactiveTime
  networkIdle
}

```

### Values [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#values "Direct link to Values")

#### [`WaitUntilGoto.domContentLoaded`](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#waituntilgotodomcontentloaded "Direct link to waituntilgotodomcontentloaded")

Fired when the DOMContentLoaded event is fired

#### [`WaitUntilGoto.load`](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#waituntilgotoload "Direct link to waituntilgotoload")

Fired when the 'load' event occurs

#### [`WaitUntilGoto.commit`](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#waituntilgotocommit "Direct link to waituntilgotocommit")

Fired when network response is received and the document started loading

#### [`WaitUntilGoto.firstMeaningfulPaint`](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#waituntilgotofirstmeaningfulpaint "Direct link to waituntilgotofirstmeaningfulpaint")

Indicates when the primary content of a page is visible to the user

#### [`WaitUntilGoto.firstContentfulPaint`](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#waituntilgotofirstcontentfulpaint "Direct link to waituntilgotofirstcontentfulpaint")

The render time of the largest image or text block visible in the viewport, relative to when the user first navigated to the page

#### [`WaitUntilGoto.interactiveTime`](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#waituntilgotointeractivetime "Direct link to waituntilgotointeractivetime")

Use with caution: Chrome's best guess as to when the page becomes interactable

#### [`WaitUntilGoto.networkIdle`](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#) [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#waituntilgotonetworkidle "Direct link to waituntilgotonetworkidle")

Use with caution: Fired when there are no network connections for at least 500 ms

### Member Of [​](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto\#member-of "Direct link to Member Of")

[`goto`](https://docs.browserless.io/bql-schema/operations/mutations/goto) mutation ● [`waitForNavigation`](https://docs.browserless.io/bql-schema/operations/mutations/wait-for-navigation) mutation

- [Values](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto#values)
- [Member Of](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto#member-of)