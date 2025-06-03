---
url: "https://docs.browserless.io/baas/v1/hosted-service/best-practices"
title: "Best Practices | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/hosted-service/best-practices#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/troubleshooting/best-practices) or [BrowserQL](https://docs.browserless.io/browserql/start).

Aside from getting everything setup and running, there's a few best practices that'll help ensure your sessions are operating well. Below is a couple of highlights for running healthy headless scripts.

## Make sure you close your session [​](https://docs.browserless.io/baas/v1/hosted-service/best-practices\#make-sure-you-close-your-session "Direct link to Make sure you close your session")

When finished with work, or on errors, make sure you run `browser.close` so that other sessions may start. browserless _will_ terminate long-running sessions via the timeout setting, but it's always a good idea to close tidly whenever you're finished.

```codeBlockLines_p187
const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://chrome.browserless.io?token=YOUR-TOKEN-HERE`,
});

const page = await browser.newPage();

try {
  await page.goto('https://www.browserless.io/');
  await page.screenshot({ path: './browserless.png' });
  browser.close();
} catch (error) {
  console.error({ error }, 'Something happened!');
  browser.close();
}

```

## Reduce `await`'s as much as possible [​](https://docs.browserless.io/baas/v1/hosted-service/best-practices\#reduce-awaits-as-much-as-possible "Direct link to reduce-awaits-as-much-as-possible")

Most of the puppeteer is async, meaning any command with `await` in front of it (or `.then`'s) is going to make a round-trip from your application to browserless and back. While you can only do so much to limit this you should definitely try and do as much as possible. For instance, use `page.evaluate` over `page.$selector` as you can accomplish a lot in one `evaluate` versus multiple `$selector` calls.

**DON'T DO**

```codeBlockLines_p187
const $button = await page.$('.buy-now');
const buttonText = await $button.getProperty('innerText');
const clicked = await $button.click();

```

**DO**

```codeBlockLines_p187
const buttonText = await page.evaluate(() => {
  const $button = document.querySelector('.buy-now');
  const clicked = $button.click();

  return $button.innerText;
});

```

## Use the GraphQL API to do pre-session checks [​](https://docs.browserless.io/baas/v1/hosted-service/best-practices\#use-the-graphql-api-to-do-pre-session-checks "Direct link to Use the GraphQL API to do pre-session checks")

If you've been getting rejections or queued, be sure to use the GraphQL API to do pre-session checks. This allows your workers to remain up and healthy, allowing sessions to go smoothly.

```codeBlockLines_p187
# https://api.browserless.io/graphql
{
  pressure(apiToken: "YOUR-API-TOKEN") {
    running
    recentlyRejected
    queued
    isAvailable
    date
  }
}

```

This request will return a JSON object with the following payload:

```codeBlockLines_p187
// JSON returned
{
  "data": {
    "pressure": {
      "running": 0,
      "recentlyRejected": 0,
      "queued": 0,
      "isAvailable": true,
      "date": 1524762532204
    }
  }
}

```

You can use the `isAvailable` boolean to check to see if the instance can handle more connections. Otherwise you're free to write any sort of custom check with the provided JSON response.

## Seen Improvements Yourself? [​](https://docs.browserless.io/baas/v1/hosted-service/best-practices\#seen-improvements-yourself "Direct link to Seen Improvements Yourself?")

If you've seen improvements or have practices you think the community would benefit from, we'd [love to hear from you!](https://www.browserless.io/contact)

- [Make sure you close your session](https://docs.browserless.io/baas/v1/hosted-service/best-practices#make-sure-you-close-your-session)
- [Reduce `await`'s as much as possible](https://docs.browserless.io/baas/v1/hosted-service/best-practices#reduce-awaits-as-much-as-possible)
- [Use the GraphQL API to do pre-session checks](https://docs.browserless.io/baas/v1/hosted-service/best-practices#use-the-graphql-api-to-do-pre-session-checks)
- [Seen Improvements Yourself?](https://docs.browserless.io/baas/v1/hosted-service/best-practices#seen-improvements-yourself)