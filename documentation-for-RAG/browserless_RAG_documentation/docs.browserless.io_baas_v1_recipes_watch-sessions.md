---
url: "https://docs.browserless.io/baas/v1/recipes/watch-sessions"
title: "Watching your sessions | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/recipes/watch-sessions#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/enterprise/watching-sessions) or [BrowserQL](https://docs.browserless.io/browserql/start).

Both the browserless docker image, and Dedicated hosted plans, have the ability to watch sessions as they run. As with most of our APIs and features, they're strongly geared towards engineers building on top of browserless. It's with these engineers in mind that we've written this document on how to watch your sessions as you work, broken up into three different methods.

1. [Watching sessions on the docker image](https://docs.browserless.io/baas/v1/recipes/watch-sessions#watching-sessions-on-the-docker-image)
2. [Using the Sessions tab in the Dedicated plans](https://docs.browserless.io/baas/v1/recipes/watch-sessions#using-the-sessions-tab-in-the-dedicated-plans)
3. Programmatically watching your sessions on Dedicated plans

## Watching sessions on the docker image [​](https://docs.browserless.io/baas/v1/recipes/watch-sessions\#watching-sessions-on-the-docker-image "Direct link to Watching sessions on the docker image")

To use the session viewer on the docker image, you don't need to do anything special in your code or how you connect to browserless. The only change you might make is add a `trackingId` to your connect call in order to sort or filter sessions to the one you care about.

In any case, the first step is to start the container as usual:

```codeBlockLines_p187
$ docker run --name browserless --rm -p 3000:3000 browserless/chrome:latest

```

Then, in your application or script connect to it.

```codeBlockLines_p187
const puppeteer = require('puppeteer');

(async () => {
  let browser = null;

  try {
    // If your script executes too quickly, you can add a ?pause query parameter
    // to the connect call to pause the script from running until you're watching it
    browser = await puppeteer.connect({
      browserWSEndpoint: `ws://localhost:3000`,
    });
    const page = await browser.newPage();
    await page.goto('https://example.com/');
  } catch (error) {
    console.log(error);
  } finally {
    browser && browser.close();
  }
})();

```

In your browser, you can visit [http://localhost:3000](http://localhost:3000/), click on the Settings icon in the top left, and click the link for the session:

If your session is immediately closing, then you can keep it open by _not_ calling browser.close at the end (just remember to terminate your script with CTRL+C or similar).

## Using the Sessions tab in the Dedicated plans [​](https://docs.browserless.io/baas/v1/recipes/watch-sessions\#using-the-sessions-tab-in-the-dedicated-plans "Direct link to Using the Sessions tab in the Dedicated plans")

In Dedicated plans, you can see your active sessions at any time by going to the Sessions portion of the account page.

Pressing the "Fetch Running Sessions" button will retrieve actively running sessions across all your workers, and show them here. The "Debugger" Link will then open up the page that you can run and view these sessions.

Anytime you connect, you can immediately see the results here after pushing the "Fetch Running Sessions" button.

## Programmatically watching your sessions on Dedicated plans [​](https://docs.browserless.io/baas/v1/recipes/watch-sessions\#programmatically-watching-your-sessions-on-dedicated-plans "Direct link to Programmatically watching your sessions on Dedicated plans")

Thanks to our powerful GraphQL API, you can programmatically retrieve your running sessions with a simple GraphQL API call. This simple feature allows you to build powerful integrations against browserless: end-users are able to witness their automation running, engineers can debug live production issues, and you can more easily pinpoint problems in your scripts.

When setting this up, you'll want to ensure that you don't accidentally expose your sessions to other users. It's for this reason that we've create a `trackingId`, which allows you to filter and more easily distinguish between running sessions.

For those that want to see the full example, see below. We'll break it down step-by-step afterwards.

**TL;DR the goods**

```codeBlockLines_p187
const puppeteer = require('puppeteer');
const fetch = require('node-fetch');
const apiToken = 'YOUR-API-TOKEN';
const trackingId = 'some-unique-id';

const getSessionsById = (trackingId) => {
  return fetch('https://api.browserless.io/graphql', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      query: `
        query getSessions($trackingId: String!, $apiToken: String!) {
          sessions(apiToken: $apiToken, trackingId: $trackingId) {
            description
            devtoolsFrontendUrl
            id
            title
            url
            trackingId
            browserId
            browserWSEndpoint
          }
        }
      `,
      variables: {
        trackingId,
        apiToken,
      },
    }),
  })
    .then((res) => res.json())
    .then((res) => res.data.sessions)
    .catch((error) => {
      console.log(`Error retrieving sessions ${error.message}`);
      return null;
    });
};

const run = async () => {
  const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

  let browser = null;

  try {
    browser = await puppeteer.connect({
      browserWSEndpoint: `wss://chrome.browserless.io?token=${apiToken}&trackingId=${trackingId}`,
    });

    const page = await browser.newPage();
    await page.goto('https://example.com');

    const [session] = await getSessionsById(trackingId);

    if (!session) {
      throw new Error(`Error retrieving session!`);
    }

    console.log(`Open: ${session.devtoolsFrontendUrl} in your browser!`);

    // Let the page stay open for 30 seconds so we can debug!
    await sleep(30000);
  } catch (error) {
    console.error(`Saw error when running: ${error.message}`);
  } finally {
    if (browser) {
      console.log(`Shutting down the browser.`);
      browser.close();
    }
  }
};

run();

