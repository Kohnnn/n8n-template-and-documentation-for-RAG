---
url: "https://docs.browserless.io/baas/avoid-bot-detection/stealth"
title: "How to bypass bot detection | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/avoid-bot-detection/stealth#__docusaurus_skipToContent_fallback)

Version: v2

On this page

Websites can have a different level of anti-bot mechanisms depending on the sensitivity of their data and budget. If your automation is being blocked, take action with the steps below.

## BrowserQL [​](https://docs.browserless.io/baas/avoid-bot-detection/stealth\#browserql "Direct link to BrowserQL")

You can use our query-language, BQL, which is designed to bypass sophisticated bot detection mechanisms effectively. This API allows you to specify a target URL and return data you care about: the HTML content, a `.png` screenshot or an unblocked browser session to use with Playwright or Puppeteer.

A simple cURL request to the API specifying your target website will return all the data needed to scrape it after it is done bypassing the bot detection:

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chrome/bql?token=YOUR-TOKEN-HERE' \
  --header 'Content-Type: application/json' \
  --data '{
  "query": "mutation Reconnect($url: String!) { goto(url: $url, waitUntil: networkIdle) { status } reconnect(timeout: 30000) { browserWSEndpoint } }",
  "variables": { "url": "https://example.com/" }
}'

```

You can use the content, or screenshot directly, or use the endpoint to run further actions with a library:

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const TOKEN = 'YOUR_API_TOKEN_HERE';
const url = "https://www.browserless.io/"

const unblock = async (url) => {
  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      "query": "mutation Reconnect($url: String!) { goto(url: $url, waitUntil: networkIdle) { status } reconnect(timeout: 30000) { browserWSEndpoint } }",
      "variables": { url }
    }),
  };

  const response = await fetch(
    `https://production-sfo.browserless.io/chromium/bql?token=${TOKEN}`,
    opts,
  );

  return await response.json();
};

// Reconnect
const { data } = await unblock(url);
const browser = await puppeteer.connect({
  browserWSEndpoint: data.reconnect.browserWSEndpoint + `?token=${TOKEN}`,
});
const pages = await browser.pages();

const page = pages.find((p) => p.url() === url);
await page.screenshot({ path: `screenshot-${Date.now()}.png` });
await browser.close();

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import { chromium } from "playwright-core";

const TOKEN = 'YOUR_API_TOKEN_HERE';
const url = "https://www.browserless.io/";

const unblock = async (url) => {
  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      "query": "mutation Reconnect($url: String!) { goto(url: $url, waitUntil: networkIdle) { status } reconnect(timeout: 30000) { browserWSEndpoint } }",
      "variables": { url }
    }),
  };

  const response = await fetch(
    `https://production-sfo.browserless.io/chromium/bql?token=${TOKEN}`,
    opts,
  );

  return await response.json();
};

const { data } = await unblock(url);

const browser = await chromium.connectOverCDP(data.reconnect.browserWSEndpoint + `?token=${TOKEN}`);
const pages = browser.contexts()[0].pages();

const page = pages.find((p) => p.url() === url);
await page.screenshot({ path: `screenshot-${Date.now()}.png` });
await browser.close();

```

```codeBlockLines_p187
import asyncio
import requests
from playwright.async_api import async_playwright

TOKEN = "YOUR_API_TOKEN_HERE"
url = "https://www.browserless.io/"

def unblock(url):
    opts = {
        "query": """mutation Reconnect($url: String!) {
            goto(url: $url, waitUntil: networkIdle) { status }
            reconnect(timeout: 30000) { browserWSEndpoint }
        }""",
        "variables": {"url": url},
    }

    response = requests.post(
        f"https://production-sfo.browserless.io/chromium/bql?token={TOKEN}",
        json=opts,
        headers={"Content-Type": "application/json"},
    )

    response.raise_for_status()
    return response.json()

async def main():
    data = unblock(url)["data"]

    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(
            data["reconnect"]["browserWSEndpoint"] + f"?token={TOKEN}"
        )
        context = browser.contexts[0]
        page = next((p for p in context.pages if p.url == url), None)
        await page.screenshot(path="screenshot.png")
        await browser.close()

