---
url: "https://docs.browserless.io/baas/v1/start"
title: "Quick Start | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/start#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

Welcome to the quick-start! Below are the top three integration we support, with quick directions on getting up and running with popular methods. See the sidebar for all the other supported API's and REST methods!

**Choose your library**

- [Using Puppeteer](https://docs.browserless.io/baas/v1/start#using-puppeteer)
- [Using Playwright](https://docs.browserless.io/baas/v1/libraries/playwright)
- [Using Selenium or WebDriver](https://docs.browserless.io/baas/v1/start#using-selenium-or-webdriver)

## Using Puppeteer [​](https://docs.browserless.io/baas/v1/start\#using-puppeteer "Direct link to Using Puppeteer")

Whether you're looking to get started, or already have an established codebase, browserless aims to make the transition as easy as possible. At a high-level, you'll need to do the following:

1. [Install puppeteer](https://docs.browserless.io/baas/v1/start#1-install-puppeteer)
2. [Setup your app](https://docs.browserless.io/baas/v1/start#2-setup-your-app)
3. [Update your app to use browserless](https://docs.browserless.io/baas/v1/start#3-update-your-app-to-use-browserless)

### 1\. Install puppeteer [​](https://docs.browserless.io/baas/v1/start\#1-install-puppeteer "Direct link to 1. Install puppeteer")

If you haven't chosen a library yet we highly recommend [puppeteer](https://github.com/puppeteer/puppeteer/) as it's fairly active and has many maintainers. It's also built by the developers of Chrome, so it's one of the highest quality libraries around.

**Installing puppeteer**

```codeBlockLines_p187
$ npm i --save puppeteer
# or
> yarn add puppeteer

```

In development you'll likely want to install puppeteer's bundled version of Chromium, however you won't need this in production as Chrome is all taken care of for you by browserless. To disable the downloading of puppeteer, simply add an environment variable when installing:

**Install for production**

```codeBlockLines_p187
# Linux
$ PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
# Windows
set PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true

$ npm install --production
# or yarn install --production

```

You can read more about puppeteer's environment variables [here](https://pptr.dev/#environment-variables).

### 2\. Setup your app [​](https://docs.browserless.io/baas/v1/start\#2-setup-your-app "Direct link to 2. Setup your app")

As an example let's write a screenshot service that takes a picture of the website and downloads it. We'll setup a route on the `/image` path and take a picture of a static webpage (though you can make this configurable if you wish):

**Screenshot service**

```codeBlockLines_p187
const express = require('express');
const puppeteer = require('puppeteer');

const app = express();

app.get('/image', async (req, res) => {
  // puppeteer.launch() => Chrome running locally (on the same hardware)
  let browser = null;

  try {
    browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto('http://www.example.com/');
    const screenshot = await page.screenshot();

    res.end(screenshot, 'binary');
  } catch (error) {
    if (!res.headersSent) {
      res.status(400).send(error.message);
    }
  } finally {
    if (browser) {
      browser.close();
    }
  }
});

app.listen(8080, () => console.log('Listening on PORT: 8080'));

```

With that in place, let's re-work some of our functionality to use browserless in production.

### 3\. Update your app to use browserless [​](https://docs.browserless.io/baas/v1/start\#3-update-your-app-to-use-browserless "Direct link to 3. Update your app to use browserless")

Once we have browserless account setup, or have it running via docker, we can simply "connect" to it in our application instead of launching Chrome.

warning

It's very important to close the browser for unit-based, otherwise you'll spend seconds on the browser running. The best practice is to implement try/catch blocks and set a custom timeout to last less than the 15 minute global timeout set by default, per your requirements.

**Screenshot service with browserless**

```codeBlockLines_p187
const express = require('express');
const puppeteer = require('puppeteer');
const IS_PRODUCTION = process.env.NODE_ENV === 'production';

const app = express();

const getBrowser = () =>
  IS_PRODUCTION
    ? // Connect to browserless so we don't run Chrome on the same hardware in production
      puppeteer.connect({ browserWSEndpoint: 'wss://chrome.browserless.io?token=YOUR-API-TOKEN' })
    : // Run the browser locally while in development
      puppeteer.launch();

app.get('/image', async (req, res) => {
  let browser = null;

  try {
    browser = await getBrowser();
    const page = await browser.newPage();

    await page.goto('http://www.example.com/');
    const screenshot = await page.screenshot();

    res.end(screenshot, 'binary');
  } catch (error) {
    if (!res.headersSent) {
      res.status(400).send(error.message);
    }
  } finally {
    if (browser) {
      browser.close();
    }
  }
});

app.listen(8080, () => console.log('Listening on PORT: 8080'));

```

That's it! Now you don't have to worry about bundling Chrome or it's dependencies in production and can continue to develop your application.

Below is a sample cURL call that will use your new service to ensure it's all working:

```codeBlockLines_p187
$ curl -X GET -o temp.png http://localhost:8080/image

```

## Using Selenium or WebDriver [​](https://docs.browserless.io/baas/v1/start\#using-selenium-or-webdriver "Direct link to Using Selenium or WebDriver")

Browserless exposes the WebDriver protocol at [https://chrome.browserless.io/webdriver](https://chrome.browserless.io/webdriver). Updating your tests, continuous-integration tests, or application to use it is as simple as specifying a remote connection.

1. [Setup WebDriver.](https://docs.browserless.io/baas/v1/start#setup-webdriver)
2. [Update the builder to use browserless.](https://docs.browserless.io/baas/v1/start#update-the-builder-to-use-browserless)

### Setup WebDriver [​](https://docs.browserless.io/baas/v1/start\#setup-webdriver "Direct link to Setup WebDriver")

For the purposes of this example we'll be using the Ruby bindings, but almost every language has an accompanying library for WebDriver. Be sure to consult your runtime's library for more direct instructions.

```codeBlockLines_p187
# You must specify --headless and --no-sandbox
options = Selenium::WebDriver::Chrome::Options.new
options.add_argument('--headless')
options.add_argument('--no-sandbox')

# Use the webdriver for going to sites, taking pictures, anything else. Make sure you close the browser when done.
driver = Selenium::WebDriver.for :chrome, options: options

```

Once that's setup, be sure to verify your script works locally before proceeding to rule out any unwanted behavior.

### Update the builder to use browserless [​](https://docs.browserless.io/baas/v1/start\#update-the-builder-to-use-browserless "Direct link to Update the builder to use browserless")

Once you have script working locally, the next step is to specify browserless as the remote server. This will give you the ability to run multiple browsers in parallel, greatly reducing the amount of time your tests take.

```codeBlockLines_p187
# You must specify --headless and --no-sandbox
caps = Selenium::WebDriver::Remote::Capabilities.chrome("goog:chromeOptions" => {
  "args" => [\
    "--disable-background-timer-throttling",\
    "--disable-backgrounding-occluded-windows",\
    "--disable-breakpad",\
    "--disable-component-extensions-with-background-pages",\
    "--disable-dev-shm-usage",\
    "--disable-extensions",\
    "--disable-features=TranslateUI,BlinkGenPropertyTrees",\
    "--disable-ipc-flooding-protection",\
    "--disable-renderer-backgrounding",\
    "--enable-features=NetworkService,NetworkServiceInProcess",\
    "--force-color-profile=srgb",\
    "--hide-scrollbars",\
    "--metrics-recording-only",\
    "--mute-audio",\
    "--headless",\
    "--no-sandbox"\
  ]
})
caps['browserless:token'] = 'YOUR-API-TOKEN'
driver = Selenium::WebDriver.for :remote, url: "https://chrome.browserless.io/webdriver", desired_capabilities: caps

# Use the webdriver for going to sites, taking pictures. Make sure you close the browser when done.
driver = Selenium::WebDriver.for :chrome, options: options

```

That's it! Once you've verified it's all working properly, the next step is to conditionally use browserless only when running in a continuous integration environment.

### What's next? [​](https://docs.browserless.io/baas/v1/start\#whats-next "Direct link to What's next?")

There's a lot more that you can configure and tune in browserless to handle the needs of your application. Be sure to read about all the options it exposes and how to get the most out of browserless.

- [Using Puppeteer](https://docs.browserless.io/baas/v1/start#using-puppeteer)
  - [1\. Install puppeteer](https://docs.browserless.io/baas/v1/start#1-install-puppeteer)
  - [2\. Setup your app](https://docs.browserless.io/baas/v1/start#2-setup-your-app)
  - [3\. Update your app to use browserless](https://docs.browserless.io/baas/v1/start#3-update-your-app-to-use-browserless)
- [Using Selenium or WebDriver](https://docs.browserless.io/baas/v1/start#using-selenium-or-webdriver)
  - [Setup WebDriver](https://docs.browserless.io/baas/v1/start#setup-webdriver)
  - [Update the builder to use browserless](https://docs.browserless.io/baas/v1/start#update-the-builder-to-use-browserless)
  - [What's next?](https://docs.browserless.io/baas/v1/start#whats-next)