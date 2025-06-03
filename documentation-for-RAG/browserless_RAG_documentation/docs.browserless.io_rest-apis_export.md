---
url: "https://docs.browserless.io/rest-apis/export"
title: "/export API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/export#__docusaurus_skipToContent_fallback)

On this page

The export API allows you to retrieve the content of any URL in its native format (HTML, PDF, images, etc.). The response format is determined by the content type of the page being accessed, with appropriate headers set to facilitate downloading or viewing the content.

You can [check the full Open API schema here](https://docs.browserless.io/open-api#tag/Browser-REST-APIs/paths/~1chrome~1export/post).

## Basic Usage [​](https://docs.browserless.io/rest-apis/export\#basic-usage "Direct link to Basic Usage")

The export API accepts a JSON payload with the target URL and configuration options.

### JSON Payload Format [​](https://docs.browserless.io/rest-apis/export\#json-payload-format "Direct link to JSON Payload Format")

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "headers": {
    "User-Agent": "Custom User Agent"
  },
  "gotoOptions": {
    "waitUntil": "networkidle0",
    "timeout": 30000
  },
  "waitForSelector": {
    "selector": "#main-content",
    "timeout": 5000
  },
  "waitForTimeout": 1000,
  "bestAttempt": false
}

```

## Parameters [​](https://docs.browserless.io/rest-apis/export\#parameters "Direct link to Parameters")

### Required Parameters [​](https://docs.browserless.io/rest-apis/export\#required-parameters "Direct link to Required Parameters")

- `url` (string) - The URL of the resource to export

### Optional Parameters [​](https://docs.browserless.io/rest-apis/export\#optional-parameters "Direct link to Optional Parameters")

- `headers` (object) - Custom HTTP headers to send with the request
- `gotoOptions` (object) - Navigation options

  - `waitUntil` (string) - When to consider navigation succeeded. Options: 'load', 'domcontentloaded', 'networkidle', 'commit'. Default: 'networkidle0'
  - `timeout` (number) - Maximum navigation time in milliseconds
  - `referer` (string) - Referer header value
- `waitForEvent` (object) - Wait for a specific event before proceeding
- `waitForFunction` (object) - Wait for a specific function to return true
- `waitForSelector` (object) - Wait for a specific selector to be present

  - `selector` (string) - CSS selector to wait for
  - `timeout` (number) - Maximum time to wait in milliseconds
- `waitForTimeout` (number) - Time in milliseconds to wait after page load
- `bestAttempt` (boolean) - Whether to continue on errors. Default: false
- `includeResources` (boolean) - Whether to include all linked resources (images, CSS, JavaScript) in a zip file. Default: false

## Response [​](https://docs.browserless.io/rest-apis/export\#response "Direct link to Response")

The API returns a streaming response with the content of the requested URL. The behavior depends on the content type detected and the `includeResources` parameter:

- When `includeResources` is `false` (default):
  - **HTML Content**: Returns the HTML with `Content-Type: text/html`. No attachment header is set, allowing the content to be rendered in the browser.
  - **PDF Content**: Returns a PDF buffer with `Content-Type: application/pdf` and sets a `Content-Disposition: attachment` header with an appropriate filename.
  - **Images and Other Binary Content**: Returns the binary content with the appropriate MIME type (e.g., `image/jpeg`, `image/png`) and sets a `Content-Disposition: attachment` header with an appropriate filename.
- When `includeResources` is `true`:
  - Returns a zip file containing the HTML and all linked resources (images, CSS, JavaScript) with `Content-Type: application/zip` and `Content-Disposition: attachment` header with an appropriate filename.

The streaming nature of the response means you should handle it accordingly in your code, using appropriate methods for reading streams rather than assuming all content can be processed as text.

## Handling Different Content Types [​](https://docs.browserless.io/rest-apis/export\#handling-different-content-types "Direct link to Handling Different Content Types")

The export API can return various content types depending on the URL being accessed. Here's how to properly handle the different response types:

### HTML Content [​](https://docs.browserless.io/rest-apis/export\#html-content "Direct link to HTML Content")

When accessing a standard web page, the API returns HTML content with `Content-Type: text/html`:

```codeBlockLines_p187
const response = await fetch(url, options);
if (response.headers.get('content-type')?.includes('text/html')) {
  const htmlContent = await response.text();
  // Process HTML content
}

