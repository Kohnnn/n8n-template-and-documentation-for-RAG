---
url: "https://docs.browserless.io/baas/troubleshooting/http-error-codes"
title: "HTTP Error Codes | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/troubleshooting/http-error-codes#__docusaurus_skipToContent_fallback)

Version: v2

On this page

This document explains the common HTTP error codes you may encounter when using Browserless and how to resolve them. If you're interested in knowing the status code of the site being navigated to by one of our REST APIs, you can find the status code and status in the headers named `x-response-code` and `x-response-status`.

## HTTP response codes [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#http-response-codes "Direct link to HTTP response codes")

- [400 Bad Request](https://docs.browserless.io/baas/troubleshooting/http-error-codes#400-bad-request)
- [401 Unauthorized](https://docs.browserless.io/baas/troubleshooting/http-error-codes#401-unauthorized)
- [404 Not Found](https://docs.browserless.io/baas/troubleshooting/http-error-codes#404-not-found)
- [408 Request Timeout](https://docs.browserless.io/baas/troubleshooting/http-error-codes#408-request-timeout)
- [429 Too Many Requests](https://docs.browserless.io/baas/troubleshooting/http-error-codes#429-too-many-requests)

## 400 Bad Request [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#400-bad-request "Direct link to 400 Bad Request")

This error indicates that the request is badly formed and could not be processed.

Troubleshoot:

- You might bee sending a malformed JSON payload.
- You might be sending invalid fields for an specific API.
- You might be setting the timeout to a negative number or over 1800000 ms.
- Your request arguments might be colliding (for instance, using our internal proxy while connecting to a `--proxy-server` in your args).

## 401 Unauthorized [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#401-unauthorized "Direct link to 401 Unauthorized")

This error indicates that the request has not been applied because it lacks valid authentication credentials for the resource.

Troubleshoot:

- You might not be sending the API key in the WebSocket Endpoint properly.
- Your HTTP Client may be caching an old API key that's no longer valid.
- You might be using an endpoint not supported by your plan, e.g. trying to use the v2 endpoints, when being on a dedicated or legacy plan.

## 404 Not Found [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#404-not-found "Direct link to 404 Not Found")

This error indicates that the request's endpoint has not been found.

Troubleshoot:

- You might be trying to request a non-existent endpoint.

## 408 Request Timeout [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#408-request-timeout "Direct link to 408 Request Timeout")

This error indicates that the request has taken too long to process.

Troubleshoot:

- You might have set the timeout too low.
- You might be trying to wait for a selector or event the doesn't exist.
- Your dedicated workers might be unhealthy and unresponsive.

## 429 Too Many Requests [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#429-too-many-requests "Direct link to 429 Too Many Requests")

This error indicates that too many requests are currently being processed.

### Exceeding Concurrency Limits [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#exceeding-concurrency-limits "Direct link to Exceeding Concurrency Limits")

The most common cause of 429 errors is exceeding your plan's concurrency limit. Each Browserless plan has a maximum number of concurrent browser sessions that can run simultaneously:

| Plan | Concurrent Browsers |
| --- | --- |
| Free | 1 |
| Prototyping | 3 |
| Starter | 15 |
| Scale | 50 |
| Enterprise | Custom |

When you attempt to start more browser sessions than your plan allows, Browserless will return a 429 error to indicate that you've reached your concurrency limit.

You can view the current pricing and concurrency limits on the [Browserless pricing page](https://www.browserless.io/pricing).

#### How to resolve concurrency limit issues [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#how-to-resolve-concurrency-limit-issues "Direct link to How to resolve concurrency limit issues")

1. **Upgrade your plan**: If you consistently need more concurrent sessions, consider upgrading to a plan with higher concurrency limits.

2. **Implement request queuing**: Add a retry mechanism with exponential backoff to your code to handle 429 responses.

3. **Optimize your automation**: Review your code to ensure you're closing browser sessions properly and not keeping unnecessary sessions open.


### Improper Browser Closure [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#improper-browser-closure "Direct link to Improper Browser Closure")

Another common cause of 429 errors is improper browser closure. If your code doesn't properly close browser instances after use, especially during errors or exceptions, you may accumulate "zombie" sessions that count against your concurrency limit.

#### Proper browser closure with Puppeteer [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#proper-browser-closure-with-puppeteer "Direct link to Proper browser closure with Puppeteer")

Here's an example of how to properly close a browser with Puppeteer, even when errors occur:

```codeBlockLines_p187
const puppeteer = require('puppeteer-core');

async function runAutomation() {
  let browser = null;

  try {
    // Connect to browserless
    browser = await puppeteer.connect({
      browserWSEndpoint: 'wss://production-sfo.browserless.io?token=YOUR_API_KEY&timeout=300000',
    });

    const page = await browser.newPage();
    await page.goto('https://example.com');

    // Your automation code here
    const title = await page.title();
    console.log(`Page title: ${title}`);

    // More operations...

    return { success: true, data: title };
  } catch (error) {
    console.error('Automation error:', error);
    return { success: false, error: error.message };
  } finally {
    // Always close the browser, even if an error occurred
    if (browser) {
      await browser.close();
    }
  }
}

// Usage
runAutomation()
  .then(result => console.log('Finished:', result))
  .catch(err => console.error('Fatal error:', err));

```

#### Proper browser closure with Playwright [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#proper-browser-closure-with-playwright "Direct link to Proper browser closure with Playwright")

Here's a similar example using Playwright:

```codeBlockLines_p187
const { chromium } = require('playwright-core');

async function runAutomation() {
  let browser = null;

  try {
    // Connect to browserless
    browser = await chromium.connect({
      wsEndpoint: 'wss://production-sfo.browserless.io/chromium/playwright?token=YOUR_API_KEY&timeout=300000',
    });

    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto('https://example.com');

    // Your automation code here
    const title = await page.title();
    console.log(`Page title: ${title}`);

    // More operations...

    return { success: true, data: title };
  } catch (error) {
    console.error('Automation error:', error);
    return { success: false, error: error.message };
  } finally {
    // Always close the browser, even if an error occurred
    if (browser) {
      await browser.close();
    }
  }
}

// Usage
runAutomation()
  .then(result => console.log('Finished:', result))
  .catch(err => console.error('Fatal error:', err));

```

### Using Timeout Flag as a Quick Fix [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#using-timeout-flag-as-a-quick-fix "Direct link to Using Timeout Flag as a Quick Fix")

While implementing proper browser closure is the best long-term solution, you can use the `timeout` query parameter as a quick fix to ensure browsers don't live past a certain time limit. By default, Browserless has a global timeout of 15 minutes, but you can override this with the `timeout` parameter:

```codeBlockLines_p187
wss://production-sfo.browserless.io?token=YOUR_API_KEY&timeout=300000

```

The timeout value is specified in milliseconds (300000ms = 5 minutes). This ensures that even if your code fails to properly close the browser, Browserless will automatically terminate the session after the specified timeout.

This approach is particularly useful when:

- You're debugging 429 errors and need a quick solution
- You have legacy code that's difficult to update with proper error handling
- You want an additional safety mechanism alongside proper browser closure

### Best Practices to Avoid 429 Errors [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#best-practices-to-avoid-429-errors "Direct link to Best Practices to Avoid 429 Errors")

1. **Always use try/catch/finally blocks**: Ensure browser instances are closed in a `finally` block to guarantee cleanup even when errors occur.

2. **Implement connection pooling**: For high-volume applications, consider implementing a connection pool to reuse browser instances instead of creating new ones for each operation.

3. **Monitor your usage**: Keep track of your concurrent session usage to avoid hitting limits unexpectedly.

4. **Set explicit timeouts**: Configure reasonable timeouts using the `timeout` parameter to prevent browser sessions from hanging indefinitely.

5. **Implement graceful shutdown**: Ensure your application properly closes all browser instances when shutting down.


If you continue to experience 429 errors despite following these best practices, please contact [Browserless support](https://www.browserless.io/contact) for assistance.

### Other Troubleshooting for 429 Errors [​](https://docs.browserless.io/baas/troubleshooting/http-error-codes\#other-troubleshooting-for-429-errors "Direct link to Other Troubleshooting for 429 Errors")

- You might be running more concurrent sessions than expected.
- Your dedicated workers might be unhealthy and unresponsive, thus rejecting any incomming traffic.

- [HTTP response codes](https://docs.browserless.io/baas/troubleshooting/http-error-codes#http-response-codes)
- [400 Bad Request](https://docs.browserless.io/baas/troubleshooting/http-error-codes#400-bad-request)
- [401 Unauthorized](https://docs.browserless.io/baas/troubleshooting/http-error-codes#401-unauthorized)
- [404 Not Found](https://docs.browserless.io/baas/troubleshooting/http-error-codes#404-not-found)
- [408 Request Timeout](https://docs.browserless.io/baas/troubleshooting/http-error-codes#408-request-timeout)
- [429 Too Many Requests](https://docs.browserless.io/baas/troubleshooting/http-error-codes#429-too-many-requests)
  - [Exceeding Concurrency Limits](https://docs.browserless.io/baas/troubleshooting/http-error-codes#exceeding-concurrency-limits)
  - [Improper Browser Closure](https://docs.browserless.io/baas/troubleshooting/http-error-codes#improper-browser-closure)
  - [Using Timeout Flag as a Quick Fix](https://docs.browserless.io/baas/troubleshooting/http-error-codes#using-timeout-flag-as-a-quick-fix)
  - [Best Practices to Avoid 429 Errors](https://docs.browserless.io/baas/troubleshooting/http-error-codes#best-practices-to-avoid-429-errors)
  - [Other Troubleshooting for 429 Errors](https://docs.browserless.io/baas/troubleshooting/http-error-codes#other-troubleshooting-for-429-errors)