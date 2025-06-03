---
url: "https://docs.browserless.io/baas/libraries/pyppeteer"
title: "Pyppeteer (Python) - UNMAINTAINED | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/libraries/pyppeteer#__docusaurus_skipToContent_fallback)

Version: v2

warning

We suggest not using this library anymore as it is now unmaintained, please consider [playwright-python](https://www.browserless.io/docs/playwright#python-playwright) as an alternative

You can use your existing python infrastructure today with browserless by using [Pyppeteer](https://github.com/pyppeteer/pyppeteer), an unofficial python port of puppeteer.

Below is a small example of getting started:

```codeBlockLines_p187
import asyncio
import pyppeteer

async def main():
  browser = await pyppeteer.launcher.connect(
    browserWSEndpoint='wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE'
    )
  page = await browser.newPage()
  url = "https://www.example.com"
  await page.goto(url)
  values = await page.evaluate('''() => document.querySelector('h1').innerHTML
    ''')
  print(values)
  await browser.close()

asyncio.get_event_loop().run_until_complete(main())

```

This will simply navigate to the example website and return the title, however it'll give you a great starting place for using Pyppeteer alongside browserless.

Be sure to [let us know if you have questions or issues](https://www.browserless.io/contact).