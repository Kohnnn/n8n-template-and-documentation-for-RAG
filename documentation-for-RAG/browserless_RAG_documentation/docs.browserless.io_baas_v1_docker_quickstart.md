---
url: "https://docs.browserless.io/baas/v1/docker/quickstart"
title: "Docker Quick Start | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/docker/quickstart#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/enterprise/docker/quickstart) or [BrowserQL](https://docs.browserless.io/browserql/start).

The docker image that powers the core of browserless is available for free for open-source projects. Using it is about as simple as using the browserless service itself with the only difference being that you'll have to launch and manage the infrastructure.

If you're interested in reading about setting up a project, then checkout the [quick-start guide here](https://docs.browserless.io/).

At a high-level, we'll do the following:

1. Run the docker image
2. Update our app to connect to this image.

## 1\. Run it with some sensible defaults [​](https://docs.browserless.io/baas/v1/docker/quickstart\#1-run-it-with-some-sensible-defaults "Direct link to 1. Run it with some sensible defaults")

Running the docker image is similar to other `docker run` commands, and all options are passed in via environment variables. In the example below, we're starting with the image with a maximum concurrency of `10`, further requests will remain open and ran when a slot opens up.

After the image is pulled (one time only), then you'll see the first of our logs, which will print the final configuration.

```codeBlockLines_p187
$ docker run \
  --rm \
  -p 3000:3000 \
  -e "MAX_CONCURRENT_SESSIONS=10" \
  browserless/chrome:latest

```

Feel free to visit [http://localhost:3000](http://localhost:3000/) to see if the image is running properly. You can also read more about the different variables on our [docker section](https://docs.browserless.io/baas/v1/docker/config).

## 2\. Update your app to use browserless [​](https://docs.browserless.io/baas/v1/docker/quickstart\#2-update-your-app-to-use-browserless "Direct link to 2. Update your app to use browserless")

Once we have browserless running we can simply use it inside of our application instead of launching it locally:

```codeBlockLines_p187
const express = require('express');
const puppeteer = require('puppeteer-core');

const app = express();

app.get('/image', async (req, res) => {
  // This was puppeteer.launch()
  const browser = await puppeteer.connect({ browserWSEndpoint: 'ws://localhost:3000' });
  const page = await browser.newPage();

  await page.goto('http://www.example.com/');
  const data = await page.screenshot();
  browser.close();

  return res.end(data, 'binary');
});

app.listen(8080);

```

## What's next? [​](https://docs.browserless.io/baas/v1/docker/quickstart\#whats-next "Direct link to What's next?")

There's a lot more that you can configure and tune in browserless to handle the needs of your application. Be sure to read about all the options it exposes and how to get the most out of the browserless image!

- [1\. Run it with some sensible defaults](https://docs.browserless.io/baas/v1/docker/quickstart#1-run-it-with-some-sensible-defaults)
- [2\. Update your app to use browserless](https://docs.browserless.io/baas/v1/docker/quickstart#2-update-your-app-to-use-browserless)
- [What's next?](https://docs.browserless.io/baas/v1/docker/quickstart#whats-next)