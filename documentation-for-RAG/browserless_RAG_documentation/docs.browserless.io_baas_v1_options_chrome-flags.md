---
url: "https://docs.browserless.io/baas/v1/options/chrome-flags"
title: "Launch Options | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/options/chrome-flags#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

- [Launching with a proxy](https://docs.browserless.io/baas/v1/options/chrome-flags#launching-with-a-proxy)
- [Blocking Ads](https://docs.browserless.io/baas/v1/options/chrome-flags#blocking-ads)
- [Running in Stealth](https://docs.browserless.io/baas/v1/options/chrome-flags#running-in-stealth)
- [Specifying a user-data-dir](https://docs.browserless.io/baas/v1/options/chrome-flags#caching-with-user-data-dir)
- [Keeping the browser alive](https://docs.browserless.io/baas/v1/options/chrome-flags#keeping-the-browser-alive)
- [Setting a width and height](https://docs.browserless.io/baas/v1/options/chrome-flags#starting-chrome-with-a-width-and-height)
- [Ignoring default flags](https://docs.browserless.io/baas/v1/options/chrome-flags#ignoring-default-flags)
- [Setting headless](https://docs.browserless.io/baas/v1/options/chrome-flags#setting-headless)
- [Overriding puppeteer launch args](https://docs.browserless.io/baas/v1/options/chrome-flags#overriding-puppeteers-launch-args)
- [Setting a Tracking ID](https://docs.browserless.io/baas/v1/options/chrome-flags#setting-a-tracking-id)
- [Overriding the session timer](https://docs.browserless.io/baas/v1/options/chrome-flags#overriding-the-session-timer)
- [Other parameters](https://docs.browserless.io/baas/v1/options/chrome-flags#other-parameters)

Browserless let's you control how Chrome is started via query-string parameters in your `puppeteer.connect`'s `browserWSEndpoint` URL, or in your REST API. This is useful in cases where you might need to start Chrome at a certain width and height, or need to use a proxy for visiting pages behind a firewall. Browserless (both hosted and self-hosted) lets you send launch arguments by specifying them as query-string parameters.

> If you've launched workers in a different region, be sure to use the appropriate load-balancer on your account page for a faster connection.

## Launching with a proxy [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#launching-with-a-proxy "Direct link to Launching with a proxy")

> Please note that many proxies only support Chromium revisions in less than puppeteer 1.18.0. This is due to Chromium dropping support for Proxy-Authorization headers. Check your proxies documentation for how to properly authenticate, and ensure that you don't need to set a Proxy-Authorization header.

```codeBlockLines_p187
wss://chrome.browserless.io/?token=YOUR_API_KEY&--proxy-server=https://my-proxy.com

```

You can start Chrome and have it issues requests via a proxy by using the query-string parameter of `--proxy-server=${server}`. This will have Chrome issues requests through the proxy server as opposed to issuing plain network requests.

NOTE: If using an authenticated proxy, where you must provide a username and password, refer to your libraries documentation on how to handle this.

## Blocking ads [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#blocking-ads "Direct link to Blocking ads")

> Available in all accounts in browserless version 1.7.0 and beyond

You can use our built-in ad-blocker for both `puppeteer.connect()` and REST API calls. You'll simply need to add a query-string parameter of `?blockAds` to your URL when connecting:

```codeBlockLines_p187
wss://chrome.browserless.io/?token=YOUR_API_KEY&blockAds

```

Or for REST API calls:

```codeBlockLines_p187
https://chrome.browserless.io/?token=YOUR_API_KEY&blockAds

```

When new pages are created, browserless will inject a request-interceptor. If a domain matches a known site, we'll abort the call. This greatly reduces the number of inbound networks calls, and can significantly improve performance.

## Running in Stealth [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#running-in-stealth "Direct link to Running in Stealth")

Newer versions of our docker image, and in our cloud environment, now include a `stealth` argument that utilizes `puppeteer-extra-stealth` to help ensure your requests run stealthfully. As with all of our launch options, simply connect or query our APIs with a `stealth` argument:

```codeBlockLines_p187
wss://chrome.browserless.io/?token=YOUR_API_KEY&stealth

```

Or for REST API calls:

```codeBlockLines_p187
https://chrome.browserless.io/?token=YOUR_API_KEY&stealth

```

## Caching with user-data-dir [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#caching-with-user-data-dir "Direct link to Caching with user-data-dir")

> Setting a user-data-dir is only available for Dedicated and self-hosted accounts (not on usage-based or cloud unit-based).

You can launch Chrome and specify a "user-data-dir" on each request to cache and make future sessions faster:

```codeBlockLines_p187
wss://chrome.browserless.io/?token=YOUR_API_KEY&--user-data-dir=~/browserless-cache-123

```

This can be used in conjuction with all our API's and integrations.

## Keeping the browser alive [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#keeping-the-browser-alive "Direct link to Keeping the browser alive")

> This feature is only supported in our puppeteer integration, and only on Dedicated and self-hosted deployments.

By default, browserless automatically closes chrome when the session disconnects. This generally meets most of the use-cases we've seen out there. However, there may be times when you want to keep the browser open even after your finished. You can do this with a `keepalive` parameter.

`keepalive` specifies how long browserless should keep the browser process open for possible reconnection later.

**Keep chrome open for 5 minutes after disconnecting**

```codeBlockLines_p187
puppeteer.connect({
  browserWSEndpoint: 'wss://chrome.browserless.io/?token=YOUR_API_KEY&keepalive=300000',
});

```

Should you use `keepalive` in your connect call, you'll also want to ensure that `browser.disconnect` is called _and not_ `browser.close`, as the latter will kill the Chrome process.

Once your app disconnects, either by design or in case of an interuppted session, we will keep the browser open for the keepalive specified (in the above example this would be 5 minutes). After that, regardless of any reconnected sessions, browserless will kill the chromium process.

In order to reconnect to an existing session, simply call the `/session` endpoint, or for Dedicated accounts use the GraphQL `sessions` query. This call will return all active sessions back, including a `browserWSEndpoint` payload you can use to re-connect puppeteer back to the browser. When combined with a `trackingId` this can make for a powerful integration and a lot of flexibility.

## Starting Chrome with a width and height [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#starting-chrome-with-a-width-and-height "Direct link to Starting Chrome with a width and height")

```codeBlockLines_p187
wss://chrome.browserless.io/?token=YOUR_API_KEY&--window-size=1200,900

```

You can also specify the dimensions Chrome should start with via the `--window-size` parameter. The value here should be a string of X and Y dimensions which translate to width and height (IE: '800,600').

## Ignoring default flags [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#ignoring-default-flags "Direct link to Ignoring default flags")

By default puppeteer specifies a certain number of launch flags in order to provide the best experience. In order to turn these off you'll need to tell browserless to ignore them. Be careful ignoring these args as it might cause chromium to become unstable or refuse to launch.

```codeBlockLines_p187
wss://chrome.browserless.io/?token=YOUR_API_KEY&ignoreDefaultArgs=--hide-scrollbars,--disable-default-apps

```

## Setting headless [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#setting-headless "Direct link to Setting headless")

In many cases setting headless won't matter, as browserless will default to this to `true`. In some special circumastances it's important to set this to `false`. As an example, our screencast API sets this to `false` in order to appropriately load an extension for testing.

```codeBlockLines_p187
wss://chrome.browserless.io/?token=YOUR_API_KEY&headless=false

```

## Overriding Puppeteer's launch args [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#overriding-puppeteers-launch-args "Direct link to Overriding Puppeteer's launch args")

Since `puppeteer.connect` differs greatly from `puppeteer.launch`, browserless a way to pass in certain parameters to "override" puppeteer's default launch arguments. These are specified through query-string parameters, and can be applied like so:

**Ignore HTTPS Errors**

```codeBlockLines_p187
// Via puppeteer.launch()
puppeteer.launch({
  ignoreHTTPSErrors: true,
});

// Via puppeteer.connect()
puppeteer.connect({
  browserWSEndpoint: 'wss://chrome.browserless.io?token=YOUR-API-TOKEN',
  ignoreHTTPSErrors: true,
});

```

**Slow Mo**

```codeBlockLines_p187
// Via puppeteer.launch()
puppeteer.launch({
  slowMo: 1000,
});

// Via puppeteer.connect()
puppeteer.connect({
  browserWSEndpoint: 'wss://chrome.browserless.io?token=YOUR-API-TOKEN',
  slowMo: 1000,
});

```

**Ignore default args**

```codeBlockLines_p187
// Via puppeteer.launch()
puppeteer.launch({
  ignoreDefaultArgs: true,
});

// Via puppeteer.connect()
puppeteer.connect({
  browserWSEndpoint: 'wss://chrome.browserless.io?token=YOUR-API-TOKEN&ignoreDefaultArgs=true',
});

```

## Setting a tracking ID [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#setting-a-tracking-id "Direct link to Setting a tracking ID")

> Tracking ID's, and the workspace queries, are only available for Dedicated and self-hosted accounts (not usage-based or cloud unit-based).

Sometimes it's useful to associate particular sessions of browserless with some other part of your application. For those instances we have mechanism called `trackingId`.

When this query-string parameter is present in a REST API call, or `puppeteer.connect`, browserless will scope both file downloads and `GET /sessions` calls to reveal the `trackingId` of the original call. For instance:

```codeBlockLines_p187
// Connect with a "trackingId" in the browserWSEndpoint:
puppeteer.connect({
  browserWSEndpoint:
    'wss://chrome.browserless.io?token=YOUR-API-TOKEN&trackingId=AwENCwMHDQoHBgwKBAUODQ',
});

// Do some work, download files
browser.close();

```

Will save downloads to a sub-directory of `AwENCwMHDQoHBgwKBAUODQ` in the workspace. Thus, a `GET /workspace` call results in the following:

```codeBlockLines_p187
[\
  {\
    created: '2019-07-15T22:11:40.157Z',\
    isDirectory: false,\
    name: 'data.csv',\
    path: '/workspace/AwENCwMHDQoHBgwKBAUODQ/data.csv',\
    size: 52,\
    workspaceId: 'AwENCwMHDQoHBgwKBAUODQ',\
  },\
];

```

Similarly, a `GET /session` call will reveal a property to identify that particular session:

```codeBlockLines_p187
[\
  {\
    "description": "",\
    "devtoolsFrontendUrl": "/devtools/inspector.html?ws=127.0.0.1:3000/devtools/page/6875C09959939E88D9BD30EC1FE1AAF0",\
    "id": "6875C09959939E88D9BD30EC1FE1AAF0",\
    "title": "Example Domain",\
    "type": "page",\
    "url": "https://example.com/",\
    "webSocketDebuggerUrl": "ws://127.0.0.1:3000/devtools/page/6875C09959939E88D9BD30EC1FE1AAF0",\
    "port": "62932",\
    "trackingId": "AwENCwMHDQoHBgwKBAUODQ"\
  }\
]

```

We'll be adding more behavioral and logging changes to surface this tracking-ID as it makes sense, so be sure to check back often to see how this can help you in your application development.

## Overriding the session timer [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#overriding-the-session-timer "Direct link to Overriding the session timer")

By default, your sessions (REST API, puppeteer.connect _and_ webdriver) are governed by a timeout. This is set via your account page for the hosted service, or by specifying `CONNECTION_TIMEOUT` in the `docker run` command. You can, on a per-job basis, override this.

For `puppeteer.connect` and REST API's, simply specify a `?timeout` query-string parameter, with the value being the time in milliseconds for the session to execute:

```codeBlockLines_p187
# REST API (10-second limit):
https://chrome.browserless.io?token=YOUR-API-TOKEN&timeout=10000

# puppeteer.connect URL (10-second limit):
wss://chrome.browserless.io?token=YOUR-API-TOKEN&timeout=10000

```

For webdriver, you must add an additional capability:

```codeBlockLines_p187
const webdriver = require('selenium-webdriver');

const chromeCapabilities = webdriver.Capabilities.chrome();
// Set the session to a 10-second limit
chromeCapabilities.set('browserless.timeout', 10000);

```

For other runtimes and selenium libraries be sure to consult your libraries documentation, or [contact us](https://www.browserless.io/contact)

## Other parameters [​](https://docs.browserless.io/baas/v1/options/chrome-flags\#other-parameters "Direct link to Other parameters")

By default browserless looks for query-string parameters beginning with `--` and passes them to Chrome upon boot. This means that most flags are supported even if they aren't documented. You can also see how we parse parameters by [reading through our code here](https://github.com/browserless/browserless/blob/v1/src/chrome-helper.ts#L88).

At this time, only certain flags and query-parameters are allowed for usage-based accounts and cloud unit-based, and are listed below:

- --proxy-server,
- --window-size,
- --disable-web-security,
- --enable-features,
- --disable-web-security,
- --disable-setuid-sandbox,
- --lang,
- --font-render-hinting,
- --force-color-profile,
- stealth,
- ignoreDefaultArgs,
- headless,
- token,
- blockAds,
- ignoreHTTPSErrors,
- slowMo,

- [Launching with a proxy](https://docs.browserless.io/baas/v1/options/chrome-flags#launching-with-a-proxy)
- [Blocking ads](https://docs.browserless.io/baas/v1/options/chrome-flags#blocking-ads)
- [Running in Stealth](https://docs.browserless.io/baas/v1/options/chrome-flags#running-in-stealth)
- [Caching with user-data-dir](https://docs.browserless.io/baas/v1/options/chrome-flags#caching-with-user-data-dir)
- [Keeping the browser alive](https://docs.browserless.io/baas/v1/options/chrome-flags#keeping-the-browser-alive)
- [Starting Chrome with a width and height](https://docs.browserless.io/baas/v1/options/chrome-flags#starting-chrome-with-a-width-and-height)
- [Ignoring default flags](https://docs.browserless.io/baas/v1/options/chrome-flags#ignoring-default-flags)
- [Setting headless](https://docs.browserless.io/baas/v1/options/chrome-flags#setting-headless)
- [Overriding Puppeteer's launch args](https://docs.browserless.io/baas/v1/options/chrome-flags#overriding-puppeteers-launch-args)
- [Setting a tracking ID](https://docs.browserless.io/baas/v1/options/chrome-flags#setting-a-tracking-id)
- [Overriding the session timer](https://docs.browserless.io/baas/v1/options/chrome-flags#overriding-the-session-timer)
- [Other parameters](https://docs.browserless.io/baas/v1/options/chrome-flags#other-parameters)