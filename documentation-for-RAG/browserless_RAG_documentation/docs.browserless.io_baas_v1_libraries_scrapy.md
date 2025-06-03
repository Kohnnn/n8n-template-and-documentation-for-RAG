---
url: "https://docs.browserless.io/baas/v1/libraries/scrapy"
title: "Scrapy (Python) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/scrapy#__docusaurus_skipToContent_fallback)

Version: v1

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/libraries/scrapy) or [BrowserQL](https://docs.browserless.io/browserql/start).

You can use Scrapy alongside [our `/content` API](https://docs.browserless.io/baas/v1/apis/content) to scrape data. All you need to do is use the start\_requests() method to make a query to the `/content` API, while keeping your scraping code the same.

Since Scrapy uses HTTP requests to just download the HTML page and build a DOM-like abstraction to be scrapped, **it can only return the initial render of a page without interacting with it**. On the other hand, the `/content` API asure the HTML content is not just downloaded, but rendered and evaluated inside a browser.

All you need to do is implement the `start_requests()` method to make a query to the `/content` API, while keeping your scraping code the same.

```codeBlockLines_p187
import json
import scrapy

class PptrDocsSpider(scrapy.Spider):
    name = "pptr-docs"

    def start_requests (self):
        options = {
            "url": "https://puppeteer.github.io/pptr.dev/",
            "gotoOptions": { "waitUntil": "networkidle0" }
        }

        yield scrapy.Request(
            url="https://chrome.browserless.io/content?token=YOUR_API_TOKEN_HERE",
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

You can use [all the options available in the `/content` API](https://chrome.browserless.io/docs/#/Browser%20API/post_content), use stealth mode, our residential proxies and more! For more reference, please see this [blogpost](https://www.browserless.io/blog/2024/02/15/scrapy-headless/).