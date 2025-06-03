---
url: "https://docs.browserless.io/baas/proxies"
title: "Proxies | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/proxies#__docusaurus_skipToContent_fallback)

Version: v2

On this page

Browserless offers two approaches to using proxies with your browser automation:

1. [**Built-in Residential Proxy**](https://docs.browserless.io/baas/proxies#built-in-residential-proxy) \- Our first-party residential proxy service available for paid cloud-unit accounts
2. [**Third Party Proxies**](https://docs.browserless.io/baas/proxies#third-party-proxies) \- Support for using your own external proxies with browserless

## Built-in Residential Proxy [​](https://docs.browserless.io/baas/proxies\#built-in-residential-proxy "Direct link to Built-in Residential Proxy")

Browserless offers a built-in residential proxy for paid cloud-unit accounts. [You can sign-up for one here](https://www.browserless.io/sign-up/).

In order to effectively use this proxy, you'll need to adjust your code or API calls to let browserless proxy the request for you. For both library connect and REST API calls, the process is the same!

Bot Detection

For strict bot detectors where browsers and a proxy aren't enough to get past, we would recommend using [**BrowserQL**](https://docs.browserless.io/browserql/start).

### Puppeteer [​](https://docs.browserless.io/baas/proxies\#puppeteer "Direct link to Puppeteer")

The following uses our built-in residential proxy, targeting a node in the US:

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const TOKEN = "YOUR_API_TOKEN_HERE";

// Simply add proxy=residential and (optionally) a country
const browserWSEndpoint =
  `wss://production-sfo.browserless.io?token=${TOKEN}&proxy=residential&proxyCountry=us`;
const url = "https://ipinfo.io/";
let browser;

try {
  browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });
  await page.goto(url);
  await page.screenshot({ path: "ip.png" });
} catch (e) {
  console.log("Error during script:", e.message);
} finally {
  browser && browser.close();
}

```

Sticky Sessions

By default, all requests will go through a random node in the proxy pool. This may not be desireable and can cause other issues. In order to keep your session "sticky" (use the same IP node), add a `proxySticky` parameter:

```codeBlockLines_p187
"http://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us&proxySticky";

```

### Playwright [​](https://docs.browserless.io/baas/proxies\#playwright "Direct link to Playwright")

Our proxy service is also available for Playwright browsers. You only need to set the same parameters as for Puppeteer.

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import playwright from "playwright-core";

const TOKEN = "YOUR_API_TOKEN_HERE"

// Simply add proxy=residential and (optionally) a country
const pwEndpoint = `wss://production-sfo.browserless.io/firefox/playwright?token=${TOKEN}&proxy=residential&proxyCountry=us`;
const browser = await playwright.firefox.connect(pwEndpoint);

const context = await browser.newContext();
const page = await context.newPage();

await page.goto("https://ipinfo.io/");
await page.screenshot({
  path: `firefox.png`,
});
await browser.close();

```

```codeBlockLines_p187
from playwright.sync_api import sync_playwright

TOKEN = "YOUR_API_TOKEN_HERE"
pw_endpoint = f"wss://production-sfo.browserless.io/firefox/playwright?token={TOKEN}&proxy=residential&proxyCountry=us"

with sync_playwright() as p:
    # Connect to the Browserless endpoint
    browser = p.firefox.connect_over_cdp(pw_endpoint)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the URL and take a screenshot
    page.goto("https://ipinfo.io/")
    page.screenshot(path="firefox.png")

    # Close the browser connection
    browser.close()

print("Screenshot saved as firefox.png")

```

```codeBlockLines_p187
import com.microsoft.playwright.*;

public class PlaywrightRemoteProxy {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String PW_ENDPOINT = "wss://production-sfo.browserless.io/firefox/playwright?token="
            + TOKEN + "&proxy=residential&proxyCountry=us";

        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.firefox().connect(PW_ENDPOINT);
            System.out.println("Connected to remote Firefox browser");

            BrowserContext context = browser.newContext();
            Page page = context.newPage();

            page.navigate("https://ipinfo.io/");
            page.screenshot(new Page.ScreenshotOptions().setPath("firefox.png"));
            System.out.println("Screenshot saved as firefox.png");

            browser.close();
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.Threading.Tasks;
using Microsoft.Playwright;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string PW_ENDPOINT = $"wss://production-sfo.browserless.io/firefox/playwright?token={TOKEN}&proxy=residential&proxyCountry=us";

        var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Firefox.ConnectAsync(PW_ENDPOINT);
        Console.WriteLine("Connected to remote Firefox browser");

        var context = await browser.NewContextAsync();
        var page = await context.NewPageAsync();

        await page.GotoAsync("https://ipinfo.io/");
        await page.ScreenshotAsync(new PageScreenshotOptions { Path = "firefox.png" });
        Console.WriteLine("Screenshot saved as firefox.png");

        await browser.CloseAsync();
    }
}