asyncio.run(main())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;
import java.net.http.*;
import java.net.URI;
import java.net.http.HttpClient;
import java.util.Map;
import com.google.gson.Gson;

public class PlaywrightExample {
    private static final String TOKEN = "YOUR_API_TOKEN_HERE";
    private static final String URL = "https://www.browserless.io/";

    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        Map<String, Object> payload = Map.of(
            "query", """
                mutation Reconnect($url: String!) {
                    goto(url: $url, waitUntil: networkIdle) { status }
                    reconnect(timeout: 30000) { browserWSEndpoint }
                }
            """,
            "variables", Map.of("url", URL)
        );

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://production-sfo.browserless.io/chromium/bql?token=" + TOKEN))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(new Gson().toJson(payload)))
            .build();

        System.out.println("Unblocking " + URL);
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) {
            throw new Exception("Error: " + response.body());
        }

        String browserWSEndpoint = new Gson().fromJson(response.body(), Map.class)
            .get("data").get("reconnect").get("browserWSEndpoint").toString();

        System.out.println("Connecting to Playwright...");
        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(browserWSEndpoint);
            Page page = browser.contexts().get(0).pages().stream()
                .filter(p -> p.url().equals(URL))
                .findFirst()
                .orElseThrow(() -> new Exception("Page not found"));

            page.screenshot(new Page.ScreenshotOptions().setPath("screenshot.png"));
        }

        System.out.println("Done!");
    }
}

```

```codeBlockLines_p187
using System;
using System.Net.Http;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using Microsoft.Playwright;

class Program
{
    private const string TOKEN = "YOUR_API_TOKEN_HERE";
    private const string URL = "https://www.browserless.io/";

    static async Task Main(string[] args)
    {
        var httpClient = new HttpClient();
        var payload = new
        {
            query = @"
                mutation Reconnect($url: String!) {
                    goto(url: $url, waitUntil: networkIdle) { status }
                    reconnect(timeout: 30000) { browserWSEndpoint }
                }",
            variables = new { url = URL }
        };

        var requestContent = new StringContent(JsonSerializer.Serialize(payload), System.Text.Encoding.UTF8, "application/json");
        var response = await httpClient.PostAsync($"https://production-sfo.browserless.io/chromium/bql?token={TOKEN}", requestContent);

        if (!response.IsSuccessStatusCode)
        {
            Console.WriteLine($"Error: {await response.Content.ReadAsStringAsync()}");
            return;
        }

        var jsonResponse = JsonSerializer.Deserialize<JsonElement>(await response.Content.ReadAsStringAsync());
        var browserWSEndpoint = jsonResponse.GetProperty("data").GetProperty("reconnect").GetProperty("browserWSEndpoint").GetString();

        var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync(browserWSEndpoint + $"?token={TOKEN}");
        var context = browser.Contexts[0];
        var page = context.Pages[0];

        Console.WriteLine("Taking screenshot...");
        await page.ScreenshotAsync(new PageScreenshotOptions { Path = "screenshot.png" });

        await browser.CloseAsync();
        Console.WriteLine("Done!");
    }
}

```

## Additional strategies [​](https://docs.browserless.io/baas/avoid-bot-detection/stealth\#additional-strategies "Direct link to Additional strategies")

If none of these do the trick, get in touch with us at [support@browserless.io](mailto:support@browserless.io) >.

We have more trick up our sleeves we can show you, such as captcha solving, [BQL methods](https://docs.browserless.io/browserql/avoid-bot-detection/bypass-tough-bot-detection), and special infrastructure on our enterprise plans.

## Try out the Stealth routes [​](https://docs.browserless.io/baas/avoid-bot-detection/stealth\#try-out-the-stealth-routes "Direct link to Try out the Stealth routes")

info

The stealth routes below are for only for paid cloud-unit or Enterprise plans.

We have native support for things like puppeteer-stealth, but also offer our own stealth routes that encompass more stealthy behaviors. We use a route path semantic for this, and today this only supports libraries that work over the Chrome Devtools Protocol.

- Puppeteer
- Playwright

```codeBlockLines_p187
// Chromium:
await puppeteer.connect({
  browserWSEndpoint:
    "wss://production-sfo.browserless.io/chromium/stealth?token=YOUR_API_TOKEN_HERE",
});

