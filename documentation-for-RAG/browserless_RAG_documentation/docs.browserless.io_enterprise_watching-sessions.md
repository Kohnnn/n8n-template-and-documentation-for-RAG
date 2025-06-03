---
url: "https://docs.browserless.io/enterprise/watching-sessions"
title: "Watching your sessions | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/watching-sessions#__docusaurus_skipToContent_fallback)

On this page

Both the Browserless docker image, and Dedicated hosted plans, have the ability to watch sessions as they run. As with most of our APIs and features, they're strongly geared towards engineers building on top of Browserless. It's with these engineers in mind that we've written this document on how to watch your sessions as you work, broken up into three different methods.

## Watching sessions on the docker image [​](https://docs.browserless.io/enterprise/watching-sessions\#watching-sessions-on-the-docker-image "Direct link to Watching sessions on the docker image")

To use the session viewer on the docker image, you don't need to do anything special in your code or how you connect to Browserless. The only change you might make is add a `id` to your connect call in order to sort or filter sessions to the one you care about.

In any case, the first step is to start the container as usual:

```codeBlockLines_p187
$ docker run --rm -p 3000:3000 ghcr.io/browserless/chrome

```

Then, in your application or script connect to it.

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer";

const browser = await puppeteer.connect({
  browserWSEndpoint: `wss://chrome.browserless.io?token=YOUR_API_TOKEN_HERE`,
});
const page = await browser.newPage();
await page.goto("https://example.com/");
await browser.close();

```

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import { chromium } from "playwright-core";

(async () => {
  const browser = await chromium.connectOverCDP(
    `wss://chrome.browserless.io?token=YOUR_API_TOKEN_HERE`
  );

  // Create a new context and page
  const context = browser.contexts()[0] || (await browser.newContext());
  const page = await context.newPage();

  // Navigate to the URL
  await page.goto("https://example.com/");
  console.log("Page loaded successfully");

  // Close the browser
  await browser.close();
})();

```

```codeBlockLines_p187
import asyncio
from playwright.async_api import async_playwright

WS_ENDPOINT = "wss://chrome.browserless.io?token=YOUR_API_TOKEN_HERE"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(WS_ENDPOINT)

        # Use existing context or create a new one
        context = browser.contexts[0] if browser.contexts else await browser.new_context()
        page = await context.new_page()

        await page.goto("https://example.com/")
        print("Page loaded successfully")

        await browser.close()

asyncio.run(main())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;

