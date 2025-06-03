---
url: "https://docs.browserless.io/baas/v1/apis/scrape"
title: "/scrape API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/scrape#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/scrape) or [BrowserQL](https://docs.browserless.io/browserql/start).

The scrape API allows for getting the contents a page, by specifying selectors you are interested in, and returning a structured JSON response. We also allow for setting a timeout option for asynchronously added elements.

The default behavior is to navigate to the URL specified, wait for the page to load (including parsing and executing of JavaScript), then waiting for the elements for a maximum of 30 seconds. All of these are configurable, and documented in detail below.

At a minimum you'll need to specify at least a `url` and an `elements` array.

Check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Browser%20API/post_scrape).

## Basic Usage [​](https://docs.browserless.io/baas/v1/apis/scrape\#basic-usage "Direct link to Basic Usage")

Below is the most basic usage, where we'll navigate to the example.com website (waiting for page-load) and parse out all `a` elements.

Internally we use `document.querySelectorAll` to retrieve all matches on a page. Using a more specific selector can narrow down the returned results.

**Get the a elements on example.com**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "a"\
    }\
  ]
}

```

**cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/scrape?token=MY_API_TOKEN \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://example.com/",
  "elements": [{\
      "selector": "a"\
  }]
}'

```

Once ran, this will return a JSON payload of the following. We return the `innerHTML` and `innerText` of all matched selectors, as well as all their `attributes`. In the case of the above call, this will return:

```codeBlockLines_p187
{
  "data": [\
    {\
      "selector": "a",\
      "results": [\
        {\
          "html": "More information...",\
          "text": "More information...",\
          "attributes": [\
            {\
              "name": "href",\
              "value": "https://www.iana.org/domains/example"\
            }\
          ]\
        }\
      ]\
    }\
  ]
}

```

## Specifying page-load behavior [​](https://docs.browserless.io/baas/v1/apis/scrape\#specifying-page-load-behavior "Direct link to Specifying page-load behavior")

The scrape API allows for setting specific page-load behaviors by setting a `gotoOptions` in the JSON body. This is passed directly into [puppeteer's `goto()` method](https://pptr.dev/api/puppeteer.page.goto).

In the example below, we'll set a `waitUntil` property and a `timeout`

**Get the H1 elements on example.com with custom goto options**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "h1"\
    }\
  ],
  "gotoOptions": {
    "timeout": 10000,
    "waitUntil": "networkidle2"
  }
}

```

This will now force selectors to be collected _after_ the network has been idle for 2 seconds, and we'll timeout the request after 10 seconds.

## Custom behavior with `waitFor` [​](https://docs.browserless.io/baas/v1/apis/scrape\#custom-behavior-with-waitfor "Direct link to custom-behavior-with-waitfor")

Sometimes it's helpful to do further actions, or wait for custom events on the page before getting data. We allow this behavior with the `waitFor` property. We closely follow [puppeteer's `waitFor()` method](https://github.com/puppeteer/puppeteer/blob/7b768838023bcb79051f5d34c96949ef253ad9a2/docs/api.md#pagewaitforselectororfunctionortimeout-options-args).

This property can accept one of three options:

- A function to be ran within the page's context, inside of the browser.
- A `number` indicating the time in milliseconds to wait.
- A valid selector to wait for.

**Waiting for a selector**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "h1"\
    }\
  ],
  "waitFor": "h1"
}

```

**Waiting for 10 seconds**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "h1"\
    }\
  ],
  "waitFor": 10000
}

```

**Waiting for a function**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "h1"\
    }\
  ],
  "waitFor": "() => document.querySelector('h1')"
}

```

**Error handling**

We do catch and return errors for invalid functions inside of `waitFor`. For instance: `() => document.querySelector('h1'))` as a `waitFor` will return an HTTP code of `400` and the following text:

```codeBlockLines_p187
Evaluation failed: SyntaxError: Unexpected token ')'
at new Function (<anonymous>)
  at waitForPredicatePageFunction (__puppeteer_evaluation_script__:2:21)

```

