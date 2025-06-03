---
url: "https://docs.browserless.io/baas/recipes/uploading-files"
title: "Uploading files to sites | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/recipes/uploading-files#__docusaurus_skipToContent_fallback)

Version: v2

On this page

When automating browser tasks, you may need to upload files to websites. This guide demonstrates how to upload files to sites using Puppeteer with Browserless.

## Example: Uploading an image to a compression site [​](https://docs.browserless.io/baas/recipes/uploading-files\#example-uploading-an-image-to-a-compression-site "Direct link to Example: Uploading an image to a compression site")

The following example shows how to upload an image file to imagecompressor.com, a site that optimizes images:

```codeBlockLines_p187
import puppeteer from "puppeteer-core";
import path from 'path';

const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

const API_TOKEN = "YOUR_API_TOKEN_HERE";
const BROWSER_WS_ENDPOINT = `wss://production-sfo.browserless.io?token=${API_TOKEN}`;

(async() => {
    const browser = await puppeteer.connect({ browserWSEndpoint: BROWSER_WS_ENDPOINT });
    const page = await browser.newPage();

    // Navigate to the image compressor website
    console.log('Navigating to imagecompressor.com...');
    await page.goto('https://imagecompressor.com/');

    // Wait for the file input to be available
    console.log('Waiting for file input...');
    await page.waitForSelector('#fileSelector');

    // Get the file input element
    const fileInput = await page.$('#fileSelector');

    // Upload the image
    console.log('Uploading image...');
    await fileInput.uploadFile(path.join(process.cwd(), 'screenshot.png'));

    // Wait 5 seconds to allow upload to process
    console.log('Waiting 5 seconds to allow upload...');
    await sleep(5000);

    // Take a screenshot to verify upload
    await page.screenshot({ path: 'imagecompressor_upload_result.png' });
    console.log('Screenshot taken: imagecompressor_upload_result.png');

    // Always close your sessions
    await browser.close();
})().catch((e) => {
    console.error('Error:', e);
});

```

## How it works [​](https://docs.browserless.io/baas/recipes/uploading-files\#how-it-works "Direct link to How it works")

1. **Connect to Browserless**: The script connects to Browserless using the WebSocket endpoint.
2. **Navigate to the target site**: Opens the image compression website.
3. **Locate the file input**: Waits for the file input element to be available.
4. **Upload the file**: Uses Puppeteer's `uploadFile` method to upload a local file.
5. **Wait for processing**: Allows time for the upload to complete.
6. **Verify the result**: Takes a screenshot to confirm the upload was successful.
7. **Clean up**: Closes the browser session.

## Tips for file uploads [​](https://docs.browserless.io/baas/recipes/uploading-files\#tips-for-file-uploads "Direct link to Tips for file uploads")

- Make sure the file exists at the specified path.
- Some sites may require clicking a button after selecting the file.
- For more complex upload forms, you might need to fill out additional fields.
- Always wait for the upload to complete before proceeding with further actions.

- [Example: Uploading an image to a compression site](https://docs.browserless.io/baas/recipes/uploading-files#example-uploading-an-image-to-a-compression-site)
- [How it works](https://docs.browserless.io/baas/recipes/uploading-files#how-it-works)
- [Tips for file uploads](https://docs.browserless.io/baas/recipes/uploading-files#tips-for-file-uploads)