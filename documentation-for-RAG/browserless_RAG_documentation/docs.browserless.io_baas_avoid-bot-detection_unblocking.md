---
url: "https://docs.browserless.io/baas/avoid-bot-detection/unblocking"
title: "How to use the Unblock API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/avoid-bot-detection/unblocking#__docusaurus_skipToContent_fallback)

Version: v2

On this page

note

Looking for full developer docs? [See them here](https://docs.browserless.io/open-api#tag/Browser-REST-APIs/paths/~1unblock%20~1chromium~1unblock/post).

When using a library like puppeteer or playwright, there's a lot of sites out there that can detect this library usage. These libraries leave traces of their existence behind in many ways (web workers, background pages, etc). With the `/unblock` API, Browserless takes a minimalistic approach into getting past bot blocks. It uses a variety of tools and strategies that we've seen work well in the past, and includes many adapters to get past more notorious mechanisms:

- We don't use any library for this API, and work directly with the browser's native remote interfaces.
- We launch and run the browser just like end-users.
- Detection of common bot blockers are listened for and corrected.
- Returns the underlying `browserWSEndpoint` to connect to, or just content and cookies.

This JSON API is flexible in how it operates. By setting all certain values to `false`, Browserless will optimize the execution of this request to only return fields you asked for, and not spend time producing the other fields.

Here's a list of common examples:

### Returning cookies only [​](https://docs.browserless.io/baas/avoid-bot-detection/unblocking\#returning-cookies-only "Direct link to Returning cookies only")

```codeBlockLines_p187
{
    "url": "https://www.example.com/",
    "cookies": true,
    "content": false,
    "browserWSEndpoint": false,
    "screenshot": false,
    "ttl": 0
}

```

### Returning content only [​](https://docs.browserless.io/baas/avoid-bot-detection/unblocking\#returning-content-only "Direct link to Returning content only")

```codeBlockLines_p187
{
    "url": "https://www.example.com/",
    "cookies": false,
    "content": true,
    "browserWSEndpoint": false,
    "screenshot": false,
    "ttl": 0
}

```

### Returning screenshots only [​](https://docs.browserless.io/baas/avoid-bot-detection/unblocking\#returning-screenshots-only "Direct link to Returning screenshots only")

```codeBlockLines_p187
{
    "url": "https://www.example.com/",
    "cookies": false,
    "content": false,
    "browserWSEndpoint": false,
    "screenshot": true,
    "ttl": 0
}

```

### Full example with a library [​](https://docs.browserless.io/baas/avoid-bot-detection/unblocking\#full-example-with-a-library "Direct link to Full example with a library")

This API is also intended to work with libraries that run on Chrome's Devtools Protocol (like puppeteer and certain APIs in playwright). What this means is you can unblock a site, then connect your library of choice to the browser and kick off your automation. It's a powerful way to work and keeps your code more focused on your needs, rather than trying to solve management-related tasks.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from 'puppeteer-core';

// The underlying site you wish automate
const url = 'https://www.example.com/';

// Your API token retrievable from the dashboard.
const token = 'YOUR_API_TOKEN_HERE';

// Set a threshold, in milliseconds, to unblock
const timeout = 5 * 60 * 1000;

// What proxy type (residential), or remove for none.
const proxy = 'residential';

// Where you want to proxy from (GB === Great Britain), or remove for none.
const proxyCountry = 'gb';

// If you want to use the same proxy IP for every network request
const proxySticky = true;

const queryParams = new URLSearchParams({
  timeout,
  proxy,
  proxyCountry,
  proxySticky,
  token,
}).toString();

const unblockURL =
  `https://production-sfo.browserless.io/chromium/unblock?${queryParams}`;

const options = {
  method: 'POST',
  headers: {
    'content-type': 'application/json'
  },
  body: JSON.stringify({
    url: url,
    browserWSEndpoint: true,
    cookies: true,
    content: true,
    screenshot: true,
    ttl: 5000,
  }),
};

try {
  console.log(`Unblocking ${url}`);

  const response = await fetch(unblockURL, options);

  if (!response.ok) {
    throw new Error(`Got non-ok response:\n` + (await response.text()));
  }

  const { browserWSEndpoint } = await response.json();

  console.log(`Got OK response! Connecting puppeteer to "${browserWSEndpoint}"...`);
  const browser = await puppeteer.connect({
    browserWSEndpoint: `${browserWSEndpoint}?${queryParams}`
  });
  // Find the page by inspecting the URL and matching it
  const pages = await browser.pages();
  const page = pages.find((p) => p.url().includes(url));
  page.on('response', (res) => {
    if (!res.ok) {
      console.log(`${res.status()}: ${res.url()}`);
    }
  });
  console.log('Reloading page with networkidle0...');
  await page.reload({
    waitUntil: 'networkidle0',
    timeout,
  });
  console.log('Taking page screenshot...');
  await page.screenshot({
    path: 'temp.png',
    fullPage: true,
  });
  console.log('Done!');
  await browser.close();
} catch (error) {
  console.error(error);
}

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import playwright from 'playwright-core';

// The underlying site you wish automate
const url = 'https://www.example.com/';

// Your API token retrievable from the dashboard.
const token = 'YOUR_API_TOKEN_HERE';

// Set a threshold, in milliseconds, to unblock
const timeout = 5 * 60 * 1000;

// What proxy type (residential), or remove for none.
const proxy = 'residential';

// Where you want to proxy from (GB === Great Britain), or remove for none.
const proxyCountry = 'gb';

// If you want to use the same proxy IP for every network request
const proxySticky = true;

const queryParams = new URLSearchParams({
  timeout,
  proxy,
  proxyCountry,
  proxySticky,
  token,
}).toString();

const unblockURL =
  `https://production-sfo.browserless.io/chromium/unblock?${queryParams}`;

const options = {
  method: 'POST',
  headers: {
    'content-type': 'application/json'
  },
  body: JSON.stringify({
    url: url,
    browserWSEndpoint: true,
    cookies: true,
    content: true,
    screenshot: true,
    ttl: 5000,
  }),
};

try {
  console.log(`Unblocking ${url}`);

  const response = await fetch(unblockURL, options);

  if (!response.ok) {
    throw new Error(`Got non-ok response:\n` + (await response.text()));
  }

  const { browserWSEndpoint } = await response.json();

  console.log(`Got OK response! Connecting Playwright to "${browserWSEndpoint}"...`);
  const browser = await playwright.chromium.connectOverCDP({
    wsEndpoint: `${browserWSEndpoint}?${queryParams}`,
  });

  // Find the page by inspecting the URL and matching it
  const contexts = browser.contexts();
  const pages = contexts.flatMap((context) => context.pages());
  const page = pages.find((p) => p.url().includes(url));

  if (!page) {
    throw new Error(`Page with URL "${url}" not found.`);
  }

  page.on('response', (res) => {
    if (!res.ok()) {
      console.log(`${res.status()}: ${res.url()}`);
    }
  });

  console.log('Reloading page with networkidle...');
  await page.reload({
    waitUntil: 'networkidle',
    timeout,
  });

  console.log('Taking page screenshot...');
  await page.screenshot({
    path: 'temp.png',
    fullPage: true,
  });

  console.log('Done!');
  await browser.close();
} catch (error) {
  console.error(error);
}

```

```codeBlockLines_p187
import asyncio
from playwright.async_api import async_playwright
import requests

# The underlying site you wish automate
url = "https://www.example.com/"

# Your API token retrievable from the dashboard.
token = "YOUR_API_TOKEN_HERE"

# Set a threshold, in milliseconds, to unblock
timeout = 5 * 60 * 1000

# What proxy type (residential), or remove for none.
proxy = "residential"

# Where you want to proxy from (GB === Great Britain), or remove for none.
proxy_country = "gb"

# If you want to use the same proxy IP for every network request
proxy_sticky = True

# Build query parameters
query_params = {
    "timeout": timeout,
    "proxy": proxy,
    "proxyCountry": proxy_country,
    "proxySticky": proxy_sticky,
    "token": token,
}

unblock_url = "https://production-sfo.browserless.io/chromium/unblock"
options = {
    "url": url,
    "browserWSEndpoint": True,
    "cookies": True,
    "content": True,
    "screenshot": True,
    "ttl": 5000,
}

try:
    print(f"Unblocking {url}...")

    # Make the POST request
    response = requests.post(unblock_url, json=options, params=query_params)

    if response.status_code != 200:
        raise Exception(f"Non-OK response:\n{response.text}")

    response_data = response.json()
    browser_ws_endpoint = response_data.get("browserWSEndpoint")

    print(f'Got OK response! Connecting Playwright to "{browser_ws_endpoint}"...')

    async def main():
        async with async_playwright() as p:
            browser = await p.chromium.connect_over_cdp(browser_ws_endpoint)

            # Find the page by inspecting the URL and matching it
            contexts = browser.contexts
            pages = [page for context in contexts for page in context.pages]
            page = next((p for p in pages if url in p.url), None)

            if not page:
                raise Exception(f"Page with URL '{url}' not found.")

            page.on(
                "response",
                lambda res: print(f"{res.status}: {res.url}") if not res.ok else None,
            )

            print("Reloading page with networkidle...")
            await page.reload(wait_until="networkidle", timeout=timeout)

            print("Taking page screenshot...")
            await page.screenshot(path="temp.png", full_page=True)

            print("Done!")
            await browser.close()

    asyncio.run(main())

except Exception as e:
    print(e)

```

```codeBlockLines_p187
import com.microsoft.playwright.*;
import java.net.http.*;
import java.net.URI;
import java.net.http.HttpClient;
import java.util.Map;
import com.google.gson.Gson;

public class PlaywrightExample {
    private static final String TOKEN = "YOUR_BROWSERLESS_API_TOKEN";
    private static final String URL = "https://www.example.com/";
    private static final int TIMEOUT = 5 * 60 * 1000;
    private static final String PROXY = "residential";
    private static final String PROXY_COUNTRY = "gb";
    private static final boolean PROXY_STICKY = true;

    public static void main(String[] args) throws Exception {
        String unblockURL = "https://production-sfo.browserless.io/chromium/unblock";
        HttpClient client = HttpClient.newHttpClient();

        // Prepare query params
        String queryParams = String.format(
            "?timeout=%d&proxy=%s&proxyCountry=%s&proxySticky=%b&token=%s",
            TIMEOUT, PROXY, PROXY_COUNTRY, PROXY_STICKY, TOKEN
        );

        // Request payload
        Map<String, Object> payload = Map.of(
            "url", URL,
            "browserWSEndpoint", true,
            "cookies", true,
            "content", true,
            "screenshot", true,
            "ttl", 5000
        );

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(unblockURL + queryParams))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(new Gson().toJson(payload)))
            .build();

        System.out.println("Unblocking " + URL);
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) {
            throw new Exception("Error: " + response.body());
        }

        String browserWSEndpoint = new Gson().fromJson(response.body(), Map.class).get("browserWSEndpoint").toString();
        System.out.println("Connecting to Playwright...");

        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(browserWSEndpoint);

            Page page = browser.contexts().get(0).pages().get(0);
            System.out.println("Reloading page...");
            page.reload(new Page.ReloadOptions().setWaitUntil(Page.LoadState.NETWORKIDLE).setTimeout(TIMEOUT));
            System.out.println("Taking screenshot...");
            page.screenshot(new Page.ScreenshotOptions().setPath("screenshot.png"));
        }

        System.out.println("Done!");
    }
}

