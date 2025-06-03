---
url: "https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent"
title: "Setting a user agent | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/avoid-bot-detection/user-agent) or [BrowserQL](https://docs.browserless.io/browserql/start).

The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent.

Many sites use this information to render the site differently for each user, and sometimes even for rudimentary bot detection. If you run chrome headless and want to take a screenshot of a page, it's a good idea to set a user agent so that web fonts load properly.

## Code [​](https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent\#code "Direct link to Code")

You can set the user agent from code, in puppeteer it would be like this:

```codeBlockLines_p187
await page.setUserAgent(
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
);

```

## REST API [​](https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent\#rest-api "Direct link to REST API")

If you're using our APIs like /screenshot, /content, /pdf, or /scrape, you can also set the user agent in the body of your request.

```codeBlockLines_p187
{
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
}

```

## Hosted service [​](https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent\#hosted-service "Direct link to Hosted service")

If you're on a usage-based, cloud unit-based or capacity-based account, you can change the user agent as so

```codeBlockLines_p187
const browser = await puppeteer.connect({
  browserWSEndpoint:
    'wss://chrome.browserless.io?token=YOUR_API_KEY&--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
});

```

## Self-hosting [​](https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent\#self-hosting "Direct link to Self-hosting")

If you're self hosting, you can set the user agent as a default launch argument.

```codeBlockLines_p187
    docker run -e "DEFAULT_LAUNCH_ARGS=[\"--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\"]" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

- [Code](https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent#code)
- [REST API](https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent#rest-api)
- [Hosted service](https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent#hosted-service)
- [Self-hosting](https://docs.browserless.io/baas/v1/recipes/setting-a-user-agent#self-hosting)