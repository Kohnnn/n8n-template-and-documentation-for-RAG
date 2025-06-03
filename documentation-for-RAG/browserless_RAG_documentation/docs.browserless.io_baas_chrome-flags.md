---
url: "https://docs.browserless.io/baas/chrome-flags"
title: "Launch Options | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/chrome-flags#__docusaurus_skipToContent_fallback)

Version: v2

On this page

## Using Launch Options [​](https://docs.browserless.io/baas/chrome-flags\#using-launch-options "Direct link to Using Launch Options")

Browserless provides two main ways to configure launch options:

1. Through the `launch` parameter in the query string, which accepts a JSON object containing both Chrome flags and Browserless-specific options
2. Through individual query parameters for commonly used options

### Using the `launch` Parameter [​](https://docs.browserless.io/baas/chrome-flags\#using-the-launch-parameter "Direct link to using-the-launch-parameter")

The `launch` parameter allows you to specify both Chrome flags and Browserless-specific options in a structured way. Here's how to use it:

- Puppeteer
- Playwright CDP
- Playwright Connect

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

// Define launch options
const launchArgs = {
  headless: false,
  stealth: true,
  args: ['--window-size=1920,1080', '--force-color-profile=srgb']
};

// Create query parameters
const queryParams = new URLSearchParams({
  token: 'YOUR_API_TOKEN_HERE',
  proxy: 'residential',
  proxyCountry: 'us',
  timeout: '180000',
  launch: JSON.stringify(launchArgs)
});

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io?${queryParams.toString()}`,
});

```

```codeBlockLines_p187
import playwright from "playwright";

// Define launch options
const launchArgs = {
  headless: false,
  stealth: true,
  args: ['--window-size=1920,1080', '--force-color-profile=srgb']
};

// Create query parameters
const queryParams = new URLSearchParams({
  token: 'YOUR_API_TOKEN_HERE',
  proxy: 'residential',
  proxyCountry: 'us',
  timeout: '180000',
  launch: JSON.stringify(launchArgs)
});

const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io?${queryParams.toString()}`
);

```

```codeBlockLines_p187
import playwright from "playwright";

// Define launch options
const launchArgs = {
  headless: false,
  stealth: true,
  args: ['--window-size=1920,1080', '--force-color-profile=srgb']
};

// Create query parameters
const queryParams = new URLSearchParams({
  token: 'YOUR_API_TOKEN_HERE',
  proxy: 'residential',
  proxyCountry: 'us',
  timeout: '180000',
  launch: JSON.stringify(launchArgs)
});

const browser = await playwright.chromium.connect(
  `wss://production-sfo.browserless.io/chrome/playwright?${queryParams.toString()}`
);

```

### Available Chrome Args [​](https://docs.browserless.io/baas/chrome-flags\#available-chrome-args "Direct link to Available Chrome Args")

All chrome flags are supported on Enterprise plans. The following chrome flags are available to all accounts:

- --disable-features,
- --disable-setuid-sandbox,
- --disable-site-isolation-trials,
- --disable-web-security,
- --enable-features,
- --font-render-hinting,
- --force-color-profile,
- --lang,
- --proxy-bypass-list,
- --proxy-server,
- --window-size,
- blockAds,
- humanlike,
- blockConsentModals,
- headless,
- ignoreDefaultArgs,
- ignoreHTTPSErrors,
- launch,
- record,
- slowMo,
- stealth,
- timeout,
- token,
- proxy,
- proxyCountry,
- proxySticky,

Browserless allows you to control how Chrome is launched through query-string parameters in your `puppeteer.connect`'s `browserWSEndpoint` URL or in your REST API calls. We allow you to set a `launch` query parameter as a way to specify Chrome launch options using a JSON object. This provides a clean, structured approach to setting up your browser environment, and it allows features like stealth mode, setting headful mode, and custom Chrome arguments.

## Launch Options (Query Parameters) [​](https://docs.browserless.io/baas/chrome-flags\#launch-options-query-parameters "Direct link to Launch Options (Query Parameters)")

Below is a list of available launch options you can use in query strings for BaaS.

| Parameter | Description | Default |
| --- | --- | --- |
| headless | Runs the browser in headless mode. Set to false to enable headful mode (with a GUI). While the GUI isn't visible in cloud environments, headful mode may help bypass bot detection. Note: it uses more resources. | `true` |
| stealth | Enables stealth mode to reduce automation signals (similar to puppeteer-extra’s stealth plugin). In BQL, stealth is always on by design and controlled via the humanlike option. In BaaS/REST, set to true to enable stealth techniques. | - `false` (for BaaS/REST)<br>- `true` (for BQL) |
| blockAds | Enables the built-in ad blocker (powered by uBlock Origin). Helps speed up scripts and reduce noise by blocking ads and trackers. Especially useful for scraping to avoid popups and clutter. | `false` |
| proxy | Routes browser traffic through a proxy. Options: proxy=residential for Browserless’s residential proxy pool; proxy=\`<your proxy URL>\` for your own proxy. Omit to use a direct connection. | none |
| proxyCountry | Used with proxy=residential to specify the exit node’s country. Accepts ISO 3166 country codes (e.g., us, gb, de). If omitted, a random location is chosen. | none |
| proxySticky | Used with proxy=residential to maintain the same proxy IP across a session (when possible). Useful for sites that expect consistent IP usage. | `false` |
| timeout | Maximum session duration in milliseconds. The session will automatically close after this time to prevent overuse. | 60000 |

### Launching with Proxies [​](https://docs.browserless.io/baas/chrome-flags\#launching-with-proxies "Direct link to Launching with Proxies")

While you can always use your own proxy service, we highly recommend using our built-in and first-party residential proxies. See our [Proxies documentation](https://docs.browserless.io/baas/proxies) for detailed information on both our built-in residential proxy and how to use third-party proxies.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/chromium?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/chromium?token=YOUR_API_TOKEN_HERE&proxy=residential&proxyCountry=us`
);

