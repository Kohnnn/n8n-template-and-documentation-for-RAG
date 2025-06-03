---
url: "https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright"
title: "A guide to use Hybrid with BQL | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#__docusaurus_skipToContent_fallback)

On this page

This guide demonstrates how to use BrowserQL with our Hybrid feature, which allows you to connect Playwright to an existing BrowserQL session. This is particularly useful when you need to:

- Use BQL-specific features
- Use Playwright's rich API alongside BQL
- Monitor browser activity through a LiveURL
- Unblock sites and perform other browser actions by using Playwright
- Need to provide a LiveURL and listen to when it's being closed.

## LiveURL directly from BQL [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#liveurl-directly-from-bql "Direct link to LiveURL directly from BQL")

A LiveURL can also be generated directly from BQL, but you won't be able to listen to when it's been closed and then continue using that browser.
The benefit of using a library such as playwright in conjunction with BQL is that you'll be able to wait for the end-user to finish using the LiveURL and then continue your automation after that, amongst other workflows.
You can generate a LiveURL from BQL directly and then use the reconnect api as well, however there's a max time to how long the reconnect URL can be alive before it dies off, so using a BQL + LiveURL + Reconnect is best done with a Library such as Playwright or Puppeteer.

## Prerequisites [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#prerequisites "Direct link to Prerequisites")

Before running this script, make sure you have:

