---
url: "https://docs.browserless.io/nav-options"
title: "Navigation Options | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/nav-options#__docusaurus_skipToContent_fallback)

On this page

BQL makes it easy to navigate websites and interact with them. Whether you're capturing screenshots, generating PDFs, or handling other automation tasks, you can use the following navigation options to change BQL's behavior.

note

The examples in this section will show you how to use the [`pdf`](https://docs.browserless.io/bql-schema/operations/mutations/pdf) and [`screenshot`](https://docs.browserless.io/bql-schema/operations/mutations/screenshot) mutations.

On this collection we’ll look at:

- [Basic Usage](https://docs.browserless.io/nav-options#basic-usage)
- [Setting HTML content](https://docs.browserless.io/pdf/html-content)
- [Rejecting Undesired Requests](https://docs.browserless.io/pdf/rejects)
- [Navigation Options](https://docs.browserless.io/pdf/navigation-options)
- [Waiting for Things](https://docs.browserless.io/pdf/waiting)

## Basic Usage [​](https://docs.browserless.io/nav-options\#basic-usage "Direct link to Basic Usage")

- PDF
- Screenshot

- BQL Query
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
mutation PDF {
  goto(url: "https://example.com") {
    status
  }

  pdf(displayHeaderFooter: true, printBackground: false, format: a0) {
    base64
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf(displayHeaderFooter: true, printBackground: false, format: a0) {\n    base64\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf(displayHeaderFooter: true, printBackground: false, format: a0) {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf(displayHeaderFooter: true, printBackground: false, format: a0) {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf(displayHeaderFooter: true, printBackground: false, format: a0) {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf(displayHeaderFooter: true, printBackground: false, format: a0) {
    base64
  }
}",
    variables = "",
    operationName = "PDF"
};

using (var client = new HttpClient())
{
    var jsonPayload = System.Text.Json.JsonSerializer.Serialize(payload);
    var content = new StringContent(jsonPayload, Encoding.UTF8, "application/json");

    var response = await client.PostAsync(endpoint, content);
    string responseBody = await response.Content.ReadAsStringAsync();

    Console.WriteLine(responseBody);
}

```

- BQL Query
- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
mutation Screenshot {
  goto(url: "https://example.com") {
    status
  }

  screenshot(omitBackground:true) {
    base64
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation Screenshot {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  screenshot(omitBackground:true) {\n    base64\n  }\n}","variables":"","operationName":"Screenshot"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation Screenshot {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  screenshot(omitBackground:true) {\n    base64\n  }\n}","variables":"","operationName":"Screenshot"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation Screenshot {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  screenshot(omitBackground:true) {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "Screenshot",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation Screenshot {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  screenshot(omitBackground:true) {\n    base64\n  }\n}","variables":"","operationName":"Screenshot"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation Screenshot {
  goto(url: ""https://example.com"") {
    status
  }

  screenshot(omitBackground: true) {
    base64
  }
}",
    variables = "",
    operationName = "Screenshot"
};

using (HttpClient httpClient = new HttpClient())
{
    var jsonPayload = System.Text.Json.JsonSerializer.Serialize(payload);
    var content = new StringContent(jsonPayload, Encoding.UTF8, "application/json");

    var response = await httpClient.PostAsync(endpoint, content);
    string responseBody = await response.Content.ReadAsStringAsync();
    Console.WriteLine(responseBody);
}

```

BQL Schemas

For more details on BQL mutations, refer to the [BrowserQL Schema](https://docs.browserless.io/bql-schema/schema) reference pages.

Rest API

[Generating PDFs](https://docs.browserless.io/rest-apis/pdf) and [Taking Screenshots](https://docs.browserless.io/rest-apis/screenshot) can also be done with Browserless Rest API.

- [Basic Usage](https://docs.browserless.io/nav-options#basic-usage)