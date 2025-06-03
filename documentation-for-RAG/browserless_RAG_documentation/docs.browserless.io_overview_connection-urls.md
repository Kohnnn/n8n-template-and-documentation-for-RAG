---
url: "https://docs.browserless.io/overview/connection-urls"
title: "Connection URLs and Endpoints | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/overview/connection-urls#__docusaurus_skipToContent_fallback)

On this page

This section covers all connection URLs and endpoints for Browserless services. Learn when to use WebSocket (wss://) vs HTTP(S) URLs, and how to include your token and options in these URLs.

### Connection URL Builder

Service Type:

BrowserQLBaaS v2REST API

Library:

PuppeteerPlaywright

Browser:

ChromiumChrome

Stealth Mode:

DisabledEnabled

Region:

US WestEurope UKEurope Amsterdam

API Token:

#### Connection URL:

Copy

```
wss://production-sfo.browserless.io/?token=YOUR_TOKEN
```

#### Code Snippet:

Copy

```
const browser = await puppeteer.connect({
  browserWSEndpoint: 'wss://production-sfo.browserless.io/?token=YOUR_TOKEN',
});
```

## Base URL and Regions [​](https://docs.browserless.io/overview/connection-urls\#base-url-and-regions "Direct link to Base URL and Regions")

Browserless has multiple regional base URLs:

- `https://production-sfo.browserless.io` (US West)
- `https://production-lon.browserless.io` (Europe UK)
- `https://production-ams.browserless.io` (Europe Amsterdam)

For WebSocket connections, simply replace `https://` with `wss://` for the same host. For
example:

- WebSocket (Puppeteer/Playwright): `wss://production-sfo.browserless.io/...`
- HTTP REST API call: `https://production-sfo.browserless.io/...`

Choose the region closest to you to reduce latency (see [Load Balancers](https://docs.browserless.io/baas/load-balancers)). All require the token query parameter.

## Using Your API Token in URLs [​](https://docs.browserless.io/overview/connection-urls\#using-your-api-token-in-urls "Direct link to Using Your API Token in URLs")

Add your API token to the URL query string as `?token=YOUR_TOKEN`. Required for authentication (see [Using your API token](https://docs.browserless.io/baas/start)). Invalid tokens result in HTTP 401/403 errors. Keep this URL secure and never expose it in client-side code or logs.

Example:
`wss://production-sfo.browserless.io?token=094632bb-e326-4c63-b953-82b55700b14c` is a basic connection string for a new Chrome session on the SFO cluster using the given token.

## BrowserQL Connection [​](https://docs.browserless.io/overview/connection-urls\#browserql-connection "Direct link to BrowserQL Connection")

If you are using the BQL IDE, the connection is handled for you (the IDE lets you select a region
and enters your token). However, advanced users can also call the BQL service directly via a
GraphQL HTTP request or WebSocket:

- **GraphQL HTTP Endpoint**: You can send a GraphQL HTTP POST to the base URL with
`/graphql`. For example: `POST https://production-sfo.browserless.io/graphql?token=YOUR_TOKEN`.
The body of the request should be a JSON with your GraphQL query or mutation. The
response will be JSON with your results. (This is usually used for the management
GraphQL API for checking session pressure, etc., not commonly for running BQL
browser sessions, which are handled by the dedicated BQL endpoint.)

- **Dedicated BQL Endpoint**: When running browser sessions with BQL, Browserless
uses a special endpoint internally (often shown as `/bql`). For instance, when a BQL
session is created, it may run at a URL like
`https://production-sfo.browserless.io/bql/SESSION_ID?token=YOUR_TOKEN`. This is typically abstracted away by the IDE or the initial request. In practice, you
will start a BQL session via the IDE or a GraphQL call, and if you need to reconnect to it
for a hybrid scenario, you'll use the reconnect URL provided in the response (which
looks like the above). In summary, for pure BQL usage, you normally don't manually
construct these URLs.


## BaaS v2 (Puppeteer/Playwright) Connection URLs [​](https://docs.browserless.io/overview/connection-urls\#baas-v2-puppeteerplaywright-connection-urls "Direct link to BaaS v2 (Puppeteer/Playwright) Connection URLs")

To connect an automation library to Browserless, use a WebSocket URL ( `wss://`). The
WebSocket endpoint tells Browserless to launch a browser for you and gives you control over it.
The format can vary slightly depending on the browser and library:

- **Puppeteer (Chrome/Chromium)**: Use the base WebSocket URL with your token.
Example: `wss://production-sfo.browserless.io?token=YOUR_TOKEN`. This
will launch a Chromium instance on Browserless. Puppeteer's browserWSEndpoint
should be set to this URL (see [How it Works](https://docs.browserless.io/baas/start)).



note





By default, this gives you a Chromium browser. Browserless treats Chrome/Chromium essentially the same; you can explicitly request Chrome by using `/chrome` in the path, but on the cloud service the default is a headless Chromium build with necessary features.

- **Playwright (Chromium via CDP)**: Playwright can connect over Chrome DevTools
Protocol (CDP) similarly to Puppeteer. You would use
`playwright.chromium.connect_over_cdp("wss://production-sfo.browserless.io?token=YOUR_TOKEN")`. This is effectively the same as Puppeteer's
approach and will give you a Chromium browser (see [Launch Options](https://docs.browserless.io/baas/chrome-flags)).

- **Playwright (Firefox)**: To use Firefox (since Playwright supports Firefox via its own
protocol), you must include the browser in the path and specify that you want the
Playwright protocol. Browserless uses a convention: `/<browser>/playwright` in the
URL for Playwright connections. So for Firefox:
`wss://production-sfo.browserless.io/firefox/playwright?token=YOUR_TOKEN` (see [How it Works](https://docs.browserless.io/baas/start)).

- **Playwright (WebKit)**:
`wss://production-sfo.browserless.io/webkit/playwright?token=YOUR_TOKEN` – spawns a WebKit browser (usually for Safari automation needs). WebKit
support is available in Browserless v2 for Playwright connections.

- **Selecting Chrome vs Chromium**: If you specifically need Chrome (the branded Google
Chrome, which might have minor differences or supports Widevine, etc.), you can use
the path `/chrome` in the URL. For example:
`wss://production-sfo.browserless.io/chrome?token=YOUR_TOKEN`. By
default, `/` or `/chromium` point to the latest Chromium. In practice, most use cases don't
require distinguishing, but the option exists.


### Summary of WebSocket URL formats [​](https://docs.browserless.io/overview/connection-urls\#summary-of-websocket-url-formats "Direct link to Summary of WebSocket URL formats")

- **Chromium (puppeteer, playwright ConnectOverCDP or other CDP libraries)**:
`wss://production-<region>.browserless.io/?token=YOUR_TOKEN`
- **Chromium (Playwright connect's method)**:
`wss://production-<region>.browserless.io/chromium/playwright?token=YOUR_TOKEN`
- **Chrome (stable version)**:
`wss://production-<region>.browserless.io/chrome?token=YOUR_TOKEN`
- **Firefox (Playwright)**:
`wss://production-<region>.browserless.io/firefox/playwright?token=YOUR_TOKEN`
- **WebKit (Playwright)**:
`wss://production-<region>.browserless.io/webkit/playwright?token=YOUR_TOKEN`

## REST APIs [​](https://docs.browserless.io/overview/connection-urls\#rest-apis "Direct link to REST APIs")

Browserless provides REST API endpoints for common operations:

```codeBlockLines_p187
// Screenshot API
https://production-sfo.browserless.io/screenshot?token=YOUR_TOKEN

// PDF API
https://production-sfo.browserless.io/pdf?token=YOUR_TOKEN

// Content API
https://production-sfo.browserless.io/content?token=YOUR_TOKEN

```

## Launch Parameters and Options [​](https://docs.browserless.io/overview/connection-urls\#launch-parameters-and-options "Direct link to Launch Parameters and Options")

Browserless allows extensive configuration of how browsers are launched and behave during
your sessions. These launch parameters can be provided either via query parameters in the
URL or through a special JSON launch payload. Whether you're using BQL, BaaS v2, or REST, these
options let you tweak the browser environment to fit your needs.

### Passing Launch Options [​](https://docs.browserless.io/overview/connection-urls\#passing-launch-options "Direct link to Passing Launch Options")

There are two ways to specify launch options on Browserless v2:

1. **Individual Query Parameters**: Many common options can be set by adding a query
parameter to your connection URL or API call. For example, `&headless=false` to run
in headful mode, `&proxy=residential` to use the built-in residential proxies, etc. This
is straightforward for boolean or simple options.

2. **Combined launch Parameter (JSON)**: For complex configurations, you can use a
single query param `launch` with a JSON string as its value. This JSON can include any
Chrome flags or Browserless-specific settings in a structured way. This approach is
useful when you need to set multiple flags at once or use non-boolean values. It's
essentially the equivalent of Puppeteer's `launch({ options })` but provided to the
cloud service. For example,
`&launch={"headless":false,"stealth":true,"args":["--window-size=1920,1080"]}` (URL-encoded) would configure a headful, stealth-enabled browser with
a specific window size (see [Launch Options](https://docs.browserless.io/baas/chrome-flags)).


Both methods achieve the same result. Under the hood, Browserless will merge any individual
query params with the JSON launch config if both are provided (individual params typically
override the JSON fields if there's overlap). For simplicity, if you only need to toggle a few
settings, use query params; if you have many settings, use the single launch param.

### Common Launch Options (Query Parameters) [​](https://docs.browserless.io/overview/connection-urls\#common-launch-options-query-parameters "Direct link to Common Launch Options (Query Parameters)")

Below is a list of common launch options you can use in query strings. Unless stated otherwise,
these can be used in BaaS v2 (library connections) and REST API calls alike. (BrowserQL
internally uses some of these, but BQL users typically set these via the IDE session settings
rather than manually in a URL.)

- **headless** (boolean): Default: true (headless mode). Set to false to launch the
browser in "headful" mode (with a GUI). In cloud environments you won't actually see a
GUI, but headful mode can sometimes bypass bot detection (since some bots detect
headless). Using `headless=false` will consume more resources. Example:
`&headless=false`.

- **stealth** (boolean): Default: false (for BaaS/REST). Enable stealth plugin/mode for
the browser. If true, Browserless will apply stealth techniques to the browser (like
puppeteer-extra's stealth plugin) to remove obvious automation signals. In BrowserQL,
stealth is generally always on by design (hence no toggle in BQL except through
humanlike). In BaaS, you might use `stealth=true` when you need some bot evasion
but are not using BQL. Example: `&stealth=true`.


You can also use the stealth URLs directly:

- `/chrome/stealth` \- For stealthy Chrome browser
- `/chromium/stealth` or `/stealth` \- For stealthy Chromium browser

These endpoints are only available for Enterprise and Cloud-unit plans and provide improved bot detection evasion compared to the stealth query parameter alone.

- **humanlike** (boolean): Default: false. (BrowserQL only.) This enables Human-like
behavior – simulation of human input patterns (mouse movements, random small
delays, etc.) to make automation less detectable. Example: `&humanlike=true`.

For a complete list of launch options, see the [Launch Options](https://docs.browserless.io/baas/chrome-flags) documentation.

- [Base URL and Regions](https://docs.browserless.io/overview/connection-urls#base-url-and-regions)
- [Using Your API Token in URLs](https://docs.browserless.io/overview/connection-urls#using-your-api-token-in-urls)
- [BrowserQL Connection](https://docs.browserless.io/overview/connection-urls#browserql-connection)
- [BaaS v2 (Puppeteer/Playwright) Connection URLs](https://docs.browserless.io/overview/connection-urls#baas-v2-puppeteerplaywright-connection-urls)
  - [Summary of WebSocket URL formats](https://docs.browserless.io/overview/connection-urls#summary-of-websocket-url-formats)
- [REST APIs](https://docs.browserless.io/overview/connection-urls#rest-apis)
- [Launch Parameters and Options](https://docs.browserless.io/overview/connection-urls#launch-parameters-and-options)
  - [Passing Launch Options](https://docs.browserless.io/overview/connection-urls#passing-launch-options)
  - [Common Launch Options (Query Parameters)](https://docs.browserless.io/overview/connection-urls#common-launch-options-query-parameters)