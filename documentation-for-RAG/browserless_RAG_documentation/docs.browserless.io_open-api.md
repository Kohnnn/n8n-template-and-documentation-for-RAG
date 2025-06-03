---
url: "https://docs.browserless.io/open-api"
title: "Browserless | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/open-api#__docusaurus_skipToContent_fallback)

![browserless logo](https://docs.browserless.io/docs/browserless-logo-inline.svg)

- Browserless.io
- Software Keys
  - Using a Software Key
- Using the Browserless Proxy
- The Browserless CDP API
  - Browserless.liveURL
  - Browserless.reconnect
  - Browserless.solveCaptcha
  - Browserless.foundCaptcha
  - Browserless.heartbeat
  - Browserless.pageId
- Changelog
- Browser REST APIs
  - post/chrome/content
  - post/chrome/download
  - post/chrome/function
  - get/json/list
  - put/json/new
  - get/json/protocol
  - get/json/version
  - post/chrome/pdf
  - post/chrome/performance
  - post/chrome/scrape
  - post/chrome/screenshot
  - post/chromium/content
  - post/chromium/download
  - post/chromium/function
  - post/chromium/pdf
  - post/chromium/performance
  - post/chromium/scrape
  - post/chromium/screenshot
  - post/edge/content
  - post/edge/download
  - post/edge/function
  - post/edge/pdf
  - post/edge/performance
  - post/edge/scrape
  - post/edge/screenshot
  - post/chrome/export
  - post/chrome/unblock
  - post/chromium/export
  - post/chromium/unblock
  - post/chrome/bql?(/\*)
  - post/chromium/bql?(/\*)
- Management REST APIs
  - get/active
  - get/kill/+(\[0-9a-zA-Z-\_\])
  - get/meta
  - get/
- Browser WebSocket APIs
  - get/devtools/browser/\*
  - get/chrome
  - get/devtools/page/\*
  - get/chrome/playwright
  - get/chromium
  - get/playwright/chromium
  - get/edge
  - get/edge/playwright
  - get/playwright/firefox
  - get/playwright/webkit
  - get/chrome/live/\*
  - get/chrome/stealth
  - get/chromium/live/\*
  - get/chromium/stealth
  - get/reconnect/\*

[API docs by Redocly](https://redocly.com/redoc/)

# Browserless (2.30.1)

Download OpenAPI specification: [Download](https://docs.browserless.io/redocusaurus/plugin-redoc-0.yaml)

## [section/Browserless.io](https://docs.browserless.io/open-api\#section/Browserless.io) Browserless.io

This service extends the Browserless open-source image with many features and enhancements for teams automating at scale. Notable features include:

- A Chrome-devtools-protocol based API for extending and enhancing libraries in a cross-language way.
- A new hybrid-automation toolkit with live session interactivity.
- Robust session management: connect, reconnect, kill and limit what a browser can do.
- Bleeding features like multiplexing numerous clients into a single Chrome process in an isolated way.
- The ability to upload and run custom extensions.
- Run multiple tokens, with access controls on each.
- Multi-browser with all the robust capabilities already in the open-source images.

There's a lot to cover here so let's get started!

## [section/Software-Keys](https://docs.browserless.io/open-api\#section/Software-Keys) Software Keys

The Enterprise image supports time-limited software keys that allow usage for a specific period without requiring any external connections or callbacks. These keys are cryptographically secure and cannot be reverse engineered. When a key expires, the container will exit with a semantic error code.

## [section/Software-Keys/Using-a-Software-Key](https://docs.browserless.io/open-api\#section/Software-Keys/Using-a-Software-Key) Using a Software Key

To use a software key, set the `KEY` environment variable when running the container:

```bash
docker run -e KEY=your-generated-key browserless/enterprise

```

## [section/Using-the-Browserless-Proxy](https://docs.browserless.io/open-api\#section/Using-the-Browserless-Proxy) Using the Browserless Proxy

> The Residential proxy is only available for Enterprise and Cloud plans.

Browserless comes with a built-in mechanism to proxy to what's called "residential" IPs. These are IP addresses are sourced from real-users running a proxy server on their home networking machines. Residential proxying is especially useful for things like bypassing certain bot blockages and more.

Using a residential proxy is as straightforward as adding a few parameters to your library or API calls. Here's the required parameters and the values they support:

- `?proxy=residential`: Specifies that you want to use the residential proxy for this request. Data-center coming soon.
- `?proxyCountry=us`: Specifies a country you wish to use for the request. A two-digit ISO code.
- `?proxySticky=true`: If you want to use the same IP address for the entirety of the session. Generally recommended for most cases.

Simply append these to your connection call, REST API calls, or any library call:

`wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN&proxy=residential&proxyCountry=us&proxySticky`

`https://production-sfo.browserless.io/chromium/unblock?token=YOUR-API-TOKEN&proxy=residential&proxyCountry=us&proxySticky`

Please do note that using a proxy will increase the amount of units consumed. Every megabyte of data transferred consumes 6 units.

## [section/The-Browserless-CDP-API](https://docs.browserless.io/open-api\#section/The-Browserless-CDP-API) The Browserless CDP API

In order to enhance the experience with open source libraries like Puppeteer, we decided to take a new approach to extending these libraries in a language-agnostic way. We call it the Browserless CDP API. Here's a quick list of what it can do:

- Generate and give back live URLs for hybrid automation.
- Solve Captchas.
- Return your page's unique identifier created by Chrome.
- Way more coming!

Since most libraries come with a way to issue "raw" CDP commands, it's an easy way to drop-in custom behaviors without having to write and maintain a library. Plus you can continue to enjoy using the same packages you've already come to know.

Getting started with this API is pretty simple. For instance, if you want to use the live viewer for a particular page, simply do the following:

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint = 'wss://production-sfo.browserless.io/chromium';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');
  const { liveURL } = await cdp.send('Browserless.liveURL');

  // liveURL = 'http://localhost:3000/live/?i=98e83bbfd396241a6963425b1feeba2f';
})();

```

You can then visit this URL in any browser to interact with the headless Chrome running someplace else.

See more below for a full list of the available APIs and features.

## [section/The-Browserless-CDP-API/Browserless.liveURL](https://docs.browserless.io/open-api\#section/The-Browserless-CDP-API/Browserless.liveURL) Browserless.liveURL

> This API is only available for Enterprise plans. [Contact us for more information here.](https://www.browserless.io/contact/)

Returns a fully-qualified URL to load into a web-browser. This URL allows for clicking, typing and other interactions with the underlying page. This URL doesn't require an authorization token, so you're free to share it externally with your own users or employees. If security is a concern, you can set a `timeout` parameter to limit the amount of time this URL is valid for. By default no `timeout` is set and the URL is good as long as the underlying browser is open.

Programmatic control of the session is also available, so you can close the live session once your code has detected a selector, network call, or whatever else. See the below example for programmatic control.

**Basic example**

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint =
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');
  const { liveURL } = await cdp.send('Browserless.liveURL');

  // liveURL = 'https://production-sfo.browserless.io/live/?i=98e83bbfd396241a6963425b1feeba2f';
})();

```

**Timeout example**

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint =
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');
  const { liveURL } = await cdp.send('Browserless.liveURL', {
    timeout: 10000, // 10 seconds to connect!
  });

  // liveURL = 'https://production-sfo.browserless.io/live/?i=98e83bbfd396241a6963425b1feeba2f';
})();