```

### Blocking ads [​](https://docs.browserless.io/baas/chrome-flags\#blocking-ads "Direct link to Blocking ads")

You can use our built-in ad-blocker for both `puppeteer.connect()` and REST API calls. You'll simply need to add a query-string parameter of `blockAds=true` to your URL when connecting:

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/chromium?token=YOUR_API_TOKEN_HERE&blockAds=true`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/chromium?token=YOUR_API_TOKEN_HERE&blockAds=true`
);

```

Under the hood, Browserless uses UBlock Origin to block ads and filter content.

## Time to Live (TTL) [​](https://docs.browserless.io/baas/chrome-flags\#time-to-live-ttl "Direct link to Time to Live (TTL)")

Use the `ttl` key in your `launch` parameter to keep the browser instance alive for a specified duration, which allows for reconnections during this period.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_KEY&ttl=30000`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_KEY&ttl=30000`
);

```

## Dynamic Launch Arguments [​](https://docs.browserless.io/baas/chrome-flags\#dynamic-launch-arguments "Direct link to Dynamic Launch Arguments")

You can pass dynamic launch arguments to Chrome by sending a JSON object and including it in the `launch` query parameter. This object can contain any Chrome launch arguments supported by Puppeteer and Browserless' launch options.

### Overriding the session timer [​](https://docs.browserless.io/baas/chrome-flags\#overriding-the-session-timer "Direct link to Overriding the session timer")

By default, your sessions are governed by a timeout. This is set via your account page for the hosted service. You can override this behavior.

- If you are running `BaaS` in Docker, you can specify a `TIMEOUT` environment variable in the `docker run` command to override the default timeout of 30 seconds.

- If you need to override the timeout on a per-job basis, simply specify a `timeout` parameter in your connect calls query-parameters, with the value being the time in milliseconds for the session to execute:



- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&timeout=10000`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&timeout=10000`
);

```

note

For other runtimes and selenium libraries be sure to consult your libraries documentation, or [contact us](https://www.browserless.io/contact)

### Stealth Mode [​](https://docs.browserless.io/baas/chrome-flags\#stealth-mode "Direct link to Stealth Mode")

You can use stealth mode to reduce bot-detection from blocking your scripts.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const launchArgs = JSON.stringify({ stealth: true });
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const launchArgs = JSON.stringify({ stealth: true });
const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`
);

```

Bot Detection

If stealth mode flags aren't enough to avoid bot detection, we recommend using [**BrowserQL**](https://docs.browserless.io/browserql/start).

### Headful mode [​](https://docs.browserless.io/baas/chrome-flags\#headful-mode "Direct link to Headful mode")

You can set the browser's headless mode using the `headless` query parameter. Running the browser in headful mode will launch the browser using the OS' GUI, in contrast to headless mode. This can be helphul to avoid more sophisticated bot-detection methods that rely on screen or rendering pattern detection.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const launchArgs = JSON.stringify({ headless: false });
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const launchArgs = JSON.stringify({ headless: false });
const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`
);

```

### Chrome launch arguments [​](https://docs.browserless.io/baas/chrome-flags\#chrome-launch-arguments "Direct link to Chrome launch arguments")

In adition to the launch options Browserless offers, you can also use some of the [Chrome launch flags](https://peter.sh/experiments/chromium-command-line-switches/) inside the `args` array of the `launch` object.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const launchArgs = JSON.stringify({
  args: ["--window-size=1920,1080", "--lang=en-US"],
});
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const launchArgs = JSON.stringify({
  args: ["--window-size=1920,1080", "--lang=en-US"],
});
const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`
);

```

### Caching with `user-data-dir` [​](https://docs.browserless.io/baas/chrome-flags\#caching-with-user-data-dir "Direct link to caching-with-user-data-dir")

warning

