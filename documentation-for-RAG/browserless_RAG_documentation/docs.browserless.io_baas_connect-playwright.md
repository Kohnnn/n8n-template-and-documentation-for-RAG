---
url: "https://docs.browserless.io/baas/connect-playwright"
title: "Connecting Playwright | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/connect-playwright#__docusaurus_skipToContent_fallback)

Version: v2

On this page

We support all Playwright protocols, and, just like with Puppeteer, you can easily switch to Browserless. The standard connect method uses playwright's built-in browser-server to handle the connection. This, generally, is a faster and more fully-featured method since it supports most of the playwright parameters (such as using a proxy and more).

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import playwright from "playwright";

// Connecting to Firefox locally
const browser = await playwright.firefox.launch();

// Connecting to Firefox via Browserless and using a proxy
const browser = await playwright.firefox.connect(`wss://production-sfo.browserless.io/firefox/playwright?token=${TOKEN}&proxy=residential`);

```

```codeBlockLines_p187
from playwright.sync_api import sync_playwright

# Connecting to Firefox locally
with sync_playwright() as p:
    browser = p.firefox.launch()

# Connecting to Firefox via Browserless with a proxy
with sync_playwright() as p:
    browser = p.firefox.connect_over_cdp(f"wss://production-sfo.browserless.io/firefox/playwright?token={TOKEN}&proxy=residential")

```

```codeBlockLines_p187
package org.example;

import com.microsoft.playwright.*;
import java.nio.file.Paths;

public class Main {
  public static void main(String[] args) {
    // Connecting to Firefox locally
    Browser browserLocal = playwright.firefox().launch();

    // Connecting to Firefox via Browserless and using a proxy
    String wsEndpoint = String.format(
      "wss://production-sfo.browserless.io/firefox/playwright?token=%s&proxy=residential",
      TOKEN
    );
    BrowserType.ConnectOptions connectOptions = new BrowserType.ConnectOptions();
    connectOptions.setWsEndpoint(wsEndpoint);
  }
}

```

```codeBlockLines_p187
using System;
using System.Threading.Tasks;
using Microsoft.Playwright;

namespace PlaywrightExample
{
    class Program
    {
        public static async Task Main(string[] args)
        {
            // Connecting to Firefox locally
            using var playwright = await Playwright.CreateAsync();
            var browserLocal = await playwright.Firefox.LaunchAsync();

            // Connecting to Firefox via Browserless and using a proxy
            using var playwright = await Playwright.CreateAsync();
            string wsEndpoint = $"wss://production-sfo.browserless.io/firefox/playwright?token={TOKEN}&proxy=residential";
            var browserRemote = await playwright.Firefox.ConnectAsync(wsEndpoint);
        }
    }
}

```

## More Playwright Details [​](https://docs.browserless.io/baas/connect-playwright\#more-playwright-details "Direct link to More Playwright Details")

Playwright is a cross-browser library written by Microsoft to aide in cross-browser testing and development.

**Warning**: To avoid errors with no apparent reason, please make sure your playwright version is compatible with one of these [versions.](https://docs.browserless.io/baas/versions)

### Using the Playwright Protocol [​](https://docs.browserless.io/baas/connect-playwright\#using-the-playwright-protocol "Direct link to Using the Playwright Protocol")

The standard `connect` method uses Playwright's built-in browser-server protocol to handle the connection. This, generally, is a faster and more fully-featured method since it supports most of the Playwright parameters (such as using a proxy and more). However, since this requires the usage of Playwright in our servers, **your client's Playwright version should match ours**.

#### Take a screenshot in Playwright with Firefox [​](https://docs.browserless.io/baas/connect-playwright\#take-a-screenshot-in-playwright-with-firefox "Direct link to Take a screenshot in Playwright with Firefox")

```codeBlockLines_p187
import playwright from "playwright-core";

const pwEndpoint = `wss://production-sfo.browserless.io/firefox/playwright?token=YOUR_API_TOKEN_HERE`;
const browser = await playwright.firefox.connect(pwEndpoint);
const context = await browser.newContext();
const page = await context.newPage();

await page.goto("https://www.whatsmybrowser.org/", { waitUntil: "domcontentloaded" });
await page.screenshot({
  path: `firefox.png`,
});

await browser.close();

```

Similarly, if you need to use another browser, just make sure the Playwright Browser object matches the endpoint.

### Using the Chrome DevTools Protocol [​](https://docs.browserless.io/baas/connect-playwright\#using-the-chrome-devtools-protocol "Direct link to Using the Chrome DevTools Protocol")

The `connectOverCDP` method allows Playwright to connect through Chrome's DevTools Protocol. While this is more functionally similar to how `puppeteer` operates, it does come with a slight performance hit since sessions are more "chatty" over the network versus Playwright's `connect`. Furthermore, **you can only use the Chrome for these connections**.

#### Take a screenshot in Playwright [​](https://docs.browserless.io/baas/connect-playwright\#take-a-screenshot-in-playwright "Direct link to Take a screenshot in Playwright")

```codeBlockLines_p187
import playwright from "playwright";

const browser = await playwright.chromium.connectOverCDP(
  "wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE"
);
const context = await browser.newContext();
const page = await context.newPage();

await page.goto("https://www.example.com/");
await page.screenshot({ path: "cdp.png" });

await browser.close();

```

### Using 3rd Party Proxies with Playwright [​](https://docs.browserless.io/baas/connect-playwright\#using-3rd-party-proxies-with-playwright "Direct link to Using 3rd Party Proxies with Playwright")

When using Playwright with browserless, you can set up a 3rd party proxy by providing proxy configuration to the `newContext()` method. This is different from how proxies are handled in Puppeteer, as Playwright allows you to specify proxy settings directly at the context level:

```codeBlockLines_p187
import playwright from "playwright-core";

const browser = await playwright.chromium.connectOverCDP(
  "wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE"
);
const context = await browser.newContext({
  proxy: {
    server: "http://domain:port",
    username: "username",
    password: "password",
  },
});
const page = await context.newPage();

await page.goto("https://icanhazip.com/");
console.log(await page.content());

await browser.close();

```

This approach applies the proxy configuration at the context level, which means all pages created from that context will use the specified proxy. For more detailed information about using proxies with Playwright, see our [Proxies](https://docs.browserless.io/baas/proxies) documentation.

- [More Playwright Details](https://docs.browserless.io/baas/connect-playwright#more-playwright-details)
  - [Using the Playwright Protocol](https://docs.browserless.io/baas/connect-playwright#using-the-playwright-protocol)
  - [Using the Chrome DevTools Protocol](https://docs.browserless.io/baas/connect-playwright#using-the-chrome-devtools-protocol)
  - [Using 3rd Party Proxies with Playwright](https://docs.browserless.io/baas/connect-playwright#using-3rd-party-proxies-with-playwright)