public class PlaywrightRemoteBrowser {
    public static void main(String[] args) {
        String wsEndpoint = "wss://chrome.browserless.io?token=YOUR_API_TOKEN_HERE";

        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(wsEndpoint);

            // Use existing context or create a new one
            BrowserContext context = browser.contexts().isEmpty()
                ? browser.newContext()
                : browser.contexts().get(0);

            Page page = context.newPage();

            page.navigate("https://example.com/");
            System.out.println("Page loaded successfully");

            browser.close();
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.Threading.Tasks;
using Microsoft.Playwright;

class Program
{
    static async Task Main(string[] args)
    {
        string wsEndpoint = "wss://chrome.browserless.io?token=YOUR_API_TOKEN_HERE";

        var playwright = await Playwright.CreateAsync();
        var browser = await playwright.Chromium.ConnectOverCDPAsync(wsEndpoint);

        // Use existing context or create a new one
        var context = browser.Contexts.Count > 0
            ? browser.Contexts[0]
            : await browser.NewContextAsync();

        var page = await context.NewPageAsync();

        await page.GotoAsync("https://example.com/");
        Console.WriteLine("Page loaded successfully");

        await browser.CloseAsync();
    }
}

```

In your browser, you can go to [http://localhost:3000/sessions](http://localhost:3000/sessions) to get a JSON of the running sessions.

info

If your session is immediately closing, then you can keep it open by _not_ calling `browser.close` at the end (just remember to terminate your script with CTRL+C or similar).

## Using the Sessions tab in the Dedicated plans [​](https://docs.browserless.io/enterprise/watching-sessions\#using-the-sessions-tab-in-the-dedicated-plans "Direct link to Using the Sessions tab in the Dedicated plans")

In Dedicated plans, you can see your active sessions at any time by going to the Sessions portion of the account page.

Pressing the "Fetch Running Sessions" button will retrieve actively running sessions across all your workers, and show them here. The "Debugger" Link will then open up the page that you can run and view these sessions.

Anytime you connect, you can immediately see the results here after pushing the "Fetch Running Sessions" button.

## Programmatically watching your sessions on Dedicated plans [​](https://docs.browserless.io/enterprise/watching-sessions\#programmatically-watching-your-sessions-on-dedicated-plans "Direct link to Programmatically watching your sessions on Dedicated plans")

Thanks to our powerful GraphQL API, you can programmatically retrieve your running sessions with a simple GraphQL API call. This simple feature allows you to build powerful integrations against browserless: end-users are able to witness their automation running, engineers can debug live production issues, and you can more easily pinpoint problems in your scripts.

When setting this up, you'll want to ensure that you don't accidentally expose your sessions to other users. It's for this reason that we've create a `id`, which allows you to filter and more easily distinguish between running sessions.

For those that want to see the full example, see below. We'll break it down step-by-step afterwards.

**TL;DR the goods**

- Puppeteer
- Playwright

```codeBlockLines_p187
import puppeteer from "puppeteer";

const apiToken = "YOUR_API_TOKEN_HERE";
const id = "some-unique-id";

const getSessionsById = (id) => {
  return fetch("https://api.browserless.io/graphql", {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({
      query: `
        query getSessions($id: String!, $apiToken: String!) {
          sessions(apiToken: $apiToken, id: $id) {
            description
            devtoolsFrontendUrl
            id
            title
            url
            id
            browserId
            browserWSEndpoint
          }
        }
      `,
      variables: {
        id,
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
      browserWSEndpoint: `wss://chrome.browserless.io?token=${apiToken}&id=${id}`,
    });

    const page = await browser.newPage();
    await page.goto("https://example.com");

    const [session] = await getSessionsById(id);

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

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
import { chromium } from "playwright-core";

const apiToken = "YOUR_API_TOKEN_HERE";
const id = "some-unique-id";

const getSessionsById = async (id) => {
  try {
    const response = await fetch("https://api.browserless.io/graphql", {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({
        query: `
          query getSessions($id: String!, $apiToken: String!) {
            sessions(apiToken: $apiToken, id: $id) {
              description
              devtoolsFrontendUrl
              id
              title
              url
              id
              browserId
              browserWSEndpoint
            }
          }
        `,
        variables: {
          id,
          apiToken,
        },
      }),
    });
    const result = await response.json();
    return result.data.sessions;
  } catch (error) {
    console.error(`Error retrieving sessions: ${error.message}`);
    return null;
  }
};

const run = async () => {
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  let browser = null;

  try {
    browser = await chromium.connectOverCDP(
      `wss://chrome.browserless.io?token=${apiToken}&id=${id}`
    );

    const context = browser.contexts()[0] || (await browser.newContext());
    const page = await context.newPage();
    await page.goto("https://example.com");

    const [session] = await getSessionsById(id);

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
      await browser.close();
    }
  }
};

run();

```

```codeBlockLines_p187
import asyncio
import requests
from playwright.async_api import async_playwright

API_TOKEN = "YOUR_API_TOKEN_HERE"
ID = "some-unique-id"

def get_sessions_by_id(session_id):
    try:
        response = requests.post(
            "https://api.browserless.io/graphql",
            json={
                "query": """
                    query getSessions($id: String!, $apiToken: String!) {
                        sessions(apiToken: $apiToken, id: $id) {
                            description
                            devtoolsFrontendUrl
                            id
                            title
                            url
                            browserId
                            browserWSEndpoint
                        }
                    }
                """,
                "variables": {
                    "id": session_id,
                    "apiToken": API_TOKEN,
                },
            },
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()
        return response.json()["data"]["sessions"]
    except Exception as e:
        print(f"Error retrieving sessions: {e}")
        return None

async def run():
    async with async_playwright() as p:
        browser = None
        try:
            browser = await p.chromium.connect_over_cdp(
                f"wss://chrome.browserless.io?token={API_TOKEN}&id={ID}"
            )

            context = browser.contexts[0] if browser.contexts else await browser.new_context()
            page = await context.new_page()
            await page.goto("https://example.com")

            sessions = get_sessions_by_id(ID)
            if not sessions:
                raise Exception("Error retrieving session!")

            session = sessions[0]
            print(f"Open: {session['devtoolsFrontendUrl']} in your browser!")

            # Let the page stay open for 30 seconds
            await asyncio.sleep(30)
        except Exception as e:
            print(f"Saw error when running: {e}")
        finally:
            if browser:
                print("Shutting down the browser.")
                await browser.close()

asyncio.run(run())

```

```codeBlockLines_p187
import com.microsoft.playwright.*;
import java.net.http.*;
import java.net.URI;
import java.net.http.HttpClient;
import java.util.*;

import com.google.gson.Gson;

public class PlaywrightRemote {
    private static final String API_TOKEN = "YOUR_API_TOKEN_HERE";
    private static final String ID = "some-unique-id";

    private static List<Map<String, Object>> getSessionsById(String id) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        String query = """
            query getSessions($id: String!, $apiToken: String!) {
                sessions(apiToken: $apiToken, id: $id) {
                    description
                    devtoolsFrontendUrl
                    id
                    title
                    url
                    browserId
                    browserWSEndpoint
                }
            }
        """;

        Map<String, Object> payload = Map.of(
            "query", query,
            "variables", Map.of("id", id, "apiToken", API_TOKEN)
        );

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://api.browserless.io/graphql"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(new Gson().toJson(payload)))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() != 200) {
            throw new Exception("Error retrieving sessions: " + response.body());
        }

        Map<String, Object> responseData = new Gson().fromJson(response.body(), Map.class);
        return (List<Map<String, Object>>) ((Map<String, Object>) responseData.get("data")).get("sessions");
    }

    public static void main(String[] args) {
        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(
                "wss://chrome.browserless.io?token=" + API_TOKEN + "&id=" + ID
            );

            BrowserContext context = browser.contexts().isEmpty() ? browser.newContext() : browser.contexts().get(0);
            Page page = context.newPage();
            page.navigate("https://example.com");

            List<Map<String, Object>> sessions = getSessionsById(ID);
            if (sessions.isEmpty()) {
                throw new Exception("Error retrieving session!");
            }

            Map<String, Object> session = sessions.get(0);
            System.out.println("Open: " + session.get("devtoolsFrontendUrl") + " in your browser!");

            Thread.sleep(30000);
            browser.close();
        } catch (Exception e) {
            System.err.println("Saw error when running: " + e.getMessage());
        }
    }
}

```

```codeBlockLines_p187
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using Microsoft.Playwright;

class Program
{
    private const string ApiToken = "YOUR_API_TOKEN_HERE";
    private const string Id = "some-unique-id";

    static async Task Main(string[] args)
    {
        var httpClient = new HttpClient();
        var playwright = await Playwright.CreateAsync();
        IBrowser browser = null;

        try
        {
            browser = await playwright.Chromium.ConnectOverCDPAsync(
                $"wss://chrome.browserless.io?token={ApiToken}&id={Id}"
            );

            var context = browser.Contexts.Count > 0 ? browser.Contexts[0] : await browser.NewContextAsync();
            var page = await context.NewPageAsync();
            await page.GotoAsync("https://example.com");

            var payload = new
            {
                query = @"
                    query getSessions($id: String!, $apiToken: String!) {
                        sessions(apiToken: $apiToken, id: $id) {
                            description
                            devtoolsFrontendUrl
                            id
                            title
                            url
                            browserId
                            browserWSEndpoint
                        }
                    }
                ",
                variables = new { id = Id, apiToken = ApiToken }
            };

            var response = await httpClient.PostAsync(
                "https://api.browserless.io/graphql",
                new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json")
            );

            response.EnsureSuccessStatusCode();
            var responseData = JsonSerializer.Deserialize<JsonElement>(await response.Content.ReadAsStringAsync());
            var sessions = responseData.GetProperty("data").GetProperty("sessions").EnumerateArray();

            if (!sessions.MoveNext())
            {
                throw new Exception("Error retrieving session!");
            }

            var session = sessions.Current;
            Console.WriteLine($"Open: {session.GetProperty("devtoolsFrontendUrl").GetString()} in your browser!");

            await Task.Delay(30000);
        }
        catch (Exception e)
        {
            Console.WriteLine($"Saw error when running: {e.Message}");
        }
        finally
        {
            if (browser != null)
            {
                Console.WriteLine("Shutting down the browser.");
                await browser.CloseAsync();
            }
        }
    }
}

```

### Selecting the modules to use [​](https://docs.browserless.io/enterprise/watching-sessions\#selecting-the-modules-to-use "Direct link to Selecting the modules to use")

For this automated example, we're using the `puppeteer` or `playwright`. These are used for running the browser.

You're free to use whatever modules you like, including Selenium, however we've found that puppeteer and playwright are the most common across the web.

Once done, let's setup the function to get sessions from the GraphQL endpoint!

### Fetching sessions [​](https://docs.browserless.io/enterprise/watching-sessions\#fetching-sessions "Direct link to Fetching sessions")

Our function below takes a single argument: the id we intend to use for the session. In a production system, you should _always_ make this ID unique as it'll prevent you from accidentally watching the wrong session. If you need a recommendation, we suggest something like a UUID or a GUID library.

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
const getSessionsById = (id) => {
  return fetch('https://api.browserless.io/graphql', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      query: `
        query getSessions($id: String!, $apiToken: String!) {
          sessions(apiToken: $apiToken, id: $id) {
            description
            devtoolsFrontendUrl
            id
            title
            url
            id
            browserId
            browserWSEndpoint
          }
        }
      `,
      variables: {
        id,
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

```codeBlockLines_p187
  import requests

  def get_sessions_by_id(session_id, api_token):
      try:
          response = requests.post(
              "https://api.browserless.io/graphql",
              json={
                  "query": """
                      query getSessions($id: String!, $apiToken: String!) {
                          sessions(apiToken: $apiToken, id: $id) {
                              description
                              devtoolsFrontendUrl
                              id
                              title
                              url
                              browserId
                              browserWSEndpoint
                          }
                      }
                  """,
                  "variables": {"id": session_id, "apiToken": api_token},
              },
              headers={"Content-Type": "application/json"},
          )

          response.raise_for_status()
          return response.json()["data"]["sessions"]
      except Exception as e:
          print(f"Error retrieving sessions: {e}")
          return None

  # Example Usage
  api_token = "YOUR_API_TOKEN_HERE"
  session_id = "some-unique-id"
  sessions = get_sessions_by_id(session_id, api_token)
  print(sessions)

```

```codeBlockLines_p187
import com.google.gson.*;
import java.net.http.*;
import java.net.URI;
import java.util.*;

public class GraphQLFetcher {
    public static List<Map<String, Object>> getSessionsById(String id, String apiToken) {
        try {
            HttpClient client = HttpClient.newHttpClient();

            String query = """
                query getSessions($id: String!, $apiToken: String!) {
                    sessions(apiToken: $apiToken, id: $id) {
                        description
                        devtoolsFrontendUrl
                        id
                        title
                        url
                        browserId
                        browserWSEndpoint
                    }
                }
            """;

            Map<String, Object> payload = Map.of(
                "query", query,
                "variables", Map.of("id", id, "apiToken", apiToken)
            );

            String requestBody = new Gson().toJson(payload);

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.browserless.io/graphql"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            if (response.statusCode() == 200) {
                JsonObject data = JsonParser.parseString(response.body())
                    .getAsJsonObject()
                    .getAsJsonObject("data");

                return new Gson().fromJson(data.getAsJsonArray("sessions"), List.class);
            } else {
                System.err.println("Failed to fetch sessions: " + response.body());
                return null;
            }
        } catch (Exception e) {
            System.err.println("Error retrieving sessions: " + e.getMessage());
            return null;
        }
    }

    public static void main(String[] args) {
        String apiToken = "YOUR_API_TOKEN_HERE";
        String id = "some-unique-id";
        List<Map<String, Object>> sessions = getSessionsById(id, apiToken);
        System.out.println(sessions);
    }
}

```

```codeBlockLines_p187
using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        string apiToken = "YOUR_API_TOKEN_HERE";
        string id = "some-unique-id";

        var sessions = await GetSessionsById(id, apiToken);
        Console.WriteLine(JsonSerializer.Serialize(sessions, new JsonSerializerOptions { WriteIndented = true }));
    }