```

Sticky Sessions

By default, all requests will go through a random node in the proxy pool. This may not be desireable and can cause other issues. In order to keep your session "sticky" (use the same IP node), add a `proxySticky` parameter:

```codeBlockLines_p187
"http://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us&proxySticky";

```

### REST APIs [​](https://docs.browserless.io/baas/proxies\#rest-apis "Direct link to REST APIs")

All of our REST-APIs function the same for proxying: simply add the proxy parameters you care about to the requests' query-string parameters, and you're all done. No need for credentials or otherwise.

Here's an examples of collecting [content](https://docs.browserless.io/baas/proxies#content), [pdf](https://docs.browserless.io/baas/proxies#pdf) and [screenshot](https://docs.browserless.io/baas/proxies#screenshot) from a United States Proxy:

#### Content [​](https://docs.browserless.io/baas/proxies\#content "Direct link to Content")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url "https://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE&proxyCountry=us&proxy=residential" \
  --header "Content-Type: application/json" \
  --data "{
    \"url\": \"https://ipinfo.io/\"
  }" \
  --output "ipinfo.html"

```

```codeBlockLines_p187
import fetch from 'node-fetch';
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";

const url = `https://production-sfo.browserless.io/content?token=${TOKEN}&proxyCountry=us&proxy=residential`;
const headers = {
    "Content-Type": "application/json"
};
const data = {
    url: "https://ipinfo.io/"
};

const fetchContent = async () => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });

    const html = await response.text();
    await writeFile("ipinfo.html", html);
    console.log("HTML content saved as ipinfo.html");
};

fetchContent();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/content?token={TOKEN}&proxyCountry=us&proxy=residential"
headers = {
    "Content-Type": "application/json"
}
data = {
    "url": "https://ipinfo.io/"
}

response = requests.post(url, headers=headers, json=data)

with open("ipinfo.html", "wb") as f:
    f.write(response.content)

print("HTML content saved as ipinfo.html")

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;

public class FetchHTML {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN + "&proxyCountry=us&proxy=residential";

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = """
            {
                "url": "https://ipinfo.io/"
            }
        """;

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            try (FileOutputStream fos = new FileOutputStream("ipinfo.html")) {
                response.body().transferTo(fos);
                System.out.println("HTML content saved to ipinfo.html");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/content?token={TOKEN}&proxyCountry=us&proxy=residential";

        var payload = new {
            url = "https://ipinfo.io/"
        };

        var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

        using var httpClient = new HttpClient();
        try {
            var response = await httpClient.PostAsync(url, jsonContent);
            response.EnsureSuccessStatusCode();

            var contentStream = await response.Content.ReadAsStreamAsync();
            using (var fileStream = new FileStream("ipinfo.html", FileMode.Create, FileAccess.Write, FileShare.None)) {
                await contentStream.CopyToAsync(fileStream);
                Console.WriteLine("HTML content saved to ipinfo.html");
            }
        } catch (Exception e) {
            Console.WriteLine("Error: " + e.Message);
        }
    }
}

```

#### PDF [​](https://docs.browserless.io/baas/proxies\#pdf "Direct link to PDF")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url "https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE&proxyCountry=us&proxy=residential" \
  --header "Content-Type: application/json" \
  --data "{
    \"url\": \"https://ipinfo.io/\"
  }" \
  --output "ipinfo.pdf"

```

```codeBlockLines_p187
import fetch from 'node-fetch';
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}&proxyCountry=us&proxy=residential`;
const headers = {
  "Content-Type": "application/json"
};
const data = {
  url: "https://ipinfo.io/"
};

const fetchPDF = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const pdfBuffer = await response.arrayBuffer();
  await writeFile("ipinfo.pdf", Buffer.from(pdfBuffer));
  console.log("PDF content saved as ipinfo.pdf");
};

