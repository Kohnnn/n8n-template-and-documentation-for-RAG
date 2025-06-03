---
url: "https://docs.browserless.io/baas/avoid-bot-detection/user-agent"
title: "Setting a user agent | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/avoid-bot-detection/user-agent#__docusaurus_skipToContent_fallback)

Version: v2

On this page

The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.

Many sites use this information to render the site differently for each user, and sometimes even for rudimentary bot detection. If you run chrome headless and want to take a screenshot of a page, it's a good idea to set a user agent so that web fonts load properly.

note

If you are having trouble getting past bot detectors, we would recommend trying [**BrowserQL**](https://docs.browserless.io/browserql/start).

## Using a Library [​](https://docs.browserless.io/baas/avoid-bot-detection/user-agent\#using-a-library "Direct link to Using a Library")

You can set the user agent from code, in puppeteer and playwright it would be like this:

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer";

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE`,
});
const page = await browser.newPage();
await page.setUserAgent(
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
);

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import { chromium } from "playwright-core";

(async () => {
  const browser = await chromium.connectOverCDP(
    `wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE`
  );

  const context = browser.contexts()[0] || (await browser.newContext());
  const page = await context.newPage();

  // Set User-Agent
  await context.setDefaultUserAgent(
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
  );
})();

```

```codeBlockLines_p187
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(
            "wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE"
        )

        context = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await context.new_page()

        # Set User-Agent
        await context.set_default_user_agent(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        )

asyncio.run(main())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;

public class PlaywrightExample {
    public static void main(String[] args) {
        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(
                "wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE"
            );

            BrowserContext context = browser.contexts().isEmpty()
                ? browser.newContext()
                : browser.contexts().get(0);

            // Set User-Agent
            context.setDefaultUserAgent(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
            );
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.Threading.Tasks;
using Microsoft.Playwright;

class Program
{
    static async Task Main(string[] args)
    {
        var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync(
            "wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE"
        );

        var context = browser.Contexts.Count > 0
            ? browser.Contexts[0]
            : await browser.NewContextAsync();

        // Set User-Agent
        await context.SetDefaultUserAgentAsync(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        );
    }
}

```

## REST API [​](https://docs.browserless.io/baas/avoid-bot-detection/user-agent\#rest-api "Direct link to REST API")

If you're using our APIs like /screenshot, /content, /pdf, or /scrape, you can also set the user agent in the body of your request.

```codeBlockLines_p187
// /content API
{
  "url": "https://example.com/",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15"
}

```

## As Launch Args [​](https://docs.browserless.io/baas/avoid-bot-detection/user-agent\#as-launch-args "Direct link to As Launch Args")

If you're on a usage-based, cloud unit-based or capacity-based account, you can change the user agent as so:

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const launchArgs = JSON.stringify({
  args: [\
    `--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36`,\
  ],
});

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`,
});

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import { chromium } from "playwright-core";

(async () => {
  const launchArgs = JSON.stringify({
    args: [\
      `--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36`,\
    ],
  });

  const browser = await chromium.connectOverCDP(
    `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`
  );
})();

```

```codeBlockLines_p187
import asyncio
from playwright.async_api import async_playwright

async def main():
    launch_args = {
        "args": [\
            "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"\
        ]
    }

    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(
            f"wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch={launch_args}"
        )

asyncio.run(main())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;

public class PlaywrightExample {
    public static void main(String[] args) {
        String launchArgs = "{\"args\": [\"--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\"]}";

        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(
                "wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=" + launchArgs
            );
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.Threading.Tasks;
using Microsoft.Playwright;

class Program
{
    static async Task Main(string[] args)
    {
        var launchArgs = new
        {
            args = new[]
            {
                "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
            }
        };

        string wsEndpoint = $"wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch={System.Text.Json.JsonSerializer.Serialize(launchArgs)}";

        var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync(wsEndpoint);
    }
}

```

- [Using a Library](https://docs.browserless.io/baas/avoid-bot-detection/user-agent#using-a-library)
- [REST API](https://docs.browserless.io/baas/avoid-bot-detection/user-agent#rest-api)
- [As Launch Args](https://docs.browserless.io/baas/avoid-bot-detection/user-agent#as-launch-args)