    static async Task<object> GetSessionsById(string id, string apiToken)
    {
        using var httpClient = new HttpClient();
        var payload = new
        {
            query = @"
                query getSessions($id: String!, $apiToken: String!) {
                    sessions(apiToken: $apiToken, id: $id) {
                        description
                        devtoolsFrontendUrl
                        id
                        title
                        url
                        browserId
                        browserWSEndpoint
                    }
                }
            ",
            variables = new { id, apiToken }
        };

        var content = new StringContent(
            JsonSerializer.Serialize(payload),
            Encoding.UTF8,
            "application/json"
        );

        try
        {
            var response = await httpClient.PostAsync("https://api.browserless.io/graphql", content);
            response.EnsureSuccessStatusCode();

            var responseBody = await response.Content.ReadAsStringAsync();
            var json = JsonSerializer.Deserialize<JsonElement>(responseBody);

            return json.GetProperty("data").GetProperty("sessions");
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error retrieving sessions: {e.Message}");
            return null;
        }
    }
}

```

The below query is the underlying GraphQL request, that says we want to retrieve the following properties for our session. In our example we only make use of the `devtoolsFrontendUrl`, so you're free to remove the others if you wish, they're there for educational purposes.

```codeBlockLines_p187
query getSessions($id: String!, $apiToken: String!) {
  sessions(apiToken: $apiToken, id: $id) {
    description
    devtoolsFrontendUrl
    id
    title
    url
    id
    browserId
    browserWSEndpoint
  }
}

