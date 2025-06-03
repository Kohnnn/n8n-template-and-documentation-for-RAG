---
url: "https://docs.browserless.io/rest-apis/content"
title: "/content API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/content#__docusaurus_skipToContent_fallback)

On this page

BrowserQL

We recommended using [**BrowserQL**](https://docs.browserless.io/browserql/start), Browserless' first-class browser automation API, to capture content from any website.

The content API allows for simple navigation to a site and capturing the page's content (including the `<head>` section). Browserless will respond with a `Content-Type` of `text/html`, and string of the site's HTML after it has been rendered and evaluated inside the browser. This is useful for capturing the content of a page that has a lot of JavaScript or other interactivity.

You can [check the full Open API schema here](https://docs.browserless.io/open-api#tag/Browser-REST-APIs/paths/~1chrome~1content/post).

## Basic Usage [​](https://docs.browserless.io/rest-apis/content\#basic-usage "Direct link to Basic Usage")

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
  https://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/"
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
    url: "https://example.com/"
};

const fetchContent = async () => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });

    const content = await response.text();
    console.log(content);
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
    "url": "https://example.com/"
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;

public class FetchContent {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN;

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = """
            {
                "url": "https://example.com/"
            }
        """;

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("Cache-Control", "no-cache")
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
  using System.Text;
  using System.Text.Json;

  class Program
  {
      static async Task Main(string[] args)
      {
          string TOKEN = "YOUR_API_TOKEN_HERE";
          string url = $"https://production-sfo.browserless.io/content?token={TOKEN}";

          var payload = new
          {
              url = "https://example.com/"
          };

          var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

          using var httpClient = new HttpClient();
          try
          {
              var request = new HttpRequestMessage(HttpMethod.Post, url)
              {
                  Content = jsonContent
              };

              request.Headers.Add("Cache-Control", "no-cache");

              var response = await httpClient.SendAsync(request);
              response.EnsureSuccessStatusCode();
              var result = await response.Content.ReadAsStringAsync();
              Console.WriteLine("Response: " + result);
          }
          catch (Exception e)
          {
              Console.WriteLine("Error: " + e.Message);
          }
      }
  }

```

## Rejecting Undesired Requests [​](https://docs.browserless.io/rest-apis/content\#rejecting-undesired-requests "Direct link to Rejecting Undesired Requests")

You can use `rejectResourceTypes` and `rejectRequestPattern` to block undesired content, resources and requests.

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
// Will reject any images and .css files
{
  "url": "https://browserless.io/"
  "rejectResourceTypes": ["image"],
  "rejectRequestPattern": ["/^.*\\.(css)"]
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://browserless.io/"
  "rejectResourceTypes": ["image"],
  "rejectRequestPattern": ["/^.*\\.(css)"]
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
    rejectResourceTypes: ["image"],
    rejectRequestPattern: ["/^.*\\.(css)"]
};

const fetchContent = async () => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });

    const content = await response.text();
    console.log(content);
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
    "rejectResourceTypes": ["image"],
    "rejectRequestPattern": ["/^.*\\.(css)"]
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import com.google.gson.*;

public class FetchContentWithRejection {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN;

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = new Gson().toJson(Map.of(
            "url", "https://browserless.io/",
            "rejectResourceTypes", new String[] { "image" },
            "rejectRequestPattern", new String[] { "/^.*\\.(css)/" }
        ));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("Cache-Control", "no-cache")
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
using System.Text;
  using System.Text.Json;

  class Program
  {
  		static async Task Main(string[] args)
  		{
  				string TOKEN = "YOUR_API_TOKEN_HERE";
  				string url = $"https://production-sfo.browserless.io/content?token={TOKEN}";

  				var payload = new
  				{
  						url = "https://browserless.io/",
  						rejectResourceTypes = new[] { "image" },
  						rejectRequestPattern = new[] { "/^.*\\.(css)/" }
  				};

  				var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

  				using var httpClient = new HttpClient();
  				try
  				{
  						var request = new HttpRequestMessage(HttpMethod.Post, url)
  						{
  								Content = jsonContent
  						};

  						request.Headers.Add("Cache-Control", "no-cache");

  						var response = await httpClient.SendAsync(request);
  						response.EnsureSuccessStatusCode();
  						var result = await response.Content.ReadAsStringAsync();
  						Console.WriteLine("Response: " + result);
  				}
  				catch (Exception e)
  				{
  						Console.WriteLine("Error: " + e.Message);
  				}
  		}
  }

```

## Navigation Options [​](https://docs.browserless.io/rest-apis/content\#navigation-options "Direct link to Navigation Options")

You can use the `gotoOptions` to modify the default navigation behavior for the requested URL. The objects mirror [Puppeteer's `GoToOptions` interface](https://pptr.dev/api/puppeteer.gotooptions).

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "gotoOptions": { "waitUntil": "networkidle2" },
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "gotoOptions": { "waitUntil": "networkidle2" }
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
    gotoOptions: { "waitUntil": "networkidle2" },
};

const fetchContent = async () => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });

    const content = await response.text();
    console.log(content);
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
    "gotoOptions": { "waitUntil": "networkidle2" }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import com.google.gson.*;