```

**Maintaining the width and height**

By default, Browserless will dynamically change the width and height of the browser to match an end-users screen. This isn't always ideal and can be disabled by setting a `resizable` value to `false`. When this is done, only your script can alter the width and height of the browser:

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint =
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();

  // Width and height will always be 1920x1080
  // and the Live URL will maintain this aspect ratio
  await page.setViewport({ width: 1920, height: 1080 });
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');
  const { liveURL } = await cdp.send('Browserless.liveURL', {
    resizable: false,
  });

  // liveURL = 'https://production-sfo.browserless.io/live/?i=98e83bbfd396241a6963425b1feeba2f';
})();

```

**Setting a Quality and Type**

Setting a "quality" and "type" effects the streamed quality of the live URL's client-side resolution. By default, Browserless sets these to quality: 100 and type of "png". You can experiment different settings to get an ideal resolutions while keep latency slow. The close to 100 quality is, the potential for higher perceived latency.

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint =
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');
  const { liveURL } = await cdp.send('Browserless.liveURL', {
    quality: 100, // Can be 1 - 100
    type: 'png', // Can be 'jpeg' or 'png'
  });

  // liveURL = 'https://production-sfo.browserless.io/live/?i=98e83bbfd396241a6963425b1feeba2f';
})();

```

It's also helpful to "wait" until the user is done doing what's needed. For that reason, Browserless will fire a custom event when the page is closed as well:

**Wait for close**

> Custom CDP Events are not supported in all libraries, including .NET Playwright.

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint =
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');

  const { liveURL } = await cdp.send('Browserless.liveURL');

  console.log(liveURL);

  // Wait for the Browserless.liveComplete event when the live page is closed.
  // Please not that not all libraries support custom CDP events.
  await new Promise((r) => cdp.on('Browserless.liveComplete', r));

  console.log('Done!');

  await browser.close();
})();

```

**Programmatic Control**

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint =
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');

  // Having the liveURLId is required in order to close it later
  const { liveURL, liveURLId } = await cdp.send('Browserless.liveURL');

  await page.waitForSelector('.my-selector');

  // Calling this CDP API with the "liveURLId" will close the session, and terminate the client
  // further usage of the liveURL will fail and no more human-control is possible
  await cdp.send('Browserless.closeLiveURL', { liveURLId });

  // Continue to process or interact with the browser, then:
  await browser.close();
})();

```

It's recommended that you double check the page prior to executing further code to make sure the page is where it should be, elements are present, and so forth. This approach makes it easy to solve hard things like second-factor authentication and more in a trivial fashion.

**Read-only LiveURL Sessions**

The `interactive: false` option allows you to create read-only LiveURL sessions where users can view the browser but cannot interact with it. This is useful for monitoring or demonstration purposes without allowing user input.

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint =
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');

  // Create a read-only LiveURL session that users can view but not interact with
  const { liveURL } = await cdp.send('Browserless.liveURL', {
    interactive: false,
  });

  console.log('Read-only LiveURL:', liveURL);

  await browser.close();
})();

```

## [section/The-Browserless-CDP-API/Browserless.reconnect](https://docs.browserless.io/open-api\#section/The-Browserless-CDP-API/Browserless.reconnect) Browserless.reconnect

> This API is only available for Enterprise plans. [Contact us for more information here.](https://www.browserless.io/contact/)

Reconnecting allows for the underlying Chrome or Chromium process to continue to run for a specified amount of time, and subsequent reconnecting back to it. With this approach you can also "share" this connection URL to other clients to connect to the same browser process, allowing you to parallelize via a single Browser process.

Once a reconnection URL is retrieved, Browserless will intercept close-based commands and stop them from terminating the browser process itself. This prevents clients from accidentally closing the process via `browser.close` or similar.

In order to use this API, simply call `Browserless.reconnect` as a CDP command. You can, optionally, set a `timeout` or an `auth` property. See the below examples for details

**Basic example with timeout**

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint =
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');

  // Allow this browser to run for 10 seconds, then shut down if nothing connects to it.
  // Defaults to the overall timeout set on the instance, which is 5 minutes if not specified.
  const { error, browserWSEndpoint } = await cdp.send('Browserless.reconnect', {
    timeout: 10000,
  });

  if (error) throw error;

  await browser.close();

  // browserWSEndpoint = 'https://production-sfo.browserless.io/reconnect/98e83bbfd396241a6963425b1feeba2f';
})();

```

If you want to enforce authentication, you can pass in an optional `auth` property that clients will need to use in order to connect with. Similar to how authentication works in general, a `token` query-string parameter will need to be applied.

**Authentication example**

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint =
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');

  // Set a custom authentication token that clients have to use in order to connect, or otherwise
  // receive a 401 Response.
  const { error, browserWSEndpoint } = await cdp.send('Browserless.reconnect', {
    auth: 'secret-auth-token',
  });

  if (error) throw error;

  await browser.close();

  // NOTE the URL here doesn't include the auth token!
  // browserWSEndpoint = 'https://production-sfo.browserless.io/reconnect/98e83bbfd396241a6963425b1feeba2f';
})();

```

**Recursive Example**

```js
import puppeteer from 'puppeteer-core';

const job = async (reconnectURL) => {
  const browserWSEndpoint =
    reconnectURL ??
    'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const [page] = await browser.page();
  const cdp = await page.createCDPSession();
  await page.goto('https://example.com');

  // Anytime Browserless.reconnect is called, this restarts the timer back to the provided value,
  // effectively "bumping" the timer forward.
  const res = await cdp.send('Browserless.reconnect', {
    timeout: 30000,
  });

  if (res.error) throw error;

  await browser.close();

  // Continuously reconnect back...
  return job(res.browserWSEndpoint);
};

job().catch((e) => console.error(e));

```

## [section/The-Browserless-CDP-API/Browserless.solveCaptcha](https://docs.browserless.io/open-api\#section/The-Browserless-CDP-API/Browserless.solveCaptcha) Browserless.solveCaptcha

> This API is only available for Enterprise and Scale and above plans on Cloud. [Contact us for more information here.](https://www.browserless.io/contact/). Only the `/chrome` and `/chromium` routes support Captcha solving.

Browserless comes with built-in captcha solving capabilities. We use a variety of techniques to try and mitigate the chances of captchas coming up, but if you happen to run into one you can simply call on our API to solve it.

Given the amount of possibilities during a captcha solve, the API returns many properties and information in order to help your script be more informed as to what happened. See the below code example for all details and fields returned by the API.

Please be aware that solving a captcha can take a few seconds up to several minutes, so you'll want to increase your timeouts accordingly for your scripts. Captcha's solved, or attempted to solve, cost 10 units.

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browser = await puppeteer.connect({
    browserWSEndpoint:
      'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN&timeout=300000',
  });

  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  await page.goto('https://www.google.com/recaptcha/api2/demo', {
    waitUntil: 'networkidle0',
  });

  const {
    // A simple boolean indicating whether the script can proceed
    ok,
    // Whether or not a captcha was found
    captchaFound,
    // A human-readable description of what occurred.
    message,
    // Whether a solve was attempted or not
    solveAttempted,
    // If the Captcha was solved, only true if found AND solved
    solved,
    // Any errors during execution are saved here:
    error,
  } = await cdp.send('Browserless.solveCaptcha', {
    // How long to wait for a Captcha to appear to solve.
    // Defaults to 10,000ms, or 10 seconds.
    appearTimeout: 30000,
  });

  console.log(message);

  if (ok) {
    await page.click('#recaptcha-demo-submit');
  } else {
    console.error(`Error solving captcha!`);
  }

  await browser.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});