```

In GraphQL terms, we're setting up a "function" here that retrieves sessions with your API Token and id. The response will contain something like:

```codeBlockLines_p187
{
  "data": {
    "sessions": [\
      {\
        "id": null,\
        "initialConnectURL": "wss://chrome.browserless.io/firefox/playwright/?token=YOUR_API_TOKEN_HERE",\
        "isTempDataDir": true,\
        "launchOptions": {},\
        "numbConnected": 1,\
        "routePath": ["/firefox/playwright", "/firefox/playwright"],\
        // ...\
      }\
    ]
  }
}

```

> In all of our returned links we _omit_ your API token, so you'll need to add it to the link manually to visit it. This is done for security purposes.

**Hooking up puppeteer/playwright**

In our puppeteer or playwright setups, the `run` function, we start the browser and begin to write our script. Once we know the page is open, we use our GraphQL fetching function to get the active sessions (filtered by id), and log the response.

In reality you can do whatever you'd like with this response: save it in a database or load it in a user's page. However, once the session is done the link will no longer respond properly, and the session will return a `404`.

Here's that code again:

- Puppeteer
- Playwright

```codeBlockLines_p187
const run = async () => {
  const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

  let browser = null;

  try {
    browser = await puppeteer.connect({
      browserWSEndpoint: `wss://chrome.browserless.io?token=${apiToken}&id=${id}`,
    });

    const page = await browser.newPage();
    await page.goto("https://example.com");

    const [session] = await getSessionsById(id);

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

- Javascript
- Python
- Java
- C#

```codeBlockLines_p187
const run = async () => {
  const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

  let browser = null;

  try {
    browser = await chromium.connectOverCDP(
      `wss://chrome.browserless.io?token=${apiToken}&id=${id}`
    );

    const context = browser.contexts()[0] || (await browser.newContext());
    const page = await context.newPage();
    await page.goto("https://example.com");

    const [session] = await getSessionsById(id);

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
      await browser.close();
    }
  }
};

