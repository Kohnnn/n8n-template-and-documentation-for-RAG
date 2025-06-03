---
url: "https://docs.browserless.io/enterprise/utility-functions/config"
title: "/config API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/utility-functions/config#__docusaurus_skipToContent_fallback)

On this page

The `/config` API will give you information about your worker's configuration, **and is only available for dedicated and self-hosted accounts**

You can [check the full Open API schema here](https://docs.browserless.io/open-api#tag/Management-REST-APIs/paths/~1config/get).

## Get your worker's configuration [​](https://docs.browserless.io/enterprise/utility-functions/config\#get-your-workers-configuration "Direct link to Get your worker's configuration")

To see your current configuration, simply issue a `GET` request to `/sessions`:

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X GET \
  https://production-sfo.browserless.io/config?token=YOUR_API_TOKEN_HERE

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/config?token=${TOKEN}`;

const fetchConfig = async () => {
  const response = await fetch(url, {
    method: 'GET'
  });

  const result = await response.json();
  console.log(result);
};

fetchConfig();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/config?token={TOKEN}"

response = requests.get(url)
result = response.json()

print(result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class FetchConfig {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/config?token=" + TOKEN;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .GET()
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
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/config?token={TOKEN}";

        using var client = new HttpClient();

        try {
            var response = await client.GetAsync(url);
            response.EnsureSuccessStatusCode();

            var result = await response.Content.ReadAsStringAsync();
            Console.WriteLine("Response: " + result);
        } catch (Exception ex) {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

Running this request will result in an JSON output like:

```codeBlockLines_p187
{
  "allowCORS": true,
  "allowFileProtocol": false,
  "allowGetCalls": false,
  "concurrent": 10,
  "data": "/tmp/browserless-data-dirs",
  "debug": "browserless*,-**:verbose",
  "errorAlertURL": null,
  "healthFailureURL": null,
  "host": "localhost",
  "maxCPU": 99,
  "maxMemory": 99,
  "metricsJSONPath": "/tmp/browserless-metrics.json",
  "port": 3001,
  "queued": 10,
  "queuedAlertURL": null,
  "rejectAlertURL": null,
  "retries": 5,
  "timeout": 30000,
  "timeoutAlertURL": null,
  "token": "6R0W53R135510"
}

```

- [Get your worker's configuration](https://docs.browserless.io/enterprise/utility-functions/config#get-your-workers-configuration)