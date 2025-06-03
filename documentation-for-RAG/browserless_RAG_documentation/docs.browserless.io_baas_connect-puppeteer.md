---
url: "https://docs.browserless.io/baas/connect-puppeteer"
title: "Connecting Puppeteer | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/connect-puppeteer#__docusaurus_skipToContent_fallback)

Version: v2

On this page

Libraries like puppeteer and chrome-remote-interface can hook into an existing Chrome instance by websocket. The hosted Browserless service only supports this type of interface since you can pass in tokens and other query-params. Typically you only need to replace how you start Chrome with a connect-like statement:

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

// Connecting to Chrome locally
const browser = await puppeteer.launch();

// Connecting to Browserless and using a proxy
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=${TOKEN}&proxy=residential`,
});

```

## More Puppeteer Details [​](https://docs.browserless.io/baas/connect-puppeteer\#more-puppeteer-details "Direct link to More Puppeteer Details")

Puppeteer is well-supported by Browserless, and is easy to upgrade an existing service or app to use it.

### Basic Usage [​](https://docs.browserless.io/baas/connect-puppeteer\#basic-usage "Direct link to Basic Usage")

In order to use the Browserless service, simply change the following:

#### Before browserless [​](https://docs.browserless.io/baas/connect-puppeteer\#before-browserless "Direct link to Before browserless")

```codeBlockLines_p187
import puppeteer from "puppeteer";

const browser = await puppeteer.launch();
const page = await browser.newPage();
// ...

```

#### After browserless [​](https://docs.browserless.io/baas/connect-puppeteer\#after-browserless "Direct link to After browserless")

```codeBlockLines_p187
import puppeteer from "puppeteer";

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE`,
});
const page = await browser.newPage();

```

If you're running the docker container to replace the location of `wss://production-sfo.browserless.io/` to wherever your container is running.

### Code Snippet [​](https://docs.browserless.io/baas/connect-puppeteer\#code-snippet "Direct link to Code Snippet")

Below is a copy-paste example (remember to replace the API key for yours!) that should be a great starting point since it shows how to use puppeteer's methods with basic exception handling and file saving:

```codeBlockLines_p187
import puppeteer from "puppeteer-core";
import fs from "fs";

async function main() {
  let browser = null;

  try {
    const url = "https://www.example.com";
    const token = "YOUR_API_TOKEN_HERE";
    const launchArgs = JSON.stringify({
      args: [`--window-size=1920,1080`],
      headless: false,
      stealth: true,
      timeout: 30000
    });

    console.log("Connecting to browser...");
    browser = await puppeteer.connect({
      browserWSEndpoint: `wss://production-sfo.browserless.io/?token=${token}&launch=${launchArgs}`,
    });

    console.log("Creating new page...");
    const page = await browser.newPage();

    page.setViewport({ width: 1920, height: 1080 }) //it's best to use this in addition to --window-size
    await page.setUserAgent('My Custom User Agent/1.0');
    console.log(`User agent: ${await page.evaluate(() => navigator.userAgent)}`);
    console.log(`Viewport size: ${JSON.stringify(await page.viewport())}`);
    console.log("Navigating to example.com...");
    await page.goto(url);

    const title = await page.title();
    console.log(`The page's title is: ${title}`);
    const html = await page.content();
    fs.writeFileSync("example.html", html);
    console.log(`HTML file saved.`);
    await page.screenshot({ path: "example.png" });
    console.log(`Screenshot saved.`);
    const pdfBuffer = await page.pdf({ format: "A4" });
    fs.writeFileSync("example.pdf", pdfBuffer);
    console.log(`PDF file saved.`);

  } catch (error) {
    console.error("An error occurred:", error.message);
  } finally {
    if (browser) {
      try {
        console.log("Closing browser...");
        await browser.close();
      } catch (closeError) {
        console.error("Error while closing browser:", closeError.message);
      }
    }
  }
}
// Run the main function
main().catch(error => {
  console.error("Unhandled error in main function:", error);
});

```

Connecting to unlocked browser sessions

If your Puppeteer scripts are getting blocked by bot detectors, you can use [**BrowserQL**](https://docs.browserless.io/browserql/start) to generate a browser instance with advanced stealth features, that you can then connect to with the provided `browserWSEndpoint` and cookies.

## Reduce `await`'s as much as possible [​](https://docs.browserless.io/baas/connect-puppeteer\#reduce-awaits-as-much-as-possible "Direct link to reduce-awaits-as-much-as-possible")

Most of the puppeteer is async, meaning any command with `await` in front of it (or `.then`'s) is going to make a round-trip from your application to browserless and back. While you can only do so much to limit this you should definitely try and do as much as possible. For instance, use `page.evaluate` over `page.$selector` as you can accomplish a lot in one `evaluate` versus multiple `$selector` calls.

**DON'T DO**

```codeBlockLines_p187
const $button = await page.$(".buy-now");
const buttonText = await $button.getProperty("innerText");
const clicked = await $button.click();

```

**DO**

```codeBlockLines_p187
const buttonText = await page.evaluate(() => {
  const $button = document.querySelector(".buy-now");
  const clicked = $button.click();

  return $button.innerText;
});

```

- [More Puppeteer Details](https://docs.browserless.io/baas/connect-puppeteer#more-puppeteer-details)
  - [Basic Usage](https://docs.browserless.io/baas/connect-puppeteer#basic-usage)
  - [Code Snippet](https://docs.browserless.io/baas/connect-puppeteer#code-snippet)
- [Reduce `await`'s as much as possible](https://docs.browserless.io/baas/connect-puppeteer#reduce-awaits-as-much-as-possible)