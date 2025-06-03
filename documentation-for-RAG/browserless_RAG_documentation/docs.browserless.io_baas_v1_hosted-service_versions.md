---
url: "https://docs.browserless.io/baas/v1/hosted-service/versions"
title: "Versions on the usage based service | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/hosted-service/versions#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/versions) or [BrowserQL](https://docs.browserless.io/browserql/start).

info

This information applies for users that use API keys on the [cloud unit-based or usage-based plan](https://www.browserless.io/sign-up-usage).

Our workers that service the usage based API keys are updated every so often, here are the versions that the hosted version currently has for certain libraries, global timeout and CLI flags supported.

## Current versions used in usage based workers [​](https://docs.browserless.io/baas/v1/hosted-service/versions\#current-versions-used-in-usage-based-workers "Direct link to Current versions used in usage based workers")

Last update: November 13th, 2023.

1. puppeteer version: `21.4.1`
2. chromedriver: `118.0.5993.70`
3. playwright-core: `1.33.0`, `1.34.3`, `1.35.1`, `1.36.2`, `1.37.1`, and `1.38.1`

info

If your code is mysteriously crashing, try using the exact version mentioned above, as some older but especially more recent versions than the above may cause conflicts.

## Global timeout [​](https://docs.browserless.io/baas/v1/hosted-service/versions\#global-timeout "Direct link to Global timeout")

By default, the global timeout is set to 15 minutes for usage-based and cloud unit-based API Keys, if you need your sessions to run longer than that, you'll want to consider upgrading to a dedicated account in order to modify this setting.

## CLI flags supported [​](https://docs.browserless.io/baas/v1/hosted-service/versions\#cli-flags-supported "Direct link to CLI flags supported")

```codeBlockLines_p187
--proxy-server,
--window-size,
--disable-web-security,
--enable-features,
--disable-web-security,
--disable-setuid-sandbox,
--lang,
--font-render-hinting,
--force-color-profile,
stealth,
ignoreDefaultArgs,
headless,
token,
blockAds,
ignoreHTTPSErrors,
slowMo,

```

## Playwright's versioning [​](https://docs.browserless.io/baas/v1/hosted-service/versions\#playwrights-versioning "Direct link to Playwright's versioning")

It is important to note that Playwright's [`connect` method](https://playwright.dev/docs/api/class-browsertype#browser-type-connect) is tightly version-coupled. Your client version must be either `1.33.0`, `1.34.3`, `1.35.1`, `1.36.2`, `1.37.1`, or `1.38.1`

Playwright's `connectOverCDP` doesn't always need to match the same playwright version on our usage based workers. This method is generally backwards/forwards compatible since it communicates directly through CDP, with the caveat to be slightly slower due to having more communication over the devtools protocol.

- [Current versions used in usage based workers](https://docs.browserless.io/baas/v1/hosted-service/versions#current-versions-used-in-usage-based-workers)
- [Global timeout](https://docs.browserless.io/baas/v1/hosted-service/versions#global-timeout)
- [CLI flags supported](https://docs.browserless.io/baas/v1/hosted-service/versions#cli-flags-supported)
- [Playwright's versioning](https://docs.browserless.io/baas/v1/hosted-service/versions#playwrights-versioning)