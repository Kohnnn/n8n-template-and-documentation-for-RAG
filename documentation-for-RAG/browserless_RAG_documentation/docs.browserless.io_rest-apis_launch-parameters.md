---
url: "https://docs.browserless.io/rest-apis/launch-parameters"
title: "Launch Parameters and Options | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/launch-parameters#__docusaurus_skipToContent_fallback)

On this page

Browserless allows extensive configuration of how browsers are launched and behave during
your sessions. These launch parameters can be provided either via query parameters in the
URL or through a special JSON launch payload. Whether you're using BQL, BaaS v2, or REST, these
options let you tweak the browser environment to fit your needs.

## Passing Launch Options [​](https://docs.browserless.io/rest-apis/launch-parameters\#passing-launch-options "Direct link to Passing Launch Options")

Two ways to specify launch options:

1. **Individual Query Parameters**: Add options directly to URLs (e.g., `&headless=false`, `&proxy=residential`). Best for simple boolean options.

2. **Combined `launch` Parameter (JSON)**: For complex configurations, use a single query param `launch` with a JSON string as its value. This JSON can include any Chrome flags or Browserless-specific settings in a structured way. It's essentially the equivalent of Puppeteer's `launch({ options })` but provided to the cloud service:







```codeBlockLines_p187
&launch={"headless":false,"stealth":true,"args":["--window-size=1920,1080"]}

```











(URL-encoded) would configure a headful, stealth-enabled browser with a specific window size.


Browserless merges both methods if used together, with individual parameters taking precedence. Use query params for simple toggles and the launch parameter for multiple settings.

## Launch Options (Query Parameters) [​](https://docs.browserless.io/rest-apis/launch-parameters\#launch-options-query-parameters "Direct link to Launch Options (Query Parameters)")

Below is a list of available launch options you can use in query strings for Browserless REST APIs.

| Parameter | Description | Default |
| --- | --- | --- |
| headless | Runs the browser in headless mode. Set to false to enable headful mode (with a GUI). While the GUI isn't visible in cloud environments, headful mode may help bypass bot detection. Note: it uses more resources. | `true` |
| stealth | Enables stealth mode to reduce automation signals (similar to puppeteer-extra’s stealth plugin). In BQL, stealth is always on by design and controlled via the humanlike option. In BaaS/REST, set to true to enable stealth techniques. | - `false` (for BaaS/REST)<br>- `true` (for BQL) |
| blockAds | Enables the built-in ad blocker (powered by uBlock Origin). Helps speed up scripts and reduce noise by blocking ads and trackers. Especially useful for scraping to avoid popups and clutter. | `false` |
| blockConsentModals | Automatically blocks or dismisses cookie/GDPR consent banners. Available in BQL sessions and the /screenshot and /pdf REST APIs. In BQL, toggle it via the IDE or launch JSON. Useful for cleaner scraping by removing overlays. | `false` |
| proxy | Routes browser traffic through a proxy. Options: proxy=residential for Browserless’s residential proxy pool; proxy=\`<your proxy URL>\` for your own proxy. Omit to use a direct connection. | none |
| proxyCountry | Used with proxy=residential to specify the exit node’s country. Accepts ISO 3166 country codes (e.g., us, gb, de). If omitted, a random location is chosen. | none |
| proxySticky | Used with proxy=residential to maintain the same proxy IP across a session (when possible). Useful for sites that expect consistent IP usage. | `false` |
| timeout | Maximum session duration in milliseconds. The session will automatically close after this time to prevent overuse. | 60000 |

info

The examples below use the `/pdf` API, but it can be applied to all APIs.

### Headless [​](https://docs.browserless.io/rest-apis/launch-parameters\#headless "Direct link to Headless")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
  curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE&headless=true \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/"
  }'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}&headless=true`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
};

const generatePDF = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const pdfBuffer = await response.arrayBuffer();
  await fs.writeFile("output.pdf", Buffer.from(pdfBuffer));
  console.log("PDF saved as output.pdf");
};

generatePDF();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}&headless=true"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
}

