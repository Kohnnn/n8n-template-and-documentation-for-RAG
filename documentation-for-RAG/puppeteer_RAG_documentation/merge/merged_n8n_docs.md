# n8n Documentation


## Advanced

### Awaitable type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.awaitable

[Skip to main content](https://pptr.dev/next/api/puppeteer.awaitable#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.awaitable)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.awaitable\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type Awaitable<T> = T | PromiseLike<T>;

```

- [Signature](https://pptr.dev/next/api/puppeteer.awaitable#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### AwaitableIterable type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.awaitableiterable

[Skip to main content](https://pptr.dev/next/api/puppeteer.awaitableiterable#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.awaitableiterable)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.awaitableiterable\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type AwaitableIterable<T> = Iterable<T> | AsyncIterable<T>;

```

- [Signature](https://pptr.dev/next/api/puppeteer.awaitableiterable#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### AwaitablePredicate type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.awaitablepredicate

[Skip to main content](https://pptr.dev/next/api/puppeteer.awaitablepredicate#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.awaitablepredicate)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.awaitablepredicate\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type AwaitablePredicate<T> = (value: T) => Awaitable<boolean>;

```

**References:** [Awaitable](https://pptr.dev/next/api/puppeteer.awaitable)

- [Signature](https://pptr.dev/next/api/puppeteer.awaitablepredicate#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### AwaitedLocator type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.awaitedlocator

[Skip to main content](https://pptr.dev/next/api/puppeteer.awaitedlocator#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.awaitedlocator)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.awaitedlocator\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type AwaitedLocator<T> = T extends Locator<infer S> ? S : never;

```

**References:** [Locator](https://pptr.dev/next/api/puppeteer.locator)

- [Signature](https://pptr.dev/next/api/puppeteer.awaitedlocator#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.waitForTarget() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.waitfortarget

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.waitfortarget#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.waitfortarget)** (24.9.0).



Waits until a [target](https://pptr.dev/next/api/puppeteer.target) matching the given `predicate` appears and returns it.

This will look all open [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.waitfortarget\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  waitForTarget(
    predicate: (x: Target) => boolean | Promise<boolean>,
    options?: WaitForTargetOptions,
  ): Promise<Target>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browser.waitfortarget\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| predicate | (x: [Target](https://pptr.dev/next/api/puppeteer.target)) =\> boolean \| Promise<boolean> |  |
| options | [WaitForTargetOptions](https://pptr.dev/next/api/puppeteer.waitfortargetoptions) | _(Optional)_ |

**Returns:**

Promise< [Target](https://pptr.dev/next/api/puppeteer.target) >

## Example [â€‹](https://pptr.dev/next/api/puppeteer.browser.waitfortarget\#example "Direct link to Example")

Finding a target for a page opened via `window.open`:

```codeBlockLines_RjmQ
await page.evaluate(() => window.open('https://www.example.com/'));
const newWindowTarget = await browser.waitForTarget(
  target => target.url() === 'https://www.example.com/',
);

```

- [Signature](https://pptr.dev/next/api/puppeteer.browser.waitfortarget#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.waitfortarget#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.browser.waitfortarget#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.waitForTarget() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.waitfortarget)** (24.9.0).



Waits until a [target](https://pptr.dev/next/api/puppeteer.target) matching the given `predicate` appears and returns it.

This will look all open [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  waitForTarget(
    predicate: (x: Target) => boolean | Promise<boolean>,
    options?: WaitForTargetOptions,
  ): Promise<Target>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| predicate | (x: [Target](https://pptr.dev/next/api/puppeteer.target)) =\> boolean \| Promise<boolean> |  |
| options | [WaitForTargetOptions](https://pptr.dev/next/api/puppeteer.waitfortargetoptions) | _(Optional)_ |

**Returns:**

Promise< [Target](https://pptr.dev/next/api/puppeteer.target) >

## Example [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget\#example "Direct link to Example")

Finding a target for a page opened via `window.open`:

```codeBlockLines_RjmQ
await page.evaluate(() => window.open('https://www.example.com/'));
const newWindowTarget = await browserContext.waitForTarget(
  target => target.url() === 'https://www.example.com/',
);

```

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DeviceRequestPrompt.waitForDevice() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice

[Skip to main content](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.devicerequestprompt.waitfordevice)** (24.9.0).



Resolve to the first device in the prompt matching a filter.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class DeviceRequestPrompt {
  waitForDevice(
    filter: (device: DeviceRequestPromptDevice) => boolean,
    options?: WaitTimeoutOptions,
  ): Promise<DeviceRequestPromptDevice>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| filter | (device: [DeviceRequestPromptDevice](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice)) =\> boolean |  |
| options | [WaitTimeoutOptions](https://pptr.dev/next/api/puppeteer.waittimeoutoptions) | _(Optional)_ |

**Returns:**

Promise< [DeviceRequestPromptDevice](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice) >

- [Signature](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---


## Other

### Puppeteer
Original URL: https://pptr.dev/category

[Skip to main content](https://pptr.dev/category#__docusaurus_skipToContent_fallback)

# Page Not Found

We could not find what you were looking for.

Please contact the owner of the site that linked you to the original URL and let them know their link is broken.

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Puppeteer | Puppeteer
Original URL: https://pptr.dev/next

[Skip to main content](https://pptr.dev/next#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/)** (24.9.0).


[![build](https://github.com/puppeteer/puppeteer/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/puppeteer/puppeteer/actions/workflows/ci.yml)[![npm puppeteer package](https://img.shields.io/npm/v/puppeteer.svg)](https://npmjs.org/package/puppeteer)

![](https://user-images.githubusercontent.com/10379601/29446482-04f7036a-841f-11e7-9872-91d1fc2ea683.png)

> Puppeteer is a JavaScript library which provides a high-level API to control
> Chrome or Firefox over the
> [DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) or [WebDriver BiDi](https://pptr.dev/webdriver-bidi).
> Puppeteer runs in the headless (no visible UI) by default

## [Get started](https://pptr.dev/docs) \| [API](https://pptr.dev/api) \| [FAQ](https://pptr.dev/faq) \| [Contributing](https://pptr.dev/contributing) \| [Troubleshooting](https://pptr.dev/troubleshooting) [â€‹](https://pptr.dev/next\#get-started--api--faq--contributing--troubleshooting "Direct link to get-started--api--faq--contributing--troubleshooting")

## Installation [â€‹](https://pptr.dev/next\#installation "Direct link to Installation")

- npm
- Yarn
- pnpm

```codeBlockLines_RjmQ
npm i puppeteer # Downloads compatible Chrome during installation.
npm i puppeteer-core # Alternatively, install as a library, without downloading Chrome.

```

```codeBlockLines_RjmQ
yarn add puppeteer # Downloads compatible Chrome during installation.
yarn add puppeteer-core # Alternatively, install as a library, without downloading Chrome.

```

```codeBlockLines_RjmQ
pnpm add puppeteer # Downloads compatible Chrome during installation.
pnpm add puppeteer-core # Alternatively, install as a library, without downloading Chrome.

```

## Example [â€‹](https://pptr.dev/next\#example "Direct link to Example")

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';
// Or import puppeteer from 'puppeteer-core';

// Launch the browser and open a new blank page
const browser = await puppeteer.launch();
const page = await browser.newPage();

// Navigate the page to a URL.
await page.goto('https://developer.chrome.com/');

// Set screen size.
await page.setViewport({width: 1080, height: 1024});

// Type into search box using accessible input name.
await page.locator('aria/Search').fill('automate beyond recorder');

// Wait and click on first result.
await page.locator('.devsite-result-item-link').click();

// Locate the full title with a unique string.
const textSelector = await page
  .locator('text/Customize and automate')
  .waitHandle();
const fullTitle = await textSelector?.evaluate(el => el.textContent);

// Print the full title.
console.log('The title of this blog post is "%s".', fullTitle);

await browser.close();

```

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### API Reference | Puppeteer
Original URL: https://pptr.dev/next/api

[Skip to main content](https://pptr.dev/next/api#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api)** (24.9.0).



## Classes [â€‹](https://pptr.dev/next/api\#classes "Direct link to Classes")

| Class | Description |
| --- | --- |
| [Accessibility](https://pptr.dev/next/api/puppeteer.accessibility) | The Accessibility class provides methods for inspecting the browser's accessibility tree. The accessibility tree is used by assistive technology such as [screen readers](https://en.wikipedia.org/wiki/Screen_reader) or [switches](https://en.wikipedia.org/wiki/Switch_access).<br>**Remarks:**<br>Accessibility is a very platform-specific thing. On different platforms, there are different screen readers that might have wildly different output.<br>Blink - Chrome's rendering engine - has a concept of "accessibility tree", which is then translated into different platform-specific APIs. Accessibility namespace gives users access to the Blink Accessibility Tree.<br>Most of the accessibility tree gets filtered out when converting from Blink AX Tree to Platform-specific AX-Tree or by assistive technologies themselves. By default, Puppeteer tries to approximate this filtering, exposing only the "interesting" nodes of the tree.<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Accessibility` class. |
| [Browser](https://pptr.dev/next/api/puppeteer.browser) | [Browser](https://pptr.dev/next/api/puppeteer.browser) represents a browser instance that is either:<br>- connected to via [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect) or - launched by [PuppeteerNode.launch()](https://pptr.dev/next/api/puppeteer.puppeteernode.launch).<br>[Browser](https://pptr.dev/next/api/puppeteer.browser) [emits](https://pptr.dev/next/api/puppeteer.eventemitter.emit) various events which are documented in the [BrowserEvent](https://pptr.dev/next/api/puppeteer.browserevent) enum.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Browser` class. |
| [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext) | [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext) represents individual user contexts within a [browser](https://pptr.dev/next/api/puppeteer.browser).<br>When a [browser](https://pptr.dev/next/api/puppeteer.browser) is launched, it has at least one default [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). Others can be created using [Browser.createBrowserContext()](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext). Each context has isolated storage (cookies/localStorage/etc.)<br>[BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext) [emits](https://pptr.dev/next/api/puppeteer.eventemitter) various events which are documented in the [BrowserContextEvent](https://pptr.dev/next/api/puppeteer.browsercontextevent) enum.<br>If a [page](https://pptr.dev/next/api/puppeteer.page) opens another [page](https://pptr.dev/next/api/puppeteer.page), e.g. using `window.open`, the popup will belong to the parent [page's browser context](https://pptr.dev/next/api/puppeteer.page.browsercontext).<br>**Remarks:**<br>In Chrome all non-default contexts are incognito, and [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext) might be incognito if you provide the `--incognito` argument when launching the browser.<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `BrowserContext` class. |
| [BrowserLauncher](https://pptr.dev/next/api/puppeteer.browserlauncher) | Describes a launcher - a class that is able to create and launch a browser instance.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `BrowserLauncher` class. |
| [CDPSession](https://pptr.dev/next/api/puppeteer.cdpsession) | The `CDPSession` instances are used to talk raw Chrome Devtools Protocol.<br>**Remarks:**<br>Protocol methods can be called with [CDPSession.send()](https://pptr.dev/next/api/puppeteer.cdpsession.send) method and protocol events can be subscribed to with `CDPSession.on` method.<br>Useful links: [DevTools Protocol Viewer](https://chromedevtools.github.io/devtools-protocol/) and [Getting Started with DevTools Protocol](https://github.com/aslushnikov/getting-started-with-cdp/blob/HEAD/README.md).<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `CDPSession` class. |
| [Connection](https://pptr.dev/next/api/puppeteer.connection) |  |
| [ConsoleMessage](https://pptr.dev/next/api/puppeteer.consolemessage) | ConsoleMessage objects are dispatched by page via the 'console' event.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `ConsoleMessage` class. |
| [Coverage](https://pptr.dev/next/api/puppeteer.coverage) | The Coverage class provides methods to gather information about parts of JavaScript and CSS that were used by the page.<br>**Remarks:**<br>To output coverage in a form consumable by [Istanbul](https://github.com/istanbuljs), see [puppeteer-to-istanbul](https://github.com/istanbuljs/puppeteer-to-istanbul).<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Coverage` class. |
| [CSSCoverage](https://pptr.dev/next/api/puppeteer.csscoverage) |  |
| [DeviceRequestPrompt](https://pptr.dev/next/api/puppeteer.devicerequestprompt) | Device request prompts let you respond to the page requesting for a device through an API like WebBluetooth.<br>**Remarks:**<br>`DeviceRequestPrompt` instances are returned via the [Page.waitForDevicePrompt()](https://pptr.dev/next/api/puppeteer.page.waitfordeviceprompt) method.<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `DeviceRequestPrompt` class. |
| [DeviceRequestPromptDevice](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice) | Device in a request prompt.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `DeviceRequestPromptDevice` class. |
| [Dialog](https://pptr.dev/next/api/puppeteer.dialog) | Dialog instances are dispatched by the [Page](https://pptr.dev/next/api/puppeteer.page) via the `dialog` event.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Dialog` class. |
| [ElementHandle](https://pptr.dev/next/api/puppeteer.elementhandle) | ElementHandle represents an in-page DOM element.<br>**Remarks:**<br>ElementHandles can be created with the [Page.$()](https://pptr.dev/next/api/puppeteer.page._) method.<br>```codeBlockLines_RjmQ<br>import puppeteer from 'puppeteer';<br>(async () => {<br>  const browser = await puppeteer.launch();<br>  const page = await browser.newPage();<br>  await page.goto('https://example.com');<br>  const hrefElement = await page.$('a');<br>  await hrefElement.click();<br>  // ...<br>})();<br>```<br>ElementHandle prevents the DOM element from being garbage-collected unless the handle is [disposed](https://pptr.dev/next/api/puppeteer.jshandle.dispose). ElementHandles are auto-disposed when their origin frame gets navigated.<br>ElementHandle instances can be used as arguments in [Page.$eval()](https://pptr.dev/next/api/puppeteer.page._eval) and [Page.evaluate()](https://pptr.dev/next/api/puppeteer.page.evaluate) methods.<br>If you're using TypeScript, ElementHandle takes a generic argument that denotes the type of element the handle is holding within. For example, if you have a handle to a `<select>` element, you can type it as `ElementHandle<HTMLSelectElement>` and you get some nicer type checks.<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `ElementHandle` class. |
| [EventEmitter](https://pptr.dev/next/api/puppeteer.eventemitter) | The EventEmitter class that many Puppeteer classes extend.<br>**Remarks:**<br>This allows you to listen to events that Puppeteer classes fire and act accordingly. Therefore you'll mostly use [on](https://pptr.dev/next/api/puppeteer.eventemitter.on) and [off](https://pptr.dev/next/api/puppeteer.eventemitter.off) to bind and unbind to event listeners.<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `EventEmitter` class. |
| [ExtensionTransport](https://pptr.dev/next/api/puppeteer.extensiontransport) | **_(Experimental)_** Experimental ExtensionTransport allows establishing a connection via chrome.debugger API if Puppeteer runs in an extension. Since Chrome DevTools Protocol is restricted for extensions, the transport implements missing commands and events.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `ExtensionTransport` class. |
| [FileChooser](https://pptr.dev/next/api/puppeteer.filechooser) | File choosers let you react to the page requesting for a file.<br>**Remarks:**<br>`FileChooser` instances are returned via the [Page.waitForFileChooser()](https://pptr.dev/next/api/puppeteer.page.waitforfilechooser) method.<br>In browsers, only one file chooser can be opened at a time. All file choosers must be accepted or canceled. Not doing so will prevent subsequent file choosers from appearing.<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `FileChooser` class. |
| [Frame](https://pptr.dev/next/api/puppeteer.frame) | Represents a DOM frame.<br>To understand frames, you can think of frames as `<iframe>` elements. Just like iframes, frames can be nested, and when JavaScript is executed in a frame, the JavaScript does not affect frames inside the ambient frame the JavaScript executes in.<br>**Remarks:**<br>Frame lifecycles are controlled by three events that are all dispatched on the parent [page](https://pptr.dev/next/api/puppeteer.frame.page):<br>- [PageEvent.FrameAttached](https://pptr.dev/next/api/puppeteer.pageevent) \- [PageEvent.FrameNavigated](https://pptr.dev/next/api/puppeteer.pageevent) \- [PageEvent.FrameDetached](https://pptr.dev/next/api/puppeteer.pageevent)<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Frame` class. |
| [HTTPRequest](https://pptr.dev/next/api/puppeteer.httprequest) | Represents an HTTP request sent by a page.<br>**Remarks:**<br>Whenever the page sends a request, such as for a network resource, the following events are emitted by Puppeteer's `page`:<br>- `request`: emitted when the request is issued by the page.<br>  <br>- `requestfinished` \- emitted when the response body is downloaded and the request is complete.<br>  <br>If request fails at some point, then instead of `requestfinished` event the `requestfailed` event is emitted.<br>All of these events provide an instance of `HTTPRequest` representing the request that occurred:<br>```codeBlockLines_RjmQ<br>page.on('request', request => ...)<br>```<br>NOTE: HTTP Error responses, such as 404 or 503, are still successful responses from HTTP standpoint, so request will complete with `requestfinished` event.<br>If request gets a 'redirect' response, the request is successfully finished with the `requestfinished` event, and a new request is issued to a redirected url.<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `HTTPRequest` class. |
| [HTTPResponse](https://pptr.dev/next/api/puppeteer.httpresponse) | The HTTPResponse class represents responses which are received by the [Page](https://pptr.dev/next/api/puppeteer.page) class.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `HTTPResponse` class. |
| [JSCoverage](https://pptr.dev/next/api/puppeteer.jscoverage) | **Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `JSCoverage` class. |
| [JSHandle](https://pptr.dev/next/api/puppeteer.jshandle) | Represents a reference to a JavaScript object. Instances can be created using [Page.evaluateHandle()](https://pptr.dev/next/api/puppeteer.page.evaluatehandle).<br>Handles prevent the referenced JavaScript object from being garbage-collected unless the handle is purposely [disposed](https://pptr.dev/next/api/puppeteer.jshandle.dispose). JSHandles are auto-disposed when their associated frame is navigated away or the parent context gets destroyed.<br>Handles can be used as arguments for any evaluation function such as [Page.$eval()](https://pptr.dev/next/api/puppeteer.page._eval), [Page.evaluate()](https://pptr.dev/next/api/puppeteer.page.evaluate), and [Page.evaluateHandle()](https://pptr.dev/next/api/puppeteer.page.evaluatehandle). They are resolved to their referenced object.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `JSHandle` class. |
| [Keyboard](https://pptr.dev/next/api/puppeteer.keyboard) | Keyboard provides an api for managing a virtual keyboard. The high level api is [Keyboard.type()](https://pptr.dev/next/api/puppeteer.keyboard.type), which takes raw characters and generates proper keydown, keypress/input, and keyup events on your page.<br>**Remarks:**<br>For finer control, you can use [Keyboard.down()](https://pptr.dev/next/api/puppeteer.keyboard.down), [Keyboard.up()](https://pptr.dev/next/api/puppeteer.keyboard.up), and [Keyboard.sendCharacter()](https://pptr.dev/next/api/puppeteer.keyboard.sendcharacter) to manually fire events as if they were generated from a real keyboard.<br>On macOS, keyboard shortcuts like `âŒ˜ A` -\> Select All do not work. See [#1313](https://github.com/puppeteer/puppeteer/issues/1313).<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Keyboard` class. |
| [Locator](https://pptr.dev/next/api/puppeteer.locator) | Locators describe a strategy of locating objects and performing an action on them. If the action fails because the object is not ready for the action, the whole operation is retried. Various preconditions for a successful action are checked automatically.<br>See [https://pptr.dev/guides/page-interactions#locators](https://pptr.dev/guides/page-interactions#locators) for details. |
| [Mouse](https://pptr.dev/next/api/puppeteer.mouse) | The Mouse class operates in main-frame CSS pixels relative to the top-left corner of the viewport.<br>**Remarks:**<br>Every `page` object has its own Mouse, accessible with [Page.mouse](https://pptr.dev/next/api/puppeteer.page#mouse).<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Mouse` class. |
| [Page](https://pptr.dev/next/api/puppeteer.page) | Page provides methods to interact with a single tab or [extension background page](https://developer.chrome.com/extensions/background_pages) in the browser.<br>note<br>One Browser instance might have multiple Page instances.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Page` class. |
| [ProtocolError](https://pptr.dev/next/api/puppeteer.protocolerror) | ProtocolError is emitted whenever there is an error from the protocol. |
| [Puppeteer](https://pptr.dev/next/api/puppeteer.puppeteer) | The main Puppeteer class.<br>IMPORTANT: if you are using Puppeteer in a Node environment, you will get an instance of [PuppeteerNode](https://pptr.dev/next/api/puppeteer.puppeteernode) when you import or require `puppeteer`. That class extends `Puppeteer`, so has all the methods documented below as well as all that are defined on [PuppeteerNode](https://pptr.dev/next/api/puppeteer.puppeteernode).<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Puppeteer` class. |
| [PuppeteerError](https://pptr.dev/next/api/puppeteer.puppeteererror) | The base class for all Puppeteer-specific errors<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `PuppeteerError` class. |
| [PuppeteerNode](https://pptr.dev/next/api/puppeteer.puppeteernode) | Extends the main [Puppeteer](https://pptr.dev/next/api/puppeteer.puppeteer) class with Node specific behaviour for fetching and downloading browsers.<br>If you're using Puppeteer in a Node environment, this is the class you'll get when you run `require('puppeteer')` (or the equivalent ES `import`).<br>**Remarks:**<br>The most common method to use is [launch](https://pptr.dev/next/api/puppeteer.puppeteernode.launch), which is used to launch and connect to a new browser instance.<br>See [the main Puppeteer class](https://pptr.dev/next/api/puppeteer.puppeteer) for methods common to all environments, such as [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect).<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `PuppeteerNode` class. |
| [ScreenRecorder](https://pptr.dev/next/api/puppeteer.screenrecorder) | **Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `ScreenRecorder` class. |
| [SecurityDetails](https://pptr.dev/next/api/puppeteer.securitydetails) | The SecurityDetails class represents the security details of a response that was received over a secure connection.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `SecurityDetails` class. |
| [Target](https://pptr.dev/next/api/puppeteer.target) | Target represents a [CDP target](https://chromedevtools.github.io/devtools-protocol/tot/Target/). In CDP a target is something that can be debugged such a frame, a page or a worker.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Target` class. |
| [TimeoutError](https://pptr.dev/next/api/puppeteer.timeouterror) | TimeoutError is emitted whenever certain operations are terminated due to timeout.<br>**Remarks:**<br>Example operations are [page.waitForSelector](https://pptr.dev/next/api/puppeteer.page.waitforselector) or [puppeteer.launch](https://pptr.dev/next/api/puppeteer.puppeteernode.launch). |
| [TouchError](https://pptr.dev/next/api/puppeteer.toucherror) | TouchError is thrown when an attempt is made to move or end a touch that does not exist. |
| [Touchscreen](https://pptr.dev/next/api/puppeteer.touchscreen) | The Touchscreen class exposes touchscreen events.<br>**Remarks:**<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Touchscreen` class. |
| [Tracing](https://pptr.dev/next/api/puppeteer.tracing) | The Tracing class exposes the tracing audit interface.<br>**Remarks:**<br>You can use `tracing.start` and `tracing.stop` to create a trace file which can be opened in Chrome DevTools or [timeline viewer](https://chromedevtools.github.io/timeline-viewer/).<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Tracing` class. |
| [UnsupportedOperation](https://pptr.dev/next/api/puppeteer.unsupportedoperation) | Puppeteer will throw this error if a method is not supported by the currently used protocol |
| [WebWorker](https://pptr.dev/next/api/puppeteer.webworker) | This class represents a [WebWorker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API).<br>**Remarks:**<br>The events `workercreated` and `workerdestroyed` are emitted on the page object to signal the worker lifecycle.<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `WebWorker` class. |

## Enumerations [â€‹](https://pptr.dev/next/api\#enumerations "Direct link to Enumerations")

| Enumeration | Description |
| --- | --- |
| [BrowserContextEvent](https://pptr.dev/next/api/puppeteer.browsercontextevent) |  |
| [BrowserEvent](https://pptr.dev/next/api/puppeteer.browserevent) | All the events a [browser instance](https://pptr.dev/next/api/puppeteer.browser) may emit. |
| [InterceptResolutionAction](https://pptr.dev/next/api/puppeteer.interceptresolutionaction) |  |
| [LocatorEvent](https://pptr.dev/next/api/puppeteer.locatorevent) | All the events that a locator instance may emit. |
| [PageEvent](https://pptr.dev/next/api/puppeteer.pageevent) | All the events that a page instance may emit. |
| [TargetType](https://pptr.dev/next/api/puppeteer.targettype) |  |

## Functions [â€‹](https://pptr.dev/next/api\#functions "Direct link to Functions")

| Function | Description |
| --- | --- |
| [connect(options)](https://pptr.dev/next/api/puppeteer.connect) |  |
| [convertCookiesPartitionKeyFromPuppeteerToCdp(partitionKey)](https://pptr.dev/next/api/puppeteer.convertcookiespartitionkeyfrompuppeteertocdp) |  |
| [defaultArgs(options)](https://pptr.dev/next/api/puppeteer.defaultargs) |  |
| [launch(options)](https://pptr.dev/next/api/puppeteer.launch) |  |
| [trimCache()](https://pptr.dev/next/api/puppeteer.trimcache) |  |

## Interfaces [â€‹](https://pptr.dev/next/api\#interfaces "Direct link to Interfaces")

| Interface | Description |
| --- | --- |
| [ActionOptions](https://pptr.dev/next/api/puppeteer.actionoptions) |  |
| [AutofillData](https://pptr.dev/next/api/puppeteer.autofilldata) |  |
| [BoundingBox](https://pptr.dev/next/api/puppeteer.boundingbox) |  |
| [BoxModel](https://pptr.dev/next/api/puppeteer.boxmodel) |  |
| [BrowserContextEvents](https://pptr.dev/next/api/puppeteer.browsercontextevents) |  |
| [BrowserContextOptions](https://pptr.dev/next/api/puppeteer.browsercontextoptions) |  |
| [BrowserEvents](https://pptr.dev/next/api/puppeteer.browserevents) |  |
| [CDPSessionEvents](https://pptr.dev/next/api/puppeteer.cdpsessionevents) |  |
| [ChromeHeadlessShellSettings](https://pptr.dev/next/api/puppeteer.chromeheadlessshellsettings) |  |
| [ChromeSettings](https://pptr.dev/next/api/puppeteer.chromesettings) |  |
| [ClickOptions](https://pptr.dev/next/api/puppeteer.clickoptions) |  |
| [CommandOptions](https://pptr.dev/next/api/puppeteer.commandoptions) |  |
| [CommonEventEmitter](https://pptr.dev/next/api/puppeteer.commoneventemitter) |  |
| [Configuration](https://pptr.dev/next/api/puppeteer.configuration) | Defines options to configure Puppeteer's behavior during installation and runtime.<br>See individual properties for more information. |
| [ConnectionTransport](https://pptr.dev/next/api/puppeteer.connectiontransport) |  |
| [ConnectOptions](https://pptr.dev/next/api/puppeteer.connectoptions) | Generic browser options that can be passed when launching any browser or when connecting to an existing browser instance. |
| [ConsoleMessageLocation](https://pptr.dev/next/api/puppeteer.consolemessagelocation) |  |
| [ContinueRequestOverrides](https://pptr.dev/next/api/puppeteer.continuerequestoverrides) |  |
|  | Represents a cookie object. |
| [CookieData](https://pptr.dev/next/api/puppeteer.cookiedata) | Cookie parameter object used to set cookies in the browser-level cookies API. |
| [CookieParam](https://pptr.dev/next/api/puppeteer.cookieparam) | Cookie parameter object used to set cookies in the page-level cookies API. |
| [CookiePartitionKey](https://pptr.dev/next/api/puppeteer.cookiepartitionkey) | Represents a cookie partition key in Chrome. |
| [CoverageEntry](https://pptr.dev/next/api/puppeteer.coverageentry) | The CoverageEntry class represents one entry of the coverage report. |
| [Credentials](https://pptr.dev/next/api/puppeteer.credentials) |  |
| [CSSCoverageOptions](https://pptr.dev/next/api/puppeteer.csscoverageoptions) | Set of configurable options for CSS coverage. |
| [CustomQueryHandler](https://pptr.dev/next/api/puppeteer.customqueryhandler) |  |
| [DebugInfo](https://pptr.dev/next/api/puppeteer.debuginfo) | **_(Experimental)_** |
| [DeleteCookiesRequest](https://pptr.dev/next/api/puppeteer.deletecookiesrequest) |  |
| [Device](https://pptr.dev/next/api/puppeteer.device) |  |
| [DownloadBehavior](https://pptr.dev/next/api/puppeteer.downloadbehavior) |  |
| [ElementScreenshotOptions](https://pptr.dev/next/api/puppeteer.elementscreenshotoptions) |  |
| [FirefoxSettings](https://pptr.dev/next/api/puppeteer.firefoxsettings) |  |
| [FrameAddScriptTagOptions](https://pptr.dev/next/api/puppeteer.frameaddscripttagoptions) |  |
| [FrameAddStyleTagOptions](https://pptr.dev/next/api/puppeteer.frameaddstyletagoptions) |  |
| [FrameEvents](https://pptr.dev/next/api/puppeteer.frameevents) |  |
| [FrameWaitForFunctionOptions](https://pptr.dev/next/api/puppeteer.framewaitforfunctionoptions) |  |
| [GeolocationOptions](https://pptr.dev/next/api/puppeteer.geolocationoptions) |  |
| [GoToOptions](https://pptr.dev/next/api/puppeteer.gotooptions) |  |
| [InterceptResolutionState](https://pptr.dev/next/api/puppeteer.interceptresolutionstate) |  |
| [InternalNetworkConditions](https://pptr.dev/next/api/puppeteer.internalnetworkconditions) |  |
| [JSCoverageEntry](https://pptr.dev/next/api/puppeteer.jscoverageentry) | The CoverageEntry class for JavaScript |
| [JSCoverageOptions](https://pptr.dev/next/api/puppeteer.jscoverageoptions) | Set of configurable options for JS coverage. |
| [KeyboardTypeOptions](https://pptr.dev/next/api/puppeteer.keyboardtypeoptions) |  |
| [KeyDownOptions](https://pptr.dev/next/api/puppeteer.keydownoptions) |  |
| [LaunchOptions](https://pptr.dev/next/api/puppeteer.launchoptions) | Generic launch options that can be passed when launching any browser. |
| [LocatorEvents](https://pptr.dev/next/api/puppeteer.locatorevents) |  |
| [LocatorScrollOptions](https://pptr.dev/next/api/puppeteer.locatorscrolloptions) |  |
| [MediaFeature](https://pptr.dev/next/api/puppeteer.mediafeature) | A media feature to emulate. |
| [Metrics](https://pptr.dev/next/api/puppeteer.metrics) |  |
| [MouseClickOptions](https://pptr.dev/next/api/puppeteer.mouseclickoptions) |  |
| [MouseMoveOptions](https://pptr.dev/next/api/puppeteer.mousemoveoptions) |  |
| [MouseOptions](https://pptr.dev/next/api/puppeteer.mouseoptions) |  |
| [MouseWheelOptions](https://pptr.dev/next/api/puppeteer.mousewheeloptions) |  |
| [Moveable](https://pptr.dev/next/api/puppeteer.moveable) |  |
| [NetworkConditions](https://pptr.dev/next/api/puppeteer.networkconditions) |  |
| [NewDocumentScriptEvaluation](https://pptr.dev/next/api/puppeteer.newdocumentscriptevaluation) |  |
| [Offset](https://pptr.dev/next/api/puppeteer.offset) |  |
| [PageEvents](https://pptr.dev/next/api/puppeteer.pageevents) | Denotes the objects received by callback functions for page events.<br>See [PageEvent](https://pptr.dev/next/api/puppeteer.pageevent) for more detail on the events and when they are emitted. |
| [PDFMargin](https://pptr.dev/next/api/puppeteer.pdfmargin) |  |
| [PDFOptions](https://pptr.dev/next/api/puppeteer.pdfoptions) | Valid options to configure PDF generation via [Page.pdf()](https://pptr.dev/next/api/puppeteer.page.pdf). |
| [Point](https://pptr.dev/next/api/puppeteer.point) |  |
| [QueryOptions](https://pptr.dev/next/api/puppeteer.queryoptions) |  |
| [RemoteAddress](https://pptr.dev/next/api/puppeteer.remoteaddress) |  |
| [ResponseForRequest](https://pptr.dev/next/api/puppeteer.responseforrequest) | Required response data to fulfill a request with. |
| [ScreencastOptions](https://pptr.dev/next/api/puppeteer.screencastoptions) | **_(Experimental)_** |
| [ScreenshotClip](https://pptr.dev/next/api/puppeteer.screenshotclip) |  |
| [ScreenshotOptions](https://pptr.dev/next/api/puppeteer.screenshotoptions) |  |
| [SerializedAXNode](https://pptr.dev/next/api/puppeteer.serializedaxnode) | Represents a Node and the properties of it that are relevant to Accessibility. |
| [SnapshotOptions](https://pptr.dev/next/api/puppeteer.snapshotoptions) |  |
| [SupportedWebDriverCapabilities](https://pptr.dev/next/api/puppeteer.supportedwebdrivercapabilities) | WebDriver BiDi capabilities that are not set by Puppeteer itself. |
| [TouchHandle](https://pptr.dev/next/api/puppeteer.touchhandle) | The TouchHandle interface exposes methods to manipulate touches that have been started |
| [TracingOptions](https://pptr.dev/next/api/puppeteer.tracingoptions) |  |
| [Viewport](https://pptr.dev/next/api/puppeteer.viewport) |  |
| [WaitForNetworkIdleOptions](https://pptr.dev/next/api/puppeteer.waitfornetworkidleoptions) |  |
| [WaitForOptions](https://pptr.dev/next/api/puppeteer.waitforoptions) |  |
| [WaitForSelectorOptions](https://pptr.dev/next/api/puppeteer.waitforselectoroptions) |  |
| [WaitForTargetOptions](https://pptr.dev/next/api/puppeteer.waitfortargetoptions) |  |
| [WaitTimeoutOptions](https://pptr.dev/next/api/puppeteer.waittimeoutoptions) |  |

## Namespaces [â€‹](https://pptr.dev/next/api\#namespaces "Direct link to Namespaces")

| Namespace | Description |
| --- | --- |
| [CDPSessionEvent](https://pptr.dev/next/api/puppeteer.cdpsessionevent) | Events that the CDPSession class emits. |

## Variables [â€‹](https://pptr.dev/next/api\#variables "Direct link to Variables")

| Variable | Description |
| --- | --- |
| [DEFAULT\_INTERCEPT\_RESOLUTION\_PRIORITY](https://pptr.dev/next/api/puppeteer.default_intercept_resolution_priority) | The default cooperative request interception resolution priority |
| [executablePath](https://pptr.dev/next/api/puppeteer.executablepath) |  |
| [KnownDevices](https://pptr.dev/next/api/puppeteer.knowndevices) | A list of devices to be used with [Page.emulate()](https://pptr.dev/next/api/puppeteer.page.emulate). |
| [MouseButton](https://pptr.dev/next/api/puppeteer.mousebutton) | Enum of valid mouse buttons. |
| [PredefinedNetworkConditions](https://pptr.dev/next/api/puppeteer.predefinednetworkconditions) | A list of pre-defined network conditions to be used with [Page.emulateNetworkConditions()](https://pptr.dev/next/api/puppeteer.page.emulatenetworkconditions). |
| [puppeteer](https://pptr.dev/next/api/puppeteer.puppeteer) |  |

## Type Aliases [â€‹](https://pptr.dev/next/api\#type-aliases "Direct link to Type Aliases")

| Type Alias | Description |
| --- | --- |
| [ActionResult](https://pptr.dev/next/api/puppeteer.actionresult) |  |
| [Awaitable](https://pptr.dev/next/api/puppeteer.awaitable) |  |
| [AwaitableIterable](https://pptr.dev/next/api/puppeteer.awaitableiterable) |  |
| [AwaitablePredicate](https://pptr.dev/next/api/puppeteer.awaitablepredicate) |  |
| [AwaitedLocator](https://pptr.dev/next/api/puppeteer.awaitedlocator) |  |
| [CDPEvents](https://pptr.dev/next/api/puppeteer.cdpevents) |  |
| [ChromeReleaseChannel](https://pptr.dev/next/api/puppeteer.chromereleasechannel) |  |
| [ConsoleMessageType](https://pptr.dev/next/api/puppeteer.consolemessagetype) | The supported types for console messages. |
| [CookiePriority](https://pptr.dev/next/api/puppeteer.cookiepriority) | Represents the cookie's 'Priority' status: [https://tools.ietf.org/html/draft-west-cookie-priority-00](https://tools.ietf.org/html/draft-west-cookie-priority-00) |
| [CookieSameSite](https://pptr.dev/next/api/puppeteer.cookiesamesite) | Represents the cookie's 'SameSite' status: [https://tools.ietf.org/html/draft-west-first-party-cookies](https://tools.ietf.org/html/draft-west-first-party-cookies) |
| [CookieSourceScheme](https://pptr.dev/next/api/puppeteer.cookiesourcescheme) | Represents the source scheme of the origin that originally set the cookie. A value of "Unset" allows protocol clients to emulate legacy cookie scope for the scheme. This is a temporary ability and it will be removed in the future. |
| [DownloadPolicy](https://pptr.dev/next/api/puppeteer.downloadpolicy) |  |
| [ElementFor](https://pptr.dev/next/api/puppeteer.elementfor) |  |
| [ErrorCode](https://pptr.dev/next/api/puppeteer.errorcode) |  |
| [EvaluateFunc](https://pptr.dev/next/api/puppeteer.evaluatefunc) |  |
| [EvaluateFuncWith](https://pptr.dev/next/api/puppeteer.evaluatefuncwith) |  |
| [EventsWithWildcard](https://pptr.dev/next/api/puppeteer.eventswithwildcard) |  |
| [EventType](https://pptr.dev/next/api/puppeteer.eventtype) |  |
| [ExperimentsConfiguration](https://pptr.dev/next/api/puppeteer.experimentsconfiguration) | Defines experiment options for Puppeteer.<br>See individual properties for more information. |
| [FlattenHandle](https://pptr.dev/next/api/puppeteer.flattenhandle) |  |
| [HandleFor](https://pptr.dev/next/api/puppeteer.handlefor) |  |
| [HandleOr](https://pptr.dev/next/api/puppeteer.handleor) |  |
| [Handler](https://pptr.dev/next/api/puppeteer.handler) |  |
| [ImageFormat](https://pptr.dev/next/api/puppeteer.imageformat) |  |
| [InnerParams](https://pptr.dev/next/api/puppeteer.innerparams) |  |
| [KeyInput](https://pptr.dev/next/api/puppeteer.keyinput) | All the valid keys that can be passed to functions that take user input, such as [keyboard.press](https://pptr.dev/next/api/puppeteer.keyboard.press) |
| [KeyPressOptions](https://pptr.dev/next/api/puppeteer.keypressoptions) |  |
| [LocatorClickOptions](https://pptr.dev/next/api/puppeteer.locatorclickoptions) |  |
| [LowerCasePaperFormat](https://pptr.dev/next/api/puppeteer.lowercasepaperformat) |  |
| [Mapper](https://pptr.dev/next/api/puppeteer.mapper) |  |
| [MouseButton](https://pptr.dev/next/api/puppeteer.mousebutton) |  |
| [NodeFor](https://pptr.dev/next/api/puppeteer.nodefor) |  |
| [PaperFormat](https://pptr.dev/next/api/puppeteer.paperformat) | All the valid paper format types when printing a PDF.<br>**Remarks:**<br>The sizes of each format are as follows:<br>- `Letter`: 8.5in x 11in / 21.59cm x 27.94cm<br>  <br>- `Legal`: 8.5in x 14in / 21.59cm x 35.56cm<br>  <br>- `Tabloid`: 11in x 17in / 27.94cm x 43.18cm<br>  <br>- `Ledger`: 17in x 11in / 43.18cm x 27.94cm<br>  <br>- `A0`: 33.1102in x 46.811in / 84.1cm x 118.9cm<br>  <br>- `A1`: 23.3858in x 33.1102in / 59.4cm x 84.1cm<br>  <br>- `A2`: 16.5354in x 23.3858in / 42cm x 59.4cm<br>  <br>- `A3`: 11.6929in x 16.5354in / 29.7cm x 42cm<br>  <br>- `A4`: 8.2677in x 11.6929in / 21cm x 29.7cm<br>  <br>- `A5`: 5.8268in x 8.2677in / 14.8cm x 21cm<br>  <br>- `A6`: 4.1339in x 5.8268in / 10.5cm x 14.8cm |
| [Permission](https://pptr.dev/next/api/puppeteer.permission) |  |
| [Predicate](https://pptr.dev/next/api/puppeteer.predicate) |  |
| [ProtocolLifeCycleEvent](https://pptr.dev/next/api/puppeteer.protocollifecycleevent) |  |
| [ProtocolType](https://pptr.dev/next/api/puppeteer.protocoltype) |  |
| [PuppeteerLifeCycleEvent](https://pptr.dev/next/api/puppeteer.puppeteerlifecycleevent) |  |
| [Quad](https://pptr.dev/next/api/puppeteer.quad) |  |
| [ResourceType](https://pptr.dev/next/api/puppeteer.resourcetype) | Resource types for HTTPRequests as perceived by the rendering engine. |
| [SupportedBrowser](https://pptr.dev/next/api/puppeteer.supportedbrowser) | Browsers supported by Puppeteer. |
| [SupportedWebDriverCapability](https://pptr.dev/next/api/puppeteer.supportedwebdrivercapability) |  |
| [TargetFilterCallback](https://pptr.dev/next/api/puppeteer.targetfiltercallback) |  |
| [VideoFormat](https://pptr.dev/next/api/puppeteer.videoformat) |  |
| [VisibilityOption](https://pptr.dev/next/api/puppeteer.visibilityoption) | Whether to wait for the element to be [visible](https://pptr.dev/next/api/puppeteer.elementhandle.isvisible) or [hidden](https://pptr.dev/next/api/puppeteer.elementhandle.ishidden). `null` to disable visibility checks. |

- [Classes](https://pptr.dev/next/api#classes)
- [Enumerations](https://pptr.dev/next/api#enumerations)
- [Functions](https://pptr.dev/next/api#functions)
- [Interfaces](https://pptr.dev/next/api#interfaces)
- [Namespaces](https://pptr.dev/next/api#namespaces)
- [Variables](https://pptr.dev/next/api#variables)
- [Type Aliases](https://pptr.dev/next/api#type-aliases)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Accessibility class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.accessibility

[Skip to main content](https://pptr.dev/next/api/puppeteer.accessibility#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.accessibility)** (24.9.0).



The Accessibility class provides methods for inspecting the browser's accessibility tree. The accessibility tree is used by assistive technology such as [screen readers](https://en.wikipedia.org/wiki/Screen_reader) or [switches](https://en.wikipedia.org/wiki/Switch_access).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.accessibility\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class Accessibility

```

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.accessibility\#remarks "Direct link to Remarks")

Accessibility is a very platform-specific thing. On different platforms, there are different screen readers that might have wildly different output.

Blink - Chrome's rendering engine - has a concept of "accessibility tree", which is then translated into different platform-specific APIs. Accessibility namespace gives users access to the Blink Accessibility Tree.

Most of the accessibility tree gets filtered out when converting from Blink AX Tree to Platform-specific AX-Tree or by assistive technologies themselves. By default, Puppeteer tries to approximate this filtering, exposing only the "interesting" nodes of the tree.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Accessibility` class.

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.accessibility\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [snapshot(options)](https://pptr.dev/next/api/puppeteer.accessibility.snapshot) |  | Captures the current state of the accessibility tree. The returned object represents the root accessible node of the page.<br>**Remarks:**<br>**NOTE** The Chrome accessibility tree contains nodes that go unused on most platforms and by most screen readers. Puppeteer will discard them as well for an easier to process tree, unless `interestingOnly` is set to `false`. |

- [Signature](https://pptr.dev/next/api/puppeteer.accessibility#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.accessibility#remarks)
- [Methods](https://pptr.dev/next/api/puppeteer.accessibility#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Accessibility.snapshot() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.accessibility.snapshot

[Skip to main content](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.accessibility.snapshot)** (24.9.0).



Captures the current state of the accessibility tree. The returned object represents the root accessible node of the page.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Accessibility {
  snapshot(options?: SnapshotOptions): Promise<SerializedAXNode | null>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [SnapshotOptions](https://pptr.dev/next/api/puppeteer.snapshotoptions) | _(Optional)_ |

**Returns:**

Promise< [SerializedAXNode](https://pptr.dev/next/api/puppeteer.serializedaxnode) \| null>

An AXNode object representing the snapshot.

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#remarks "Direct link to Remarks")

**NOTE** The Chrome accessibility tree contains nodes that go unused on most platforms and by most screen readers. Puppeteer will discard them as well for an easier to process tree, unless `interestingOnly` is set to `false`.

## Example 1 [â€‹](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#example-1 "Direct link to Example 1")

An example of dumping the entire accessibility tree:

```codeBlockLines_RjmQ
const snapshot = await page.accessibility.snapshot();
console.log(snapshot);

```

## Example 2 [â€‹](https://pptr.dev/next/api/puppeteer.accessibility.snapshot\#example-2 "Direct link to Example 2")

An example of logging the focused node's name:

```codeBlockLines_RjmQ
const snapshot = await page.accessibility.snapshot();
const node = findFocusedNode(snapshot);
console.log(node && node.name);

function findFocusedNode(node) {
  if (node.focused) return node;
  for (const child of node.children || []) {
    const foundNode = findFocusedNode(child);
    return foundNode;
  }
  return null;
}

```

- [Signature](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#remarks)
- [Example 1](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#example-1)
- [Example 2](https://pptr.dev/next/api/puppeteer.accessibility.snapshot#example-2)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ActionOptions interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.actionoptions

[Skip to main content](https://pptr.dev/next/api/puppeteer.actionoptions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.actionoptions)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.actionoptions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ActionOptions

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.actionoptions\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| signal | `optional` | AbortSignal | A signal to abort the locator action. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.actionoptions#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.actionoptions#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ActionResult type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.actionresult

[Skip to main content](https://pptr.dev/next/api/puppeteer.actionresult#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.actionresult)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.actionresult\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type ActionResult = 'continue' | 'abort' | 'respond';

```

- [Signature](https://pptr.dev/next/api/puppeteer.actionresult#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### AutofillData interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.autofilldata

[Skip to main content](https://pptr.dev/next/api/puppeteer.autofilldata#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.autofilldata)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.autofilldata\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface AutofillData

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.autofilldata\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| creditCard |  | { number: string; name: string; expiryMonth: string; expiryYear: string; cvc: string; } | See [Autofill.CreditCard](https://chromedevtools.github.io/devtools-protocol/tot/Autofill/#type-CreditCard). |  |

- [Signature](https://pptr.dev/next/api/puppeteer.autofilldata#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.autofilldata#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BoundingBox interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.boundingbox

[Skip to main content](https://pptr.dev/next/api/puppeteer.boundingbox#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.boundingbox)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.boundingbox\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface BoundingBox extends Point

```

**Extends:** [Point](https://pptr.dev/next/api/puppeteer.point)

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.boundingbox\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| height |  | number | the height of the element in pixels. |  |
| width |  | number | the width of the element in pixels. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.boundingbox#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.boundingbox#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BoxModel interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.boxmodel

[Skip to main content](https://pptr.dev/next/api/puppeteer.boxmodel#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.boxmodel)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.boxmodel\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface BoxModel

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.boxmodel\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| border |  | [Quad](https://pptr.dev/next/api/puppeteer.quad) |  |  |
| content |  | [Quad](https://pptr.dev/next/api/puppeteer.quad) |  |  |
| height |  | number |  |  |
| margin |  | [Quad](https://pptr.dev/next/api/puppeteer.quad) |  |  |
| padding |  | [Quad](https://pptr.dev/next/api/puppeteer.quad) |  |  |
| width |  | number |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.boxmodel#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.boxmodel#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.browserContexts() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.browsercontexts

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.browsercontexts#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.browsercontexts)** (24.9.0).



Gets a list of open [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).

In a newly-created [browser](https://pptr.dev/next/api/puppeteer.browser), this will return a single instance of [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.browsercontexts\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract browserContexts(): BrowserContext[];
}

```

**Returns:**

[BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext)\[\]

- [Signature](https://pptr.dev/next/api/puppeteer.browser.browsercontexts#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.close() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.close

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.close#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.close)** (24.9.0).



Closes this [browser](https://pptr.dev/next/api/puppeteer.browser) and all associated [pages](https://pptr.dev/next/api/puppeteer.page).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.close\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract close(): Promise<void>;
}

```

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.close#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.cookies() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.cookies

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.cookies#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.cookies)** (24.9.0).



Returns all cookies in the default [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.cookies\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  cookies(): Promise<Cookie[]>;
}

```

**Returns:**

Promise< [Cookie](https://pptr.dev/next/api/puppeteer.cookie)\[\]>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browser.cookies\#remarks "Direct link to Remarks")

Shortcut for [browser.defaultBrowserContext().cookies()](https://pptr.dev/next/api/puppeteer.browsercontext.cookies).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.cookies#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.cookies#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.createBrowserContext() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.createbrowsercontext)** (24.9.0).



Creates a new [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).

This won't share cookies/cache with other [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract createBrowserContext(
    options?: BrowserContextOptions,
  ): Promise<BrowserContext>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [BrowserContextOptions](https://pptr.dev/next/api/puppeteer.browsercontextoptions) | _(Optional)_ |

**Returns:**

Promise< [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext) >

## Example [â€‹](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext\#example "Direct link to Example")

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch();
// Create a new browser context.
const context = await browser.createBrowserContext();
// Create a new page in a pristine context.
const page = await context.newPage();
// Do stuff
await page.goto('https://example.com');

```

- [Signature](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.defaultBrowserContext() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.defaultbrowsercontext)** (24.9.0).



Gets the default [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract defaultBrowserContext(): BrowserContext;
}

```

**Returns:**

[BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext)

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext\#remarks "Direct link to Remarks")

The default [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) cannot be closed.

- [Signature](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.deleteCookie() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.deletecookie

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.deletecookie#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.deletecookie)** (24.9.0).



Removes cookies from the default [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.deletecookie\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  deleteCookie(...cookies: Cookie[]): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browser.deletecookie\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| cookies | [Cookie](https://pptr.dev/next/api/puppeteer.cookie)\[\] |  |

**Returns:**

Promise<void>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browser.deletecookie\#remarks "Direct link to Remarks")

Shortcut for [browser.defaultBrowserContext().deleteCookie()](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.deletecookie#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.deletecookie#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.deletecookie#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.disconnect() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.disconnect

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.disconnect#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.disconnect)** (24.9.0).



Disconnects Puppeteer from this [browser](https://pptr.dev/next/api/puppeteer.browser), but leaves the process running.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.disconnect\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract disconnect(): Promise<void>;
}

```

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.disconnect#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.installExtension() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.installextension

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.installextension#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.installextension)** (24.9.0).



Installs an extension and returns the ID. In Chrome, this is only available if the browser was created using `pipe: true` and the `--enable-unsafe-extension-debugging` flag is set.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.installextension\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract installExtension(path: string): Promise<string>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browser.installextension\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| path | string |  |

**Returns:**

Promise<string>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.installextension#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.installextension#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.isConnected() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.isconnected

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.isconnected#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.isconnected)** (24.9.0).



> Warning: This API is now obsolete.
>
> Use [Browser.connected](https://pptr.dev/next/api/puppeteer.browser).

Whether Puppeteer is connected to this [browser](https://pptr.dev/next/api/puppeteer.browser).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.isconnected\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  isConnected(): boolean;
}

```

**Returns:**

boolean

- [Signature](https://pptr.dev/next/api/puppeteer.browser.isconnected#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser)** (24.9.0).



[Browser](https://pptr.dev/next/api/puppeteer.browser) represents a browser instance that is either:

- connected to via [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect) or - launched by [PuppeteerNode.launch()](https://pptr.dev/next/api/puppeteer.puppeteernode.launch).

[Browser](https://pptr.dev/next/api/puppeteer.browser) [emits](https://pptr.dev/next/api/puppeteer.eventemitter.emit) various events which are documented in the [BrowserEvent](https://pptr.dev/next/api/puppeteer.browserevent) enum.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class Browser extends EventEmitter<BrowserEvents>

```

**Extends:** [EventEmitter](https://pptr.dev/next/api/puppeteer.eventemitter) < [BrowserEvents](https://pptr.dev/next/api/puppeteer.browserevents) >

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browser\#remarks "Direct link to Remarks")

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Browser` class.

## Example 1 [â€‹](https://pptr.dev/next/api/puppeteer.browser\#example-1 "Direct link to Example 1")

Using a [Browser](https://pptr.dev/next/api/puppeteer.browser) to create a [Page](https://pptr.dev/next/api/puppeteer.page):

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';

const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('https://example.com');
await browser.close();

```

## Example 2 [â€‹](https://pptr.dev/next/api/puppeteer.browser\#example-2 "Direct link to Example 2")

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

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.browser\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| connected | `readonly` | boolean | Whether Puppeteer is connected to this [browser](https://pptr.dev/next/api/puppeteer.browser). |
| debugInfo | `readonly` | [DebugInfo](https://pptr.dev/next/api/puppeteer.debuginfo) | **_(Experimental)_** Get debug information from Puppeteer.<br>**Remarks:**<br>Currently, includes pending protocol calls. In the future, we might add more info. |

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.browser\#methods "Direct link to Methods")

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

---

### Browser.newPage() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.newpage

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.newpage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.newpage)** (24.9.0).



Creates a new [page](https://pptr.dev/next/api/puppeteer.page) in the [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.newpage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract newPage(): Promise<Page>;
}

```

**Returns:**

Promise< [Page](https://pptr.dev/next/api/puppeteer.page) >

- [Signature](https://pptr.dev/next/api/puppeteer.browser.newpage#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.pages() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.pages

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.pages#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.pages)** (24.9.0).



Gets a list of all open [pages](https://pptr.dev/next/api/puppeteer.page) inside this [Browser](https://pptr.dev/next/api/puppeteer.browser).

If there are multiple [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext), this returns all [pages](https://pptr.dev/next/api/puppeteer.page) in all [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.pages\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  pages(): Promise<Page[]>;
}

```

**Returns:**

Promise< [Page](https://pptr.dev/next/api/puppeteer.page)\[\]>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browser.pages\#remarks "Direct link to Remarks")

Non-visible [pages](https://pptr.dev/next/api/puppeteer.page), such as `"background_page"`, will not be listed here. You can find them using [Target.page()](https://pptr.dev/next/api/puppeteer.target.page).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.pages#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.pages#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.process() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.process

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.process#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.process)** (24.9.0).



Gets the associated [ChildProcess](https://nodejs.org/api/child_process.html#class-childprocess).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.process\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract process(): ChildProcess | null;
}

```

**Returns:**

ChildProcess \| null

`null` if this instance was connected to via [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.process#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.setCookie() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.setcookie

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.setcookie#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.setcookie)** (24.9.0).



Sets cookies in the default [BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.setcookie\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  setCookie(...cookies: CookieData[]): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browser.setcookie\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| cookies | [CookieData](https://pptr.dev/next/api/puppeteer.cookiedata)\[\] |  |

**Returns:**

Promise<void>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browser.setcookie\#remarks "Direct link to Remarks")

Shortcut for [browser.defaultBrowserContext().setCookie()](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie).

- [Signature](https://pptr.dev/next/api/puppeteer.browser.setcookie#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.setcookie#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.setcookie#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.target() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.target

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.target#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.target)** (24.9.0).



Gets the [target](https://pptr.dev/next/api/puppeteer.target) associated with the [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext)).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.target\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract target(): Target;
}

```

**Returns:**

[Target](https://pptr.dev/next/api/puppeteer.target)

- [Signature](https://pptr.dev/next/api/puppeteer.browser.target#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.targets() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.targets

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.targets#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.targets)** (24.9.0).



Gets all active [targets](https://pptr.dev/next/api/puppeteer.target).

In case of multiple [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext), this returns all [targets](https://pptr.dev/next/api/puppeteer.target) in all [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.targets\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract targets(): Target[];
}

```

**Returns:**

[Target](https://pptr.dev/next/api/puppeteer.target)\[\]

- [Signature](https://pptr.dev/next/api/puppeteer.browser.targets#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.uninstallExtension() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.uninstallextension

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.uninstallextension#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.uninstallextension)** (24.9.0).



Uninstalls an extension. In Chrome, this is only available if the browser was created using `pipe: true` and the `--enable-unsafe-extension-debugging` flag is set.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.uninstallextension\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract uninstallExtension(id: string): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browser.uninstallextension\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| id | string |  |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.uninstallextension#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browser.uninstallextension#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.userAgent() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.useragent

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.useragent#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.useragent)** (24.9.0).



Gets this [browser's](https://pptr.dev/next/api/puppeteer.browser) original user agent.

[Pages](https://pptr.dev/next/api/puppeteer.page) can override the user agent with [Page.setUserAgent()](https://pptr.dev/next/api/puppeteer.page.setuseragent).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.useragent\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract userAgent(): Promise<string>;
}

```

**Returns:**

Promise<string>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.useragent#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.version() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.version

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.version#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.version)** (24.9.0).



Gets a string representing this [browser's](https://pptr.dev/next/api/puppeteer.browser) name and version.

For headless browser, this is similar to `"HeadlessChrome/61.0.3153.0"`. For non-headless or new-headless, this is similar to `"Chrome/61.0.3153.0"`. For Firefox, it is similar to `"Firefox/116.0a1"`.

The format of [Browser.version()](https://pptr.dev/next/api/puppeteer.browser.version) might change with future releases of browsers.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.version\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract version(): Promise<string>;
}

```

**Returns:**

Promise<string>

- [Signature](https://pptr.dev/next/api/puppeteer.browser.version#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Browser.wsEndpoint() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browser.wsendpoint

[Skip to main content](https://pptr.dev/next/api/puppeteer.browser.wsendpoint#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browser.wsendpoint)** (24.9.0).



Gets the WebSocket URL to connect to this [browser](https://pptr.dev/next/api/puppeteer.browser).

This is usually used with [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect).

You can find the debugger URL ( `webSocketDebuggerUrl`) from `http://HOST:PORT/json/version`.

See [browser endpoint](https://chromedevtools.github.io/devtools-protocol/#how-do-i-access-the-browser-target) for more information.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browser.wsendpoint\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Browser {
  abstract wsEndpoint(): string;
}

```

**Returns:**

string

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browser.wsendpoint\#remarks "Direct link to Remarks")

The format is always `ws://HOST:PORT/devtools/browser/<id>`.

- [Signature](https://pptr.dev/next/api/puppeteer.browser.wsendpoint#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browser.wsendpoint#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.browser() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.browser

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.browser#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.browser)** (24.9.0).



Gets the [browser](https://pptr.dev/next/api/puppeteer.browser) associated with this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.browser\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract browser(): Browser;
}

```

**Returns:**

[Browser](https://pptr.dev/next/api/puppeteer.browser)

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.browser#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.clearPermissionOverrides() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.clearpermissionoverrides)** (24.9.0).



Clears all permission overrides for this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract clearPermissionOverrides(): Promise<void>;
}

```

**Returns:**

Promise<void>

## Example [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides\#example "Direct link to Example")

Clearing overridden permissions in the [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext):

```codeBlockLines_RjmQ
const context = browser.defaultBrowserContext();
context.overridePermissions('https://example.com', ['clipboard-read']);
// do stuff ..
context.clearPermissionOverrides();

```

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides#signature)
- [Example](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.close() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.close

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.close#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.close)** (24.9.0).



Closes this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) and all associated [pages](https://pptr.dev/next/api/puppeteer.page).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.close\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract close(): Promise<void>;
}

```

**Returns:**

Promise<void>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.close\#remarks "Direct link to Remarks")

The [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext) cannot be closed.

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.close#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browsercontext.close#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.cookies() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.cookies

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.cookies#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.cookies)** (24.9.0).



Gets all cookies in the browser context.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.cookies\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract cookies(): Promise<Cookie[]>;
}

```

**Returns:**

Promise< [Cookie](https://pptr.dev/next/api/puppeteer.cookie)\[\]>

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.cookies#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.deleteCookie() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.deletecookie)** (24.9.0).



Removes cookie in the browser context

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  deleteCookie(...cookies: Cookie[]): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| cookies | [Cookie](https://pptr.dev/next/api/puppeteer.cookie)\[\] | [cookie](https://pptr.dev/next/api/puppeteer.cookie) to remove |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext)** (24.9.0).



[BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext) represents individual user contexts within a [browser](https://pptr.dev/next/api/puppeteer.browser).

When a [browser](https://pptr.dev/next/api/puppeteer.browser) is launched, it has at least one default [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). Others can be created using [Browser.createBrowserContext()](https://pptr.dev/next/api/puppeteer.browser.createbrowsercontext). Each context has isolated storage (cookies/localStorage/etc.)

[BrowserContext](https://pptr.dev/next/api/puppeteer.browsercontext) [emits](https://pptr.dev/next/api/puppeteer.eventemitter) various events which are documented in the [BrowserContextEvent](https://pptr.dev/next/api/puppeteer.browsercontextevent) enum.

If a [page](https://pptr.dev/next/api/puppeteer.page) opens another [page](https://pptr.dev/next/api/puppeteer.page), e.g. using `window.open`, the popup will belong to the parent [page's browser context](https://pptr.dev/next/api/puppeteer.page.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class BrowserContext extends EventEmitter<BrowserContextEvents>

```

**Extends:** [EventEmitter](https://pptr.dev/next/api/puppeteer.eventemitter) < [BrowserContextEvents](https://pptr.dev/next/api/puppeteer.browsercontextevents) >

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext\#remarks "Direct link to Remarks")

In Chrome all non-default contexts are incognito, and [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext) might be incognito if you provide the `--incognito` argument when launching the browser.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `BrowserContext` class.

## Example [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext\#example "Direct link to Example")

Creating a new [browser context](https://pptr.dev/next/api/puppeteer.browsercontext):

```codeBlockLines_RjmQ
// Create a new browser context
const context = await browser.createBrowserContext();
// Create a new page inside context.
const page = await context.newPage();
// ... do stuff with page ...
await page.goto('https://example.com');
// Dispose context once it's no longer needed.
await context.close();

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| closed | `readonly` | boolean | Whether this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) is closed. |
| id | `readonly` | string \| undefined | Identifier for this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [browser()](https://pptr.dev/next/api/puppeteer.browsercontext.browser) |  | Gets the [browser](https://pptr.dev/next/api/puppeteer.browser) associated with this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [clearPermissionOverrides()](https://pptr.dev/next/api/puppeteer.browsercontext.clearpermissionoverrides) |  | Clears all permission overrides for this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [close()](https://pptr.dev/next/api/puppeteer.browsercontext.close) |  | Closes this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) and all associated [pages](https://pptr.dev/next/api/puppeteer.page).<br>**Remarks:**<br>The [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext) cannot be closed. |
| [cookies()](https://pptr.dev/next/api/puppeteer.browsercontext.cookies) |  | Gets all cookies in the browser context. |
| [deleteCookie(cookies)](https://pptr.dev/next/api/puppeteer.browsercontext.deletecookie) |  | Removes cookie in the browser context |
| [newPage()](https://pptr.dev/next/api/puppeteer.browsercontext.newpage) |  | Creates a new [page](https://pptr.dev/next/api/puppeteer.page) in this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [overridePermissions(origin, permissions)](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions) |  | Grants this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) the given `permissions` within the given `origin`. |
| [pages()](https://pptr.dev/next/api/puppeteer.browsercontext.pages) |  | Gets a list of all open [pages](https://pptr.dev/next/api/puppeteer.page) inside this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).<br>**Remarks:**<br>Non-visible [pages](https://pptr.dev/next/api/puppeteer.page), such as `"background_page"`, will not be listed here. You can find them using [Target.page()](https://pptr.dev/next/api/puppeteer.target.page). |
| [setCookie(cookies)](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie) |  | Sets a cookie in the browser context. |
| [targets()](https://pptr.dev/next/api/puppeteer.browsercontext.targets) |  | Gets all active [targets](https://pptr.dev/next/api/puppeteer.target) inside this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext). |
| [waitForTarget(predicate, options)](https://pptr.dev/next/api/puppeteer.browsercontext.waitfortarget) |  | Waits until a [target](https://pptr.dev/next/api/puppeteer.target) matching the given `predicate` appears and returns it.<br>This will look all open [browser contexts](https://pptr.dev/next/api/puppeteer.browsercontext). |

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browsercontext#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.browsercontext#example)
- [Properties](https://pptr.dev/next/api/puppeteer.browsercontext#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.browsercontext#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.newPage() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.newpage

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.newpage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.newpage)** (24.9.0).



Creates a new [page](https://pptr.dev/next/api/puppeteer.page) in this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.newpage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract newPage(): Promise<Page>;
}

```

**Returns:**

Promise< [Page](https://pptr.dev/next/api/puppeteer.page) >

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.newpage#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.overridePermissions() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.overridepermissions)** (24.9.0).



Grants this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext) the given `permissions` within the given `origin`.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract overridePermissions(
    origin: string,
    permissions: Permission[],
  ): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| origin | string | The origin to grant permissions to, e.g. " [https://example.com](https://example.com/)". |
| permissions | [Permission](https://pptr.dev/next/api/puppeteer.permission)\[\] | An array of permissions to grant. All permissions that are not listed here will be automatically denied. |

**Returns:**

Promise<void>

## Example [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions\#example "Direct link to Example")

Overriding permissions in the [default browser context](https://pptr.dev/next/api/puppeteer.browser.defaultbrowsercontext):

```codeBlockLines_RjmQ
const context = browser.defaultBrowserContext();
await context.overridePermissions('https://html5demos.com', ['geolocation']);

```

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.browsercontext.overridepermissions#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.pages() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.pages

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.pages#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.pages)** (24.9.0).



Gets a list of all open [pages](https://pptr.dev/next/api/puppeteer.page) inside this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.pages\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract pages(): Promise<Page[]>;
}

```

**Returns:**

Promise< [Page](https://pptr.dev/next/api/puppeteer.page)\[\]>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.pages\#remarks "Direct link to Remarks")

Non-visible [pages](https://pptr.dev/next/api/puppeteer.page), such as `"background_page"`, will not be listed here. You can find them using [Target.page()](https://pptr.dev/next/api/puppeteer.target.page).

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.pages#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browsercontext.pages#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.setCookie() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.setcookie

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.setcookie)** (24.9.0).



Sets a cookie in the browser context.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract setCookie(...cookies: CookieData[]): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| cookies | [CookieData](https://pptr.dev/next/api/puppeteer.cookiedata)\[\] |  |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browsercontext.setcookie#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContext.targets() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontext.targets

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontext.targets#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontext.targets)** (24.9.0).



Gets all active [targets](https://pptr.dev/next/api/puppeteer.target) inside this [browser context](https://pptr.dev/next/api/puppeteer.browsercontext).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontext.targets\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserContext {
  abstract targets(): Target[];
}

```

**Returns:**

[Target](https://pptr.dev/next/api/puppeteer.target)\[\]

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontext.targets#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContextEvent enum | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontextevent

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontextevent#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontextevent)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontextevent\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare const enum BrowserContextEvent

```

## Enumeration Members [â€‹](https://pptr.dev/next/api/puppeteer.browsercontextevent\#enumeration-members "Direct link to Enumeration Members")

| Member | Value | Description |
| --- | --- | --- |
| TargetChanged | `"targetchanged"` | Emitted when the url of a target inside the browser context changes. Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance. |
| TargetCreated | `"targetcreated"` | Emitted when a target is created within the browser context, for example when a new page is opened by [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) or by [browserContext.newPage](https://pptr.dev/next/api/puppeteer.browsercontext.newpage)<br>Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance. |
| TargetDestroyed | `"targetdestroyed"` | Emitted when a target is destroyed within the browser context, for example when a page is closed. Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance. |

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontextevent#signature)
- [Enumeration Members](https://pptr.dev/next/api/puppeteer.browsercontextevent#enumeration-members)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContextEvents interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontextevents

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontextevents#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontextevents)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontextevents\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface BrowserContextEvents extends Record<EventType, unknown>

```

**Extends:** Record< [EventType](https://pptr.dev/next/api/puppeteer.eventtype), unknown>

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.browsercontextevents\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| targetchanged |  | [Target](https://pptr.dev/next/api/puppeteer.target) |  |  |
| targetcreated |  | [Target](https://pptr.dev/next/api/puppeteer.target) |  |  |
| targetdestroyed |  | [Target](https://pptr.dev/next/api/puppeteer.target) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontextevents#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.browsercontextevents#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserContextOptions interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browsercontextoptions

[Skip to main content](https://pptr.dev/next/api/puppeteer.browsercontextoptions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browsercontextoptions)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browsercontextoptions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface BrowserContextOptions

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.browsercontextoptions\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| downloadBehavior | `optional` | [DownloadBehavior](https://pptr.dev/next/api/puppeteer.downloadbehavior) | Behavior definition for when downloading a file.<br>**Remarks:**<br>If not set, the default behavior will be used. |  |
| proxyBypassList | `optional` | string\[\] | Bypass the proxy for the given list of hosts. |  |
| proxyServer | `optional` | string | Proxy server with optional port to use for all requests. Username and password can be set in `Page.authenticate`. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.browsercontextoptions#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.browsercontextoptions#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserEvent enum | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browserevent

[Skip to main content](https://pptr.dev/next/api/puppeteer.browserevent#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browserevent)** (24.9.0).



All the events a [browser instance](https://pptr.dev/next/api/puppeteer.browser) may emit.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browserevent\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare const enum BrowserEvent

```

## Enumeration Members [â€‹](https://pptr.dev/next/api/puppeteer.browserevent\#enumeration-members "Direct link to Enumeration Members")

| Member | Value | Description |
| --- | --- | --- |
| Disconnected | `"disconnected"` | Emitted when Puppeteer gets disconnected from the browser instance. This might happen because either:<br>- The browser closes/crashes or - [Browser.disconnect()](https://pptr.dev/next/api/puppeteer.browser.disconnect) was called. |
| TargetChanged | `"targetchanged"` | Emitted when the URL of a target changes. Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance.<br>**Remarks:**<br>Note that this includes target changes in all browser contexts. |
| TargetCreated | `"targetcreated"` | Emitted when a target is created, for example when a new page is opened by [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) or by [browser.newPage](https://pptr.dev/next/api/puppeteer.browser.newpage)<br>Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance.<br>**Remarks:**<br>Note that this includes target creations in all browser contexts. |
| TargetDestroyed | `"targetdestroyed"` | Emitted when a target is destroyed, for example when a page is closed. Contains a [Target](https://pptr.dev/next/api/puppeteer.target) instance.<br>**Remarks:**<br>Note that this includes target destructions in all browser contexts. |

- [Signature](https://pptr.dev/next/api/puppeteer.browserevent#signature)
- [Enumeration Members](https://pptr.dev/next/api/puppeteer.browserevent#enumeration-members)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserEvents interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browserevents

[Skip to main content](https://pptr.dev/next/api/puppeteer.browserevents#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browserevents)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browserevents\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface BrowserEvents extends Record<EventType, unknown>

```

**Extends:** Record< [EventType](https://pptr.dev/next/api/puppeteer.eventtype), unknown>

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.browserevents\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| disconnected |  | undefined |  |  |
| targetchanged |  | [Target](https://pptr.dev/next/api/puppeteer.target) |  |  |
| targetcreated |  | [Target](https://pptr.dev/next/api/puppeteer.target) |  |  |
| targetdestroyed |  | [Target](https://pptr.dev/next/api/puppeteer.target) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.browserevents#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.browserevents#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserLauncher.defaultArgs() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browserlauncher.defaultargs

[Skip to main content](https://pptr.dev/next/api/puppeteer.browserlauncher.defaultargs#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browserlauncher.defaultargs)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher.defaultargs\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserLauncher {
  abstract defaultArgs(object: LaunchOptions): string[];
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher.defaultargs\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| object | [LaunchOptions](https://pptr.dev/next/api/puppeteer.launchoptions) |  |

**Returns:**

string\[\]

- [Signature](https://pptr.dev/next/api/puppeteer.browserlauncher.defaultargs#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browserlauncher.defaultargs#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserLauncher.executablePath() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browserlauncher.executablepath

[Skip to main content](https://pptr.dev/next/api/puppeteer.browserlauncher.executablepath#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browserlauncher.executablepath)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher.executablepath\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserLauncher {
  abstract executablePath(
    channel?: ChromeReleaseChannel,
    validatePath?: boolean,
  ): string;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher.executablepath\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| channel | [ChromeReleaseChannel](https://pptr.dev/next/api/puppeteer.chromereleasechannel) | _(Optional)_ |
| validatePath | boolean | _(Optional)_ |

**Returns:**

string

- [Signature](https://pptr.dev/next/api/puppeteer.browserlauncher.executablepath#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browserlauncher.executablepath#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserLauncher.launch() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browserlauncher.launch

[Skip to main content](https://pptr.dev/next/api/puppeteer.browserlauncher.launch#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browserlauncher.launch)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher.launch\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class BrowserLauncher {
  launch(options?: LaunchOptions): Promise<Browser>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher.launch\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [LaunchOptions](https://pptr.dev/next/api/puppeteer.launchoptions) | _(Optional)_ |

**Returns:**

Promise< [Browser](https://pptr.dev/next/api/puppeteer.browser) >

- [Signature](https://pptr.dev/next/api/puppeteer.browserlauncher.launch#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.browserlauncher.launch#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### BrowserLauncher class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.browserlauncher

[Skip to main content](https://pptr.dev/next/api/puppeteer.browserlauncher#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.browserlauncher)** (24.9.0).



Describes a launcher - a class that is able to create and launch a browser instance.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class BrowserLauncher

```

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher\#remarks "Direct link to Remarks")

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `BrowserLauncher` class.

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| browser | `readonly` | [SupportedBrowser](https://pptr.dev/next/api/puppeteer.supportedbrowser) |  |

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.browserlauncher\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [defaultArgs(object)](https://pptr.dev/next/api/puppeteer.browserlauncher.defaultargs) |  |  |
| [executablePath(channel, validatePath)](https://pptr.dev/next/api/puppeteer.browserlauncher.executablepath) |  |  |
| [launch(options)](https://pptr.dev/next/api/puppeteer.browserlauncher.launch) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.browserlauncher#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.browserlauncher#remarks)
- [Properties](https://pptr.dev/next/api/puppeteer.browserlauncher#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.browserlauncher#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPEvents type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpevents

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpevents#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpevents)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpevents\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type CDPEvents = {
  [Property in keyof ProtocolMapping.Events]: ProtocolMapping.Events[Property][0];
};

```

- [Signature](https://pptr.dev/next/api/puppeteer.cdpevents#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPSession.connection() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpsession.connection

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsession.connection#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsession.connection)** (24.9.0).



The underlying connection for this session, if any.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession.connection\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class CDPSession {
  abstract connection(): Connection | undefined;
}

```

**Returns:**

[Connection](https://pptr.dev/next/api/puppeteer.connection) \| undefined

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsession.connection#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPSession.detach() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpsession.detach

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsession.detach#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsession.detach)** (24.9.0).



Detaches the cdpSession from the target. Once detached, the cdpSession object won't emit any events and can't be used to send messages.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession.detach\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class CDPSession {
  abstract detach(): Promise<void>;
}

```

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsession.detach#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPSession.id() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpsession.id

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsession.id#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsession.id)** (24.9.0).



Returns the session's id.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession.id\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class CDPSession {
  abstract id(): string;
}

```

**Returns:**

string

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsession.id#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPSession class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpsession

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsession#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsession)** (24.9.0).



The `CDPSession` instances are used to talk raw Chrome Devtools Protocol.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class CDPSession extends EventEmitter<CDPSessionEvents>

```

**Extends:** [EventEmitter](https://pptr.dev/next/api/puppeteer.eventemitter) < [CDPSessionEvents](https://pptr.dev/next/api/puppeteer.cdpsessionevents) >

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession\#remarks "Direct link to Remarks")

Protocol methods can be called with [CDPSession.send()](https://pptr.dev/next/api/puppeteer.cdpsession.send) method and protocol events can be subscribed to with `CDPSession.on` method.

Useful links: [DevTools Protocol Viewer](https://chromedevtools.github.io/devtools-protocol/) and [Getting Started with DevTools Protocol](https://github.com/aslushnikov/getting-started-with-cdp/blob/HEAD/README.md).

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `CDPSession` class.

## Example [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession\#example "Direct link to Example")

```codeBlockLines_RjmQ
const client = await page.createCDPSession();
await client.send('Animation.enable');
client.on('Animation.animationCreated', () =>
  console.log('Animation created!'),
);
const response = await client.send('Animation.getPlaybackRate');
console.log('playback rate is ' + response.playbackRate);
await client.send('Animation.setPlaybackRate', {
  playbackRate: response.playbackRate / 2,
});

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| detached | `readonly` | boolean | True if the session has been detached, false otherwise. |

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [connection()](https://pptr.dev/next/api/puppeteer.cdpsession.connection) |  | The underlying connection for this session, if any. |
| [detach()](https://pptr.dev/next/api/puppeteer.cdpsession.detach) |  | Detaches the cdpSession from the target. Once detached, the cdpSession object won't emit any events and can't be used to send messages. |
| [id()](https://pptr.dev/next/api/puppeteer.cdpsession.id) |  | Returns the session's id. |
| [send(method, params, options)](https://pptr.dev/next/api/puppeteer.cdpsession.send) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsession#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.cdpsession#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.cdpsession#example)
- [Properties](https://pptr.dev/next/api/puppeteer.cdpsession#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.cdpsession#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPSession.send() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpsession.send

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsession.send#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsession.send)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession.send\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class CDPSession {
  abstract send<T extends keyof ProtocolMapping.Commands>(
    method: T,
    params?: ProtocolMapping.Commands[T]['paramsType'][0],
    options?: CommandOptions,
  ): Promise<ProtocolMapping.Commands[T]['returnType']>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.cdpsession.send\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| method | T |  |
| params | ProtocolMapping.Commands\[T\]\['paramsType'\]\[0\] | _(Optional)_ |
| options | [CommandOptions](https://pptr.dev/next/api/puppeteer.commandoptions) | _(Optional)_ |

**Returns:**

Promise<ProtocolMapping.Commands\[T\]\['returnType'\]>

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsession.send#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.cdpsession.send#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPSessionEvent namespace | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpsessionevent

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsessionevent#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsessionevent)** (24.9.0).



Events that the CDPSession class emits.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpsessionevent\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare namespace CDPSessionEvent

```

## Variables [â€‹](https://pptr.dev/next/api/puppeteer.cdpsessionevent\#variables "Direct link to Variables")

| Variable | Description |
| --- | --- |
| [SessionAttached](https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessionattached) |  |
| [SessionDetached](https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessiondetached) |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsessionevent#signature)
- [Variables](https://pptr.dev/next/api/puppeteer.cdpsessionevent#variables)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPSessionEvent.SessionAttached variable | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessionattached

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessionattached#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsessionevent.sessionattached)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessionattached\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
SessionAttached: 'sessionattached';

```

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessionattached#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPSessionEvent.SessionDetached variable | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessiondetached

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessiondetached#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsessionevent.sessiondetached)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessiondetached\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
SessionDetached: 'sessiondetached';

```

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsessionevent.sessiondetached#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CDPSessionEvents interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cdpsessionevents

[Skip to main content](https://pptr.dev/next/api/puppeteer.cdpsessionevents#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cdpsessionevents)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cdpsessionevents\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CDPSessionEvents extends CDPEvents, Record<EventType, unknown>

```

**Extends:** [CDPEvents](https://pptr.dev/next/api/puppeteer.cdpevents), Record< [EventType](https://pptr.dev/next/api/puppeteer.eventtype), unknown>

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.cdpsessionevents\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| sessionattached |  | [CDPSession](https://pptr.dev/next/api/puppeteer.cdpsession) |  |  |
| sessiondetached |  | [CDPSession](https://pptr.dev/next/api/puppeteer.cdpsession) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cdpsessionevents#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.cdpsessionevents#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ChromeHeadlessShellSettings interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.chromeheadlessshellsettings

[Skip to main content](https://pptr.dev/next/api/puppeteer.chromeheadlessshellsettings#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.chromeheadlessshellsettings)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.chromeheadlessshellsettings\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ChromeHeadlessShellSettings

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.chromeheadlessshellsettings\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| downloadBaseUrl | `optional` | string | Specifies the URL prefix that is used to download the browser.<br>Can be overridden by `PUPPETEER_CHROME_HEADLESS_SHELL_DOWNLOAD_BASE_URL`.<br>**Remarks:**<br>This must include the protocol and may even need a path prefix. This must **not** include a trailing slash similar to the default. | [https://storage.googleapis.com/chrome-for-testing-public](https://storage.googleapis.com/chrome-for-testing-public) |
| skipDownload | `optional` | boolean | Tells Puppeteer to not download the browser during installation.<br>Can be overridden by `PUPPETEER_CHROME_HEADLESS_SHELL_SKIP_DOWNLOAD` or `PUPPETEER_SKIP_CHROME_HEADLESS_SHELL_DOWNLOAD`. | false |
| version | `optional` | string | Specifies a certain version of the browser you'd like Puppeteer to use.<br>Can be overridden by `PUPPETEER_CHROME_HEADLESS_SHELL_VERSION`.<br>See [puppeteer.launch](https://pptr.dev/next/api/puppeteer.puppeteernode.launch) on how executable path is inferred. | The pinned browser version supported by the current Puppeteer version. |

- [Signature](https://pptr.dev/next/api/puppeteer.chromeheadlessshellsettings#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.chromeheadlessshellsettings#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ChromeSettings interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.chromesettings

[Skip to main content](https://pptr.dev/next/api/puppeteer.chromesettings#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.chromesettings)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.chromesettings\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ChromeSettings

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.chromesettings\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| downloadBaseUrl | `optional` | string | Specifies the URL prefix that is used to download the browser.<br>Can be overridden by `PUPPETEER_CHROME_DOWNLOAD_BASE_URL`.<br>**Remarks:**<br>This must include the protocol and may even need a path prefix. This must **not** include a trailing slash similar to the default. | [https://storage.googleapis.com/chrome-for-testing-public](https://storage.googleapis.com/chrome-for-testing-public) |
| skipDownload | `optional` | boolean | Tells Puppeteer to not download the browser during installation.<br>Can be overridden by `PUPPETEER_CHROME_SKIP_DOWNLOAD`. | false |
| version | `optional` | string | Specifies a certain version of the browser you'd like Puppeteer to use.<br>Can be overridden by `PUPPETEER_CHROME_VERSION` or `PUPPETEER_SKIP_CHROME_DOWNLOAD`.<br>See [puppeteer.launch](https://pptr.dev/next/api/puppeteer.puppeteernode.launch) on how executable path is inferred. | The pinned browser version supported by the current Puppeteer version. |

- [Signature](https://pptr.dev/next/api/puppeteer.chromesettings#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.chromesettings#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ClickOptions interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.clickoptions

[Skip to main content](https://pptr.dev/next/api/puppeteer.clickoptions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.clickoptions)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.clickoptions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ClickOptions extends MouseClickOptions

```

**Extends:** [MouseClickOptions](https://pptr.dev/next/api/puppeteer.mouseclickoptions)

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.clickoptions\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| offset | `optional` | [Offset](https://pptr.dev/next/api/puppeteer.offset) | Offset for the clickable point relative to the top-left corner of the border box. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.clickoptions#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.clickoptions#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CommandOptions interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.commandoptions

[Skip to main content](https://pptr.dev/next/api/puppeteer.commandoptions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commandoptions)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.commandoptions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CommandOptions

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.commandoptions\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| timeout |  | number |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.commandoptions#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.commandoptions#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CommonEventEmitter.emit() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.commoneventemitter.emit

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.emit)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  emit<Key extends keyof Events>(type: Key, event: Events[Key]): boolean;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| type | Key |  |
| event | Events\[Key\] |  |

**Returns:**

boolean

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CommonEventEmitter.listenerCount() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.commoneventemitter.listenercount

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.listenercount#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.listenercount)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.listenercount\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  listenerCount(event: keyof Events): number;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.listenercount\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| event | keyof Events |  |

**Returns:**

number

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.listenercount#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.listenercount#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CommonEventEmitter interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.commoneventemitter

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CommonEventEmitter<Events extends Record<EventType, unknown>>

```

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter\#methods "Direct link to Methods")

| Method | Description |
| --- | --- |
| [emit(type, event)](https://pptr.dev/next/api/puppeteer.commoneventemitter.emit) |  |
| [listenerCount(event)](https://pptr.dev/next/api/puppeteer.commoneventemitter.listenercount) |  |
| [off(type, handler)](https://pptr.dev/next/api/puppeteer.commoneventemitter.off) |  |
| [on(type, handler)](https://pptr.dev/next/api/puppeteer.commoneventemitter.on) |  |
| [once(type, handler)](https://pptr.dev/next/api/puppeteer.commoneventemitter.once) |  |
| [removeAllListeners(event)](https://pptr.dev/next/api/puppeteer.commoneventemitter.removealllisteners) |  |

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter#signature)
- [Methods](https://pptr.dev/next/api/puppeteer.commoneventemitter#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CommonEventEmitter.off() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.commoneventemitter.off

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.off#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.off)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.off\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  off<Key extends keyof Events>(
    type: Key,
    handler?: Handler<Events[Key]>,
  ): this;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.off\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| type | Key |  |
| handler | [Handler](https://pptr.dev/next/api/puppeteer.handler) <Events\[Key\]> | _(Optional)_ |

**Returns:**

this

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.off#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.off#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CommonEventEmitter.on() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.commoneventemitter.on

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.on#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.on)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.on\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  on<Key extends keyof Events>(type: Key, handler: Handler<Events[Key]>): this;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.on\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| type | Key |  |
| handler | [Handler](https://pptr.dev/next/api/puppeteer.handler) <Events\[Key\]> |  |

**Returns:**

this

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.on#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.on#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CommonEventEmitter.once() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.commoneventemitter.once

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.once#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.once)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.once\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  once<Key extends keyof Events>(
    type: Key,
    handler: Handler<Events[Key]>,
  ): this;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.once\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| type | Key |  |
| handler | [Handler](https://pptr.dev/next/api/puppeteer.handler) <Events\[Key\]> |  |

**Returns:**

this

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.once#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.once#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CommonEventEmitter.removeAllListeners() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.commoneventemitter.removealllisteners

[Skip to main content](https://pptr.dev/next/api/puppeteer.commoneventemitter.removealllisteners#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.commoneventemitter.removealllisteners)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.removealllisteners\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface CommonEventEmitter {
  removeAllListeners(event?: keyof Events): this;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.commoneventemitter.removealllisteners\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| event | keyof Events | _(Optional)_ |

**Returns:**

this

- [Signature](https://pptr.dev/next/api/puppeteer.commoneventemitter.removealllisteners#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.commoneventemitter.removealllisteners#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Configuration interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.configuration

[Skip to main content](https://pptr.dev/next/api/puppeteer.configuration#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.configuration)** (24.9.0).



Defines options to configure Puppeteer's behavior during installation and runtime.

See individual properties for more information.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.configuration\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface Configuration

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.configuration\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| "chrome-headless-shell" | `optional` | [ChromeHeadlessShellSettings](https://pptr.dev/next/api/puppeteer.chromeheadlessshellsettings) |  |  |
| cacheDirectory | `optional` | string | Defines the directory to be used by Puppeteer for caching.<br>Can be overridden by `PUPPETEER_CACHE_DIR`. | `path.join(os.homedir(), '.cache', 'puppeteer')` |
| chrome | `optional` | [ChromeSettings](https://pptr.dev/next/api/puppeteer.chromesettings) |  |  |
| defaultBrowser | `optional` | [SupportedBrowser](https://pptr.dev/next/api/puppeteer.supportedbrowser) | Specifies which browser you'd like Puppeteer to use.<br>Can be overridden by `PUPPETEER_BROWSER`. | `chrome` |
| executablePath | `optional` | string | Specifies an executable path to be used in [puppeteer.launch](https://pptr.dev/next/api/puppeteer.puppeteernode.launch).<br>Can be overridden by `PUPPETEER_EXECUTABLE_PATH`. | **Auto-computed.** |
| experiments | `optional` | [ExperimentsConfiguration](https://pptr.dev/next/api/puppeteer.experimentsconfiguration) | Defines experimental options for Puppeteer. |  |
| firefox | `optional` | [FirefoxSettings](https://pptr.dev/next/api/puppeteer.firefoxsettings) |  |  |
| logLevel | `optional` | 'silent' \| 'error' \| 'warn' | Tells Puppeteer to log at the given level. | `warn` |
| skipDownload | `optional` | boolean | Tells Puppeteer to not download during installation.<br>Can be overridden by `PUPPETEER_SKIP_DOWNLOAD`. |  |
| temporaryDirectory | `optional` | string | Defines the directory to be used by Puppeteer for creating temporary files.<br>Can be overridden by `PUPPETEER_TMP_DIR`. | `os.tmpdir()` |

- [Signature](https://pptr.dev/next/api/puppeteer.configuration#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.configuration#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### connect() function | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connect

[Skip to main content](https://pptr.dev/next/api/puppeteer.connect#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connect)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connect\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
connect: (options: PuppeteerCore.ConnectOptions) =>
  Promise<PuppeteerCore.Browser>;

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.connect\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [PuppeteerCore.ConnectOptions](https://pptr.dev/next/api/puppeteer.connectoptions) |  |

**Returns:**

Promise< [PuppeteerCore.Browser](https://pptr.dev/next/api/puppeteer.browser) >

- [Signature](https://pptr.dev/next/api/puppeteer.connect#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.connect#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Connection.(constructor) | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connection._constructor_

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection._constructor_#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection._constructor_)** (24.9.0).



Constructs a new instance of the `Connection` class

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connection._constructor_\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Connection {
  constructor(
    url: string,
    transport: ConnectionTransport,
    delay?: number,
    timeout?: number,
    rawErrors?: boolean,
  );
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.connection._constructor_\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| url | string |  |
| transport | [ConnectionTransport](https://pptr.dev/next/api/puppeteer.connectiontransport) |  |
| delay | number | _(Optional)_ |
| timeout | number | _(Optional)_ |
| rawErrors | boolean | _(Optional)_ |

- [Signature](https://pptr.dev/next/api/puppeteer.connection._constructor_#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.connection._constructor_#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Connection.createSession() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connection.createsession

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection.createsession#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection.createsession)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connection.createsession\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Connection {
  createSession(targetInfo: Protocol.Target.TargetInfo): Promise<CDPSession>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.connection.createsession\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| targetInfo | Protocol.Target.TargetInfo | The target info |

**Returns:**

Promise< [CDPSession](https://pptr.dev/next/api/puppeteer.cdpsession) >

The CDP session that is created

- [Signature](https://pptr.dev/next/api/puppeteer.connection.createsession#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.connection.createsession#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Connection.dispose() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connection.dispose

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection.dispose#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection.dispose)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connection.dispose\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Connection {
  dispose(): void;
}

```

**Returns:**

void

- [Signature](https://pptr.dev/next/api/puppeteer.connection.dispose#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Connection.fromSession() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connection.fromsession

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection.fromsession#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection.fromsession)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connection.fromsession\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Connection {
  static fromSession(session: CDPSession): Connection | undefined;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.connection.fromsession\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| session | [CDPSession](https://pptr.dev/next/api/puppeteer.cdpsession) |  |

**Returns:**

[Connection](https://pptr.dev/next/api/puppeteer.connection) \| undefined

- [Signature](https://pptr.dev/next/api/puppeteer.connection.fromsession#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.connection.fromsession#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Connection class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connection

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connection\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class Connection extends EventEmitter<CDPSessionEvents>

```

**Extends:** [EventEmitter](https://pptr.dev/next/api/puppeteer.eventemitter) < [CDPSessionEvents](https://pptr.dev/next/api/puppeteer.cdpsessionevents) >

## Constructors [â€‹](https://pptr.dev/next/api/puppeteer.connection\#constructors "Direct link to Constructors")

| Constructor | Modifiers | Description |
| --- | --- | --- |
| [(constructor)(url, transport, delay, timeout, rawErrors)](https://pptr.dev/next/api/puppeteer.connection._constructor_) |  | Constructs a new instance of the `Connection` class |

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.connection\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| timeout | `readonly` | number |  |

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.connection\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [createSession(targetInfo)](https://pptr.dev/next/api/puppeteer.connection.createsession) |  |  |
| [dispose()](https://pptr.dev/next/api/puppeteer.connection.dispose) |  |  |
| [fromSession(session)](https://pptr.dev/next/api/puppeteer.connection.fromsession) | `static` |  |
| [send(method, params, options)](https://pptr.dev/next/api/puppeteer.connection.send) |  |  |
| [session(sessionId)](https://pptr.dev/next/api/puppeteer.connection.session) |  |  |
| [url()](https://pptr.dev/next/api/puppeteer.connection.url) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.connection#signature)
- [Constructors](https://pptr.dev/next/api/puppeteer.connection#constructors)
- [Properties](https://pptr.dev/next/api/puppeteer.connection#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.connection#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Connection.send() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connection.send

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection.send#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection.send)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connection.send\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Connection {
  send<T extends keyof ProtocolMapping.Commands>(
    method: T,
    params?: ProtocolMapping.Commands[T]['paramsType'][0],
    options?: CommandOptions,
  ): Promise<ProtocolMapping.Commands[T]['returnType']>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.connection.send\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| method | T |  |
| params | ProtocolMapping.Commands\[T\]\['paramsType'\]\[0\] | _(Optional)_ |
| options | [CommandOptions](https://pptr.dev/next/api/puppeteer.commandoptions) | _(Optional)_ |

**Returns:**

Promise<ProtocolMapping.Commands\[T\]\['returnType'\]>

- [Signature](https://pptr.dev/next/api/puppeteer.connection.send#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.connection.send#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Connection.session() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connection.session

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection.session#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection.session)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connection.session\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Connection {
  session(sessionId: string): CDPSession | null;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.connection.session\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| sessionId | string | The session id |

**Returns:**

[CDPSession](https://pptr.dev/next/api/puppeteer.cdpsession) \| null

The current CDP session if it exists

- [Signature](https://pptr.dev/next/api/puppeteer.connection.session#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.connection.session#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Connection.url() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connection.url

[Skip to main content](https://pptr.dev/next/api/puppeteer.connection.url#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connection.url)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connection.url\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Connection {
  url(): string;
}

```

**Returns:**

string

- [Signature](https://pptr.dev/next/api/puppeteer.connection.url#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConnectionTransport.close() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connectiontransport.close

[Skip to main content](https://pptr.dev/next/api/puppeteer.connectiontransport.close#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connectiontransport.close)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connectiontransport.close\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface ConnectionTransport {
  close(): void;
}

```

**Returns:**

void

- [Signature](https://pptr.dev/next/api/puppeteer.connectiontransport.close#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConnectionTransport interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connectiontransport

[Skip to main content](https://pptr.dev/next/api/puppeteer.connectiontransport#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connectiontransport)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connectiontransport\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ConnectionTransport

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.connectiontransport\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| onclose | `optional` | () =\> void |  |  |
| onmessage | `optional` | (message: string) => void |  |  |

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.connectiontransport\#methods "Direct link to Methods")

| Method | Description |
| --- | --- |
| [close()](https://pptr.dev/next/api/puppeteer.connectiontransport.close) |  |
| [send(message)](https://pptr.dev/next/api/puppeteer.connectiontransport.send) |  |

- [Signature](https://pptr.dev/next/api/puppeteer.connectiontransport#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.connectiontransport#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.connectiontransport#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConnectionTransport.send() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connectiontransport.send

[Skip to main content](https://pptr.dev/next/api/puppeteer.connectiontransport.send#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connectiontransport.send)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connectiontransport.send\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
interface ConnectionTransport {
  send(message: string): void;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.connectiontransport.send\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| message | string |  |

**Returns:**

void

- [Signature](https://pptr.dev/next/api/puppeteer.connectiontransport.send#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.connectiontransport.send#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConnectOptions interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.connectoptions

[Skip to main content](https://pptr.dev/next/api/puppeteer.connectoptions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.connectoptions)** (24.9.0).



Generic browser options that can be passed when launching any browser or when connecting to an existing browser instance.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.connectoptions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ConnectOptions

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.connectoptions\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| acceptInsecureCerts | `optional` | boolean | Whether to ignore HTTPS errors during navigation. | `false` |
| browserURL | `optional` | string |  |  |
| browserWSEndpoint | `optional` | string |  |  |
| capabilities | `optional` | [SupportedWebDriverCapabilities](https://pptr.dev/next/api/puppeteer.supportedwebdrivercapabilities) | WebDriver BiDi capabilities passed to BiDi `session.new`.<br>**Remarks:**<br>Only works for `protocol="webDriverBiDi"` and [Puppeteer.connect()](https://pptr.dev/next/api/puppeteer.puppeteer.connect). |  |
| defaultViewport | `optional` | [Viewport](https://pptr.dev/next/api/puppeteer.viewport) \| null | Sets the viewport for each page. | '{width: 800, height: 600}' |
| downloadBehavior | `optional` | [DownloadBehavior](https://pptr.dev/next/api/puppeteer.downloadbehavior) | Sets the download behavior for the context. |  |
| headers | `optional` | Record<string, string> | Headers to use for the web socket connection.<br>**Remarks:**<br>Only works in the Node.js environment. |  |
| protocol | `optional` | [ProtocolType](https://pptr.dev/next/api/puppeteer.protocoltype) |  | Determined at run time:<br>- Launching Chrome - 'cdp'.<br>  <br>- Launching Firefox - 'webDriverBiDi'.<br>  <br>- Connecting to a browser - 'cdp'. |
| protocolTimeout | `optional` | number | Timeout setting for individual protocol (CDP) calls. | `180_000` |
| slowMo | `optional` | number | Slows down Puppeteer operations by the specified amount of milliseconds to aid debugging. |  |
| targetFilter | `optional` | [TargetFilterCallback](https://pptr.dev/next/api/puppeteer.targetfiltercallback) | Callback to decide if Puppeteer should connect to a given target or not. |  |
| transport | `optional` | [ConnectionTransport](https://pptr.dev/next/api/puppeteer.connectiontransport) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.connectoptions#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.connectoptions#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConsoleMessage.args() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.consolemessage.args

[Skip to main content](https://pptr.dev/next/api/puppeteer.consolemessage.args#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.consolemessage.args)** (24.9.0).



An array of arguments passed to the console.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.consolemessage.args\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ConsoleMessage {
  args(): JSHandle[];
}

```

**Returns:**

[JSHandle](https://pptr.dev/next/api/puppeteer.jshandle)\[\]

- [Signature](https://pptr.dev/next/api/puppeteer.consolemessage.args#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConsoleMessage.location() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.consolemessage.location

[Skip to main content](https://pptr.dev/next/api/puppeteer.consolemessage.location#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.consolemessage.location)** (24.9.0).



The location of the console message.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.consolemessage.location\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ConsoleMessage {
  location(): ConsoleMessageLocation;
}

```

**Returns:**

[ConsoleMessageLocation](https://pptr.dev/next/api/puppeteer.consolemessagelocation)

- [Signature](https://pptr.dev/next/api/puppeteer.consolemessage.location#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConsoleMessage class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.consolemessage

[Skip to main content](https://pptr.dev/next/api/puppeteer.consolemessage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.consolemessage)** (24.9.0).



ConsoleMessage objects are dispatched by page via the 'console' event.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.consolemessage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class ConsoleMessage

```

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.consolemessage\#remarks "Direct link to Remarks")

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `ConsoleMessage` class.

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.consolemessage\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [args()](https://pptr.dev/next/api/puppeteer.consolemessage.args) |  | An array of arguments passed to the console. |
| [location()](https://pptr.dev/next/api/puppeteer.consolemessage.location) |  | The location of the console message. |
| [stackTrace()](https://pptr.dev/next/api/puppeteer.consolemessage.stacktrace) |  | The array of locations on the stack of the console message. |
| [text()](https://pptr.dev/next/api/puppeteer.consolemessage.text) |  | The text of the console message. |
| [type()](https://pptr.dev/next/api/puppeteer.consolemessage.type) |  | The type of the console message. |

- [Signature](https://pptr.dev/next/api/puppeteer.consolemessage#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.consolemessage#remarks)
- [Methods](https://pptr.dev/next/api/puppeteer.consolemessage#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConsoleMessage.stackTrace() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.consolemessage.stacktrace

[Skip to main content](https://pptr.dev/next/api/puppeteer.consolemessage.stacktrace#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.consolemessage.stacktrace)** (24.9.0).



The array of locations on the stack of the console message.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.consolemessage.stacktrace\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ConsoleMessage {
  stackTrace(): ConsoleMessageLocation[];
}

```

**Returns:**

[ConsoleMessageLocation](https://pptr.dev/next/api/puppeteer.consolemessagelocation)\[\]

- [Signature](https://pptr.dev/next/api/puppeteer.consolemessage.stacktrace#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConsoleMessage.text() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.consolemessage.text

[Skip to main content](https://pptr.dev/next/api/puppeteer.consolemessage.text#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.consolemessage.text)** (24.9.0).



The text of the console message.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.consolemessage.text\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ConsoleMessage {
  text(): string;
}

```

**Returns:**

string

- [Signature](https://pptr.dev/next/api/puppeteer.consolemessage.text#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConsoleMessage.type() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.consolemessage.type

[Skip to main content](https://pptr.dev/next/api/puppeteer.consolemessage.type#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.consolemessage.type)** (24.9.0).



The type of the console message.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.consolemessage.type\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ConsoleMessage {
  type(): ConsoleMessageType;
}

```

**Returns:**

[ConsoleMessageType](https://pptr.dev/next/api/puppeteer.consolemessagetype)

- [Signature](https://pptr.dev/next/api/puppeteer.consolemessage.type#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConsoleMessageLocation interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.consolemessagelocation

[Skip to main content](https://pptr.dev/next/api/puppeteer.consolemessagelocation#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.consolemessagelocation)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.consolemessagelocation\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ConsoleMessageLocation

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.consolemessagelocation\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| columnNumber | `optional` | number | 0-based column number in the resource if known or `undefined` otherwise. |  |
| lineNumber | `optional` | number | 0-based line number in the resource if known or `undefined` otherwise. |  |
| url | `optional` | string | URL of the resource if known or `undefined` otherwise. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.consolemessagelocation#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.consolemessagelocation#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ConsoleMessageType type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.consolemessagetype

[Skip to main content](https://pptr.dev/next/api/puppeteer.consolemessagetype#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.consolemessagetype)** (24.9.0).



The supported types for console messages.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.consolemessagetype\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type ConsoleMessageType =
  | 'log'
  | 'debug'
  | 'info'
  | 'error'
  | 'warn'
  | 'dir'
  | 'dirxml'
  | 'table'
  | 'trace'
  | 'clear'
  | 'startGroup'
  | 'startGroupCollapsed'
  | 'endGroup'
  | 'assert'
  | 'profile'
  | 'profileEnd'
  | 'count'
  | 'timeEnd'
  | 'verbose';

```

- [Signature](https://pptr.dev/next/api/puppeteer.consolemessagetype#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ContinueRequestOverrides interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.continuerequestoverrides

[Skip to main content](https://pptr.dev/next/api/puppeteer.continuerequestoverrides#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.continuerequestoverrides)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.continuerequestoverrides\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface ContinueRequestOverrides

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.continuerequestoverrides\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| headers | `optional` | Record<string, string> |  |  |
| method | `optional` | string |  |  |
| postData | `optional` | string |  |  |
| url | `optional` | string | If set, the request URL will change. This is not a redirect. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.continuerequestoverrides#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.continuerequestoverrides#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### convertCookiesPartitionKeyFromPuppeteerToCdp() function | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.convertcookiespartitionkeyfrompuppeteertocdp

[Skip to main content](https://pptr.dev/next/api/puppeteer.convertcookiespartitionkeyfrompuppeteertocdp#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.convertcookiespartitionkeyfrompuppeteertocdp)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.convertcookiespartitionkeyfrompuppeteertocdp\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare function convertCookiesPartitionKeyFromPuppeteerToCdp(
  partitionKey: CookiePartitionKey | string | undefined,
): Protocol.Network.CookiePartitionKey | undefined;

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.convertcookiespartitionkeyfrompuppeteertocdp\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| partitionKey | [CookiePartitionKey](https://pptr.dev/next/api/puppeteer.cookiepartitionkey) \| string \| undefined |  |

**Returns:**

Protocol.Network.CookiePartitionKey \| undefined

- [Signature](https://pptr.dev/next/api/puppeteer.convertcookiespartitionkeyfrompuppeteertocdp#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.convertcookiespartitionkeyfrompuppeteertocdp#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Cookie interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cookie

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookie#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookie)** (24.9.0).



Represents a cookie object.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cookie\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface Cookie extends CookieData

```

**Extends:** [CookieData](https://pptr.dev/next/api/puppeteer.cookiedata)

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.cookie\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| domain |  | string | Cookie domain. |  |
| expires |  | number | Cookie expiration date as the number of seconds since the UNIX epoch. Set to `-1` for session cookies |  |
| httpOnly |  | boolean | True if cookie is http-only. |  |
| name |  | string | Cookie name. |  |
| partitionKey | `optional` | [CookiePartitionKey](https://pptr.dev/next/api/puppeteer.cookiepartitionkey) \| string | Cookie partition key. In Chrome, it is the top-level site the partitioned cookie is available in. In Firefox, it matches the source origin in the [PartitionKey](https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey). |  |
| partitionKeyOpaque | `optional` | boolean | True if cookie partition key is opaque. Supported only in Chrome. |  |
| path |  | string | Cookie path. |  |
| priority | `optional` | [CookiePriority](https://pptr.dev/next/api/puppeteer.cookiepriority) | Cookie Priority. Supported only in Chrome. |  |
| sameParty | `optional` | boolean | True if cookie is SameParty. Supported only in Chrome. |  |
| sameSite | `optional` | [CookieSameSite](https://pptr.dev/next/api/puppeteer.cookiesamesite) | Cookie SameSite type. |  |
| secure |  | boolean | True if cookie is secure. |  |
| session |  | boolean | True in case of session cookie. |  |
| size |  | number | Cookie size. |  |
| sourceScheme | `optional` | [CookieSourceScheme](https://pptr.dev/next/api/puppeteer.cookiesourcescheme) | Cookie source scheme type. Supported only in Chrome. |  |
| value |  | string | Cookie value. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cookie#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.cookie#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CookieData interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cookiedata

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookiedata#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookiedata)** (24.9.0).



Cookie parameter object used to set cookies in the browser-level cookies API.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cookiedata\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CookieData

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.cookiedata\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| domain |  | string | Cookie domain. |  |
| expires | `optional` | number | Cookie expiration date, session cookie if not set |  |
| httpOnly | `optional` | boolean | True if cookie is http-only. |  |
| name |  | string | Cookie name. |  |
| partitionKey | `optional` | [CookiePartitionKey](https://pptr.dev/next/api/puppeteer.cookiepartitionkey) \| string | Cookie partition key. In Chrome, it matches the top-level site the partitioned cookie is available in. In Firefox, it matches the source origin in the [PartitionKey](https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey). |  |
| path | `optional` | string | Cookie path. |  |
| priority | `optional` | [CookiePriority](https://pptr.dev/next/api/puppeteer.cookiepriority) | Cookie Priority. Supported only in Chrome. |  |
| sameParty | `optional` | boolean | True if cookie is SameParty. Supported only in Chrome. |  |
| sameSite | `optional` | [CookieSameSite](https://pptr.dev/next/api/puppeteer.cookiesamesite) | Cookie SameSite type. |  |
| secure | `optional` | boolean | True if cookie is secure. |  |
| sourceScheme | `optional` | [CookieSourceScheme](https://pptr.dev/next/api/puppeteer.cookiesourcescheme) | Cookie source scheme type. Supported only in Chrome. |  |
| value |  | string | Cookie value. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cookiedata#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.cookiedata#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CookieParam interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cookieparam

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookieparam#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookieparam)** (24.9.0).



Cookie parameter object used to set cookies in the page-level cookies API.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cookieparam\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CookieParam

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.cookieparam\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| domain | `optional` | string | Cookie domain. |  |
| expires | `optional` | number | Cookie expiration date, session cookie if not set |  |
| httpOnly | `optional` | boolean | True if cookie is http-only. |  |
| name |  | string | Cookie name. |  |
| partitionKey | `optional` | [CookiePartitionKey](https://pptr.dev/next/api/puppeteer.cookiepartitionkey) \| string | Cookie partition key. In Chrome, it matches the top-level site the partitioned cookie is available in. In Firefox, it matches the source origin in the [PartitionKey](https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey). |  |
| path | `optional` | string | Cookie path. |  |
| priority | `optional` | [CookiePriority](https://pptr.dev/next/api/puppeteer.cookiepriority) | Cookie Priority. Supported only in Chrome. |  |
| sameParty | `optional` | boolean | True if cookie is SameParty. Supported only in Chrome. |  |
| sameSite | `optional` | [CookieSameSite](https://pptr.dev/next/api/puppeteer.cookiesamesite) | Cookie SameSite type. |  |
| secure | `optional` | boolean | True if cookie is secure. |  |
| sourceScheme | `optional` | [CookieSourceScheme](https://pptr.dev/next/api/puppeteer.cookiesourcescheme) | Cookie source scheme type. Supported only in Chrome. |  |
| url | `optional` | string | The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, and source scheme values of the created cookie. |  |
| value |  | string | Cookie value. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cookieparam#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.cookieparam#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CookiePartitionKey interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cookiepartitionkey

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookiepartitionkey#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookiepartitionkey)** (24.9.0).



Represents a cookie partition key in Chrome.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cookiepartitionkey\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CookiePartitionKey

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.cookiepartitionkey\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| hasCrossSiteAncestor | `optional` | boolean | Indicates if the cookie has any ancestors that are cross-site to the topLevelSite.<br>Supported only in Chrome. |  |
| sourceOrigin |  | string | The site of the top-level URL the browser was visiting at the start of the request to the endpoint that set the cookie.<br>In Chrome, maps to the CDP's `topLevelSite` partition key. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.cookiepartitionkey#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.cookiepartitionkey#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CookiePriority type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cookiepriority

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookiepriority#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookiepriority)** (24.9.0).



Represents the cookie's 'Priority' status: [https://tools.ietf.org/html/draft-west-cookie-priority-00](https://tools.ietf.org/html/draft-west-cookie-priority-00)

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cookiepriority\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type CookiePriority = 'Low' | 'Medium' | 'High';

```

- [Signature](https://pptr.dev/next/api/puppeteer.cookiepriority#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CookieSameSite type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cookiesamesite

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookiesamesite#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookiesamesite)** (24.9.0).



Represents the cookie's 'SameSite' status: [https://tools.ietf.org/html/draft-west-first-party-cookies](https://tools.ietf.org/html/draft-west-first-party-cookies)

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cookiesamesite\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type CookieSameSite = 'Strict' | 'Lax' | 'None';

```

- [Signature](https://pptr.dev/next/api/puppeteer.cookiesamesite#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CookieSourceScheme type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.cookiesourcescheme

[Skip to main content](https://pptr.dev/next/api/puppeteer.cookiesourcescheme#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.cookiesourcescheme)** (24.9.0).



Represents the source scheme of the origin that originally set the cookie. A value of "Unset" allows protocol clients to emulate legacy cookie scope for the scheme. This is a temporary ability and it will be removed in the future.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.cookiesourcescheme\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type CookieSourceScheme = 'Unset' | 'NonSecure' | 'Secure';

```

- [Signature](https://pptr.dev/next/api/puppeteer.cookiesourcescheme#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Coverage class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.coverage

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverage)** (24.9.0).



The Coverage class provides methods to gather information about parts of JavaScript and CSS that were used by the page.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.coverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class Coverage

```

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.coverage\#remarks "Direct link to Remarks")

To output coverage in a form consumable by [Istanbul](https://github.com/istanbuljs), see [puppeteer-to-istanbul](https://github.com/istanbuljs/puppeteer-to-istanbul).

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Coverage` class.

## Example [â€‹](https://pptr.dev/next/api/puppeteer.coverage\#example "Direct link to Example")

An example of using JavaScript and CSS coverage to get percentage of initially executed code:

```codeBlockLines_RjmQ
// Enable both JavaScript and CSS coverage
await Promise.all([\
  page.coverage.startJSCoverage(),\
  page.coverage.startCSSCoverage(),\
]);
// Navigate to page
await page.goto('https://example.com');
// Disable both JavaScript and CSS coverage
const [jsCoverage, cssCoverage] = await Promise.all([\
  page.coverage.stopJSCoverage(),\
  page.coverage.stopCSSCoverage(),\
]);
let totalBytes = 0;
let usedBytes = 0;
const coverage = [...jsCoverage, ...cssCoverage];
for (const entry of coverage) {
  totalBytes += entry.text.length;
  for (const range of entry.ranges) usedBytes += range.end - range.start - 1;
}
console.log(`Bytes used: ${(usedBytes / totalBytes) * 100}%`);

```

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.coverage\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [startCSSCoverage(options)](https://pptr.dev/next/api/puppeteer.coverage.startcsscoverage) |  |  |
| [startJSCoverage(options)](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage) |  | **Remarks:**<br>Anonymous scripts are ones that don't have an associated url. These are scripts that are dynamically created on the page using `eval` or `new Function`. If `reportAnonymousScripts` is set to `true`, anonymous scripts URL will start with `debugger://VM` (unless a magic //# sourceURL comment is present, in which case that will the be URL). |
| [stopCSSCoverage()](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage) |  | Promise that resolves to the array of coverage reports for all stylesheets.<br>**Remarks:**<br>CSS Coverage doesn't include dynamically injected style tags without sourceURLs. |
| [stopJSCoverage()](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage) |  | Promise that resolves to the array of coverage reports for all scripts.<br>**Remarks:**<br>JavaScript Coverage doesn't include anonymous scripts by default. However, scripts with sourceURLs are reported. |

- [Signature](https://pptr.dev/next/api/puppeteer.coverage#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.coverage#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.coverage#example)
- [Methods](https://pptr.dev/next/api/puppeteer.coverage#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Coverage.startCSSCoverage() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.coverage.startcsscoverage

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverage.startcsscoverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverage.startcsscoverage)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.coverage.startcsscoverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Coverage {
  startCSSCoverage(options?: CSSCoverageOptions): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.coverage.startcsscoverage\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [CSSCoverageOptions](https://pptr.dev/next/api/puppeteer.csscoverageoptions) | _(Optional)_ Set of configurable options for coverage, defaults to `resetOnNavigation : true` |

**Returns:**

Promise<void>

Promise that resolves when coverage is started.

- [Signature](https://pptr.dev/next/api/puppeteer.coverage.startcsscoverage#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.coverage.startcsscoverage#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Coverage.startJSCoverage() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.coverage.startjscoverage

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverage.startjscoverage)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Coverage {
  startJSCoverage(options?: JSCoverageOptions): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [JSCoverageOptions](https://pptr.dev/next/api/puppeteer.jscoverageoptions) | _(Optional)_ Set of configurable options for coverage defaults to `resetOnNavigation : true, reportAnonymousScripts : false,` `includeRawScriptCoverage : false, useBlockCoverage : true` |

**Returns:**

Promise<void>

Promise that resolves when coverage is started.

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage\#remarks "Direct link to Remarks")

Anonymous scripts are ones that don't have an associated url. These are scripts that are dynamically created on the page using `eval` or `new Function`. If `reportAnonymousScripts` is set to `true`, anonymous scripts URL will start with `debugger://VM` (unless a magic //# sourceURL comment is present, in which case that will the be URL).

- [Signature](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.coverage.startjscoverage#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Coverage.stopCSSCoverage() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverage.stopcsscoverage)** (24.9.0).



Promise that resolves to the array of coverage reports for all stylesheets.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Coverage {
  stopCSSCoverage(): Promise<CoverageEntry[]>;
}

```

**Returns:**

Promise< [CoverageEntry](https://pptr.dev/next/api/puppeteer.coverageentry)\[\]>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage\#remarks "Direct link to Remarks")

CSS Coverage doesn't include dynamically injected style tags without sourceURLs.

- [Signature](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.coverage.stopcsscoverage#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Coverage.stopJSCoverage() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverage.stopjscoverage)** (24.9.0).



Promise that resolves to the array of coverage reports for all scripts.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Coverage {
  stopJSCoverage(): Promise<JSCoverageEntry[]>;
}

```

**Returns:**

Promise< [JSCoverageEntry](https://pptr.dev/next/api/puppeteer.jscoverageentry)\[\]>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage\#remarks "Direct link to Remarks")

JavaScript Coverage doesn't include anonymous scripts by default. However, scripts with sourceURLs are reported.

- [Signature](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.coverage.stopjscoverage#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CoverageEntry interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.coverageentry

[Skip to main content](https://pptr.dev/next/api/puppeteer.coverageentry#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.coverageentry)** (24.9.0).



The CoverageEntry class represents one entry of the coverage report.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.coverageentry\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CoverageEntry

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.coverageentry\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| ranges |  | Array<{ start: number; end: number; }> | The covered range as start and end positions. |  |
| text |  | string | The content of the style sheet or script. |  |
| url |  | string | The URL of the style sheet or script. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.coverageentry#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.coverageentry#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Credentials interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.credentials

[Skip to main content](https://pptr.dev/next/api/puppeteer.credentials#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.credentials)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.credentials\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface Credentials

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.credentials\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| password |  | string |  |  |
| username |  | string |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.credentials#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.credentials#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CSSCoverage.(constructor) | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.csscoverage._constructor_

[Skip to main content](https://pptr.dev/next/api/puppeteer.csscoverage._constructor_#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.csscoverage._constructor_)** (24.9.0).



Constructs a new instance of the `CSSCoverage` class

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.csscoverage._constructor_\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class CSSCoverage {
  constructor(client: CDPSession);
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.csscoverage._constructor_\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| client | [CDPSession](https://pptr.dev/next/api/puppeteer.cdpsession) |  |

- [Signature](https://pptr.dev/next/api/puppeteer.csscoverage._constructor_#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.csscoverage._constructor_#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CSSCoverage class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.csscoverage

[Skip to main content](https://pptr.dev/next/api/puppeteer.csscoverage#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.csscoverage)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.csscoverage\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class CSSCoverage

```

## Constructors [â€‹](https://pptr.dev/next/api/puppeteer.csscoverage\#constructors "Direct link to Constructors")

| Constructor | Modifiers | Description |
| --- | --- | --- |
| [(constructor)(client)](https://pptr.dev/next/api/puppeteer.csscoverage._constructor_) |  | Constructs a new instance of the `CSSCoverage` class |

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.csscoverage\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [start(options)](https://pptr.dev/next/api/puppeteer.csscoverage.start) |  |  |
| [stop()](https://pptr.dev/next/api/puppeteer.csscoverage.stop) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.csscoverage#signature)
- [Constructors](https://pptr.dev/next/api/puppeteer.csscoverage#constructors)
- [Methods](https://pptr.dev/next/api/puppeteer.csscoverage#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CSSCoverage.start() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.csscoverage.start

[Skip to main content](https://pptr.dev/next/api/puppeteer.csscoverage.start#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.csscoverage.start)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.csscoverage.start\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class CSSCoverage {
  start(options?: {resetOnNavigation?: boolean}): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.csscoverage.start\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | { resetOnNavigation?: boolean; } | _(Optional)_ |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.csscoverage.start#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.csscoverage.start#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CSSCoverage.stop() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.csscoverage.stop

[Skip to main content](https://pptr.dev/next/api/puppeteer.csscoverage.stop#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.csscoverage.stop)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.csscoverage.stop\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class CSSCoverage {
  stop(): Promise<CoverageEntry[]>;
}

```

**Returns:**

Promise< [CoverageEntry](https://pptr.dev/next/api/puppeteer.coverageentry)\[\]>

- [Signature](https://pptr.dev/next/api/puppeteer.csscoverage.stop#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CSSCoverageOptions interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.csscoverageoptions

[Skip to main content](https://pptr.dev/next/api/puppeteer.csscoverageoptions#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.csscoverageoptions)** (24.9.0).



Set of configurable options for CSS coverage.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.csscoverageoptions\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CSSCoverageOptions

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.csscoverageoptions\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| resetOnNavigation | `optional` | boolean | Whether to reset coverage on every navigation. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.csscoverageoptions#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.csscoverageoptions#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### CustomQueryHandler interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.customqueryhandler

[Skip to main content](https://pptr.dev/next/api/puppeteer.customqueryhandler#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.customqueryhandler)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.customqueryhandler\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface CustomQueryHandler

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.customqueryhandler\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| queryAll | `optional` | (node: Node, selector: string) => Iterable<Node> | Searches for some [Nodes](https://developer.mozilla.org/en-US/docs/Web/API/Node) matching the given `selector` from [node](https://developer.mozilla.org/en-US/docs/Web/API/Node). |  |
| queryOne | `optional` | (node: Node, selector: string) => Node \| null | Searches for a [Node](https://developer.mozilla.org/en-US/docs/Web/API/Node) matching the given `selector` from [node](https://developer.mozilla.org/en-US/docs/Web/API/Node). |  |

- [Signature](https://pptr.dev/next/api/puppeteer.customqueryhandler#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.customqueryhandler#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DebugInfo interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.debuginfo

[Skip to main content](https://pptr.dev/next/api/puppeteer.debuginfo#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.debuginfo)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.debuginfo\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface DebugInfo

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.debuginfo\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| pendingProtocolErrors |  | Error\[\] |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.debuginfo#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.debuginfo#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DEFAULT_INTERCEPT_RESOLUTION_PRIORITY variable | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.default_intercept_resolution_priority

[Skip to main content](https://pptr.dev/next/api/puppeteer.default_intercept_resolution_priority#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.default_intercept_resolution_priority)** (24.9.0).



The default cooperative request interception resolution priority

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.default_intercept_resolution_priority\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
DEFAULT_INTERCEPT_RESOLUTION_PRIORITY = 0;

```

- [Signature](https://pptr.dev/next/api/puppeteer.default_intercept_resolution_priority#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### defaultArgs() function | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.defaultargs

[Skip to main content](https://pptr.dev/next/api/puppeteer.defaultargs#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.defaultargs)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.defaultargs\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
defaultArgs: (options?: PuppeteerCore.LaunchOptions) => string[]

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.defaultargs\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| options | [PuppeteerCore.LaunchOptions](https://pptr.dev/next/api/puppeteer.launchoptions) | _(Optional)_ |

**Returns:**

string\[\]

- [Signature](https://pptr.dev/next/api/puppeteer.defaultargs#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.defaultargs#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DeleteCookiesRequest interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.deletecookiesrequest

[Skip to main content](https://pptr.dev/next/api/puppeteer.deletecookiesrequest#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.deletecookiesrequest)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.deletecookiesrequest\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface DeleteCookiesRequest

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.deletecookiesrequest\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| domain | `optional` | string | If specified, deletes only cookies with the exact domain. |  |
| name |  | string | Name of the cookies to remove. |  |
| partitionKey | `optional` | [CookiePartitionKey](https://pptr.dev/next/api/puppeteer.cookiepartitionkey) \| string | If specified, deletes cookies in the given partition key. In Chrome, partitionKey matches the top-level site the partitioned cookie is available in. In Firefox, it matches the source origin in the [PartitionKey](https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey). |  |
| path | `optional` | string | If specified, deletes only cookies with the exact path. |  |
| url | `optional` | string | If specified, deletes all the cookies with the given name where domain and path match provided URL. Otherwise, deletes only cookies related to the current page's domain. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.deletecookiesrequest#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.deletecookiesrequest#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Device interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.device

[Skip to main content](https://pptr.dev/next/api/puppeteer.device#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.device)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.device\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface Device

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.device\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| userAgent |  | string |  |  |
| viewport |  | [Viewport](https://pptr.dev/next/api/puppeteer.viewport) |  |  |

- [Signature](https://pptr.dev/next/api/puppeteer.device#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.device#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DeviceRequestPrompt.cancel() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.devicerequestprompt.cancel

[Skip to main content](https://pptr.dev/next/api/puppeteer.devicerequestprompt.cancel#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.devicerequestprompt.cancel)** (24.9.0).



Cancel the prompt.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt.cancel\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class DeviceRequestPrompt {
  cancel(): Promise<void>;
}

```

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.devicerequestprompt.cancel#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DeviceRequestPrompt class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.devicerequestprompt

[Skip to main content](https://pptr.dev/next/api/puppeteer.devicerequestprompt#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.devicerequestprompt)** (24.9.0).



Device request prompts let you respond to the page requesting for a device through an API like WebBluetooth.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class DeviceRequestPrompt

```

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#remarks "Direct link to Remarks")

`DeviceRequestPrompt` instances are returned via the [Page.waitForDevicePrompt()](https://pptr.dev/next/api/puppeteer.page.waitfordeviceprompt) method.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `DeviceRequestPrompt` class.

## Example [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#example "Direct link to Example")

```codeBlockLines_RjmQ
const [devicePrompt] = Promise.all([\
  page.waitForDevicePrompt(),\
  page.click('#connect-bluetooth'),\
]);
await devicePrompt.select(
  await devicePrompt.waitForDevice(({name}) => name.includes('My Device')),
);

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| devices |  | [DeviceRequestPromptDevice](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice)\[\] | Current list of selectable devices. |

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [cancel()](https://pptr.dev/next/api/puppeteer.devicerequestprompt.cancel) |  | Cancel the prompt. |
| [select(device)](https://pptr.dev/next/api/puppeteer.devicerequestprompt.select) |  | Select a device in the prompt's list. |
| [waitForDevice(filter, options)](https://pptr.dev/next/api/puppeteer.devicerequestprompt.waitfordevice) |  | Resolve to the first device in the prompt matching a filter. |

- [Signature](https://pptr.dev/next/api/puppeteer.devicerequestprompt#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.devicerequestprompt#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.devicerequestprompt#example)
- [Properties](https://pptr.dev/next/api/puppeteer.devicerequestprompt#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.devicerequestprompt#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DeviceRequestPrompt.select() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.devicerequestprompt.select

[Skip to main content](https://pptr.dev/next/api/puppeteer.devicerequestprompt.select#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.devicerequestprompt.select)** (24.9.0).



Select a device in the prompt's list.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt.select\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class DeviceRequestPrompt {
  select(device: DeviceRequestPromptDevice): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestprompt.select\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| device | [DeviceRequestPromptDevice](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice) |  |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.devicerequestprompt.select#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.devicerequestprompt.select#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DeviceRequestPromptDevice class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice

[Skip to main content](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.devicerequestpromptdevice)** (24.9.0).



Device in a request prompt.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare class DeviceRequestPromptDevice

```

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice\#remarks "Direct link to Remarks")

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `DeviceRequestPromptDevice` class.

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| id |  | string | Device id during a prompt. |
| name |  | string | Device name as it appears in a prompt. |

- [Signature](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice#remarks)
- [Properties](https://pptr.dev/next/api/puppeteer.devicerequestpromptdevice#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Dialog.accept() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.dialog.accept

[Skip to main content](https://pptr.dev/next/api/puppeteer.dialog.accept#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.dialog.accept)** (24.9.0).



A promise that resolves when the dialog has been accepted.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.dialog.accept\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Dialog {
  accept(promptText?: string): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.dialog.accept\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| promptText | string | _(Optional)_ optional text that will be entered in the dialog prompt. Has no effect if the dialog's type is not `prompt`. |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.dialog.accept#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.dialog.accept#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Dialog.defaultValue() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.dialog.defaultvalue

[Skip to main content](https://pptr.dev/next/api/puppeteer.dialog.defaultvalue#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.dialog.defaultvalue)** (24.9.0).



The default value of the prompt, or an empty string if the dialog is not a `prompt`.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.dialog.defaultvalue\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Dialog {
  defaultValue(): string;
}

```

**Returns:**

string

- [Signature](https://pptr.dev/next/api/puppeteer.dialog.defaultvalue#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Dialog.dismiss() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.dialog.dismiss

[Skip to main content](https://pptr.dev/next/api/puppeteer.dialog.dismiss#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.dialog.dismiss)** (24.9.0).



A promise which will resolve once the dialog has been dismissed

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.dialog.dismiss\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Dialog {
  dismiss(): Promise<void>;
}

```

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.dialog.dismiss#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Dialog class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.dialog

[Skip to main content](https://pptr.dev/next/api/puppeteer.dialog#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.dialog)** (24.9.0).



Dialog instances are dispatched by the [Page](https://pptr.dev/next/api/puppeteer.page) via the `dialog` event.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.dialog\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class Dialog

```

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.dialog\#remarks "Direct link to Remarks")

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Dialog` class.

## Example [â€‹](https://pptr.dev/next/api/puppeteer.dialog\#example "Direct link to Example")

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  page.on('dialog', async dialog => {
    console.log(dialog.message());
    await dialog.dismiss();
    await browser.close();
  });
  page.evaluate(() => alert('1'));
})();

```

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.dialog\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [accept(promptText)](https://pptr.dev/next/api/puppeteer.dialog.accept) |  | A promise that resolves when the dialog has been accepted. |
| [defaultValue()](https://pptr.dev/next/api/puppeteer.dialog.defaultvalue) |  | The default value of the prompt, or an empty string if the dialog is not a `prompt`. |
| [dismiss()](https://pptr.dev/next/api/puppeteer.dialog.dismiss) |  | A promise which will resolve once the dialog has been dismissed |
| [message()](https://pptr.dev/next/api/puppeteer.dialog.message) |  | The message displayed in the dialog. |
| [type()](https://pptr.dev/next/api/puppeteer.dialog.type) |  | The type of the dialog. |

- [Signature](https://pptr.dev/next/api/puppeteer.dialog#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.dialog#remarks)
- [Example](https://pptr.dev/next/api/puppeteer.dialog#example)
- [Methods](https://pptr.dev/next/api/puppeteer.dialog#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Dialog.message() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.dialog.message

[Skip to main content](https://pptr.dev/next/api/puppeteer.dialog.message#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.dialog.message)** (24.9.0).



The message displayed in the dialog.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.dialog.message\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Dialog {
  message(): string;
}

```

**Returns:**

string

- [Signature](https://pptr.dev/next/api/puppeteer.dialog.message#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Dialog.type() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.dialog.type

[Skip to main content](https://pptr.dev/next/api/puppeteer.dialog.type#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.dialog.type)** (24.9.0).



The type of the dialog.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.dialog.type\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class Dialog {
  type(): Protocol.Page.DialogType;
}

```

**Returns:**

Protocol.Page.DialogType

- [Signature](https://pptr.dev/next/api/puppeteer.dialog.type#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DownloadBehavior interface | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.downloadbehavior

[Skip to main content](https://pptr.dev/next/api/puppeteer.downloadbehavior#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.downloadbehavior)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.downloadbehavior\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export interface DownloadBehavior

```

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.downloadbehavior\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description | Default |
| --- | --- | --- | --- | --- |
| downloadPath | `optional` | string | The default path to save downloaded files to.<br>**Remarks:**<br>Setting this is required if behavior is set to `allow` or `allowAndName`. |  |
| policy |  | [DownloadPolicy](https://pptr.dev/next/api/puppeteer.downloadpolicy) | Whether to allow all or deny all download requests, or use default behavior if available.<br>**Remarks:**<br>Setting this to `allowAndName` will name all files according to their download guids. |  |

- [Signature](https://pptr.dev/next/api/puppeteer.downloadbehavior#signature)
- [Properties](https://pptr.dev/next/api/puppeteer.downloadbehavior#properties)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### DownloadPolicy type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.downloadpolicy

[Skip to main content](https://pptr.dev/next/api/puppeteer.downloadpolicy#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.downloadpolicy)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.downloadpolicy\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type DownloadPolicy = 'deny' | 'allow' | 'allowAndName' | 'default';

```

- [Signature](https://pptr.dev/next/api/puppeteer.downloadpolicy#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementFor type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementfor

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementfor#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementfor)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementfor\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type ElementFor<
  TagName extends keyof HTMLElementTagNameMap | keyof SVGElementTagNameMap,
> = TagName extends keyof HTMLElementTagNameMap
  ? HTMLElementTagNameMap[TagName]
  : TagName extends keyof SVGElementTagNameMap
    ? SVGElementTagNameMap[TagName]
    : never;

```

- [Signature](https://pptr.dev/next/api/puppeteer.elementfor#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.$() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle._

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle._#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle._)** (24.9.0).



Queries the current element for an element matching the given selector.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle._\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  $<Selector extends string>(
    selector: Selector,
  ): Promise<ElementHandle<NodeFor<Selector>> | null>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle._\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| selector | Selector | [selector](https://pptr.dev/guides/page-interactions#selectors) to query the page for. [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) can be passed as-is and a [Puppeteer-specific selector syntax](https://pptr.dev/guides/page-interactions#non-css-selectors) allows querying by [text](https://pptr.dev/guides/page-interactions#text-selectors--p-text), [a11y role and name](https://pptr.dev/guides/page-interactions#aria-selectors--p-aria), and [xpath](https://pptr.dev/guides/page-interactions#xpath-selectors--p-xpath) and [combining these queries across shadow roots](https://pptr.dev/guides/page-interactions#querying-elements-in-shadow-dom). Alternatively, you can specify the selector type using a [prefix](https://pptr.dev/guides/page-interactions#prefixed-selector-syntax). |

**Returns:**

Promise< [ElementHandle](https://pptr.dev/next/api/puppeteer.elementhandle) < [NodeFor](https://pptr.dev/next/api/puppeteer.nodefor) <Selector>> \| null>

A [element handle](https://pptr.dev/next/api/puppeteer.elementhandle) to the first element matching the given selector. Otherwise, `null`.

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle._#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle._#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.$$() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle.__

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.__#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.__)** (24.9.0).



Queries the current element for all elements matching the given selector.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.__\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  $$<Selector extends string>(
    selector: Selector,
    options?: QueryOptions,
  ): Promise<Array<ElementHandle<NodeFor<Selector>>>>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.__\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| selector | Selector | [selector](https://pptr.dev/guides/page-interactions#selectors) to query the page for. [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) can be passed as-is and a [Puppeteer-specific selector syntax](https://pptr.dev/guides/page-interactions#non-css-selectors) allows querying by [text](https://pptr.dev/guides/page-interactions#text-selectors--p-text), [a11y role and name](https://pptr.dev/guides/page-interactions#aria-selectors--p-aria), and [xpath](https://pptr.dev/guides/page-interactions#xpath-selectors--p-xpath) and [combining these queries across shadow roots](https://pptr.dev/guides/page-interactions#querying-elements-in-shadow-dom). Alternatively, you can specify the selector type using a [prefix](https://pptr.dev/guides/page-interactions#prefixed-selector-syntax). |
| options | [QueryOptions](https://pptr.dev/next/api/puppeteer.queryoptions) | _(Optional)_ |

**Returns:**

Promise<Array< [ElementHandle](https://pptr.dev/next/api/puppeteer.elementhandle) < [NodeFor](https://pptr.dev/next/api/puppeteer.nodefor) <Selector>>>>

An array of [element handles](https://pptr.dev/next/api/puppeteer.elementhandle) that point to elements matching the given selector.

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.__#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.__#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.$$eval() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle.__eval

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.__eval#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.__eval)** (24.9.0).



Runs the given function on an array of elements matching the given selector in the current element.

If the given function returns a promise, then this method will wait till the promise resolves.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.__eval\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  $$eval<
    Selector extends string,
    Params extends unknown[],
    Func extends EvaluateFuncWith<
      Array<NodeFor<Selector>>,
      Params
    > = EvaluateFuncWith<Array<NodeFor<Selector>>, Params>,
  >(
    selector: Selector,
    pageFunction: Func | string,
    ...args: Params
  ): Promise<Awaited<ReturnType<Func>>>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.__eval\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| selector | Selector | [selector](https://pptr.dev/guides/page-interactions#selectors) to query the page for. [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) can be passed as-is and a [Puppeteer-specific selector syntax](https://pptr.dev/guides/page-interactions#non-css-selectors) allows querying by [text](https://pptr.dev/guides/page-interactions#text-selectors--p-text), [a11y role and name](https://pptr.dev/guides/page-interactions#aria-selectors--p-aria), and [xpath](https://pptr.dev/guides/page-interactions#xpath-selectors--p-xpath) and [combining these queries across shadow roots](https://pptr.dev/guides/page-interactions#querying-elements-in-shadow-dom). Alternatively, you can specify the selector type using a [prefix](https://pptr.dev/guides/page-interactions#prefixed-selector-syntax). |
| pageFunction | Func \| string | The function to be evaluated in the element's page's context. An array of elements matching the given selector will be passed to the function as its first argument. |
| args | Params | Additional arguments to pass to `pageFunction`. |

**Returns:**

Promise<Awaited<ReturnType<Func>>>

A promise to the result of the function.

## Example [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.__eval\#example "Direct link to Example")

HTML:

```codeBlockLines_RjmQ
<div class="feed">
  <div class="tweet">Hello!</div>
  <div class="tweet">Hi!</div>
</div>

```

JavaScript:

```codeBlockLines_RjmQ
const feedHandle = await page.$('.feed');
expect(
  await feedHandle.$$eval('.tweet', nodes => nodes.map(n => n.innerText)),
).toEqual(['Hello!', 'Hi!']);

```

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.__eval#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.__eval#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.elementhandle.__eval#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.$eval() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle._eval

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle._eval#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle._eval)** (24.9.0).



Runs the given function on the first element matching the given selector in the current element.

If the given function returns a promise, then this method will wait till the promise resolves.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle._eval\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  $eval<
    Selector extends string,
    Params extends unknown[],
    Func extends EvaluateFuncWith<NodeFor<Selector>, Params> = EvaluateFuncWith<
      NodeFor<Selector>,
      Params
    >,
  >(
    selector: Selector,
    pageFunction: Func | string,
    ...args: Params
  ): Promise<Awaited<ReturnType<Func>>>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle._eval\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| selector | Selector | [selector](https://pptr.dev/guides/page-interactions#selectors) to query the page for. [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors) can be passed as-is and a [Puppeteer-specific selector syntax](https://pptr.dev/guides/page-interactions#non-css-selectors) allows querying by [text](https://pptr.dev/guides/page-interactions#text-selectors--p-text), [a11y role and name](https://pptr.dev/guides/page-interactions#aria-selectors--p-aria), and [xpath](https://pptr.dev/guides/page-interactions#xpath-selectors--p-xpath) and [combining these queries across shadow roots](https://pptr.dev/guides/page-interactions#querying-elements-in-shadow-dom). Alternatively, you can specify the selector type using a [prefix](https://pptr.dev/guides/page-interactions#prefixed-selector-syntax). |
| pageFunction | Func \| string | The function to be evaluated in this element's page's context. The first element matching the selector will be passed in as the first argument. |
| args | Params | Additional arguments to pass to `pageFunction`. |

**Returns:**

Promise<Awaited<ReturnType<Func>>>

A promise to the result of the function.

## Example [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle._eval\#example "Direct link to Example")

```codeBlockLines_RjmQ
const tweetHandle = await page.$('.tweet');
expect(await tweetHandle.$eval('.like', node => node.innerText)).toBe('100');
expect(await tweetHandle.$eval('.retweets', node => node.innerText)).toBe('10');

```

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle._eval#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle._eval#parameters)
- [Example](https://pptr.dev/next/api/puppeteer.elementhandle._eval#example)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.autofill() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle.autofill

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.autofill#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.autofill)** (24.9.0).



If the element is a form input, you can use [ElementHandle.autofill()](https://pptr.dev/next/api/puppeteer.elementhandle.autofill) to test if the form is compatible with the browser's autofill implementation. Throws an error if the form cannot be autofilled.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.autofill\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  abstract autofill(data: AutofillData): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.autofill\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| data | [AutofillData](https://pptr.dev/next/api/puppeteer.autofilldata) |  |

**Returns:**

Promise<void>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.autofill\#remarks "Direct link to Remarks")

Currently, Puppeteer supports auto-filling credit card information only and in Chrome in the new headless and headful modes only.

```codeBlockLines_RjmQ
// Select an input on the credit card form.
const name = await page.waitForSelector('form #name');
// Trigger autofill with the desired data.
await name.autofill({
  creditCard: {
    number: '4444444444444444',
    name: 'John Smith',
    expiryMonth: '01',
    expiryYear: '2030',
    cvc: '123',
  },
});

```

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.autofill#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.autofill#parameters)
- [Remarks](https://pptr.dev/next/api/puppeteer.elementhandle.autofill#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.backendNodeId() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle.backendnodeid

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.backendnodeid#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.backendnodeid)** (24.9.0).



When connected using Chrome DevTools Protocol, it returns a DOM.BackendNodeId for the element.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.backendnodeid\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  abstract backendNodeId(): Promise<number>;
}

```

**Returns:**

Promise<number>

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.backendnodeid#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.boundingBox() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.boundingbox)** (24.9.0).



This method returns the bounding box of the element (relative to the main frame), or `null` if the element is [not part of the layout](https://drafts.csswg.org/css-display-4/#box-generation) (example: `display: none`).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  boundingBox(): Promise<BoundingBox | null>;
}

```

**Returns:**

Promise< [BoundingBox](https://pptr.dev/next/api/puppeteer.boundingbox) \| null>

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.boxModel() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.boxmodel)** (24.9.0).



This method returns boxes of the element, or `null` if the element is [not part of the layout](https://drafts.csswg.org/css-display-4/#box-generation) (example: `display: none`).

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  boxModel(): Promise<BoxModel | null>;
}

```

**Returns:**

Promise< [BoxModel](https://pptr.dev/next/api/puppeteer.boxmodel) \| null>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel\#remarks "Direct link to Remarks")

Boxes are represented as an array of points; Each Point is an object `{x, y}`. Box points are sorted clock-wise.

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel#remarks)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.click() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle.click

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.click#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.click)** (24.9.0).



This method scrolls element into view if needed, and then uses [Page.mouse](https://pptr.dev/next/api/puppeteer.page#mouse) to click in the center of the element. If the element is detached from DOM, the method throws an error.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.click\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  click(
    this: ElementHandle<Element>,
    options?: Readonly<ClickOptions>,
  ): Promise<void>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.click\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| this | [ElementHandle](https://pptr.dev/next/api/puppeteer.elementhandle) <Element> |  |
| options | Readonly< [ClickOptions](https://pptr.dev/next/api/puppeteer.clickoptions) > | _(Optional)_ |

**Returns:**

Promise<void>

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.click#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.click#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.clickablePoint() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle.clickablepoint

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.clickablepoint#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.clickablepoint)** (24.9.0).



Returns the middle point within an element unless a specific offset is provided.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.clickablepoint\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  clickablePoint(offset?: Offset): Promise<Point>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.clickablepoint\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| offset | [Offset](https://pptr.dev/next/api/puppeteer.offset) | _(Optional)_ |

**Returns:**

Promise< [Point](https://pptr.dev/next/api/puppeteer.point) >

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.clickablepoint#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.clickablepoint#parameters)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle.contentFrame() method | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle.contentframe

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle.contentframe)** (24.9.0).



## contentFrame(): Promise<Frame>

Resolves the frame associated with the element, if any. Always exists for HTMLIFrameElements.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  abstract contentFrame(this: ElementHandle<HTMLIFrameElement>): Promise<Frame>;
}

```

## Parameters [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe\#parameters "Direct link to Parameters")

| Parameter | Type | Description |
| --- | --- | --- |
| this | [ElementHandle](https://pptr.dev/next/api/puppeteer.elementhandle) <HTMLIFrameElement> |  |

**Returns:**

Promise< [Frame](https://pptr.dev/next/api/puppeteer.frame) >

## contentFrame(): Promise<Frame \| null>

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe\#signature-1 "Direct link to Signature")

```codeBlockLines_RjmQ
class ElementHandle {
  abstract contentFrame(): Promise<Frame | null>;
}

```

**Returns:**

Promise< [Frame](https://pptr.dev/next/api/puppeteer.frame) \| null>

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe#signature)
- [Parameters](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe#parameters)
  - [Signature](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe#signature-1)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### ElementHandle class | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.elementhandle

[Skip to main content](https://pptr.dev/next/api/puppeteer.elementhandle#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.elementhandle)** (24.9.0).



ElementHandle represents an in-page DOM element.

### Signature [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export declare abstract class ElementHandle<ElementType extends Node = Element> extends JSHandle<ElementType>

```

**Extends:** [JSHandle](https://pptr.dev/next/api/puppeteer.jshandle) <ElementType>

## Remarks [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle\#remarks "Direct link to Remarks")

ElementHandles can be created with the [Page.$()](https://pptr.dev/next/api/puppeteer.page._) method.

```codeBlockLines_RjmQ
import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');
  const hrefElement = await page.$('a');
  await hrefElement.click();
  // ...
})();

```

ElementHandle prevents the DOM element from being garbage-collected unless the handle is [disposed](https://pptr.dev/next/api/puppeteer.jshandle.dispose). ElementHandles are auto-disposed when their origin frame gets navigated.

ElementHandle instances can be used as arguments in [Page.$eval()](https://pptr.dev/next/api/puppeteer.page._eval) and [Page.evaluate()](https://pptr.dev/next/api/puppeteer.page.evaluate) methods.

If you're using TypeScript, ElementHandle takes a generic argument that denotes the type of element the handle is holding within. For example, if you have a handle to a `<select>` element, you can type it as `ElementHandle<HTMLSelectElement>` and you get some nicer type checks.

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `ElementHandle` class.

## Properties [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle\#properties "Direct link to Properties")

| Property | Modifiers | Type | Description |
| --- | --- | --- | --- |
| frame | `readonly` | [Frame](https://pptr.dev/next/api/puppeteer.frame) | Frame corresponding to the current handle. |

## Methods [â€‹](https://pptr.dev/next/api/puppeteer.elementhandle\#methods "Direct link to Methods")

| Method | Modifiers | Description |
| --- | --- | --- |
| [$(selector)](https://pptr.dev/next/api/puppeteer.elementhandle._) |  | Queries the current element for an element matching the given selector. |
| [$$(selector, options)](https://pptr.dev/next/api/puppeteer.elementhandle.__) |  | Queries the current element for all elements matching the given selector. |
| [$$eval(selector, pageFunction, args)](https://pptr.dev/next/api/puppeteer.elementhandle.__eval) |  | Runs the given function on an array of elements matching the given selector in the current element.<br>If the given function returns a promise, then this method will wait till the promise resolves. |
| [$eval(selector, pageFunction, args)](https://pptr.dev/next/api/puppeteer.elementhandle._eval) |  | Runs the given function on the first element matching the given selector in the current element.<br>If the given function returns a promise, then this method will wait till the promise resolves. |
| [autofill(data)](https://pptr.dev/next/api/puppeteer.elementhandle.autofill) |  | If the element is a form input, you can use [ElementHandle.autofill()](https://pptr.dev/next/api/puppeteer.elementhandle.autofill) to test if the form is compatible with the browser's autofill implementation. Throws an error if the form cannot be autofilled.<br>**Remarks:**<br>Currently, Puppeteer supports auto-filling credit card information only and in Chrome in the new headless and headful modes only.<br>```codeBlockLines_RjmQ<br>// Select an input on the credit card form.<br>const name = await page.waitForSelector('form #name');<br>// Trigger autofill with the desired data.<br>await name.autofill({<br>  creditCard: {<br>    number: '4444444444444444',<br>    name: 'John Smith',<br>    expiryMonth: '01',<br>    expiryYear: '2030',<br>    cvc: '123',<br>  },<br>});<br>``` |
| [backendNodeId()](https://pptr.dev/next/api/puppeteer.elementhandle.backendnodeid) |  | When connected using Chrome DevTools Protocol, it returns a DOM.BackendNodeId for the element. |
| [boundingBox()](https://pptr.dev/next/api/puppeteer.elementhandle.boundingbox) |  | This method returns the bounding box of the element (relative to the main frame), or `null` if the element is [not part of the layout](https://drafts.csswg.org/css-display-4/#box-generation) (example: `display: none`). |
| [boxModel()](https://pptr.dev/next/api/puppeteer.elementhandle.boxmodel) |  | This method returns boxes of the element, or `null` if the element is [not part of the layout](https://drafts.csswg.org/css-display-4/#box-generation) (example: `display: none`).<br>**Remarks:**<br>Boxes are represented as an array of points; Each Point is an object `{x, y}`. Box points are sorted clock-wise. |
| [click(this, options)](https://pptr.dev/next/api/puppeteer.elementhandle.click) |  | This method scrolls element into view if needed, and then uses [Page.mouse](https://pptr.dev/next/api/puppeteer.page#mouse) to click in the center of the element. If the element is detached from DOM, the method throws an error. |
| [clickablePoint(offset)](https://pptr.dev/next/api/puppeteer.elementhandle.clickablepoint) |  | Returns the middle point within an element unless a specific offset is provided. |
| [contentFrame(this)](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe) |  | Resolves the frame associated with the element, if any. Always exists for HTMLIFrameElements. |
| [contentFrame()](https://pptr.dev/next/api/puppeteer.elementhandle.contentframe) |  |  |
| [drag(this, target)](https://pptr.dev/next/api/puppeteer.elementhandle.drag) |  | Drags an element over the given element or point. |
| [dragAndDrop(this, target, options)](https://pptr.dev/next/api/puppeteer.elementhandle.draganddrop) | `deprecated` | **Deprecated:**<br>Use `ElementHandle.drop` instead. |
| [dragEnter(this, data)](https://pptr.dev/next/api/puppeteer.elementhandle.dragenter) | `deprecated` | **Deprecated:**<br>Do not use. `dragenter` will automatically be performed during dragging. |
| [dragOver(this, data)](https://pptr.dev/next/api/puppeteer.elementhandle.dragover) | `deprecated` | **Deprecated:**<br>Do not use. `dragover` will automatically be performed during dragging. |
| [drop(this, element)](https://pptr.dev/next/api/puppeteer.elementhandle.drop) |  | Drops the given element onto the current one. |
| [drop(this, data)](https://pptr.dev/next/api/puppeteer.elementhandle.drop) | `deprecated` | **Deprecated:**<br>No longer supported. |
| [focus()](https://pptr.dev/next/api/puppeteer.elementhandle.focus) |  | Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the element. |
| [hover(this)](https://pptr.dev/next/api/puppeteer.elementhandle.hover) |  | This method scrolls element into view if needed, and then uses [Page.mouse](https://pptr.dev/next/api/puppeteer.page#mouse) to hover over the center of the element. If the element is detached from DOM, the method throws an error. |
| [isHidden()](https://pptr.dev/next/api/puppeteer.elementhandle.ishidden) |  | An element is considered to be hidden if at least one of the following is true:<br>- the element has no [computed styles](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle).<br>  <br>- the element has an empty [bounding client rect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).<br>  <br>- the element's [visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility) is `hidden` or `collapse`. |
| [isIntersectingViewport(this, options)](https://pptr.dev/next/api/puppeteer.elementhandle.isintersectingviewport) |  | Resolves to true if the element is visible in the current viewport. If an element is an SVG, we check if the svg owner element is in the viewport instead. See [https://crbug.com/963246](https://crbug.com/963246). |
| [isVisible()](https://pptr.dev/next/api/puppeteer.elementhandle.isvisible) |  | An element is considered to be visible if all of the following is true:<br>- the element has [computed styles](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle).<br>  <br>- the element has a non-empty [bounding client rect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).<br>  <br>- the element's [visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility) is not `hidden` or `collapse`. |
| [press(key, options)](https://pptr.dev/next/api/puppeteer.elementhandle.press) |  | Focuses the element, and then uses [Keyboard.down()](https://pptr.dev/next/api/puppeteer.keyboard.down) and [Keyboard.up()](https://pptr.dev/next/api/puppeteer.keyboard.up).<br>**Remarks:**<br>If `key` is a single character and no modifier keys besides `Shift` are being held down, a `keypress`/ `input` event will also be generated. The `text` option can be specified to force an input event to be generated.<br>**NOTE** Modifier keys DO affect `elementHandle.press`. Holding down `Shift` will type the text in upper case. |
| [screenshot(options)](https://pptr.dev/next/api/puppeteer.elementhandle.screenshot) |  | This method scrolls element into view if needed, and then uses [Page.screenshot()](https://pptr.dev/next/api/puppeteer.page.screenshot) to take a screenshot of the element. If the element is detached from DOM, the method throws an error. |
| [screenshot(options)](https://pptr.dev/next/api/puppeteer.elementhandle.screenshot) |  |  |
| [scrollIntoView(this)](https://pptr.dev/next/api/puppeteer.elementhandle.scrollintoview) |  | Scrolls the element into view using either the automation protocol client or by calling element.scrollIntoView. |
| [select(values)](https://pptr.dev/next/api/puppeteer.elementhandle.select) |  | Triggers a `change` and `input` event once all the provided options have been selected. If there's no `<select>` element matching `selector`, the method throws an error. |
| [tap(this)](https://pptr.dev/next/api/puppeteer.elementhandle.tap) |  | This method scrolls element into view if needed, and then uses [Touchscreen.tap()](https://pptr.dev/next/api/puppeteer.touchscreen.tap) to tap in the center of the element. If the element is detached from DOM, the method throws an error. |
| [toElement(tagName)](https://pptr.dev/next/api/puppeteer.elementhandle.toelement) |  | Converts the current handle to the given element type. |
| [touchEnd(this)](https://pptr.dev/next/api/puppeteer.elementhandle.touchend) |  |  |
| [touchMove(this, touch)](https://pptr.dev/next/api/puppeteer.elementhandle.touchmove) |  | This method scrolls the element into view if needed, and then moves the touch to the center of the element. |
| [touchStart(this)](https://pptr.dev/next/api/puppeteer.elementhandle.touchstart) |  | This method scrolls the element into view if needed, and then starts a touch in the center of the element. |
| [type(text, options)](https://pptr.dev/next/api/puppeteer.elementhandle.type) |  | Focuses the element, and then sends a `keydown`, `keypress`/ `input`, and `keyup` event for each character in the text.<br>To press a special key, like `Control` or `ArrowDown`, use [ElementHandle.press()](https://pptr.dev/next/api/puppeteer.elementhandle.press). |
| [uploadFile(this, paths)](https://pptr.dev/next/api/puppeteer.elementhandle.uploadfile) |  | Sets the value of an [input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input) to the given file paths.<br>**Remarks:**<br>This will not validate whether the file paths exists. Also, if a path is relative, then it is resolved against the [current working directory](https://nodejs.org/api/process.html#process_process_cwd). For locals script connecting to remote chrome environments, paths must be absolute. |
| [waitForSelector(selector, options)](https://pptr.dev/next/api/puppeteer.elementhandle.waitforselector) |  | Wait for an element matching the given selector to appear in the current element.<br>Unlike [Frame.waitForSelector()](https://pptr.dev/next/api/puppeteer.frame.waitforselector), this method does not work across navigations or if the element is detached from DOM. |

- [Signature](https://pptr.dev/next/api/puppeteer.elementhandle#signature)
- [Remarks](https://pptr.dev/next/api/puppeteer.elementhandle#remarks)
- [Properties](https://pptr.dev/next/api/puppeteer.elementhandle#properties)
- [Methods](https://pptr.dev/next/api/puppeteer.elementhandle#methods)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

### Search the documentation | Puppeteer
Original URL: https://pptr.dev/search

[Skip to main content](https://pptr.dev/search#__docusaurus_skipToContent_fallback)

# Search the documentation

[Search by Algolia](https://www.algolia.com/)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---


## Release Notes

### ChromeReleaseChannel type | Puppeteer
Original URL: https://pptr.dev/next/api/puppeteer.chromereleasechannel

[Skip to main content](https://pptr.dev/next/api/puppeteer.chromereleasechannel#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api/puppeteer.chromereleasechannel)** (24.9.0).



### Signature [â€‹](https://pptr.dev/next/api/puppeteer.chromereleasechannel\#signature "Direct link to Signature")

```codeBlockLines_RjmQ
export type ChromeReleaseChannel =
  | 'chrome'
  | 'chrome-beta'
  | 'chrome-canary'
  | 'chrome-dev';

```

- [Signature](https://pptr.dev/next/api/puppeteer.chromereleasechannel#signature)

pptr.dev, Puppeteer's documentation site, uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay, got it!

---

