---
url: "https://pptr.dev/next"
title: "Puppeteer | Puppeteer"
---

[Skip to main content](https://pptr.dev/next#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/)** (24.9.0).

Version: Next

[![build](https://github.com/puppeteer/puppeteer/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/puppeteer/puppeteer/actions/workflows/ci.yml)[![npm puppeteer package](https://img.shields.io/npm/v/puppeteer.svg)](https://npmjs.org/package/puppeteer)

![](https://user-images.githubusercontent.com/10379601/29446482-04f7036a-841f-11e7-9872-91d1fc2ea683.png)

> Puppeteer is a JavaScript library which provides a high-level API to control
> Chrome or Firefox over the
> [DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) or [WebDriver BiDi](https://pptr.dev/webdriver-bidi).
> Puppeteer runs in the headless (no visible UI) by default

## [Get started](https://pptr.dev/docs) \| [API](https://pptr.dev/api) \| [FAQ](https://pptr.dev/faq) \| [Contributing](https://pptr.dev/contributing) \| [Troubleshooting](https://pptr.dev/troubleshooting) [​](https://pptr.dev/next\#get-started--api--faq--contributing--troubleshooting "Direct link to get-started--api--faq--contributing--troubleshooting")

## Installation [​](https://pptr.dev/next\#installation "Direct link to Installation")

- npm
- Yarn
- pnpm

```codeBlockLines_RjmQ
npm i puppeteer # Downloads compatible Chrome during installation.
npm i puppeteer-core # Alternatively, install as a library, without downloading Chrome.

```

```codeBlockLines_RjmQ
yarn add puppeteer # Downloads compatible Chrome during installation.
yarn add puppeteer-core # Alternatively, install as a library, without downloading Chrome.

```

```codeBlockLines_RjmQ
pnpm add puppeteer # Downloads compatible Chrome during installation.
pnpm add puppeteer-core # Alternatively, install as a library, without downloading Chrome.

```

## Example [​](https://pptr.dev/next\#example "Direct link to Example")

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';
// Or import puppeteer from 'puppeteer-core';

// Launch the browser and open a new blank page
const browser = await puppeteer.launch();
const page = await browser.newPage();

// Navigate the page to a URL.
await page.goto('https://developer.chrome.com/');

// Set screen size.
await page.setViewport({width: 1080, height: 1024});

// Type into search box using accessible input name.
await page.locator('aria/Search').fill('automate beyond recorder');

// Wait and click on first result.
await page.locator('.devsite-result-item-link').click();

// Locate the full title with a unique string.
const textSelector = await page
  .locator('text/Customize and automate')
  .waitHandle();
const fullTitle = await textSelector?.evaluate(el => el.textContent);

// Print the full title.
console.log('The title of this blog post is "%s".', fullTitle);

await browser.close();

```

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!