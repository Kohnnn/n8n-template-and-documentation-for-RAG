---
url: "https://docs.browserless.io/baas/session-management/recording-liveurl"
title: "Recording Sessions with LiveURL Integration | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/session-management/recording-liveurl#__docusaurus_skipToContent_fallback)

Version: v2

On this page

This guide demonstrates how to use Browserless's recording capabilities alongside LiveURL for interactive sessions. This combination is particularly useful when you need to:

- Record user interactions for training or debugging
- Provide a live interactive experience while capturing the session
- Monitor login processes with visual feedback
- Create documentation with recorded sessions
- Debug complex user flows with visual playback

## Prerequisites [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#prerequisites "Direct link to Prerequisites")

Before running this script, make sure you have:

1. Node.js installed on your system
2. A browserless API key
3. The required npm packages:







```codeBlockLines_p187
npm install puppeteer-core

```


## Complete Example [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#complete-example "Direct link to Complete Example")

Here's a complete example that shows how to:

1. Connect to Browserless with recording enabled
2. Generate a LiveURL for user interaction
3. Monitor for successful login with visual feedback
4. Save the recording for later playback

```codeBlockLines_p187
import puppeteer from 'puppeteer-core';
import fs from "fs";

// Utility function to create a delay
const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

// Configure browserless.io connection parameters
const queryParams = new URLSearchParams({
  token: "YOUR-API-KEY",
  timeout: 180000,
  headless: true,
}).toString();

// Main automation function
(async() => {
  let browser = null;

  try {
    // Connect to browserless.io with recording enabled
    browser = await puppeteer.connect({
      browserWSEndpoint: `wss://production-sfo.browserless.io?record=true&${queryParams}`,
    });
    console.log('Connected to browserless.io');

    // Create a new page and navigate to the login form
    const page = await browser.newPage();
    await page.goto('https://practicetestautomation.com/practice-test-login/', {
      waitUntil: 'networkidle2'
    });
    console.log('Navigated to login page');

    // Set up CDP session for browserless features
    const cdp = await page.createCDPSession();

    // Start recording the session
    await cdp.send("Browserless.startRecording");

    // Generate live URL for user interaction
    const { liveURL } = await cdp.send('Browserless.liveURL', {
      timeout: 600_000
    });
    console.log('Click for live experience:', liveURL);

    // Monitor for successful login
    await page.waitForFunction(() => {
      // Check for success indicators in URL or page content
      const currentUrl = window.location.href;
      const isSuccess = currentUrl.includes('logged-in') ||
                       currentUrl.includes('dashboard') ||
                       document.querySelector('.post-login') !== null;

      if (isSuccess) {
        // Show success notification
        const notification = document.createElement('div');
        notification.style.cssText = `
          position: fixed;
          top: 20px;
          left: 50%;
          transform: translateX(-50%);
          background-color: #4CAF50;
          color: white;
          padding: 15px 30px;
          border-radius: 5px;
          z-index: 9999;
          font-family: Arial, sans-serif;
          box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        `;
        notification.textContent = 'You can safely close the tab, login was successful.';
        document.body.appendChild(notification);
        return true;
      }
      return false;
    }, { timeout: 60000 }); // Wait up to 60 seconds for successful login

    // Wait for user to close the live URL
    await new Promise((r) => cdp.on('Browserless.liveComplete', r));
    console.log(`Live URL closed on page: ${page.url()}`);
    console.log('You can now continue automation on this site.');

    // Stop recording and save the recording
    const response = await cdp.send("Browserless.stopRecording");
    const file = Buffer.from(response.value, "binary");
    await fs.promises.writeFile("./record.webm", file);
    console.log('Recording saved as record.webm');

  } catch (error) {
    // Log any errors that occur during execution
    console.error('An error occurred:', error);
  } finally {
    // Ensure browser is always closed, even if an error occurs
    if (browser) {
      try {
        await browser.close();
        console.log('Browser closed successfully');
      } catch (closeError) {
        console.error('Error closing browser:', closeError);
      }
    }
  }
})().catch((e) => {
  console.error('Fatal error:', e);
  process.exit(1);
});

