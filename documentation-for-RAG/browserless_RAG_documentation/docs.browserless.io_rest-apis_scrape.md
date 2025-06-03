---
url: "https://docs.browserless.io/rest-apis/scrape"
title: "/scrape API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/scrape#__docusaurus_skipToContent_fallback)

On this page

BrowserQL

We recommended using [**BrowserQL**](https://docs.browserless.io/browserql/start), Browserless' first-class browser automation API, to scrape content from any website.

The /scrape API allows for getting the contents a page, by specifying selectors you are interested in, and returning a structured JSON response. We also allow for setting a timeout option for asynchronously added elements.

The default behavior is to navigate to the URL specified, wait for the page to load (including parsing and executing of JavaScript), then waiting for the elements for a maximum of 30 seconds. All of these are configurable, and documented in detail below.

At a minimum you'll need to specify at least a `url` and an `elements` array.

You can [check the full Open API schema here](https://docs.browserless.io/open-api#tag/Browser-REST-APIs/paths/~1chrome~1scrape/post).

## Basic Usage [​](https://docs.browserless.io/rest-apis/scrape\#basic-usage "Direct link to Basic Usage")

Below is the most basic usage, where we'll navigate to the example.com website (waiting for page-load) and parse out all a elements.

Internally we use document.querySelectorAll to retrieve all matches on a page. Using a more specific selector can narrow down the returned results.

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://browserless.io/",
  "elements": [\
    { "selector": "h1" }\
  ]
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/scrape?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://browserless.io/",
  "elements": [\
    { "selector": "h1" }\
  ]
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/scrape?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://browserless.io/",
  elements: [\
    { selector: "h1" }\
  ]
};

const scrapeContent = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

scrapeContent();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/scrape?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://browserless.io/",
    "elements": [\
        { "selector": "h1" }\
    ]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print(result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class ScrapeContent {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/scrape?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://browserless.io/",
            "elements": [\
                { "selector": "h1" }\
            ]
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
        string url = $"https://production-sfo.browserless.io/scrape?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://browserless.io/"",
            ""elements"": [\
                { ""selector"": ""h1"" }\
            ]
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

**Response Example**

```codeBlockLines_p187
{
  "data": [\
    {\
      "results": [\
        {\
          "attributes": [\
            { "name": "class", "value": "..." }\
          ],\
          "height": 120,\
          "html": "Headless browser automation, without the hosting headaches",\
          "left": 32,\
          "text": "Headless browser automation, without the hosting headaches",\
          "top": 196,\
          "width": 736\
        }\
      ],\
      "selector": "h1"\
    }\
  ]
}

```

## Specifying page-load behavior [​](https://docs.browserless.io/rest-apis/scrape\#specifying-page-load-behavior "Direct link to Specifying page-load behavior")

The scrape API allows for setting specific page-load behaviors by setting a `gotoOptions` in the JSON body. This is passed directly into [puppeteer's `goto()` method](https://pptr.dev/api/puppeteer.page.goto).

In the example below, we'll set a `waitUntil` property and a `timeout`.

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    { "selector": "h1" }\
  ],
  "gotoOptions": {
    "timeout": 10000,
    "waitUntil": "networkidle2"
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/scrape?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://example.com/",
  "elements": [\
    { "selector": "h1" }\
  ],
  "gotoOptions": {
    "timeout": 10000,
    "waitUntil": "networkidle2"
  }
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/scrape?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  elements: [\
    { selector: "h1" }\
  ],
  gotoOptions: {
    timeout: 10000,
    waitUntil: "networkidle2"
  }
};

const scrapeContent = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

scrapeContent();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/scrape?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "elements": [\
        { "selector": "h1" }\
    ],
    "gotoOptions": {
        "timeout": 10000,
        "waitUntil": "networkidle2"
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

public class ScrapeContentWithOptions {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/scrape?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "elements": [\
                { "selector": "h1" }\
            ],
            "gotoOptions": {
                "timeout": 10000,
                "waitUntil": "networkidle2"
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
        string url = $"https://production-sfo.browserless.io/scrape?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""elements"": [\
                { ""selector"": ""h1"" }\
            ],
            ""gotoOptions"": {
                ""timeout"": 10000,
                ""waitUntil"": ""networkidle2""
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

## Custom behavior with `waitFor` options [​](https://docs.browserless.io/rest-apis/scrape\#custom-behavior-with-waitfor-options "Direct link to custom-behavior-with-waitfor-options")

Sometimes it's helpful to do further actions, or wait for custom events on the page before getting data. We allow this behavior with the `waitFor` properties.

### waitForTimeout [​](https://docs.browserless.io/rest-apis/scrape\#waitfortimeout "Direct link to waitForTimeout")

Waits for the given number of milliseconds before continue execution.

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    { "selector": "h1" }\
  ],
  "waitForTimeout": 1000,
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/scrape?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://example.com/",
  "elements": [\
    { "selector": "h1" }\
  ],
  "waitForTimeout": 1000
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/scrape?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  elements: [\
    { selector: "h1" }\
  ],
  waitForTimeout: 1000
};

const scrapeContent = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

scrapeContent();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/scrape?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "elements": [\
        { "selector": "h1" }\
    ],
    "waitForTimeout": 1000
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print(result)

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;

public class ScrapeContentWithTimeout {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/scrape?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "elements": [\
                { "selector": "h1" }\
            ],
            "waitForTimeout": 1000
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
        string url = $"https://production-sfo.browserless.io/scrape?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""elements"": [\
                { ""selector"": ""h1"" }\
            ],
            ""waitForTimeout"": 1000
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

### waitForSelector [​](https://docs.browserless.io/rest-apis/scrape\#waitforselector "Direct link to waitForSelector")

Wait for a selector to appear in page. If at the moment of calling the method the selector already exists, the method will return immediately. If the selector doesn't appear after the timeout milliseconds of waiting, the function will throw an exception.

#### Example [​](https://docs.browserless.io/rest-apis/scrape\#example "Direct link to Example")

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    { "selector": "h1" }\
  ],
  "waitForSelector": {
    "selector": "h1",
    "timeout": 5000
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/scrape?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://example.com/",
  "elements": [\
    { "selector": "h1" }\
  ],
  "waitForSelector": {
    "selector": "h1",
    "timeout": 5000
  }
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/scrape?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  elements: [\
    { selector: "h1" }\
  ],
  waitForSelector: {
    selector: "h1",
    timeout: 5000
  }
};

const scrapeContent = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

scrapeContent();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/scrape?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "elements": [\
        { "selector": "h1" }\
    ],
    "waitForSelector": {
        "selector": "h1",
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

public class ScrapeContentWithWaitForSelector {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/scrape?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "elements": [\
                { "selector": "h1" }\
            ],
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
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/scrape?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""elements"": [\
                { ""selector"": ""h1"" }\
            ],
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

### waitForFunction [​](https://docs.browserless.io/rest-apis/scrape\#waitforfunction "Direct link to waitForFunction")

Waits for the provided function to return before cotinue. The function can be any valid JS function, including `async` functions.

#### Example [​](https://docs.browserless.io/rest-apis/scrape\#example-1 "Direct link to Example")

**JS function**

```codeBlockLines_p187
async () => {
  const res = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const json = await res.json();

  document.querySelector("h1").innerText = json.title;
}

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
  "elements": [\
    { "selector": "h1" }\
  ],
  "waitForFunction": {
    "fn": "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
    "timeout": 5000
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/scrape?token=YOUR_API_TOKEN_HERE \
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
const url = `https://production-sfo.browserless.io/scrape?token=${TOKEN}`;
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

const scrapeContent = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

scrapeContent();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/scrape?token={TOKEN}"
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

public class ScrapeContentWithWaitForFunction {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/scrape?token=" + TOKEN;

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
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/scrape?token={TOKEN}";

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

### waitForEvent [​](https://docs.browserless.io/rest-apis/scrape\#waitforevent "Direct link to waitForEvent")

Waits for an event to happen on the page before cotinue.

#### Example [​](https://docs.browserless.io/rest-apis/scrape\#example-2 "Direct link to Example")

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
// Will fail since the event never fires
{
  "url": "https://example.com/",
  "elements": [\
    { "selector": "h1" }\
  ],
  "waitForEvent": {
    "event": "fullscreenchange",
    "timeout": 5000
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://example.com/",
  "elements": [\
    { "selector": "h1" }\
  ],
  "waitForEvent": {
    "event": "fullscreenchange",
    "timeout": 5000
  }
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/content?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  elements: [\
    { selector: "h1" }\
  ],
  waitForEvent: {
    event: "fullscreenchange",
    timeout: 5000
  }
};

const fetchContent = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

fetchContent();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/content?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "elements": [\
        { "selector": "h1" }\
    ],
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

public class FetchContentWithWaitForEvent {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "elements": [\
                { "selector": "h1" }\
            ],
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
using System.Text.Json;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/content?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""elements"": [\
                { ""selector"": ""h1"" }\
            ],
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

- [Basic Usage](https://docs.browserless.io/rest-apis/scrape#basic-usage)
- [Specifying page-load behavior](https://docs.browserless.io/rest-apis/scrape#specifying-page-load-behavior)
- [Custom behavior with `waitFor` options](https://docs.browserless.io/rest-apis/scrape#custom-behavior-with-waitfor-options)
  - [waitForTimeout](https://docs.browserless.io/rest-apis/scrape#waitfortimeout)
  - [waitForSelector](https://docs.browserless.io/rest-apis/scrape#waitforselector)
  - [waitForFunction](https://docs.browserless.io/rest-apis/scrape#waitforfunction)
  - [waitForEvent](https://docs.browserless.io/rest-apis/scrape#waitforevent)