```

### PDF Content [​](https://docs.browserless.io/rest-apis/export\#pdf-content "Direct link to PDF Content")

When accessing PDF files or when the server returns PDF content, the API returns a PDF buffer with `Content-Type: application/pdf`:

```codeBlockLines_p187
const response = await fetch(url, options);
if (response.headers.get('content-type')?.includes('application/pdf')) {
  const arrayBuffer = await response.arrayBuffer();
  const pdfBuffer = Buffer.from(arrayBuffer);
  // Save or process PDF buffer
}

```

### Binary Content (Images, etc.) [​](https://docs.browserless.io/rest-apis/export\#binary-content-images-etc "Direct link to Binary Content (Images, etc.)")

For other binary content like images, the API returns the appropriate content type and sets attachment headers:

```codeBlockLines_p187
const response = await fetch(url, options);
const contentType = response.headers.get('content-type');
if (contentType?.includes('image/') || !contentType?.includes('text/')) {
  const arrayBuffer = await response.arrayBuffer();
  const binaryBuffer = Buffer.from(arrayBuffer);
  // Save or process binary buffer
}

```

## Error Handling [​](https://docs.browserless.io/rest-apis/export\#error-handling "Direct link to Error Handling")

The API may return the following error responses:

- `400 Bad Request` \- Invalid parameters, missing URL, or no content received
- `404 Not Found` \- Page not found
- `408 Request Timeout` \- Page load timeout
- `500 Internal Server Error` \- Server-side error

## Examples [​](https://docs.browserless.io/rest-apis/export\#examples "Direct link to Examples")

### Basic Export Request [​](https://docs.browserless.io/rest-apis/export\#basic-export-request "Direct link to Basic Export Request")

This example demonstrates how to export a web page using the most basic configuration. It shows how to properly handle the streamed response by detecting the content type and saving the content with the appropriate file extension.

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/export?token=YOUR_API_TOKEN_HERE \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com/"
  }'

```

```codeBlockLines_p187
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/export?token=${TOKEN}`;
const headers = {
  'Content-Type': 'application/json'
};

const data = {
  url: "https://example.com/"
};

const exportPage = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  // Get content type to determine how to handle the response
  const contentType = response.headers.get('content-type');

  // Get filename from Content-Disposition header or create a default one based on content type
  let filename = 'downloaded-content';
  const disposition = response.headers.get('content-disposition');
  if (disposition && disposition.includes('filename=')) {
    const filenameMatch = disposition.match(/filename="(.+?)"/);
    if (filenameMatch) filename = filenameMatch[1];
  } else if (contentType) {
    // Set appropriate extension based on content type
    if (contentType.includes('text/html')) filename = 'page.html';
    else if (contentType.includes('application/pdf')) filename = 'document.pdf';
    else if (contentType.includes('image/')) {
      const ext = contentType.split('/')[1];
      filename = `image.${ext}`;
    }
  }

  // Handle response based on content type
  if (contentType && contentType.includes('text/html')) {
    // Handle HTML content as text
    const content = await response.text();
    await writeFile(filename, content);
  } else {
    // Handle binary content (PDFs, images, etc.)
    const arrayBuffer = await response.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);
    await writeFile(filename, buffer);
  }

  console.log(`Content saved as ${filename}`);
};

exportPage();

```

```codeBlockLines_p187
import requests
import re

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/export?token={TOKEN}"
headers = {
    'Content-Type': 'application/json'
}

data = {
    "url": "https://example.com/"
}

response = requests.post(url, headers=headers, json=data)

# Get content type and determine appropriate filename
content_type = response.headers.get('Content-Type', '')
disposition = response.headers.get('Content-Disposition', '')

# Try to get filename from Content-Disposition header
filename = 'downloaded-content'
if disposition and 'filename=' in disposition:
    match = re.search('filename="(.+?)"', disposition)
    if match:
        filename = match.group(1)
