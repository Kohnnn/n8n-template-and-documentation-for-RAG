---
url: "https://docs.browserless.io/enterprise/user-data-directory"
title: "User Data Directory for persisting sessions | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/user-data-directory#__docusaurus_skipToContent_fallback)

On this page

The `--user-data-dir` flag in browserless allows you to persist browser data such as cookies, localStorage, cache, and login sessions across multiple browser sessions. This is particularly useful for maintaining authenticated states and user preferences without having to re-authenticate or reconfigure settings each time.

note

The `--user-data-dir` feature is only available for Enterprise plans with dedicated fleets. It cannot be used with shared plans.

## Important details when implementing User Data Directories [​](https://docs.browserless.io/enterprise/user-data-directory\#important-details-when-implementing-user-data-directories "Direct link to Important details when implementing User Data Directories")

The directory will be created if it doesn't exist. When using `--user-data-dir`, make sure to use a unique directory path for each different browser profile you want to maintain. You can only instantiate one browser per userdatadir at a time, meaning it's 1-1 and you can't use the same path in the flag for multiple concurrent browsers.

### Pointing to a specific dedicated worker on Enterprise plans [​](https://docs.browserless.io/enterprise/user-data-directory\#pointing-to-a-specific-dedicated-worker-on-enterprise-plans "Direct link to Pointing to a specific dedicated worker on Enterprise plans")

User data directories are stored locally on each worker's file system and do not sync across your fleet. For example, a browser instance using `--user-data-dir=~/u/1` on Worker #1 will not be accessible from Worker #2. No need to worry! Browserless allows you to point at a specific worker by using the endpoint provided on your account page under "Production" Clusters. Click on the cell under the Address column to copy the endpoint for the worker you need. You'll want to keep track of which browser session was persisted initially on which worker to ensure consistent access.

- Your BQL endpoints would change from `https://chrome.browserless.io/bql` to something like `https://chrome.browserless.io/p/53616c7465645f5ff8cc738d5eecb3032823d67e37578fe4531b0f9a83dc80856c66d0fe36aba4d2f4bc5f01c18bdfab/bql?token=YOUR_API_TOKEN_HERE&--user-data-dir=~/custompath/123`
- Your websocket connections would change from `wss://chrome.browserless.io/chromium` to something like `wss://chrome.browserless.io/p/53616c7465645f5ff8cc738d5eecb3032823d67e37578fe4531b0f9a83dc80856c66d0fe36aba4d2f4bc5f01c18bdfab/chromium?token=YOUR_API_TOKEN_HERE&--user-data-dir=~/custompath/456`

## Using the userdatadir with Puppeteer and Playwright [​](https://docs.browserless.io/enterprise/user-data-directory\#using-the-userdatadir-with-puppeteer-and-playwright "Direct link to Using the userdatadir with Puppeteer and Playwright")

The following examples demonstrate how to use the `--user-data-dir` flag with both Puppeteer and Playwright. These examples show how to persist a login session to browserless.io - once you log in and close the tab, running the script again will show you already logged in.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from 'puppeteer-core';

const launchArgs = {
  headless: false,
  args: ['--user-data-dir=~/u/1']
};

const queryParams = new URLSearchParams({
  token: "YOUR_API_TOKEN_HERE", //this script using userdatadir only works for dedicated machines
  timeout: 300000,
  launch: JSON.stringify(launchArgs)
}).toString();

(async () => {
  let browser;
  try {
    browser = await puppeteer.connect({
      browserWSEndpoint: `wss://chrome.browserless.io/chromium?${queryParams}`,
      defaultViewport: null
    });

    console.log('Connected');

    const page = await browser.newPage();
    await page.goto('https://account.browserless.io/', {
      waitUntil: 'domcontentloaded'
    });

    console.log('Navigated');

    const client = await page.target().createCDPSession();
    const { liveURL } = await client.send('Browserless.liveURL', {
      timeout: 300000
    });

    console.log('Click for live experience:', liveURL);

    await new Promise((resolve) => {
      client.on('Browserless.liveComplete', resolve);
    });

    console.log(`Live URL closed on page: ${page.url()}`);

    await browser.close();
  } catch (error) {
    console.error('An error occurred:', error);
    if (browser) {
      await browser.close().catch(console.error);
    }
    throw error;
  }
})().catch(error => {
  console.error('Fatal error:', error);
});

