---
url: "https://docs.browserless.io/rest-apis/connection-urls"
title: "Connection URLs and Endpoints | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/connection-urls#__docusaurus_skipToContent_fallback)

On this page

This page explains all the connection URLs and endpoints available for **BrowserQL**, including how to authenticate with your API token, choose the right regional base URL, and interact with the BQL service. Whether you're using the BQL IDE or making direct API calls, this guide covers everything you need to connect and start automating.

## Base URL and Regions [​](https://docs.browserless.io/rest-apis/connection-urls\#base-url-and-regions "Direct link to Base URL and Regions")

Browserless has multiple regional base URLs:

- `https://production-sfo.browserless.io` (US West)
- `https://production-lon.browserless.io` (Europe UK)
- `https://production-ams.browserless.io` (Europe Amsterdam)

Choose the region closest to you to reduce latency (see [Load Balancers](https://docs.browserless.io/baas/load-balancers)). All require the token query parameter.

## Using Your API Token in URLs [​](https://docs.browserless.io/rest-apis/connection-urls\#using-your-api-token-in-urls "Direct link to Using Your API Token in URLs")

Add your API token to the URL query string as `?token=YOUR_TOKEN`. Required for authentication (see see [BQL Connection URL Builder](https://docs.browserless.io/browserql/connection-urls)). Invalid tokens result in HTTP 401/403 errors. Keep this URL secure and never expose it in client-side code or logs.

Example:
`https://production-sfo.browserless.io/chromium/bql?token=094632bb-e326-4c63-b953-82b55700b14c` is a basic connection string for a new Chromium session on the SFO cluster using the given token.

Below you can select your preferences of region and browser to define your URL:

### REST API Connection URL Builder

Service Type:

REST API

Endpoint:

ScreenshotPDFContentDownloadExportfunctionUnblockScrapePerformance

Region:

US WestEurope UKEurope Amsterdam

API Token:

#### Connection URL:

Copy

```
https://production-sfo.browserless.io/screenshot?token=YOUR_TOKEN
```

#### Code Snippet:

Copy

```
curl -X POST \
  'https://production-sfo.browserless.io/screenshot?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://example.com"
  }'
```

- [Base URL and Regions](https://docs.browserless.io/rest-apis/connection-urls#base-url-and-regions)
- [Using Your API Token in URLs](https://docs.browserless.io/rest-apis/connection-urls#using-your-api-token-in-urls)