```

```codeBlockLines_p187
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using Microsoft.Playwright;

class Program
{
    static async Task Main(string[] args)
    {
        const string TOKEN = "YOUR_BROWSERLESS_API_TOKEN";
        const string URL = "https://www.example.com/";
        const int TIMEOUT = 5 * 60 * 1000;
        const string PROXY = "residential";
        const string PROXY_COUNTRY = "gb";
        const bool PROXY_STICKY = true;

        var unblockUrl = "https://production-sfo.browserless.io/chromium/unblock";
        using var httpClient = new HttpClient();

        var queryParams = $"?timeout={TIMEOUT}&proxy={PROXY}&proxyCountry={PROXY_COUNTRY}&proxySticky={PROXY_STICKY}&token={TOKEN}";
        var payload = new
        {
            url = URL,
            browserWSEndpoint = true,
            cookies = true,
            content = true,
            screenshot = true,
            ttl = 5000
        };

        var requestContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");
        var response = await httpClient.PostAsync(unblockUrl + queryParams, requestContent);

        if (!response.IsSuccessStatusCode)
        {
            throw new Exception($"Error: {await response.Content.ReadAsStringAsync()}");
        }

        var responseData = JsonSerializer.Deserialize<Dictionary<string, object>>(await response.Content.ReadAsStringAsync());
        var browserWSEndpoint = responseData["browserWSEndpoint"].ToString();

        Console.WriteLine("Connecting to Playwright...");
        using var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync(browserWSEndpoint);

        var context = browser.Contexts[0];
        var page = context.Pages[0];

        Console.WriteLine("Reloading page...");
        await page.ReloadAsync(new PageReloadOptions { WaitUntil = WaitUntilState.NetworkIdle, Timeout = TIMEOUT });

        Console.WriteLine("Taking screenshot...");
        await page.ScreenshotAsync(new PageScreenshotOptions { Path = "screenshot.png", FullPage = true });

        Console.WriteLine("Done!");
    }
}

```

With this powerful API you can get past a lot of common bot detection mechanisms and worry less about your automation.

- [Returning cookies only](https://docs.browserless.io/baas/avoid-bot-detection/unblocking#returning-cookies-only)
- [Returning content only](https://docs.browserless.io/baas/avoid-bot-detection/unblocking#returning-content-only)
- [Returning screenshots only](https://docs.browserless.io/baas/avoid-bot-detection/unblocking#returning-screenshots-only)
- [Full example with a library](https://docs.browserless.io/baas/avoid-bot-detection/unblocking#full-example-with-a-library)