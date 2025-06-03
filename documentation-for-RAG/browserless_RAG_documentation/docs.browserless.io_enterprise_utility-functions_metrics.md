---
url: "https://docs.browserless.io/enterprise/utility-functions/metrics"
title: "/metrics API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/utility-functions/metrics#__docusaurus_skipToContent_fallback)

On this page

The metrics API allows you to retrieve an array of session statistics. The data returned will have a maximum date of 1 week.

You can [check the full Open API schema here](https://docs.browserless.io/open-api#tag/Management-REST-APIs/paths/~1metrics/get).

## Gathering metrics from your workers [​](https://docs.browserless.io/enterprise/utility-functions/metrics\#gathering-metrics-from-your-workers "Direct link to Gathering metrics from your workers")

To see statistics regarding your workers, simply issue a `GET` request to `/metrics`:

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X GET \
  https://production-sfo.browserless.io/metrics?token=YOUR_API_TOKEN_HERE

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/metrics?token=${TOKEN}`;

const fetchMetrics = async () => {
  const response = await fetch(url, {
    method: 'GET'
  });

  const result = await response.json();
  console.log(result);
};

fetchMetrics();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/metrics?token={TOKEN}"

response = requests.get(url)
result = response.json()

print(result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class FetchMetrics {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/metrics?token=" + TOKEN;

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
        string url = $"https://production-sfo.browserless.io/metrics?token={TOKEN}";

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

warning

Remember that running this in the browser will expose your API key!

Running this request will result in an output like:

```codeBlockLines_p187
[\
  {\
    "error": 3,\
    "maxConcurrent": 4,\
    "queued": 0,\
    "rejected": 0,\
    "running": 3,\
    "sessionTimes": [992, 1041, 802],\
    "successful": 0,\
    "timedout": 0,\
    "unauthorized": 0,\
    "unhealthy": 0,\
    "maxTime": 1041,\
    "meanTime": 945,\
    "minTime": 802,\
    "totalTime": 2835,\
    "units": 3,\
    "date": 1709134233732,\
    "cpu": 0.024877870173220466,\
    "memory": 0.7784158564199399\
  },\
  // ...\
]

```

### /metrics/total [​](https://docs.browserless.io/enterprise/utility-functions/metrics\#metricstotal "Direct link to /metrics/total")

This route will output a similar payload, but with the total stats of all sessions.

- [Gathering metrics from your workers](https://docs.browserless.io/enterprise/utility-functions/metrics#gathering-metrics-from-your-workers)
  - [/metrics/total](https://docs.browserless.io/enterprise/utility-functions/metrics#metricstotal)