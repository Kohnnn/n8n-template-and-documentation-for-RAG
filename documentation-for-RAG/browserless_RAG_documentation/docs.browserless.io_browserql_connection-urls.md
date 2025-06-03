---
url: "https://docs.browserless.io/browserql/connection-urls"
title: "Connection URLs and Endpoints | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/connection-urls#__docusaurus_skipToContent_fallback)

On this page

This page explains all the connection URLs and endpoints available for **BrowserQL**, including how to authenticate with your API token, choose the right regional base URL, and interact with the BQL service. Whether you're using the BQL IDE or making direct API calls, this guide covers everything you need to connect and start automating.

## Base URL and Regions [​](https://docs.browserless.io/browserql/connection-urls\#base-url-and-regions "Direct link to Base URL and Regions")

Browserless has multiple regional base URLs:

- `https://production-sfo.browserless.io` (US West)
- `https://production-lon.browserless.io` (Europe UK)
- `https://production-ams.browserless.io` (Europe Amsterdam)

Choose the region closest to you to reduce latency (see [Load Balancers](https://docs.browserless.io/baas/load-balancers)). All require the token query parameter.

## Using Your API Token in URLs [​](https://docs.browserless.io/browserql/connection-urls\#using-your-api-token-in-urls "Direct link to Using Your API Token in URLs")

Add your API token to the URL query string as `?token=YOUR_TOKEN`. Required for authentication (see see [BQL Connection URL Builder](https://docs.browserless.io/browserql/connection-urls)). Invalid tokens result in HTTP 401/403 errors. Keep this URL secure and never expose it in client-side code or logs.

Example:
`https://production-sfo.browserless.io/chromium/bql?token=094632bb-e326-4c63-b953-82b55700b14c` is a basic connection string for a new Chromium session on the SFO cluster using the given token.

Below you can select your preferences of region and browser to define your URL:

### BQL Connection URL Builder

Service Type:

BrowserQL

Browser:

ChromiumChrome

Region:

US WestEurope UKEurope Amsterdam

API Token:

#### Connection URL:

Copy

```
https://production-sfo.browserless.io/chromium/bql?token=YOUR_TOKEN
```

#### Code Snippet:

Copy

```
const response = await fetch('https://production-sfo.browserless.io/chromium/bql?token=YOUR_TOKEN', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    query: `mutation MyQuery($url: String!) {
      goto(url: $url) {
        status
      }
      # Add more BQL operations here
    }`,
    variables: { url: 'https://example.com' }
  }),
});
```

## BrowserQL Connection [​](https://docs.browserless.io/browserql/connection-urls\#browserql-connection "Direct link to BrowserQL Connection")

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


- [Base URL and Regions](https://docs.browserless.io/browserql/connection-urls#base-url-and-regions)
- [Using Your API Token in URLs](https://docs.browserless.io/browserql/connection-urls#using-your-api-token-in-urls)
- [BrowserQL Connection](https://docs.browserless.io/browserql/connection-urls#browserql-connection)