---
url: "https://docs.browserless.io/baas/session-management/screencasting"
title: "Screencast API | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/session-management/screencasting#__docusaurus_skipToContent_fallback)

Version: v2

On this page

The screencast API allows for generating `webm` video files on demand of your Puppeteer or Playwright scripts. The API supports recording audio.

The resulting video's dimensions are inherited by the width and height of the browser. You can change this very easily by calling `page.setViewport` with your dimensions in your scripts as well as setting `--window-size` in the URL.

## Usage [​](https://docs.browserless.io/baas/session-management/screencasting\#usage "Direct link to Usage")

This API works over CDP, thus you can use with with Puppeteer, Playwright, ChromeCDP or any other library that support CDP connections. **You must add `record=true` to your connection string in order to use this API**.

- Puppeteer
- Playwright

```codeBlockLines_p187
import fs from "fs";
import puppeteer from "puppeteer-core";

const sleep = (ms) => new Promise((res) => setTimeout(res, ms));
const token = "YOUR_API_TOKEN_HERE"

const wsEndpoint = `wss://production-sfo.browserless.io?token=${token}&headless=false&stealth&record=true`;
const browser = await puppeteer.connect({ browserWSEndpoint: wsEndpoint });
const page = await browser.newPage();
await page.goto("https://browserless.io");

// The magic happens here
const cdp = await page.createCDPSession();
await cdp.send("Browserless.startRecording");
await sleep(15000);
const response = await cdp.send("Browserless.stopRecording");
// ☝️ The response is a string containing a valid webm file

const file = Buffer.from(response.value, "binary");
await fs.promises.writeFile("./recording.webm", file);

await browser.close();

```

- Javascript
- Python
- Java
- C#

warning

On Playwright, you **must** use the already existing context and page and avoid creating new ones.

```codeBlockLines_p187
import playwright from "playwright";
import fs from "fs/promises";

const sleep = (ms) => new Promise((res) => setTimeout(res, ms));
const token = "YOUR_API_TOKEN_HERE";

const wsEndpoint = `wss://production-sfo.browserless.io?token=${token}&headless=false&stealth&record=true`;

(async () => {
  // Connect to the remote browser
  const browser = await playwright.chromium.connectOverCDP(wsEndpoint);

  // Reuse the context and page
  const context = browser.contexts()[0];
  const page = context.pages()[0];
  await page.goto("https://browserless.io");

  // The magic happens here
  const cdpSession = await page.context().newCDPSession(page);
  await cdpSession.send("Browserless.startRecording");
  // Wait for some time while recording
  await sleep(15000);

  // Stop recording and get the response
  const response = await cdpSession.send("Browserless.stopRecording");
  const file = Buffer.from(response.value, "binary");

  // Save the recording as a webm file
  await fs.writeFile("./recording.webm", file);

  await browser.close();
})();

```

warning

On Playwright, you **must** use the already existing context and page and avoid creating new ones.

```codeBlockLines_p187
from playwright.sync_api import sync_playwright
import time

TOKEN = "YOUR_API_TOKEN_HERE"
WS_ENDPOINT = (
    f"wss://production-sfo.browserless.io?token={TOKEN}&headless=false&stealth&record=true"
)

with sync_playwright() as playwright:
    # Connect to the remote browser
    browser = playwright.chromium.connect_over_cdp(WS_ENDPOINT)

    # Reuse the context and page
    context = browser.contexts[0]
    page = context.pages[0]
    page.goto("https://browserless.io")

    # The magic happens here
    cdp_session = context.new_cdp_session(page)
    cdp_session.send("Browserless.startRecording")

    # Wait for some time while recording
    time.sleep(15)

    # Stop recording and get the response
    response = cdp_session.send("Browserless.stopRecording")
    recording_data = response["value"]

    # Directly write the binary data to a file
    with open("recording.webm", "wb") as file:
        file.write(recording_data.encode("latin1"))

    browser.close()

```

warning

On Playwright, you **must** use the already existing context and page and avoid creating new ones.

```codeBlockLines_p187
import com.microsoft.playwright.*;
import java.nio.file.*;

public class App {
  public static void main(String[] args) {
    String TOKEN = "YOUR_API_TOKEN_HERE";
    String WS_ENDPOINT = String.format("wss://production-sfo.browserless.io?token=%s&headless=false&stealth&record=true",
        TOKEN);

    try (Playwright playwright = Playwright.create()) {
      // Connect to the remote browser
      Browser browser = playwright.chromium().connectOverCDP(WS_ENDPOINT);

      // Reuse the context and page
      Page page = browser.contexts().get(0).pages().get(0);
      page.navigate("https://browserless.io");

      // Start recording
      CDPSession cdpSession = browser.contexts().get(0).newCDPSession(page);
      cdpSession.send("Browserless.startRecording", null);

      // Wait for 15 seconds
      Thread.sleep(15000);

      // Stop recording
      var response = cdpSession.send("Browserless.stopRecording", null);
      String recordingData = response.get("value").getAsString();

      // Write binary data to a file
      byte[] fileData = recordingData.getBytes("ISO-8859-1");
      Files.write(Paths.get("recording.webm"), fileData);

      System.out.println("Recording saved as 'recording.webm'");
      browser.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}

```

warning

On Playwright, you **must** use the already existing context and page and avoid creating new ones.

```codeBlockLines_p187
using Microsoft.Playwright;
using System;
using System.IO;
using System.Text;

class BrowserlessRecording
{
    public static async Task Main(string[] args)
    {
        string TOKEN = "YOUR_API_TOKEN_HERE";
        string WS_ENDPOINT = $"wss://production-sfo.browserless.io?token={TOKEN}&headless=false&stealth&record=true";

        using var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync(WS_ENDPOINT);

        // Reuse the context and page
        var context = browser.Contexts[0];
        var page = context.Pages[0];

        await page.GotoAsync("https://browserless.io");

        // Start recording
        var cdpSession = await context.NewCDPSessionAsync(page);
        await cdpSession.SendAsync("Browserless.startRecording");

        // Wait for 15 seconds
        await Task.Delay(15000);

        // Stop recording
        var response = await cdpSession.SendAsync("Browserless.stopRecording");
        string recordingData = response.Value<string>("value");

        // Write binary data to a file
        byte[] fileData = Encoding.GetEncoding("ISO-8859-1").GetBytes(recordingData);
        await File.WriteAllBytesAsync("recording.webm", fileData);

        Console.WriteLine("Recording saved as 'recording.webm'");
        await browser.CloseAsync();
    }
}

```

- [Usage](https://docs.browserless.io/baas/session-management/screencasting#usage)