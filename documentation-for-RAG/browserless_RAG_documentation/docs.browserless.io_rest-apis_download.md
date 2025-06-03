---
url: "https://docs.browserless.io/rest-apis/download"
title: "/download API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/download#__docusaurus_skipToContent_fallback)

On this page

The `/download` API is used for returning files Chrome has downloaded during the execution of puppeteer code, which is ran inside context of the browser. Browserless sets up a blank page, a fresh download directory, injects your puppeteer code, and then executes it. You can load external libraries via the `import` syntax, and import ESM-style modules that are written for execution inside of the browser. Once your script is finished, any downloaded files from Chromium are returned back with the appropriate content-type header.

You can [check the full Open API schema here](https://docs.browserless.io/open-api#tag/Browser-REST-APIs/paths/~1chrome~1download/post).

warning

If your download request doesn't result in a **file** being downloaded, Browserless will likely time out the function.

## Basic Usage [​](https://docs.browserless.io/rest-apis/download\#basic-usage "Direct link to Basic Usage")

Here's an example of downloading a file created in the browser (a CSV file):

```codeBlockLines_p187
import puppeteer from "puppeteer";

async function run() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Here we generate a json file and have the browser download it
  await page.evaluate(() => {
    const json = {
      ping: "pong",
      rnd: [...Array(5)].map(() => Math.random()),
    };
    const jsonContent = `data:application/json,${JSON.stringify(json)}`;
    const encodedUri = encodeURI(jsonContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "data.json");
    document.body.appendChild(link);
    return link.click();
  });
  await browser.close();
}

run();

```

This might come as a surprise, but unfortunately in puppeteer there's no way to know if the file was downloaded, or an API to even get it. You'll have to _know_ ahead of time where files are kept, and watch the file system for it to complete. Instead of wiring up all that code you can send Browserless an HTTP request and it takes care of all the underlying file-system calls:

**JS Code**

```codeBlockLines_p187
export default function ({ page }){
  await page.evaluate(() => {
    const json = {
      ping: "pong",
      rnd: [...Array(5)].map(() => Math.random())
    }
    const jsonContent = `data:application/json,${JSON.stringify(json)}`;
    const encodedUri = encodeURI(jsonContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "data.json");
    document.body.appendChild(link);
    return link.click();
  });
}

```

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/download?token=YOUR_API_TOKEN_HERE \
  -H 'Content-Type: application/javascript' \
  -d 'export default function ({ page }){
  await page.evaluate(() => {
    const json = {
      ping: "pong",
      rnd: [...Array(5)].map(() => Math.random())
    }
    const jsonContent = `data:application/json,${JSON.stringify(json)}`;
    const encodedUri = encodeURI(jsonContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "data.json");
    document.body.appendChild(link);
    return link.click();
  });
};'

```

```codeBlockLines_p187
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/download?token=${TOKEN}`;
const headers = {
  "Content-Type": "application/javascript"
};

const data = `
export default async function ({ page }) {
  await page.evaluate(() => {
    const json = {
      ping: "pong",
      rnd: [...Array(5)].map(() => Math.random())
    };
    const jsonContent = \`data:application/json,\${JSON.stringify(json)}\`;
    const encodedUri = encodeURI(jsonContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "data.json");
    document.body.appendChild(link);
    link.click();
  });
};
`;

const downloadFile = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: data
  });

  const buffer = await response.arrayBuffer();
  await writeFile("data.json", Buffer.from(buffer));
  console.log("File saved as data.json");
};

downloadFile();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/download?token={TOKEN}"
headers = {
    "Content-Type": "application/javascript"
}

data = """
export default async function ({ page }) {
  await page.evaluate(() => {
    const json = {
      ping: "pong",
      rnd: [...Array(5)].map(() => Math.random())
    };
    const jsonContent = `data:application/json,${JSON.stringify(json)}`;
    const encodedUri = encodeURI(jsonContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "data.json");
    document.body.appendChild(link);
    link.click();
  });
};
"""

response = requests.post(url, headers=headers, data=data)

with open("data.json", "wb") as file:
    file.write(response.content)

print("File saved as data.json")

```

```codeBlockLines_p187
import java.io.*;
import java.net.*;
import java.net.http.*;

public class DownloadJsonFile {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/download?token=" + TOKEN;

