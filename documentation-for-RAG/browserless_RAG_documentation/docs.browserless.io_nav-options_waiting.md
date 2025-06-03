---
url: "https://docs.browserless.io/nav-options/waiting"
title: "Waiting for Things | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/nav-options/waiting#__docusaurus_skipToContent_fallback)

On this page

- PDF
- Screenshot

BrowserQL offers 5 different ways to wait for preconditions to be met on the page before returning the response. These are:

- [waitForNavigation](https://docs.browserless.io/nav-options/waiting#waitfornavigation)
- [waitForRequest](https://docs.browserless.io/nav-options/waiting#waitforrequest)
- [waitForResponse](https://docs.browserless.io/nav-options/waiting#waitforresponse)
- [waitForSelector](https://docs.browserless.io/nav-options/waiting#waitforselector)
- [waitForTimeout](https://docs.browserless.io/nav-options/waiting#waitfortimeout)

BQL Schemas

For more details on BQL mutations, refer to the [BrowserQL Schema](https://docs.browserless.io/bql-schema/schema) reference pages.

Rest API

[Generating PDFs](https://docs.browserless.io/rest-apis/pdf) and [Taking Screenshots](https://docs.browserless.io/rest-apis/screenshot) can also be done with Browserless Rest API.

## waitForNavigation [​](https://docs.browserless.io/nav-options/waiting\#waitfornavigation "Direct link to waitForNavigation")

Waits for a navigation even to fire, useful for clicking an element and waiting for a page load.

The object can have any of these values:

- `timeout`: Float, optional — The maximum amount of time, in milliseconds, to wait for the page to load, overriding any defaults. Default timeout is 30 seconds, or 30000.
- `waitUntil`: [WaitUntilGoto enum](https://docs.browserless.io/bql-schema/types/enums/wait-until-goto), optional — When to consider the page fully-loaded and proceed with further execution

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
  goto(url: "https://example.com/") {
    status
  }

  waitForNavigation(waitUntil: load) {
    status
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForNavigation(waitUntil: load) {\n    status\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForNavigation(waitUntil: load) {\n    status\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForNavigation(waitUntil: load) {\n    status\n  }\n}",
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
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForNavigation(waitUntil: load) {\n    status\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForNavigation(waitUntil: load) {
    status
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
  goto(url: "https://example.com/") {
    status
  }

  waitForNavigation(waitUntil: load) {
    status
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForNavigation(waitUntil: load) {\n    status\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForNavigation(waitUntil: load) {\n    status\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForNavigation(waitUntil: load) {\n    status\n  }\n}",
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
    .body({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForNavigation(waitUntil: load) {\n    status\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation Screenshot {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForNavigation(waitUntil: load) {
    status
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

## waitForRequest [​](https://docs.browserless.io/nav-options/waiting\#waitforrequest "Direct link to waitForRequest")

Waits for the browser to make a particular request.

The object can have any of these values:

- `method`: [Method](https://docs.browserless.io/bql-schema/types/enums/method), optional — The method of the request to wait for.
- `timeout`: Float, optional — How long to wait for the request to be made before timing out, overriding any defaults. Default timeout is 30 seconds, or 30000.
- `url`: String, optional — The pattern of the request URL to wait for, using glob-style pattern-matching.

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
  goto(url: "https://example.com/") {
    status
  }

  waitForRequest(method: GET) {
    time
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForRequest(method: GET) {\n    time\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForRequest(method: GET) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForRequest(method: GET) {\n    time\n  }\n}",
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
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForRequest(method: GET) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForRequest(method: GET) {
    time
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
  goto(url: "https://example.com/") {
    status
  }

  waitForRequest(method: GET) {
    time
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForRequest(method: GET) {\n    time\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForRequest(method: GET) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForRequest(method: GET) {\n    time\n  }\n}",
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
    .body({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForRequest(method: GET) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation Screenshot {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForRequest(method: GET) {
    time
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

## waitForResponse [​](https://docs.browserless.io/nav-options/waiting\#waitforresponse "Direct link to waitForResponse")

Waits for a particular network response to be made back to the browser.

The object can have any of these values:

- `statuses`: \[int\] list, optional — The HTTP Response code(s) of the URL to wait for. Can be a single HTTP code or a list of desired codes.
- `url`: String, optional — The pattern of the response URL to wait for, using glob-style pattern-matching.

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
  goto(url: "https://example.com/") {
    status
  }

  waitForResponse(codes: [200]) {
    time
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForResponse(codes: [200]) {\n    time\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForResponse(codes: [200]) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForResponse(codes: [200]) {\n    time\n  }\n}",
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
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForResponse(codes: [200]) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForResponse(codes: [200]) {
    time
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
  goto(url: "https://example.com/") {
    status
  }

  waitForResponse(codes: [200]) {
    time
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForResponse(codes: [200]) {\n    time\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForResponse(codes: [200]) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForResponse(codes: [200]) {\n    time\n  }\n}",
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
    .body({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForResponse(codes: [200]) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation Screenshot {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForResponse(codes: [200]) {
    time
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

## waitForSelector [​](https://docs.browserless.io/nav-options/waiting\#waitforselector "Direct link to waitForSelector")

Wait for a selector to appear in page. If at the moment of calling the method the selector already exists, the method will return immediately. If the selector doesn't appear after the timeout milliseconds of waiting, the function will throw.

The object can have any of these values:

- `selector`: String, required — A valid CSS selector.
- `timeout`: Number, optional — Maximum number of milliseconds to wait for the selector before failing.
- `visible`: Boolean, optional — Wait for the selected element to be present in DOM and to be visible, i.e. to not have `display: none` or `visibility: hidden` CSS properties.

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
  goto(url: "https://example.com/") {
    status
  }

  waitForSelector(selector: "h1" timeout: 5000) {
    selector
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForSelector(selector: \"h1\" timeout: 5000) {\n    selector\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForSelector(selector: \"h1\" timeout: 5000) {\n    selector\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForSelector(selector: \"h1\" timeout: 5000) {\n    selector\n  }\n}",
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
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForSelector(selector: \"h1\" timeout: 5000) {\n    selector\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForSelector(selector: ""h1"" timeout: 5000) {
    selector
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
  goto(url: "https://example.com/") {
    status
  }

  waitForSelector(selector: "h1" timeout: 5000) {
    selector
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForSelector(selector: \"h1\" timeout: 5000) {\n    selector\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForSelector(selector: \"h1\" timeout: 5000) {\n    selector\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForSelector(selector: \"h1\" timeout: 5000) {\n    selector\n  }\n}",
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
    .body({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForSelector(selector: \"h1\" timeout: 5000) {\n    selector\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation Screenshot {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForSelector(selector: ""h1"" timeout: 5000) {
    selector
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

## waitForTimeout [​](https://docs.browserless.io/nav-options/waiting\#waitfortimeout "Direct link to waitForTimeout")

Wait for a period of time, defined in milliseconds.

The object needs the following value:

- `time`: Float, required - The amount of time to wait for, in milliseconds.

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
  goto(url: "https://example.com/") {
    status
  }

  waitForTimeout(time: 1000) {
    time
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForTimeout(time: 1000) {\n    time\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForTimeout(time: 1000) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForTimeout(time: 1000) {\n    time\n  }\n}",
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
    .body({"query":"mutation PDF {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForTimeout(time: 1000) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation PDF {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForTimeout(time: 1000) {
    time
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
  goto(url: "https://example.com/") {
    status
  }

  waitForTimeout(time: 1000) {
    time
  }
}

```

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  --data '{"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForTimeout(time: 1000) {\n    time\n  }\n}","variables":"","operationName":"PDF"}'

```

```codeBlockLines_p187
const endpoint = "https://production-sfo.browserless.io/chromium/bql";
const token = "YOUR_API_TOKEN_HERE";

const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForTimeout(time: 1000) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
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
    "query": "mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForTimeout(time: 1000) {\n    time\n  }\n}",
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
    .body({"query":"mutation Screenshot {\n  goto(url: \"https://example.com/\") {\n    status\n  }\n\n  waitForTimeout(time: 1000) {\n    time\n  }\n}","variables":"","operationName":"PDF"})
    .asString();

```

```codeBlockLines_p187
string url = "https://production-sfo.browserless.io/chromium/bql";
string token = "YOUR_API_TOKEN_HERE";
string endpoint = $"{url}?token={token}";

var payload = new
{
    query = @"mutation Screenshot {
  goto(url: ""https://example.com/"") {
    status
  }

  waitForTimeout(time: 1000) {
    time
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

- [waitForNavigation](https://docs.browserless.io/nav-options/waiting#waitfornavigation)
- [waitForRequest](https://docs.browserless.io/nav-options/waiting#waitforrequest)
- [waitForResponse](https://docs.browserless.io/nav-options/waiting#waitforresponse)
- [waitForSelector](https://docs.browserless.io/nav-options/waiting#waitforselector)
- [waitForTimeout](https://docs.browserless.io/nav-options/waiting#waitfortimeout)