```

In general, if an `ok` response is sent back from this API, then your script is good to proceed with further actions. If a captcha is to suddenly appears after an action then you might want to listen for the `Browserless.foundCaptcha` event (see below) and retry solving.

## [section/The-Browserless-CDP-API/Browserless.foundCaptcha](https://docs.browserless.io/open-api\#section/The-Browserless-CDP-API/Browserless.foundCaptcha) Browserless.foundCaptcha

> This API is only available for Enterprise and Scale and above plans on Cloud. [Contact us for more information here.](https://www.browserless.io/contact/). Only the `/chrome` and `/chromium` routes support Captcha solving.

> Custom CDP Events are not supported in all libraries, including .NET Playwright.

Emitted whenever a captcha widget is found on the page. Useful for checking if there's a captcha and deciding whether or not to proceed with solving.

The example below stops until a captcha is found, which may or may not be the case with every website out there.

```js
import puppeteer from 'puppeteer-core';

// Recaptcha
(async () => {
  const browser = await puppeteer.connect({
    browserWSEndpoint:
      'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN&timeout=300000',
  });

  const page = await browser.newPage();
  const cdp = await page.createCDPSession();

  await page.goto('https://www.google.com/recaptcha/api2/demo', {
    waitUntil: 'networkidle0',
  });

  // Please note that not all libraries support custom CDP events.
  await new Promise((resolve) =>
    cdp.on('Browserless.captchaFound', () => {
      console.log('Found a captcha!');
      return resolve();
    }),
  );

  const { solved, error } = await cdp.send('Browserless.solveCaptcha');
  console.log({
    solved,
    error,
  });

  // Continue...
  await page.click('#recaptcha-demo-submit');
})().catch((e) => {
  console.error(e);
  process.exit(1);
});

```

## [section/The-Browserless-CDP-API/Browserless.heartbeat](https://docs.browserless.io/open-api\#section/The-Browserless-CDP-API/Browserless.heartbeat) Browserless.heartbeat

> This API is only available for Enterprise hosted and Starter and above plans on Cloud. [Contact us for more information here.](https://www.browserless.io/contact/).

> Custom CDP Events are not supported in all libraries, including .NET Playwright.

A custom event emitted every several seconds, signaling a live connection. This is useful for a few reasons:

- It ensure that your connection with the browser is still good.
- Sending data can trigger some load-balancing technologies to not kill the connection.

Today this event is emitted every 30 seconds.

```js
import puppeteer from 'puppeteer-core';

const browserWSEndpoint = `wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN`;

(async () => {
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  await page.goto('https://example.com/');
  const client = await page.createCDPSession();

  client.on('Browserless.heartbeat', () => {
    console.log('Browserless.heartbeat');
  });
})();

```

## [section/The-Browserless-CDP-API/Browserless.pageId](https://docs.browserless.io/open-api\#section/The-Browserless-CDP-API/Browserless.pageId) Browserless.pageId

> This API is only available for Enterprise hosted and Starter and above plans on Cloud. [Contact us for more information here.](https://www.browserless.io/contact/).

A simple helper utility to return the page's unique ID. Since most libraries treat this ID as opaque, and some even hide it, knowing the page's ID can be of great help when interacting with other parts of Browserless.

```js
import puppeteer from 'puppeteer-core';

(async () => {
  const browserWSEndpoint = 'wss://production-sfo.browserless.io/chromium';
  const browser = await puppeteer.connect({ browserWSEndpoint });
  const page = await browser.newPage();
  const cdp = await page.createCDPSession();
  const { pageId } = await cdp.send('Browserless.pageId');

  // pageId = 'ABC12354AFDC123';
})();

```

You can, optionally, try and "find" this ID in puppeteer or similar libraries. Given that puppeteer has this property underscored, it's likely to change or be unavailable in the future, and requires the infamous `// @ts-ignore` comment to allow TypeScript compilation.

```ts
const getPageId = (page: Page): string => {
  // @ts-ignore
  return page.target()._targetId;
};

```

## [section/Changelog](https://docs.browserless.io/open-api\#section/Changelog) Changelog

## [tag/Browser-REST-APIs](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs) Browser REST APIs

## [tag/Browser-REST-APIs/paths/~1chrome~1content/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1content/post)/chrome/content

A JSON-based API. Given a "url" or "html" field, runs and returns HTML content after the page has loaded and JavaScript has parsed.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean<br>Whether or not to allow JavaScript to run on the page. |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

An HTML payload of the website or HTML after JavaScript
parsing and execution.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/content

https://docs.browserless.io/chrome/content

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

## [tag/Browser-REST-APIs/paths/~1chrome~1download/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1download/post)/chrome/download

A JSON or JavaScript content-type API for returning files Chrome has downloaded during
the execution of puppeteer code, which is ran inside context of the browser.
Browserless sets up a blank page, a fresh download directory, injects your puppeteer code, and then executes it.
You can load external libraries via the "import" syntax, and import ESM-style modules
that are written for execution inside of the browser. Once your script is finished, any
downloaded files from Chromium are returned back with the appropriate content-type header.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema:   application/jsonapplication/javascriptapplication/json

|     |     |
| --- | --- |
| code<br>required | string |
| context | object |

### Responses

**200**

Responses are determined by the returned value of the downloads
themselves, so there isn't a static response type for this API.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/download

https://docs.browserless.io/chrome/download

### Request samples

- Payload

Content type

application/jsonapplication/javascriptapplication/json

Copy
Expand all  Collapse all

`{
"code": "string",
"context": { }}`

## [tag/Browser-REST-APIs/paths/~1chrome~1function/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1function/post)/chrome/function

A JSON or JavaScript content-type API for running puppeteer code in the browser's context.
Browserless sets up a blank page, injects your puppeteer code, and runs it.
You can optionally load external libraries via the "import" module that are meant for browser usage.
Values returned from the function are checked and an appropriate content-type and response is sent back
to your HTTP call.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema:   application/jsonapplication/javascriptapplication/json

|     |     |
| --- | --- |
| code<br>required | string |
| context | object |

### Responses

**200**

