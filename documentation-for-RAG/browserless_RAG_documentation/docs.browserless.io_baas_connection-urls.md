---
url: "https://docs.browserless.io/baas/connection-urls"
title: "Connection URLs and Endpoints | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/connection-urls#__docusaurus_skipToContent_fallback)

Version: v2

On this page

This page explains all the connection URLs and endpoints available for **BaaS**, including how to authenticate with your API token, choose the optimal regional base URL, and connect using WebSocket or HTTP. Whether you're using Puppeteer or Playwright, this guide provides everything you need to connect and automate effectively.

## Base URL and Regions [​](https://docs.browserless.io/baas/connection-urls\#base-url-and-regions "Direct link to Base URL and Regions")

Browserless has multiple regional base URLs:

- `https://production-sfo.browserless.io` (US West)
- `https://production-lon.browserless.io` (Europe UK)
- `https://production-ams.browserless.io` (Europe Amsterdam)

For WebSocket connections, simply replace `https://` with `wss://` for the same host. For
example:

- WebSocket (Puppeteer/Playwright): `wss://production-sfo.browserless.io/...`
- HTTP REST API call: `https://production-sfo.browserless.io/...`

Choose the region closest to you to reduce latency (see [Load Balancers](https://docs.browserless.io/baas/load-balancers)). All require the token query parameter.

## Using Your API Token in URLs [​](https://docs.browserless.io/baas/connection-urls\#using-your-api-token-in-urls "Direct link to Using Your API Token in URLs")

Add your API token to the URL query string as `?token=YOUR_TOKEN`. Required for authentication (see [BaaS Connection URL Builder](https://docs.browserless.io/baas/connection-urls)). Invalid tokens result in HTTP 401/403 errors. Keep this URL secure and never expose it in client-side code or logs.

Example:
`wss://production-sfo.browserless.io/chrome?token=094632bb-e326-4c63-b953-82b55700b14c` is a basic connection string for a new Chrome session on the SFO cluster using the given token.

Below you can select your preferences of region, library, stealth mode and browser to define your URL:

### BaaS Connection URL Builder

Service Type:

BaaS v2

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

## BaaS v2 (Puppeteer/Playwright) Connection URLs [​](https://docs.browserless.io/baas/connection-urls\#baas-v2-puppeteerplaywright-connection-urls "Direct link to BaaS v2 (Puppeteer/Playwright) Connection URLs")

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


### Summary of WebSocket URL formats [​](https://docs.browserless.io/baas/connection-urls\#summary-of-websocket-url-formats "Direct link to Summary of WebSocket URL formats")

The following are URL formats for each browser available:

- **Chromium (Puppeteer or CDP)**:
`wss://production-<region>.browserless.io/?token=YOUR_TOKEN`
- **Chromium (Playwright server mode)**:
`wss://production-<region>.browserless.io/chromium/playwright?token=YOUR_TOKEN`
- **Chrome (explicit)**:
`wss://production-<region>.browserless.io/chrome?token=YOUR_TOKEN`
- **Firefox (Playwright)**:
`wss://production-<region>.browserless.io/firefox/playwright?token=YOUR_TOKEN`
- **WebKit (Playwright)**:
`wss://production-<region>.browserless.io/webkit/playwright?token=YOUR_TOKEN`

- [Base URL and Regions](https://docs.browserless.io/baas/connection-urls#base-url-and-regions)
- [Using Your API Token in URLs](https://docs.browserless.io/baas/connection-urls#using-your-api-token-in-urls)
- [BaaS v2 (Puppeteer/Playwright) Connection URLs](https://docs.browserless.io/baas/connection-urls#baas-v2-puppeteerplaywright-connection-urls)
  - [Summary of WebSocket URL formats](https://docs.browserless.io/baas/connection-urls#summary-of-websocket-url-formats)