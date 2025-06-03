---
url: "https://docs.browserless.io/rest-apis/unblock"
title: "/unblock API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/unblock#__docusaurus_skipToContent_fallback)

On this page

BrowserQL

We recommended using [**BrowserQL**](https://docs.browserless.io/browserql/start), Browserless' first-class browser automation API, to bypass any bot detection mechanisms.

The `/unblock` API is designed to bypass bot detection mechanisms such as Datadome and other passive CAPTCHAs. There are two main ways to use the API

For solving Cloudflare turnstiles, reCAPTCHA, or hCAPTCHA, you'll want to use our BrowserQL tool with the `verify` mutation. See [BrowserQL CAPTCHA Solving Guide](https://docs.browserless.io/browserql/bot-detection/solving-captchas#verify) for more details.

- Grab the HTML or screenshot of a page with `content` or `screenshot` set to true.
- Generate a WebSocket endpoint to perform automations with Playwright, Puppeteer or another CDP library.

Using the /unblock API is charged at 10 units per page. It works best when combined with our [Browserless Residential Proxy Service](https://docs.browserless.io/baas/proxies).

This API is particularly useful for developers who need to automate web interactions on sites that employ sophisticated bot detection and blocking techniques. It offers four different ways to wait for preconditions to be met before returning a response.

You can [view the complete Unblock API OpenAPI specification](https://docs.browserless.io/open-api#tag/Browser-REST-APIs/paths/~1unblock%20~1chromium~1unblock/post) for all properties and documentation.

## Retrieving HTML [​](https://docs.browserless.io/rest-apis/unblock\#retrieving-html "Direct link to Retrieving HTML")

If you'd like to retrieve the HTML of a page for scraping, you can set the `content` field to `true` in the JSON payload. With a proxy enabled, this would be:

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/unblock?token=YOUR_API_TOKEN_HERE&proxy=residential' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "https://example.com/",
  "browserWSEndpoint": false,
  "cookies": false,
  "content": true,
  "screenshot": false
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/unblock?token=${TOKEN}&proxy=residential`;
const headers = {
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  browserWSEndpoint: false,
  cookies: false,
  content: true,
  screenshot: false
};

const fetchContent = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const content = await response.json();
  console.log(content);
};

fetchContent();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/unblock?token={TOKEN}&proxy=residential"
headers = {
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "browserWSEndpoint": False,
    "cookies": False,
    "content": True,
    "screenshot": False
}

response = requests.post(url, headers=headers, json=data)

print(response.json())

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class FetchUnblockedContent {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/unblock?token=" + TOKEN + "&proxy=residential";

        String jsonData = """
        {
            "url": "https://example.com/",
            "browserWSEndpoint": false,
            "cookies": false,
            "content": true,
            "screenshot": false
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Response: " + response.body());
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/unblock?token={TOKEN}&proxy=residential";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""browserWSEndpoint"": false,
            ""cookies"": false,
            ""content"": true,
            ""screenshot"": false
        }";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try
        {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            var result = await response.Content.ReadAsStringAsync();
            Console.WriteLine("Response: " + result);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

Which will result in a response containing the unblocked page's HTML:

```codeBlockLines_p187
{
  "browserWSEndpoint": "wss://production-sfo.browserless.io/e/53616c7465645f5fa57aca44763bd816bb1aa1f1210ed871a908fd60235848ce6e4bcc0a8fcfe08c6d96eff8d68d556e/devtools/browser/646b292c-bd2a-4964-af18-9c1a6081c32e",
  "content": "<!DOCTYPE html><html>...</html>",
  "cookies": [],
  "screenshot": null,
  "ttl": 60000
}

```

You can then process this HTML with libraries such as [Scrapy](https://docs.browserless.io/baas/libraries/scrapy) or [Beautiful Soup](https://docs.browserless.io/baas/libraries/beautifulsoup).

## Creating an endpoint [​](https://docs.browserless.io/rest-apis/unblock\#creating-an-endpoint "Direct link to Creating an endpoint")

The /unblock API can get past a bot detector, then give you the cookies and a connection to the browser instance to use in your automations.

**JSON Payload**

This is a JSON object containing the URL of the site you wish to unblock, along with the parameters you want in the response. If you're reconnecting to the browser, you **always** want to set the `ttl` the `browserWSEndpoint` and `cookies`.

```codeBlockLines_p187
{
  "url": "https://example.com",
  "browserWSEndpoint": true,
  "cookies": true,
  "content": false,
  "screenshot": false,
  "ttl": 30000
}

```

We would recommend using /unblock with a residential proxy, such as in this example.

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/unblock?token=YOUR_API_TOKEN_HERE&proxy=residential' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "https://example.com",
  "browserWSEndpoint": true,
  "cookies": true,
  "content": false,
  "screenshot": false,
  "ttl": 30000
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/unblock?token=${TOKEN}&proxy=residential`;
const headers = {
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com",
  browserWSEndpoint: true,
  cookies: true,
  content: false,
  screenshot: false,
  ttl: 30000
};

const fetchBrowserWSEndpoint = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

fetchBrowserWSEndpoint();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/unblock?token={TOKEN}&proxy=residential"
headers = {
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com",
    "browserWSEndpoint": True,
    "cookies": True,
    "content": False,
    "screenshot": False,
    "ttl": 30000
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print(result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class FetchBrowserWSEndpoint {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/unblock?token=" + TOKEN + "&proxy=residential";

        String jsonData = """
        {
            "url": "https://example.com",
            "browserWSEndpoint": true,
            "cookies": true,
            "content": false,
            "screenshot": false,
            "ttl": 30000
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Response: " + response.body());
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
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main(string[] args)
      {
          string TOKEN = "YOUR_API_TOKEN_HERE";
          string url = $"https://production-sfo.browserless.io/unblock?token={TOKEN}&proxy=residential";

          string jsonData = @"
          {
              ""url"": ""https://example.com"",
              ""browserWSEndpoint"": true,
              ""cookies"": true,
              ""content"": false,
              ""screenshot"": false,
              ""ttl"": 30000
          }";

          using var client = new HttpClient();
          var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

          try
          {
              var response = await client.PostAsync(url, content);
              response.EnsureSuccessStatusCode();

              var result = await response.Content.ReadAsStringAsync();
              Console.WriteLine("Response: " + result);
          }
          catch (Exception ex)
          {
              Console.WriteLine($"Error: {ex.Message}");
          }
      }
  }

```

Which will return a JSON response like this:

```codeBlockLines_p187
{
  "browserWSEndpoint": "wss://production-sfo.browserless.io/p/53616c7465645f5f0d2e4012516859fdda7cc1ae0b16c6c5ec739d5d9f19a3d3c9b49c8a814b0fd1beae934b2e8050a0/devtools/browser/102ea3e9-74d7-42c9-a856-1bf254649b9a",
  "content": null,
  "cookies": [\
    {\
      name: "session_id",\
      value: "XYZ123",\
      domain: "example.com",\
      path: "/",\
      secure: true,\
      httpOnly: true,\
    },\
  ],
  "screenshot": null,
  "ttl": 30000
}

```

After receiving the response with the `browserWSEndpoint` and `cookies`, you can use Puppeteer, Playwright or another CDP library to connect to the browser instance and inject the cookies to continue your scraping process:

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const TOKEN = "YOUR_API_TOKEN_HERE";

const unblock = async (url) => {
  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url: url,
      browserWSEndpoint: true,
      cookies: false,
      content: false,
      screenshot: false,
      ttl: 10000,
    }),
  };

  const response = await fetch(
    `https://production-sfo.browserless.io/chromium/unblock?token=${TOKEN}`,
    opts,
  );

  return await response.json();
};

// Reconnect
const { browserWSEndpoint, cookies } = await unblock("https://browserless.io/");

const browser = await puppeteer.connect({
  browserWSEndpoint: browserWSEndpoint + `?token=${TOKEN}`,
});
const page = (await browser.pages())[0];

// Or inject cookies into the page
// await page.setCookie(...response.cookies);
// await page.goto("https://browserless.io/");
// await page.screenshot({ path: "screenshot.png" });

await page.screenshot({ path: `screenshot-${Date.now()}.png` });
await browser.close();

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import playwright from "playwright-core";

const TOKEN = "YOUR_API_TOKEN_HERE";

const unblock = async (url) => {
  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url: url,
      browserWSEndpoint: true,
      cookies: false,
      content: false,
      screenshot: false,
      ttl: 10000,
    }),
  };

  const response = await fetch(
    `https://production-sfo.browserless.io/chromium/unblock?token=${TOKEN}`,
    opts
  );

  return await response.json();
};

// Reconnect
const { browserWSEndpoint, cookies } = await unblock("https://browserless.io/");

const browser = await playwright.chromium.connect(`${browserWSEndpoint}?token=${TOKEN}`);
const context = await browser.newContext();

const page = await context.newPage();

// Or inject cookies into the page
// await page.context().addCookies(cookies);
// await page.goto("https://browserless.io/");
// await page.screenshot({ path: "screenshot.png" });

await page.screenshot({ path: `screenshot-${Date.now()}.png` });
await browser.close();

```

```codeBlockLines_p187
from playwright.sync_api import sync_playwright
import requests
import json

TOKEN = "YOUR_API_TOKEN_HERE"

def unblock(url):
    opts = {
        "url": url,
        "browserWSEndpoint": True,
        "cookies": False,
        "content": False,
        "screenshot": False,
        "ttl": 10000
    }

    response = requests.post(
        f"https://production-sfo.browserless.io/chromium/unblock?token={TOKEN}",
        headers={"Content-Type": "application/json"},
        data=json.dumps(opts)
    )

    return response.json()

with sync_playwright() as p:
    unblock_response = unblock("https://browserless.io/")
    browserWSEndpoint = unblock_response["browserWSEndpoint"]
    cookies = unblock_response.get("cookies", [])

    browser = p.chromium.connect(f"{browserWSEndpoint}?token={TOKEN}")
    context = browser.new_context()

    page = context.new_page()
    # Inject cookies if needed
    # context.add_cookies(cookies)
    # page.goto("https://browserless.io/")
    # page.screenshot(path="screenshot.png")

    page.screenshot(path=f"screenshot-{int(time.time())}.png")
    browser.close()

```

```codeBlockLines_p187
import com.microsoft.playwright.*;
import org.json.JSONObject;

import java.net.http.*;
import java.net.URI;

public class PlaywrightUnblock {
    private static final String TOKEN = "YOUR_API_TOKEN_HERE";

    public static JSONObject unblock(String url) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        String requestBody = new JSONObject()
                .put("url", url)
                .put("browserWSEndpoint", true)
                .put("cookies", false)
                .put("content", false)
                .put("screenshot", false)
                .put("ttl", 10000)
                .toString();

        HttpRequest request = HttpRequest.newBuilder()
                .uri(new URI("https://production-sfo.browserless.io/chromium/unblock?token=" + TOKEN))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        return new JSONObject(response.body());
    }

    public static void main(String[] args) throws Exception {
        JSONObject unblockResponse = unblock("https://browserless.io/");
        String browserWSEndpoint = unblockResponse.getString("browserWSEndpoint");

        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connect(browserWSEndpoint + "?token=" + TOKEN);
            BrowserContext context = browser.newContext();
            Page page = context.newPage();

            // Inject cookies if needed
            // context.addCookies(cookiesArray);
            // page.navigate("https://browserless.io/");
            // page.screenshot(new Page.ScreenshotOptions().setPath(Paths.get("screenshot.png")));

            page.screenshot(new Page.ScreenshotOptions().setPath(Paths.get("screenshot-" + System.currentTimeMillis() + ".png")));
            browser.close();
        }
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
      private const string TOKEN = "YOUR_API_TOKEN_HERE";

      static async Task<JsonElement> UnblockAsync(string url)
      {
          using var client = new HttpClient();
          var opts = new
          {
              url = url,
              browserWSEndpoint = true,
              cookies = false,
              content = false,
              screenshot = false,
              ttl = 10000
          };

          var response = await client.PostAsync(
              $"https://production-sfo.browserless.io/chromium/unblock?token={TOKEN}",
              new StringContent(JsonSerializer.Serialize(opts), Encoding.UTF8, "application/json")
          );

          response.EnsureSuccessStatusCode();
          var jsonResponse = await response.Content.ReadAsStringAsync();
          return JsonSerializer.Deserialize<JsonElement>(jsonResponse);
      }

      static async Task Main(string[] args)
      {
          try
          {
              var unblockResponse = await UnblockAsync("https://browserless.io/");
              Console.WriteLine("Unblock Response:");
              Console.WriteLine(unblockResponse);

              string browserWSEndpoint = unblockResponse.GetProperty("browserWSEndpoint").GetString();
              Console.WriteLine($"Connecting to WebSocket: {browserWSEndpoint}");

              var playwright = await Playwright.CreateAsync();
              var browser = await playwright.Chromium.ConnectOverCDPAsync($"{browserWSEndpoint}?token={TOKEN}");

              var context = await browser.NewContextAsync();
              var page = await context.NewPageAsync();

              Console.WriteLine("Taking screenshot...");
              await page.ScreenshotAsync(new PageScreenshotOptions { Path = $"screenshot-{DateTimeOffset.UtcNow.ToUnixTimeMilliseconds()}.png" });

              await browser.CloseAsync();
              Console.WriteLine("Browser closed successfully.");
          }
          catch (Exception ex)
          {
              Console.WriteLine($"Error: {ex.Message}");
          }
      }
  }

```

## Waiting for Things [​](https://docs.browserless.io/rest-apis/unblock\#waiting-for-things "Direct link to Waiting for Things")

Browserless offers 4 different ways to wait for preconditions to be met on the page before returning the response. These are `events`, `functions`, `selectors` and `timeouts`.

### waitForEvent [​](https://docs.browserless.io/rest-apis/unblock\#waitforevent "Direct link to waitForEvent")

Waits for an event to happen on the page before continuing:

#### Example [​](https://docs.browserless.io/rest-apis/unblock\#example "Direct link to Example")

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
// Will fail since the event never fires on this page,
// but used for demonstration purposes
{
  "url": "https://example.com/",
  "waitForEvent": {
    "event": "fullscreenchange",
    "timeout": 5000
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/unblock?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://example.com/",
  "waitForEvent": {
    "event": "fullscreenchange",
    "timeout": 5000
  }
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/unblock?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  waitForEvent: {
    event: "fullscreenchange",
    timeout: 5000
  }
};

const unblockRequest = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

unblockRequest();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/unblock?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "waitForEvent": {
        "event": "fullscreenchange",
        "timeout": 5000
    }
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print(result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class UnblockRequestWithWaitForEvent {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/unblock?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "waitForEvent": {
                "event": "fullscreenchange",
                "timeout": 5000
            }
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Cache-Control", "no-cache")
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Response: " + response.body());
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
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/unblock?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""waitForEvent"": {
                ""event"": ""fullscreenchange"",
                ""timeout"": 5000
            }
        }";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            var result = await response.Content.ReadAsStringAsync();
            Console.WriteLine("Response: " + result);
        } catch (Exception ex) {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

### waitForFunction [​](https://docs.browserless.io/rest-apis/unblock\#waitforfunction "Direct link to waitForFunction")

Waits for the provided function to return before continuing. The function can be any valid JavaScript function including `async` functions.

#### Example [​](https://docs.browserless.io/rest-apis/unblock\#example-1 "Direct link to Example")

**JS function**

```codeBlockLines_p187
async () => {
  const res = await fetch("https://jsonplaceholder.typicode.com/todos/1");
  const json = await res.json();

  document.querySelector("h1").innerText = json.title;
};

```

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "waitForFunction": {
    "fn": "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
    "timeout": 5000
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/unblock?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://example.com/",
  "waitForFunction": {
    "fn": "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
    "timeout": 5000
  }
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/unblock?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  waitForFunction: {
    fn: "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
    timeout: 5000
  }
};

const unblockRequest = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

unblockRequest();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/unblock?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "waitForFunction": {
        "fn": "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
        "timeout": 5000
    }
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print(result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class UnblockRequestWithWaitForFunction {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/unblock?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "waitForFunction": {
                "fn": "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
                "timeout": 5000
            }
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Cache-Control", "no-cache")
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Response: " + response.body());
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
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/unblock?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""waitForFunction"": {
                ""fn"": ""async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}"",
                ""timeout"": 5000
            }
        }";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            var result = await response.Content.ReadAsStringAsync();
            Console.WriteLine("Response: " + result);
        } catch (Exception ex) {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

### waitForSelector [​](https://docs.browserless.io/rest-apis/unblock\#waitforselector "Direct link to waitForSelector")

Waits for a selector to appear on the page. If at the moment of calling this API, the selector already exists, the method will return immediately. If the selector doesn't appear after the timeout milliseconds of waiting the API will return a non-200 response code with an error message as the body of the response.

The object can have any of these values:

- `selector`: String, required — A valid CSS selector.
- `hidden` Boolean, optional — Wait for the selected element to not be found in the DOM or to be hidden, i.e. have `display: none` or `visibility: hidden` CSS properties.
- `timeout`: Number, optional — Maximum number of milliseconds to wait for the selector before failing.
- `visible`: Boolean, optional — Wait for the selected element to be present in DOM and to be visible, i.e. to not have `display: none` or `visibility: hidden` CSS properties.

#### Example [​](https://docs.browserless.io/rest-apis/unblock\#example-2 "Direct link to Example")

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "waitForSelector": {
    "selector": "h1",
    "timeout": 5000
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/unblock?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://example.com/",
  "waitForSelector": {
    "selector": "h1",
    "timeout": 5000
  }
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/unblock?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  waitForSelector: {
    selector: "h1",
    timeout: 5000
  }
};

const unblockRequest = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log("Response:", result);
};

unblockRequest();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/unblock?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "waitForSelector": {
        "selector": "h1",
        "timeout": 5000
    }
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print("Response:", result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class UnblockRequestWithWaitForSelector {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/unblock?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "waitForSelector": {
                "selector": "h1",
                "timeout": 5000
            }
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Cache-Control", "no-cache")
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Response: " + response.body());
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
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/unblock?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""waitForSelector"": {
                ""selector"": ""h1"",
                ""timeout"": 5000
            }
        }";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            var result = await response.Content.ReadAsStringAsync();
            Console.WriteLine("Response: " + result);
        } catch (Exception ex) {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

- [Retrieving HTML](https://docs.browserless.io/rest-apis/unblock#retrieving-html)
- [Creating an endpoint](https://docs.browserless.io/rest-apis/unblock#creating-an-endpoint)
- [Waiting for Things](https://docs.browserless.io/rest-apis/unblock#waiting-for-things)
  - [waitForEvent](https://docs.browserless.io/rest-apis/unblock#waitforevent)
  - [waitForFunction](https://docs.browserless.io/rest-apis/unblock#waitforfunction)
  - [waitForSelector](https://docs.browserless.io/rest-apis/unblock#waitforselector)