Responses are determined by the returned value of the function
itself. Binary responses (PDF's, screenshots) are returned back
as binary data, and primitive JavaScript values are returned back
by type (HTML data is "text/html", Objects are "application/json")

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/function

https://docs.browserless.io/chrome/function

### Request samples

- Payload

Content type

application/jsonapplication/javascriptapplication/json

Copy
Expand all  Collapse all

`{
"code": "string",
"context": { }}`

## [tag/Browser-REST-APIs/paths/~1json~1list/get](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1json~1list/get)/json/list

Returns a JSON payload that acts as a pass-through to the DevTools /json/list HTTP API in Chromium and Chrome.
Browserless crafts this payload so that remote clients can connect to the underlying "webSocketDebuggerUrl"
properly, excluding any API tokens in that URL. If under authentication be sure to include your authorization.

### Responses

**200**

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/json/list

https://docs.browserless.io/json/list

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`[\
{\
"description": "string",\
"devtoolsFrontendUrl": "string",\
"id": "string",\
"title": "string",\
"type": "string",\
"url": "string",\
"webSocketDebuggerUrl": "string"}]`

## [tag/Browser-REST-APIs/paths/~1json~1new/put](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1json~1new/put)/json/new

Returns a JSON payload that acts as a pass-through to the DevTools /json/new HTTP API in Chromium.
Browserless mocks this payload so that remote clients can connect to the underlying "webSocketDebuggerUrl"
which will cause Browserless to start the browser and proxy that request into a blank page.

### Responses

**200**

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

put/json/new

https://docs.browserless.io/json/new

### Response samples

- 200

Content type

application/json

Copy

`{
"description": "string",
"devtoolsFrontendUrl": "string",
"id": "string",
"title": "string",
"type": "string",
"url": "string",
"webSocketDebuggerUrl": "string"}`

## [tag/Browser-REST-APIs/paths/~1json~1protocol/get](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1json~1protocol/get)/json/protocol

Returns Protocol JSON meta-data that Chrome and Chromium come with.

### Responses

**200**

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/json/protocol

https://docs.browserless.io/json/protocol

### Response samples

- 200

Content type

application/json

Copy

`{ }`

## [tag/Browser-REST-APIs/paths/~1json~1version/get](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1json~1version/get)/json/version

Returns a JSON payload that acts as a pass-through to the DevTools /json/version protocol in Chrome and Chromium.

### Responses

**200**

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/json/version

https://docs.browserless.io/json/version

### Response samples

- 200

Content type

application/json

Copy

`{
"description": "string",
"devtoolsFrontendUrl": "string",
"id": "string",
"title": "string",
"type": "string",
"url": "string",
"webSocketDebuggerUrl": "string"}`

## [tag/Browser-REST-APIs/paths/~1chrome~1pdf/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1pdf/post)/chrome/pdf

A JSON-based API for getting a PDF binary from either a supplied
"url" or "html" payload in your request. Many options exist for
injecting cookies, request interceptors, user-agents and waiting for
selectors, timers and more.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| options | object<br>Valid options to configure PDF generation via {@link Page.pdf}. |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

Responds with an application/pdf content-type and a binary PDF

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/pdf

https://docs.browserless.io/chrome/pdf

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"options": {
"scale": 0,
"displayHeaderFooter": true,
"headerTemplate": "string",
"footerTemplate": "string",
"printBackground": true,
"landscape": true,
"pageRanges": "string",
"format": "A0",
"width": "string",
"height": "string",
"preferCSSPageSize": true,
"margin": {
"top": "string",
"bottom": "string",
"left": "string",
"right": "string"},
"path": "string",
"omitBackground": true,
"tagged": true,
"outline": true,
"timeout": 0,
"waitForFonts": true},
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

## [tag/Browser-REST-APIs/paths/~1chrome~1performance/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1performance/post)/chrome/performance

Run lighthouse performance audits with a supplied "url" in your JSON payload.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| budgets | Array of objects |
| config | object |
| url | string |

### Responses

**200**

The response of the lighthouse stats. Response objects are
determined by the type of budgets and config in the POST
JSON body

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/performance

https://docs.browserless.io/chrome/performance

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"budgets": [\
{ }],
"config": { },
"url": "string"}`

### Response samples

- 200

Content type

application/json

Copy

`{ }`

## [tag/Browser-REST-APIs/paths/~1chrome~1scrape/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1scrape/post)/chrome/scrape

A JSON-based API that returns text, html, and meta-data from a given list of selectors.
Debugging information is available by sending in the appropriate flags in the "debugOpts"
property. Responds with an array of JSON objects.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| debugOpts | object |
| elements | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

The JSON response body

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/scrape

https://docs.browserless.io/chrome/scrape

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"debugOpts": {
"console": true,
"cookies": true,
"html": true,
"network": true,
"screenshot": true},
"elements": [\
{\
"selector": "string",\
"timeout": 0}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"data": [\
{\
"results": [\
{\
"attributes": [\
{\
"name": "string",\
"value": "string"}],\
"height": 0,\
"html": "string",\
"left": 0,\
"text": "string",\
"top": 0,\
"width": 0}],\
"selector": "string"}],
"debug": {
"console": [\
"string"],
"cookies": [\
{\
"name": "string",\
"value": "string",\
"domain": "string",\
"path": "string",\
"expires": 0,\
"size": 0,\
"httpOnly": true,\
"secure": true,\
"session": true,\
"sameSite": "Lax",\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true},\
"partitionKeyOpaque": true}],
"html": null,
"network": {
"inbound": [\
{\
"headers": null,\
"status": 0,\
"url": "string"}],
"outbound": [\
{\
"headers": null,\
"method": "string",\
"url": "string"}]},
"screenshot": null}}`

## [tag/Browser-REST-APIs/paths/~1chrome~1screenshot/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1screenshot/post)/chrome/screenshot

A JSON-based API for getting a screenshot binary from either a supplied
"url" or "html" payload in your request. Many options exist including
cookies, user-agents, setting timers and network mocks.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| options | object |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| scrollPage | boolean |
| selector | string |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

Response can either be a text/plain base64 encoded body
or a binary stream with png/jpeg as a content-type

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/screenshot

https://docs.browserless.io/chrome/screenshot

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"options": {
"optimizeForSpeed": true,
"type": "jpeg",
"quality": 0,
"fromSurface": true,
"fullPage": true,
"omitBackground": true,
"path": "string",
"clip": {
"scale": 0,
"width": 0,
"height": 0,
"x": 0,
"y": 0},
"encoding": "base64",
"captureBeyondViewport": true},
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"scrollPage": true,
"selector": "string",
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

## [tag/Browser-REST-APIs/paths/~1chromium~1content/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1content/post)/chromium/content

A JSON-based API. Given a "url" or "html" field, runs and returns HTML content after the page has loaded and JavaScript has parsed.

**Note:** This endpoint is also available at: `/content` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean<br>Whether or not to allow JavaScript to run on the page. |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

An HTML payload of the website or HTML after JavaScript
parsing and execution.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/content

https://docs.browserless.io/chromium/content

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

## [tag/Browser-REST-APIs/paths/~1chromium~1download/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1download/post)/chromium/download

A JSON or JavaScript content-type API for returning files Chrome has downloaded during
the execution of puppeteer code, which is ran inside context of the browser.
Browserless sets up a blank page, a fresh download directory, injects your puppeteer code, and then executes it.
You can load external libraries via the "import" syntax, and import ESM-style modules
that are written for execution inside of the browser. Once your script is finished, any
downloaded files from Chromium are returned back with the appropriate content-type header.

**Note:** This endpoint is also available at: `/download` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema:   application/jsonapplication/javascriptapplication/json

|     |     |
| --- | --- |
| code<br>required | string |
| context | object |

### Responses

**200**

Responses are determined by the returned value of the downloads
themselves, so there isn't a static response type for this API.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/download

https://docs.browserless.io/chromium/download

### Request samples

- Payload

Content type

application/jsonapplication/javascriptapplication/json

Copy
Expand all  Collapse all

`{
"code": "string",
"context": { }}`

## [tag/Browser-REST-APIs/paths/~1chromium~1function/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1function/post)/chromium/function

A JSON or JavaScript content-type API for running puppeteer code in the browser's context.
Browserless sets up a blank page, injects your puppeteer code, and runs it.
You can optionally load external libraries via the "import" module that are meant for browser usage.
Values returned from the function are checked and an appropriate content-type and response is sent back
to your HTTP call.

**Note:** This endpoint is also available at: `/function` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema:   application/jsonapplication/javascriptapplication/json

|     |     |
| --- | --- |
| code<br>required | string |
| context | object |

