---
url: "https://docs.browserless.io/baas/session-management/reconnect"
title: "Reconnect to an existing Browser | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/session-management/reconnect#__docusaurus_skipToContent_fallback)

Version: v2

On this page

note

Looking for full developer docs? [See them here](https://docs.browserless.io/open-api#section/The-Browserless-CDP-API/Browserless.reconnect).
This feature is only available on the Enterprise plans.

Reconnecting to an existing browser is useful if you want to avoid logging in multiple times, or if you leave a process pending and want to open a websocket connection again once you're ready to resume automation, amongst other use cases.

If you want to reconnect to a browser, all you have to do is fetch the browser's websocket endpoint which you can reconnect with later. You do so by using a CDP connection to the browser and triggering the `Browserless.reconnect` CDP command, which will keep that browser alive and allow you to reconnect to it within the specified timeout. This virtually replaces the `keepalive` flag that was previously used in V1.

## Sample snippet [​](https://docs.browserless.io/baas/session-management/reconnect\#sample-snippet "Direct link to Sample snippet")

You can use the returned `browserWSEndpoint` to reconnect to a browser and continue working. The example below takes a screenshot after reconnecting:

- Puppeteer
- Playwright
- Python
- Java
- C#

```codeBlockLines_p187
import puppeteer from 'puppeteer-core';

const url = 'https://www.example.com';
const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

const queryParams = new URLSearchParams({
  token: 'YOUR_API_TOKEN_HERE',
  timeout: 60000,
}).toString();

(async () => {
  const browser = await puppeteer.connect({
    browserWSEndpoint: `wss://production-sfo.browserless.io/chromium?${queryParams}`,
  });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto(url);

  // Allow this browser to run for 1 minute, then shut down if nothing connects to it.
  // Defaults to the overall timeout set on the instance, which is 5 minutes if not specified.
  const { error, browserWSEndpoint } = await cdp.send('Browserless.reconnect', {
    timeout: 60000,
  });

  if (error) throw error;
  console.log(`${browserWSEndpoint}?${queryParams}`);

  await browser.close();
  //Reconnect using the browserWSEndpoint that was returned from the CDP command.
  const browserReconnect = await puppeteer.connect({
    browserWSEndpoint: `${browserWSEndpoint}?${queryParams}`,
  });
  const [pageReconnect] = await browserReconnect.pages();
  await pageReconnect.goto(url);
  await sleep(2000);
  await pageReconnect.screenshot({
    path: 'reconnected.png',
    fullPage: true,
  });
  await browserReconnect.close();

})().catch((e) => {
  console.error(e);
  process.exit(1);
});

```

```codeBlockLines_p187
import playwright from 'playwright-core';

const url = 'https://www.example.com';
const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

const queryParams = new URLSearchParams({
  token: 'YOUR_API_TOKEN_HERE',
  timeout: 60000,
}).toString();

(async () => {
  const browser = await playwright.chromium.connectOverCDP(
    `wss://production-sfo.browserless.io/chromium?${queryParams}`
  );
  const page = await browser.newPage();
  const cdpSession = await page.context().newCDPSession(page);
  await page.goto(url);

  // Allow this browser to run for 1 minute, then shut down if nothing connects to it.
  // Defaults to the overall timeout set on the instance, which is 5 minutes if not specified.
  const { error, browserWSEndpoint } = await cdpSession.send('Browserless.reconnect', {
    timeout: 60000,
  });

  if (error) throw new Error(error);
  console.log(`${browserWSEndpoint}?${queryParams}`);

  await browser.close();

  // Reconnect using the browserWSEndpoint that was returned from the CDP command.
  const browserReconnect = await playwright.chromium.connectOverCDP(
    `${browserWSEndpoint}?${queryParams}`
  );
  const pageReconnect = await browserReconnect.newPage();
  await pageReconnect.goto(url);
  await sleep(2000);
  await pageReconnect.screenshot({
    path: 'reconnected.png',
    fullPage: true,
  });
  await browserReconnect.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});

```

```codeBlockLines_p187
from playwright.sync_api import sync_playwright
from time import sleep

url = "https://www.example.com"
query_params = "token=YOUR_API_TOKEN_HERE&timeout=60000"
ws_endpoint = f"wss://production-sfo.browserless.io/chromium?{query_params}"

with sync_playwright() as playwright:
    # Connect to the remote Chromium browser
    browser = playwright.chromium.connect_over_cdp(ws_endpoint)
    context = browser.new_context()
    page = context.new_page()
    cdp_session = context.new_cdp_session(page)

    # Navigate to the URL
    page.goto(url)

    # Send the `Browserless.reconnect` command
    response = cdp_session.send("Browserless.reconnect", {"timeout": 60000})
    browser_ws_endpoint = response.get("browserWSEndpoint")
    if response.get("error") is not None:
        raise Exception(response["error"])

    print(f"{browser_ws_endpoint}?{query_params}")

    # Close the current browser connection
    browser.close()

    # Reconnect using the returned WebSocket endpoint
    browser_reconnect = playwright.chromium.connect_over_cdp(browser_ws_endpoint + "?" + query_params)
    context_reconnect = browser_reconnect.new_context()
    page_reconnect = context_reconnect.new_page()
    page_reconnect.goto(url)

    sleep(2)

    # Take a screenshot
    page_reconnect.screenshot(path="reconnected.png", full_page=True)

    browser_reconnect.close()

