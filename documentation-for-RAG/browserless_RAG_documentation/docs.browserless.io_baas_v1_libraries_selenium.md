---
url: "https://docs.browserless.io/baas/v1/libraries/selenium"
title: "Selenium | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/selenium#__docusaurus_skipToContent_fallback)

Version: v1

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

We're happy to support the web-driver protocol, largely used by Selenium. You'll likely need to consult your libraries documentation since there's many options and alternatives for remote connections. Below is a small example of using the `chrome-webdriver` library and how to use browserless with it.

**Before**

```codeBlockLines_p187
const webdriver = require('selenium-webdriver');
const fs = require('fs');

const chromeCapabilities = webdriver.Capabilities.chrome();
chromeCapabilities.set('goog:chromeOptions', {
  // Set args similar to puppeteer's for best performance
  args: [\
    '--disable-background-timer-throttling',\
    '--disable-backgrounding-occluded-windows',\
    '--disable-breakpad',\
    '--disable-component-extensions-with-background-pages',\
    '--disable-dev-shm-usage',\
    '--disable-extensions',\
    '--disable-features=TranslateUI,BlinkGenPropertyTrees',\
    '--disable-ipc-flooding-protection',\
    '--disable-renderer-backgrounding',\
    '--enable-features=NetworkService,NetworkServiceInProcess',\
    '--force-color-profile=srgb',\
    '--hide-scrollbars',\
    '--metrics-recording-only',\
    '--mute-audio',\
    '--headless',\
    '--no-sandbox',\
  ],
});

const driver = new webdriver.Builder()
  .forBrowser('chrome')
  .withCapabilities(chromeCapabilities)
  .build();

(async () => {
  try {
    await driver.get('https://www.example.com/');

    // Take screenshot of results page. Save to disk.
    const base64png = await driver.takeScreenshot();
    fs.writeFileSync('.no-git/screenshot.png', new Buffer(base64png, 'base64'));
  } finally {
    driver.quit();
  }
})();

```

**After**

```codeBlockLines_p187
const webdriver = require('selenium-webdriver');
const fs = require('fs');

const chromeCapabilities = webdriver.Capabilities.chrome();
chromeCapabilities.set('browserless:token', 'YOUR-API-TOKEN');
chromeCapabilities.set('goog:chromeOptions', {
  args: [\
    '--disable-background-timer-throttling',\
    '--disable-backgrounding-occluded-windows',\
    '--disable-breakpad',\
    '--disable-component-extensions-with-background-pages',\
    '--disable-dev-shm-usage',\
    '--disable-extensions',\
    '--disable-features=TranslateUI,BlinkGenPropertyTrees',\
    '--disable-ipc-flooding-protection',\
    '--disable-renderer-backgrounding',\
    '--enable-features=NetworkService,NetworkServiceInProcess',\
    '--force-color-profile=srgb',\
    '--hide-scrollbars',\
    '--metrics-recording-only',\
    '--mute-audio',\
    '--headless',\
    '--no-sandbox',\
  ],
});

const driver = new webdriver.Builder()
  .forBrowser('chrome')
  .withCapabilities(chromeCapabilities)
  // Specify browserless for the server
  .usingServer('https://chrome.browserless.io/webdriver')
  .build();

(async () => {
  try {
    await driver.get('https://www.example.com/');

    // Take screenshot of results page. Save to disk.
    const base64png = await driver.takeScreenshot();
    fs.writeFileSync('.no-git/screenshot.png', new Buffer(base64png, 'base64'));
  } finally {
    driver.quit();
  }
})();

```

If you're using the hosted service, be sure to set the extra option for the browserless token:

**Token Auth**

```codeBlockLines_p187
chromeCapabilities.set('browserless:token', 'YOUR-API-TOKEN');

```

The reason you can't append use the standard `?token=YOUR-API-TOKEN` is due to limitations in many of the Selenium libraries where query-string parameters are dropped from the server URL.