        String javascriptCode = """
        export default async function ({ page }) {
            await page.evaluate(() => {
                const json = {
                    ping: "pong",
                    rnd: [...Array(5)].map(() => Math.random())
                };
                const jsonContent = `data:application/json,${JSON.stringify(json)}`;
                const encodedUri = encodeURI(jsonContent);
                const link = document.createElement("a");

                link.setAttribute("href", encodedUri);
                link.setAttribute("download", "data.json");
                document.body.appendChild(link);
                link.click();
            });
        };
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/javascript")
            .POST(HttpRequest.BodyPublishers.ofString(javascriptCode))
            .build();

        try {
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());

            try (InputStream in = response.body();
                FileOutputStream fileOut = new FileOutputStream("data.json")) {
                in.transferTo(fileOut);
                System.out.println("File saved as data.json");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/download?token={TOKEN}";

        string javascriptCode = @"
        export default async function ({ page }) {
            await page.evaluate(() => {
                const json = {
                    ping: 'pong',
                    rnd: [...Array(5)].map(() => Math.random())
                };
                const jsonContent = `data:application/json,${JSON.stringify(json)}`;
                const encodedUri = encodeURI(jsonContent);
                const link = document.createElement('a');

                link.setAttribute('href', encodedUri);
                link.setAttribute('download', 'data.json');
                document.body.appendChild(link);
                link.click();
            });
        };";

        using var client = new HttpClient();
        var content = new StringContent(javascriptCode, Encoding.UTF8, "application/javascript");

        try
        {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            using var stream = await response.Content.ReadAsStreamAsync();

            using var fileStream = new FileStream("data.json", FileMode.Create, FileAccess.Write);
            await stream.CopyToAsync(fileStream);

            Console.WriteLine("File saved as data.json");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

This API is sensitive to the downloaded file and will return an appropriate `Content-Type` with the response.

## Import libraries [​](https://docs.browserless.io/rest-apis/download\#import-libraries "Direct link to Import libraries")

Both the `/function` and the `/download` API environments use [Ecmascript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules). This means you can use `import` syntax over HTTP. For instance, let's try leading the [Fake](https://fakerjs.dev/) module.

**JS Code**

```codeBlockLines_p187
import { faker } from "https://esm.sh/@faker-js/faker";

export default async function ({ page }) {
  const rndName = faker.person.fullName();
  const rndEmail = faker.internet.email();

  await page.evaluate(
    (name, email) => {
      const jsonStr = JSON.stringify({ name, email });
      const jsonContent = `data:application/json,${jsonStr}`;
      const encodedUri = encodeURI(jsonContent);
      const link = document.createElement("a");

      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "data.json");
      document.body.appendChild(link);
      return link.click();
    },
    rndName,
    rndEmail
  );
}

```

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl -X POST \
  https://production-sfo.browserless.io/download?token=YOUR_API_TOKEN_HERE \
  -H 'Content-Type: application/javascript' \
  -d 'import { faker } from '\''https://esm.sh/@faker-js/faker'\'';

export default async function ({ page }) {
  const rndName = faker.person.fullName();
  const rndEmail = faker.internet.email();

  await page.evaluate((name, email) => {
    const jsonStr = JSON.stringify({name, email});
    const jsonContent = `data:application/json,${jsonStr}`;
    const encodedUri = encodeURI(jsonContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "data.json");
    document.body.appendChild(link);
    return link.click();
  }, rndName, rndEmail);
}'

```

```codeBlockLines_p187
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/download?token=${TOKEN}`;
const headers = {
  "Content-Type": "application/javascript"
};

const data = `
import { faker } from 'https://esm.sh/@faker-js/faker';

export default async function ({ page }) {
  const rndName = faker.person.fullName();
  const rndEmail = faker.internet.email();

  await page.evaluate((name, email) => {
    const jsonStr = JSON.stringify({ name, email });
    const jsonContent = \`data:application/json,\${jsonStr}\`;
    const encodedUri = encodeURI(jsonContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "data.json");
    document.body.appendChild(link);
    link.click();
  }, rndName, rndEmail);
};
`;

const downloadFile = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: data
  });

  const buffer = await response.arrayBuffer();
  await writeFile("data.json", Buffer.from(buffer));
  console.log("File saved as data.json");
};

downloadFile();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/download?token={TOKEN}"
headers = {
    "Content-Type": "application/javascript"
}

data = """
import { faker } from 'https://esm.sh/@faker-js/faker';

export default async function ({ page }) {
  const rndName = faker.person.fullName();
  const rndEmail = faker.internet.email();

  await page.evaluate((name, email) => {
    const jsonStr = JSON.stringify({ name, email });
    const jsonContent = `data:application/json,${jsonStr}`;
    const encodedUri = encodeURI(jsonContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "data.json");
    document.body.appendChild(link);
    link.click();
  }, rndName, rndEmail);
};
"""

response = requests.post(url, headers=headers, data=data)

with open("data.json", "wb") as file:
    file.write(response.content)

print("File saved as data.json")

```

```codeBlockLines_p187
import java.io.*;
import java.net.*;
import java.net.http.*;

public class DownloadJsonFileWithFaker {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/download?token=" + TOKEN;

        String javascriptCode = """
        import { faker } from 'https://esm.sh/@faker-js/faker';