1. Node.js installed on your system
2. A browserless API key
3. The required npm packages, make sure the playwright version is [supported by Browserless](https://docs.browserless.io/baas/private-deployment/versions)






```codeBlockLines_p187
npm install playwright-core@1.50.1

```


## Complete Example [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#complete-example "Direct link to Complete Example")

Here's a complete example that shows how to:

1. Initialize a BrowserQL session
2. Connect Playwright to the session
3. Monitor the session through a LiveURL
4. Perform browser actions
5. Capture screenshots

```codeBlockLines_p187
// Import required dependencies
import { chromium } from 'playwright-core';
const token = "YOUR-API-KEY";
const timeout = 5 * 60 * 1000; // 5 minutes timeout
const url = 'https://www.example.com';

// Configure query parameters for BrowserQL
const queryParams = new URLSearchParams({
  token,
  timeout,
  proxy: "residential", // Use residential proxy for better bot detection bypassing
  proxyCountry: "us"   // Set proxy country to US or whichever country the target site is for
}).toString();

// Define the BQL mutation to initialize the session
const query = `
  mutation ReconnectToPlaywright($url: String!) {
    goto(url: $url, waitUntil: networkIdle) {
      status
    }
    #The mutation below is an example of a bql-specific mutations you could need before connecting to playwright
    #verify(type: cloudflare) {
      #found
      #solved
      #time
    #}
    reconnect(timeout: 30000) {
      browserWSEndpoint
    }
  }
`;

const variables = { url };

// Construct the BrowserQL endpoint URL
const endpoint = `https://production-sfo.browserless.io/chromium/bql?${queryParams}`;

// Configure the fetch request options
const options = {
  method: 'POST',
  headers: {
    'content-type': 'application/json',
  },
  body: JSON.stringify({
    query,
    variables,
  }),
};

// Main execution function
(async () => {
  try {
    console.log(`Initializing BrowserQL session for URL: ${url}`);

    // Send the initial BQL query
    const response = await fetch(endpoint, options);

    if (!response.ok) {
      throw new Error(`Failed to initialize session:\n${await response.text()}`);
    }

    // Extract the WebSocket endpoint for Playwright connection
    const { data } = await response.json();
    const browserWSEndpoint = data.reconnect.browserWSEndpoint;
    const endpointReconnect = `${browserWSEndpoint}?${queryParams}`;

    console.log(`Session initialized! Connecting Playwright to ${endpointReconnect}`);

    // Connect Playwright to the BrowserQL session
    const browser = await chromium.connectOverCDP(endpointReconnect);

    // Get the existing context and page
    const [context] = await browser.contexts();
    const page = await context.pages()[0];

    // Create a CDP session for advanced browser control
    const cdpSession = await context.newCDPSession(page);

    // Get the LiveURL for monitoring the session
    const { liveURL } = await cdpSession.send('Browserless.liveURL');
    console.log('Monitor or interact with your session at:', liveURL); //You can open this in a new tab or place it inside an iFrame

    // Example: Perform some browser actions
    // await page.click('.some-button');
    // await page.type('.some-input', 'Hello World');
    /*await page.evaluate(() => {
      document.getElementById("myElement")?.remove();
    });*/

    // Wait for the live session to complete
    await new Promise((resolve) => {
      cdpSession.on('Browserless.liveComplete', resolve);
    });

    console.log(`Session completed. URL the session ended on: ${page.url()}`);

    // Capture a screenshot of the final state
    await page.screenshot({
      fullPage: false,
      path: 'session-screenshot.png'
    });

    // Clean up: close the browser connection
    await browser.close();
    console.log('Browser session closed successfully.');
  } catch (error) {
    console.error('Session error:', error);
  }
})();

```

## Understanding the Code [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#understanding-the-code "Direct link to Understanding the Code")

### 1\. Initial Setup [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#1-initial-setup "Direct link to 1. Initial Setup")

- The script requires a browserless API key to work, [sign up here](https://www.browserless.io/pricing)
- It configures a 5-minute timeout and sets up residential proxy settings
- The `queryParams` object contains all necessary parameters for the BrowserQL session

### 2\. BQL Query [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#2-bql-query "Direct link to 2. BQL Query")

- The `ReconnectToPlaywright` mutation is used to:

1. Navigate to the specified URL
2. Wait for network activity to settle
3. Use BQL-specific features such as verifying cloudflare
4. Get a WebSocket endpoint for Playwright connection

### 3\. Playwright Integration [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#3-playwright-integration "Direct link to 3. Playwright Integration")

- After getting the WebSocket endpoint, Playwright connects to the BrowserQL session
- The script retrieves the existing browser context and page
- You can further manipulate the website with Playwright, such as removing unwanted HTML elements before sharing the LiveURL to your end-user.
- A CDP (Chrome DevTools Protocol) session is created for advanced browser control

### 4\. Live Monitoring [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#4-live-monitoring "Direct link to 4. Live Monitoring")

- The script obtains a LiveURL through the CDP session
- This URL allows you to monitor and interact with the browser session in real-time
- The session continues until the `Browserless.liveComplete` event is received

### 5\. Cleanup [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#5-cleanup "Direct link to 5. Cleanup")

- The script captures a screenshot of the final state
- Finally, it properly closes the browser connection

## Best Practices [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#best-practices "Direct link to Best Practices")

1. **Error Handling**
   - Always wrap the main execution in a try-catch block
   - Log errors with meaningful messages
   - Clean up resources in case of errors
2. **Session Management**
   - Set appropriate timeouts for your use case
   - Use residential proxies when needed
   - Monitor the LiveURL for debugging
3. **Resource Cleanup**
   - Always close browser connections
   - Save important data (screenshots, logs) before cleanup

## Common Use Cases [​](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright\#common-use-cases "Direct link to Common Use Cases")

1. **Debugging BQL Queries**
   - Use the LiveURL to monitor query execution
   - Watch network requests and responses
   - Debug JavaScript errors in real-time
2. **Complex Browser Automation**
   - Combine BQL's simplicity and unblocking features with Playwright's power
   - Use CDP for advanced browser control
   - Capture screenshots and network data
3. **Testing and Monitoring**
   - Monitor browser sessions in real-time
   - Observe the actual flow of an automation
   - Debug issues with live browser inspection

- [LiveURL directly from BQL](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#liveurl-directly-from-bql)
- [Prerequisites](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#prerequisites)
- [Complete Example](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#complete-example)
- [Understanding the Code](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#understanding-the-code)
  - [1\. Initial Setup](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#1-initial-setup)
  - [2\. BQL Query](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#2-bql-query)
  - [3\. Playwright Integration](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#3-playwright-integration)
  - [4\. Live Monitoring](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#4-live-monitoring)
  - [5\. Cleanup](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#5-cleanup)
- [Best Practices](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#best-practices)
- [Common Use Cases](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright#common-use-cases)