Setting a `user-data-dir` is only available for Dedicated and self-hosted accounts (not on usage-based or cloud unit-based)

You can launch Chrome and specify a "user-data-dir" on each request to cache and make future sessions faster:

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const launchArgs = JSON.stringify({
  args: ["--user-data-dir=~/browserless-cache-123"],
});
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const launchArgs = JSON.stringify({
  args: ["--user-data-dir=~/browserless-cache-123"],
});
const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`
);

```

This can be used in conjuction with all our API's and integrations.

### Ignoring default flags [​](https://docs.browserless.io/baas/chrome-flags\#ignoring-default-flags "Direct link to Ignoring default flags")

By default Puppeteer specifies a certain number of launch flags in order to provide the best experience. In order to turn these off you'll want to tell Browserless to ignore them.

danger

Be careful ignoring these args as it might cause chromium to become unstable or refuse to launch.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer-core";

const launchArgs = JSON.stringify({
  args: ["--hide-scrollbars", "--disable-default-apps"],
});
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`,
});
// ...

```

```codeBlockLines_p187
import playwright from "playwright";

const launchArgs = JSON.stringify({
  args: ["--hide-scrollbars", "--disable-default-apps"],
});
const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io/?token=YOUR_API_TOKEN_HERE&launch=${launchArgs}`
);

```

### Overriding Puppeteer's launch args [​](https://docs.browserless.io/baas/chrome-flags\#overriding-puppeteers-launch-args "Direct link to Overriding Puppeteer's launch args")

Since `puppeteer.connect` differs greatly from `puppeteer.launch`, Browserless allows to override Puppeteer's default launch arguments. These are specified through query-string parameters, and can be applied like so:

### Ignore HTTPS Errors [​](https://docs.browserless.io/baas/chrome-flags\#ignore-https-errors "Direct link to Ignore HTTPS Errors")

```codeBlockLines_p187
// Via puppeteer.launch()
puppeteer.launch({
  ignoreHTTPSErrors: true,
});

// Via puppeteer.connect()
puppeteer.connect({
  browserWSEndpoint: "wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE",
  ignoreHTTPSErrors: true,
});

```

### Slow Mo [​](https://docs.browserless.io/baas/chrome-flags\#slow-mo "Direct link to Slow Mo")

```codeBlockLines_p187
// Via puppeteer.launch()
puppeteer.launch({
  slowMo: 1000,
});

// Via puppeteer.connect()
puppeteer.connect({
  browserWSEndpoint: "wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE",
  slowMo: 1000,
});

```

### Ignore default args [​](https://docs.browserless.io/baas/chrome-flags\#ignore-default-args "Direct link to Ignore default args")

```codeBlockLines_p187
// Via puppeteer.launch()
puppeteer.launch({
  ignoreDefaultArgs: true,
});

// Via puppeteer.connect()
puppeteer.connect({
  browserWSEndpoint:
    "wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE&ignoreDefaultArgs=true",
});

```

- [Using Launch Options](https://docs.browserless.io/baas/chrome-flags#using-launch-options)
  - [Using the `launch` Parameter](https://docs.browserless.io/baas/chrome-flags#using-the-launch-parameter)
  - [Available Chrome Args](https://docs.browserless.io/baas/chrome-flags#available-chrome-args)
- [Launch Options (Query Parameters)](https://docs.browserless.io/baas/chrome-flags#launch-options-query-parameters)
  - [Launching with Proxies](https://docs.browserless.io/baas/chrome-flags#launching-with-proxies)
  - [Blocking ads](https://docs.browserless.io/baas/chrome-flags#blocking-ads)
- [Time to Live (TTL)](https://docs.browserless.io/baas/chrome-flags#time-to-live-ttl)
- [Dynamic Launch Arguments](https://docs.browserless.io/baas/chrome-flags#dynamic-launch-arguments)
  - [Overriding the session timer](https://docs.browserless.io/baas/chrome-flags#overriding-the-session-timer)
  - [Stealth Mode](https://docs.browserless.io/baas/chrome-flags#stealth-mode)
  - [Headful mode](https://docs.browserless.io/baas/chrome-flags#headful-mode)
  - [Chrome launch arguments](https://docs.browserless.io/baas/chrome-flags#chrome-launch-arguments)
  - [Caching with `user-data-dir`](https://docs.browserless.io/baas/chrome-flags#caching-with-user-data-dir)
  - [Ignoring default flags](https://docs.browserless.io/baas/chrome-flags#ignoring-default-flags)
  - [Overriding Puppeteer's launch args](https://docs.browserless.io/baas/chrome-flags#overriding-puppeteers-launch-args)
  - [Ignore HTTPS Errors](https://docs.browserless.io/baas/chrome-flags#ignore-https-errors)
  - [Slow Mo](https://docs.browserless.io/baas/chrome-flags#slow-mo)
  - [Ignore default args](https://docs.browserless.io/baas/chrome-flags#ignore-default-args)