### Responses

**200**

Responses are determined by the returned value of the function
itself. Binary responses (PDF's, screenshots) are returned back
as binary data, and primitive JavaScript values are returned back
by type (HTML data is "text/html", Objects are "application/json")

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/function

https://docs.browserless.io/chromium/function

### Request samples

- Payload

Content type

application/jsonapplication/javascriptapplication/json

Copy
Expand all  Collapse all

`{
"code": "string",
"context": { }}`

## [tag/Browser-REST-APIs/paths/~1chromium~1pdf/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1pdf/post)/chromium/pdf

A JSON-based API for getting a PDF binary from either a supplied
"url" or "html" payload in your request. Many options exist for
injecting cookies, request interceptors, user-agents and waiting for
selectors, timers and more.

**Note:** This endpoint is also available at: `/pdf` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| blockConsentModals | boolean |
| cookies | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| options | object<br>Valid options to configure PDF generation via {@link Page.pdf}. |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean |
| url | string |
| userAgent | string |
| viewport | object |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/pdf

https://docs.browserless.io/chromium/pdf

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"blockConsentModals": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"options": {
"scale": 0,
"displayHeaderFooter": true,
"headerTemplate": "string",
"footerTemplate": "string",
"printBackground": true,
"landscape": true,
"pageRanges": "string",
"format": "A0",
"width": "string",
"height": "string",
"preferCSSPageSize": true,
"margin": {
"top": "string",
"bottom": "string",
"left": "string",
"right": "string"},
"path": "string",
"omitBackground": true,
"tagged": true,
"outline": true,
"timeout": 0,
"waitForFonts": true},
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

## [tag/Browser-REST-APIs/paths/~1chromium~1performance/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1performance/post)/chromium/performance

Run lighthouse performance audits with a supplied "url" in your JSON payload.

**Note:** This endpoint is also available at: `/performance` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| budgets | Array of objects |
| config | object |
| url | string |

### Responses

**200**

The response of the lighthouse stats. Response objects are
determined by the type of budgets and config in the POST
JSON body

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/performance

https://docs.browserless.io/chromium/performance

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"budgets": [\
{ }],
"config": { },
"url": "string"}`

### Response samples

- 200

Content type

application/json

Copy

`{ }`

## [tag/Browser-REST-APIs/paths/~1chromium~1scrape/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1scrape/post)/chromium/scrape

A JSON-based API that returns text, html, and meta-data from a given list of selectors.
Debugging information is available by sending in the appropriate flags in the "debugOpts"
property. Responds with an array of JSON objects.

**Note:** This endpoint is also available at: `/scrape` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| debugOpts | object |
| elements | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

The JSON response body

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/scrape

https://docs.browserless.io/chromium/scrape

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"debugOpts": {
"console": true,
"cookies": true,
"html": true,
"network": true,
"screenshot": true},
"elements": [\
{\
"selector": "string",\
"timeout": 0}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"data": [\
{\
"results": [\
{\
"attributes": [\
{\
"name": "string",\
"value": "string"}],\
"height": 0,\
"html": "string",\
"left": 0,\
"text": "string",\
"top": 0,\
"width": 0}],\
"selector": "string"}],
"debug": {
"console": [\
"string"],
"cookies": [\
{\
"name": "string",\
"value": "string",\
"domain": "string",\
"path": "string",\
"expires": 0,\
"size": 0,\
"httpOnly": true,\
"secure": true,\
"session": true,\
"sameSite": "Lax",\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true},\
"partitionKeyOpaque": true}],
"html": null,
"network": {
"inbound": [\
{\
"headers": null,\
"status": 0,\
"url": "string"}],
"outbound": [\
{\
"headers": null,\
"method": "string",\
"url": "string"}]},
"screenshot": null}}`

## [tag/Browser-REST-APIs/paths/~1chromium~1screenshot/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1screenshot/post)/chromium/screenshot

A JSON-based API for getting a screenshot binary from either a supplied
"url" or "html" payload in your request. Many options exist including
cookies, user-agents, setting timers and network mocks.

**Note:** This endpoint is also available at: `/screenshot` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| blockConsentModals | boolean |
| cookies | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| options | object |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| scrollPage | boolean |
| selector | string |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean |
| url | string |
| userAgent | string |
| viewport | object |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/screenshot

https://docs.browserless.io/chromium/screenshot

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"blockConsentModals": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"options": {
"optimizeForSpeed": true,
"type": "jpeg",
"quality": 0,
"fromSurface": true,
"fullPage": true,
"omitBackground": true,
"path": "string",
"clip": {
"scale": 0,
"width": 0,
"height": 0,
"x": 0,
"y": 0},
"encoding": "base64",
"captureBeyondViewport": true},
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"scrollPage": true,
"selector": "string",
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

## [tag/Browser-REST-APIs/paths/~1edge~1content/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1edge~1content/post)/edge/content

A JSON-based API. Given a "url" or "html" field, runs and returns HTML content after the page has loaded and JavaScript has parsed.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean<br>Whether or not to allow JavaScript to run on the page. |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

An HTML payload of the website or HTML after JavaScript
parsing and execution.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/edge/content

https://docs.browserless.io/edge/content

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

## [tag/Browser-REST-APIs/paths/~1edge~1download/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1edge~1download/post)/edge/download

A JSON or JavaScript content-type API for returning files Chrome has downloaded during
the execution of puppeteer code, which is ran inside context of the browser.
Browserless sets up a blank page, a fresh download directory, injects your puppeteer code, and then executes it.
You can load external libraries via the "import" syntax, and import ESM-style modules
that are written for execution inside of the browser. Once your script is finished, any
downloaded files from Chromium are returned back with the appropriate content-type header.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema:   application/jsonapplication/javascriptapplication/json

|     |     |
| --- | --- |
| code<br>required | string |
| context | object |

### Responses

**200**

Responses are determined by the returned value of the downloads
themselves, so there isn't a static response type for this API.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/edge/download

https://docs.browserless.io/edge/download

### Request samples

- Payload

Content type

application/jsonapplication/javascriptapplication/json

Copy
Expand all  Collapse all

`{
"code": "string",
"context": { }}`

## [tag/Browser-REST-APIs/paths/~1edge~1function/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1edge~1function/post)/edge/function

A JSON or JavaScript content-type API for running puppeteer code in the browser's context.
Browserless sets up a blank page, injects your puppeteer code, and runs it.
You can optionally load external libraries via the "import" module that are meant for browser usage.
Values returned from the function are checked and an appropriate content-type and response is sent back
to your HTTP call.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema:   application/jsonapplication/javascriptapplication/json

|     |     |
| --- | --- |
| code<br>required | string |
| context | object |

### Responses

**200**

