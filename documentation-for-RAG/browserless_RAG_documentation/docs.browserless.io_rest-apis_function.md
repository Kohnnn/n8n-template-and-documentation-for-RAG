---
url: "https://docs.browserless.io/rest-apis/function"
title: "/function API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/function#__docusaurus_skipToContent_fallback)

On this page

A quick way to run commands with Browserless is via our `/function` API. You can use Python, NodeJS or any other language that supports making HTTP requests, so you don't need to install any libraries on your end.

The `/function` endpoint allows for `POST` ing of custom code and context to run them with. The code function, which only supports puppeteer code, gets called with an object containing several properties: a `page` property, which is a puppeteer page object, and `context` which is the context you provide in the JSON body.

Functions should return an object with two properties: `data` and `type`. `data` can be whatever you'd like (Buffer, JSON, or plain text) and `type` is a string describing the Content-Type of `data`. Browserless reads both of these from your functions return value and resolves the request appropriately.

You can [view the complete Function API OpenAPI specification](https://docs.browserless.io/open-api#tag/Browser-REST-APIs/paths/~1chrome~1function/post).

## Basic Usage [​](https://docs.browserless.io/rest-apis/function\#basic-usage "Direct link to Basic Usage")

Both the `/function` and the `/download` API environments use [Ecmascript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules). You can use any code and native APIs available in the Chrome browser environment.

**JS Code**

```codeBlockLines_p187
export default async function ({ page }) {
  const rndNumber = () => {
    return Math.floor(Math.random() * (10**6 - 0));
  };

  await page.goto("https://example.com/");
  const url = await page.title();
  const numbers = [...Array(5)].map(() => rndNumber());

  return {
    data: {
      url,
      numbers,
    },
    // Make sure to match the appropriate content here
    type: "application/json",
  };
}

```

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/function?token=YOUR_API_TOKEN_HERE \
  -H 'Content-Type: application/javascript' \
  -d 'export default async function ({ page }) {
  const rndNumber = () => {
    return Math.floor(Math.random() * (10**6 - 0));
  };

  await page.goto("https://example.com/");
  const url = await page.title();
  const numbers = [...Array(5)].map(() => rndNumber());

  return {
    data: {
      url,
      numbers,
    },
    // Make sure to match the appropriate content here
    type: "application/json",
  };
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/function?token=${TOKEN}`;
const headers = {
  "Content-Type": "application/javascript"
};

const data = `
export default async function ({ page }) {
  const rndNumber = () => {
    return Math.floor(Math.random() * (10**6 - 0));
  };

  await page.goto("https://example.com/");
  const url = await page.title();
  const numbers = [...Array(5)].map(() => rndNumber());

  return {
    data: {
      url,
      numbers,
    },
    type: "application/json",
  };
}`;

const sendRequest = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: data
  });

  const result = await response.json();
  console.log(result);
};

sendRequest();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/function?token={TOKEN}"
headers = {
    "Content-Type": "application/javascript"
}

data = """
export default async function ({ page }) {
  const rndNumber = () => {
    return Math.floor(Math.random() * (10**6 - 0));
  };

  await page.goto("https://example.com/");
  const url = await page.title();
  const numbers = [...Array(5)].map(() => rndNumber());

  return {
    data: {
      url,
      numbers,
    },
    type: "application/json",
  };
}
"""

response = requests.post(url, headers=headers, data=data)

result = response.json()
print(result)

```

```codeBlockLines_p187
import java.net.URI;
import java.net.http.*;
import org.json.JSONObject;

public class BrowserlessFunction {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/function?token=" + TOKEN;

        String javascriptCode = """
        export default async function ({ page }) {
            const rndNumber = () => {
                return Math.floor(Math.random() * (10**6 - 0));
            };

            await page.goto("https://example.com/");
            const url = await page.title();
            const numbers = [...Array(5)].map(() => rndNumber());

            return {
                data: {
                    url,
                    numbers,
                },
                type: "application/json",
            };
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/javascript")
            .POST(HttpRequest.BodyPublishers.ofString(javascriptCode))
            .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            JSONObject jsonResponse = new JSONObject(response.body());
            System.out.println(jsonResponse.toString(4));
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
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/function?token={TOKEN}";

        string javascriptCode = @"
        export default async function ({ page }) {
            const rndNumber = () => {
                return Math.floor(Math.random() * (10**6 - 0));
            };

            await page.goto('https://example.com/');
            const url = await page.title();
            const numbers = [...Array(5)].map(() => rndNumber());

            return {
                data: {
                    url,
                    numbers,
                },
                type: 'application/json',
            };
        }
        ";

        using var client = new HttpClient();
        var content = new StringContent(javascriptCode, Encoding.UTF8, "application/javascript");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            var result = await response.Content.ReadAsStringAsync();
            Console.WriteLine(result);
        } catch (Exception ex) {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

**Example Reponse**

```codeBlockLines_p187
{
  "data": {
    "url": "Example Domain",
    "numbers": [\
      854246,\
      114512,\
      212580,\
      482122,\
      107878\
    ]
  },
  "type": "application/json"
}

```

## Importing libraries [​](https://docs.browserless.io/rest-apis/function\#importing-libraries "Direct link to Importing libraries")

Since the `/function` API uses ESM modules, you can use `import` syntax over HTTP to load moules. For instance, let's try leading the [Fake](https://fakerjs.dev/) module.

**JS Code**

```codeBlockLines_p187
import { faker } from "https://esm.sh/@faker-js/faker";

export default async function () {
  const Internet = faker.internet;
  const rndData = [...Array(5)].map(() => ({
    domain: Internet.domainName(),
    ip: Internet.ip(),
    mac: Internet.mac(),
    protocol: Internet.protocol(),
  }));

  return {
    data: { domains: rndData },
    type: "application/json",
  };
}

```

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X POST \
https://production-sfo.browserless.io/function?token=YOUR_API_TOKEN_HERE \
-H 'Content-Type: application/javascript' \
-d 'import { faker } from "https://esm.sh/@faker-js/faker";

export default async function () {
const Internet = faker.internet;
const rndData = [...Array(5)].map(() => ({
  domain: Internet.domainName(),
  ip: Internet.ip(),
  mac: Internet.mac(),
  protocol: Internet.protocol(),
}));

return {
  data: { domains: rndData },
  type: "application/json",
};
}'

```

```codeBlockLines_p187
const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/function?token=${TOKEN}`;
const headers = {
  "Content-Type": "application/javascript"
};

const data = `
import { faker } from "https://esm.sh/@faker-js/faker";

export default async function () {
  const Internet = faker.internet;
  const rndData = [...Array(5)].map(() => ({
    domain: Internet.domainName(),
    ip: Internet.ip(),
    mac: Internet.mac(),
    protocol: Internet.protocol(),
  }));

  return {
    data: { domains: rndData },
    type: "application/json",
  };
}`;

const sendRequest = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: data
  });

  const result = await response.json();
  console.log(result);
};