        export default async function ({ page }) {
            const rndName = faker.person.fullName();
            const rndEmail = faker.internet.email();

            await page.evaluate((name, email) => {
                const jsonStr = JSON.stringify({ name, email });
                const jsonContent = `data:application/json,${jsonStr}`;
                const encodedUri = encodeURI(jsonContent);
                const link = document.createElement("a");

                link.setAttribute("href", encodedUri);
                link.setAttribute("download", "data.json");
                document.body.appendChild(link);
                link.click();
            }, rndName, rndEmail);
        };
        """;

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .header("Content-Type", "application/javascript")
            .POST(HttpRequest.BodyPublishers.ofString(javascriptCode))
            .build();

        try {
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());

            try (InputStream in = response.body();
                 FileOutputStream fileOut = new FileOutputStream("data.json")) {
                in.transferTo(fileOut);
                System.out.println("File saved as data.json");
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
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/download?token={TOKEN}";

        string javascriptCode = @"
          import { faker } from 'https://esm.sh/@faker-js/faker';

          export default async function ({ page }) {
              const rndName = faker.person.fullName();
              const rndEmail = faker.internet.email();

              await page.evaluate((name, email) => {
                  const jsonStr = JSON.stringify({ name, email });
                  const jsonContent = `data:application/json,${jsonStr}`;
                  const encodedUri = encodeURI(jsonContent);
                  const link = document.createElement('a');

                  link.setAttribute('href', encodedUri);
                  link.setAttribute('download', 'data.json');
                  document.body.appendChild(link);
                  link.click();
              }, rndName, rndEmail);
          };";

        using var client = new HttpClient();
        var content = new StringContent(javascriptCode, Encoding.UTF8, "application/javascript");

        try
        {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            using var stream = await response.Content.ReadAsStreamAsync();
            using var fileStream = new FileStream("data.json", FileMode.Create, FileAccess.Write);
            await stream.CopyToAsync(fileStream);

            Console.WriteLine("File saved as data.json");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

**Example response**

```codeBlockLines_p187
{
  "name": "Jasmine Littel",
  "email": "Giovanna26@hotmail.com"
}

```

## JSON API [​](https://docs.browserless.io/rest-apis/download\#json-api "Direct link to JSON API")

You can also use the /download API sending a JSON payload. You must send an object with the following values:

- `code`: String, required — custom download code.
- `context`: Object, optional — value used to pass context values and arguments to the `code`

### Example [​](https://docs.browserless.io/rest-apis/download\#example "Direct link to Example")

**JS Code**

```codeBlockLines_p187
export default async function ({ page, context }) {
  await page.evaluate((context) => {
    const json = {
      url: context.url,
      ping: "pong",
      rnd: [...Array(context.arrayLen)].map(() => Math.random()),
    };
    const jsonContent = `data:application/json,${JSON.stringify(json)}`;
    const encodedUri = encodeURI(jsonContent);
    const link = document.createElement("a");

    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "data.json");
    document.body.appendChild(link);
    return link.click();
  }, context);
}

```

- cURL
- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
curl --request POST \
  --url 'https://production-sfo.browserless.io/download?token=YOUR_API_TOKEN_HERE' \
  --header 'Content-Type: application/json' \
  # Minified code
  --data '{
  "code": "export default async function({page:t,context:a}){await t.evaluate(t=>{let a={url:t.url,ping:`pong`,rnd:[...Array(t.arrayLen)].map(()=>Math.random())},e=`data:application/json,${JSON.stringify(a)}`,n=encodeURI(e),r=document.createElement(`a`);return r.setAttribute(`href`,n),r.setAttribute(`download`,`data.json`),document.body.appendChild(r),r.click()},a)};",
  "context": {
    "url": "https://browserless.io/",
    "arrayLen": 10
  }
}''

```

```codeBlockLines_p187
import { writeFile } from 'fs/promises';

const TOKEN = "YOUR_API_TOKEN_HERE";
const url = `https://production-sfo.browserless.io/download?token=${TOKEN}`;
const headers = {
  'Content-Type': 'application/json'
};

// Minified code
const data = {
  code: "export default async function({page:t,context:a}){await t.evaluate(t=>{let a={url:t.url,ping:`pong`,rnd:[...Array(t.arrayLen)].map(()=>Math.random())},e=`data:application/json,${JSON.stringify(a)}`,n=encodeURI(e),r=document.createElement(`a`);return r.setAttribute(`href`,n),r.setAttribute(`download`,`data.json`),document.body.appendChild(r),r.click()},a)};",
  context: {
    url: "https://browserless.io/",
    arrayLen: 10
  }
};

const downloadFile = async () => {
  const response = await fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data)
  });

  const buffer = await response.arrayBuffer();
  await writeFile("data.json", Buffer.from(buffer));
  console.log("File saved as data.json");
};

downloadFile();

```

```codeBlockLines_p187
import requests

TOKEN = "YOUR_API_TOKEN_HERE"
url = f"https://production-sfo.browserless.io/download?token={TOKEN}"
headers = {
    'Content-Type': 'application/json'
}

# Minified code
data = {
    "code": "export default async function({page:t,context:a}){await t.evaluate(t=>{let a={url:t.url,ping:`pong`,rnd:[...Array(t.arrayLen)].map(()=>Math.random())},e=`data:application/json,${JSON.stringify(a)}`,n=encodeURI(e),r=document.createElement(`a`);return r.setAttribute(`href`,n),r.setAttribute(`download`,`data.json`),document.body.appendChild(r),r.click()},a)};",
    "context": {
        "url": "https://browserless.io/",
        "arrayLen": 10
    }
}

response = requests.post(url, headers=headers, json=data)

with open("data.json", "wb") as file:
    file.write(response.content)

print("File saved as data.json")

```

```codeBlockLines_p187
import java.io.*;
import java.net.http.*;
import java.net.URI;

public class DownloadJsonFileWithMinifiedCode {
    public static void main(String[] args) {
        String TOKEN = "YOUR_API_TOKEN_HERE";
        String url = "https://production-sfo.browserless.io/download?token=" + TOKEN;

        String jsonData = """
        {
            "code": "export default async function({page:t,context:a}){await t.evaluate(t=>{let a={url:t.url,ping:`pong`,rnd:[...Array(t.arrayLen)].map(()=>Math.random())},e=`data:application/json,${JSON.stringify(a)}`,n=encodeURI(e),r=document.createElement(`a`);return r.setAttribute(`href`,n),r.setAttribute(`download`,`data.json`),document.body.appendChild(r),r.click()},a)};",
            "context": {
                "url": "https://browserless.io/",
                "arrayLen": 10
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
            HttpResponse<InputStream> response = client.send(request, HttpResponse.BodyHandlers.ofInputStream());

            try (InputStream in = response.body();
                 FileOutputStream fileOut = new FileOutputStream("data.json")) {
                in.transferTo(fileOut);
                System.out.println("File saved as data.json");
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
using System.Threading.Tasks;

class Program {
    static async Task Main(string[] args) {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string url = $"https://production-sfo.browserless.io/download?token={TOKEN}";

        string jsonData = @"
        {
            ""code"": ""export default async function({page:t,context:a}){await t.evaluate(t=>{let a={url:t.url,ping:`pong`,rnd:[...Array(t.arrayLen)].map(()=>Math.random())},e=`data:application/json,${JSON.stringify(a)}`,n=encodeURI(e),r=document.createElement(`a`);return r.setAttribute(`href`,n),r.setAttribute(`download`,`data.json`),document.body.appendChild(r),r.click()},a)};"",
            ""context"": {
                ""url"": ""https://browserless.io/"",
                ""arrayLen"": 10
            }
        }
        ";

        using var client = new HttpClient();
        var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

        try {
            var response = await client.PostAsync(url, content);
            response.EnsureSuccessStatusCode();

            using var stream = await response.Content.ReadAsStreamAsync();
            using var fileStream = new FileStream("data.json", FileMode.Create, FileAccess.Write);
            await stream.CopyToAsync(fileStream);

            Console.WriteLine("File saved as data.json");
        } catch (Exception ex) {
            Console.WriteLine("Error: " + ex.Message);
        }
    }
}

```

- [Basic Usage](https://docs.browserless.io/rest-apis/download#basic-usage)
- [Import libraries](https://docs.browserless.io/rest-apis/download#import-libraries)
- [JSON API](https://docs.browserless.io/rest-apis/download#json-api)
  - [Example](https://docs.browserless.io/rest-apis/download#example)