run();

```

```codeBlockLines_p187
async def run():
    async with async_playwright() as p:
        browser = None
        try:
            browser = await p.chromium.connect_over_cdp(
                f"wss://chrome.browserless.io?token={API_TOKEN}&id={ID}"
            )

            context = browser.contexts[0] if browser.contexts else await browser.new_context()
            page = await context.new_page()
            await page.goto("https://example.com")

            sessions = get_sessions_by_id(ID)
            if not sessions:
                raise Exception("Error retrieving session!")

            session = sessions[0]
            print(f"Open: {session['devtoolsFrontendUrl']} in your browser!")

            # Let the page stay open for 30 seconds
            await asyncio.sleep(30)
        except Exception as e:
            print(f"Saw error when running: {e}")
        finally:
            if browser:
                print("Shutting down the browser.")
                await browser.close()

asyncio.run(run())

```

```codeBlockLines_p187
public class PlaywrightRunExample {
    public static void run(String apiToken, String id, SessionFetcher fetcher) {
        try (Playwright playwright = Playwright.create()) {
            Browser browser = playwright.chromium().connectOverCDP(
                "wss://chrome.browserless.io?token=" + apiToken + "&id=" + id
            );

            BrowserContext context = browser.contexts().isEmpty()
                ? browser.newContext()
                : browser.contexts().get(0);
            Page page = context.newPage();

            page.navigate("https://example.com");

            List<Map<String, Object>> sessions = fetcher.getSessionsById(id);
            if (sessions.isEmpty()) {
                throw new Exception("Error retrieving session!");
            }

            Map<String, Object> session = sessions.get(0);
            System.out.println(
                "Open: " + session.get("devtoolsFrontendUrl") + " in your browser (be sure to add your &token to it!)"
            );

            // Let the page stay open for 30 seconds
            TimeUnit.SECONDS.sleep(30);
        } catch (Exception e) {
            System.err.println("Saw error when running: " + e.getMessage());
        }
    }

