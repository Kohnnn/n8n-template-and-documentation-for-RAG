---
url: "https://docs.browserless.io/baas/libraries/beautifulsoup"
title: "Beautiful Soup (Python) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/libraries/beautifulsoup#__docusaurus_skipToContent_fallback)

Version: v2

On this page

Beautiful Soup is one the most popular scrapping libraries. It allows you to use Python to easily parse an existing HTML string to scrape its data in an easy and fast manner. You can use Beautiful Soup alongside our [/content](https://docs.browserless.io/rest-apis/content) or [BrowserQL](https://docs.browserless.io/browserql/start) to scrape any website.

Both of these APIs will render the content in a browser before HTML, with the difference that BrowserQL uses advanced stealth techniques to first bypass bot detectors.

## Basic Usage [​](https://docs.browserless.io/baas/libraries/beautifulsoup\#basic-usage "Direct link to Basic Usage")

Just like [Cheerio](https://www.npmjs.com/package/cheerio), Beautiful Soup is _only_ a parser, it does not provide any API to _get_ the HTML string in the first place. Usually, to get the HTML string from a website, you would use the `requests` library to download the page, like this:

```codeBlockLines_p187
import requests
from bs4 import BeautifulSoup

url = 'https://browserless.io/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
entries = soup.find_all('a')

for entry in entries:
    print(entry.text.strip())

```

Here's the main problem: since `requests` just downloads the HTML, **it can only return the _source code_ of a page without interacting with it**. Which means that any page that relies on JavaScript and user interactions to render content, will not be downloaded properly.

On the other hand, the `/content` API ensures that the HTML content is not just downloaded, but rendered and evaluated inside a browser. You can use the `requests` library to make an HTTP request to our api, this way:

```codeBlockLines_p187
import requests
from bs4 import BeautifulSoup

response = requests.post("https://production-sfo.browserless.io/content",
    params={ "token": "YOUR_API_TOKEN_HERE"},
    json={
        "waitForTimeout": 5000,
        "url": "https://puppeteer.github.io/pptr.dev/"
    }
)

soup = BeautifulSoup(response.text, 'html.parser')
entries = soup.find_all("a", class_="pptr-sidebar-item")

for entry in entries:
    print(entry.text.strip())

```

In the example, we are using the [old Puppeteer doc site](https://puppeteer.github.io/pptr.dev/), which relies heavily on JS to render its content. With a usual `requests` or `cURL` request, it would only download the page's source code, the JavaScript wouldn't be interpreted and the content wouldn't be rendered.

Using our API, you can use [all the options available in the `/content` API](https://docs.browserless.io/rest-apis/content), use stealth mode, our residential proxies and more! For more reference, please check our [OpenAPI](https://docs.browserless.io/open-api/#tag/Browser-REST-APIs/paths/~1chrome~1content/post).

## Bypass bot-blockers using `/unblock` [​](https://docs.browserless.io/baas/libraries/beautifulsoup\#bypass-bot-blockers-using-unblock "Direct link to bypass-bot-blockers-using-unblock")

In cases where websites implement aggressive bot-detection mechanisms, you can use the `/unblock` API to bypass these. The `/unblock` API uses a variety of tools and strategies to override and hide the footprints that headless browsers leave behind, allowing you to access bot-protected websites from a remote interface.

Similar to the `/content` API, the `/unblock` API renders and evaluates the page in a browser, but with extra stealth features. This makes it ideal for scraping highly protected websites.

```codeBlockLines_p187
import json
import requests
from bs4 import BeautifulSoup

response = requests.post("https://production-sfo.browserless.io/unblock",
    params={ "token": "YOUR_API_TOKEN_HERE"},
    json={
        "waitForTimeout": 5000,
        "url": "https://puppeteer.github.io/pptr.dev/"
    }
)

html_content = json.loads(response.text)['content']
soup = BeautifulSoup(html_content, 'html.parser')

entries = soup.find_all("a", class_="pptr-sidebar-item")
for entry in entries:
    print(entry.text.strip())

```

- [Basic Usage](https://docs.browserless.io/baas/libraries/beautifulsoup#basic-usage)
- [Bypass bot-blockers using `/unblock`](https://docs.browserless.io/baas/libraries/beautifulsoup#bypass-bot-blockers-using-unblock)