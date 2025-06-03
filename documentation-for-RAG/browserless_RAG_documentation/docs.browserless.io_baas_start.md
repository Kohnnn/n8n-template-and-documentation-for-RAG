---
url: "https://docs.browserless.io/baas/start"
title: "Browsers as a Service | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/start#__docusaurus_skipToContent_fallback)

Version: v2

On this page

Browserless is a cloud-based service for running headless browsers at scale. **Browsers as a Service (BaaS) v2** is a direct browser-as-a-service API that you can connect to using standard libraries like Puppeteer or Playwright. BaaS v2 closely mimics running a browser locally, allowing you to use familiar code by simply changing the connection URL to point at Browserless.

Ideal use case

BaaS features are best suited for sites where bot detection isn't an issue, especially your own site. For getting past detectors, we'd recommend checking out [**BrowserQL**](https://docs.browserless.io/browserql/start).

## How Browserless Works [​](https://docs.browserless.io/baas/start\#how-browserless-works "Direct link to How Browserless Works")

Browserless works almost identically to how most libraries and web-drivers work when ran locally. There's no additional software you need to install on your production machines or complicated setup steps. As a matter of fact, the only thing you really need to when using the Browserless' service is merely change where your code references the browser.

Browserless runs browsers in a cloud environment, and exposes most of the Chrome DevTools protocol and the Playwright Protocols to you. On top of exposing these commands, it also:

- Isolates your session from all others.
- Can run concurrent requests without interfering with others.
- Cleans up sessions after 30 seconds.
- Starts a clean copy of a browser for each session.
- Restarts automatically if anything crashes.
- Queues requests if thresholds are met.
- Helps bypass bot detectors.

You can use the hosted service either by connecting an automation library as described below, or by using one of our HTTP APIs.

## Getting Started [​](https://docs.browserless.io/baas/start\#getting-started "Direct link to Getting Started")

To use BaaS, you need a unique token, created when you sign-up for a Browserless account:

1. [Sign up for a Browserless account](https://account.browserless.io/signup/email?plan=free) (free plan available).
2. Get your **API Key**.

Once your worker(s) are ready you should use this token anytime you interact with the service.

You can use this token with most of our integrations by simply appending a `?token=YOUR_API_TOKEN_HERE` as a query-string parameter.

## Global Endpoints [​](https://docs.browserless.io/baas/start\#global-endpoints "Direct link to Global Endpoints")

Browserless operates multiple regional endpoints for low-latency access. The primary shared clusters are in US West (SFO), EU West (London), and EU Central (Amsterdam) ( [Load Balancers](https://docs.browserless.io/baas/load-balancers)). For example:

- `https://production-sfo.browserless.io` – San Francisco, USA (default US endpoint)
- `https://production-lon.browserless.io` – London, UK (European endpoint)
- `https://production-ams.browserless.io` – Amsterdam, NL (another EU endpoint)

You can use the endpoint closest to your servers or users. All endpoints offer the same API and require your token.

## Connecting Libraries [​](https://docs.browserless.io/baas/start\#connecting-libraries "Direct link to Connecting Libraries")

BaaS can be connected to standard libraries like Puppeteer or Playwright. The pages below guide you through an example on how to connect to your preffered choice:

- [Connecting Puppeteer](https://docs.browserless.io/baas/connect-puppeteer)
- [Connecting Playwright](https://docs.browserless.io/baas/connect-playwright)

## Next Steps [​](https://docs.browserless.io/baas/start\#next-steps "Direct link to Next Steps")

Before exploring all BaaS has to offer, learn more about connecting and building an URL for your needs, and all launch parameters available:

- [Connection URLs and Endpoints](https://docs.browserless.io/baas/connection-urls)
- [Launch Parameters and Options](https://docs.browserless.io/baas/chrome-flags)

Want to explore more?

BaaS provides a wide range of functionalities that help your web scraping process. To discover all the capabilities Browserless has to offer, start with the following guides:

- [Cloud Services](https://docs.browserless.io/baas/session-management/reconnect)
- [REST APIs](https://docs.browserless.io/rest-apis/intro)
- [Utility Functions](https://docs.browserless.io/enterprise/utility-functions/intro)

**Advanced Features**

Learn about more advanced features that you can take advantage when using BaaS:

- [Human-in-the-Loop Automations](https://docs.browserless.io/baas/hybrid-automation)
- [Screencasting](https://docs.browserless.io/baas/session-management/screencasting)
- [Live debugger](https://docs.browserless.io/enterprise/live-debugger)

- [How Browserless Works](https://docs.browserless.io/baas/start#how-browserless-works)
- [Getting Started](https://docs.browserless.io/baas/start#getting-started)
- [Global Endpoints](https://docs.browserless.io/baas/start#global-endpoints)
- [Connecting Libraries](https://docs.browserless.io/baas/start#connecting-libraries)
- [Next Steps](https://docs.browserless.io/baas/start#next-steps)