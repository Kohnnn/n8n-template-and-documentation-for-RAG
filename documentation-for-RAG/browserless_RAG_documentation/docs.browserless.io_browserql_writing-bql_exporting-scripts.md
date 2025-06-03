---
url: "https://docs.browserless.io/browserql/writing-bql/exporting-scripts"
title: "Exporting Scripts | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/writing-bql/exporting-scripts#__docusaurus_skipToContent_fallback)

On this page

BrowserQL IDE allows you to export any of your queries into different languages. This feature makes your life easier when integrating our functionalities into your scraping application. This allows you to try and test your queries in our IDE, and quickly move a working one into your code.

## Example [​](https://docs.browserless.io/browserql/writing-bql/exporting-scripts\#example "Direct link to Example")

In this example, the BQL query will navigate to [https://news.ycombinator.com/](https://news.ycombinator.com/), click on the Jobs tab, and extract the HTML from the page:

- BQL Query
- Export Query as Code

```codeBlockLines_p187
mutation ExtractJobsHTML {
  goto(url: "https://news.ycombinator.com", waitUntil: firstMeaningfulPaint) {
    status
  }

  click(selector: "span.pagetop > a[href='jobs']") {
    x
    y
  }

  html {
    html
  }
}

```

- Javascript
- Python
- Java

```codeBlockLines_p187
const url = 'https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE';
const options = {
  method: 'POST',
  body: '{"query":"mutation ExtractJobsHTML {\n  goto(url: \"https://news.ycombinator.com\", waitUntil: firstMeaningfulPaint) {\n    status\n  }\n  \n  click(selector: \"span.pagetop > a[href=\'jobs\']\") {\n    x\n    y\n  }\n  \n  html {\n    html\n  }\n}","variables":null,"operationName":"ExtractJobsHTML"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}

```

```codeBlockLines_p187
import http.client

conn = http.client.HTTPSConnection("production-sfo.browserless.io")

payload = "{\"query\":\"mutation ExtractJobsHTML {\\n  goto(url: \\\"https://news.ycombinator.com\\\", waitUntil: firstMeaningfulPaint) {\\n    status\\n  }\\n  \\n  click(selector: \\\"span.pagetop > a[href='jobs']\\\") {\\n    x\\n    y\\n  }\\n  \\n  html {\\n    html\\n  }\\n}\",\"variables\":null,\"operationName\":\"ExtractJobsHTML\"}"

conn.request("POST", "/chromium/bql?token=YOUR_API_TOKEN_HERE", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

```

```codeBlockLines_p187
HttpResponse<String> response = Unirest.post("https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE")
.body("{\"query\":\"mutation ExtractJobsHTML {\\n  goto(url: \\\"https://news.ycombinator.com\\\", waitUntil: firstMeaningfulPaint) {\\n    status\\n  }\\n  \\n  click(selector: \\\"span.pagetop > a[href='jobs']\\\") {\\n    x\\n    y\\n  }\\n  \\n  html {\\n    html\\n  }\\n}\",\"variables\":null,\"operationName\":\"ExtractJobsHTML\"}")
.asString();

```

Now, using BrowserQL Editor to export this script in your preferred coding language to integrate it with a application that reads the HTML and extracts the title and link from it, creating an array with this information.

BrowserQL API

Find out how to export your queries and integrate it in your code by [calling the BrowserQL API](https://docs.browserless.io/browserql/using-the-ide/using-api-calls).

- Javascript
- Python
- Java

```codeBlockLines_p187
const { JSDOM } = require("jsdom");

async function ExtractJobsHTML() {
    const url = "https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE";
    const options = {
      method: 'POST',
      body: '{"query":"mutation ExtractJobsHTML {\n  goto(url: \"https://news.ycombinator.com\", waitUntil: firstMeaningfulPaint) {\n    status\n  }\n  \n  click(selector: \"span.pagetop > a[href=\'jobs\']\") {\n    x\n    y\n  }\n  \n  html {\n    html\n  }\n}","variables":null,"operationName":"ExtractJobsHTML"}'
    };

    let response;

    try {
      response = await fetch(url, options);
    } catch (error) {
      console.error(error);
    }

    const json = await response.json();
    const html = json.data.html.html;

    const dom = new JSDOM(html);
    const document = dom.window.document;
    const rows = document.querySelectorAll("tr.athing");

    const titlesAndLinks = [];
    rows.forEach((row) => {
        const anchor = row.querySelector("a");
        if (anchor) {
            titlesAndLinks.push({
                title: anchor.textContent.trim(),
                link: anchor.href.trim(),
            });
        }
    });

    console.log(titlesAndLinks);
}

ExtractJobsHTML();

```

```codeBlockLines_p187
import http.client
from bs4 import BeautifulSoup
import json

conn = http.client.HTTPSConnection("production-sfo.browserless.io")

payload = '{"query":"mutation ExtractJobsHTML {\\n  goto(url: \\"https://news.ycombinator.com\\", waitUntil: firstMeaningfulPaint) {\\n    status\\n  }\\n  \\n  click(selector: \\"span.pagetop > a[href=\'jobs\']\\") {\\n    x\\n    y\\n  }\\n  \\n  html {\\n    html\\n  }\\n}","variables":null,"operationName":"ExtractJobsHTML"}'

headers = {"Content-Type": "application/json"}

conn.request(
    "POST",
    "/chromium/bql?token=YOUR_API_TOKEN_HERE",
    payload,
    headers,
)

res = conn.getresponse()
response = res.read()

response_json = json.loads(response.decode("utf-8"))

html = response_json["data"]["html"]["html"]

soup = BeautifulSoup(html, "html.parser")

titles_and_links = []

for job in soup.find_all("tr", class_="athing"):
    title_tag = job.find("a")
    if title_tag:
        titles_and_links.append(
            {"title": title_tag.text.strip(), "link": title_tag["href"].strip()}
        )

print(titles_and_links)

```

```codeBlockLines_p187
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class ExtractJobsHTML {
    public static void main(String[] args) throws Exception {
        HttpResponse<String> response = Unirest.post("https://production-sfo.browserless.io/chromium/bql?token=YOUR_API_TOKEN_HERE")
            .body("{\"query\":\"mutation ExtractJobsHTML {\\n  goto(url: \\\"https://news.ycombinator.com\\\", waitUntil: firstMeaningfulPaint) {\\n    status\\n  }\\n  \\n  click(selector: \\\"span.pagetop > a[href='jobs']\\\") {\\n    x\\n    y\\n  }\\n  \\n  html {\\n    html\\n  }\\n}\",\"variables\":null,\"operationName\":\"ExtractJobsHTML\"}")
            .asString();

        // Parse JSON response
        JsonObject jsonResponse = JsonParser.parseString(response.getBody()).getAsJsonObject();
        String html = jsonResponse.getAsJsonObject("data").getAsJsonObject("html").get("html").getAsString();

        // Parse HTML with Jsoup
        Document doc = Jsoup.parse(html);
        Elements jobs = doc.select("tr.athing");

        for (Element job : jobs) {
            Element titleTag = job.selectFirst("a");
            if (titleTag != null) {
                System.out.println("Title: " + titleTag.text());
                System.out.println("Link: " + titleTag.attr("href"));
            }
        }
    }
}

```

- [Example](https://docs.browserless.io/browserql/writing-bql/exporting-scripts#example)