    interface SessionFetcher {
        List<Map<String, Object>> getSessionsById(String id);
    }
}

```

```codeBlockLines_p187
class Program
{
    static async Task Run(string apiToken, string id, Func<string, Task<List<Dictionary<string, string>>>> getSessionsById)
    {
        IBrowser browser = null;

        try
        {
            var playwright = await Playwright.CreateAsync();
            browser = await playwright.Chromium.ConnectOverCDPAsync(
                $"wss://chrome.browserless.io?token={apiToken}&id={id}"
            );

            var context = browser.Contexts.Count > 0 ? browser.Contexts[0] : await browser.NewContextAsync();
            var page = await context.NewPageAsync();
            await page.GotoAsync("https://example.com");

            var sessions = await getSessionsById(id);
            if (sessions.Count == 0)
            {
                throw new Exception("Error retrieving session!");
            }

            var session = sessions[0];
            Console.WriteLine(
                $"Open: {session["devtoolsFrontendUrl"]} in your browser (be sure to add your &token to it!)"
            );

            // Let the page stay open for 30 seconds
            await Task.Delay(30000);
        }
        catch (Exception e)
        {
            Console.WriteLine($"Saw error when running: {e.Message}");
        }
        finally
        {
            if (browser != null)
            {
                Console.WriteLine("Shutting down the browser.");
                await browser.CloseAsync();
            }
        }
    }
}

```

You'll note that we have a `page.waitFor` call in here as well: this is to ensure you have time to visit the debugging page. In a production system, the page interactions can happen quickly, and so it's easy to go to a debug page and miss all of the interactivity. If it's crucial that you witness the script as it runs we recommend pausing the script on startup with the `&pause` query-string parameter in your `puppeteer.connect` call.

That's it! You've successfully setup a running puppeteer session, and have a way to view the session as needed! If you've found this helpful, or need help with an issue, please [let us know](https://www.browserless.io/contact)

- [Watching sessions on the docker image](https://docs.browserless.io/enterprise/watching-sessions#watching-sessions-on-the-docker-image)
- [Using the Sessions tab in the Dedicated plans](https://docs.browserless.io/enterprise/watching-sessions#using-the-sessions-tab-in-the-dedicated-plans)
- [Programmatically watching your sessions on Dedicated plans](https://docs.browserless.io/enterprise/watching-sessions#programmatically-watching-your-sessions-on-dedicated-plans)
  - [Selecting the modules to use](https://docs.browserless.io/enterprise/watching-sessions#selecting-the-modules-to-use)
  - [Fetching sessions](https://docs.browserless.io/enterprise/watching-sessions#fetching-sessions)