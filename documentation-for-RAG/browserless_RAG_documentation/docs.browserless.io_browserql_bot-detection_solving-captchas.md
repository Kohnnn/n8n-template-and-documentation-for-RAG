---
url: "https://docs.browserless.io/browserql/bot-detection/solving-captchas"
title: "Solving CAPTCHAs | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/bot-detection/solving-captchas#__docusaurus_skipToContent_fallback)

On this page

CAPTCHAs are a common roadblock in automation. BrowserQL includes built-in support for CAPTCHA challenges. BQL will automatically detect and interacts with CAPTCHAs, even those embedded in iframes or shadow DOMs. You can use the following mutations:

- [Verify](https://docs.browserless.io/browserql/bot-detection/solving-captchas#verify)
- [Solve](https://docs.browserless.io/browserql/bot-detection/solving-captchas#solve)

## Verify [​](https://docs.browserless.io/browserql/bot-detection/solving-captchas\#verify "Direct link to Verify")

The [`Verify`](https://docs.browserless.io/bql-schema/operations/mutations/verify) mutation clicks a verification button to assert human-like interaction. This mutation can be used to surpass cloudflare's human verification step.

If you're not sure whether a site has Cloudflare protection, you can use the `if` mutation with a `waitForSelector` to conditionally run the verification. Since the `if` mutation doesn't wait for a selector to be present, adding a `waitForSelector` before it ensures the Cloudflare turnstile is available before attempting verification.

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

### Conditional Cloudflare Verification [​](https://docs.browserless.io/browserql/bot-detection/solving-captchas\#conditional-cloudflare-verification "Direct link to Conditional Cloudflare Verification")

Here's an example of using conditional verification with the `if` mutation:

```codeBlockLines_p187
    goto(url: "https://www.browserless.io/practice-form") {
      status
    }
    waitForSelector(selector:".cf-turnstile",timeout:1000){
      time
    }
    if(selector:".cf-turnstile"){
      verify(type:cloudflare,timeout:30000){
        found
        solved
        time
      }
    }
    html{
      html
    }

```

Note that `.cf-turnstile` is specific to our sample website. For your own implementation, you should look for a selector that works for your target website. Some alternatives that might work on other sites include `a[href*="cloudflare.com"]` or other Cloudflare-specific elements.

## Solve [​](https://docs.browserless.io/browserql/bot-detection/solving-captchas\#solve "Direct link to Solve")

The [`Solve`](https://docs.browserless.io/bql-schema/operations/mutations/solve) mutation solves a captcha, specified by the "type" of captcha to solve. Currently, BQL can solve **turnstile reCAPTCHAs** and **hCAPTCHAs** only. Image-based CAPTCHAs are not supported yet.

info

When solving reCAPTCHAs, it's normal if there isn't a visual confirmation that the CAPTCHA has been solved (i.e., the checkbox may not appear ticked). This is expected behavior. After solving, you should proceed and click on the form's submit button.

- hCaptcha
- reCAPTCHA

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
mutation SolveCaptcha {
  goto(url: "https://protected.domain") {
    status
  }

  solve(type: recaptcha) {
    found
    solved
    time
  }
}

```

### Form Submission After Solving [​](https://docs.browserless.io/browserql/bot-detection/solving-captchas\#form-submission-after-solving "Direct link to Form Submission After Solving")

After solving a CAPTCHA, you should proceed with form submission by clicking the submit button:

```codeBlockLines_p187
mutation SolveAndSubmit {
  goto(url: "https://protected.domain") {
    status
  }

  solve(type: recaptcha) {
    found
    solved
    time
  }

  click(selector: "button[type='submit']") {
    time
  }
}

```

If there isn't a submit button available, you can trigger form submission manually using the `evaluate` mutation:

```codeBlockLines_p187
mutation SolveAndTriggerSubmit {
  goto(url: "https://protected.domain") {
    status
  }

  solve(type: recaptcha) {
    found
    solved
    time
  }

  evaluate(content: "window.onSubmit()") {
    time
  }
}

```

Replace `window.onSubmit()` with the appropriate JavaScript function that submits the form on your target website.

- [Verify](https://docs.browserless.io/browserql/bot-detection/solving-captchas#verify)
  - [Conditional Cloudflare Verification](https://docs.browserless.io/browserql/bot-detection/solving-captchas#conditional-cloudflare-verification)
- [Solve](https://docs.browserless.io/browserql/bot-detection/solving-captchas#solve)
  - [Form Submission After Solving](https://docs.browserless.io/browserql/bot-detection/solving-captchas#form-submission-after-solving)