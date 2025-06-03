---
url: "https://docs.browserless.io/baas/avoid-bot-detection/captchas"
title: "Solving Captchas | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/avoid-bot-detection/captchas#__docusaurus_skipToContent_fallback)

Version: v2

On this page

info

Looking for full developer docs? [See them here](https://docs.browserless.io/open-api#section/The-Browserless-CDP-API/Browserless.solveCaptcha).
This feature is only available on the Scale plan and Enterprise plans.

Some sites won't allow you to bypass their captchas or strictly enforce them to be solved on some sites. You can solve these captchas with Browserless without much effort. You can have a listener waiting to see if a captcha is found and you can also solve them programmatically.

Every captcha you solve costs 10 units from your plan.

note

Many passive captchas can be prevented from showing with our [**BrowserQL**](https://docs.browserless.io/browserql/start), that hides signs of browser automation.

## Find a captcha programmatically [​](https://docs.browserless.io/baas/avoid-bot-detection/captchas\#find-a-captcha-programmatically "Direct link to Find a captcha programmatically")

You can listen for captchas on the site, in puppeteer it would be like this:

- Puppeteer
- Playwright

```codeBlockLines_p187
const cdp = await page.createCDPSession();
await new Promise((resolve) =>
  cdp.on("Browserless.captchaFound", () => {
    console.log("Found a captcha!");
    return resolve();
  })
);

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
const cdp = await page.context().newCDPSession(page);

await new Promise((resolve) =>
  cdp.on("Browserless.captchaFound", () => {
    console.log("Found a captcha!");
    return resolve();
  })
);

```

```codeBlockLines_p187
cdp = await page.context.new_cdp_session(page)

async def handle_captcha_found(event):
    print("Found a captcha!")
    return

cdp.on("Browserless.captchaFound", handle_captcha_found)

# Wait for the event to resolve
await asyncio.Future()

```

```codeBlockLines_p187
CDPSession cdp = page.context().newCDPSession(page);

cdp.addListener("Browserless.captchaFound", event -> {
    System.out.println("Found a captcha!");
    // You can add additional handling logic here
});

```

```codeBlockLines_p187
var cdp = await page.Context.NewCDPSessionAsync(page);

cdp.On("Browserless.captchaFound", e =>
{
    Console.WriteLine("Found a captcha!");
    // Additional logic can be added here
});

```

## Solve a captcha programmatically [​](https://docs.browserless.io/baas/avoid-bot-detection/captchas\#solve-a-captcha-programmatically "Direct link to Solve a captcha programmatically")

You can solve the captcha from code, in puppeteer it would be like this:

- Puppeteer
- Playwright

```codeBlockLines_p187
const cdp = await page.createCDPSession();
const { solved, error } = await cdp.send("Browserless.solveCaptcha");
console.log({
  solved,
  error,
});

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
const cdp = await page.context().newCDPSession(page);

const { solved, error } = await cdp.send("Browserless.solveCaptcha");
console.log({
  solved,
  error,
});

```

```codeBlockLines_p187
cdp = await page.context.new_cdp_session(page)

result = await cdp.send("Browserless.solveCaptcha")
solved = result.get("solved")
error = result.get("error")

print({
    "solved": solved,
    "error": error,
})

```

```codeBlockLines_p187
CDPSession cdp = page.context().newCDPSession(page);

Map<String, Object> result = cdp.send("Browserless.solveCaptcha");
Boolean solved = (Boolean) result.get("solved");
String error = (String) result.get("error");

System.out.println(Map.of(
    "solved", solved,
    "error", error
));

```

```codeBlockLines_p187
var cdp = await page.Context.NewCDPSessionAsync(page);

var result = await cdp.SendAsync<Dictionary<string, object>>("Browserless.solveCaptcha");
var solved = result.ContainsKey("solved") ? result["solved"] : null;
var error = result.ContainsKey("error") ? result["error"] : null;

Console.WriteLine(new {
    solved,
    error
});

```

## Script Examples [​](https://docs.browserless.io/baas/avoid-bot-detection/captchas\#script-examples "Direct link to Script Examples")

### Puppeteer [​](https://docs.browserless.io/baas/avoid-bot-detection/captchas\#puppeteer "Direct link to Puppeteer")

Here's a sample snippet you can run to demonstrate this works.

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const waitForCaptcha = (cdpSession) => {
  return new Promise((resolve) =>
    cdpSession.on("Browserless.captchaFound", resolve)
  );
};

const browserWSEndpoint =
  "wss://production-sfo.browserless.io/chromium?token=YOUR_API_TOKEN_HERE&timeout=300000";

try {
  const browser = await puppeteer.connect({ browserWSEndpoint });

  const page = await browser.newPage();
  const cdp = await page.createCDPSession();

  await page.goto("https://www.google.com/recaptcha/api2/demo", {
    waitUntil: "networkidle0",
  });

  await waitForCaptcha(cdp);
  console.log("Captcha found!");

  const { solved, error } = await cdp.send("Browserless.solveCaptcha");
  console.log({ solved, error });

  // Continue...
  await page.click("#recaptcha-demo-submit");
  await browser.close();
} catch (e) {
  console.error("There was a big error :(", e);
  process.exit(1);
}

```

### Playwright [​](https://docs.browserless.io/baas/avoid-bot-detection/captchas\#playwright "Direct link to Playwright")

Playwright works a bit different than Puppeteer in regards to its pages, as it uses it own browser protocols to communicate. For that reason, **you'll need to connect over CDP**. And while most of the steps are the same as in Puppeteer, **you should use the default existing context and page instead of creating a new one**.

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import playwright from "playwright-core";

const waitForCaptcha = (cdpSession) => {
  return new Promise((resolve) =>
    cdpSession.on("Browserless.captchaFound", resolve)
  );
};
const pwEndpoint = `wss://production-sfo.browserless.io/chromium?token=YOUR_API_TOKEN_HERE`;

try {
  const browser = await playwright.chromium.connectOverCDP(pwEndpoint);
  // 👇 Queue we're re-using the existing context and page
  const context = browser.contexts()[0];
  const page = context.pages()[0];

  await page.goto("https://www.google.com/recaptcha/api2/demo", {
    waitUntil: "networkidle0",
  });

  const cdp = await page.context().newCDPSession(page);
  await waitForCaptcha(cdp);
  console.log("Captcha found!");

  const { solved, error } = await cdp.send("Browserless.solveCaptcha");

  console.log({ solved, error });

  // Continue...
  await page.click("#recaptcha-demo-submit");
  await browser.close();
} catch (e) {
  console.error("There was a big error :(", e);
  process.exit(1);
}

```

```codeBlockLines_p187
import asyncio
from playwright.async_api import async_playwright

async def wait_for_captcha(cdp_session):
    # Wait for the "Browserless.captchaFound" event
    future = asyncio.Future()

    def handle_captcha_found(event):
        print("Captcha found!")
        future.set_result(event)

    cdp_session.on("Browserless.captchaFound", handle_captcha_found)
    return await future

async def main():
    pw_endpoint = "wss://production-sfo.browserless.io/chromium?token=YOUR_API_TOKEN_HERE"
    async with async_playwright() as p:
        try:
            # Connect to the browser
            browser = await p.chromium.connect_over_cdp(pw_endpoint)

            # Use the first context and page
            context = browser.contexts[0]
            page = context.pages[0]

            # Navigate to the captcha demo page
            await page.goto("https://www.google.com/recaptcha/api2/demo", wait_until="networkidle")

            # Create a CDP session
            cdp = await page.context.new_cdp_session(page)

            # Wait for captcha to be found
            await wait_for_captcha(cdp)

            # Solve the captcha
            result = await cdp.send("Browserless.solveCaptcha")
            solved, error = result.get("solved"), result.get("error")
            print({"solved": solved, "error": error})

            # Continue after solving captcha
            await page.click("#recaptcha-demo-submit")
            await browser.close()
        except Exception as e:
            print("There was a big error :(", e)

asyncio.run(main())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;
import com.microsoft.playwright.options.*;

import java.util.*;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

public class PlaywrightCaptchaExample {
    public static void main(String[] args) {
        String pwEndpoint = "wss://production-sfo.browserless.io/chromium?token=YOUR_API_TOKEN_HERE";

        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(pwEndpoint);

            // Reuse the existing context and page
            BrowserContext context = browser.contexts().get(0);
            Page page = context.pages().get(0);

            // Navigate to the captcha demo page
            page.navigate("https://www.google.com/recaptcha/api2/demo", new Page.NavigateOptions()
                .setWaitUntil(LoadState.NETWORKIDLE));

            // Create a CDP session
            CDPSession cdp = page.context().newCDPSession(page);

            // Wait for captcha to be found
            CompletableFuture<Void> captchaFound = new CompletableFuture<>();
            cdp.on("Browserless.captchaFound", event -> {
                System.out.println("Captcha found!");
                captchaFound.complete(null);
            });

            captchaFound.get(); // Wait for the event

            // Solve the captcha
            Map<String, Object> result = cdp.send("Browserless.solveCaptcha");
            System.out.println("Result: " + result);

            // Continue after solving captcha
            page.click("#recaptcha-demo-submit");
            browser.close();
        } catch (ExecutionException | InterruptedException e) {
            System.err.println("There was a big error :(" + e.getMessage());
            e.printStackTrace();
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.Playwright;

class Program
{
    static async Task Main(string[] args)
    {
        var pwEndpoint = "wss://production-sfo.browserless.io/chromium?token=YOUR_API_TOKEN_HERE";

        try
        {
            var playwright = await Playwright.CreateAsync();
            var browser = await playwright.Chromium.ConnectOverCDPAsync(pwEndpoint);

            // Use the first context and page
            var context = browser.Contexts[0];
            var page = context.Pages[0];

            // Navigate to the captcha demo page
            await page.GotoAsync("https://www.google.com/recaptcha/api2/demo", new PageGotoOptions
            {
                WaitUntil = WaitUntilState.NetworkIdle
            });

            // Create a CDP session
            var cdp = await page.Context.NewCDPSessionAsync(page);

            // Wait for captcha to be found
            var captchaFound = new TaskCompletionSource<bool>();
            cdp.On("Browserless.captchaFound", _ =>
            {
                Console.WriteLine("Captcha found!");
                captchaFound.TrySetResult(true);
            });

            await captchaFound.Task;

            // Solve the captcha
            var result = await cdp.SendAsync<Dictionary<string, object>>("Browserless.solveCaptcha");
            Console.WriteLine($"Solved: {result["solved"]}, Error: {result["error"]}");

            // Continue after solving captcha
            await page.ClickAsync("#recaptcha-demo-submit");
            await browser.CloseAsync();
        }
        catch (Exception e)
        {
            Console.WriteLine("There was a big error :(");
            Console.WriteLine(e.Message);
        }
    }
}

```

- [Find a captcha programmatically](https://docs.browserless.io/baas/avoid-bot-detection/captchas#find-a-captcha-programmatically)
- [Solve a captcha programmatically](https://docs.browserless.io/baas/avoid-bot-detection/captchas#solve-a-captcha-programmatically)
- [Script Examples](https://docs.browserless.io/baas/avoid-bot-detection/captchas#script-examples)
  - [Puppeteer](https://docs.browserless.io/baas/avoid-bot-detection/captchas#puppeteer)
  - [Playwright](https://docs.browserless.io/baas/avoid-bot-detection/captchas#playwright)