else:
    # Create filename based on content type
    if 'text/html' in content_type:
        filename = 'page.html'
    elif 'application/pdf' in content_type:
        filename = 'document.pdf'
    elif 'image/' in content_type:
        ext = content_type.split('/')[1]
        filename = f"image.{ext}"

# Write content to file using binary mode for all types to ensure proper handling
with open(filename, "wb") as file:
    file.write(response.content)

print(f"Content saved as {filename}")

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ExportPage {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/export?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/"
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<byte[]> response = client.send(request, HttpResponse.BodyHandlers.ofByteArray());

            // Get content type and determine appropriate filename
            String contentType = response.headers().firstValue("Content-Type").orElse("");
            String disposition = response.headers().firstValue("Content-Disposition").orElse("");

            // Try to get filename from Content-Disposition header
            String filename = "downloaded-content";
            if (disposition.contains("filename=")) {
                Pattern pattern = Pattern.compile("filename=\"(.+?)\"");
                Matcher matcher = pattern.matcher(disposition);
                if (matcher.find()) {
                    filename = matcher.group(1);
                }
            } else {
                // Create filename based on content type
                if (contentType.contains("text/html")) {
                    filename = "page.html";
                } else if (contentType.contains("application/pdf")) {
                    filename = "document.pdf";
                } else if (contentType.contains("image/")) {
                    String ext = contentType.split("/")[1];
                    filename = "image." + ext;
                }
            }

            // Write content to file
            try (FileOutputStream fileOutputStream = new FileOutputStream(filename)) {
                fileOutputStream.write(response.body());
                System.out.println("Content saved as " + filename);
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
using System.Text.RegularExpressions;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/export?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/""
        }
        ";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            // Get content type and determine appropriate filename
            var contentType = response.Content.Headers.ContentType?.MediaType ?? "";
            var disposition = response.Content.Headers.ContentDisposition?.ToString() ?? "";

            // Try to get filename from Content-Disposition header
            string filename = "downloaded-content";
            if (disposition.Contains("filename=")) {
                var match = Regex.Match(disposition, "filename=\"(.+?)\"");
                if (match.Success) {
                    filename = match.Groups[1].Value;
                }
            } else {
                // Create filename based on content type
                if (contentType.Contains("text/html")) {
                    filename = "page.html";
                } else if (contentType.Contains("application/pdf")) {
                    filename = "document.pdf";
                } else if (contentType.Contains("image/")) {
                    var ext = contentType.Split('/')[1];
                    filename = $"image.{ext}";
                }
            }

            // Handle all content types as binary for consistency
            var bytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync(filename, bytes);

            Console.WriteLine($"Content saved as {filename}");
        } catch (Exception ex) {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

### Export with Custom Navigation Options [​](https://docs.browserless.io/rest-apis/export\#export-with-custom-navigation-options "Direct link to Export with Custom Navigation Options")

This example demonstrates how to export a web page with custom navigation options, such as waiting for specific network events or DOM elements to load. These options help ensure the page is fully rendered before capturing the content.

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/export?token=YOUR_API_TOKEN_HERE \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com/",
    "gotoOptions": {
      "waitUntil": "networkidle0",
      "timeout": 60000
    },
    "waitForSelector": {
      "selector": "#main-content",
      "timeout": 5000
    }
  }'

```

```codeBlockLines_p187
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/export?token=${TOKEN}`;
const headers = {
  'Content-Type': 'application/json'
};

const data = {
  url: "https://example.com/",
  gotoOptions: {
    waitUntil: "networkidle0",
    timeout: 60000
  },
  waitForSelector: {
    selector: "#main-content",
    timeout: 5000
  }
};

const exportPage = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  // Get content type to determine how to handle the response
  const contentType = response.headers.get('content-type');

  // Get filename from Content-Disposition header or create a default one based on content type
  let filename = 'downloaded-content';
  const disposition = response.headers.get('content-disposition');
  if (disposition && disposition.includes('filename=')) {
    const filenameMatch = disposition.match(/filename="(.+?)"/);
    if (filenameMatch) filename = filenameMatch[1];
  } else if (contentType) {
    // Set appropriate extension based on content type
    if (contentType.includes('text/html')) filename = 'page.html';
    else if (contentType.includes('application/pdf')) filename = 'document.pdf';
    else if (contentType.includes('image/')) {
      const ext = contentType.split('/')[1];
      filename = `image.${ext}`;
    }
  }

  // Handle response based on content type
  if (contentType && contentType.includes('text/html')) {
    // Handle HTML content as text
    const content = await response.text();
    await writeFile(filename, content);
  } else {
    // Handle binary content (PDFs, images, etc.)
    const arrayBuffer = await response.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);
    await writeFile(filename, buffer);
  }

  console.log(`Content saved as ${filename}`);
};

exportPage();

```