```

```codeBlockLines_p187
import { chromium } from 'playwright-core';

const launchArgs = {
  headless: false,
  stealth: true,
  args: ['--user-data-dir=~/u/1']
};
const queryParams = new URLSearchParams({
  token: "YOUR_API_TOKEN_HERE", //this script using userdatadir only works for dedicated machines
  timeout: 300000,
  launch: JSON.stringify(launchArgs)
}).toString();

(async () => {
  let browser;
  try {
    browser = await chromium.connectOverCDP(
      `wss://chrome.browserless.io/chromium/stealth?${queryParams}`
    );
    console.log('Connected');
    const [context] = await browser.contexts();
    const page = await context.newPage();
    await page.goto('https://account.browserless.io/', {
      waitUntil: 'domcontentloaded'
    });
    console.log('Navigated');
    const cdpSession = await context.newCDPSession(page);
    const { liveURL } = await cdpSession.send('Browserless.liveURL', {
      timeout: 300000
    });
    console.log('Click for live experience:', liveURL);
    await new Promise((resolve) => {
      cdpSession.on('Browserless.liveComplete', resolve);
    });

    console.log(`Live URL closed on page: ${page.url()}`);

    await browser.close();
  } catch (error) {
    console.error('An error occurred:', error);
    if (browser) {
      await browser.close().catch(console.error);
    }
    throw error;
  }
})().catch(error => {
  console.error('Fatal error:', error);
});

```

## Using with BrowserQL [​](https://docs.browserless.io/enterprise/user-data-directory\#using-with-browserql "Direct link to Using with BrowserQL")

The following example demonstrates how to use the `--user-data-dir` flag with BrowserQL to persist browser state. This example shows how to toggle dark mode on w3schools.com - each time you run it, the initial state will be different since it's persisting the toggle state from previous runs.

```codeBlockLines_p187
import puppeteer from 'puppeteer-core';

const url = 'https://www.browserless.io/';
const token = 'YOUR_API_TOKEN_HERE'; //this script using userdatadir only works for dedicated machines
const timeout = 5 * 60 * 1000;
const launchArgs = {
  args: ['--user-data-dir=~/id-togle-test-123']
};
const queryParams = new URLSearchParams({
  timeout,
  token,
  launch: JSON.stringify(launchArgs)
}).toString();

const query = `
  mutation DarkModeToggle {
    goto(url: "https://www.w3schools.com/", waitUntil: domContentLoaded) {
      status
    }
    DarkModeClassBefore:evaluate(content: "document.body.className") {
      value
    }
    click(selector:"#tnb-dark-mode-toggle-btn"){
      time
    }
    DarkModeClassAfter:evaluate(content: "document.body.className") {
      value
    }
  }
`;

const variables = { url };

const endpoint =
  `https://chrome.browserless.io/chromium/bql?${queryParams}`;

const options = {
  method: 'POST',
  headers: {
    'content-type': 'application/json'
  },
  body: JSON.stringify({
    query,
  }),
};

try {
  console.log(`Running BQL Query: ${url}`);

  const response = await fetch(endpoint, options);

  if (!response.ok) {
    throw new Error(`Got non-ok response:\n` + (await response.text()));
  }

  const { data } = await response.json();

  console.log("Full response data:", JSON.stringify(data, null, 2));

  if (data && data.DarkModeClassBefore && data.DarkModeClassAfter) {
    console.log("Dark mode toggle results:");
    console.log("Before:", data.DarkModeClassBefore.value);
    console.log("After:", data.DarkModeClassAfter.value);
    console.log("Click time:", data.click.time, "ms");
  } else {
    console.log("Unexpected response structure:", data);
  }
} catch (error) {
  console.error(error);
}

```

- [Important details when implementing User Data Directories](https://docs.browserless.io/enterprise/user-data-directory#important-details-when-implementing-user-data-directories)
  - [Pointing to a specific dedicated worker on Enterprise plans](https://docs.browserless.io/enterprise/user-data-directory#pointing-to-a-specific-dedicated-worker-on-enterprise-plans)
- [Using the userdatadir with Puppeteer and Playwright](https://docs.browserless.io/enterprise/user-data-directory#using-the-userdatadir-with-puppeteer-and-playwright)
- [Using with BrowserQL](https://docs.browserless.io/enterprise/user-data-directory#using-with-browserql)