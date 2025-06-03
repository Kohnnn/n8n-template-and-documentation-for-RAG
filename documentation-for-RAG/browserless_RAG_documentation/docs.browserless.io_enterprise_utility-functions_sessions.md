---
url: "https://docs.browserless.io/enterprise/utility-functions/sessions"
title: "/sessions API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/utility-functions/sessions#__docusaurus_skipToContent_fallback)

On this page

The sessions API allows you to gather information about the currently running sessions **and is only available for dedicated and self-hosted accounts**

You can [check the full Open API schema here](https://docs.browserless.io/open-api#tag/Management-REST-APIs/paths/~1sessions/get).

## Gathering information from your running sessions [​](https://docs.browserless.io/enterprise/utility-functions/sessions\#gathering-information-from-your-running-sessions "Direct link to Gathering information from your running sessions")

To see information regarding the running sessions, simply issue a `GET` request to `/sessions`:

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X GET \
  https://production-sfo.browserless.io/sessions?token=YOUR_API_TOKEN_HERE

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/sessions?token=${TOKEN}`;

const fetchSessions = async () => {
  const response = await fetch(url, {
    method: 'GET'
  });

  const result = await response.json();
  console.log(result);
};

fetchSessions();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/sessions?token={TOKEN}"

response = requests.get(url)
result = response.json()

print(result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class FetchSessions {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/sessions?token=" + TOKEN;

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
        string url = $"https://production-sfo.browserless.io/sessions?token={TOKEN}";

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
[{\
  "id": null,\
  "initialConnectURL": "wss://production-sfo.browserless.io/firefox/playwright/?token=YOUR_API_TOKEN_HERE",\
  "isTempDataDir": true,\
  "launchOptions": {},\
  "numbConnected": 1,\
  "routePath": ["/firefox/playwright", "/firefox/playwright"],\
  "startedOn": 1709584439748,\
  "ttl": 0,\
  "userDataDir": null,\
  "browser": "FirefoxPlaywright",\
  "browserId": "d9a8570a73666d79d79ac23f07cf8966",\
  "killURL": null,\
  "running": true,\
  "timeAliveMs": 10118,\
  "type": "browser"\
}]

```

- [Gathering information from your running sessions](https://docs.browserless.io/enterprise/utility-functions/sessions#gathering-information-from-your-running-sessions)