```codeBlockLines_p187
import requests
import re

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/export?token={TOKEN}"
headers = {
    'Content-Type': 'application/json'
}

data = {
    "url": "https://example.com/",
    "gotoOptions": {
        "waitUntil": "networkidle0",
        "timeout": 60000
    },
    "waitForSelector": {
        "selector": "#main-content",
        "timeout": 5000
    }
}

response = requests.post(url, headers=headers, json=data)

# Get content type and determine appropriate filename
content_type = response.headers.get('Content-Type', '')
disposition = response.headers.get('Content-Disposition', '')

# Try to get filename from Content-Disposition header
filename = 'downloaded-content'
if disposition and 'filename=' in disposition:
    match = re.search('filename="(.+?)"', disposition)
    if match:
        filename = match.group(1)
else:
    # Create filename based on content type
    if 'text/html' in content_type:
        filename = 'page.html'
    elif 'application/pdf' in content_type:
        filename = 'document.pdf'
    elif 'image/' in content_type:
        ext = content_type.split('/')[1]
        filename = f"image.{ext}"

# Write content to file using binary mode for all types to ensure proper handling
with open(filename, "wb") as file:
    file.write(response.content)

print(f"Content saved as {filename}")

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ExportPageWithOptions {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/export?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "gotoOptions": {
                "waitUntil": "networkidle0",
                "timeout": 60000
            },
            "waitForSelector": {
                "selector": "#main-content",
                "timeout": 5000
            }
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<byte[]> response = client.send(request, HttpResponse.BodyHandlers.ofByteArray());

            // Get content type and determine appropriate filename
            String contentType = response.headers().firstValue("Content-Type").orElse("");
            String disposition = response.headers().firstValue("Content-Disposition").orElse("");

            // Try to get filename from Content-Disposition header
            String filename = "downloaded-content";
            if (disposition.contains("filename=")) {
                Pattern pattern = Pattern.compile("filename=\"(.+?)\"");
                Matcher matcher = pattern.matcher(disposition);
                if (matcher.find()) {
                    filename = matcher.group(1);
                }
            } else {
                // Create filename based on content type
                if (contentType.contains("text/html")) {
                    filename = "page.html";
                } else if (contentType.contains("application/pdf")) {
                    filename = "document.pdf";
                } else if (contentType.contains("image/")) {
                    String ext = contentType.split("/")[1];
                    filename = "image." + ext;
                }
            }

            // Write content to file
            try (FileOutputStream fileOutputStream = new FileOutputStream(filename)) {
                fileOutputStream.write(response.body());
                System.out.println("Content saved as " + filename);
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
using System.Text.RegularExpressions;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/export?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""gotoOptions"": {
                ""waitUntil"": ""networkidle0"",
                ""timeout"": 60000
            },
            ""waitForSelector"": {
                ""selector"": ""#main-content"",
                ""timeout"": 5000
            }
        }
        ";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            // Get content type and determine appropriate filename
            var contentType = response.Content.Headers.ContentType?.MediaType ?? "";
            var disposition = response.Content.Headers.ContentDisposition?.ToString() ?? "";

            // Try to get filename from Content-Disposition header
            string filename = "downloaded-content";
            if (disposition.Contains("filename=")) {
                var match = Regex.Match(disposition, "filename=\"(.+?)\"");
                if (match.Success) {
                    filename = match.Groups[1].Value;
                }
            } else {
                // Create filename based on content type
                if (contentType.Contains("text/html")) {
                    filename = "page.html";
                } else if (contentType.Contains("application/pdf")) {
                    filename = "document.pdf";
                } else if (contentType.Contains("image/")) {
                    var ext = contentType.Split('/')[1];
                    filename = $"image.{ext}";
                }
            }

            // Handle all content types as binary for consistency
            var bytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync(filename, bytes);

            Console.WriteLine($"Content saved as {filename}");
        } catch (Exception ex) {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

### Export with Custom Headers [​](https://docs.browserless.io/rest-apis/export\#export-with-custom-headers "Direct link to Export with Custom Headers")

This example demonstrates how to export a web page with custom HTTP headers. Custom headers allow you to modify the browser's behavior when accessing the page, such as changing the User-Agent or setting language preferences.

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/export?token=YOUR_API_TOKEN_HERE \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com/",
    "headers": {
      "User-Agent": "Custom User Agent",
      "Accept-Language": "en-US"
    }
  }'

```

