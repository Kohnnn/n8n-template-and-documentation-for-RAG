---
url: "https://docs.browserless.io/overview/launch-parameters"
title: "Launch Parameters | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/overview/launch-parameters#__docusaurus_skipToContent_fallback)

On this page

Configure how browsers launch and behave with parameters provided via URL query parameters or JSON payload. This section covers available options, defaults, and usage across [BrowserQL](https://docs.browserless.io/browserql/start), [BaaS v2](https://docs.browserless.io/baas/start), and [REST APIs](https://docs.browserless.io/rest-apis/intro).

## Passing Launch Options [​](https://docs.browserless.io/overview/launch-parameters\#passing-launch-options "Direct link to Passing Launch Options")

Two ways to specify launch options:

1. **Individual Query Parameters**: Add options directly to URLs (e.g., `&headless=false`, `&proxy=residential`). Best for simple boolean options.

2. **Combined `launch` Parameter (JSON)**: For complex configurations, use a single query param `launch` with a JSON string as its value. This JSON can include any Chrome flags or Browserless-specific settings in a structured way. It's essentially the equivalent of Puppeteer's `launch({ options })` but provided to the cloud service:







```codeBlockLines_p187
&launch={"headless":false,"stealth":true,"args":["--window-size=1920,1080"]}

```











(URL-encoded) would configure a headful, stealth-enabled browser with a specific window size.


Browserless merges both methods if used together, with individual parameters taking precedence. Use query params for simple toggles and the launch parameter for multiple settings.

## Common Launch Options [​](https://docs.browserless.io/overview/launch-parameters\#common-launch-options "Direct link to Common Launch Options")

Below is a list of common launch options you can use in query strings. Unless stated otherwise,
these can be used in BaaS v2 (library connections) and REST API calls alike. BrowserQL
internally uses some of these, but BQL users typically set these via the IDE session settings
rather than manually in a URL.

| Parameter | Description | Default | BrowserQL | BaaS v2 | REST APIs |
| --- | --- | --- | --- | --- | --- |
| headless | Runs the browser in headless mode. Set to false to enable headful mode (with a GUI). While the GUI isn't visible in cloud environments, headful mode may help bypass bot detection. Note: it uses more resources. | `true` | ✅ | ✅ | ✅ |
| stealth | Enables stealth mode to reduce automation signals (similar to puppeteer-extra’s stealth plugin). In BQL, stealth is always on by design and controlled via the humanlike option. In BaaS/REST, set to true to enable stealth techniques. | - `false` (for BaaS/REST)<br>- `true` (for BQL) | ✅ | ✅ | ✅ |
| humanlike | Simulates human-like behavior such as natural mouse movement, typing, and random delays. In the BQL IDE, this can be toggled in session settings. For direct BQL GraphQL calls, use humanlike: true in the launch payload. Recommended for strict bot detection scenarios. | `false` | ✅ | ❌ | ❌ |
| blockAds | Enables the built-in ad blocker (powered by uBlock Origin). Helps speed up scripts and reduce noise by blocking ads and trackers. Especially useful for scraping to avoid popups and clutter. | `false` | ✅ | ✅ | ✅ |
| blockConsentModals | Automatically blocks or dismisses cookie/GDPR consent banners. Available in BQL sessions and the /screenshot and /pdf REST APIs. In BQL, toggle it via the IDE or launch JSON. Useful for cleaner scraping by removing overlays. | `false` | ✅ | ❌ | ✅ |
| proxy | Routes browser traffic through a proxy. Options: proxy=residential for Browserless’s residential proxy pool; proxy=\`<your proxy URL>\` for your own proxy. Omit to use a direct connection. | none | ✅ | ✅ | ✅ |
| proxyCountry | Used with proxy=residential to specify the exit node’s country. Accepts ISO 3166 country codes (e.g., us, gb, de). If omitted, a random location is chosen. | none | ✅ | ✅ | ✅ |
| proxySticky | Used with proxy=residential to maintain the same proxy IP across a session (when possible). Useful for sites that expect consistent IP usage. | `false` | ✅ | ✅ | ✅ |
| timeout | Maximum session duration in milliseconds. The session will automatically close after this time to prevent overuse. | 60000 | ✅ | ✅ | ✅ |

## BaaS v2 Advanced Options [​](https://docs.browserless.io/overview/launch-parameters\#baas-v2-advanced-options "Direct link to BaaS v2 Advanced Options")

For BaaS v2, you can use the `launch` parameter to pass a JSON object with advanced Chrome flags and Puppeteer options. Learn more in our [Launch Options guide](https://docs.browserless.io/baas/chrome-flags):

- Puppeteer
- Playwright

```codeBlockLines_p187
const launchArgs = {
  headless: false,
  stealth: true,
  args: ['--window-size=1920,1080', '--force-color-profile=srgb']
};

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://production-sfo.browserless.io?token=YOUR_API_TOKEN&launch=${JSON.stringify(launchArgs)}`,
});

```

```codeBlockLines_p187
const launchArgs = {
  headless: false,
  stealth: true,
  args: ['--window-size=1920,1080', '--force-color-profile=srgb']
};

const browser = await playwright.chromium.connectOverCDP(
  `wss://production-sfo.browserless.io?token=YOUR_API_TOKEN&launch=${JSON.stringify(launchArgs)}`
);

```

## REST API Options [​](https://docs.browserless.io/overview/launch-parameters\#rest-api-options "Direct link to REST API Options")

When using REST APIs, you can include launch parameters in the URL query string or in the JSON body of your request:

```codeBlockLines_p187
// In URL query string
fetch("https://production-sfo.browserless.io/screenshot?token=YOUR_API_TOKEN&blockAds=true&stealth=true")

// In JSON body
fetch("https://production-sfo.browserless.io/pdf?token=YOUR_API_TOKEN", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    url: "https://example.com",
    options: { format: "A4" },
    launch: { stealth: true, blockAds: true }
  })
})

```

For a comprehensive list of available REST API endpoints and their parameters, please refer to our [Swagger API documentation](https://docs.browserless.io/open-api).

For a comprehensive list of Chrome flags and browserless-specific options, please refer to our [Launch Options](https://docs.browserless.io/baas/chrome-flags) documentation.

- [Passing Launch Options](https://docs.browserless.io/overview/launch-parameters#passing-launch-options)
- [Common Launch Options](https://docs.browserless.io/overview/launch-parameters#common-launch-options)
- [BaaS v2 Advanced Options](https://docs.browserless.io/overview/launch-parameters#baas-v2-advanced-options)
- [REST API Options](https://docs.browserless.io/overview/launch-parameters#rest-api-options)