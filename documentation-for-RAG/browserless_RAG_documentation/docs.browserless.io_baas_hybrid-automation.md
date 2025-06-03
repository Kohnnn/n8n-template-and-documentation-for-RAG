---
url: "https://docs.browserless.io/baas/hybrid-automation"
title: "Hybrid automation - human in the loop | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/hybrid-automation#__docusaurus_skipToContent_fallback)

Version: v2

On this page

info

Hybrid Automation is only available on paid plans.

Hybrid automation allows you to have humans intervene in an automation workflow, or even take complete control. This is useful in case a user needs to input their credentials, handle 2FA or simply perform some actions on a website before resuming automation. This can be done with Puppeteer, Playwright and virtually any library that supports CDP connections.

![hybrid automation preview](https://docs.browserless.io/img/hybrid_automation.gif)

## Default behavior [​](https://docs.browserless.io/baas/hybrid-automation\#default-behavior "Direct link to Default behavior")

When creating a `liveURL` in our Chrome Devtools API, Browserless will return a one-time link to a webpage which you can share with your end-users. No API tokens or other secretive information is shared in this link, and no additional software or third-party packages are required. By default, this feature intends to mimic the underlying browser's screen to your end users, and will adjust the underlying browser to "fit" your end-users screen. As an example: If your user has a screen of 1920x1080, then we'll resize the underlying browser to match. This is configurable by specifying a value of `resizable: false` when creating this URL, which will preserve whatever viewport the browser currently is.

Interactions with the page are also turned on by default. This means your end user can click, type, scroll, touch, or tap on the page and interact with the page. We use a compressed video stream to preserve as much bandwidth as possible, and you can also configure a `quality` option, with values of 1 - 100 to lessen the amount of network consumption. This is ideal for streaming to mobile devices.

Below is a full example, with all options set, feel free to adjust this as your use-case demands:

```codeBlockLines_p187
import puppeteer from 'puppeteer-core';

const login = async () => {
  const browser = await puppeteer.connect({
    browserWSEndpoint: 'wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE',
  });
  const page = await browser.newPage();

  await page.goto('https://www.gmail.com/');
  const cdp = await page.createCDPSession();

  const { liveURL } = await cdp.send('Browserless.liveURL', {
    // Maintain the underlying browser viewport and don't resize to match the end users display.
    // End users will get a stream that maintains the aspect ratio.
    resizable: false,

    // Disable interactivity: useful for viewing the page as your code runs.
    interactable: false,

    // Set quality to "50" to help with bandwidth consumption.
    quality: 50

    // Finally, only allow this to run for 5 minutes (300000ms)
    timeout: 300_000,
  });

  console.log(liveURL);

  // More code or scripts...
  await browser.close();
};

login();

```

## How to stream a remote headless browsers [​](https://docs.browserless.io/baas/hybrid-automation\#how-to-stream-a-remote-headless-browsers "Direct link to How to stream a remote headless browsers")

Browserless communicates with the browser at a CDP layer to return the `Browserless.liveURL`, which is a fully-qualified URL that doesn't require a token, which means you can share this with the end users. The URL can be opened in a new tab or displayed as an iFrame on your website where they will be able to click, type and interact with the browser.

You can also listen for the `Browserless.captchaFound` and `Browserless.liveComplete` events to identify when there's a captcha on the screen and also when a customers has completed their automation and closed the interactive tab.

Here's a sample snippet where you want end users to log in to Gmail with their credentials/2FA.

```codeBlockLines_p187
import puppeteer from 'puppeteer-core';

const login = async () => {
  const browser = await puppeteer.connect({
    browserWSEndpoint: 'wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE',
  });
  const page = await browser.newPage();

  await page.goto('https://www.gmail.com/');
  const cdp = await page.createCDPSession();
  const { liveURL } = await cdp.send('Browserless.liveURL');

  // Send this one-time link to your end-users.
  // This URL doesn't contain an API-token so there's no
  // secrets being leaked by doing so
  console.log(`Shareable Public URL:`, liveURL);

  //This event is fired when a captcha is found on the page.
  await new Promise((resolve) =>
    cdp.on('Browserless.captchaFound', () => {
      console.log('Found a captcha!');
      return resolve();
    }),
  );

  // This event is fired after a user closes the page.
  // Assuming the page is where it's supposed to be, we can
  // proceed with doing further automations
  await new Promise((r) => cdp.on('Browserless.liveComplete', r));

  // Implement your scraping, data collections or further automations here.

  // Don't forget to close!
  browser.close();
};

login().catch((e) => console.log(e));

```

## Reusing the session after login [​](https://docs.browserless.io/baas/hybrid-automation\#reusing-the-session-after-login "Direct link to Reusing the session after login")

If you're using the hybrid automation for logging into a platform, you can reutilize the cookies, session and cache on subsequent browser sessions by using the `&--user-data-dir` flag.

```codeBlockLines_p187
puppeteer.connect({
  browserWSEndpoint: 'wss://production-sfo.browserless.io/?token=YOUR_API_KEY&--user-data-dir=~/browserless-cache-123',
});

```

## Multiple LiveURL sessions, captcha solving and more advanced use [​](https://docs.browserless.io/baas/hybrid-automation\#multiple-liveurl-sessions-captcha-solving-and-more-advanced-use "Direct link to Multiple LiveURL sessions, captcha solving and more advanced use")

The hybrid automation features can be combined to create more sophisticated workflows. You can use this example as a starting point to create even more sophisticated workflows. Here's an example that demonstrates:

1. Generating a LiveURL for user interaction
2. Adding a countdown timer to show session limits
3. Detecting and handling captchas
4. Creating multiple LiveURL sessions in sequence
5. Adding UI overlays to guide user behavior

````codeBlockLines_p187
import puppeteer from 'puppeteer-core';
const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

// Configuration for timeouts
// BROWSER_TIMEOUT: Total time the browser session can run (6 minutes)
// LIVE_URL_TIMEOUT: Time each LiveURL session can run (2 minutes)
const BROWSER_TIMEOUT = 6*60*1000; // 6 minutes in milliseconds
const LIVE_URL_TIMEOUT = 2*60*1000; // 2 minutes in milliseconds

const queryParams = new URLSearchParams({
  token: "YOUR_API_TOKEN_HERE",
  timeout: BROWSER_TIMEOUT,
  headless: true,
}).toString();

// Main automation function
(async() => {
  let browser = null;
  let sessionStartTime = null; // Tracks when each LiveURL session starts
  let browserStartTime = null; // Tracks when the browser session starts

  try {
    browser = await puppeteer.connect({
      browserWSEndpoint: `wss://production-sfo.browserless.io?${queryParams}`,
    });
    console.log('Connected to browserless.io!');

    const page = await browser.newPage();

    // Reinject banner after page navigation to maintain countdown
    page.on('load', async () => {
      if (sessionStartTime) {
        await injectTimeoutBanner(page, sessionStartTime, browserStartTime);
      }
    });

    // Initial page navigation and banner setup
    await page.goto('https://www.google.com', {
      waitUntil: 'networkidle2'
    });
    console.log('Navigated');

    // Record start times and inject initial banner with the timer countdown so users know how much time they have left
    browserStartTime = Date.now();
    sessionStartTime = Date.now();
    await injectTimeoutBanner(page, sessionStartTime, browserStartTime);

    // Create first LiveURL session
    const cdp = await page.createCDPSession();
    const { liveURL } = await cdp.send('Browserless.liveURL', {
      timeout: LIVE_URL_TIMEOUT
    });
    //You can embed this liveURL in your website or send it to the user via email or text message
    console.log('Click for live experience:', liveURL);

    // Wait for CAPTCHA detection
    let captchaFound = false;
    await new Promise((resolve) =>
      cdp.on('Browserless.captchaFound', () => {
        console.log('Found a captcha!');
        captchaFound = true;
        return resolve();
      }),
    );

    // Only handle CAPTCHA if one was found
    if (captchaFound) {
      // Add full-screen overlay and notification when CAPTCHA is detected so the user can't interact with the page while it's being solved
      await addCaptchaOverlay(page);

      // Wait for user to close the live URL
      await new Promise((r) => cdp.on('Browserless.liveComplete', r));
      console.log(`Live URL closed on page: ${page.url()}`);

      // Solve the CAPTCHA
      const { solved, error } = await cdp.send('Browserless.solveCaptcha', {
        appearTimeout: 20000
      });

      await page.waitForNavigation({ waitUntil: 'networkidle2' });
      console.log({
        solved,
        error,
      });
    }

    // Create second LiveURL session
    const { liveURL: newLiveURL } = await cdp.send('Browserless.liveURL', {
      timeout: LIVE_URL_TIMEOUT
    });
    console.log('Click for live experience:', newLiveURL);

    // Reset session timer for new LiveURL session
    sessionStartTime = Date.now();
    await injectTimeoutBanner(page, sessionStartTime, browserStartTime);

    // Wait for user to close the new live URL
    await new Promise((r) => cdp.on('Browserless.liveComplete', r));
    console.log(`Live URL closed on page: ${page.url()}`);

  } catch (error) {
    console.error('An error occurred:', error);
  } finally {
    // Ensure browser is always closed
    if (browser) {
      try {
        await browser.close();
        console.log('Browser closed successfully');
      } catch (closeError) {
        console.error('Error closing browser:', closeError);
      }
    }
  }
})().catch((e) => {
  console.error('Fatal error:', e);
  process.exit(1);
});

// Function to create and update the timeout banner
async function injectTimeoutBanner(page, startTime, browserStartTime) {
  // Wait 1 second to ensure page is fully loaded
  await sleep(1000);

  await page.evaluate((liveTimeoutMs, browserTimeoutMs, startTime, browserStartTime) => {
    // Remove existing banner if it exists
    const existingBanner = document.getElementById('timeout-banner');
    if (existingBanner) {
      existingBanner.remove();
    }

    // Create timeout banner with styling
    const banner = document.createElement('div');
    banner.id = 'timeout-banner';
    banner.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      background-color: #333;
      color: white;
      padding: 10px 15px;
      border-radius: 5px;
      z-index: 9999;
      font-family: Arial, sans-serif;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
      font-size: 14px;
    `;

    // Function to update the countdown display
    const updateCountdown = () => {
      const elapsed = Date.now() - startTime;
      const browserElapsed = Date.now() - browserStartTime;
      const liveRemaining = Math.max(0, liveTimeoutMs - elapsed);
      const browserRemaining = Math.max(0, browserTimeoutMs - browserElapsed);
      const remaining = Math.min(liveRemaining, browserRemaining);

      const minutes = Math.floor(remaining / 60000);
      const seconds = Math.floor((remaining % 60000) / 1000);

      banner.textContent = `Session timeout in: ${minutes}:${seconds.toString().padStart(2, '0')}`;

      if (remaining <= 0) {
        banner.style.backgroundColor = '#ff0000';
        banner.textContent = 'Session expired!';
      } else if (remaining <= 30000) { // Last 30 seconds
        banner.style.backgroundColor = '#ff9900';
      }
    };

    // Initial update and set up interval for countdown
    updateCountdown();
    const intervalId = setInterval(updateCountdown, 1000);
    window.timeoutBannerInterval = intervalId;

    document.body.appendChild(banner);
  }, LIVE_URL_TIMEOUT, BROWSER_TIMEOUT, startTime, browserStartTime);
}

// Function to add overlay and notification when CAPTCHA is detected
async function addCaptchaOverlay(page) {
  await page.evaluate(() => {
    // Create full-screen overlay to block interaction
    const overlay = document.createElement('div');
    overlay.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      z-index: 9998;
      cursor: not-allowed;
    `;
    document.body.appendChild(overlay);

    // Create notification message
    const notification = document.createElement('div');
    notification.style.cssText = `
      position: fixed;
      top: 20px;
      left: 50%;
      transform: translateX(-50%);
      background-color: #ff4444;
      color: white;
      padding: 15px 30px;
      border-radius: 5px;
      z-index: 9999;
      font-family: Arial, sans-serif;
      box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    `;

    notification.textContent = 'Please close this tab so that we can perform some tasks (solve captcha in this case)';
    document.body.appendChild(notification);
  });
}

## Using Hybrid Automation with Python and Playwright

The hybrid automation features can also be used with Python and Playwright. The main difference is in how we handle event listeners and async operations. Here's a complete example:

```python
import asyncio
import logging
from playwright.async_api import async_playwright
from urllib.parse import urlencode

logging.basicConfig(level=logging.DEBUG)

# Configuring query parameters
params = {
    "token": "YOUR_API_TOKEN_HERE",
    "timeout": 60000,
    "proxy": "residential",
    "proxyCountry": "US"
}
query_params = urlencode(params)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(f"wss://production-sfo.browserless.io/chromium?{query_params}")
        print('Connected')
        context = browser.contexts[0]
        page = await context.new_page()
        await page.goto('https://www.example.com', wait_until='networkidle')
        print('Navigated')

        cdp_session = await context.new_cdp_session(page)
        print('printing liveURL')
        response = await cdp_session.send('Browserless.liveURL', {
            'timeout': 600000
        })
        print(response)

        live_complete = asyncio.Future()

        def handle_event(params):
            print("Browserless.liveComplete:", params)
            live_complete.set_result(None)

        # Register the event handler
        cdp_session.on('Browserless.liveComplete', handle_event)

        # Wait for the future to complete
        await live_complete

        print("Page closed, current URL:", page.url)

        # Screenshot
        await page.screenshot(path='temp.png', full_page=True)

        await browser.close()

# Run the main function
asyncio.run(main())

````

## Additional LiveURL Options [​](https://docs.browserless.io/baas/hybrid-automation\#additional-liveurl-options "Direct link to Additional LiveURL Options")

The LiveURL feature supports several additional options for customizing behavior:

- **Quality and Type**: Control the streamed quality and format (jpeg/png)
- **Wait for Close**: Listen for events when the live page is closed
- **Programmatic Control**: Manage LiveURL sessions programmatically
- **Interactive:false**: Create read-only streaming sessions

For full developer documentation on these options, [see the CDP API documentation](https://docs.browserless.io/open-api#section/The-Browserless-CDP-API/Browserless.liveURL).

- [Default behavior](https://docs.browserless.io/baas/hybrid-automation#default-behavior)
- [How to stream a remote headless browsers](https://docs.browserless.io/baas/hybrid-automation#how-to-stream-a-remote-headless-browsers)
- [Reusing the session after login](https://docs.browserless.io/baas/hybrid-automation#reusing-the-session-after-login)
- [Multiple LiveURL sessions, captcha solving and more advanced use](https://docs.browserless.io/baas/hybrid-automation#multiple-liveurl-sessions-captcha-solving-and-more-advanced-use)
- [Additional LiveURL Options](https://docs.browserless.io/baas/hybrid-automation#additional-liveurl-options)