```codeBlockLines_p187
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/export?token=${TOKEN}`;
const headers = {
  'Content-Type': 'application/json'
};

const data = {
  url: "https://example.com/",
  headers: {
    "User-Agent": "Custom User Agent",
    "Accept-Language": "en-US"
  }
};

const exportPage = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  // Get content type to determine how to handle the response
  const contentType = response.headers.get('content-type');

  // Get filename from Content-Disposition header or create a default one based on content type
  let filename = 'downloaded-content';
  const disposition = response.headers.get('content-disposition');
  if (disposition && disposition.includes('filename=')) {
    const filenameMatch = disposition.match(/filename="(.+?)"/);
    if (filenameMatch) filename = filenameMatch[1];
  } else if (contentType) {
    // Set appropriate extension based on content type
    if (contentType.includes('text/html')) filename = 'page.html';
    else if (contentType.includes('application/pdf')) filename = 'document.pdf';
    else if (contentType.includes('image/')) {
      const ext = contentType.split('/')[1];
      filename = `image.${ext}`;
    }
  }

  // Handle response based on content type
  if (contentType && contentType.includes('text/html')) {
    // Handle HTML content as text
    const content = await response.text();
    await writeFile(filename, content);
  } else {
    // Handle binary content (PDFs, images, etc.)
    const arrayBuffer = await response.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);
    await writeFile(filename, buffer);
  }

  console.log(`Content saved as ${filename}`);
};

exportPage();

```

```codeBlockLines_p187
import requests
import re

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/export?token={TOKEN}"
headers = {
    'Content-Type': 'application/json'
}

data = {
    "url": "https://example.com/",
    "headers": {
        "User-Agent": "Custom User Agent",
        "Accept-Language": "en-US"
    }
}

response = requests.post(url, headers=headers, json=data)

# Get content type and determine appropriate filename
content_type = response.headers.get('Content-Type', '')
disposition = response.headers.get('Content-Disposition', '')

# Try to get filename from Content-Disposition header
filename = 'downloaded-content'
if disposition and 'filename=' in disposition:
    match = re.search('filename="(.+?)"', disposition)
    if match:
        filename = match.group(1)
else:
    # Create filename based on content type
    if 'text/html' in content_type:
        filename = 'page.html'
    elif 'application/pdf' in content_type:
        filename = 'document.pdf'
    elif 'image/' in content_type:
        ext = content_type.split('/')[1]
        filename = f"image.{ext}"

# Write content to file using binary mode for all types to ensure proper handling
with open(filename, "wb") as file:
    file.write(response.content)

