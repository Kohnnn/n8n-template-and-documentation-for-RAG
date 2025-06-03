---
url: "https://docs.browserless.io/bql-schema/types/objects/captcha-response"
title: "CaptchaResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/captcha-response#__docusaurus_skipToContent_fallback)

On this page

Response returned after a captcha has been solved

```codeBlockLines_p187
type CaptchaResponse {
  found: Boolean
  solved: Boolean
  time: Float
  token: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#fields "Direct link to Fields")

#### [`CaptchaResponse.found`](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#captcharesponsefoundboolean- "Direct link to captcharesponsefoundboolean-")

If a captcha was found or not

#### [`CaptchaResponse.solved`](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#captcharesponsesolvedboolean- "Direct link to captcharesponsesolvedboolean-")

If a captcha was found, whether or not it was solved

#### [`CaptchaResponse.time`](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#captcharesponsetimefloat- "Direct link to captcharesponsetimefloat-")

The total time it took to find, and solve, the captcha

#### [`CaptchaResponse.token`](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#captcharesponsetokenstring- "Direct link to captcharesponsetokenstring-")

The solved token of the response, if any is provided

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/captcha-response\#returned-by "Direct link to Returned By")

[`solve`](https://docs.browserless.io/bql-schema/operations/mutations/solve) mutation ● [`verify`](https://docs.browserless.io/bql-schema/operations/mutations/verify) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/captcha-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/captcha-response#returned-by)