// Chrome:
await puppeteer.connect({
  browserWSEndpoint:
    "wss://production-sfo.browserless.io/chrome/stealth?token=YOUR_API_TOKEN_HERE",
});

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
// Chromium
const chromiumBrowser = await playwright.chromium.connectOverCDP(
  "wss://production-sfo.browserless.io/chromium/stealth?token=YOUR_API_TOKEN_HERE"
);

// Chrome
const chromeBrowser = await playwright.chromium.connectOverCDP(
  "wss://production-sfo.browserless.io/chrome/stealth?token=YOUR_API_TOKEN_HERE"
);

```

```codeBlockLines_p187
import asyncio
from playwright.async_api import async_playwright

CHROMIUM_URL = "wss://production-sfo.browserless.io/chromium/stealth?token=YOUR_API_TOKEN_HERE"
CHROME_URL = "wss://production-sfo.browserless.io/chrome/stealth?token=YOUR_API_TOKEN_HERE"

async def main():
    async with async_playwright() as p:
        # Chromium
        chromium_browser = await p.chromium.connect_over_cdp(CHROMIUM_URL)

        # Chrome
        chrome_browser = await p.chromium.connect_over_cdp(CHROME_URL)

asyncio.run(main())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;

public class PlaywrightConnectExample {
    public static void main(String[] args) {
        String CHROMIUM_URL = "wss://production-sfo.browserless.io/chromium/stealth?token=YOUR_API_TOKEN_HERE";
        String CHROME_URL = "wss://production-sfo.browserless.io/chrome/stealth?token=YOUR_API_TOKEN_HERE";

        try (Playwright playwright = Playwright.create()) {
            // Chromium
            Browser chromiumBrowser = playwright.chromium().connectOverCDP(CHROMIUM_URL);

            // Chrome
            Browser chromeBrowser = playwright.chromium().connectOverCDP(CHROME_URL);
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
        string chromiumUrl = "wss://production-sfo.browserless.io/chromium/stealth?token=YOUR_API_TOKEN_HERE";
        string chromeUrl = "wss://production-sfo.browserless.io/chrome/stealth?token=YOUR_API_TOKEN_HERE";

        var playwright = await Playwright.CreateAsync();

        // Chromium
        var chromiumBrowser = await playwright.Chromium.ConnectOverCDPAsync(chromiumUrl);

        // Chrome
        var chromeBrowser = await playwright.Chromium.ConnectOverCDPAsync(chromeUrl);
    }
}

```

These routes incorporate many of the anti-detection mechanisms below, which you're free to try as well.

## Launch args to bypass bot detection [​](https://docs.browserless.io/baas/avoid-bot-detection/stealth\#launch-args-to-bypass-bot-detection "Direct link to Launch args to bypass bot detection")

### Use the `headless` arg [​](https://docs.browserless.io/baas/avoid-bot-detection/stealth\#use-the-headless-arg "Direct link to use-the-headless-arg")

Most bot detectors will check your user-agent, which by default explicitly claims you're running headless chrome. This is a dead giveaway. It can be changed by setting a specific user-agent but we highly recommend you use the &headless=false flag instead, which changes your user-agent to a more credible one.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const launchArgs = JSON.stringify({ headless: false });
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`,
});

//...

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import { chromium } from "playwright-core";

const launchArgs = JSON.stringify({ headless: false });
const browser = await chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`
);

// ...

```

```codeBlockLines_p187
import asyncio
from playwright.async_api import async_playwright

LAUNCH_ARGS = '{"headless": false}'
WS_ENDPOINT = f"wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch={LAUNCH_ARGS}"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(WS_ENDPOINT)

        # ...

asyncio.run(main())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;

public class PlaywrightConnectExample {
    public static void main(String[] args) {
        String launchArgs = "{\"headless\": false}";
        String WS_ENDPOINT = "wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=" + launchArgs;

        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(WS_ENDPOINT);

            // ...

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
        string launchArgs = "{\"headless\": false}";
        string wsEndpoint = $"wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch={launchArgs}";

        var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync(wsEndpoint);

        // ...
    }
}

```