print(f"Content saved as {filename}")

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ExportPageWithHeaders {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/export?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "headers": {
                "User-Agent": "Custom User Agent",
                "Accept-Language": "en-US"
            }
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<byte[]> response = client.send(request, HttpResponse.BodyHandlers.ofByteArray());

            // Get content type and determine appropriate filename
            String contentType = response.headers().firstValue("Content-Type").orElse("");
            String disposition = response.headers().firstValue("Content-Disposition").orElse("");

            // Try to get filename from Content-Disposition header
            String filename = "downloaded-content";
            if (disposition.contains("filename=")) {
                Pattern pattern = Pattern.compile("filename=\"(.+?)\"");
                Matcher matcher = pattern.matcher(disposition);
                if (matcher.find()) {
                    filename = matcher.group(1);
                }
            } else {
                // Create filename based on content type
                if (contentType.contains("text/html")) {
                    filename = "page.html";
                } else if (contentType.contains("application/pdf")) {
                    filename = "document.pdf";
                } else if (contentType.contains("image/")) {
                    String ext = contentType.split("/")[1];
                    filename = "image." + ext;
                }
            }

            // Write content to file
            try (FileOutputStream fileOutputStream = new FileOutputStream(filename)) {
                fileOutputStream.write(response.body());
                System.out.println("Content saved as " + filename);
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
using System.Text.RegularExpressions;
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/export?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""headers"": {
                ""User-Agent"": ""Custom User Agent"",
                ""Accept-Language"": ""en-US""
            }
        }
        ";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            // Get content type and determine appropriate filename
            var contentType = response.Content.Headers.ContentType?.MediaType ?? "";
            var disposition = response.Content.Headers.ContentDisposition?.ToString() ?? "";

            // Try to get filename from Content-Disposition header
            string filename = "downloaded-content";
            if (disposition.Contains("filename=")) {
                var match = Regex.Match(disposition, "filename=\"(.+?)\"");
                if (match.Success) {
                    filename = match.Groups[1].Value;
                }
            } else {
                // Create filename based on content type
                if (contentType.Contains("text/html")) {
                    filename = "page.html";
                } else if (contentType.Contains("application/pdf")) {
                    filename = "document.pdf";
                } else if (contentType.Contains("image/")) {
                    var ext = contentType.Split('/')[1];
                    filename = $"image.{ext}";
                }
            }

            // Handle all content types as binary for consistency
            var bytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync(filename, bytes);

            Console.WriteLine($"Content saved as {filename}");
        } catch (Exception ex) {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

### Export with Resource Download [​](https://docs.browserless.io/rest-apis/export\#export-with-resource-download "Direct link to Export with Resource Download")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/export?token=YOUR_API_TOKEN_HERE \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com/",
    "includeResources": true
  }' \
  --output "webpage.zip"

```

```codeBlockLines_p187
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/export?token=${TOKEN}`;
const headers = {
  'Content-Type': 'application/json'
};

const data = {
  url: "https://example.com/",
  includeResources: true
};

const exportPage = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const buffer = await response.arrayBuffer();
  await writeFile("webpage.zip", Buffer.from(buffer));
  console.log("Page with resources saved as webpage.zip");
};

exportPage();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/export?token={TOKEN}"
headers = {
    'Content-Type': 'application/json'
}

data = {
    "url": "https://example.com/",
    "includeResources": True
}

response = requests.post(url, headers=headers, json=data)

with open("webpage.zip", "wb") as file:
    file.write(response.content)

print("Page with resources saved as webpage.zip")

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;
import java.nio.file.Files;
import java.nio.file.Paths;

public class ExportPageWithResources {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/export?token=" + TOKEN;

        String jsonData = """
        {
            "url": "https://example.com/",
            "includeResources": true
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(jsonData))
            .build();

        try {
            HttpResponse<byte[]> response = client.send(request, HttpResponse.BodyHandlers.ofByteArray());
            Files.write(Paths.get("webpage.zip"), response.body());
            System.out.println("Page with resources saved as webpage.zip");
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

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/export?token={TOKEN}";

        string jsonData = @"
        {
            ""url"": ""https://example.com/"",
            ""includeResources"": true
        }
        ";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            var bytes = await response.Content.ReadAsByteArrayAsync();
            await File.WriteAllBytesAsync("webpage.zip", bytes);

            Console.WriteLine("Page with resources saved as webpage.zip");
        } catch (Exception ex) {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

## Handling Different Content Types [​](https://docs.browserless.io/rest-apis/export\#handling-different-content-types-1 "Direct link to Handling Different Content Types")

The export API can return various content types depending on the URL being accessed. Here's how to properly handle the different response types:

### HTML Content [​](https://docs.browserless.io/rest-apis/export\#html-content-1 "Direct link to HTML Content")

When accessing a standard web page, the API returns HTML content with `Content-Type: text/html`:

```codeBlockLines_p187
const response = await fetch(url, options);
if (response.headers.get('content-type')?.includes('text/html')) {
  const htmlContent = await response.text();
  // Process HTML content
}

