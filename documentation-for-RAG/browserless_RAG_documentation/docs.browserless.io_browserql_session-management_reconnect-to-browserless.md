---
url: "https://docs.browserless.io/browserql/session-management/reconnect-to-browserless"
title: "Maintaining Sessions with Reconnects | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#__docusaurus_skipToContent_fallback)

On this page

The Session-Reconnect features allow you to maintain continuity across multiple browser sessions or integrate with other automation tools. This section covers how to reconnect to an existing browser session, pass control between BrowserQL and external libraries, and create persistent workflows that can be accessed and controlled across different sessions or systems.

Similar to connecting a 3rd-party library, you can also reconnect back and execute more BrowserQL as well. BQL does this by generating a new unique URL to use for running more queries. You can take this URL, append your API-token to it, and run more query language.

Scraping websites with traditional tools like Puppeteer or Playwright can be inefficient due to repeated session restarts and unnecessary proxy usage. Reconnects maintains browser sessions, preserving cookies, cache, and session data across multiple requests, bringing the following benefits:

- **Reduced proxy usage:** Save up to 90% of proxy bandwidth.
- **Improved efficiency:** Avoid repetitive loading of static content.
- **Lower detection risk:** Maintain consistent session states to avoid bot detection mechanisms like CAPTCHAs.

## Implementing Reconnects with BrowserQL [​](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless\#implementing-reconnects-with-browserql "Direct link to Implementing Reconnects with BrowserQL")

This guide will go through the following steps to maintain a sessions using Reconnects:

