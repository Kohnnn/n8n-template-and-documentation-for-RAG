---
url: "https://docs.browserless.io/baas/libraries/scrapy"
title: "Scrapy (Python) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/libraries/scrapy#__docusaurus_skipToContent_fallback)

Version: v2

On this page

You can use Scrapy alongside our [/content API](https://docs.browserless.io/rest-apis/content) or [BrowserQL](https://docs.browserless.io/browserql/start) to scrape data. All you need to do is use the `start_requests()` method to make a query to the `/content` or BrowserQL, while keeping your scraping code the same.

## Basic Usage [​](https://docs.browserless.io/baas/libraries/scrapy\#basic-usage "Direct link to Basic Usage")

Since Scrapy uses HTTP requests to just download the HTML page and build a DOM-like abstraction to be scrapped, **it can only return the initial render of a page without interacting with it**. On the other hand, the `/content` API asure the HTML content is not just downloaded, but rendered and evaluated inside a browser, while BrowserQL uses advanced stealth techniques to bypass bot detectors before rendering a page.

All you need to do is implement the `start_requests()` method to make a query to the `/content` API, while keeping your scraping code the same.

```codeBlockLines_p187
import json
import scrapy

class PptrDocsSpider(scrapy.Spider):
    name = "pptr-docs"

    def start_requests (self):
        options = {
            "url": "https://puppeteer.github.io/pptr.dev/",
            "waitForTimeout": 5000
        }

        yield scrapy.Request(
            url="https://production-sfo.browserless.io/content?token=YOUR_API_TOKEN_HERE",
            method='POST',
            dont_filter=True,
            headers={"Content-Type": "application/json"},
            body=json.dumps(options)
        )

    def parse(self, response):
        entries = response.css('sidebar-component a.pptr-sidebar-item')
        for entry in entries:
            yield{
                'title' : entry.css('::text').get(),
                'url' : entry.css('::attr(href)').get(),
            }

```

You can use [all the options available in the `/content` API](https://docs.browserless.io/rest-apis/content), use stealth mode, our residential proxies and more! For more reference, please see this [blogpost](https://www.browserless.io/blog/2024/02/15/scrapy-headless/).

## Bypass bot-blockers using `/unblock` [​](https://docs.browserless.io/baas/libraries/scrapy\#bypass-bot-blockers-using-unblock "Direct link to bypass-bot-blockers-using-unblock")

In cases where websites implement aggressive bot-detection mechanisms, you can use the `/unblock` API to bypass these. The `/unblock` API uses a variety of tools and strategies to override and hide the footprints that headless browsers leave behind, allowing you to access bot-protected websites from a remote interface.

Similar to the `/content` API, the `/unblock` API renders and evaluates the page in a browser, but with extra stealth features. This makes it ideal for scraping highly protected websites.

You want to make the `/unblock` request yeilding the `scrapy.Request()` method, and **extracting the html content from the JSON in the `parse()` method**. Here's an example:

```codeBlockLines_p187
import json
import scrapy

class PptrDocsSpider(scrapy.Spider):
    name = "pptr-docs"

    def start_requests (self):
        options = {
            "url": "https://puppeteer.github.io/pptr.dev/",
            "waitForTimeout": 5000
        }

        yield scrapy.Request(
            url="https://production-sfo.browserless.io/unblock?token=YOUR_API_TOKEN_HERE",
            method='POST',
            dont_filter=True,
            headers={"Content-Type": "application/json"},
            body=json.dumps(options)
        )

    def parse(self, response):
        # Extracts the content from the response
        html_content = json.loads(response.text)['content']
        dom = scrapy.Selector(text=html_content)

        # Continue as normal
        entries = dom.css('sidebar-component a.pptr-sidebar-item')
        for entry in entries:
            yield{
                'title' : entry.css('::text').get(),
                'url' : entry.css('::attr(href)').get(),
            }

```

- [Basic Usage](https://docs.browserless.io/baas/libraries/scrapy#basic-usage)
- [Bypass bot-blockers using `/unblock`](https://docs.browserless.io/baas/libraries/scrapy#bypass-bot-blockers-using-unblock)