## Cookies, headers and other options [​](https://docs.browserless.io/baas/v1/apis/scrape\#cookies-headers-and-other-options "Direct link to Cookies, headers and other options")

As with our other APIs, you can inject things like `cookies`, `headers` and other options, including intercepting requests and responses. These follow the pattern set by [puppeteer's `setCokkie()`](https://pptr.dev/15.3.0/api/puppeteer.page.setcookie) and [`setExtraHTTPHeaders()` methods](https://pptr.dev/15.3.0/api/puppeteer.page.setextrahttpheaders).

**Setting a special cookie**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "h1"\
    }\
  ],
  "cookies": [\
    {\
      "name": "my-special-cookie",\
      "value": "foo-bar",\
      "url": "https://www.example.com",\
      "path": "/",\
      "sameSite": "Strict"\
    }\
  ]
}

```

**Adding an authentication header**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "h1"\
    }\
  ],
  "setExtraHTTPHeaders": {
    "Authentication": "Basic foo-bar"
  }
}

```

**Intercepting requests**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "h1"\
    }\
  ],
  "rejectRequestPattern": ["png", "jpg"]
}

```

## Element timeouts [​](https://docs.browserless.io/baas/v1/apis/scrape\#element-timeouts "Direct link to Element timeouts")

browserless will wait for the elements specified for up to 30 seconds to be inserted in the page. This is useful for single-page applications that can load data on the fly. You can conditionally change this timer by specifying a `timeout` property per-element.

**Using a custom timeout of 10 seconds**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "h1",\
      "timeout": 10000\
    },\
    {\
      "selector": "a",\
      "timeout": 5000\
    }\
  ]
}

```

## Debugging [​](https://docs.browserless.io/baas/v1/apis/scrape\#debugging "Direct link to Debugging")

Without a doubt, one of the most frustrating aspects of scraping is debugging broken scripts. This is nothing new for browserless, and though we offer [excellent debugging tools](https://www.browserless.io/blog/2019/04/18/live-debugger/), we thought it'd be appropriate to add some extra information in the JSON response to help make debugging even easier.

As of today, we offer five payloads to help debug the page: `html`, `screenshot`, `console`, `cookies` and `network`. Each is listed below.

**HTML**: This is the raw HTML of the webpage, after all page-load and `waitFor` functions have ran.

**Screenshot**: A full-page JPEG of the page encoded in `base64`.

**Console**: An array of all the various `console` messages the page has written out.

**Cookies**: An array of objects specifying all the cookies currently set on the page.

**Network**: An object with two properties: `inbound` and `outbound`, representing the outgoing requests as well as their inbound responses.

In order to get this debugging information, you'll need to specify that you want it in your JSON POST payload. This is made optional due to the fact that generating these properties can take additional resources away from other concurrent work. You'll need to specify what fields you want, by adding a `debug` object and declaring what fields you want returned. Here's an example of getting all the fields back:

**Requesting all debug fields**

```codeBlockLines_p187
{
  "url": "https://example.com/",
  "elements": [\
    {\
      "selector": "h1",\
      "timeout": 10000\
    },\
    {\
      "selector": "a",\
      "timeout": 5000\
    }\
  ],
  "debug": {
    "screenshot": true,
    "console": true,
    "network": true,
    "cookies": true,
    "html": true
  }
}

```

- [Basic Usage](https://docs.browserless.io/baas/v1/apis/scrape#basic-usage)
- [Specifying page-load behavior](https://docs.browserless.io/baas/v1/apis/scrape#specifying-page-load-behavior)
- [Custom behavior with `waitFor`](https://docs.browserless.io/baas/v1/apis/scrape#custom-behavior-with-waitfor)
- [Cookies, headers and other options](https://docs.browserless.io/baas/v1/apis/scrape#cookies-headers-and-other-options)
- [Element timeouts](https://docs.browserless.io/baas/v1/apis/scrape#element-timeouts)
- [Debugging](https://docs.browserless.io/baas/v1/apis/scrape#debugging)