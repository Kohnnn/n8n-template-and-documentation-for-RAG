---
url: "https://docs.browserless.io/enterprise/docker/quickstart"
title: "Docker Quick Start | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/docker/quickstart#__docusaurus_skipToContent_fallback)

On this page

The docker image that powers the core of Browserless is available for free for open-source projects. Using it is about as simple as using the Browserless service itself with the only difference being that you'll have to launch and manage the infrastructure.

At a high-level, we'll do the following:

1. [Run the docker image](https://docs.browserless.io/enterprise/docker/quickstart#1-run-it-with-some-sensible-defaults).
2. [Update our app to connect to this image](https://docs.browserless.io/enterprise/docker/quickstart#2-update-your-app-to-use-browserless).

## 1\. Run it with some sensible defaults [​](https://docs.browserless.io/enterprise/docker/quickstart\#1-run-it-with-some-sensible-defaults "Direct link to 1. Run it with some sensible defaults")

Running the docker image is similar to other `docker run` commands, and all options are passed in via environment variables. In the example below, we're starting with the image with a maximum concurrency of `10`, further requests will remain open and ran when a slot opens up. We're also setting the token to `6R0W53R135510`.

warning

Browserless is designed to **always** require a token. This means that, if you don't pass a `TOKEN` env variable, **a randomly generated token will be set**.

After the image is pulled (one time only), then you'll see the first of our logs, which will print the final configuration.

```codeBlockLines_p187
$ docker run \
  --rm \
  -p 3000:3000 \
  -e "CONCURRENT=10" \
  -e "TOKEN=6R0W53R135510" \
  ghcr.io/browserless/chromium

```

Feel free to visit [http://localhost:3000/docs](http://localhost:3000/docs) to see if the image is running properly. You can also read more about the different variables on our [docker section](https://docs.browserless.io/enterprise/docker/config).

## 2\. Update your app to use Browserless [​](https://docs.browserless.io/enterprise/docker/quickstart\#2-update-your-app-to-use-browserless "Direct link to 2. Update your app to use Browserless")

Once we have Browserless running we can simply use it inside of our application instead of launching it locally. There's more details in our docs about using Puppeteer or Playwright, but here is an example:

- Puppeteer
- Playwright

```codeBlockLines_p187
const express = require("express");
const puppeteer = require("puppeteer-core");

const app = express();

app.get("/image", async (req, res) => {
// This was puppeteer.launch()
const browser = await puppeteer.connect({
  browserWSEndpoint: "ws://localhost:3000?token=6R0W53R135510",
});
const page = await browser.newPage();

await page.goto("http://www.example.com/");
const data = await page.screenshot();
browser.close();

return res.end(data, "binary");
});

app.listen(8080);

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
const express = require('express');
const playwright = require('playwright');

const app = express();

app.get('/image', async (req, res) => {
  const browser = await playwright.chromium.connectOverCDP('ws://localhost:3000?token=6R0W53R135510');

  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('http://www.example.com/');
  await new Promise((resolve) => setTimeout(resolve, 5000));
  const data = await page.screenshot({ type: 'png' });

  await browser.close();

  return res.end(data, 'binary');
});

app.listen(8080);

```

```codeBlockLines_p187
from flask import Flask, send_file
from playwright.sync_api import sync_playwright
import io

app = Flask(__name__)

@app.route("/image", methods=["GET"])
def capture_image():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("ws://localhost:3000?token=6R0W53R135510")
        context = browser.new_context()
        page = context.new_page()

        page.goto("http://www.example.com/")
        page.wait_for_timeout(5000)
        screenshot = page.screenshot(type="png")

        browser.close()

        return send_file(io.BytesIO(screenshot), mimetype="image/png")

if __name__ == "__main__":
    app.run(port=8080)

```

```codeBlockLines_p187
import com.microsoft.playwright.*;
import static spark.Spark.*;
import java.io.OutputStream;

public class PlaywrightImageServer {
    public static void main(String[] args) {
        port(8080);

        get("/image", (req, res) -> {
            try (Playwright playwright = Playwright.create()) {
                Browser browser = playwright.chromium().connectOverCDP("ws://localhost:3000?token=6R0W53R135510");
                BrowserContext context = browser.newContext();
                Page page = context.newPage();

                page.navigate("http://www.example.com/");
                page.waitForTimeout(5000);
                byte[] screenshot = page.screenshot(new Page.ScreenshotOptions().setType("png"));

                browser.close();

                res.type("image/png");
                OutputStream outputStream = res.raw().getOutputStream();
                outputStream.write(screenshot);
                outputStream.flush();

                return res.raw();
            } catch (Exception e) {
                res.status(500);
                return "Error capturing screenshot: " + e.getMessage();
            }
        });
    }
}

```

```codeBlockLines_p187
using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Hosting;
using Microsoft.Playwright;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/image", async context =>
{
    try
    {
        var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync("ws://localhost:3000?token=6R0W53R135510");

        var page = await (await browser.NewContextAsync()).NewPageAsync();
        await page.GotoAsync("http://www.example.com/");
        await Task.Delay(5000);

        var screenshot = await page.ScreenshotAsync(new PageScreenshotOptions { Type = ScreenshotType.Png });

        context.Response.ContentType = "image/png";
        await context.Response.Body.WriteAsync(screenshot);

        await browser.CloseAsync();
    }
    catch (Exception e)
    {
        context.Response.StatusCode = 500;
        await context.Response.WriteAsync("Error capturing screenshot: " + e.Message);
    }
});

app.Run("http://localhost:8080");

```

## What's next? [​](https://docs.browserless.io/enterprise/docker/quickstart\#whats-next "Direct link to What's next?")

There's a lot more that you can configure and tune in Browserless to handle the needs of your application. Be sure to read about all the options it exposes and how to get the most out of the Browserless image!

We also have docs for extra features for licensed users such as:

- [Watching sessions](https://docs.browserless.io/enterprise/watching-sessions)
- [Live Debugger](https://docs.browserless.io/enterprise/live-debugger)
- [Utility Functions](https://docs.browserless.io/enterprise/utility-functions/intro)
- [Worker settings](https://docs.browserless.io/enterprise/private-deployment/worker-settings)

- [1\. Run it with some sensible defaults](https://docs.browserless.io/enterprise/docker/quickstart#1-run-it-with-some-sensible-defaults)
- [2\. Update your app to use Browserless](https://docs.browserless.io/enterprise/docker/quickstart#2-update-your-app-to-use-browserless)
- [What's next?](https://docs.browserless.io/enterprise/docker/quickstart#whats-next)