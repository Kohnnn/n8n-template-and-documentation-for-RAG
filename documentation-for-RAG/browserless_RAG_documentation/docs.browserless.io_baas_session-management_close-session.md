---
url: "https://docs.browserless.io/baas/session-management/close-session"
title: "Close Browser Sessions | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/session-management/close-session#__docusaurus_skipToContent_fallback)

Version: v2

When finished with work, or on errors, make sure you run `browser.close` so that other sessions may start. browserless _will_ terminate long-running sessions via the timeout setting, but it's always a good idea to close tidly whenever you're finished.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const TOKEN = "YOUR_API_TOKEN_HERE";

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io?token=${TOKEN}`,
});

const page = await browser.newPage();

try {
  await page.goto("https://www.browserless.io/");
  await page.screenshot({ path: "./browserless.png" });
  browser.close();
} catch (error) {
  console.error({ error }, "Something happened!");
  browser.close();
}

```

```codeBlockLines_p187
import playwright from "playwright";

const TOKEN = "YOUR_API_TOKEN_HERE";

const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io?token=${TOKEN}`
);

const page = await browser.newPage();

try {
  await page.goto("https://www.browserless.io/");
  await page.screenshot({ path: "./browserless.png" });
  browser.close();
} catch (error) {
  console.error({ error }, "Something happened!");
  browser.close();
}

```