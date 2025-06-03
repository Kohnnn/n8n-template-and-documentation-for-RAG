---
url: "https://pptr.dev/next/api"
title: "API Reference | Puppeteer"
---

[Skip to main content](https://pptr.dev/next/api#__docusaurus_skipToContent_fallback)

This is unreleased documentation for Puppeteer **Next** version.

For up-to-date documentation, see the **[latest version](https://pptr.dev/api)** (24.9.0).

Version: Next

On this page

## Classes [​](https://pptr.dev/next/api\#classes "Direct link to Classes")

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
| [Keyboard](https://pptr.dev/next/api/puppeteer.keyboard) | Keyboard provides an api for managing a virtual keyboard. The high level api is [Keyboard.type()](https://pptr.dev/next/api/puppeteer.keyboard.type), which takes raw characters and generates proper keydown, keypress/input, and keyup events on your page.<br>**Remarks:**<br>For finer control, you can use [Keyboard.down()](https://pptr.dev/next/api/puppeteer.keyboard.down), [Keyboard.up()](https://pptr.dev/next/api/puppeteer.keyboard.up), and [Keyboard.sendCharacter()](https://pptr.dev/next/api/puppeteer.keyboard.sendcharacter) to manually fire events as if they were generated from a real keyboard.<br>On macOS, keyboard shortcuts like `⌘ A` -\> Select All do not work. See [#1313](https://github.com/puppeteer/puppeteer/issues/1313).<br>The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `Keyboard` class. |
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

## Enumerations [​](https://pptr.dev/next/api\#enumerations "Direct link to Enumerations")

| Enumeration | Description |
| --- | --- |
| [BrowserContextEvent](https://pptr.dev/next/api/puppeteer.browsercontextevent) |  |
| [BrowserEvent](https://pptr.dev/next/api/puppeteer.browserevent) | All the events a [browser instance](https://pptr.dev/next/api/puppeteer.browser) may emit. |
| [InterceptResolutionAction](https://pptr.dev/next/api/puppeteer.interceptresolutionaction) |  |
| [LocatorEvent](https://pptr.dev/next/api/puppeteer.locatorevent) | All the events that a locator instance may emit. |
| [PageEvent](https://pptr.dev/next/api/puppeteer.pageevent) | All the events that a page instance may emit. |
| [TargetType](https://pptr.dev/next/api/puppeteer.targettype) |  |

## Functions [​](https://pptr.dev/next/api\#functions "Direct link to Functions")

| Function | Description |
| --- | --- |
| [connect(options)](https://pptr.dev/next/api/puppeteer.connect) |  |
| [convertCookiesPartitionKeyFromPuppeteerToCdp(partitionKey)](https://pptr.dev/next/api/puppeteer.convertcookiespartitionkeyfrompuppeteertocdp) |  |
| [defaultArgs(options)](https://pptr.dev/next/api/puppeteer.defaultargs) |  |
| [launch(options)](https://pptr.dev/next/api/puppeteer.launch) |  |
| [trimCache()](https://pptr.dev/next/api/puppeteer.trimcache) |  |

## Interfaces [​](https://pptr.dev/next/api\#interfaces "Direct link to Interfaces")

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

## Namespaces [​](https://pptr.dev/next/api\#namespaces "Direct link to Namespaces")

| Namespace | Description |
| --- | --- |
| [CDPSessionEvent](https://pptr.dev/next/api/puppeteer.cdpsessionevent) | Events that the CDPSession class emits. |

## Variables [​](https://pptr.dev/next/api\#variables "Direct link to Variables")

| Variable | Description |
| --- | --- |
| [DEFAULT\_INTERCEPT\_RESOLUTION\_PRIORITY](https://pptr.dev/next/api/puppeteer.default_intercept_resolution_priority) | The default cooperative request interception resolution priority |
| [executablePath](https://pptr.dev/next/api/puppeteer.executablepath) |  |
| [KnownDevices](https://pptr.dev/next/api/puppeteer.knowndevices) | A list of devices to be used with [Page.emulate()](https://pptr.dev/next/api/puppeteer.page.emulate). |
| [MouseButton](https://pptr.dev/next/api/puppeteer.mousebutton) | Enum of valid mouse buttons. |
| [PredefinedNetworkConditions](https://pptr.dev/next/api/puppeteer.predefinednetworkconditions) | A list of pre-defined network conditions to be used with [Page.emulateNetworkConditions()](https://pptr.dev/next/api/puppeteer.page.emulatenetworkconditions). |
| [puppeteer](https://pptr.dev/next/api/puppeteer.puppeteer) |  |

## Type Aliases [​](https://pptr.dev/next/api\#type-aliases "Direct link to Type Aliases")

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