response = requests.post(url, headers=headers, json=data)

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDF {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN + "&headless=true";

        String jsonData = """
        {
            "url": "https://example.com/",
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
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            Files.copy(response.body(), Paths.get("output.pdf"), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("PDF saved as output.pdf");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}&headless=true";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
          }";

        using var client = new HttpClient();

        var request = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new StringContent(jsonData, Encoding.UTF8, "application/json")
        };

        request.Headers.Add("Cache-Control", "no-cache");

        try
        {
            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();
            var pdfBytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync("output.pdf", pdfBytes);
            Console.WriteLine("PDF saved as output.pdf");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

### Stealth [​](https://docs.browserless.io/rest-apis/launch-parameters\#stealth "Direct link to Stealth")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
  curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE&stealth=true \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/"
  }'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}&stealth=true`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
};

const generatePDF = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const pdfBuffer = await response.arrayBuffer();
  await fs.writeFile("output.pdf", Buffer.from(pdfBuffer));
  console.log("PDF saved as output.pdf");
};

generatePDF();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}&stealth=true"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
}

response = requests.post(url, headers=headers, json=data)

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDF {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN + "&stealth=true";

        String jsonData = """
        {
            "url": "https://example.com/",
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
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            Files.copy(response.body(), Paths.get("output.pdf"), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("PDF saved as output.pdf");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}&stealth=true";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
          }";

        using var client = new HttpClient();

        var request = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new StringContent(jsonData, Encoding.UTF8, "application/json")
        };

        request.Headers.Add("Cache-Control", "no-cache");

        try
        {
            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();
            var pdfBytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync("output.pdf", pdfBytes);
            Console.WriteLine("PDF saved as output.pdf");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

### Blocking Ads [​](https://docs.browserless.io/rest-apis/launch-parameters\#blocking-ads "Direct link to Blocking Ads")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
  curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE&blockAds=true \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/"
  }'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}&blockAds=true`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
};

const generatePDF = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const pdfBuffer = await response.arrayBuffer();
  await fs.writeFile("output.pdf", Buffer.from(pdfBuffer));
  console.log("PDF saved as output.pdf");
};

generatePDF();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}&blockAds=true"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
}

response = requests.post(url, headers=headers, json=data)

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDF {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN + "&blockAds=true";

        String jsonData = """
        {
            "url": "https://example.com/",
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
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            Files.copy(response.body(), Paths.get("output.pdf"), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("PDF saved as output.pdf");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}&blockAds=true";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
          }";

        using var client = new HttpClient();

        var request = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new StringContent(jsonData, Encoding.UTF8, "application/json")
        };

        request.Headers.Add("Cache-Control", "no-cache");

        try
        {
            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();
            var pdfBytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync("output.pdf", pdfBytes);
            Console.WriteLine("PDF saved as output.pdf");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

Under the hood, Browserless uses UBlock Origin to block ads and filter content.

### Block Consent Modals [​](https://docs.browserless.io/rest-apis/launch-parameters\#block-consent-modals "Direct link to Block Consent Modals")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
  curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE&blockConsentModals=true \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/"
  }'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}&blockConsentModals=true`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
};

const generatePDF = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const pdfBuffer = await response.arrayBuffer();
  await fs.writeFile("output.pdf", Buffer.from(pdfBuffer));
  console.log("PDF saved as output.pdf");
};

generatePDF();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}&blockConsentModals=true"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
}

response = requests.post(url, headers=headers, json=data)

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDF {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN + "&blockConsentModals=true";

        String jsonData = """
        {
            "url": "https://example.com/",
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
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            Files.copy(response.body(), Paths.get("output.pdf"), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("PDF saved as output.pdf");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}&blockConsentModals=true";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
          }";

        using var client = new HttpClient();

        var request = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new StringContent(jsonData, Encoding.UTF8, "application/json")
        };

        request.Headers.Add("Cache-Control", "no-cache");

        try
        {
            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();
            var pdfBytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync("output.pdf", pdfBytes);
            Console.WriteLine("PDF saved as output.pdf");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

### Proxy [​](https://docs.browserless.io/rest-apis/launch-parameters\#proxy "Direct link to Proxy")

Using `http://user:pass@host:port` as an example proxy URL:

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
  curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE&proxy=http://user:pass@host:port \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/"
  }'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}&proxy=http://user:pass@host:port`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
};

const generatePDF = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const pdfBuffer = await response.arrayBuffer();
  await fs.writeFile("output.pdf", Buffer.from(pdfBuffer));
  console.log("PDF saved as output.pdf");
};

generatePDF();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}&proxy=http://user:pass@host:port"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
}

