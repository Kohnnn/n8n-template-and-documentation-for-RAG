---
url: "https://docs.browserless.io/browserql/launch-parameters"
title: "Launch Parameters and Options | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/launch-parameters#__docusaurus_skipToContent_fallback)

On this page

Browserless allows extensive configuration of how browsers are launched and behave during
your sessions. These launch parameters can be provided either via query parameters in the
URL or through a special JSON launch payload. Whether you're using BQL, BaaS v2, or REST, these
options let you tweak the browser environment to fit your needs.

## Passing Launch Options [​](https://docs.browserless.io/browserql/launch-parameters\#passing-launch-options "Direct link to Passing Launch Options")

Two ways to specify launch options:

1. **Individual Query Parameters**: Add options directly to URLs (e.g., `&headless=false`, `&proxy=residential`). Best for simple boolean options.

2. **Combined `launch` Parameter (JSON)**: For complex configurations, use a single query param `launch` with a JSON string as its value. This JSON can include any Chrome flags or Browserless-specific settings in a structured way. It's essentially the equivalent of Puppeteer's `launch({ options })` but provided to the cloud service:







```codeBlockLines_p187
&launch={"headless":false,"stealth":true,"args":["--window-size=1920,1080"]}

```











(URL-encoded) would configure a headful, stealth-enabled browser with a specific window size.


Browserless merges both methods if used together, with individual parameters taking precedence. Use query params for simple toggles and the launch parameter for multiple settings.

## Launch Options (Query Parameters) [​](https://docs.browserless.io/browserql/launch-parameters\#launch-options-query-parameters "Direct link to Launch Options (Query Parameters)")

Below is a list of available launch options you can use in query strings. BrowserQL
internally uses some of these, but BQL users typically set these via the IDE session settings
rather than manually in a URL.

| Parameter | Description | Default |
| --- | --- | --- |
| headless | Runs the browser in headless mode. Set to false to enable headful mode (with a GUI). While the GUI isn't visible in cloud environments, headful mode may help bypass bot detection. Note: it uses more resources. | `true` |
| stealth | Enables stealth mode to reduce automation signals (similar to puppeteer-extra’s stealth plugin). In BQL, stealth is always on by design and controlled via the humanlike option. In BaaS/REST, set to true to enable stealth techniques. | - `false` (for BaaS/REST)<br>- `true` (for BQL) |
| humanlike | Simulates human-like behavior such as natural mouse movement, typing, and random delays. In the BQL IDE, this can be toggled in session settings. For direct BQL GraphQL calls, use humanlike: true in the launch payload. Recommended for strict bot detection scenarios. | `false` |
| blockAds | Enables the built-in ad blocker (powered by uBlock Origin). Helps speed up scripts and reduce noise by blocking ads and trackers. Especially useful for scraping to avoid popups and clutter. | `false` |
| blockConsentModals | Automatically blocks or dismisses cookie/GDPR consent banners. Available in BQL sessions and the /screenshot and /pdf REST APIs. In BQL, toggle it via the IDE or launch JSON. Useful for cleaner scraping by removing overlays. | `false` |
| proxy | Routes browser traffic through a proxy. Options: proxy=residential for Browserless’s residential proxy pool; proxy=\`<your proxy URL>\` for your own proxy. Omit to use a direct connection. | none |
| proxyCountry | Used with proxy=residential to specify the exit node’s country. Accepts ISO 3166 country codes (e.g., us, gb, de). If omitted, a random location is chosen. | none |
| proxySticky | Used with proxy=residential to maintain the same proxy IP across a session (when possible). Useful for sites that expect consistent IP usage. | `false` |
| timeout | Maximum session duration in milliseconds. The session will automatically close after this time to prevent overuse. | 60000 |

### Headless [​](https://docs.browserless.io/browserql/launch-parameters\#headless "Direct link to Headless")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&headless=false' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(\n    url: \"https://example.com\"\n  ) {\n    status\n  }\n  simple: pdf {\n    base64\n  }\n}","variables":{},"operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&headless=false";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&headless=false"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&headless=false";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&headless=false";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf {
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

### Stealth [​](https://docs.browserless.io/browserql/launch-parameters\#stealth "Direct link to Stealth")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&stealth=false' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(\n    url: \"https://example.com\"\n  ) {\n    status\n  }\n  simple: pdf {\n    base64\n  }\n}","variables":{},"operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&stealth=false";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&stealth=false"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&stealth=false";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&stealth=false";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf {
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

### Human Like behavior [​](https://docs.browserless.io/browserql/launch-parameters\#human-like-behavior "Direct link to Human Like behavior")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&humanlike=true' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(\n    url: \"https://example.com\"\n  ) {\n    status\n  }\n  simple: pdf {\n    base64\n  }\n}","variables":{},"operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&humanlike=true";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&humanlike=true"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&humanlike=true";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&humanlike=true";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf {
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

### Block Ads [​](https://docs.browserless.io/browserql/launch-parameters\#block-ads "Direct link to Block Ads")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&adBlock=true' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(\n    url: \"https://example.com\"\n  ) {\n    status\n  }\n  simple: pdf {\n    base64\n  }\n}","variables":{},"operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&adBlock=true";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&adBlock=true"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&adBlock=true";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&adBlock=true";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf {
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

### Block Consent Modals [​](https://docs.browserless.io/browserql/launch-parameters\#block-consent-modals "Direct link to Block Consent Modals")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&blockConsentModals=true' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(\n    url: \"https://example.com\"\n  ) {\n    status\n  }\n  simple: pdf {\n    base64\n  }\n}","variables":{},"operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&blockConsentModals=true";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&blockConsentModals=true"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&blockConsentModals=true";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&blockConsentModals=true";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf {
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

### Proxy [​](https://docs.browserless.io/browserql/launch-parameters\#proxy "Direct link to Proxy")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(\n    url: \"https://example.com\"\n  ) {\n    status\n  }\n  simple: pdf {\n    base64\n  }\n}","variables":{},"operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf {
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

### Proxy Country [​](https://docs.browserless.io/browserql/launch-parameters\#proxy-country "Direct link to Proxy Country")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=br' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(\n    url: \"https://example.com\"\n  ) {\n    status\n  }\n  simple: pdf {\n    base64\n  }\n}","variables":{},"operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=br";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=br"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=br";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=br";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf {
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

### Proxy Sticky [​](https://docs.browserless.io/browserql/launch-parameters\#proxy-sticky "Direct link to Proxy Sticky")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxySticky=true' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(\n    url: \"https://example.com\"\n  ) {\n    status\n  }\n  simple: pdf {\n    base64\n  }\n}","variables":{},"operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxySticky=true";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxySticky=true"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxySticky=true";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&proxy=residential&proxySticky=true";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf {
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

### Timeout [​](https://docs.browserless.io/browserql/launch-parameters\#timeout "Direct link to Timeout")

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&timeout=25000' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(\n    url: \"https://example.com\"\n  ) {\n    status\n  }\n  simple: pdf {\n    base64\n  }\n}","variables":{},"operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&timeout=25000";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
};

const url = `${endpoint}?token=${token}`;
const response = await fetch(url, options);
const data = await response.json();

console.log(data);

```

