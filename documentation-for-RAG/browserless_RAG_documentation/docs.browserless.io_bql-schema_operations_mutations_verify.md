---
url: "https://docs.browserless.io/bql-schema/operations/mutations/verify"
title: "verify | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/verify#__docusaurus_skipToContent_fallback)

On this page

🚨 **EXPERIMENTAL** 🚨
Clicks a verification button to assert human-like

Example:

```codeBlockLines_p187
mutation Verify {
  goto(url: "https://protected.domain") {
    status
  }

  verify(type: cloudflare) {
    found
    solved
    time
  }
}

```

```codeBlockLines_p187
verify(
  type: VerifyTypes!
  timeout: Float
  wait: Boolean = true
): CaptchaResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/verify\#arguments "Direct link to Arguments")

#### [`verify.type`](https://docs.browserless.io/bql-schema/operations/mutations/verify\#) ● [`VerifyTypes!`](https://docs.browserless.io/bql-schema/types/enums/verify-types) non-nullenum [​](https://docs.browserless.io/bql-schema/operations/mutations/verify\#verifytypeverifytypes-- "Direct link to verifytypeverifytypes--")

An enum of the type of captcha to look for and solve

#### [`verify.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/verify\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/verify\#verifytimeoutfloat- "Direct link to verifytimeoutfloat-")

A time, in milliseconds, to wait for a verification to appear. Only valid when wait = true. Default timeout is 30 seconds, or 30000.

#### [`verify.wait`](https://docs.browserless.io/bql-schema/operations/mutations/verify\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/verify\#verifywaitboolean- "Direct link to verifywaitboolean-")

Whether or not to wait for the verification to be present on the page

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/verify\#type "Direct link to Type")

#### [`CaptchaResponse`](https://docs.browserless.io/bql-schema/types/objects/captcha-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/verify\#captcharesponse- "Direct link to captcharesponse-")

Response returned after a captcha has been solved

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/verify#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/verify#type)