response = requests.post(url, headers=headers, json=data)

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDF {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN + "&proxy=http://user:pass@host:port";

        String jsonData = """
        {
            "url": "https://example.com/",
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
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            Files.copy(response.body(), Paths.get("output.pdf"), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("PDF saved as output.pdf");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}&proxy=http://user:pass@host:port";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
          }";

        using var client = new HttpClient();

        var request = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new StringContent(jsonData, Encoding.UTF8, "application/json")
        };

        request.Headers.Add("Cache-Control", "no-cache");

        try
        {
            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();
            var pdfBytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync("output.pdf", pdfBytes);
            Console.WriteLine("PDF saved as output.pdf");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

### Proxy Country [​](https://docs.browserless.io/rest-apis/launch-parameters\#proxy-country "Direct link to Proxy Country")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
  curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/"
  }'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}&proxy=residential&proxyCountry=us`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
};

const generatePDF = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const pdfBuffer = await response.arrayBuffer();
  await fs.writeFile("output.pdf", Buffer.from(pdfBuffer));
  console.log("PDF saved as output.pdf");
};

generatePDF();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}&proxy=residential&proxyCountry=us"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
}

response = requests.post(url, headers=headers, json=data)

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDF {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN + "&proxy=residential&proxyCountry=us";

        String jsonData = """
        {
            "url": "https://example.com/",
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
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            Files.copy(response.body(), Paths.get("output.pdf"), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("PDF saved as output.pdf");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}&proxy=residential&proxyCountry=us";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
          }";

        using var client = new HttpClient();

        var request = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new StringContent(jsonData, Encoding.UTF8, "application/json")
        };

        request.Headers.Add("Cache-Control", "no-cache");

        try
        {
            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();
            var pdfBytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync("output.pdf", pdfBytes);
            Console.WriteLine("PDF saved as output.pdf");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

### Proxy Sticky [​](https://docs.browserless.io/rest-apis/launch-parameters\#proxy-sticky "Direct link to Proxy Sticky")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
  curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE&proxy=residential&proxySticky=true \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/"
  }'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}&proxy=residential&proxySticky=true`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
};

const generatePDF = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const pdfBuffer = await response.arrayBuffer();
  await fs.writeFile("output.pdf", Buffer.from(pdfBuffer));
  console.log("PDF saved as output.pdf");
};

generatePDF();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}&proxy=residential&proxySticky=true"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
}

response = requests.post(url, headers=headers, json=data)

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDF {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN + "&proxy=residential&proxySticky=true";

        String jsonData = """
        {
            "url": "https://example.com/",
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
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            Files.copy(response.body(), Paths.get("output.pdf"), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("PDF saved as output.pdf");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}&proxy=residential&proxySticky=true";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
          }";

        using var client = new HttpClient();

        var request = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new StringContent(jsonData, Encoding.UTF8, "application/json")
        };

        request.Headers.Add("Cache-Control", "no-cache");

        try
        {
            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();
            var pdfBytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync("output.pdf", pdfBytes);
            Console.WriteLine("PDF saved as output.pdf");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

### Timeout [​](https://docs.browserless.io/rest-apis/launch-parameters\#timeout "Direct link to Timeout")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
  curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE&timeout=25000 \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/"
  }'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}&timeout=25000`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
};

const generatePDF = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const pdfBuffer = await response.arrayBuffer();
  await fs.writeFile("output.pdf", Buffer.from(pdfBuffer));
  console.log("PDF saved as output.pdf");
};

generatePDF();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}&timeout=25000"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
}

response = requests.post(url, headers=headers, json=data)

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDF {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN + "&timeout=25000";

        String jsonData = """
        {
            "url": "https://example.com/",
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
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());
            Files.copy(response.body(), Paths.get("output.pdf"), StandardCopyOption.REPLACE_EXISTING);
            System.out.println("PDF saved as output.pdf");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}&timeout=25000";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
          }";

        using var client = new HttpClient();

        var request = new HttpRequestMessage(HttpMethod.Post, url)
        {
            Content = new StringContent(jsonData, Encoding.UTF8, "application/json")
        };

        request.Headers.Add("Cache-Control", "no-cache");

        try
        {
            var response = await client.SendAsync(request);
            response.EnsureSuccessStatusCode();
            var pdfBytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync("output.pdf", pdfBytes);
            Console.WriteLine("PDF saved as output.pdf");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}

```

- [Passing Launch Options](https://docs.browserless.io/rest-apis/launch-parameters#passing-launch-options)
- [Launch Options (Query Parameters)](https://docs.browserless.io/rest-apis/launch-parameters#launch-options-query-parameters)
  - [Headless](https://docs.browserless.io/rest-apis/launch-parameters#headless)
  - [Stealth](https://docs.browserless.io/rest-apis/launch-parameters#stealth)
  - [Blocking Ads](https://docs.browserless.io/rest-apis/launch-parameters#blocking-ads)
  - [Block Consent Modals](https://docs.browserless.io/rest-apis/launch-parameters#block-consent-modals)
  - [Proxy](https://docs.browserless.io/rest-apis/launch-parameters#proxy)
  - [Proxy Country](https://docs.browserless.io/rest-apis/launch-parameters#proxy-country)
  - [Proxy Sticky](https://docs.browserless.io/rest-apis/launch-parameters#proxy-sticky)
  - [Timeout](https://docs.browserless.io/rest-apis/launch-parameters#timeout)