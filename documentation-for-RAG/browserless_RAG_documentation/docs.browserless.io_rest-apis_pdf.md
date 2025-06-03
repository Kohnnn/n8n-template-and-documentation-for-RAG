---
url: "https://docs.browserless.io/rest-apis/pdf"
title: "/pdf API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/pdf#__docusaurus_skipToContent_fallback)

On this page

The `/pdf` API allows for simple navigation to a site and capturing a PDF. Browserless will respond with a `Content-Type` of `application/pdf` and a Buffer of the PDF file. Similar to screenshots, this REST API also exposes puppeteer's `pdf` options via an `options` property in the JSON body for granular control.

You can [view the complete PDF API OpenAPI specification](https://docs.browserless.io/open-api#tag/Browser-REST-APIs/paths/~1chrome~1pdf/post) for all options and properties.

info

This route requires either a `url` or `html` property in the JSON body. When `html` is present Browserless will render the HTML for you and capture the PDF

## Basic Usage [​](https://docs.browserless.io/rest-apis/pdf\#basic-usage "Direct link to Basic Usage")

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
// JSON body
// `options` are the options available via puppeteer's Page.pdf() method
// (see our Open API documentation)
{
  "url": "https://example.com/",
  "options": {
    "displayHeaderFooter": true,
    "printBackground": false,
    "format": "A0"
    // Queue the lack of a `path` parameter
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "options": {
    "displayHeaderFooter": true,
    "printBackground": false,
    "format": "A0"
  }
}'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  options: {
    displayHeaderFooter: true,
    printBackground: false,
    format: "A0"
  }
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
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "options": {
        "displayHeaderFooter": True,
        "printBackground": False,
        "format": "A0"
    }
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
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "options": {
                "displayHeaderFooter": true,
                "printBackground": false,
                "format": "A0"
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
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
              ""options"": {
                  ""displayHeaderFooter"": true,
                  ""printBackground"": false,
                  ""format"": ""A0""
              }
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

warning

We do not allow setting a `options.path`

## Setting HTML content [​](https://docs.browserless.io/rest-apis/pdf\#setting-html-content "Direct link to Setting HTML content")

You can set the HTML content of the page to render dynamically generated content as well.

danger

**When this propriety is set, the `url` propriety must not be present.**

Here’s the request in the specified format, with examples for `curl`, JavaScript, and Python.

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
// JSON body
// `options` are the options available via puppeteer's Page.pdf() method
// (see our Open API documentation)
{
  "html": "<h1>Hello World!</h1>",
  "options": {
    "displayHeaderFooter": true,
    "printBackground": false,
    "format": "A0"
    // Queue the lack of a `path` parameter
  }
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "html": "<h1>Hello World!</h1>",
  "options": {
    "displayHeaderFooter": true,
    "printBackground": false,
    "format": "A0"
  }
}'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  html: "<h1>Hello World!</h1>",
  options: {
    displayHeaderFooter: true,
    printBackground: false,
    format: "A0"
  }
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
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "html": "<h1>Hello World!</h1>",
    "options": {
        "displayHeaderFooter": True,
        "printBackground": False,
        "format": "A0"
    }
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

public class GeneratePDFWithHTML {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN;

        String jsonData = """
        {
            "html": "<h1>Hello World!</h1>",
            "options": {
                "displayHeaderFooter": true,
                "printBackground": false,
                "format": "A0"
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
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}";

        string jsonData = @"
          {
              ""html"": ""<h1>Hello World!</h1>"",
              ""options"": {
                  ""displayHeaderFooter"": true,
                  ""printBackground"": false,
                  ""format"": ""A0""
              }
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

warning

We do not allow to set a `options.path`

## Adding custom styles and scripts [​](https://docs.browserless.io/rest-apis/pdf\#adding-custom-styles-and-scripts "Direct link to Adding custom styles and scripts")

Browserless offers ways to load additional stylesheets and script tags to the page as well. This give you full control and allows you to override page elements to suite your needs.

- JSON payload
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "addScriptTag": [\
    { "url": "https://code.jquery.com/jquery-3.7.1.min.js" },\
    { "content": "document.querySelector(`h1`).innerText = `Hello Word!`" }\
  ],
  "addStyleTag": [\
    {\
      "content": "body { height: 100vh;  background: linear-gradient(45deg, #da5a44, #a32784);}"\
    },\
    {\
      "url": "https://interactive-examples.mdn.mozilla.net/live-examples/css-examples/text-decoration/text-decoration-color.css"\
    }\
  ]
}

```

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "addScriptTag": [\
    { "url": "https://code.jquery.com/jquery-3.7.1.min.js" },\
    { "content": "document.querySelector(`h1`).innerText = `Hello World!`" }\
  ],
  "addStyleTag": [\
    {\
      "content": "body { height: 100vh; background: linear-gradient(45deg, #da5a44, #a32784); }"\
    },\
    {\
      "url": "https://interactive-examples.mdn.mozilla.net/live-examples/css-examples/text-decoration/text-decoration-color.css"\
    }\
  ]
}'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  addScriptTag: [\
    { url: "https://code.jquery.com/jquery-3.7.1.min.js" },\
    { content: "document.querySelector(`h1`).innerText = `Hello World!`" }\
  ],
  addStyleTag: [\
    {\
      content: "body { height: 100vh; background: linear-gradient(45deg, #da5a44, #a32784); }"\
    },\
    {\
      url: "https://interactive-examples.mdn.mozilla.net/live-examples/css-examples/text-decoration/text-decoration-color.css"\
    }\
  ]
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
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "addScriptTag": [\
        { "url": "https://code.jquery.com/jquery-3.7.1.min.js" },\
        { "content": "document.querySelector(`h1`).innerText = `Hello World!`" }\
    ],
    "addStyleTag": [\
        {\
            "content": "body { height: 100vh; background: linear-gradient(45deg, #da5a44, #a32784); }"\
        },\
        {\
            "url": "https://interactive-examples.mdn.mozilla.net/live-examples/css-examples/text-decoration/text-decoration-color.css"\
        }\
    ]
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

public class GeneratePDFWithScriptAndStyle {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "addScriptTag": [\
                { "url": "https://code.jquery.com/jquery-3.7.1.min.js" },\
                { "content": "document.querySelector(`h1`).innerText = `Hello World!`" }\
            ],
            "addStyleTag": [\
                {\
                    "content": "body { height: 100vh; background: linear-gradient(45deg, #da5a44, #a32784); }"\
                },\
                {\
                    "url": "https://interactive-examples.mdn.mozilla.net/live-examples/css-examples/text-decoration/text-decoration-color.css"\
                }\
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
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
              ""addScriptTag"": [\
                  { ""url"": ""https://code.jquery.com/jquery-3.7.1.min.js"" },\
                  { ""content"": ""document.querySelector(`h1`).innerText = `Hello World!`"" }\
              ],
              ""addStyleTag"": [\
                  {\
                      ""content"": ""body { height: 100vh; background: linear-gradient(45deg, #da5a44, #a32784); }""\
                  },\
                  {\
                      ""url"": ""https://interactive-examples.mdn.mozilla.net/live-examples/css-examples/text-decoration/text-decoration-color.css""\
                  }\
              ]
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

## Rejecting Undesired Requests [​](https://docs.browserless.io/rest-apis/pdf\#rejecting-undesired-requests "Direct link to Rejecting Undesired Requests")

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
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type': 'application/json' \
  -d '{
  "url": "https://browserless.io/",
  "rejectResourceTypes": ["image"],
  "rejectRequestPattern": ["/^.*\\.(css)"]
}'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://browserless.io/",
  rejectResourceTypes: ["image"],
  rejectRequestPattern: ["^.*\\.(css)"]
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
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://browserless.io/",
    "rejectResourceTypes": ["image"],
    "rejectRequestPattern": ["^.*\\.(css)"]
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

public class GeneratePDFWithRejections {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://browserless.io/",
            "rejectResourceTypes": ["image"],
            "rejectRequestPattern": ["^.*\\\\.(css)"]
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
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}";

        string jsonData = @"
          {
              ""url"": ""https://browserless.io/"",
              ""rejectResourceTypes"": [""image""],
              ""rejectRequestPattern"": [""^.*\\\\.(css)""]
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

## Navigation Options [​](https://docs.browserless.io/rest-apis/pdf\#navigation-options "Direct link to Navigation Options")

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
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "gotoOptions": { "waitUntil": "networkidle2" }
}'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  gotoOptions: { waitUntil: "networkidle2" }
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
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}"
headers = {
    "Cache-Control": "no-cache",
    "Content-Type": "application/json"
}

data = {
    "url": "https://example.com/",
    "gotoOptions": { "waitUntil": "networkidle2" }
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

public class GeneratePDFWithGotoOptions {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "gotoOptions": { "waitUntil": "networkidle2" }
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
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
              ""gotoOptions"": { ""waitUntil"": ""networkidle2"" }
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

## Continue on Error [​](https://docs.browserless.io/rest-apis/pdf\#continue-on-error "Direct link to Continue on Error")

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
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "bestAttempt": true,
  "waitForSelector": { "selector": "table", "timeout": 500 }
}'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}`;
const headers = {
  "Cache-Control": "no-cache",
  "Content-Type": "application/json"
};

const data = {
  url: "https://example.com/",
  bestAttempt: true,
  waitForSelector: { selector: "table", timeout: 500 }
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
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}"
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

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDFWithBestAttempt {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "bestAttempt": true,
            "waitForSelector": { "selector": "table", "timeout": 500 }
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
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
              ""bestAttempt"": true,
              ""waitForSelector"": { ""selector"": ""table"", ""timeout"": 500 }
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

## Waiting for Things [​](https://docs.browserless.io/rest-apis/pdf\#waiting-for-things "Direct link to Waiting for Things")

Browserless offers 4 different ways to wait for preconditions to be met on the page before returning the response. These are `events`, `functions`, `selectors` and `timeouts`.

### waitForEvent [​](https://docs.browserless.io/rest-apis/pdf\#waitforevent "Direct link to waitForEvent")

Waits for an event to happen on the page before continuing:

#### Example [​](https://docs.browserless.io/rest-apis/pdf\#example "Direct link to Example")

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
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE \
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
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}`;
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
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}"
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

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDFWithWaitForEvent {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN;

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
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
              ""waitForEvent"": {
                  ""event"": ""fullscreenchange"",
                  ""timeout"": 5000
              }
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

### waitForFunction [​](https://docs.browserless.io/rest-apis/pdf\#waitforfunction "Direct link to waitForFunction")

Waits for the provided function to return before continuing. The function can be any valid JavaScript or EcmaScript function, and `async` functions are supported.

#### Example [​](https://docs.browserless.io/rest-apis/pdf\#example-1 "Direct link to Example")

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
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE \
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
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}`;
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
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}"
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

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDFWithWaitForFunction {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN;

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
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
              ""waitForFunction"": {
                  ""fn"": ""async()=>{let t=await fetch('https://jsonplaceholder.typicode.com/todos/1'),e=await t.json();document.querySelector('h1').innerText=e.title}"",
                  ""timeout"": 5000
              }
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

### waitForSelector [​](https://docs.browserless.io/rest-apis/pdf\#waitforselector "Direct link to waitForSelector")

Wait for a selector to appear in page. If at the moment of calling the method the selector already exists, the method will return immediately. If the selector doesn't appear after the timeout milliseconds of waiting, the function will throw.

The object can have any of these values:

- `selector`: String, required — A valid CSS selector.
- `hidden` Boolean, optional — Wait for the selected element to not be found in the DOM or to be hidden, i.e. have `display: none` or `visibility: hidden` CSS properties.
- `timeout`: Number, optional — Maximum number of milliseconds to wait for the selector before failing.
- `visible`: Boolean, optional — Wait for the selected element to be present in DOM and to be visible, i.e. to not have `display: none` or `visibility: hidden` CSS properties.

#### Example [​](https://docs.browserless.io/rest-apis/pdf\#example-2 "Direct link to Example")

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
  https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN_HERE \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "waitForSelector": {
    "selector": "h1",
    "timeout": 5000
  }
}'

```

```codeBlockLines_p187
import fs from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/pdf?token=${TOKEN}`;
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
url = f"https://production-sfo.browserless.io/pdf?token={TOKEN}"
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

with open("output.pdf", "wb") as file:
    file.write(response.content)

print("PDF saved as output.pdf")

```

```codeBlockLines_p187
import java.io.*;
import java.net.URI;
import java.net.http.*;
import java.nio.file.*;

public class GeneratePDFWithWaitForSelector {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/pdf?token=" + TOKEN;

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
        string url = $"https://production-sfo.browserless.io/pdf?token={TOKEN}";

        string jsonData = @"
          {
              ""url"": ""https://example.com/"",
              ""waitForSelector"": {
                  ""selector"": ""h1"",
                  ""timeout"": 5000
              }
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

- [Basic Usage](https://docs.browserless.io/rest-apis/pdf#basic-usage)
- [Setting HTML content](https://docs.browserless.io/rest-apis/pdf#setting-html-content)
- [Adding custom styles and scripts](https://docs.browserless.io/rest-apis/pdf#adding-custom-styles-and-scripts)
- [Rejecting Undesired Requests](https://docs.browserless.io/rest-apis/pdf#rejecting-undesired-requests)
- [Navigation Options](https://docs.browserless.io/rest-apis/pdf#navigation-options)
- [Continue on Error](https://docs.browserless.io/rest-apis/pdf#continue-on-error)
- [Waiting for Things](https://docs.browserless.io/rest-apis/pdf#waiting-for-things)
  - [waitForEvent](https://docs.browserless.io/rest-apis/pdf#waitforevent)
  - [waitForFunction](https://docs.browserless.io/rest-apis/pdf#waitforfunction)
  - [waitForSelector](https://docs.browserless.io/rest-apis/pdf#waitforselector)