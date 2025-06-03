---
url: "https://docs.browserless.io/browserql/session-management/persisting-sessions"
title: "Persisting Sessions | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/session-management/persisting-sessions#__docusaurus_skipToContent_fallback)

On this page

## Persisting Browser Sessions with User Data Directory [​](https://docs.browserless.io/browserql/session-management/persisting-sessions\#persisting-browser-sessions-with-user-data-directory "Direct link to Persisting Browser Sessions with User Data Directory")

The `--user-data-dir` flag in browserless allows you to persist browser data such as cookies, localStorage, cache, and login sessions across multiple browser sessions. This is particularly useful for maintaining authenticated states and user preferences without having to re-authenticate or reconfigure settings each time.

note

The `--user-data-dir` feature is only available for Enterprise plans with dedicated fleets. It cannot be used with shared plans.

## Important details when implementing User Data Directories [​](https://docs.browserless.io/browserql/session-management/persisting-sessions\#important-details-when-implementing-user-data-directories "Direct link to Important details when implementing User Data Directories")

The directory will be created if it doesn't exist. When using `--user-data-dir`, make sure to use a unique directory path for each different browser profile you want to maintain. You can only instantiate one browser per userdatadir at a time, meaning it's 1-1 and you can't use the same path in the flag for multiple concurrent browsers.

### Pointing to a specific dedicated worker on Enterprise plans [​](https://docs.browserless.io/browserql/session-management/persisting-sessions\#pointing-to-a-specific-dedicated-worker-on-enterprise-plans "Direct link to Pointing to a specific dedicated worker on Enterprise plans")

User data directories are stored locally on each worker's file system and do not sync across your fleet. For example, a browser instance using `--user-data-dir=~/u/1` on Worker #1 will not be accessible from Worker #2. No need to worry! Browserless allows you to point at a specific worker by using the endpoint provided on your account page under "Production" Clusters. Click on the cell under the Address column to copy the endpoint for the worker you need. You'll want to keep track of which browser session was persisted initially on which worker to ensure consistent access.

- Your BQL endpoints would change from `https://chrome.browserless.io/bql` to something like `https://chrome.browserless.io/p/53616c7465645f5ff8cc738d5eecb3032823d67e37578fe4531b0f9a83dc80856c66d0fe36aba4d2f4bc5f01c18bdfab/bql?token=YOUR_API_TOKEN_HERE&--user-data-dir=~/custompath/123`

## Example: Persisting Dark Mode Preference with BrowserQL [​](https://docs.browserless.io/browserql/session-management/persisting-sessions\#example-persisting-dark-mode-preference-with-browserql "Direct link to Example: Persisting Dark Mode Preference with BrowserQL")

The following example demonstrates how to use the `--user-data-dir` flag with BrowserQL to persist browser state. This example shows how to toggle dark mode on w3schools.com - each time you run it, the initial state will be different since it's persisting the toggle state from previous runs.

```codeBlockLines_p187
const url = 'https://www.browserless.io/';
const token = 'YOUR_API_TOKEN_HERE'; //this script using userdatadir only works for dedicated machines
const timeout = 5 * 60 * 1000;
const launchArgs = {
  args: ['--user-data-dir=~/id-togle-test-123']
};
const queryParams = new URLSearchParams({
  timeout,
  token,
  launch: JSON.stringify(launchArgs)
}).toString();

const query = `
  mutation DarkModeToggle {
    goto(url: "https://www.w3schools.com/", waitUntil: domContentLoaded) {
      status
    }
    DarkModeClassBefore:evaluate(content: "document.body.className") {
      value
    }
    click(selector:"#tnb-dark-mode-toggle-btn"){
      time
    }
    DarkModeClassAfter:evaluate(content: "document.body.className") {
      value
    }
  }
`;

const variables = { url };

const endpoint =
  `https://chrome.browserless.io/chromium/bql?${queryParams}`;

const options = {
  method: 'POST',
  headers: {
    'content-type': 'application/json'
  },
  body: JSON.stringify({
    query,
  }),
};

try {
  console.log(`Running BQL Query: ${url}`);

  const response = await fetch(endpoint, options);

  if (!response.ok) {
    throw new Error(`Got non-ok response:\n` + (await response.text()));
  }

  const { data } = await response.json();

  console.log("Full response data:", JSON.stringify(data, null, 2));

  if (data && data.DarkModeClassBefore && data.DarkModeClassAfter) {
    console.log("Dark mode toggle results:");
    console.log("Before:", data.DarkModeClassBefore.value);
    console.log("After:", data.DarkModeClassAfter.value);
    console.log("Click time:", data.click.time, "ms");
  } else {
    console.log("Unexpected response structure:", data);
  }
} catch (error) {
  console.error(error);
}

```

This example demonstrates how to:

1. Configure a user data directory with the `--user-data-dir` flag
2. Navigate to a website
3. Check the current state (dark mode on/off)
4. Toggle the state
5. Verify the change

When you run this script multiple times, you'll notice that the initial state persists between runs, demonstrating that the browser session is being maintained.

- [Persisting Browser Sessions with User Data Directory](https://docs.browserless.io/browserql/session-management/persisting-sessions#persisting-browser-sessions-with-user-data-directory)
- [Important details when implementing User Data Directories](https://docs.browserless.io/browserql/session-management/persisting-sessions#important-details-when-implementing-user-data-directories)
  - [Pointing to a specific dedicated worker on Enterprise plans](https://docs.browserless.io/browserql/session-management/persisting-sessions#pointing-to-a-specific-dedicated-worker-on-enterprise-plans)
- [Example: Persisting Dark Mode Preference with BrowserQL](https://docs.browserless.io/browserql/session-management/persisting-sessions#example-persisting-dark-mode-preference-with-browserql)