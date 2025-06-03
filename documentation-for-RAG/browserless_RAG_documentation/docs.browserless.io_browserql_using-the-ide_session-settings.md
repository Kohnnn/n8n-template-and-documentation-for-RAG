---
url: "https://docs.browserless.io/browserql/using-the-ide/session-settings"
title: "Session Settings | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/using-the-ide/session-settings#__docusaurus_skipToContent_fallback)

On this page

BrowserQL Editor allows you to have multiple sessions, each with their own particular configurations. For example, you can have a first section running on chrome, with human-like behavior active, while the second one runs on chromium, without human-like behavior, and with a proxy.

## Configuring Session Settings [​](https://docs.browserless.io/browserql/using-the-ide/session-settings\#configuring-session-settings "Direct link to Configuring Session Settings")

Session Settings allows you to configure the following for each individual tab in the editor:

- **Browser**: Choose which browser the session will use. Either Chromium or Chrome.
- **Human-like Behavior**: Select whether the automation should imitate human behavior, including smooth mouse movements and typing patterns that resemble those of a person.
- **Adblock**: Toggle adblock on/off in the session. Useful for accessing websites cluttered with intrusive ads, improving page readability, reducing distractions, and speeding up data scraping workflows.
- **Residential Proxy**: Route the browser's requests through a residential proxy network. This enhances anonymity and mimics real user traffic, making it ideal for accessing geographically restricted content or bypassing anti-bot measures. _Note that this will significantly increase unit consumption_. Refer to the [Using a Proxy](https://docs.browserless.io/browserql/bot-detection/proxies) guide for more details.

Below shows how to configure different session settings, where:

### First Session

- **Browser**: `Chrome`
- **Human-like Behavior**: `On`
- **Adblock**: `On`
- **Residential Proxy**: `Off`

### Second Session

- **Browser**: `Chromium`
- **Human-like Behavior**: `Off`
- **Adblock**: `Off`
- **Residential Proxy**: `On`

Your browser does not support the video tag.

- [Configuring Session Settings](https://docs.browserless.io/browserql/using-the-ide/session-settings#configuring-session-settings)