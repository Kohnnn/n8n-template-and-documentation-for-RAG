---
url: "https://docs.browserless.io/baas/v1/libraries/puppeteer"
title: "Puppeteer | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/puppeteer#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start#connecting-puppeteer) or [BrowserQL](https://docs.browserless.io/browserql/start).

Puppeteer is well-supported by browserless, and is easy to upgrade an existing service or app to use it. In order to use the browserless service, simply change the following:

**Before browserless**

```codeBlockLines_p187
import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Remember to catch errors and close!
})();

```

**After browserless**

```codeBlockLines_p187
import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.connect({
    browserWSEndpoint: `wss://chrome.browserless.io/`,
  });
  const page = await browser.newPage();

  // Remember to catch errors and close!
})();

```

Please note that if you're running the docker container to replace the location of `wss://chrome.browserless.io/` to wherever your container is running.

## Specifying launch flags [​](https://docs.browserless.io/baas/v1/libraries/puppeteer\#specifying-launch-flags "Direct link to Specifying launch flags")

You can specify launch-arguments through query-string parameters inside the `browserWSEndpoint`. As an example, if you want to start the browser with a pre-defined width and height you can specify it like so:

**Setting width and height**

```codeBlockLines_p187
import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.connect({
    browserWSEndpoint: `wss://chrome.browserless.io?--window-size=1200,900`,
  });
  const page = await browser.newPage();

  // Remember to catch errors and close!
})();

```

- [Specifying launch flags](https://docs.browserless.io/baas/v1/libraries/puppeteer#specifying-launch-flags)