```codeBlockLines_p187
import requests

endpoint = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&timeout=25000"
query_string = {
    "token": "YOUR_API_TOKEN_HERE",
}
headers = {
    "Content-Type": "application/json",
}
payload = {
    "query": "mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}",
    "variables": None,
    "operationName": "PDF",
}

response = requests.post(endpoint, params=query_string, headers=headers, json=payload)
print(response.json())

```

```codeBlockLines_p187
String url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&timeout=25000";
String token = "YOUR_API_TOKEN_HERE";
String endpoint = String.format("%s?token=%s%s%s", url, token);

HttpResponse<String> response = Unirest.post(endpoint)
    .header("Content-Type", "application/json")
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com\") {\n    status\n  }\n\n  pdf {\n    base64\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE&timeout=25000";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com"") {
    status
  }

  pdf {
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

- [Passing Launch Options](https://docs.browserless.io/browserql/launch-parameters#passing-launch-options)
- [Launch Options (Query Parameters)](https://docs.browserless.io/browserql/launch-parameters#launch-options-query-parameters)
  - [Headless](https://docs.browserless.io/browserql/launch-parameters#headless)
  - [Stealth](https://docs.browserless.io/browserql/launch-parameters#stealth)
  - [Human Like behavior](https://docs.browserless.io/browserql/launch-parameters#human-like-behavior)
  - [Block Ads](https://docs.browserless.io/browserql/launch-parameters#block-ads)
  - [Block Consent Modals](https://docs.browserless.io/browserql/launch-parameters#block-consent-modals)
  - [Proxy](https://docs.browserless.io/browserql/launch-parameters#proxy)
  - [Proxy Country](https://docs.browserless.io/browserql/launch-parameters#proxy-country)
  - [Proxy Sticky](https://docs.browserless.io/browserql/launch-parameters#proxy-sticky)
  - [Timeout](https://docs.browserless.io/browserql/launch-parameters#timeout)