sendRequest();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/function?token={TOKEN}"
headers = {
    "Content-Type": "application/javascript"
}

data = """
import { faker } from "https://esm.sh/@faker-js/faker";

export default async function () {
  const Internet = faker.internet;
  const rndData = [...Array(5)].map(() => ({
    domain: Internet.domainName(),
    ip: Internet.ip(),
    mac: Internet.mac(),
    protocol: Internet.protocol(),
  }));

  return {
    data: { domains: rndData },
    type: "application/json",
  };
}
"""

response = requests.post(url, headers=headers, data=data)
result = response.json()
print(result)

```

```codeBlockLines_p187
import java.net.URI;
import java.net.http.*;
import org.json.JSONObject;

public class BrowserlessFakerFunction {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/function?token=" + TOKEN;

        String javascriptCode = """
        import { faker } from "https://esm.sh/@faker-js/faker";

        export default async function () {
            const Internet = faker.internet;
            const rndData = [...Array(5)].map(() => ({
                domain: Internet.domainName(),
                ip: Internet.ip(),
                mac: Internet.mac(),
                protocol: Internet.protocol(),
            }));

            return {
                data: { domains: rndData },
                type: "application/json",
            };
        }
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/javascript")
            .POST(HttpRequest.BodyPublishers.ofString(javascriptCode))
            .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            JSONObject jsonResponse = new JSONObject(response.body());
            System.out.println(jsonResponse.toString(4));
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
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/function?token={TOKEN}";

        string javascriptCode = @"
        import { faker } from 'https://esm.sh/@faker-js/faker';

        export default async function () {
            const Internet = faker.internet;
            const rndData = [...Array(5)].map(() => ({
                domain: Internet.domainName(),
                ip: Internet.ip(),
                mac: Internet.mac(),
                protocol: Internet.protocol(),
            }));

            return {
                data: { domains: rndData },
                type: 'application/json',
            };
        }
        ";

        using var client = new HttpClient();
        var content = new StringContent(javascriptCode, Encoding.UTF8, "application/javascript");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            var result = await response.Content.ReadAsStringAsync();
            Console.WriteLine(result);
        } catch (Exception ex) {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

## JSON API [​](https://docs.browserless.io/rest-apis/function\#json-api "Direct link to JSON API")

You can also use the /function API sending a JSON payload. You must send an object with the following values:

- `code`: String, required — custom function code.
- `context`: Object, optional — value used to pass context values and arguments to the `code`

### Example [​](https://docs.browserless.io/rest-apis/function\#example "Direct link to Example")

**JS Code**

```codeBlockLines_p187
import { faker } from "https://esm.sh/@faker-js/faker";

export default async function ({ context }) {
  const Internet = faker.internet;
  const rndData = [...Array(context.len)].map(() => ({
    domain: Internet.domainName(),
    ip: Internet.ip(),
    mac: Internet.mac(),
    protocol: Internet.protocol(),
  }));

  return {
    data: {
      domains: rndData,
      length: context.len
    },
    type: "application/json",
  };
}

```

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/function?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  # Minified code
  --data '{
  "code": "import{faker as a}from\"https://esm.sh/@faker-js/faker\";export default async function({context:o}){let t=a.internet,e=[...Array(o.len)].map(()=>({domain:t.domainName(),ip:t.ip(),mac:t.mac(),protocol:t.protocol()}));return{data:{domains:e,length:o.len},type:`application/json`}};",
  "context": {
    "len": 10
  }
}'

```

```codeBlockLines_p187
import fetch from 'node-fetch';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/function?token=${TOKEN}`;
const headers = {
  "Content-Type": "application/json"
};

const data = {
  code: 'import{faker as a}from"https://esm.sh/@faker-js/faker";export default async function({context:o}){let t=a.internet,e=[...Array(o.len)].map(()=>({domain:t.domainName(),ip:t.ip(),mac:t.mac(),protocol:t.protocol()}));return{data:{domains:e,length:o.len},type:`application/json`}};',
  context: { len: 10 }
};

const sendRequest = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);
};

sendRequest();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/function?token={TOKEN}"
headers = {
    "Content-Type": "application/json"
}

data = {
    "code": 'import{faker as a}from"https://esm.sh/@faker-js/faker";export default async function({context:o}){let t=a.internet,e=[...Array(o.len)].map(()=>({domain:t.domainName(),ip:t.ip(),mac:t.mac(),protocol:t.protocol()}));return{data:{domains:e,length:o.len},type:`application/json`}};',
    "context": {
        "len": 10
    }
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)

```

```codeBlockLines_p187
import java.net.URI;
import java.net.http.*;
import org.json.JSONObject;

public class BrowserlessFakerMinified {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/function?token=" + TOKEN;

        String jsonData = """
        {
            "code": "import{faker as a}from\\\"https://esm.sh/@faker-js/faker\\\";export default async function({context:o}){let t=a.internet,e=[...Array(o.len)].map(()=>({domain:t.domainName(),ip:t.ip(),mac:t.mac(),protocol:t.protocol()}));return{data:{domains:e,length:o.len},type:`application/json`}};",
            "context": {
                "len": 10
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
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            JSONObject jsonResponse = new JSONObject(response.body());
            System.out.println(jsonResponse.toString(4));
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
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/function?token={TOKEN}";

        string jsonData = @"
        {
            ""code"": ""import{faker as a}from\""https://esm.sh/@faker-js/faker\"";export default async function({context:o}){let t=a.internet,e=[...Array(o.len)].map(()=>({domain:t.domainName(),ip:t.ip(),mac:t.mac(),protocol:t.protocol()}));return{data:{domains:e,length:o.len},type:`application/json`}};"",
            ""context"": {
                ""len"": 10
            }
        }
        ";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            var result = await response.Content.ReadAsStringAsync();
            Console.WriteLine(result);
        } catch (Exception ex) {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

- [Basic Usage](https://docs.browserless.io/rest-apis/function#basic-usage)
- [Importing libraries](https://docs.browserless.io/rest-apis/function#importing-libraries)
- [JSON API](https://docs.browserless.io/rest-apis/function#json-api)
  - [Example](https://docs.browserless.io/rest-apis/function#example)