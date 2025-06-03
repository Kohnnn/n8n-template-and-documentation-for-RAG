---
url: "https://docs.browserless.io/baas/v1/libraries/playwright"
title: "Playwright | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/playwright#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start#connecting-playwright) or [BrowserQL](https://docs.browserless.io/browserql/start).

`playwright` is a new cross-browser library written by Microsoft to aide in cross-browser testing and development. This page helps you get started quickly connecting remotely to browserless instead of launching browsers locally. You can find more detailed documentation on [playwright's documentation site](https://playwright.dev/docs/api/class-browsertype#browser-type-connect-over-cdp).

We support playwright in several languages:

- [Javascript](https://docs.browserless.io/baas/v1/libraries/playwright#javascript-playwright)
- [Java](https://docs.browserless.io/baas/v1/libraries/playwright#java-playwright)
- [C#.NET](https://docs.browserless.io/baas/v1/libraries/playwright#cnet-playwright)
- [Python](https://docs.browserless.io/baas/v1/libraries/playwright#python-playwright)

> NOTE: To avoid errors with no apparent reason, please make sure your playwright version is compatible with one of these [versions.](https://www.browserless.io/docs/versions#playwrights-versioning).

## Javascript playwright [​](https://docs.browserless.io/baas/v1/libraries/playwright\#javascript-playwright "Direct link to Javascript playwright")

We support `playwright` for Javascript out of the box via their `pw.chromium.connect` method. As of now, we only support their `chromium` option, but we're working on other browsers as well.

browserless supports two different methods for connecting via playwright, each with its own benefits and drawbacks. In short, there are two API methods that we support:

### `playwright.chromium.connect(wsEndpoint: string)` [​](https://docs.browserless.io/baas/v1/libraries/playwright\#playwrightchromiumconnectwsendpoint-string "Direct link to playwrightchromiumconnectwsendpoint-string")

The standard `connect` method uses playwright's built-in browser-server to handle the connection. This, generally, is a faster and more fully-featured method since it supports most of the playwright parameters (such as using a proxy and more). However, since this requires the usage of playwright in our implementation, things like ad-blocking and stealth aren't supported. In order to utilize those, you'll need to see our integration with `connectOverCDP`.

> NOTE: If you are using a usage-based or cloud unit-based API key, your playwright version must match one of our supported versions, read more info on [playwright compatible versions.](https://www.browserless.io/docs/versions)

**Take a screenshot in playwright**

```codeBlockLines_p187
const pw = require('playwright');

(async () => {
  const browser = await pw.chromium.connect(
    'wss://chrome.browserless.io/playwright?token=YOUR-API-TOKEN'
  );
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://www.example.com/');
  await page.screenshot({ path: 'example.png' });

  await browser.close();
})();

```

### `playwright.chromium.connectOverCDP(wsEndpoint: string)` [​](https://docs.browserless.io/baas/v1/libraries/playwright\#playwrightchromiumconnectovercdpwsendpoint-string "Direct link to playwrightchromiumconnectovercdpwsendpoint-string")

The "connectOverCDP" endpoint allows playwright to connect through Chrome's DevTools Protocol. While this is more functionally similar to how puppeteer operates, it does come with a slight performance hit since sessions are more "chatty" over the network versus playwright's `connect`. Because it's similar to puppeteer, you can use one of our built-in helpers like ad-blocking or stealth to your session. If you're wanting to use playwright's proxy helper then you'll need to use the `connect` method instead.

**Take a screenshot in playwright**

```codeBlockLines_p187
const pw = require('playwright');

(async () => {
  const browser = await pw.chromium.connectOverCDP(
    'wss://chrome.browserless.io?token=YOUR-API-TOKEN'
  );
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('https://www.example.com/');
  await page.screenshot({ path: 'example.png' });

  await browser.close();
})();

```

## Java playwright [​](https://docs.browserless.io/baas/v1/libraries/playwright\#java-playwright "Direct link to Java playwright")

We support `playwright` for Java out of the box via their `playwright.chromium().connectOverCDP` method. As of now, we only support their `chromium` option, but we're working on other browsers as well.

Here's a simple snippet of its implementation.

**Scrape a site title with playwright**

```codeBlockLines_p187
import com.microsoft.playwright.*;

 public class Main {
   public static void main(String[] args) {
    try (Playwright playwright = Playwright.create()) {
      BrowserType chromium = playwright.chromium();
      Browser browser = playwright.chromium().connectOverCDP("wss://chrome.browserless.io?token=YOUR-API-TOKEN");
      Page page = browser.newPage();
      page.navigate("https://example.com");
      System.out.println(page.title());
      browser.close();
    }
     catch(Exception exception){
       System.out.println(exception);
     }
  }
}

```

### Alternate method that allows using authenticated proxies [​](https://docs.browserless.io/baas/v1/libraries/playwright\#alternate-method-that-allows-using-authenticated-proxies "Direct link to Alternate method that allows using authenticated proxies")

Here's a slightly more complex way to instantiate the page through a context. This technique is useful because we can apply options to the context, such as a proxy.

**Use a proxy with remote playwright**

```codeBlockLines_p187
import com.microsoft.playwright.Browser;
import com.microsoft.playwright.Page;
import com.microsoft.playwright.Playwright;
import com.microsoft.playwright.options.*;

public class Main {
  public static void main(String[] args) {
    try {
      Playwright playwright = Playwright.create();
      Browser browser = playwright.chromium().connectOverCDP("wss://chrome.browserless.io?token=YOUR-API-TOKEN");
      var context = browser.newContext(new Browser.NewContextOptions()
        .setProxy(new Proxy("https://YOUR-PROXY-SERVER-DOMAIN:PORT")
          .setUsername("proxyUsername")
          .setPassword("proxyPassword")));

      Page page = context.newPage();
      page.navigate("https://www.whatismyip.com/", new Page.NavigateOptions()
                    .setWaitUntil(WaitUntilState.DOMCONTENTLOADED));
      String myIP = page.innerHTML(".the-ipv4");
      System.out.println(myIP);
      browser.close();
    } catch (Exception exception) {
      exception.printStackTrace();
    }
  }
}

```

## C\#.NET Playwright [​](https://docs.browserless.io/baas/v1/libraries/playwright\#cnet-playwright "Direct link to C\#.NET Playwright")

We support `playwright` for C#.NET out of the box via their `playwright.Chromium.connectOverCDPAsync` method. As of now, we only support their `chromium` option, but we're working on other browsers as well.

**Take a screenshot in playwright**

```codeBlockLines_p187
using Microsoft.Playwright;
using System.Threading.Tasks;
using System;

class Program
{
    public static async Task Main()
    {
        try{
          using var playwright = await Playwright.CreateAsync();
          await using var browser = await playwright.Chromium.ConnectOverCDPAsync("wss://chrome.browserless.io?token=YOUR-API-TOKEN");
          var page = await browser.NewPageAsync();
          await page.GotoAsync("https://example.com/", new PageGotoOptions { WaitUntil = WaitUntilState.NetworkIdle });
          await page.ScreenshotAsync(new PageScreenshotOptions { Path = "example.png" });
        }
        catch (Exception e){
        Debug.WriteLine(e.ToString());
      }
    }
}

```

## Python playwright [​](https://docs.browserless.io/baas/v1/libraries/playwright\#python-playwright "Direct link to Python playwright")

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

**Use a proxy with remote playwright in Python**

Simply add the proxy parameter to the `new_context` as shown below.

```codeBlockLines_p187
  context = browser.new_context(
    proxy={"server": "http://proxyprovider.com:porthere", "username": "yourusername", "password": "yourpassword"}
  )

```

You can use all the same APIs and helper functions directly with browserless, and begin to scale out your `playwright` applications and tests today.

What's more, [is that you can use all of the same launch arguments for puppeteer](https://docs.browserless.io/baas/v1/options/chrome-flags), directly with `playwright` and `connectOverCDP`!

- [Javascript playwright](https://docs.browserless.io/baas/v1/libraries/playwright#javascript-playwright)
  - [`playwright.chromium.connect(wsEndpoint: string)`](https://docs.browserless.io/baas/v1/libraries/playwright#playwrightchromiumconnectwsendpoint-string)
  - [`playwright.chromium.connectOverCDP(wsEndpoint: string)`](https://docs.browserless.io/baas/v1/libraries/playwright#playwrightchromiumconnectovercdpwsendpoint-string)
- [Java playwright](https://docs.browserless.io/baas/v1/libraries/playwright#java-playwright)
  - [Alternate method that allows using authenticated proxies](https://docs.browserless.io/baas/v1/libraries/playwright#alternate-method-that-allows-using-authenticated-proxies)
- [C#.NET Playwright](https://docs.browserless.io/baas/v1/libraries/playwright#cnet-playwright)
- [Python playwright](https://docs.browserless.io/baas/v1/libraries/playwright#python-playwright)