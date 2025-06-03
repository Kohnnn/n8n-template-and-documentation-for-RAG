---
url: "https://docs.browserless.io/browserql/start"
title: "BrowserQL | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/start#__docusaurus_skipToContent_fallback)

On this page

Browserless is a cloud-based service for running headless browsers at scale, and **BrowserQL** is our first-class browser automation API, and includes powerful options like human-like, reconnecting and proxying. It's a full rethink of how to do browser automation with a minimalistic stealth-first approach. It combines many decades of development and research, and includes a fully-featured editor, with a live view of the session, and built-in docs. No more context switching!

## What is BrowserQL? [​](https://docs.browserless.io/browserql/start\#what-is-browserql "Direct link to What is BrowserQL?")

**BrowserQL** (BQL) is a GraphQL-based API for browser automation. BQL is a first-class, stealth-focused solution ideal for bypassing CAPTCHAs and bot detectors. It comes with a fully-featured web IDE and uses a minimalistic, scriptable query language instead of traditional code.

BQL redefines how browser automation is done. Instead of traditional code, BQL uses a minimal, scriptable query language that’s purpose-built for human-like automation. It’s tightly integrated with a powerful web-based IDE that includes:

- A live session preview.
- Built-in documentation.
- No installation or CLI required.
- Zero context switching.

This makes it ideal for developers and automation engineers who want to move fast without sacrificing control or stealth.

## Why Use BrowserQL? [​](https://docs.browserless.io/browserql/start\#why-use-browserql "Direct link to Why Use BrowserQL?")

BrowserQL is the **best solution** when you need to:

- Bypass **advanced bot detection systems**.
- Automate **CAPTCHA-solving flows**.
- Mimic **human-like interactions** reliably.
- Build **stealth-first automations** at scale.

With decades of research and development behind it, BrowserQL is a production-grade solution designed to succeed where traditional browser automation fails.

## Getting Started [​](https://docs.browserless.io/browserql/start\#getting-started "Direct link to Getting Started")

To begin using BQL:

1. [Sign up for a Browserless account](https://account.browserless.io/signup/email?plan=free) (free plan available).
2. Get your **API Key**.
3. Access the BQL web editor: [https://account.browserless.io/bql](https://account.browserless.io/bql).

Everything is accessible via your account dashboard—no installations required.

Requirements

BrowserQL does not require any CLI tools, local runtime, or libraries. All you need is a Browserless account to access the cloud editor and generate your API key.

## Global Endpoints [​](https://docs.browserless.io/browserql/start\#global-endpoints "Direct link to Global Endpoints")

Browserless operates multiple regional endpoints for low-latency access. The primary shared clusters are in US West (SFO), EU West (London), and EU Central (Amsterdam) ( [Load Balancers](https://docs.browserless.io/baas/load-balancers)). For example:

- `https://production-sfo.browserless.io` – San Francisco, USA (default US endpoint)
- `https://production-lon.browserless.io` – London, UK (European endpoint)
- `https://production-ams.browserless.io` – Amsterdam, NL (another EU endpoint)

You can use the endpoint closest to your servers or users. All endpoints offer the same API and require your token.

## Next Steps [​](https://docs.browserless.io/browserql/start\#next-steps "Direct link to Next Steps")

Before exploring all BQL has to offer, learn more about connecting and building an URL for your needs, and all launch parameters available:

- [Connection URLs and Endpoints](https://docs.browserless.io/browserql/connection-urls)
- [Launch Parameters and Options](https://docs.browserless.io/browserql/launch-parameters)

Want to explore more?

If you already have an automation library that works over WebSockets, you can mix-and-match BrowserQL with the library of your choice. To learn how to integrate BQL, check the guides below:

- [Connecting with Puppeteer](https://docs.browserless.io/browserql/connecting-libraries/puppeteer)
- [Connecting with Playwright](https://docs.browserless.io/browserql/connecting-libraries/playwright)

There's a lot more to BQL than just this. Our Editor comes with built-in documentation, a live Viewer and Devtools to get you started. Refer to the following pages to learn more about BQL:

- [Acessing Pages with Bot Detection](https://docs.browserless.io/browserql/bot-detection/accessing-pages)
- [Writing BQL Queries](https://docs.browserless.io/browserql/writing-bql/language-basics)
- [Mutation Reference](https://docs.browserless.io/bql-schema/schema)
- [Using the IDE](https://docs.browserless.io/browserql/using-the-ide/ide-features)

- [What is BrowserQL?](https://docs.browserless.io/browserql/start#what-is-browserql)
- [Why Use BrowserQL?](https://docs.browserless.io/browserql/start#why-use-browserql)
- [Getting Started](https://docs.browserless.io/browserql/start#getting-started)
- [Global Endpoints](https://docs.browserless.io/browserql/start#global-endpoints)
- [Next Steps](https://docs.browserless.io/browserql/start#next-steps)