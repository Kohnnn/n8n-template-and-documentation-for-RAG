---
url: "https://pptr.dev/next/api/puppeteer.browser"
title: "Browser class | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser)** (24.9.0).

Version: Next

On this page

[Browser](https://pptr.dev/next/api/puppeteer.browser) represents a browser instance that is either:

- connected to via [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect) or - launched by [PuppeteerNode.launch()](https://pptr.dev/next/api/puppeteer.puppeteernode.launch).

[Browser](https://pptr.dev/next/api/puppeteer.browser) [emits](https://pptr.dev/next/api/puppeteer.eventemitter.emit) various events which are documented in the [BrowserEvent](https://pptr.dev/next/api/puppeteer.browserevent) enum.

### Signature [​](https://pptr.dev/next/api/puppeteer.browser\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class Browser extends EventEmitter<BrowserEvents>

```

**Extends:** [EventEmitter](https://pptr.dev/next/api/puppeteer.eventemitter) < [BrowserEvents](https://pptr.dev/next/api/puppeteer.browserevents) >

## Remarks [​](https://pptr.dev/next/api/puppeteer.browser\#remarks "Direct link to Remarks")

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Browser` class.

## Example 1 [​](https://pptr.dev/next/api/puppeteer.browser\#example-1 "Direct link to Example 1")

Using a [Browser](https://pptr.dev/next/api/puppeteer.browser) to create a [Page](https://pptr.dev/next/api/puppeteer.page):

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
await browser.close();

```

## Example 2 [​](https://pptr.dev/next/api/puppeteer.browser\#example-2 "Direct link to Example 2")

Disconnecting from and reconnecting to a [Browser](https://pptr.dev/next/api/puppeteer.browser):

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch();
// Store the endpoint to be able to reconnect to the browser.
const browserWSEndpoint = browser.wsEndpoint();
// Disconnect puppeteer from the browser.
await browser.disconnect();

// Use the endpoint to reestablish a connection
const browser2 = await puppeteer.connect({browserWSEndpoint});
// Close the browser.
await browser2.close();

```

## Properties [​](https://pptr.dev/next/api/puppeteer.browser\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| connected | `readonly` | boolean | Whether Puppeteer is connected to this [browser](https://pptr.dev/next/api/puppeteer.browser). |
| debugInfo | `readonly` | [DebugInfo](https://pptr.dev/next/api/puppeteer.debuginfo) | **_(Experimental)_** Get debug information from Puppeteer.<br>**Remarks:**<br>Currently, includes pending protocol calls. In the future, we might add more info. |

## Methods [​](https://pptr.dev/next/api/puppeteer.browser\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [browserContexts()](https://pptr.dev/next/api/puppeteer.browser.browsercontexts) |  | Gets a list of open [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).<br>In a newly-created [browser](https://pptr.dev/next/api/puppeteer.browser), this will return a single instance of [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [close()](https://pptr.dev/next/api/puppeteer.browser.close) |  | Closes this [browser](https://pptr.dev/next/api/puppeteer.browser) and all associated [pages](https://pptr.dev/next/api/puppeteer.page). |
| [cookies()](https://pptr.dev/next/api/puppeteer.browser.cookies) |  | Returns all cookies in the default [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).<br>**Remarks:**<br>Shortcut for [browser.defaultBrowserContext().cookies()](https://pptr.dev/next/api/puppeteer.browsercontext.cookies). |
| [createBrowserContext(options)](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext) |  | Creates a new [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).<br>This won't share cookies/cache with other [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [defaultBrowserContext()](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext) |  | Gets the default [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).<br>**Remarks:**<br>The default [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) cannot be closed. |
| [deleteCookie(cookies)](https://pptr.dev/next/api/puppeteer.browser.deletecookie) |  | Removes cookies from the default [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).<br>**Remarks:**<br>Shortcut for [browser.defaultBrowserContext().deleteCookie()](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie). |
| [disconnect()](https://pptr.dev/next/api/puppeteer.browser.disconnect) |  | Disconnects Puppeteer from this [browser](https://pptr.dev/next/api/puppeteer.browser), but leaves the process running. |
| [installExtension(path)](https://pptr.dev/next/api/puppeteer.browser.installextension) |  | Installs an extension and returns the ID. In Chrome, this is only available if the browser was created using `pipe: true` and the `--enable-unsafe-extension-debugging` flag is set. |
| [isConnected()](https://pptr.dev/next/api/puppeteer.browser.isconnected) | `deprecated` | Whether Puppeteer is connected to this [browser](https://pptr.dev/next/api/puppeteer.browser).<br>**Deprecated:**<br>Use [Browser.connected](https://pptr.dev/next/api/puppeteer.browser). |
| [newPage()](https://pptr.dev/next/api/puppeteer.browser.newpage) |  | Creates a new [page](https://pptr.dev/next/api/puppeteer.page) in the [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext). |
| [pages()](https://pptr.dev/next/api/puppeteer.browser.pages) |  | Gets a list of all open [pages](https://pptr.dev/next/api/puppeteer.page) inside this [Browser](https://pptr.dev/next/api/puppeteer.browser).<br>If there are multiple [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext), this returns all [pages](https://pptr.dev/next/api/puppeteer.page) in all [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).<br>**Remarks:**<br>Non-visible [pages](https://pptr.dev/next/api/puppeteer.page), such as `"background_page"`, will not be listed here. You can find them using [Target.page()](https://pptr.dev/next/api/puppeteer.target.page). |
| [process()](https://pptr.dev/next/api/puppeteer.browser.process) |  | Gets the associated [ChildProcess](https://nodejs.org/api/child_process.html#class-childprocess). |
| [setCookie(cookies)](https://pptr.dev/next/api/puppeteer.browser.setcookie) |  | Sets cookies in the default [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).<br>**Remarks:**<br>Shortcut for [browser.defaultBrowserContext().setCookie()](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie). |
| [target()](https://pptr.dev/next/api/puppeteer.browser.target) |  | Gets the [target](https://pptr.dev/next/api/puppeteer.target) associated with the [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext)). |
| [targets()](https://pptr.dev/next/api/puppeteer.browser.targets) |  | Gets all active [targets](https://pptr.dev/next/api/puppeteer.target).<br>In case of multiple [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext), this returns all [targets](https://pptr.dev/next/api/puppeteer.target) in all [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [uninstallExtension(id)](https://pptr.dev/next/api/puppeteer.browser.uninstallextension) |  | Uninstalls an extension. In Chrome, this is only available if the browser was created using `pipe: true` and the `--enable-unsafe-extension-debugging` flag is set. |
| [userAgent()](https://pptr.dev/next/api/puppeteer.browser.useragent) |  | Gets this [browser's](https://pptr.dev/next/api/puppeteer.browser) original user agent.<br>[Pages](https://pptr.dev/next/api/puppeteer.page) can override the user agent with [Page.setUserAgent()](https://pptr.dev/next/api/puppeteer.page.setuseragent). |
| [version()](https://pptr.dev/next/api/puppeteer.browser.version) |  | Gets a string representing this [browser's](https://pptr.dev/next/api/puppeteer.browser) name and version.<br>For headless browser, this is similar to `"HeadlessChrome/61.0.3153.0"`. For non-headless or new-headless, this is similar to `"Chrome/61.0.3153.0"`. For Firefox, it is similar to `"Firefox/116.0a1"`.<br>The format of [Browser.version()](https://pptr.dev/next/api/puppeteer.browser.version) might change with future releases of browsers. |
| [waitForTarget(predicate, options)](https://pptr.dev/next/api/puppeteer.browser.waitfortarget) |  | Waits until a [target](https://pptr.dev/next/api/puppeteer.target) matching the given `predicate` appears and returns it.<br>This will look all open [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [wsEndpoint()](https://pptr.dev/next/api/puppeteer.browser.wsendpoint) |  | Gets the WebSocket URL to connect to this [browser](https://pptr.dev/next/api/puppeteer.browser).<br>This is usually used with [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect).<br>You can find the debugger URL ( `webSocketDebuggerUrl`) from `http://HOST:PORT/json/version`.<br>See [browser endpoint](https://chromedevtools.github.io/devtools-protocol/#how-do-i-access-the-browser-target) for more information.<br>**Remarks:**<br>The format is always `ws://HOST:PORT/devtools/browser/<id>`. |

- [Signature](https://pptr.dev/next/api/puppeteer.browser#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser#remarks)
- [Example 1](https://pptr.dev/next/api/puppeteer.browser#example-1)
- [Example 2](https://pptr.dev/next/api/puppeteer.browser#example-2)
- [Properties](https://pptr.dev/next/api/puppeteer.browser#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.browser#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!