fetchPDF();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}&proxyCountry=us&proxy=residential"
headers = {
    "Content-Type": "application/json"
}
data = {
    "url": "https://ipinfo.io/"
}

response = requests.post(url, headers=headers, json=data)

with open("ipinfo.pdf", "wb") as f:
    f.write(response.content)

print("PDF content saved as ipinfo.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;

public class FetchPDF {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN + "&proxyCountry=us&proxy=residential";

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = """
            {
                "url": "https://ipinfo.io/"
            }
        """;

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            try (FileOutputStream fos = new FileOutputStream("ipinfo.pdf")) {
                response.body().transferTo(fos);
                System.out.println("PDF saved as ipinfo.pdf");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}&proxyCountry=us&proxy=residential";

        var payload = new {
            url = "https://ipinfo.io/"
        };

        var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

        using var httpClient = new HttpClient();
        try {
            var response = await httpClient.PostAsync(url, jsonContent);
            response.EnsureSuccessStatusCode();

            var contentStream = await response.Content.ReadAsStreamAsync();
            using (var fileStream = new FileStream("ipinfo.pdf", FileMode.Create, FileAccess.Write, FileShare.None)) {
                await contentStream.CopyToAsync(fileStream);
                Console.WriteLine("PDF saved as ipinfo.pdf");
            }
        } catch (Exception e) {
            Console.WriteLine("Error: " + e.Message);
        }
    }
}

```

#### Screenshot [​](https://docs.browserless.io/baas/proxies\#screenshot "Direct link to Screenshot")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url "https://production-sfo.browserless.io/screenshot?token=YOUR_API_TOKEN_HERE&proxyCountry=us&proxy=residential" \
  --header "Content-Type: application/json" \
  --data "{
    \"url\": \"https://ipinfo.io/\"
  }" \
  --output "ipinfo.png"

```

```codeBlockLines_p187
import fetch from 'node-fetch';
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/screenshot?token=${TOKEN}&proxyCountry=us&proxy=residential`;
const headers = {
  "Content-Type": "application/json"
};
const data = {
  url: "https://ipinfo.io/"
};

const fetchScreenshot = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const imageBuffer = await response.arrayBuffer();
  await writeFile("ipinfo.png", Buffer.from(imageBuffer));
  console.log("Screenshot saved as ipinfo.png");
};

fetchScreenshot();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/screenshot?token={TOKEN}&proxyCountry=us&proxy=residential"
headers = {
    "Content-Type": "application/json"
}
data = {
    "url": "https://ipinfo.io/"
}

response = requests.post(url, headers=headers, json=data)

with open("ipinfo.png", "wb") as f:
    f.write(response.content)

print("Screenshot saved as ipinfo.png")

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;

public class FetchScreenshot {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/screenshot?token=" + TOKEN + "&proxyCountry=us&proxy=residential";

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = """
            {
                "url": "https://ipinfo.io/"
            }
        """;

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            try (FileOutputStream fos = new FileOutputStream("ipinfo.png")) {
                response.body().transferTo(fos);
                System.out.println("Screenshot saved as ipinfo.png");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/screenshot?token={TOKEN}&proxyCountry=us&proxy=residential";

        var payload = new {
            url = "https://ipinfo.io/"
        };

        var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

        using var httpClient = new HttpClient();
        try {
            var response = await httpClient.PostAsync(url, jsonContent);
            response.EnsureSuccessStatusCode();

            var contentStream = await response.Content.ReadAsStreamAsync();
            using (var fileStream = new FileStream("ipinfo.png", FileMode.Create, FileAccess.Write, FileShare.None)) {
                await contentStream.CopyToAsync(fileStream);
                Console.WriteLine("Screenshot saved as ipinfo.png");
            }
        } catch (Exception e) {
            Console.WriteLine("Error: " + e.Message);
        }
    }
}

```

## Third Party Proxies [​](https://docs.browserless.io/baas/proxies\#third-party-proxies "Direct link to Third Party Proxies")

Both browserless, and Chrome itself, support the usage of external proxies. If you want to use an external, or 3rd party proxy, please continue to read below. In general there's two things you'll have to do:

- Specify the address of where the proxy is with the `--proxy-server` switch.
- Optionally, you'll also need to send in your username and password if the proxy is authenticated.

### Specifying the proxy [​](https://docs.browserless.io/baas/proxies\#specifying-the-proxy "Direct link to Specifying the proxy")

Regardless of whether or not you're using our REST API's or the puppeteer integration, you'll need to specify _where_ the proxy is. Chrome has a command-line flag to do this, and we support this in browserless via the following query-string parameter:

```codeBlockLines_p187
?--proxy-server=https://YOUR-PROXY-SERVER-DOMAIN:PORT

