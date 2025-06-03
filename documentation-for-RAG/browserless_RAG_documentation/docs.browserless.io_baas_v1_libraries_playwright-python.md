---
url: "https://docs.browserless.io/baas/v1/libraries/playwright-python"
title: "Python (Playwright) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/playwright-python#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start#connecting-playwright) or [BrowserQL](https://docs.browserless.io/browserql/start).

We support `playwright` for Python out of the box via their `playwright.chromium().connect_over_cdp` method.

Here's a simple snippet of its implementation, we can add additional features through the context, such as a proxy, shown below as well, feel free to remove that if you're not going to use one.

Find more of the [playwright documentation for python here.](https://playwright.dev/python/docs/api/class-browsercontext)

```codeBlockLines_p187
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  browser = p.chromium.connect_over_cdp('wss://chrome.browserless.io?token=your_token')
  context = browser.new_context()
  page = context.new_page()
  page.goto('http://www.example.com',wait_until='domcontentloaded')
  print(page.content())
  context.close()

```

## Built-in proxy [​](https://docs.browserless.io/baas/v1/libraries/playwright-python\#built-in-proxy "Direct link to Built-in proxy")

Use our in-built residential proxies seamlessly, which will consume units from your subscription, more info here.
Your connection would look like this

```codeBlockLines_p187
  browser = p.chromium.connect_over_cdp('wss://chrome.browserless.io?token=your_token&proxy=residential&proxySticky&proxyCountry=us')

```

You can set your IP address to be geolocated in a specific country with the [&proxyCountry flag](https://www.browserless.io/docs/proxying#all-proxy-options).

## Third party proxies [​](https://docs.browserless.io/baas/v1/libraries/playwright-python\#third-party-proxies "Direct link to Third party proxies")

If you want to bring your own third party proxy, add these parameters to the `new_context` as shown below.

```codeBlockLines_p187
  context = browser.new_context(
    proxy={"server": "http://proxyprovider.com:porthere", "username": "yourusername", "password": "yourpassword"}
  )

```

- [Built-in proxy](https://docs.browserless.io/baas/v1/libraries/playwright-python#built-in-proxy)
- [Third party proxies](https://docs.browserless.io/baas/v1/libraries/playwright-python#third-party-proxies)