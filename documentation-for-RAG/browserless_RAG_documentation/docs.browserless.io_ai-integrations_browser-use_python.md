---
url: "https://docs.browserless.io/ai-integrations/browser-use/python"
title: "Browser Use Integration | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/ai-integrations/browser-use/python#__docusaurus_skipToContent_fallback)

On this page

[Browser Use](https://github.com/browser-use/browser-use) is a Python library that allows AI agents to control a browser. By integrating Browserless with Browser Use, you can provide your AI applications with powerful web browsing capabilities without managing browser infrastructure.

## Prerequisites [​](https://docs.browserless.io/ai-integrations/browser-use/python\#prerequisites "Direct link to Prerequisites")

- Python 3.11 or higher
- An active Browserless API Token (available in your [account dashboard](https://account.browserless.io/))

## Step-by-Step Setup [​](https://docs.browserless.io/ai-integrations/browser-use/python\#step-by-step-setup "Direct link to Step-by-Step Setup")

**1\. Get your API Key**

Go to your [Browserless Account Dashboard](https://account.browserless.io/) and copy your API token.

Then set the `BROWSERLESS_API_TOKEN` environment variable in your `.env` file:

- .env file
- Command line

```codeBlockLines_p187
BROWSERLESS_API_TOKEN=your-token-here
ANTHROPIC_API_KEY=your-anthropic-key-here

```

```codeBlockLines_p187
export BROWSERLESS_API_TOKEN=your-token-here
export ANTHROPIC_API_KEY=your-anthropic-key-here

```

**2\. Create a virtual environment**

Set up a Python virtual environment to manage your dependencies:

- venv
- conda

```codeBlockLines_p187
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```

```codeBlockLines_p187
conda create -n browser-use-env python=3.10
conda activate browser-use-env

```

**3\. Install required packages**

Install Browser Use and other required packages:

- pip
- Poetry

```codeBlockLines_p187
pip install browser-use python-dotenv langchain-anthropic

```

```codeBlockLines_p187
poetry add browser-use python-dotenv langchain-anthropic

```

**4\. Create the browser\_session.py file**

Create a file named `browser_session.py` with the following complete code:

```codeBlockLines_p187
from typing import Optional
from browser_use.browser.context import BrowserSession, BrowserContext, BrowserContextConfig
from playwright.async_api import Page, BrowserContext as PlaywrightContext

class ExtendedBrowserSession(BrowserSession):
    """Extended version of BrowserSession that includes current_page"""
    def __init__(
        self,
        context: PlaywrightContext,
        cached_state: Optional[dict] = None,
        current_page: Optional[Page] = None
    ):
        super().__init__(context=context, cached_state=cached_state)
        self.current_page = current_page

class UseBrowserlessContext(BrowserContext):
    async def _initialize_session(self) -> ExtendedBrowserSession:
        """Initialize a browser session using existing Browserless page.

        Returns:
            ExtendedBrowserSession: The initialized browser session with current page.
        """
        playwright_browser = await self.browser.get_playwright_browser()
        context = await self._create_context(playwright_browser)
        self._add_new_page_listener(context)

        self.session = ExtendedBrowserSession(
            context=context,
            cached_state=None,
        )

        # Get existing page or create new one
        self.session.current_page = context.pages[0] if context.pages else await context.new_page()

        # Initialize session state
        self.session.cached_state = await self._update_state()

        return self.session

```

**5\. Create the main.py file**

Create a new file named `main.py` with the following complete code:

```codeBlockLines_p187
from dotenv import load_dotenv
import os
import asyncio
from browser_use import Browser, BrowserConfig, Agent
from browser_session import UseBrowserlessContext, ExtendedBrowserSession
from browser_use.browser.context import BrowserContextConfig
from langchain_anthropic import ChatAnthropic

async def setup_browser() -> tuple[Browser, UseBrowserlessContext]:
    """Set up browser and context configurations.

    Returns:
        tuple[Browser, UseBrowserlessContext]: Configured browser and context.
    """
    # Browserless connection URL with token (using CDP)
    browserless_url = f"wss://production-sfo.browserless.io?token={os.environ['BROWSERLESS_API_TOKEN']}&proxy=residential"

    browser = Browser(config=BrowserConfig(cdp_url=browserless_url))
    context = UseBrowserlessContext(
        browser,
        BrowserContextConfig(
            wait_for_network_idle_page_load_time=10.0,
            highlight_elements=True,
        )
    )

    return browser, context

async def setup_agent(browser: Browser, context: UseBrowserlessContext) -> Agent:
    """Set up the browser automation agent.

    Args:
        browser: Configured browser instance
        context: Browser context for the agent

    Returns:
        Agent: Configured automation agent
    """
    llm = ChatAnthropic(
        model_name="claude-3-5-sonnet-20240620",
        temperature=0.0,
        timeout=100,
    )

    return Agent(
        task="go to https://example.com, navigate the site and report what you found",
        llm=llm,
        browser=browser,
        browser_context=context,
    )

async def main():
    load_dotenv()

    browser, context = await setup_browser()
    print("Browser and context initialized")

    session = await context.get_session()
    print("Session obtained")

    try:
        agent = await setup_agent(browser, context)
        print("Agent configured, running now...")
        await agent.run()
    finally:
        # Close the browser
        print("Closing browser")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

```

**6\. Run your application**

Run your application with the following command:

```codeBlockLines_p187
python main.py

```

You should see output indicating that the browser is initialized and the agent is running.

## How It Works [​](https://docs.browserless.io/ai-integrations/browser-use/python\#how-it-works "Direct link to How It Works")

**1\. Connection Setup**: Browser Use connects to Browserless using the WebSocket endpoint with your API token
**2\. Agent Configuration**: The AI agent is configured with a task and a language model
**3\. Automation**: The agent uses the browser to navigate and interact with websites
**4\. LLM Integration**: The agent leverages an LLM (like Claude) to interpret web content and make decisions

## Additional Configuration [​](https://docs.browserless.io/ai-integrations/browser-use/python\#additional-configuration "Direct link to Additional Configuration")

### Proxy Support [​](https://docs.browserless.io/ai-integrations/browser-use/python\#proxy-support "Direct link to Proxy Support")

You can enable a residential proxy for improved website compatibility:

```codeBlockLines_p187
browserless_url = f"wss://production-sfo.browserless.io?token={os.environ['BROWSERLESS_API_TOKEN']}&proxy=residential"

```

### Context Configuration [​](https://docs.browserless.io/ai-integrations/browser-use/python\#context-configuration "Direct link to Context Configuration")

Customize the browser context with additional settings:

```codeBlockLines_p187
context = UseBrowserlessContext(
    browser,
    BrowserContextConfig(
        wait_for_network_idle_page_load_time=10.0,
        highlight_elements=True,
        # Additional configuration options
        user_agent="Custom User Agent",
        viewport_size={"width": 1920, "height": 1080},
        ignore_https_errors=True,
    )
)

```

## Advanced Features [​](https://docs.browserless.io/ai-integrations/browser-use/python\#advanced-features "Direct link to Advanced Features")

### CDP Events and LiveURL [​](https://docs.browserless.io/ai-integrations/browser-use/python\#cdp-events-and-liveurl "Direct link to CDP Events and LiveURL")

Browserless provides powerful Chrome DevTools Protocol (CDP) events that can enhance your browser automation. Here are some key features:

1. **LiveURL for User Interaction**







```codeBlockLines_p187
# Create a CDP session
cdp = await page.createCDPSession()

# Generate a LiveURL for user interaction
response = await cdp.send('Browserless.liveURL', {
       "timeout": 600000  # 10 minutes timeout
})
live_url = response["liveURL"]
print(f"Share this URL with users: {live_url}")

# Wait for user to complete interaction
future = asyncio.Future()
cdp.on('Browserless.liveComplete', lambda: future.set_result(True))
await future

```











For more details, see our [LiveURL Documentation](https://docs.browserless.io/baas/session-management/recording-liveurl).

2. **Captcha Detection**







```codeBlockLines_p187
# Listen for captcha detection
cdp.on('Browserless.captchaFound', lambda: print('Captcha detected!'))

# Solve captcha automatically
response = await cdp.send('Browserless.solveCaptcha', {
       "appearTimeout": 20000
})
solved, error = response.get("solved"), response.get("error")

```











Learn more about handling captchas in our [Hybrid Automation Guide](https://docs.browserless.io/baas/hybrid-automation).

3. **Session Recording**







```codeBlockLines_p187
# Start recording the session
await cdp.send("Browserless.startRecording")

# ... perform actions ...

# Stop recording and save
response = await cdp.send("Browserless.stopRecording")
with open("recording.webm", "wb") as f:
       f.write(response.value)

```











See our [Recording Documentation](https://docs.browserless.io/baas/session-management/recording-liveurl) for more details.


### Complete Example with CDP Events [​](https://docs.browserless.io/ai-integrations/browser-use/python\#complete-example-with-cdp-events "Direct link to Complete Example with CDP Events")

Here's a complete example that combines LiveURL, captcha handling, and session recording:

```codeBlockLines_p187
from browser_use import Browser, BrowserConfig, Agent
from browser_session import UseBrowserlessContext, ExtendedBrowserSession
from browser_use.browser.context import BrowserContextConfig
from langchain_anthropic import ChatAnthropic
import asyncio
import os

async def setup_browser() -> tuple[Browser, UseBrowserlessContext]:
    browserless_url = f"wss://production-sfo.browserless.io?token={os.environ['BROWSERLESS_API_TOKEN']}"

    browser = Browser(config=BrowserConfig(cdp_url=browserless_url))
    context = UseBrowserlessContext(
        browser,
        BrowserContextConfig(
            wait_for_network_idle_page_load_time=10.0,
            highlight_elements=True,
        )
    )

    return browser, context

async def main():
    browser, context = await setup_browser()
    session = await context.get_session()

    try:
        # Create CDP session
        cdp = await session.current_page.createCDPSession()

        # Start recording
        await cdp.send("Browserless.startRecording")

        # Generate LiveURL
        response = await cdp.send('Browserless.liveURL', {
            "timeout": 600000
        })
        live_url = response["liveURL"]
        print(f"Share this URL with users: {live_url}")

        # Handle captcha if detected
        cdp.on('Browserless.captchaFound', lambda: print('Captcha detected!'))

        # Wait for user interaction
        future = asyncio.Future()
        cdp.on('Browserless.liveComplete', lambda: future.set_result(True))
        await future

        # Stop recording and save
        response = await cdp.send("Browserless.stopRecording")
        with open("recording.webm", "wb") as f:
            f.write(response.value)

    finally:
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

```

For more information about CDP events and features, please refer to:

- [Browserless CDP Events Documentation](https://docs.browserless.io/baas/session-management/recording-liveurl)
- [Hybrid Automation Guide](https://docs.browserless.io/baas/hybrid-automation)
- [BrowserQL Integration](https://docs.browserless.io/browserql/recipes/hybrid-bql-playwright)

## Advanced Usage [​](https://docs.browserless.io/ai-integrations/browser-use/python\#advanced-usage "Direct link to Advanced Usage")

For more advanced usage scenarios, please refer to:

- [Browser Use Documentation](https://github.com/browser-use/browser-use)
- [Browserless BaaS Documentation](https://docs.browserless.io/baas/start)
- [Integrating with other LLM providers](https://docs.browserless.io/ai-integrations/start)

- [Prerequisites](https://docs.browserless.io/ai-integrations/browser-use/python#prerequisites)
- [Step-by-Step Setup](https://docs.browserless.io/ai-integrations/browser-use/python#step-by-step-setup)
- [How It Works](https://docs.browserless.io/ai-integrations/browser-use/python#how-it-works)
- [Additional Configuration](https://docs.browserless.io/ai-integrations/browser-use/python#additional-configuration)
  - [Proxy Support](https://docs.browserless.io/ai-integrations/browser-use/python#proxy-support)
  - [Context Configuration](https://docs.browserless.io/ai-integrations/browser-use/python#context-configuration)
- [Advanced Features](https://docs.browserless.io/ai-integrations/browser-use/python#advanced-features)
  - [CDP Events and LiveURL](https://docs.browserless.io/ai-integrations/browser-use/python#cdp-events-and-liveurl)
  - [Complete Example with CDP Events](https://docs.browserless.io/ai-integrations/browser-use/python#complete-example-with-cdp-events)
- [Advanced Usage](https://docs.browserless.io/ai-integrations/browser-use/python#advanced-usage)