```

### PDF Content [​](https://docs.browserless.io/rest-apis/export\#pdf-content-1 "Direct link to PDF Content")

When accessing PDF files or when the server returns PDF content, the API returns a PDF buffer with `Content-Type: application/pdf`:

```codeBlockLines_p187
const response = await fetch(url, options);
if (response.headers.get('content-type')?.includes('application/pdf')) {
  const arrayBuffer = await response.arrayBuffer();
  const pdfBuffer = Buffer.from(arrayBuffer);
  // Save or process PDF buffer
}

```

### Binary Content (Images, etc.) [​](https://docs.browserless.io/rest-apis/export\#binary-content-images-etc-1 "Direct link to Binary Content (Images, etc.)")

For other binary content like images, the API returns the appropriate content type and sets attachment headers:

```codeBlockLines_p187
const response = await fetch(url, options);
const contentType = response.headers.get('content-type');
if (contentType?.includes('image/') || !contentType?.includes('text/')) {
  const arrayBuffer = await response.arrayBuffer();
  const binaryBuffer = Buffer.from(arrayBuffer);
  // Save or process binary buffer
}

```

## Best Practices [​](https://docs.browserless.io/rest-apis/export\#best-practices "Direct link to Best Practices")

### Navigation and Timing [​](https://docs.browserless.io/rest-apis/export\#navigation-and-timing "Direct link to Navigation and Timing")

1. **Page Load Strategies**
   - Use appropriate `waitUntil` options based on your needs:

     - `load` \- Wait for the load event (good for static pages)
     - `domcontentloaded` \- Wait for the DOMContentLoaded event (faster but may miss dynamic content)
     - `networkidle0` \- Wait until there are no network connections for at least 500ms (good for single-page applications)
     - `networkidle2` \- Wait until there are no more than 2 network connections for at least 500ms (good for pages with background activity)
2. **Timeout Management**
   - Set reasonable timeout values based on your target page's complexity
   - Consider increasing timeouts for:
     - Pages with heavy JavaScript execution
     - Pages with large media files
     - Pages with complex animations
     - Pages with slow network conditions
3. **Content Waiting**
   - Use `waitForSelector` when you need to ensure specific content is loaded
   - Combine with `waitForTimeout` for additional stability
   - Consider using multiple selectors for critical content
   - Use `bestAttempt: true` for more resilient scraping, but be aware it may return incomplete content

### Resource Management [​](https://docs.browserless.io/rest-apis/export\#resource-management "Direct link to Resource Management")

4. **Asset Handling**
   - Use `includeAssets` wisely to control export size
   - Consider excluding unnecessary resource types:
     - Images for text-only exports
     - Stylesheets for raw content
     - Scripts for static content
   - Use `rejectResourceTypes` to filter specific asset types
   - Implement size limits for large resources
5. **Network Optimization**
   - Use `rejectRequestPattern` to exclude unnecessary requests
   - Consider implementing request throttling
   - Cache frequently accessed resources
   - Monitor and optimize network usage

### Error Handling and Reliability [​](https://docs.browserless.io/rest-apis/export\#error-handling-and-reliability "Direct link to Error Handling and Reliability")

6. **Robust Error Handling**
   - Implement proper error handling for:
     - Network timeouts
     - Resource loading failures
     - Invalid URLs
     - Rate limiting
   - Use appropriate HTTP status codes
   - Implement retry mechanisms for transient failures
7. **Content Validation**
   - Verify content completeness
   - Check for expected elements
   - Validate content structure
   - Implement checksums for critical content

### Security Considerations [​](https://docs.browserless.io/rest-apis/export\#security-considerations "Direct link to Security Considerations")

8. **URL and Content Safety**
   - Always use HTTPS URLs when possible
   - Validate URLs before making requests
   - Sanitize user-provided URLs
   - Implement content size limits
   - Be cautious when setting custom headers
9. **Authentication and Authorization**
   - Use secure methods for API token storage
   - Implement proper access controls
   - Monitor and log access attempts
   - Rotate API tokens regularly

### Performance Optimization [​](https://docs.browserless.io/rest-apis/export\#performance-optimization "Direct link to Performance Optimization")

10. **Export Size Management**
    - Implement compression where appropriate
    - Use appropriate export formats
    - Consider splitting large exports
    - Implement cleanup mechanisms for temporary files
11. **Concurrent Operations**
    - Implement proper rate limiting
    - Use appropriate concurrency levels
    - Monitor system resources
    - Implement queue management for high-volume operations

### Monitoring and Maintenance [​](https://docs.browserless.io/rest-apis/export\#monitoring-and-maintenance "Direct link to Monitoring and Maintenance")

12. **Logging and Monitoring**
    - Implement comprehensive logging
    - Monitor success/failure rates
    - Track export sizes and durations
    - Set up alerts for failures
    - Monitor rate limit usage
13. **Maintenance**
    - Regularly review and update selectors
    - Monitor for changes in target sites
    - Update error handling as needed
    - Review and optimize timeout values
    - Maintain documentation of changes

For additional support, please refer to the [Browserless documentation](https://docs.browserless.io/) or contact support.

- [Basic Usage](https://docs.browserless.io/rest-apis/export#basic-usage)
  - [JSON Payload Format](https://docs.browserless.io/rest-apis/export#json-payload-format)
- [Parameters](https://docs.browserless.io/rest-apis/export#parameters)
  - [Required Parameters](https://docs.browserless.io/rest-apis/export#required-parameters)
  - [Optional Parameters](https://docs.browserless.io/rest-apis/export#optional-parameters)
- [Response](https://docs.browserless.io/rest-apis/export#response)
- [Handling Different Content Types](https://docs.browserless.io/rest-apis/export#handling-different-content-types)
  - [HTML Content](https://docs.browserless.io/rest-apis/export#html-content)
  - [PDF Content](https://docs.browserless.io/rest-apis/export#pdf-content)
  - [Binary Content (Images, etc.)](https://docs.browserless.io/rest-apis/export#binary-content-images-etc)
- [Error Handling](https://docs.browserless.io/rest-apis/export#error-handling)
- [Examples](https://docs.browserless.io/rest-apis/export#examples)
  - [Basic Export Request](https://docs.browserless.io/rest-apis/export#basic-export-request)
  - [Export with Custom Navigation Options](https://docs.browserless.io/rest-apis/export#export-with-custom-navigation-options)
  - [Export with Custom Headers](https://docs.browserless.io/rest-apis/export#export-with-custom-headers)
  - [Export with Resource Download](https://docs.browserless.io/rest-apis/export#export-with-resource-download)
- [Handling Different Content Types](https://docs.browserless.io/rest-apis/export#handling-different-content-types-1)
  - [HTML Content](https://docs.browserless.io/rest-apis/export#html-content-1)
  - [PDF Content](https://docs.browserless.io/rest-apis/export#pdf-content-1)
  - [Binary Content (Images, etc.)](https://docs.browserless.io/rest-apis/export#binary-content-images-etc-1)
- [Best Practices](https://docs.browserless.io/rest-apis/export#best-practices)
  - [Navigation and Timing](https://docs.browserless.io/rest-apis/export#navigation-and-timing)
  - [Resource Management](https://docs.browserless.io/rest-apis/export#resource-management)
  - [Error Handling and Reliability](https://docs.browserless.io/rest-apis/export#error-handling-and-reliability)
  - [Security Considerations](https://docs.browserless.io/rest-apis/export#security-considerations)
  - [Performance Optimization](https://docs.browserless.io/rest-apis/export#performance-optimization)
  - [Monitoring and Maintenance](https://docs.browserless.io/rest-apis/export#monitoring-and-maintenance)