1. [Initiate a session](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#step-1-initial-setup).
2. [Scrape data using the reconnect URL](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#step-2-using-the-reconnect-url).
3. [Refresh your session URL regularly to maintain stability](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#step-3-refreshing-your-session).

### Step 1: Initial Setup [​](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless\#step-1-initial-setup "Direct link to Step 1: Initial Setup")

Start by initiating a session with BrowserQL. This first query opens the browser, navigates to your target URL, and provides a reconnect URL to reuse the same session.

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import fetch from 'node-fetch';

const API_KEY = "YOUR_API_TOKEN_HERE";
const BQL_ENDPOINT = "https://production-sfo.browserless.io/chromium/bql";

const sessionQuery = `
mutation StartSession {
  goto(url: "https://example.com", waitUntil: networkIdle) {
    status
  }
  reconnect(timeout: 60000) { # Keeps session open for 60 seconds
    BrowserQLEndpoint
  }
}`;

async function startSession() {
  const response = await fetch(BQL_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${API_KEY}`,
    },
    body: JSON.stringify({ query: sessionQuery }),
  });

  const data = await response.json();
  console.log("Reconnect URL:", data.data.reconnect.BrowserQLEndpoint);
  return data.data.reconnect.BrowserQLEndpoint;
}

startSession();

```

```codeBlockLines_p187
import requests

API_KEY = "YOUR_API_TOKEN_HERE"
BQL_ENDPOINT = "https://production-sfo.browserless.io/chromium/bql"

session_query = """
mutation StartSession {
  goto(url: "https://example.com", waitUntil: networkIdle) {
    status
  }
  reconnect(timeout: 60000) {
    BrowserQLEndpoint
  }
}
"""

def start_session():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {"query": session_query}
    response = requests.post(BQL_ENDPOINT, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    endpoint = data['data']['reconnect']['BrowserQLEndpoint']
    print("Reconnect URL:", endpoint)
    return endpoint

start_session()

```

```codeBlockLines_p187
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class BrowserlessSession {

    private static final String API_KEY = "YOUR_API_TOKEN_HERE";
    private static final String BQL_ENDPOINT = "https://production-sfo.browserless.io/chromium/bql";

    private static final String SESSION_QUERY = """
        mutation StartSession {
          goto(url: "https://example.com", waitUntil: networkIdle) {
            status
          }
          reconnect(timeout: 60000) {
            BrowserQLEndpoint
          }
        }
        """;

    public static void main(String[] args) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();

        String jsonPayload = "{\"query\": " + new ObjectMapper().writeValueAsString(SESSION_QUERY) + "}";

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(BQL_ENDPOINT))
            .header("Content-Type", "application/json")
            .header("Authorization", "Bearer " + API_KEY)
            .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        ObjectMapper mapper = new ObjectMapper();
        JsonNode root = mapper.readTree(response.body());

        String endpoint = root.path("data")
                              .path("reconnect")
                              .path("BrowserQLEndpoint")
                              .asText();

        System.out.println("Reconnect URL: " + endpoint);
    }
}

```

```codeBlockLines_p187
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    private const string ApiKey = "YOUR_API_TOKEN_HERE";
    private const string BqlEndpoint = "https://production-sfo.browserless.io/chromium/bql";

    private const string sessionQuery = @"
    mutation StartSession {
      goto(url: ""https://example.com"", waitUntil: networkIdle) {
        status
      }
      reconnect(timeout: 60000) {
        BrowserQLEndpoint
      }
    }";

    static async Task Main()
    {
        using var client = new HttpClient();

        client.DefaultRequestHeaders.Add("Authorization", $"Bearer {ApiKey}");

        var payload = new
        {
            query = sessionQuery
        };

        var content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

        var response = await client.PostAsync(BqlEndpoint, content);
        response.EnsureSuccessStatusCode();

        var responseBody = await response.Content.ReadAsStringAsync();
        using var doc = JsonDocument.Parse(responseBody);
        var endpoint = doc.RootElement.GetProperty("data")
                                    .GetProperty("reconnect")
                                    .GetProperty("BrowserQLEndpoint")
                                    .GetString();

        Console.WriteLine("Reconnect URL: " + endpoint);
    }
}

```

### Step 2: Using the Reconnect URL [​](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless\#step-2-using-the-reconnect-url "Direct link to Step 2: Using the Reconnect URL")

Use the reconnect URL provided by the initial session setup to make subsequent queries without starting a new browser instance.

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
const RECONNECT_BQL_ENDPOINT = "YOUR_RECONNECT_BQL_ENDPOINT";

const scrapeQuery = `
mutation FetchData {
  text(selector: ".product-title") {
    text
  }
}`;

async function fetchData() {
  const response = await fetch(RECONNECT_BQL_ENDPOINT, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: scrapeQuery }),
  });

  const data = await response.json();
  console.log("Fetched Data:", data.data.text.text);
}

fetchData();

```

```codeBlockLines_p187
import requests

RECONNECT_BQL_ENDPOINT = "YOUR_RECONNECT_BQL_ENDPOINT"

scrape_query = """
mutation FetchData {
  text(selector: ".product-title") {
    text
  }
}
"""

def fetch_data():
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        RECONNECT_BQL_ENDPOINT,
        json={"query": scrape_query},
        headers=headers
    )
    response.raise_for_status()
    data = response.json()
    print("Fetched Data:", data['data']['text']['text'])

fetch_data()

```

```codeBlockLines_p187
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class FetchData {

    private static final String RECONNECT_BQL_ENDPOINT = "YOUR_RECONNECT_BQL_ENDPOINT";

    private static final String SCRAPE_QUERY = """
        mutation FetchData {
          text(selector: ".product-title") {
            text
          }
        }
        """;

    public static void main(String[] args) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();

        String jsonPayload = "{\"query\": " + new ObjectMapper().writeValueAsString(SCRAPE_QUERY) + "}";

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(RECONNECT_BQL_ENDPOINT))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        ObjectMapper mapper = new ObjectMapper();
        JsonNode root = mapper.readTree(response.body());

        String fetchedText = root.path("data").path("text").path("text").asText();

        System.out.println("Fetched Data: " + fetchedText);
    }
}

```

```codeBlockLines_p187
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    private const string ReconnectBqlEndpoint = "YOUR_RECONNECT_BQL_ENDPOINT";

    private const string scrapeQuery = @"
    mutation FetchData {
      text(selector: "".product-title"") {
        text
      }
    }";

    static async Task Main()
    {
        using var client = new HttpClient();

        var payload = new
        {
            query = scrapeQuery
        };

        var content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

        var response = await client.PostAsync(ReconnectBqlEndpoint, content);
        response.EnsureSuccessStatusCode();

        var responseBody = await response.Content.ReadAsStringAsync();
        using var doc = JsonDocument.Parse(responseBody);

        var fetchedText = doc.RootElement.GetProperty("data")
                                        .GetProperty("text")
                                        .GetProperty("text")
                                        .GetString();

        Console.WriteLine("Fetched Data: " + fetchedText);
    }
}

```

### Step 3: Refreshing Your Session [​](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless\#step-3-refreshing-your-session "Direct link to Step 3: Refreshing Your Session")

To avoid instability, refresh the reconnect endpoint periodically.

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
const refreshQuery = `
mutation RefreshSession {
  reconnect(timeout: 60000) { # Extends session timeout
    BrowserQLEndpoint
  }
}`;

async function refreshSession() {
  const response = await fetch(BQL_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${API_KEY}`,
    },
    body: JSON.stringify({ query: refreshQuery }),
  });

  const data = await response.json();
  console.log("New Reconnect URL:", data.data.reconnect.BrowserQLEndpoint);
  return data.data.reconnect.BrowserQLEndpoint;
}