```

```codeBlockLines_p187
import com.microsoft.playwright.*;
import com.google.gson.JsonObject;
import java.nio.file.Paths;

public class App {
  public static void main(String[] args) {
    String url = "https://www.example.com";
    String token = "YOUR_API_TOKEN_HERE";
    String queryParams = String.format("token=%s&timeout=60000", token);
    String wsEndpoint = String.format("wss://production-sfo.browserless.io/chromium?%s", queryParams);

    try (Playwright playwright = Playwright.create()) {
      // Connect to the remote Chromium browser
      Browser browser = playwright.chromium().connectOverCDP(wsEndpoint);
      BrowserContext context = browser.newContext();
      Page page = context.newPage();
      CDPSession cdpSession = page.context().newCDPSession(page);

      // Navigate to the URL
      page.navigate(url);

      // Send the `Browserless.reconnect` command using a JsonObject
      JsonObject reconnectParams = new JsonObject();
      reconnectParams.addProperty("timeout", 60000);
      JsonObject response = cdpSession.send("Browserless.reconnect", reconnectParams);

      // Extract the `browserWSEndpoint` from the response
      String browserWSEndpoint = response.get("browserWSEndpoint").getAsString();
      if (response.has("error") && !response.get("error").isJsonNull()) {
        throw new RuntimeException("Error: " + response.get("error").getAsString());
      }

      System.out.println(browserWSEndpoint + "?" + queryParams);

      // Close the current browser connection
      browser.close();

      // Reconnect using the returned WebSocket endpoint
      Browser browserReconnect = playwright.chromium().connectOverCDP(browserWSEndpoint + "?" + queryParams);
      BrowserContext contextReconnect = browserReconnect.newContext();
      Page pageReconnect = contextReconnect.newPage();
      pageReconnect.navigate(url);
      Thread.sleep(2000);

      // Take a screenshot
      pageReconnect.screenshot(new Page.ScreenshotOptions()
          .setPath(Paths.get("reconnected.png"))
          .setFullPage(true));

      browserReconnect.close();
    } catch (Exception ex) {
      System.out.println("Exception: " + ex.Message);
    }
  }
}

```

```codeBlockLines_p187
using Microsoft.Playwright;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class BrowserlessReconnect
{
    public static async Task Main(string[] args)
    {
        string url = "https://www.example.com";
        string queryParams = "token=YOUR_API_TOKEN_HERE&timeout=60000";
        string wsEndpoint = $"wss://production-sfo.browserless.io/chromium?{queryParams}";

        using var playwright = await Playwright.CreateAsync();

        try
        {
            // Connect to the remote Chromium browser
            var browser = await playwright.Chromium.ConnectOverCDPAsync(wsEndpoint);
            var context = await browser.NewContextAsync();
            var page = await context.NewPageAsync();
            var cdpSession = await context.NewCDPSessionAsync(page);

            // Navigate to the URL
            await page.GotoAsync(url);

            // Send the `Browserless.reconnect` command
            var response = await cdpSession.SendAsync("Browserless.reconnect", new { timeout = 60000 });

            if (response.TryGetValue("error", out var error) && error != null)
            {
                throw new Exception($"Error: {error}");
            }

            string browserWSEndpoint = response["browserWSEndpoint"].ToString();
            System.Console.WriteLine(browserWSEndpoint + "?" + queryParams);

            // Close the current browser connection
            await browser.CloseAsync();

            // Reconnect using the returned WebSocket endpoint
            var browserReconnect = await playwright.Chromium.ConnectOverCDPAsync(browserWSEndpoint + "?" + queryParams);
            var contextReconnect = await browserReconnect.NewContextAsync();
            var pageReconnect = await contextReconnect.NewPageAsync();
            await pageReconnect.GotoAsync(url);
            await Task.Delay(2000);

            // Take a screenshot
            await pageReconnect.ScreenshotAsync(new PageScreenshotOptions
            {
                Path = "reconnected.png",
                FullPage = true
            });

            await browserReconnect.CloseAsync();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Exception: {ex.Message}");
        }
    }
}

```

## Session Timeout [​](https://docs.browserless.io/baas/session-management/reconnect\#session-timeout "Direct link to Session Timeout")

By default, your sessions are governed by a timeout. This is set via your account page for the hosted service. You can override this behavior.

- If you are running `BaaS` in Docker, you can specify a `TIMEOUT` environment variable in the `docker run` command to override the default timeout of 30 seconds.

- If you need to override the timeout on a per-job basis, simply specify a `timeout` parameter in your connect calls query-parameters, with the value being the time in milliseconds for the session to execute:



- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&timeout=10000`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&timeout=10000`
);

```

note

For other runtimes and selenium libraries be sure to consult your libraries documentation, or [contact us](https://www.browserless.io/contact)

- [Sample snippet](https://docs.browserless.io/baas/session-management/reconnect#sample-snippet)
- [Session Timeout](https://docs.browserless.io/baas/session-management/reconnect#session-timeout)