public class FetchContent {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN;

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = new Gson().toJson(Map.of(
            "url", "https://example.com/",
            "gotoOptions", Map.of("waitUntil", "networkidle2")
        ));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("Cache-Control", "no-cache")
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
using System.Text;
	using System.Text.Json;

	class Program
	{
			static async Task Main(string[] args)
			{
					string TOKEN = "YOUR_API_TOKEN_HERE";
					string url = $"https://production-sfo.browserless.io/content?token={TOKEN}";

					var payload = new
					{
							url = "https://example.com/",
							gotoOptions = new { waitUntil = "networkidle2" }
					};

					var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

					using var httpClient = new HttpClient();
					try
					{
							var request = new HttpRequestMessage(HttpMethod.Post, url)
							{
									Content = jsonContent
							};

							request.Headers.Add("Cache-Control", "no-cache");

							var response = await httpClient.SendAsync(request);
							response.EnsureSuccessStatusCode();
							var result = await response.Content.ReadAsStringAsync();
							Console.WriteLine("Response: " + result);
					}
					catch (Exception e)
					{
							Console.WriteLine("Error: " + e.Message);
					}
			}
	}

```

## Continue on error [​](https://docs.browserless.io/rest-apis/content\#continue-on-error "Direct link to Continue on error")

You can use `bestAttempt` to make Browserless attempt to proceed when async events fail or timeout. This includes things like the `goto` or `waitForSelector` proprieties in the JSON payload.

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "bestAttempt": true,

  // This would fail without bestAttempt
  "waitForSelector": { "selector": "table", "timeout": 500 }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "bestAttempt": true,
  "waitForSelector": { "selector": "table", "timeout": 500 }
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
    bestAttempt: true,
    waitForSelector: { "selector": "table", "timeout": 500 }
};

const fetchContent = async () => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });

    const content = await response.text();
    console.log(content);
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
    "bestAttempt": True,
    "waitForSelector": { "selector": "table", "timeout": 500 }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import com.google.gson.*;

public class FetchContentWithWait {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN;

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = new Gson().toJson(Map.of(
            "url", "https://example.com/",
            "bestAttempt", true,
            "waitForSelector", Map.of(
                "selector", "table",
                "timeout", 500
            )
        ));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("Cache-Control", "no-cache")
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
using System.Text;
	using System.Text.Json;

	class Program
	{
			static async Task Main(string[] args)
			{
					string TOKEN = "YOUR_API_TOKEN_HERE";
					string url = $"https://production-sfo.browserless.io/content?token={TOKEN}";

					var payload = new
					{
							url = "https://example.com/",
							bestAttempt = true,
							waitForSelector = new
							{
									selector = "table",
									timeout = 500
							}
					};

					var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

					using var httpClient = new HttpClient();
					try
					{
							var request = new HttpRequestMessage(HttpMethod.Post, url)
							{
									Content = jsonContent
							};

							request.Headers.Add("Cache-Control", "no-cache");

							var response = await httpClient.SendAsync(request);
							response.EnsureSuccessStatusCode();
							var result = await response.Content.ReadAsStringAsync();
							Console.WriteLine("Response: " + result);
					}
					catch (Exception e)
					{
							Console.WriteLine("Error: " + e.Message);
					}
			}
	}

```

## Waiting for Things [​](https://docs.browserless.io/rest-apis/content\#waiting-for-things "Direct link to Waiting for Things")

Browserless offers 4 different ways to wait for preconditions to be met on page. These are events, functions, selectors and timeouts.

### waitForEvent [​](https://docs.browserless.io/rest-apis/content\#waitforevent "Direct link to waitForEvent")

Waits for an event to happen on the page before cotinue

#### Example [​](https://docs.browserless.io/rest-apis/content\#example "Direct link to Example")

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
  -H 'Content-Type: application/json' \
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
const url = `https://production-sfo.browserless.io/content?token=${TOKEN}`;
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

const fetchContent = async () => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });

    const content = await response.text();
    console.log(content);
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
    "waitForEvent": {
      "event": "fullscreenchange",
      "timeout": 5000
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import com.google.gson.*;

public class FetchContentWithEvent {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN;

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = new Gson().toJson(Map.of(
            "url", "https://example.com/",
            "waitForEvent", Map.of(
                "event", "fullscreenchange",
                "timeout", 5000
            )
        ));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("Cache-Control", "no-cache")
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
using System.Text;
	using System.Text.Json;

	class Program
	{
			static async Task Main(string[] args)
			{
					string TOKEN = "YOUR_API_TOKEN_HERE";
					string url = $"https://production-sfo.browserless.io/content?token={TOKEN}";

					var payload = new
					{
							url = "https://example.com/",
							waitForEvent = new
							{
									@event = "fullscreenchange",
									timeout = 5000
							}
					};

					var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

					using var httpClient = new HttpClient();
					try
					{
							var request = new HttpRequestMessage(HttpMethod.Post, url)
							{
									Content = jsonContent
							};

							request.Headers.Add("Cache-Control", "no-cache");

							var response = await httpClient.SendAsync(request);
							response.EnsureSuccessStatusCode();
							var result = await response.Content.ReadAsStringAsync();
							Console.WriteLine("Response: " + result);
					}
					catch (Exception e)
					{
							Console.WriteLine("Error: " + e.Message);
					}
			}
	}

```

### waitForFunction [​](https://docs.browserless.io/rest-apis/content\#waitforfunction "Direct link to waitForFunction")

Waits for the provided function to return before cotinue. The function can be any valid JavaScript or EcmaScript function, and `async` functions are supported.

#### Example [​](https://docs.browserless.io/rest-apis/content\#example-1 "Direct link to Example")

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
  "waitForFunction": {
    "fn": "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
    "timeout": 5000
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
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
const url = `https://production-sfo.browserless.io/content?token=${TOKEN}`;
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

const fetchContent = async () => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });

    const content = await response.text();
    console.log(content);
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
    "waitForFunction": {
        "fn": "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
        "timeout": 5000
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import com.google.gson.*;

public class FetchContentWithFunction {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN;

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = new Gson().toJson(Map.of(
            "url", "https://example.com/",
            "waitForFunction", Map.of(
                "fn", "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
                "timeout", 5000
            )
        ));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("Cache-Control", "no-cache")
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
using System.Text;
	using System.Text.Json;

	class Program
	{
			static async Task Main(string[] args)
			{
					string TOKEN = "YOUR_API_TOKEN_HERE";
					string url = $"https://production-sfo.browserless.io/content?token={TOKEN}";

					var payload = new
					{
							url = "https://example.com/",
							waitForFunction = new
							{
									fn = "async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}",
									timeout = 5000
							}
					};

					var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

					using var httpClient = new HttpClient();
					try
					{
							var request = new HttpRequestMessage(HttpMethod.Post, url)
							{
									Content = jsonContent
							};

							request.Headers.Add("Cache-Control", "no-cache");

							var response = await httpClient.SendAsync(request);
							response.EnsureSuccessStatusCode();
							var result = await response.Content.ReadAsStringAsync();
							Console.WriteLine("Response: " + result);
					}
					catch (Exception e)
					{
							Console.WriteLine("Error: " + e.Message);
					}
			}
	}

```

### waitForSelector [​](https://docs.browserless.io/rest-apis/content\#waitforselector "Direct link to waitForSelector")

Wait for a selector to appear in page. If at the moment of calling the method the selector already exists, the method will return immediately. If the selector doesn't appear after the timeout milliseconds of waiting, the function will throw.

The object can have any of these values:

- `selector`: String, required — A valid CSS selector.
- `hidden` Boolean, optional — Wait for the selected element to not be found in the DOM or to be hidden, i.e. have `display: none` or `visibility: hidden` CSS properties.
- `timeout`: Number, optional — Maximum number of milliseconds to wait for the selector before failing.
- `visible`: Boolean, optional — Wait for the selected element to be present in DOM and to be visible, i.e. to not have `display: none` or `visibility: hidden` CSS properties.

#### Example [​](https://docs.browserless.io/rest-apis/content\#example-2 "Direct link to Example")

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
  -H 'Content-Type: application/json' \
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
const url = `https://production-sfo.browserless.io/content?token=${TOKEN}`;
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

const fetchContent = async () => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });

    const content = await response.text();
    console.log(content);
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
    "waitForEvent": {
        "event": "fullscreenchange",
        "timeout": 5000
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import com.google.gson.*;

public class FetchContentWithWaitForEvent {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN;

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = new Gson().toJson(Map.of(
            "url", "https://example.com/",
            "waitForEvent", Map.of(
                "event", "fullscreenchange",
                "timeout", 5000
            )
        ));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("Cache-Control", "no-cache")
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
using System.Text;
	using System.Text.Json;

	class Program
	{
			static async Task Main(string[] args)
			{
					string TOKEN = "YOUR_API_TOKEN_HERE";
					string url = $"https://production-sfo.browserless.io/content?token={TOKEN}";

					var payload = new
					{
							url = "https://example.com/",
							waitForEvent = new
							{
									@event = "fullscreenchange",
									timeout = 5000
							}
					};

					var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

					using var httpClient = new HttpClient();
					try
					{
							var request = new HttpRequestMessage(HttpMethod.Post, url)
							{
									Content = jsonContent
							};

							request.Headers.Add("Cache-Control", "no-cache");

							var response = await httpClient.SendAsync(request);
							response.EnsureSuccessStatusCode();
							var result = await response.Content.ReadAsStringAsync();
							Console.WriteLine("Response: " + result);
					}
					catch (Exception e)
					{
							Console.WriteLine("Error: " + e.Message);
					}
			}
	}

```

### waitForTimeout [​](https://docs.browserless.io/rest-apis/content\#waitfortimeout "Direct link to waitForTimeout")

Waits for a specified timeout before continuing.

#### Example [​](https://docs.browserless.io/rest-apis/content\#example-3 "Direct link to Example")

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "waitForTimeout": 10000
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "waitForTimeout": 10000
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
    waitForTimeout: 10000
};

const fetchContent = async () => {
    const response = await fetch(url, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });

    const content = await response.text();
    console.log(content);
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
    "waitForTimeout": 10000
}

response = requests.post(url, headers=headers, json=data)
print(response.text)

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import com.google.gson.*;

public class FetchContentWithWaitForTimeout {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/content?token=" + TOKEN;

        HttpClient client = HttpClient.newHttpClient();

        String jsonData = new Gson().toJson(Map.of(
            "url", "https://example.com/",
            "waitForTimeout", 10000
        ));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .header("Cache-Control", "no-cache")
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
using System.Text;
	using System.Text.Json;

	class Program
	{
			static async Task Main(string[] args)
			{
					string TOKEN = "YOUR_API_TOKEN_HERE";
					string url = $"https://production-sfo.browserless.io/content?token={TOKEN}";

					var payload = new
					{
							url = "https://example.com/",
							waitForTimeout = 10000
					};

					var jsonContent = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json");

					using var httpClient = new HttpClient();
					try
					{
							var request = new HttpRequestMessage(HttpMethod.Post, url)
							{
									Content = jsonContent
							};

							request.Headers.Add("Cache-Control", "no-cache");

							var response = await httpClient.SendAsync(request);
							response.EnsureSuccessStatusCode();
							var result = await response.Content.ReadAsStringAsync();
							Console.WriteLine("Response: " + result);
					}
					catch (Exception e)
					{
							Console.WriteLine("Error: " + e.Message);
					}
			}
	}

```

- [Basic Usage](https://docs.browserless.io/rest-apis/content#basic-usage)
- [Rejecting Undesired Requests](https://docs.browserless.io/rest-apis/content#rejecting-undesired-requests)
- [Navigation Options](https://docs.browserless.io/rest-apis/content#navigation-options)
- [Continue on error](https://docs.browserless.io/rest-apis/content#continue-on-error)
- [Waiting for Things](https://docs.browserless.io/rest-apis/content#waiting-for-things)
  - [waitForEvent](https://docs.browserless.io/rest-apis/content#waitforevent)
  - [waitForFunction](https://docs.browserless.io/rest-apis/content#waitforfunction)
  - [waitForSelector](https://docs.browserless.io/rest-apis/content#waitforselector)
  - [waitForTimeout](https://docs.browserless.io/rest-apis/content#waitfortimeout)