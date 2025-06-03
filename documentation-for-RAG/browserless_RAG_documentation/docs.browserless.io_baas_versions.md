---
url: "https://docs.browserless.io/baas/versions"
title: "Versions on the shared fleet | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/versions#__docusaurus_skipToContent_fallback)

Version: v2

On this page

Our workers that service plans such as the Starter and Scale plans are updated every so often, here are the versions that the hosted version currently has for certain libraries, global timeout and CLI flags supported.

## Current versions used in usage based workers [​](https://docs.browserless.io/baas/versions\#current-versions-used-in-usage-based-workers "Direct link to Current versions used in usage based workers")

Last update: February 24, 2025.

1. **Puppeteer**: `24.2.1`
2. **Playwright**: `1.50.1`, `1.49.1`, `1.48.2`, `1.47.2`, `1.46.1`, `1.45.3`, `1.44.1`, `1.43.1`, `1.42.1`, `1.41.2`
3. **Chromium**: `133.0.6943.16`
4. **Chrome**: `133.0.6943.127`
5. **Firefox**: `134.0`
6. **Webkit**: `18.2`

info

If your code is mysteriously crashing, try using the exact version mentioned above, as some older but especially more recent versions than the above may cause conflicts.

## Global timeout [​](https://docs.browserless.io/baas/versions\#global-timeout "Direct link to Global timeout")

By default, the global timeout is set to 15 minutes for usage-based and cloud unit-based API Keys, if you need your sessions to run longer than that, you'll want to consider upgrading to a dedicated account in order to modify this setting.

## CLI flags supported [​](https://docs.browserless.io/baas/versions\#cli-flags-supported "Direct link to CLI flags supported")

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

## Playwright's versioning [​](https://docs.browserless.io/baas/versions\#playwrights-versioning "Direct link to Playwright's versioning")

It is important to note that Playwright's [`connect` method](https://playwright.dev/docs/api/class-browsertype#browser-type-connect) is tightly version-coupled. Your client version must be either one of the ones listed above.

Playwright's `connectOverCDP` doesn't always need to match the same playwright version on our usage based workers. This method is generally backwards/forwards compatible since it communicates directly through CDP, with the caveat to be slightly slower due to having more communication over the devtools protocol.

- [Current versions used in usage based workers](https://docs.browserless.io/baas/versions#current-versions-used-in-usage-based-workers)
- [Global timeout](https://docs.browserless.io/baas/versions#global-timeout)
- [CLI flags supported](https://docs.browserless.io/baas/versions#cli-flags-supported)
- [Playwright's versioning](https://docs.browserless.io/baas/versions#playwrights-versioning)