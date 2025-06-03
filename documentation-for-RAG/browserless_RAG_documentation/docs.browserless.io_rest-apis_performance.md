---
url: "https://docs.browserless.io/rest-apis/performance"
title: "/performance API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/performance#__docusaurus_skipToContent_fallback)

On this page

The performance API reveals key metrics about a site's accessibility, best practices, performance, PWA information, and SEO, from a performance standpoint. It includes useful metrics like latency, time-to-interaction, design contrast other recommendations. This API is powered by [Google's Lighthouse](https://github.com/GoogleChrome/lighthouse) project, and it's compatible with its CLI options.

In order to gather this data, send a `POST` request to `https://production-sfo.browserless.io/performance` if on a hosted plan, with a simple JSON payload containing a valid URL.

warning

Due to the number of checks gathered it can take anywhere from several seconds to minutes depending on the site and size of the worker.

You can [check the full Open API schema here](https://docs.browserless.io/open-api#tag/Browser-REST-APIs/paths/~1chrome~1performance/post).

### Examples [​](https://docs.browserless.io/rest-apis/performance\#examples "Direct link to Examples")

1. [Basic Usage](https://docs.browserless.io/rest-apis/performance#basic-usage)
2. [Gathering metrics for a category](https://docs.browserless.io/rest-apis/performance#gathering-metrics-for-a-category)
3. [Gathering metrics from a single audit](https://docs.browserless.io/rest-apis/performance#gathering-metrics-from-a-single-audit)

## Basic Usage [​](https://docs.browserless.io/rest-apis/performance\#basic-usage "Direct link to Basic Usage")

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/"
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/performance?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://example.com/"
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/performance?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/"
};

const fetchPerformanceMetrics = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

fetchPerformanceMetrics();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/performance?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/"
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print(result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class FetchPerformanceMetrics {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/performance?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/"
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
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/performance?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/""
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

By default, the `/performance` API will gather **all** the metrics. This will not only result in a **really** big JSON response (350kb to 800kb on average) and it **will** take some seconds (to minutes) to complete.

Each test has a score that indicates how well it performed, where 1 is the maximum and 0 is the lowest, generating a response like this:

```codeBlockLines_p187
  // ...
  "audits": {
    "is-on-https": {
      "title": "Uses HTTPS",
      "score": 1
      // ...
    },
    "viewport": {
      "title": "Has a `<meta name=\"viewport\">` tag with `width` or `initial-scale`",
      "score": 1
      // ...
    },
    "first-contentful-paint": {
      "score": 1,
      "displayValue": "0.8 s"
      // ...
    }
    // ...
  }

```

## Gathering metrics for a category [​](https://docs.browserless.io/rest-apis/performance\#gathering-metrics-for-a-category "Direct link to Gathering metrics for a category")

You can get metrics from specific categories, using the `config` property. [Just like Lighthouse](https://github.com/GoogleChrome/lighthouse/blob/master/readme.md#cli-options), available categories are `accessibility`, `best practices`, `performance`, `pwa`, and `seo`

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com",
  "config": {
    "extends": "lighthouse:default",
    "settings": {
      "onlyCategories": ["accessibility"]
    }
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/performance?token=YOUR_API_TOKEN_HERE' \
  --header 'Cache-Control: no-cache' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "https://browserless.io",
  "config": {
    "extends": "lighthouse:default",
    "settings": {
      "onlyCategories": ["accessibility"]
    }
  }
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/performance?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://browserless.io",
  config: {
    extends: "lighthouse:default",
    settings: {
      onlyCategories: ["accessibility"]
    }
  }
};

const fetchPerformanceMetrics = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

fetchPerformanceMetrics();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/performance?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://browserless.io",
    "config": {
        "extends": "lighthouse:default",
        "settings": {
            "onlyCategories": ["accessibility"]
        }
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

public class FetchPerformanceWithConfig {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/performance?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://browserless.io",
            "config": {
                "extends": "lighthouse:default",
                "settings": {
                    "onlyCategories": ["accessibility"]
                }
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
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/performance?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://browserless.io"",
            ""config"": {
                ""extends"": ""lighthouse:default"",
                ""settings"": {
                    ""onlyCategories"": [""accessibility""]
                }
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

This will gather the predefined metrics defined by Lighthouse for that category:

```codeBlockLines_p187
  // ...
  "audits": {
    "aria-command-name": {
      "title": "`button`, `link`, and `menuitem` elements have accessible names",
      "score": 1
      // ...
    },
    "aria-hidden-body": {
      "title": "`[aria-hidden=\"true\"]` is not present on the document `<body>`",
      "score": 1
      // ...
    },
    "aria-hidden-focus": {
      "title": "`[aria-hidden=\"true\"]` elements do not contain focusable descendents",
      "score": 1
      // ...
    },
    // ...
  }

```

## Gathering metrics from a single audit [​](https://docs.browserless.io/rest-apis/performance\#gathering-metrics-from-a-single-audit "Direct link to Gathering metrics from a single audit")

You can get any specific metrics [valid in Lighthouse](https://github.com/GoogleChrome/lighthouse/tree/master/core/audits)

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://browserless.io",
  "config": {
    "extends": "lighthouse:default",
    "settings": {
      "onlyAudits": ["unminified-css"]
    }
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/performance?token=YOUR_API_TOKEN_HERE' \
  --header 'Cache-Control: no-cache' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "https://browserless.io",
  "config": {
    "extends": "lighthouse:default",
    "settings": {
      "onlyCategories": ["accessibility"]
    }
  }
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/performance?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://browserless.io",
  config: {
    extends: "lighthouse:default",
    settings: {
      onlyCategories: ["accessibility"]
    }
  }
};

const fetchPerformanceMetrics = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

fetchPerformanceMetrics();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/performance?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://browserless.io",
    "config": {
        "extends": "lighthouse:default",
        "settings": {
            "onlyCategories": ["accessibility"]
        }
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

public class FetchPerformanceWithConfig {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/performance?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://browserless.io",
            "config": {
                "extends": "lighthouse:default",
                "settings": {
                    "onlyCategories": ["accessibility"]
                }
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
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/performance?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://browserless.io"",
            ""config"": {
                ""extends"": ""lighthouse:default"",
                ""settings"": {
                    ""onlyCategories"": [""accessibility""]
                }
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

**Response example**

```codeBlockLines_p187
  // ...
  "audits": {
    "unminified-css": {
      "title": "Minify CSS",
      "score": 1
      // ...
    },
    // ...
  }

```

- [Examples](https://docs.browserless.io/rest-apis/performance#examples)
- [Basic Usage](https://docs.browserless.io/rest-apis/performance#basic-usage)
- [Gathering metrics for a category](https://docs.browserless.io/rest-apis/performance#gathering-metrics-for-a-category)
- [Gathering metrics from a single audit](https://docs.browserless.io/rest-apis/performance#gathering-metrics-from-a-single-audit)