```

### Selecting the modules to use [​](https://docs.browserless.io/baas/v1/recipes/watch-sessions\#selecting-the-modules-to-use "Direct link to Selecting the modules to use")

For this automated example, we're using the `puppeteer` module as well as the `node-fetch` package. Puppeteer is used for running the browser, and `node-fetch` for doing the API calls to browserless to get sessions.

You're free to use whatever modules you like, including Selenium or even axios, however we've found that puppeteer and node-fetch are the most common across the web.

Once done, let's setup the function to get sessions from the GraphQL endpoint!

### Fetching sessions [​](https://docs.browserless.io/baas/v1/recipes/watch-sessions\#fetching-sessions "Direct link to Fetching sessions")

Our function below takes a single argument: the trackingId we intend to use for the session. In a production system, you should _always_ make this ID unique as it'll prevent you from accidentally watching the wrong session. If you need a recommendation, we suggest something like a UUID or a GUID library.

```codeBlockLines_p187
const getSessionsById = (trackingId) => {
  return fetch('https://api.browserless.io/graphql', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      query: `
        query getSessions($trackingId: String!, $apiToken: String!) {
          sessions(apiToken: $apiToken, trackingId: $trackingId) {
            description
            devtoolsFrontendUrl
            id
            title
            url
            trackingId
            browserId
            browserWSEndpoint
          }
        }
      `,
      variables: {
        trackingId,
        apiToken,
      },
    });
  })
  .then((res) => res.json())
  .then((res) => res.data.sessions)
  .catch((error) => {
    console.log(`Error retrieving sessions ${error.message}`);
    return null;
  });
};

```

The below query is the underlying GraphQL request, that says we want to retrieve the following properties for our session. In our example we only make use of the `devtoolsFrontendUrl`, so you're free to remove the others if you wish, they're there for educational purposes.

```codeBlockLines_p187
query getSessions($trackingId: String!, $apiToken: String!) {
  sessions(apiToken: $apiToken, trackingId: $trackingId) {
    description
    devtoolsFrontendUrl
    id
    title
    url
    trackingId
    browserId
    browserWSEndpoint
  }
}

```

In GraphQL terms, we're setting up a "function" here that retrieves sessions with your API Token and trackingId. The response will contain something like:

```codeBlockLines_p187
{
  "data": {
    "sessions": [\
      {\
        "description": "",\
        "devtoolsFrontendUrl": "https://chrome.browserless.io/p/53616c7465645...",\
        "id": "CE39322DD6F46305A46FF92A0B41E4F2",\
        "title": "Example Site",\
        "url": "https://example.com",\
        "trackingId": "some-unique-id",\
        "browserId": "a69f18cf-23d9-4b5e-82c0-b817f2fd4e82",\
        "browserWSEndpoint": "wss://chrome.browserless.io/p/53616c7465645f5f325..."\
      }\
    ]
  }
}

```

> In all of our returned links we _omit_ your API token, so you'll need to add it to the link manually to visit it. This is done for security purposes.

**Hooking up puppeteer**

In our puppeteer setup, the `run` function, we start the browser and begin to write our script. Once we know the page is open, we use our GraphQL fetching function to get the active sessions (filtered by trackingId), and log the response.

In reality you can do whatever you'd like with this response: save it in a database or load it in a user's page. However, once the session is done the link will no longer respond properly, and the session will return a `404`.

Here's that code again:

```codeBlockLines_p187
const run = async () => {
  const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

  let browser = null;

  try {
    browser = await puppeteer.connect({
      browserWSEndpoint: `wss://chrome.browserless.io?token=${apiToken}&trackingId=${trackingId}`,
    });

    const page = await browser.newPage();
    await page.goto('https://example.com');

    const [session] = await getSessionsById(trackingId);

    if (!session) {
      throw new Error(`Error retrieving session!`);
    }

    console.log(
      `Open: ${session.devtoolsFrontendUrl} in your browser (be sure to add your &token to it!)`
    );

    // Let the page stay open for 30 seconds so we can debug!
    await sleep(30000);
  } catch (error) {
    console.error(`Saw error when running: ${error.message}`);
  } finally {
    if (browser) {
      console.log(`Shutting down the browser.`);
      browser.close();
    }
  }
};

```

You'll note that we have a `page.waitFor` call in here as well: this is to ensure you have time to visit the debugging page. In a production system, the page interactions can happen quickly, and so it's easy to go to a debug page and miss all of the interactivity. If it's crucial that you witness the script as it runs we recommend pausing the script on startup with the `&pause` query-string parameter in your `puppeteer.connect` call.

That's it! You've successfully setup a running puppeteer session, and have a way to view the session as needed! If you've found this helpful, or need help with an issue, please [let us know](https://www.browserless.io/contact)

- [Watching sessions on the docker image](https://docs.browserless.io/baas/v1/recipes/watch-sessions#watching-sessions-on-the-docker-image)
- [Using the Sessions tab in the Dedicated plans](https://docs.browserless.io/baas/v1/recipes/watch-sessions#using-the-sessions-tab-in-the-dedicated-plans)
- [Programmatically watching your sessions on Dedicated plans](https://docs.browserless.io/baas/v1/recipes/watch-sessions#programmatically-watching-your-sessions-on-dedicated-plans)
  - [Selecting the modules to use](https://docs.browserless.io/baas/v1/recipes/watch-sessions#selecting-the-modules-to-use)
  - [Fetching sessions](https://docs.browserless.io/baas/v1/recipes/watch-sessions#fetching-sessions)