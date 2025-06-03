---
url: "https://docs.browserless.io/baas/v1/apis/screencast"
title: "/screencast API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/apis/screencast#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/rest-apis/intro) or [BrowserQL](https://docs.browserless.io/browserql/start).

> The screencast API is still under beta, and isn't recommended yet for production usage.

The screencast API allows for generating video files, on demand, of your puppeteer scripts. This simple REST API allows for POSTing of an `application/json` _or_ `application/javascript` body of your code you'd like to record. The resulting response is a `webm` file with the video attached. Audio is now supported in our screencast API as of docker version `1.8.0`.

The resulting video's dimensions are _inherited_ by the width and height of the browser. You can change this very easily by calling `page.setViewport` with your dimensions in your scripts as well as setting `--window-size` in the URL.

Check out this API schema defined in [Swagger](https://chrome.browserless.io/docs/#/Browser%20API/post_screencast).

## Basic Usage [​](https://docs.browserless.io/baas/v1/apis/screencast\#basic-usage "Direct link to Basic Usage")

**Example body**

```codeBlockLines_p187
module.exports = async ({ page }) => {
  const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

  await page.setViewport({ width: 1920, height: 1080 });
  await page.goto('https://www.youtube.com/watch?v=GnEmD17kYsE');
  await sleep(10000);
};

```

And the resulting `cURL` call:

**Full cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/screencast?token=MY-API-TOKEN&--window-size=1920,1080 \
  -o video.webm \
  -H 'Content-Type: application/javascript' \
  -d '
    module.exports = async ({ page }) => {
      const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

      await page.setViewport({ width: 1920, height: 1080 });
      await page.goto(`https://www.youtube.com/watch?v=GnEmD17kYsE`);
      await sleep(10000);
    };
  '

```

## Using `application/javascript` content-type [​](https://docs.browserless.io/baas/v1/apis/screencast\#using-applicationjavascript-content-type "Direct link to using-applicationjavascript-content-type")

The `application/javascript` content-type is great for testing quick scripts and seeing their output and works with many tools like postman for faster feedback. When using this API you'll need to specify an appropriate content-type for the body of the request. When the type is `application/json` the /screencast API follows a similar semantic of the `/function` API, where you'll apply both a `code` property and a `context` property.

This makes your request more reusable as you can specify arguments in the `context` property that your code can reference. The only limitation is that all parameters will need to be hard-coded.

**Example code body**

```codeBlockLines_p187
module.exports = async ({ page, context }) => {
  const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

  const { url, wait, width, height } = context;
  await page.setViewport({ width, height });
  await page.goto(url);
  await sleep(wait);
};

```

**context object example**

```codeBlockLines_p187
// JSON body
// Code is minified here!
{
  "code": "module.exports = async ({ page, context }) => { const sleep = (ms) => new Promise((res) => setTimeout(res, ms)); const { url, wait, width, height } = context; await page.setViewport({ width, height }); await page.goto(url); await sleep(wait); };",
  "context": {
    "url": "https://www.youtube.com/watch?v=GnEmD17kYsE",
    "wait": 1000,
    "width": 1920,
    "height": 1080
  }
}

```

**Full cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/screencast?token=YOUR-API-TOKEN&--window-size=1920,1080 \
  -o video.webm \
  -H 'Content-Type: application/json' \
  -d '{
  "code": "module.exports = async ({ page, context }) => { const sleep = (ms) => new Promise((res) => setTimeout(res, ms)); const { url, wait, width, height } = context; await page.setViewport({ width, height }); await page.goto(url); await sleep(wait); };",
  "context": {
    "url": "https://www.youtube.com/watch?v=GnEmD17kYsE",
    "wait": 5000,
    "width": 1920,
    "height": 1080
  }
}'

```

## Programmatic control [​](https://docs.browserless.io/baas/v1/apis/screencast\#programmatic-control "Direct link to Programmatic control")

By default, browserless will start recording the session immediately and will stop once your function completes execution. You can change this behavior by using two functions in your code: `startScreencast` and `stopScreencast`:

**Starting the screencast after load**

```codeBlockLines_p187
module.exports = async ({ page, startScreencast, stopScreencast }) => {
  const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

  await page.goto('https://vclock.com/stopwatch');
  await page.click('#btn-resume');
  startScreencast();
  await sleep(5000);
  stopScreencast();
};

```

**Full cURL request**

```codeBlockLines_p187
curl -X POST \
  https://chrome.browserless.io/screencast?token=YOUR-API-TOKEN \
  -H 'Content-Type: application/javascript' \
  -d 'module.exports = async ({ page, startScreencast, stopScreencast }) => {
    const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

    await page.goto("https://vclock.com/stopwatch");
    await page.click("#btn-resume");
    startScreencast();
    await sleep(5000);
    stopScreencast();
}'

```

- [Basic Usage](https://docs.browserless.io/baas/v1/apis/screencast#basic-usage)
- [Using `application/javascript` content-type](https://docs.browserless.io/baas/v1/apis/screencast#using-applicationjavascript-content-type)
- [Programmatic control](https://docs.browserless.io/baas/v1/apis/screencast#programmatic-control)