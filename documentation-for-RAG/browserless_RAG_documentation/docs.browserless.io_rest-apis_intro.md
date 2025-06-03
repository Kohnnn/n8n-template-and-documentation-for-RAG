---
url: "https://docs.browserless.io/rest-apis/intro"
title: "REST APIs | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/rest-apis/intro#__docusaurus_skipToContent_fallback)

On this page

Browserless is a cloud-based service for running headless browsers at scale. It provides multiple offerings for different use cases, all using the same cloud infrastructure but accessed in various ways.

Browserless RESTful APIs are a set of ready-made HTTP endpoints for common browser tasks (such as generating PDFs or screenshots, scraping content, etc.). These endpoints let you perform automation via simple HTTP(S) requests without writing a full script. They are great for quick integrations or one-off tasks, although not as flexible for complex flows.

## Benefits of REST APIs [​](https://docs.browserless.io/rest-apis/intro\#benefits-of-rest-apis "Direct link to Benefits of REST APIs")

- **Simplicity**: Interact with browser functionality using simple HTTP requests
- **Language Agnostic**: Use any programming language or tool that can make HTTP requests
- **Stateless Operations**: No need to maintain browser sessions for simple operations
- **Scalability**: Easily integrate browser functionality into your applications at scale
- **Low Overhead**: Minimize resource usage for simple browser tasks

## When to Use REST APIs [​](https://docs.browserless.io/rest-apis/intro\#when-to-use-rest-apis "Direct link to When to Use REST APIs")

REST APIs are ideal for:

- Simple, one-off browser operations (screenshots, PDF generation, content extraction)
- Integrations where maintaining a browser session is unnecessary
- Applications written in languages without robust browser automation libraries
- Serverless functions or microservices where simplicity is paramount
- High-throughput scenarios where connection overhead should be minimized

For more complex automation scenarios, especially those involving bot detection bypass, consider using [BrowserQL](https://docs.browserless.io/browserql/start), which provides a more powerful and flexible approach.

## Getting Started [​](https://docs.browserless.io/rest-apis/intro\#getting-started "Direct link to Getting Started")

To use the APIs, you need a unique token, created when you sign-up for a Browserless account:

1. [Sign up for a Browserless account](https://account.browserless.io/signup/email?plan=free) (free plan available).
2. Get your **API Key**.

Once ready you should use this token anytime you interact with the service.

You can use this token with most of our integrations by simply appending a `?token=YOUR_API_TOKEN_HERE` as a query-string parameter.

## Global Endpoints [​](https://docs.browserless.io/rest-apis/intro\#global-endpoints "Direct link to Global Endpoints")

Browserless operates multiple regional endpoints for low-latency access. The primary shared clusters are in US West (SFO), EU West (London), and EU Central (Amsterdam) ( [Load Balancers](https://docs.browserless.io/baas/load-balancers)). For example:

- `https://production-sfo.browserless.io` – San Francisco, USA (default US endpoint)
- `https://production-lon.browserless.io` – London, UK (European endpoint)
- `https://production-ams.browserless.io` – Amsterdam, NL (another EU endpoint)

You can use the endpoint closest to your servers or users. All endpoints offer the same API and require your token.

## Available REST APIs [​](https://docs.browserless.io/rest-apis/intro\#available-rest-apis "Direct link to Available REST APIs")

Browserless has production ready APIs for various browser operations. Each API accepts different parameters and options.

Schemas

The schemas for each endpoint are displayed in the [Browserless OpenAPI Documentation](https://docs.browserless.io/open-api).

The Browser APIs help you execute specific tasks for your use-case, and are available for both shared and enterprise users.

- [/content](https://docs.browserless.io/rest-apis/content), to return HTML of dynamic content
- [/unblock](https://docs.browserless.io/rest-apis/unblock), to return HTML, screenshots or cookies for protected sites
- [/download](https://docs.browserless.io/rest-apis/download), return files Chrome has downloaded
- [/function](https://docs.browserless.io/rest-apis/function), run HTTP requests without installing a library
- [/pdf](https://docs.browserless.io/rest-apis/pdf), export a page as a PDF
- [/screenshot](https://docs.browserless.io/rest-apis/screenshot), capture a .png or .jpg
- [/scrape](https://docs.browserless.io/rest-apis/scrape), return the structured JSON
- [/export](https://docs.browserless.io/rest-apis/export), create self-contained exports of any URL resource for offline access, optionally including all linked resources (images, CSS, JavaScript) as a zip file
- [/performance](https://docs.browserless.io/rest-apis/performance), run parallel Google Lighthouse tests

Bot Detection

For strict bot detectors where browsers and a proxy aren't enough to get past, we would recommend using [**BrowserQL**](https://docs.browserless.io/browserql/start).

## Next Steps [​](https://docs.browserless.io/rest-apis/intro\#next-steps "Direct link to Next Steps")

Before exploring all Browserless REST APIs have to offer, learn more about connecting and building an URL for your needs, and all launch parameters available:

- [Connection URLs and Endpoints](https://docs.browserless.io/rest-apis/connection-urls)
- [Launch Parameters and Options](https://docs.browserless.io/rest-apis/launch-parameters)

- [Benefits of REST APIs](https://docs.browserless.io/rest-apis/intro#benefits-of-rest-apis)
- [When to Use REST APIs](https://docs.browserless.io/rest-apis/intro#when-to-use-rest-apis)
- [Getting Started](https://docs.browserless.io/rest-apis/intro#getting-started)
- [Global Endpoints](https://docs.browserless.io/rest-apis/intro#global-endpoints)
- [Available REST APIs](https://docs.browserless.io/rest-apis/intro#available-rest-apis)
- [Next Steps](https://docs.browserless.io/rest-apis/intro#next-steps)