```

```codeBlockLines_p187
import requests

API_KEY = "YOUR_API_TOKEN_HERE"
BQL_ENDPOINT = "https://production-sfo.browserless.io/chromium/bql"

refresh_query = """
mutation RefreshSession {
  reconnect(timeout: 60000) {
    BrowserQLEndpoint
  }
}
"""

def refresh_session():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.post(
        BQL_ENDPOINT,
        json={"query": refresh_query},
        headers=headers
    )
    response.raise_for_status()
    data = response.json()
    endpoint = data['data']['reconnect']['BrowserQLEndpoint']
    print("New Reconnect URL:", endpoint)
    return endpoint

refresh_session()

```

```codeBlockLines_p187
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class RefreshSession {

    private static final String API_KEY = "YOUR_API_TOKEN_HERE";
    private static final String BQL_ENDPOINT = "https://production-sfo.browserless.io/chromium/bql";

    private static final String REFRESH_QUERY = """
        mutation RefreshSession {
          reconnect(timeout: 60000) {
            BrowserQLEndpoint
          }
        }
        """;

    public static void main(String[] args) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();

        String jsonPayload = "{\"query\": " + new ObjectMapper().writeValueAsString(REFRESH_QUERY) + "}";

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(BQL_ENDPOINT))
            .header("Content-Type", "application/json")
            .header("Authorization", "Bearer " + API_KEY)
            .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        ObjectMapper mapper = new ObjectMapper();
        JsonNode root = mapper.readTree(response.body());

        String endpoint = root.path("data").path("reconnect").path("BrowserQLEndpoint").asText();

        System.out.println("New Reconnect URL: " + endpoint);
    }
}

```

```codeBlockLines_p187
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    private const string ApiKey = "YOUR_API_TOKEN_HERE";
    private const string BqlEndpoint = "https://production-sfo.browserless.io/chromium/bql";

    private const string refreshQuery = @"
    mutation RefreshSession {
      reconnect(timeout: 60000) {
        BrowserQLEndpoint
      }
    }";

    static async Task Main()
    {
        using var client = new HttpClient();
        client.DefaultRequestHeaders.Add("Authorization", $"Bearer {ApiKey}");

        var payload = new
        {
            query = refreshQuery
        };

        var content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

        var response = await client.PostAsync(BqlEndpoint, content);
        response.EnsureSuccessStatusCode();

        var responseBody = await response.Content.ReadAsStringAsync();
        using var doc = JsonDocument.Parse(responseBody);

        var endpoint = doc.RootElement.GetProperty("data")
                                      .GetProperty("reconnect")
                                      .GetProperty("BrowserQLEndpoint")
                                      .GetString();

        Console.WriteLine("New Reconnect URL: " + endpoint);
    }
}

```

### Full Example Code [​](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless\#full-example-code "Direct link to Full Example Code")

Here's a complete example demonstrating all steps together:

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import fetch from 'node-fetch';

const API_KEY = "YOUR_API_TOKEN_HERE";
const BQL_ENDPOINT = "https://production-sfo.browserless.io/chromium/bql";

const sessionQuery = `
mutation StartSession {
  goto(url: "https://example.com", waitUntil: networkIdle) {
    status
  }
  reconnect(timeout: 60000) { # Keeps session open for 60 seconds
    BrowserQLEndpoint
  }
}`;

async function startSession() {
  const response = await fetch(BQL_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${API_KEY}`,
    },
    body: JSON.stringify({ query: sessionQuery }),
  });

  const data = await response.json();
  console.log("Reconnect URL:", data.data.reconnect.BrowserQLEndpoint);
  return data.data.reconnect.BrowserQLEndpoint;
}

async function fetchData(reconnectUrl) {
  const scrapeQuery = `
mutation FetchData {
  text(selector: ".product-title") {
    text
  }
}`;

  const response = await fetch(reconnectUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query: scrapeQuery }),
  });

  const data = await response.json();
  console.log("Fetched Data:", data.data.text.text);
}