```

## Understanding the Code [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#understanding-the-code "Direct link to Understanding the Code")

### 1\. Initial Setup [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#1-initial-setup "Direct link to 1. Initial Setup")

- The script uses environment variables for secure API key storage
- It configures a 3-minute timeout for the browser session
- The `queryParams` object contains all necessary parameters for the Browserless connection

### 2\. Browser Connection [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#2-browser-connection "Direct link to 2. Browser Connection")

- Connects to Browserless with recording enabled via the `record=true` parameter
- Creates a new page and navigates to the target login form
- Sets up a CDP session for advanced browser control

### 3\. Recording and LiveURL Integration [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#3-recording-and-liveurl-integration "Direct link to 3. Recording and LiveURL Integration")

- Starts the recording session using `Browserless.startRecording`
- Generates a LiveURL with a 10-minute timeout
- This URL allows users to interact with the page while being recorded

### 4\. Login Monitoring [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#4-login-monitoring "Direct link to 4. Login Monitoring")

- Uses `waitForFunction` to monitor for successful login indicators
- Adds a visual notification when login is successful
- Waits for the user to close the LiveURL before proceeding

### 5\. Recording Management [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#5-recording-management "Direct link to 5. Recording Management")

- Stops the recording when the session is complete
- Saves the recording as a WebM file for later playback
- Ensures proper cleanup of browser resources

note

All recordings are saved in WebM format, which provides efficient compression while maintaining quality. This format is compatible with most modern browsers and video players.

## Best Practices [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#best-practices "Direct link to Best Practices")

### 1\. Error Handling [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#1-error-handling "Direct link to 1. Error Handling")

- Always wrap the main execution in a try-catch block
- Use a finally block to ensure browser cleanup
- Log errors with meaningful messages

### 2\. Session Management [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#2-session-management "Direct link to 2. Session Management")

- Set appropriate timeouts for your use case
- Store your API key securely
- Monitor the LiveURL for debugging

### 3\. Recording Optimization [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#3-recording-optimization "Direct link to 3. Recording Optimization")

- Start recording only when needed to reduce file size
- Consider recording quality settings for different use cases
- Save recordings with meaningful names and timestamps

## Common Use Cases [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#common-use-cases "Direct link to Common Use Cases")

### 1\. User Training [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#1-user-training "Direct link to 1. User Training")

- Record user interactions for training materials
- Create step-by-step guides with visual demonstrations
- Document complex workflows for team reference

### 2\. Debugging and Support [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#2-debugging-and-support "Direct link to 2. Debugging and Support")

- Capture user-reported issues for troubleshooting
- Record session replays for bug reports
- Provide visual context for support tickets

### 3\. Quality Assurance [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#3-quality-assurance "Direct link to 3. Quality Assurance")

- Record test sessions for regression testing
- Document expected behavior for new features
- Create visual test cases for team review

## Advanced Techniques [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#advanced-techniques "Direct link to Advanced Techniques")

### 1\. Custom Recording Triggers [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#1-custom-recording-triggers "Direct link to 1. Custom Recording Triggers")

```codeBlockLines_p187
// Start recording only after specific conditions are met
await page.waitForSelector('.login-form');
await cdp.send("Browserless.startRecording");

```

### 2\. Audio Recording [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#2-audio-recording "Direct link to 2. Audio Recording")

```codeBlockLines_p187
// Audio is automatically captured with the recording
// No additional configuration is needed
await cdp.send("Browserless.startRecording");

```

### 3\. Conditional Recording [​](https://docs.browserless.io/baas/session-management/recording-liveurl\#3-conditional-recording "Direct link to 3. Conditional Recording")

```codeBlockLines_p187
// Only record if a specific element is present
const hasLoginForm = await page.$('.login-form');
if (hasLoginForm) {
  await cdp.send("Browserless.startRecording");
}

```

- [Prerequisites](https://docs.browserless.io/baas/session-management/recording-liveurl#prerequisites)
- [Complete Example](https://docs.browserless.io/baas/session-management/recording-liveurl#complete-example)
- [Understanding the Code](https://docs.browserless.io/baas/session-management/recording-liveurl#understanding-the-code)
  - [1\. Initial Setup](https://docs.browserless.io/baas/session-management/recording-liveurl#1-initial-setup)
  - [2\. Browser Connection](https://docs.browserless.io/baas/session-management/recording-liveurl#2-browser-connection)
  - [3\. Recording and LiveURL Integration](https://docs.browserless.io/baas/session-management/recording-liveurl#3-recording-and-liveurl-integration)
  - [4\. Login Monitoring](https://docs.browserless.io/baas/session-management/recording-liveurl#4-login-monitoring)
  - [5\. Recording Management](https://docs.browserless.io/baas/session-management/recording-liveurl#5-recording-management)
- [Best Practices](https://docs.browserless.io/baas/session-management/recording-liveurl#best-practices)
  - [1\. Error Handling](https://docs.browserless.io/baas/session-management/recording-liveurl#1-error-handling)
  - [2\. Session Management](https://docs.browserless.io/baas/session-management/recording-liveurl#2-session-management)
  - [3\. Recording Optimization](https://docs.browserless.io/baas/session-management/recording-liveurl#3-recording-optimization)
- [Common Use Cases](https://docs.browserless.io/baas/session-management/recording-liveurl#common-use-cases)
  - [1\. User Training](https://docs.browserless.io/baas/session-management/recording-liveurl#1-user-training)
  - [2\. Debugging and Support](https://docs.browserless.io/baas/session-management/recording-liveurl#2-debugging-and-support)
  - [3\. Quality Assurance](https://docs.browserless.io/baas/session-management/recording-liveurl#3-quality-assurance)
- [Advanced Techniques](https://docs.browserless.io/baas/session-management/recording-liveurl#advanced-techniques)
  - [1\. Custom Recording Triggers](https://docs.browserless.io/baas/session-management/recording-liveurl#1-custom-recording-triggers)
  - [2\. Audio Recording](https://docs.browserless.io/baas/session-management/recording-liveurl#2-audio-recording)
  - [3\. Conditional Recording](https://docs.browserless.io/baas/session-management/recording-liveurl#3-conditional-recording)