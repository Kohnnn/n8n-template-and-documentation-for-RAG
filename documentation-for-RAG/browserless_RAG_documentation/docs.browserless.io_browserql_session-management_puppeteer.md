---
url: "https://docs.browserless.io/browserql/session-management/puppeteer"
title: "Puppeteer | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/session-management/puppeteer#__docusaurus_skipToContent_fallback)

On this page

If you're already using Puppeteer working with WebSockets, you can still mix-and-match BrowserQL in your scripts. This is perfect for getting past a nasty bot blockage and then connecting your existing scripts back.

Reconnecting with More BQL

You can also run _more_ BrowserQL at a later time by doing the same process this guide will teach you. Refer to the [Reconnecting with More BQL](https://docs.browserless.io/browserql/writing-bql/reconnecting-bql) guide for more details.

## Using Reconnect [​](https://docs.browserless.io/browserql/session-management/puppeteer\#using-reconnect "Direct link to Using Reconnect")

With BQL, you'll navigate to the desired page, do the actions you require, like verifying or solving a captcha, and finally, use the [`reconnect`](https://docs.browserless.io/bql-schema/operations/mutations/reconnect) mutation to retrieve a websocket endpoint. This endpoint will be your entry point when starting your Puppeteer connection.

Using the [https://example.com/](https://example.com/) page, you can run the following BrowserQL query then ask for a connection back:

Reconnect Timeout

The `reconnect` mutation has a `timeout` argument, which is a limit (in milliseconds) for how long the browser should be available before it gets shutdown when nothing connects to it. If a connection were to happen after this time, a semantic `404` is returned back. When a connection happens, this will clear the timer and the session can continue past this limit.

```codeBlockLines_p187
mutation Reconnect {
  goto(url: "https://example.com/", waitUntil: networkIdle) {
    status
  }

  reconnect (timeout: 30000) {
    browserWSEndpoint
  }
}

```

## Connecting with Puppeteer [​](https://docs.browserless.io/browserql/session-management/puppeteer\#connecting-with-puppeteer "Direct link to Connecting with Puppeteer")

Now, you need to integrate the BQL query above into your Puppeteer code. You can use BrowserQL Editor's Export Query as Code to translate any query into multiple code languages, like Javascript.

- Learn how to [Export Query as Code](https://docs.browserless.io/browserql/writing-bql/exporting-scripts).
- See the [Available programming languages](https://docs.browserless.io/browserql/using-the-ide/ide-features#query-as-code).

With the query turned into JS code, you can integrate the code into your script. The example below uses the `browserWSEndpoint` to make a connection with Puppeteer, and takes a screenshot of the webpage:

```codeBlockLines_p187
import puppeteer from 'puppeteer-core';

const url = 'https://example.com';
const token = 'YOUR_API_TOKEN_HERE';
const timeout = 5 * 60 * 1000;

const queryParams = new URLSearchParams({
  timeout,
  token,
}).toString();

const query = `
  mutation Reconnect($url: String!) {
    goto(url: $url, waitUntil: networkIdle) {
      status
    }
    reconnect(timeout: 30000) {
      browserWSEndpoint
    }
  }
`;

const variables = { url };

const endpoint = `https://production-sfo.browserless.io/chromium/bql?${queryParams}`;

const options = {
  method: 'POST',
  headers: {
    'content-type': 'application/json'
  },
  body: JSON.stringify({
    query,
    variables,
  }),
};

try {
  console.log(`Running BQL Query: ${url}`);

  const response = await fetch(endpoint, options);

  if (!response.ok) {
    throw new Error(`Got non-ok response:\n` + (await response.text()));
  }

  const { data } = await response.json();
  const browserWSEndpoint = data.reconnect.browserWSEndpoint
  console.log(`Got OK response! Connecting puppeteer to ${browserWSEndpoint}`);
  const browser = await puppeteer.connect({
    browserWSEndpoint,
  });
  console.log(`Connected to ${await browser.version()}`);
  const pages = await browser.pages();
  const page = pages.find((p) => p.url().includes(url));
  await page.screenshot({ fullPage: true, path: 'temp.png' });
  await browser.close();
} catch (error) {
  console.error(error);
}

```

- [Using Reconnect](https://docs.browserless.io/browserql/session-management/puppeteer#using-reconnect)
- [Connecting with Puppeteer](https://docs.browserless.io/browserql/session-management/puppeteer#connecting-with-puppeteer)