async function refreshSession() {
  const refreshQuery = `
mutation RefreshSession {
  reconnect(timeout: 60000) { # Extends session timeout
    BrowserQLEndpoint
  }
}`;
  const response = await fetch(BQL_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${API_KEY}`,
    },
    body: JSON.stringify({ query: refreshQuery }),
  });

  const data = await response.json();
  console.log("New Reconnect URL:", data.data.reconnect.BrowserQLEndpoint);
  return data.data.reconnect.BrowserQLEndpoint;
}

(async () => {
  let reconnectUrl = await startSession();
  let pagesScraped = 0;
  const PAGE_LIMIT = 20;

  for (let i = 0; i < 100; i++) {
    if (pagesScraped >= PAGE_LIMIT) {
      reconnectUrl = await refreshSession();
      pagesScraped = 0;
    }

    const data = await fetchData(reconnectUrl);
    console.log(`Scraped Page ${i + 1}:`, data);
    pagesScraped++;
  }
})();

```

```codeBlockLines_p187
import requests

API_KEY = "YOUR_API_TOKEN_HERE"
BQL_ENDPOINT = "https://production-sfo.browserless.io/chromium/bql"

session_query = """
mutation StartSession {
  goto(url: "https://example.com", waitUntil: networkIdle) {
    status
  }
  reconnect(timeout: 60000) {
    BrowserQLEndpoint
  }
}
"""

refresh_query = """
mutation RefreshSession {
  reconnect(timeout: 60000) {
    BrowserQLEndpoint
  }
}
"""

scrape_query = """
mutation FetchData {
  text(selector: ".product-title") {
    text
  }
}
"""

def start_session():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.post(BQL_ENDPOINT, json={"query": session_query}, headers=headers)
    response.raise_for_status()
    endpoint = response.json()['data']['reconnect']['BrowserQLEndpoint']
    print("Reconnect URL:", endpoint)
    return endpoint

def refresh_session():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.post(BQL_ENDPOINT, json={"query": refresh_query}, headers=headers)
    response.raise_for_status()
    endpoint = response.json()['data']['reconnect']['BrowserQLEndpoint']
    print("New Reconnect URL:", endpoint)
    return endpoint

def fetch_data(reconnect_url):
    headers = {"Content-Type": "application/json"}
    response = requests.post(reconnect_url, json={"query": scrape_query}, headers=headers)
    response.raise_for_status()
    data = response.json()['data']['text']['text']
    print("Fetched Data:", data)
    return data

def main():
    reconnect_url = start_session()
    pages_scraped = 0
    PAGE_LIMIT = 20

    for i in range(100):
        if pages_scraped >= PAGE_LIMIT:
            reconnect_url = refresh_session()
            pages_scraped = 0

        data = fetch_data(reconnect_url)
        print(f"Scraped Page {i + 1}:", data)
        pages_scraped += 1

if __name__ == "__main__":
    main()

```

```codeBlockLines_p187
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class BrowserlessScraper {

    static final String API_KEY = "YOUR_API_TOKEN_HERE";
    static final String BQL_ENDPOINT = "https://production-sfo.browserless.io/chromium/bql";
    static final ObjectMapper mapper = new ObjectMapper();
    static final HttpClient client = HttpClient.newHttpClient();

    static String executeQuery(String url, String query, boolean auth) throws Exception {
        String payload = mapper.writeValueAsString(new Query(query));
        var requestBuilder = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(payload));

        if (auth) requestBuilder.header("Authorization", "Bearer " + API_KEY);

        var response = client.send(requestBuilder.build(), HttpResponse.BodyHandlers.ofString());
        return response.body();
    }

    static String startSession() throws Exception {
        String sessionQuery = """
        mutation StartSession {
          goto(url: "https://example.com", waitUntil: networkIdle) { status }
          reconnect(timeout: 60000) { BrowserQLEndpoint }
        }""";
        String json = executeQuery(BQL_ENDPOINT, sessionQuery, true);
        return mapper.readTree(json).path("data").path("reconnect").path("BrowserQLEndpoint").asText();
    }

    static String refreshSession() throws Exception {
        String refreshQuery = """
        mutation RefreshSession {
          reconnect(timeout: 60000) { BrowserQLEndpoint }
        }""";
        String json = executeQuery(BQL_ENDPOINT, refreshQuery, true);
        return mapper.readTree(json).path("data").path("reconnect").path("BrowserQLEndpoint").asText();
    }

    static String fetchData(String reconnectUrl) throws Exception {
        String scrapeQuery = """
        mutation FetchData {
          text(selector: ".product-title") { text }
        }""";
        String json = executeQuery(reconnectUrl, scrapeQuery, false);
        return mapper.readTree(json).path("data").path("text").path("text").asText();
    }

    public static void main(String[] args) throws Exception {
        String reconnectUrl = startSession();
        System.out.println("Reconnect URL: " + reconnectUrl);
        int pagesScraped = 0, PAGE_LIMIT = 20;

        for (int i = 0; i < 100; i++) {
            if (pagesScraped >= PAGE_LIMIT) {
                reconnectUrl = refreshSession();
                System.out.println("New Reconnect URL: " + reconnectUrl);
                pagesScraped = 0;
            }

            String data = fetchData(reconnectUrl);
            System.out.printf("Scraped Page %d: %s%n", i + 1, data);
            pagesScraped++;
        }
    }

    static class Query {
        public String query;
        Query(String q) { this.query = q; }
    }
}

```

```codeBlockLines_p187
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    const string ApiKey = "YOUR_API_TOKEN_HERE";
    const string BqlEndpoint = "https://production-sfo.browserless.io/chromium/bql";

    const string sessionQuery = @"
    mutation StartSession {
      goto(url: ""https://example.com"", waitUntil: networkIdle) { status }
      reconnect(timeout: 60000) { BrowserQLEndpoint }
    }";

    const string refreshQuery = @"
    mutation RefreshSession {
      reconnect(timeout: 60000) { BrowserQLEndpoint }
    }";

    const string scrapeQuery = @"
    mutation FetchData {
      text(selector: "".product-title"") { text }
    }";

    static async Task<string> ExecuteQuery(string url, string query, bool auth)
    {
        using var client = new HttpClient();
        if (auth) client.DefaultRequestHeaders.Add("Authorization", $"Bearer {ApiKey}");

        var content = new StringContent(JsonSerializer.Serialize(new { query }), Encoding.UTF8, "application/json");
        var response = await client.PostAsync(url, content);
        response.EnsureSuccessStatusCode();

        var json = await response.Content.ReadAsStringAsync();
        return json;
    }

    static async Task Main()
    {
        var jsonDoc = JsonDocument.Parse(await ExecuteQuery(BqlEndpoint, sessionQuery, true));
        var reconnectUrl = jsonDoc.RootElement.GetProperty("data").GetProperty("reconnect").GetProperty("BrowserQLEndpoint").GetString();
        Console.WriteLine("Reconnect URL: " + reconnectUrl);

        int pagesScraped = 0, PAGE_LIMIT = 20;

        for (int i = 0; i < 100; i++)
        {
            if (pagesScraped >= PAGE_LIMIT)
            {
                jsonDoc = JsonDocument.Parse(await ExecuteQuery(BqlEndpoint, refreshQuery, true));
                reconnectUrl = jsonDoc.RootElement.GetProperty("data").GetProperty("reconnect").GetProperty("BrowserQLEndpoint").GetString();
                Console.WriteLine("New Reconnect URL: " + reconnectUrl);
                pagesScraped = 0;
            }

            jsonDoc = JsonDocument.Parse(await ExecuteQuery(reconnectUrl, scrapeQuery, false));
            var data = jsonDoc.RootElement.GetProperty("data").GetProperty("text").GetProperty("text").GetString();
            Console.WriteLine($"Scraped Page {i + 1}: {data}");
            pagesScraped++;
        }
    }
}

```

## Improving Efficiency with BrowserQL's Reject API [​](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless\#improving-efficiency-with-browserqls-reject-api "Direct link to Improving Efficiency with BrowserQL's Reject API")

BrowserQL also lets you reject unnecessary requests (e.g., images, media) to optimize resource usage:

```codeBlockLines_p187
mutation OptimizeSession {
  setRequestInterception(enabled: true)
  reject(patterns: ["*.png", "*.jpg", "*.mp4"])
}

```

Use this to further streamline your scraping tasks.

## Common Issues [​](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless\#common-issues "Direct link to Common Issues")

### CAPTCHA Challenges [​](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless\#captcha-challenges "Direct link to CAPTCHA Challenges")

If you encounter CAPTCHAs, ensure your session maintains human-like interaction patterns by reducing request rates and maintaining stable sessions.

### Session Timeouts [​](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless\#session-timeouts "Direct link to Session Timeouts")

Set appropriate timeout values to ensure sessions remain active without resource leaks:

```codeBlockLines_p187
reconnect(timeout: 120000)

```

- [Implementing Reconnects with BrowserQL](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#implementing-reconnects-with-browserql)
  - [Step 1: Initial Setup](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#step-1-initial-setup)
  - [Step 2: Using the Reconnect URL](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#step-2-using-the-reconnect-url)
  - [Step 3: Refreshing Your Session](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#step-3-refreshing-your-session)
  - [Full Example Code](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#full-example-code)
- [Improving Efficiency with BrowserQL's Reject API](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#improving-efficiency-with-browserqls-reject-api)
- [Common Issues](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#common-issues)
  - [CAPTCHA Challenges](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#captcha-challenges)
  - [Session Timeouts](https://docs.browserless.io/browserql/session-management/reconnect-to-browserless#session-timeouts)