```

You can set this parameter in our [live debugger](https://chrome.browserless.io/debugger) by clicking on the gear icon on the left panel and modifying the Browser URL field.

If you're using a proxy that doesn't require a password (maybe just an IP address filter), then that's it! You're free to now use this proxy going forward! Otherwise read on.

### Using username and password [​](https://docs.browserless.io/baas/proxies\#using-username-and-password "Direct link to Using username and password")

#### Method 1: page.authenticate (Puppeteer) [​](https://docs.browserless.io/baas/proxies\#method-1-pageauthenticate-puppeteer "Direct link to Method 1: page.authenticate (Puppeteer)")

Most proxies will require some means of authentication. There's generally two ways you can do this in Puppeteer, and also in browserless. The first more common method is the `page.authenticate`:

```codeBlockLines_p187
await page.authenticate({
  username: 'joel',
  password: 'browserless-rocks',
});

```

Doing this will apply these parameters to your network requests going forward.

In our REST API's you can specify these fields with the following in your POST JSON body. These parameters work for the `pdf`, `content` and `screenshot` APIs:

```codeBlockLines_p187
{
  "authenticate": {
    "username": "joel",
    "password": "browserless-rocks"
  }
}

```

#### Method 2: page.setExtraHTTPHeaders (Puppeteer) [​](https://docs.browserless.io/baas/proxies\#method-2-pagesetextrahttpheaders-puppeteer "Direct link to Method 2: page.setExtraHTTPHeaders (Puppeteer)")

The other mechanism is to use HTTP headers to send in extra authorization information. Puppeteer makes this pretty easy by allowing us to send in new HTTP headers via `page.setExtraHTTPHeaders`:

> NOTE: This is deprecated in most libraries now, so it's worth keeping in mind that using authentication methods in each library is now the standard.

```codeBlockLines_p187
// Remember to base64 encode your username:password!
await page.setExtraHTTPHeaders({
  'Proxy-Authorization': 'Basic username:password',
  // OR
  Authorization: 'Basic username:password',
});

```

Refer to your libraries documentation on what the name of the headers is, and how to properly encode it.

We also allow this in our REST APIs as well, via the `setExtraHTTPHeaders` property:

```codeBlockLines_p187
{
  "setExtraHTTPHeaders": {
    "Proxy-Authorization": "Basic username:password",
    // OR
    "Authorization": "Basic username:password"
  }
}

```

This will allow your REST APIs to utilize the prior provided proxy!

### Using Proxies with Playwright [​](https://docs.browserless.io/baas/proxies\#using-proxies-with-playwright "Direct link to Using Proxies with Playwright")

Playwright handles proxies differently than Puppeteer. Instead of using `page.authenticate()` or `setExtraHTTPHeaders()`, Playwright allows you to specify proxy settings directly at the context level, which means all pages created from that context will use the specified proxy.

#### Method: browser.newContext() with proxy option (Playwright) [​](https://docs.browserless.io/baas/proxies\#method-browsernewcontext-with-proxy-option-playwright "Direct link to Method: browser.newContext() with proxy option (Playwright)")

When using Playwright with browserless, you can set up a proxy by providing proxy configuration to the `newContext()` method:

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

- [Built-in Residential Proxy](https://docs.browserless.io/baas/proxies#built-in-residential-proxy)
  - [Puppeteer](https://docs.browserless.io/baas/proxies#puppeteer)
  - [Playwright](https://docs.browserless.io/baas/proxies#playwright)
  - [REST APIs](https://docs.browserless.io/baas/proxies#rest-apis)
- [Third Party Proxies](https://docs.browserless.io/baas/proxies#third-party-proxies)
  - [Specifying the proxy](https://docs.browserless.io/baas/proxies#specifying-the-proxy)
  - [Using username and password](https://docs.browserless.io/baas/proxies#using-username-and-password)
  - [Using Proxies with Playwright](https://docs.browserless.io/baas/proxies#using-proxies-with-playwright)