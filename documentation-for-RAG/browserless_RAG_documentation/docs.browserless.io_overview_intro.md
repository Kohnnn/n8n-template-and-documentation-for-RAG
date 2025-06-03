---
url: "https://docs.browserless.io/overview/intro"
title: "Introduction to Browserless | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/overview/intro#__docusaurus_skipToContent_fallback)

On this page

Browserless is a cloud-based service for running headless browsers at scale. It provides multiple offerings for different use cases, all using the same cloud infrastructure but accessed in various ways. This overview introduces the three main Browserless offerings (excluding legacy v1, which is deprecated) and when to use each:

- **[BrowserQL (BQL)](https://docs.browserless.io/browserql/start)** – A GraphQL-based API for browser automation. BQL is a first-class, stealth-focused solution ideal for bypassing [CAPTCHAs](https://docs.browserless.io/browserql/bot-detection/solving-captchas) and bot detectors. It comes with a fully-featured web IDE and uses a minimalistic, scriptable query language instead of traditional code.

- **[Browsers as a Service (BaaS) v2](https://docs.browserless.io/baas/start)** – A direct browser-as-a-service API that you can connect to using standard libraries like [Puppeteer](https://docs.browserless.io/baas/start#connecting-puppeteer) or [Playwright](https://docs.browserless.io/baas/start#connecting-playwright). BaaS v2 closely mimics running a browser locally, allowing you to use familiar code by simply changing the connection URL to point at Browserless.

- **[RESTful APIs](https://docs.browserless.io/rest-apis/intro)** – A set of ready-made HTTP endpoints for common browser tasks (such as generating PDFs or screenshots, scraping content, etc.). These endpoints let you perform automation via simple HTTP(S) requests without writing a full script. They are great for quick integrations or one-off tasks, although not as flexible for complex flows.


Which to choose?

Don't know which solution better fits your needs? Refer to the [API Comparison page](https://docs.browserless.io/overview/comparison), and find detailed information defining the best solution for each situation.

## API Tokens and Authentication [​](https://docs.browserless.io/overview/intro\#api-tokens-and-authentication "Direct link to API Tokens and Authentication")

All Browserless cloud offerings require an API token for authentication. When you sign up, you'll get a unique token associated with your account. Include this token in every request, usually as a query parameter `?token=<YOUR_API_TOKEN>`. (The token can also be provided via headers in some cases, but using the token in query strings is most reliable.) [Get your API token](https://account.browserless.io/).

## Global Endpoints [​](https://docs.browserless.io/overview/intro\#global-endpoints "Direct link to Global Endpoints")

Browserless operates multiple regional endpoints for low-latency access. The primary shared clusters are in US West (SFO), EU West (London), and EU Central (Amsterdam) ( [Load Balancers](https://docs.browserless.io/baas/load-balancers)). For example:

- `https://production-sfo.browserless.io` – San Francisco, USA (default US endpoint)
- `https://production-lon.browserless.io` – London, UK (European endpoint)
- `https://production-ams.browserless.io` – Amsterdam, NL (another EU endpoint)

You can use the endpoint closest to your servers or users. All endpoints offer the same API and require your token.

## Getting Started Checklist [​](https://docs.browserless.io/overview/intro\#getting-started-checklist "Direct link to Getting Started Checklist")

To quickly get started with Browserless:

1. [Get your API token](https://account.browserless.io/)
2. Choose an API ( [BrowserQL](https://docs.browserless.io/browserql/start), [BaaS v2](https://docs.browserless.io/baas/start), or [REST APIs](https://docs.browserless.io/rest-apis/intro))
3. Follow the respective Quick Start guide for your chosen API

- [API Tokens and Authentication](https://docs.browserless.io/overview/intro#api-tokens-and-authentication)
- [Global Endpoints](https://docs.browserless.io/overview/intro#global-endpoints)
- [Getting Started Checklist](https://docs.browserless.io/overview/intro#getting-started-checklist)