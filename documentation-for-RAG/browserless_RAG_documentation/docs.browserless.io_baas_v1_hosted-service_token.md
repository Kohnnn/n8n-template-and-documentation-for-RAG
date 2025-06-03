---
url: "https://docs.browserless.io/baas/v1/hosted-service/token"
title: "Using your API token | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/hosted-service/token#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/start) or [BrowserQL](https://docs.browserless.io/browserql/start).

When you sign-up for a browserless account, we create a unique token that allows you to interact with the service. Once your worker(s) are ready you should use this token anytime you interact with the service.

You can use this token with most of our integrations by simply appending a `?token=YOUR-API-TOKEN` as a query-string parameter. **The only exception is the webdriver integration as most libraries strip query-parameters for remote servers**. For webdriver connections, use the format `https://YOUR-API-TOKEN@chrome.browserless.io/webdriver`.

For the purposes of illustrating these examples, we'll assume your API-TOKEN is `094632bb-e326-4c63-b953-82b55700b14c`.

## Example integrations [​](https://docs.browserless.io/baas/v1/hosted-service/token\#example-integrations "Direct link to Example integrations")

### Puppeteer with your API Token [​](https://docs.browserless.io/baas/v1/hosted-service/token\#puppeteer-with-your-api-token "Direct link to Puppeteer with your API Token")

```codeBlockLines_p187
const browser = puppeteer.connect({
  browserWSEndpoint: 'wss://chrome.browserless.io?token=094632bb-e326-4c63-b953-82b55700b14c',
});

```

### REST with your API Token [​](https://docs.browserless.io/baas/v1/hosted-service/token\#rest-with-your-api-token "Direct link to REST with your API Token")

#### Query parameter [​](https://docs.browserless.io/baas/v1/hosted-service/token\#query-parameter "Direct link to Query parameter")

The basic way to send your API token over HTTP, is to simply add it as a query parameter:

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/content?token=094632bb-e326-4c63-b953-82b55700b14c \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '
{
  "url": "https://example.com/"
}'

```

#### Header Authentication [​](https://docs.browserless.io/baas/v1/hosted-service/token\#header-authentication "Direct link to Header Authentication")

You can also add an `Authorization` header for REST API requests as well. Browserless uses the `Basic` auth scheme to get the token:

warning

As per [the HTTP specification](https://httpwg.org/specs/rfc9110.html#authentication), the token **must** be encoded in base64, otherwise you can get `4XX` or `5XX` responses.

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/content \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Basic MDk0NjMyYmItZTMyNi00YzYzLWI5NTMtODJiNTU3MDBiMTRj' \
  -d '
{
  "url": "https://example.com/"
}'

```

### Webdriver with your API Token [​](https://docs.browserless.io/baas/v1/hosted-service/token\#webdriver-with-your-api-token "Direct link to Webdriver with your API Token")

warning

Webdriver and Selenium are deprecated in Browserless V2 and beyond, and will eventually be removed altogether from our cloud.

```codeBlockLines_p187
const chromeCapabilities = webdriver.Capabilities.chrome();
chromeCapabilities.set('browserless:token', '094632bb-e326-4c63-b953-82b55700b14c');
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
  .usingServer('https://chrome.browserless.io/webdriver')
  .build();

```

- [Example integrations](https://docs.browserless.io/baas/v1/hosted-service/token#example-integrations)
  - [Puppeteer with your API Token](https://docs.browserless.io/baas/v1/hosted-service/token#puppeteer-with-your-api-token)
  - [REST with your API Token](https://docs.browserless.io/baas/v1/hosted-service/token#rest-with-your-api-token)
  - [Webdriver with your API Token](https://docs.browserless.io/baas/v1/hosted-service/token#webdriver-with-your-api-token)