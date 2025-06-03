---
url: "https://docs.browserless.io/browserql/session-management/playwright"
title: "Playwright | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/session-management/playwright#__docusaurus_skipToContent_fallback)

On this page

If you're already using Playwright working with WebSockets, you can still mix-and-match BrowserQL in your scripts. This is perfect for getting past a nasty bot blockage and then connecting your existing scripts back.

Reconnecting with More BQL

You can also run _more_ BrowserQL at a later time by doing the same process this guide will teach you. Refer to the [Reconnecting with More BQL](https://docs.browserless.io/browserql/writing-bql/reconnecting-bql) guide for more details.

## Using Reconnect [​](https://docs.browserless.io/browserql/session-management/playwright\#using-reconnect "Direct link to Using Reconnect")

With BQL, you'll navigate to the desired page, do the actions you require, like verifying or solving a captcha, and finally, use the [`reconnect`](https://docs.browserless.io/bql-schema/operations/mutations/reconnect) mutation to retrieve a websocket endpoint. This endpoint will be your entry point when starting your Playwright connection.

Using the [https://example.com/](https://example.com/) page, you can run the following BrowserQL query then ask for a connection back:

Reconnect Timeout

The `reconnect` mutation has a `timeout` argument, which is a limit (in milliseconds) for how long the browser should be available before it gets shutdown when nothing connects to it. If a connection were to happen after this time, a semantic `404` is returned back. When a connection happens, this will clear the timer and the session can continue past this limit.

```codeBlockLines_p187
mutation Reconnect {
  goto(url: "https://example.com/", waitUntil: networkIdle) {
    status
  }

  reconnect (timeout: 30000) {
    browserWSEndpoint
  }
}

```

## Connecting with Playwright [​](https://docs.browserless.io/browserql/session-management/playwright\#connecting-with-playwright "Direct link to Connecting with Playwright")

Now, you need to integrate the BQL query above into your Playwright code. You can use BQL Editor's Export Query as Code to translate any query into multiple code languages, like Javascript.

- Learn how to [Export Query as Code](https://docs.browserless.io/browserql/writing-bql/exporting-scripts).
- See the [Available programming languages](https://docs.browserless.io/browserql/using-the-ide/ide-features#query-as-code).

With the query turned into your preffered code language, you can integrate the code into your script. The example below uses the `browserWSEndpoint` to make a connection with Playwright, and takes a screenshot of the webpage:

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import playwright from 'playwright-core';

const url = 'https://example.com';
const token = 'YOUR_API_TOKEN_HERE';
const timeout = 5 * 60 * 1000;

const queryParams = new URLSearchParams({
  timeout,
  token,
}).toString();

const query = `
  mutation Reconnect($url: String!) {
    goto(url: $url, waitUntil: networkIdle) {
      status
    }
    reconnect(timeout: 30000) {
      browserWSEndpoint
    }
  }
`;

const variables = { url };

const endpoint =
  `https://production-sfo.browserless.io/playwright./bql?${queryParams}`;

const options = {
  method: 'POST',
  headers: {
    'content-type': 'application/json',
  },
  body: JSON.stringify({
    query,
    variables,
  }),
};

(async () => {
  try {
    console.log(`Running BQL Query: ${url}`);

    const response = await fetch(endpoint, options);

    if (!response.ok) {
      throw new Error(`Got non-ok response:\n` + (await response.text()));
    }

    const { data } = await response.json();
    const browserWSEndpoint = data.reconnect.browserWSEndpoint;

    console.log(`Got OK response! Connecting Playwright to ${browserWSEndpoint}`);

    const browser = await playwright.chromium.connectOverCDP(browserWSEndpoint);
    const context = browser.contexts()[0];
    const page = context.pages().find((p) => p.url().includes(url));

    if (!page) {
      throw new Error(`Could not find a page matching ${url}`);
    }

    await page.screenshot({ fullPage: true, path: 'temp.png' });

    await browser.close();
  } catch (error) {
    console.error(error);
  }
})();

```

```codeBlockLines_p187
import requests
from playwright.sync_api import sync_playwright

url = "https://example.com"
token = "YOUR_API_TOKEN_HERE"
timeout = 5 * 60 * 1000

query_params = f"token={token}&timeout={timeout}"
endpoint = f"https://production-sfo.browserless.io/chromium/bql?{query_params}"

query = """
  mutation Reconnect($url: String!) {
    goto(url: $url, waitUntil: networkIdle) {
      status
    }
    reconnect(timeout: 30000) {
      browserWSEndpoint
    }
  }
"""

variables = {"url": url}

headers = {"content-type": "application/json"}

body = {"query": query, "variables": variables}

try:
    print(f"Running BQL Query: {url}")
    response = requests.post(endpoint, json=body, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Got non-ok response:\n{response.text}")

    data = response.json().get("data")
    browser_ws_endpoint = data["reconnect"]["browserWSEndpoint"]
    print(f"Got OK response! Connecting Playwright to {browser_ws_endpoint}")

    with sync_playwright() as playwright:
        browser = playwright.chromium.connect_over_cdp(browser_ws_endpoint)
        context = browser.contexts[0]
        page = next((p for p in context.pages if url in p.url), None)

        if not page:
            raise Exception(f"Could not find a page matching {url}")

        page.screenshot(path="temp.png", full_page=True)

        browser.close()

except Exception as e:
    print(f"Error: {e}")

```

```codeBlockLines_p187
package com.example;

import com.microsoft.playwright.*;
import com.google.gson.*;
import java.net.http.*;
import java.net.URI;
import java.util.*;

public class PlaywrightBQL {
    public static void main(String[] args) {
        String url = "https://example.com";
        String token = "YOUR_API_TOKEN_HERE";
        int timeout = 5 * 60 * 1000;

        String queryParams = String.format("token=%s&timeout=%d", token, timeout);
        String endpoint = String.format("https://production-sfo.browserless.io/chromium/bql?%s", queryParams);

        String query = """
                mutation Reconnect($url: String!) {
                  goto(url: $url, waitUntil: networkIdle) {
                    status
                  }
                  reconnect(timeout: 30000) {
                    browserWSEndpoint
                  }
                }
                """;

        JsonObject variables = new JsonObject();
        variables.addProperty("url", url);

        JsonObject body = new JsonObject();
        body.addProperty("query", query);
        body.add("variables", variables);

        try {
            // Send GraphQL request
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(endpoint))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() != 200) {
                throw new RuntimeException("Failed request: " + response.body());
            }

            // Parse response
            JsonObject data = JsonParser.parseString(response.body()).getAsJsonObject().getAsJsonObject("data");
            String browserWSEndpoint = data.getAsJsonObject("reconnect").get("browserWSEndpoint").getAsString();

            System.out.println("Connecting Playwright to " + browserWSEndpoint);

            try (Playwright playwright = Playwright.create()) {
                Browser browser = playwright.chromium().connectOverCDP(browserWSEndpoint);
                BrowserContext context = browser.contexts().get(0);
                Page page = context.pages().stream()
                        .filter(p -> p.url().contains(url))
                        .findFirst()
                        .orElseThrow(() -> new RuntimeException("Page not found"));

                page.screenshot(new Page.ScreenshotOptions().setPath("temp.png").setFullPage(true));
                browser.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using Microsoft.Playwright;

class Program
{
    static async System.Threading.Tasks.Task Main(string[] args)
    {
        string url = "https://example.com";
        string token = "YOUR_API_TOKEN_HERE";
        int timeout = 5 * 60 * 1000;

        string queryParams = $"token={token}&timeout={timeout}";
        string endpoint = $"https://production-sfo.browserless.io/chromium/bql?{queryParams}";

        string query = @"
        mutation Reconnect($url: String!) {
          goto(url: $url, waitUntil: networkIdle) {
            status
          }
          reconnect(timeout: 30000) {
            browserWSEndpoint
          }
        }";

        var body = new
        {
            query = query,
            variables = new { url }
        };

        try
        {
            // Send GraphQL request
            using var client = new HttpClient();
            var requestContent = new StringContent(JsonSerializer.Serialize(body), Encoding.UTF8, "application/json");
            var response = await client.PostAsync(endpoint, requestContent);

            if (!response.IsSuccessStatusCode)
            {
                throw new Exception($"Request failed: {await response.Content.ReadAsStringAsync()}");
            }

            var jsonResponse = JsonNode.Parse(await response.Content.ReadAsStringAsync());
            string browserWSEndpoint = jsonResponse["data"]["reconnect"]["browserWSEndpoint"].ToString();

            Console.WriteLine($"Connecting Playwright to {browserWSEndpoint}");

            // Connect to Playwright
            using var playwright = await Playwright.CreateAsync();
            var browser = await playwright.Chromium.ConnectOverCDPAsync(browserWSEndpoint);
            var context = browser.Contexts[0];
            var page = context.Pages.Find(p => p.Url.Contains(url)) ?? throw new Exception("Page not found");

            // Take screenshot
            await page.ScreenshotAsync(new PageScreenshotOptions { Path = "temp.png", FullPage = true });

            await browser.CloseAsync();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

- [Using Reconnect](https://docs.browserless.io/browserql/session-management/playwright#using-reconnect)
- [Connecting with Playwright](https://docs.browserless.io/browserql/session-management/playwright#connecting-with-playwright)