Responses are determined by the returned value of the function
itself. Binary responses (PDF's, screenshots) are returned back
as binary data, and primitive JavaScript values are returned back
by type (HTML data is "text/html", Objects are "application/json")

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/edge/function

https://docs.browserless.io/edge/function

### Request samples

- Payload

Content type

application/jsonapplication/javascriptapplication/json

Copy
Expand all  Collapse all

`{
"code": "string",
"context": { }}`

## [tag/Browser-REST-APIs/paths/~1edge~1pdf/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1edge~1pdf/post)/edge/pdf

A JSON-based API for getting a PDF binary from either a supplied
"url" or "html" payload in your request. Many options exist for
injecting cookies, request interceptors, user-agents and waiting for
selectors, timers and more.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| options | object<br>Valid options to configure PDF generation via {@link Page.pdf}. |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

Responds with an application/pdf content-type and a binary PDF

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/edge/pdf

https://docs.browserless.io/edge/pdf

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"options": {
"scale": 0,
"displayHeaderFooter": true,
"headerTemplate": "string",
"footerTemplate": "string",
"printBackground": true,
"landscape": true,
"pageRanges": "string",
"format": "A0",
"width": "string",
"height": "string",
"preferCSSPageSize": true,
"margin": {
"top": "string",
"bottom": "string",
"left": "string",
"right": "string"},
"path": "string",
"omitBackground": true,
"tagged": true,
"outline": true,
"timeout": 0,
"waitForFonts": true},
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

## [tag/Browser-REST-APIs/paths/~1edge~1performance/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1edge~1performance/post)/edge/performance

Run lighthouse performance audits with a supplied "url" in your JSON payload.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| budgets | Array of objects |
| config | object |
| url | string |

### Responses

**200**

The response of the lighthouse stats. Response objects are
determined by the type of budgets and config in the POST
JSON body

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/edge/performance

https://docs.browserless.io/edge/performance

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"budgets": [\
{ }],
"config": { },
"url": "string"}`

### Response samples

- 200

Content type

application/json

Copy

`{ }`

## [tag/Browser-REST-APIs/paths/~1edge~1scrape/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1edge~1scrape/post)/edge/scrape

A JSON-based API that returns text, html, and meta-data from a given list of selectors.
Debugging information is available by sending in the appropriate flags in the "debugOpts"
property. Responds with an array of JSON objects.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| debugOpts | object |
| elements | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

The JSON response body

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/edge/scrape

https://docs.browserless.io/edge/scrape

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"debugOpts": {
"console": true,
"cookies": true,
"html": true,
"network": true,
"screenshot": true},
"elements": [\
{\
"selector": "string",\
"timeout": 0}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"data": [\
{\
"results": [\
{\
"attributes": [\
{\
"name": "string",\
"value": "string"}],\
"height": 0,\
"html": "string",\
"left": 0,\
"text": "string",\
"top": 0,\
"width": 0}],\
"selector": "string"}],
"debug": {
"console": [\
"string"],
"cookies": [\
{\
"name": "string",\
"value": "string",\
"domain": "string",\
"path": "string",\
"expires": 0,\
"size": 0,\
"httpOnly": true,\
"secure": true,\
"session": true,\
"sameSite": "Lax",\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true},\
"partitionKeyOpaque": true}],
"html": null,
"network": {
"inbound": [\
{\
"headers": null,\
"status": 0,\
"url": "string"}],
"outbound": [\
{\
"headers": null,\
"method": "string",\
"url": "string"}]},
"screenshot": null}}`

## [tag/Browser-REST-APIs/paths/~1edge~1screenshot/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1edge~1screenshot/post)/edge/screenshot

A JSON-based API for getting a screenshot binary from either a supplied
"url" or "html" payload in your request. Many options exist including
cookies, user-agents, setting timers and network mocks.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| addScriptTag | Array of objects |
| addStyleTag | Array of objects |
| authenticate | object or null |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| cookies | Array of objects |
| emulateMediaType | string |
| gotoOptions | object |
| html | string |
| options | object |
| rejectRequestPattern | Array of strings |
| rejectResourceTypes | Array of strings<br>Items Enum:"cspviolationreport""document""eventsource""fetch""font""image""manifest""media""other""ping""prefetch""preflight""script""signedexchange""stylesheet""texttrack""websocket""xhr" |
| requestInterceptors | Array of objects |
| scrollPage | boolean |
| selector | string |
| setExtraHTTPHeaders | object |
| setJavaScriptEnabled | boolean |
| url | string |
| userAgent | string |
| viewport | object or null |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

Response can either be a text/plain base64 encoded body
or a binary stream with png/jpeg as a content-type

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/edge/screenshot

https://docs.browserless.io/edge/screenshot

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"addScriptTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string",\
"type": "string",\
"id": "string"}],
"addStyleTag": [\
{\
"url": "string",\
"path": "string",\
"content": "string"}],
"authenticate": {
"username": "string",
"password": "string"},
"bestAttempt": true,
"cookies": [\
{\
"name": "string",\
"value": "string",\
"url": "string",\
"domain": "string",\
"path": "string",\
"secure": true,\
"httpOnly": true,\
"sameSite": "Lax",\
"expires": 0,\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true}}],
"emulateMediaType": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"html": "string",
"options": {
"optimizeForSpeed": true,
"type": "jpeg",
"quality": 0,
"fromSurface": true,
"fullPage": true,
"omitBackground": true,
"path": "string",
"clip": {
"scale": 0,
"width": 0,
"height": 0,
"x": 0,
"y": 0},
"encoding": "base64",
"captureBeyondViewport": true},
"rejectRequestPattern": [\
"string"],
"rejectResourceTypes": [\
"cspviolationreport"],
"requestInterceptors": [\
{\
"pattern": "string",\
"response": {\
"status": 0,\
"headers": { },\
"contentType": "string",\
"body": {\
"BYTES_PER_ELEMENT": 0,\
"buffer": {\
"byteLength": 0,\
"__@toStringTag@14939": "string"},\
"byteLength": 0,\
"byteOffset": 0,\
"length": 0,\
"__@toStringTag@14939": "Uint8Array"}}}],
"scrollPage": true,
"selector": "string",
"setExtraHTTPHeaders": { },
"setJavaScriptEnabled": true,
"url": "string",
"userAgent": "string",
"viewport": {
"width": 0,
"height": 0,
"deviceScaleFactor": 0,
"isMobile": true,
"isLandscape": true,
"hasTouch": true},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

## [tag/Browser-REST-APIs/paths/~1chrome~1export/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1export/post)/chrome/export

> This API is only available for Enterprise, hosted and self-hosted plans. [Contact us for more information here.](https://www.browserless.io/contact/)

Exports a webpage to a PDF or image format. This API is useful for generating reports, screenshots, or PDFs of web pages.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| url | string<br>The URL of the site you want to archive. |
| gotoOptions | object |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |
| headers | object |

### Responses

**200**

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/export

https://docs.browserless.io/chrome/export

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"bestAttempt": true,
"url": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0,
"headers": { }}`

### Response samples

- 200

Content type

application/json

Copy

`{
"html": "string"}`

## [tag/Browser-REST-APIs/paths/~1chrome~1unblock/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1unblock/post)/chrome/unblock

> This API is only available for Enterprise and Cloud-unit plans. [Contact us for more information here.](https://www.browserless.io/contact/), or [sign-up here](https://www.browserless.io/pricing/).

Unblocks the provided URL from being blocked due to bot detection.
Returns a payload of Cookies, HTML, a base64 encoded screenshot,
and a "browserWSEndpoint" to allow connecting to the browser when
specified in the JSON Payload. Only supports CDP or Puppeteer
like libraries when connecting to the "browserWSEndpoint".

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| url | string<br>The URL of the site you want to unblock. |
| browserWSEndpoint | boolean<br>Whether or not to keep the underlying browser alive and around for<br>future reconnects. Defaults to false. |
| cookies | boolean<br>Whether or not to to return cookies for the site, defaults to true. |
| content | boolean<br>Whether or not to to return content for the site, defaults to true. |
| screenshot | boolean<br>Whether or not to to return a full-page screenshot for the site, defaults to true. |
| ttl | number<br>When the browserWSEndpoint is requested this tells<br>browserless how long to keep this browser alive for<br>re-connection until shutting it down completely.<br>Maximum of 30000 for 30 seconds (30,000ms). |
| gotoOptions | object |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/unblock

https://docs.browserless.io/chrome/unblock

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"bestAttempt": true,
"url": "string",
"browserWSEndpoint": true,
"cookies": true,
"content": true,
"screenshot": true,
"ttl": 0,
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"cookies": [\
{\
"name": "string",\
"value": "string",\
"domain": "string",\
"path": "string",\
"expires": 0,\
"size": 0,\
"httpOnly": true,\
"secure": true,\
"session": true,\
"sameSite": "Lax",\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true},\
"partitionKeyOpaque": true}],
"content": "string",
"browserWSEndpoint": "string",
"ttl": 0,
"screenshot": "string"}`