### Use the `stealth` arg [​](https://docs.browserless.io/baas/avoid-bot-detection/stealth\#use-the-stealth-arg "Direct link to use-the-stealth-arg")

The stealth flag implements Puppeteer's puppeteer-extra-plugin-stealth plugin which applies various techniques to make detection of headless puppeteer harder. This flag may backfire and be easily detected by some sites, so consider avoiding it as well.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const launchArgs = JSON.stringify({ stealth: true });
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`,
});

//...

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import { chromium } from "playwright-core";

const launchArgs = JSON.stringify({ stealth: true });
const browser = await chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`
);

// ...

```

```codeBlockLines_p187
import asyncio
from playwright.async_api import async_playwright

LAUNCH_ARGS = '{"stealth": true}'
WS_ENDPOINT = f"wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch={LAUNCH_ARGS}"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(WS_ENDPOINT)

        # ...

asyncio.run(main())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;

public class PlaywrightConnectExample {
    public static void main(String[] args) {
        String launchArgs = "{\"stealth\": true}";
        String WS_ENDPOINT = "wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=" + launchArgs;

        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(WS_ENDPOINT);

            // ...

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
        string launchArgs = "{\"stealth\": true}";
        string wsEndpoint = $"wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch={launchArgs}";

        var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync(wsEndpoint);

        // ...
    }
}

```

### Use a proxy [​](https://docs.browserless.io/baas/avoid-bot-detection/stealth\#use-a-proxy "Direct link to Use a proxy")

Finally, the hardest sites to crack down check your IP address; there are two type of bocks that can occur, those based on type of IP, and those based on frequency of requests (rate-limits).

- Sites checking the type of IP address will detect your data-center IP addresses when using Browserless. To overcome this, using a proxy with residential IP addresses will be the best option.
- Sites that work the first few times and then stop working, are probably rate-limiting and it's not the residential part of it that blocks us. For these cases, you don't necessarily need a residential proxy and data-center IP addresses that rotate should be enough.

Browserless offers a residential proxy API that you can easily incorporate into your scripts.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const browserWSEndpoint = "wss://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us&proxySticky";
const browser = await puppeteer.connect({ browserWSEndpoint });

//...

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import { chromium } from "playwright-core";

const browserWSEndpoint = "wss://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us&proxySticky";
const browser = await chromium.connectOverCDP(browserWSEndpoint);

// ...

```

```codeBlockLines_p187
import asyncio
from playwright.async_api import async_playwright

WS_ENDPOINT = "wss://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us&proxySticky"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(WS_ENDPOINT)

        # ...

asyncio.run(main())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;

public class PlaywrightConnectExample {
    public static void main(String[] args) {
        String WS_ENDPOINT = "wss://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us&proxySticky";

        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(WS_ENDPOINT);

            // ...

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
        string wsEndpoint = "wss://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us&proxySticky";

        var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync(wsEndpoint);

        // ...
    }
}

```

Utilizing proxies remains a crucial strategy in bypassing bot detection. Depending on the site's mechanism, you might need a proxy with residential IP addresses or a data-center IP that rotates. For more information about these topics, please check our documentation on [our built-in proxy](https://www.browserless.io/docs/proxying) and [third-party proxy](https://www.browserless.io/docs/using-a-proxy).

- [BrowserQL](https://docs.browserless.io/baas/avoid-bot-detection/stealth#browserql)
- [Additional strategies](https://docs.browserless.io/baas/avoid-bot-detection/stealth#additional-strategies)
- [Try out the Stealth routes](https://docs.browserless.io/baas/avoid-bot-detection/stealth#try-out-the-stealth-routes)
- [Launch args to bypass bot detection](https://docs.browserless.io/baas/avoid-bot-detection/stealth#launch-args-to-bypass-bot-detection)
  - [Use the `headless` arg](https://docs.browserless.io/baas/avoid-bot-detection/stealth#use-the-headless-arg)
  - [Use the `stealth` arg](https://docs.browserless.io/baas/avoid-bot-detection/stealth#use-the-stealth-arg)
  - [Use a proxy](https://docs.browserless.io/baas/avoid-bot-detection/stealth#use-a-proxy)