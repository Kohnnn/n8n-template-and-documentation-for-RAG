---
url: "https://docs.browserless.io/bql-schema/operations/mutations/solve"
title: "solve | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/solve#__docusaurus_skipToContent_fallback)

On this page

🚨 **EXPERIMENTAL** 🚨
Solves a captcha or other challenge, specified by the "type" of captcha to solve

Example:

```codeBlockLines_p187
mutation SolveCaptcha {
  goto(url: "https://protected.domain") {
    status
  }

  solve(type: hcaptcha) {
    found
    solved
    time
  }
}

```

```codeBlockLines_p187
solve(
  type: CaptchaTypes!
  timeout: Float
  wait: Boolean = true
): CaptchaResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/solve\#arguments "Direct link to Arguments")

#### [`solve.type`](https://docs.browserless.io/bql-schema/operations/mutations/solve\#) ● [`CaptchaTypes!`](https://docs.browserless.io/bql-schema/types/enums/captcha-types) non-nullenum [​](https://docs.browserless.io/bql-schema/operations/mutations/solve\#solvetypecaptchatypes-- "Direct link to solvetypecaptchatypes--")

An enum of the type of captcha to look for and solve

#### [`solve.timeout`](https://docs.browserless.io/bql-schema/operations/mutations/solve\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/solve\#solvetimeoutfloat- "Direct link to solvetimeoutfloat-")

A time, in milliseconds, to wait for a captcha to appear. Only valid when wait = true.
If a captcha is found then this timer doesn't have an effect on timing-out the solve

#### [`solve.wait`](https://docs.browserless.io/bql-schema/operations/mutations/solve\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/solve\#solvewaitboolean- "Direct link to solvewaitboolean-")

Whether or not to wait for the Captcha to be present on the page

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/solve\#type "Direct link to Type")

#### [`CaptchaResponse`](https://docs.browserless.io/bql-schema/types/objects/captcha-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/solve\#captcharesponse- "Direct link to captcharesponse-")

Response returned after a captcha has been solved

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/solve#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/solve#type)