## [tag/Browser-REST-APIs/paths/~1chromium~1export/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1export/post)/chromium/export

> This API is only available for Enterprise, hosted and self-hosted plans. [Contact us for more information here.](https://www.browserless.io/contact/)

Exports a webpage to a PDF or image format. This API is useful for generating reports, screenshots, or PDFs of web pages.

**Note:** This endpoint is also available at: `/export` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| url | string<br>The URL of the site you want to archive. |
| gotoOptions | object |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |
| headers | object |

### Responses

**200**

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/export

https://docs.browserless.io/chromium/export

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"bestAttempt": true,
"url": "string",
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0,
"headers": { }}`

### Response samples

- 200

Content type

application/json

Copy

`{
"html": "string"}`

## [tag/Browser-REST-APIs/paths/~1chromium~1unblock/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1unblock/post)/chromium/unblock

> This API is only available for Enterprise and Cloud-unit plans. [Contact us for more information here.](https://www.browserless.io/contact/), or [sign-up here](https://www.browserless.io/pricing/).

Unblocks the provided URL from being blocked due to bot detection.
Returns a payload of Cookies, HTML, a base64 encoded screenshot,
and a "browserWSEndpoint" to allow connecting to the browser when
specified in the JSON Payload. Only supports CDP or Puppeteer
like libraries when connecting to the "browserWSEndpoint".

**Note:** This endpoint is also available at: `/unblock` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| bestAttempt | boolean<br>When bestAttempt is set to true, browserless attempt to proceed<br>when "awaited" events fail or timeout. This includes things like<br>goto, waitForSelector, and more. |
| url | string<br>The URL of the site you want to unblock. |
| browserWSEndpoint | boolean<br>Whether or not to keep the underlying browser alive and around for<br>future reconnects. Defaults to false. |
| cookies | boolean<br>Whether or not to to return cookies for the site, defaults to true. |
| content | boolean<br>Whether or not to to return content for the site, defaults to true. |
| screenshot | boolean<br>Whether or not to to return a full-page screenshot for the site, defaults to true. |
| ttl | number<br>When the browserWSEndpoint is requested this tells<br>browserless how long to keep this browser alive for<br>re-connection until shutting it down completely.<br>Maximum of 30000 for 30 seconds (30,000ms). |
| gotoOptions | object |
| waitForEvent | object |
| waitForFunction | object |
| waitForSelector | object |
| waitForTimeout | number |

### Responses

**200**

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/unblock

https://docs.browserless.io/chromium/unblock

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"bestAttempt": true,
"url": "string",
"browserWSEndpoint": true,
"cookies": true,
"content": true,
"screenshot": true,
"ttl": 0,
"gotoOptions": {
"referer": "string",
"referrerPolicy": "string",
"timeout": 0,
"waitUntil": [\
"domcontentloaded"],
"signal": {
"aborted": true,
"onabort": { },
"reason": null}},
"waitForEvent": {
"event": "string",
"timeout": 0},
"waitForFunction": {
"fn": "string",
"polling": "string",
"timeout": 0},
"waitForSelector": {
"hidden": true,
"selector": "string",
"timeout": 0,
"visible": true},
"waitForTimeout": 0}`

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"cookies": [\
{\
"name": "string",\
"value": "string",\
"domain": "string",\
"path": "string",\
"expires": 0,\
"size": 0,\
"httpOnly": true,\
"secure": true,\
"session": true,\
"sameSite": "Lax",\
"priority": "High",\
"sameParty": true,\
"sourceScheme": "NonSecure",\
"partitionKey": {\
"sourceOrigin": "string",\
"hasCrossSiteAncestor": true},\
"partitionKeyOpaque": true}],
"content": "string",
"browserWSEndpoint": "string",
"ttl": 0,
"screenshot": "string"}`

## [tag/Browser-REST-APIs/paths/~1chrome~1bql?(~1*)/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chrome~1bql?(~1*)/post)/chrome/bql?(/\*)

> This API is only available for Enterprise, hosted and self-hosted plans. [Contact us for more information here.](https://www.browserless.io/contact/)

Parses and executes BrowserQL requests, powered by the BrowserQL Editor or by other API integrations. See the BrowserQL Editor for more documentation on this API.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| blockConsentModals | boolean |
| humanlike | boolean |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| query | string |
| operationName | string |
| variables | object |

### Responses

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chrome/bql?(/\*)

https://docs.browserless.io/chrome/bql?(/\*)

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"query": "string",
"operationName": "string",
"variables": {
"property1": null,
"property2": null}}`

## [tag/Browser-REST-APIs/paths/~1chromium~1bql?(~1*)/post](https://docs.browserless.io/open-api\#tag/Browser-REST-APIs/paths/~1chromium~1bql?(~1*)/post)/chromium/bql?(/\*)

> This API is only available for Enterprise, hosted and self-hosted plans. [Contact us for more information here.](https://www.browserless.io/contact/)

Parses and executes BrowserQL requests, powered by the BrowserQL Editor or by other API integrations. See the BrowserQL Editor for more documentation on this API.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| blockConsentModals | boolean |
| humanlike | boolean |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| query | string |
| operationName | string |
| variables | object |

### Responses

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

post/chromium/bql?(/\*)

https://docs.browserless.io/chromium/bql?(/\*)

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{
"query": "string",
"operationName": "string",
"variables": {
"property1": null,
"property2": null}}`

## [tag/Management-REST-APIs](https://docs.browserless.io/open-api\#tag/Management-REST-APIs) Management REST APIs

## [tag/Management-REST-APIs/paths/~1active/get](https://docs.browserless.io/open-api\#tag/Management-REST-APIs/paths/~1active/get)/active

Returns a simple "204" HTTP code, with no response, indicating that the service itself is up and running.
Useful for liveliness probes or other external checks.

### Responses

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/active

https://docs.browserless.io/active

## [tag/Management-REST-APIs/paths/~1kill~1+([0-9a-zA-Z-_])/get](https://docs.browserless.io/open-api\#tag/Management-REST-APIs/paths/~1kill~1+([0-9a-zA-Z-_])/get)/kill/+(\[0-9a-zA-Z-\_\])

Kill running sessions based on BrowserId or TrackingId.

##### query Parameters

|     |     |
| --- | --- |
| token<br>required | string<br>The authorization token |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| browserId | string |
| launch | object or object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| trackingId | string<br>Custom session identifier |

### Responses

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/kill/+(\[0-9a-zA-Z-\_\])

https://docs.browserless.io/kill/+(\[0-9a-zA-Z-\_\])

## [tag/Management-REST-APIs/paths/~1meta/get](https://docs.browserless.io/open-api\#tag/Management-REST-APIs/paths/~1meta/get)/meta

Returns a JSON payload of the current system versions, including the core API version.

### Responses

**200**

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/meta

https://docs.browserless.io/meta

### Response samples

- 200

Content type

application/json

Copy
Expand all  Collapse all

`{
"version": "string",
"chromium": null,
"webkit": null,
"firefox": null,
"playwright": [\
"string"],
"puppeteer": [\
"string"]}`

## [tag/Management-REST-APIs/paths/~1/get](https://docs.browserless.io/open-api\#tag/Management-REST-APIs/paths/~1/get)/

Serves static files inside of this "static" directory. Content-types will vary depending on the type =of file being returned.

### Responses

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/

https://docs.browserless.io/

## [tag/Browser-WebSocket-APIs](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs) Browser WebSocket APIs

## [tag/Browser-WebSocket-APIs/paths/~1devtools~1browser~1*/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1devtools~1browser~1*/get)/devtools/browser/\*

Connect to an already-running Chromium process with a library like
puppeteer, or others, that work over chrome-devtools-protocol. Chromium
must already be launched in order to not return a 404.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/devtools/browser/\*

https://docs.browserless.io/devtools/browser/\*

## [tag/Browser-WebSocket-APIs/paths/~1chrome/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1chrome/get)/chrome

Launch and connect to Chromium with a library like puppeteer or others that work over chrome-devtools-protocol.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| record | boolean |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/chrome

https://docs.browserless.io/chrome

## [tag/Browser-WebSocket-APIs/paths/~1devtools~1page~1*/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1devtools~1page~1*/get)/devtools/page/\*

Connect to an existing page in Chromium with a library like
chrome-remote-interface or others that work the page websocketDebugger
URL. You can get this unique URL by calling the /json/list API
or by finding the page's unique ID from your library of choice.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/devtools/page/\*

https://docs.browserless.io/devtools/page/\*

## [tag/Browser-WebSocket-APIs/paths/~1chrome~1playwright/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1chrome~1playwright/get)/chrome/playwright

Connect to Chromium with any playwright style library.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/chrome/playwright

https://docs.browserless.io/chrome/playwright

## [tag/Browser-WebSocket-APIs/paths/~1chromium/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1chromium/get)/chromium

Launch and connect to Chromium with a library like puppeteer or others that work over chrome-devtools-protocol.

**Note:** This endpoint is also available at: \`\` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| record | boolean |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/chromium

https://docs.browserless.io/chromium

## [tag/Browser-WebSocket-APIs/paths/~1playwright~1chromium/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1playwright~1chromium/get)/playwright/chromium

Connect to Chromium with any playwright style library.

**Note:** This endpoint is also available at: `/chromium/playwright` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/playwright/chromium

https://docs.browserless.io/playwright/chromium

## [tag/Browser-WebSocket-APIs/paths/~1edge/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1edge/get)/edge

Launch and connect to Chromium with a library like puppeteer or others that work over chrome-devtools-protocol.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/edge

https://docs.browserless.io/edge

## [tag/Browser-WebSocket-APIs/paths/~1edge~1playwright/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1edge~1playwright/get)/edge/playwright

Connect to Chromium with any playwright style library.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/edge/playwright

https://docs.browserless.io/edge/playwright

## [tag/Browser-WebSocket-APIs/paths/~1playwright~1firefox/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1playwright~1firefox/get)/playwright/firefox

Connect to Firefox with any playwright-compliant library.

**Note:** This endpoint is also available at: `/firefox/playwright` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/playwright/firefox

https://docs.browserless.io/playwright/firefox

## [tag/Browser-WebSocket-APIs/paths/~1playwright~1webkit/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1playwright~1webkit/get)/playwright/webkit

Connect to Webkit with any playwright-compliant library.

**Note:** This endpoint is also available at: `/webkit/playwright` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | object or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/playwright/webkit

https://docs.browserless.io/playwright/webkit

## [tag/Browser-WebSocket-APIs/paths/~1chrome~1live~1*/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1chrome~1live~1*/get)/chrome/live/\*

> This API is only available for Enterprise plans and self-hosted Enterprise plans. [Contact us for more information here.](https://www.browserless.io/contact/), or [sign-up here](https://www.browserless.io/pricing/).

Websocket back-end that powers the live session experience.

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/chrome/live/\*

https://docs.browserless.io/chrome/live/\*

## [tag/Browser-WebSocket-APIs/paths/~1chrome~1stealth/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1chrome~1stealth/get)/chrome/stealth

> This API is only available for Enterprise and Cloud-unit plans. [Contact us for more information here.](https://www.browserless.io/contact/), or [sign-up here](https://www.browserless.io/pricing/).

Launch and connect to Stealthy Chromium with a library like puppeteer or others that work over chrome-devtools-protocol for scraping in a more stealth-like fashion.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/chrome/stealth

https://docs.browserless.io/chrome/stealth

## [tag/Browser-WebSocket-APIs/paths/~1chromium~1live~1*/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1chromium~1live~1*/get)/chromium/live/\*

> This API is only available for Enterprise plans and self-hosted Enterprise plans. [Contact us for more information here.](https://www.browserless.io/contact/), or [sign-up here](https://www.browserless.io/pricing/).

Websocket back-end that powers the live session experience.

**Note:** This endpoint is also available at: `/live/*` for backwards compatibility.

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/chromium/live/\*

https://docs.browserless.io/chromium/live/\*

## [tag/Browser-WebSocket-APIs/paths/~1chromium~1stealth/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1chromium~1stealth/get)/chromium/stealth

> This API is only available for Enterprise and Cloud-unit plans. [Contact us for more information here.](https://www.browserless.io/contact/), or [sign-up here](https://www.browserless.io/pricing/).

Launch and connect to Stealthy Chromium with a library like puppeteer or others that work over chrome-devtools-protocol for scraping in a more stealth-like fashion.

**Note:** This endpoint is also available at: `/stealth` for backwards compatibility.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/chromium/stealth

https://docs.browserless.io/chromium/stealth

## [tag/Browser-WebSocket-APIs/paths/~1reconnect~1*/get](https://docs.browserless.io/open-api\#tag/Browser-WebSocket-APIs/paths/~1reconnect~1*/get)/reconnect/\*

Reconnect to an existing Chromium or Chrome session with a library like puppeteer or others that work over chrome-devtools-protocol.

##### query Parameters

|     |     |
| --- | --- |
| blockAds | boolean<br>Whether or nor to load ad-blocking extensions for the session.<br>This currently uses uBlock-Lite and may cause certain sites<br>to not load properly. |
| launch | any or any or string<br>Launch options, which can be either an object<br>of puppeteer.launch options or playwright.launchServer<br>options, depending on the API. Must be either JSON<br>object, or a base64-encoded JSON object. |
| timeout | number<br>Override the system-level timeout for this request.<br>Accepts a value in milliseconds. |
| token | string<br>The authorization token |
| trackingId | string<br>Custom session identifier |

### Responses

**101**

Indicates successful WebSocket upgrade.

**400**

The request contains errors or didn't properly encode content.

**401**

The request is missing, or contains bad, authorization credentials.

**404**

Resource couldn't be found.

**408**

The request took has taken too long to process.

**429**

Too many requests are currently being processed.

**500**

An internal error occurred when handling the request.

get/reconnect/\*

https://docs.browserless.io/reconnect/\*