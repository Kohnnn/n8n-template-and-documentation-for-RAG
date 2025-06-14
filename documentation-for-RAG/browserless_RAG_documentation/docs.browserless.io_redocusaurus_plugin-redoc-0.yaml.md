---
url: "https://docs.browserless.io/redocusaurus/plugin-redoc-0.yaml"
title: undefined
---

customSiteTitle: Browserless Documentation
definitions:
 FrameAddScriptTagOptions:
 type: object
 properties:
 url:
 description: URL of the script to be added.
 type: string
 path:
 description: Path to a JavaScript file to be injected into the frame.
 type: string
 content:
 description: JavaScript to be injected into the frame.
 type: string
 type:
 description: >-
 Sets the \`type\` of the script. Use \`module\` in order to load an ES2015
 module.
 type: string
 id:
 description: Sets the \`id\` of the script.
 type: string
 additionalProperties: false
 FrameAddStyleTagOptions:
 type: object
 properties:
 url:
 description: the URL of the CSS file to be added.
 type: string
 path:
 description: The path to a CSS file to be injected into the frame.
 type: string
 content:
 description: Raw CSS content to be injected into the frame.
 type: string
 additionalProperties: false
 Credentials:
 type: object
 properties:
 username:
 type: string
 password:
 type: string
 additionalProperties: false
 required:
 \- password
 \- username
 CookieParam:
 description: \|-
 Cookie parameter object used to set cookies in the page-level cookies
 API.
 type: object
 properties:
 name:
 description: Cookie name.
 type: string
 value:
 description: Cookie value.
 type: string
 url:
 description: >-
 The request-URI to associate with the setting of the cookie. This
 value can affect

 the default domain, path, and source scheme values of the created
 cookie.
 type: string
 domain:
 description: Cookie domain.
 type: string
 path:
 description: Cookie path.
 type: string
 secure:
 description: True if cookie is secure.
 type: boolean
 httpOnly:
 description: True if cookie is http-only.
 type: boolean
 sameSite:
 description: Cookie SameSite type.
 enum:
 \- Lax
 \- None
 \- Strict
 type: string
 expires:
 description: Cookie expiration date, session cookie if not set
 type: number
 priority:
 description: Cookie Priority. Supported only in Chrome.
 enum:
 \- High
 \- Low
 \- Medium
 type: string
 sameParty:
 description: True if cookie is SameParty. Supported only in Chrome.
 type: boolean
 sourceScheme:
 description: Cookie source scheme type. Supported only in Chrome.
 enum:
 \- NonSecure
 \- Secure
 \- Unset
 type: string
 partitionKey:
 description: >-
 Cookie partition key. In Chrome, it matches the top-level site the

 partitioned cookie is available in. In Firefox, it matches the

 source origin in the

 {@link https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey
 PartitionKey}.
 anyOf:
 \- $ref: '#/definitions/CookiePartitionKey'
 \- type: string
 additionalProperties: false
 required:
 \- name
 \- value
 CookiePartitionKey:
 description: Represents a cookie partition key in Chrome.
 type: object
 properties:
 sourceOrigin:
 description: >-
 The site of the top-level URL the browser was visiting at the start of
 the request

 to the endpoint that set the cookie.

 In Chrome, maps to the CDP's \`topLevelSite\` partition key.
 type: string
 hasCrossSiteAncestor:
 description: \|-
 Indicates if the cookie has any ancestors that are cross-site to
 the topLevelSite.

 Supported only in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- sourceOrigin
 GoToOptions:
 type: object
 properties:
 referer:
 description: >-
 If provided, it will take preference over the referer header value set
 by

 {@link Page.setExtraHTTPHeaderspage.setExtraHTTPHeaders()}.
 type: string
 referrerPolicy:
 description: >-
 If provided, it will take preference over the referer-policy header
 value

 set by {@link Page.setExtraHTTPHeaderspage.setExtraHTTPHeaders()}.
 type: string
 timeout:
 description: >-
 Maximum wait time in milliseconds. Pass 0 to disable the timeout.

 The default value can be changed by using the

 {@link Page.setDefaultTimeout} or {@link
 Page.setDefaultNavigationTimeout}

 methods.
 type: number
 waitUntil:
 description: >-
 When to consider waiting succeeds. Given an array of event strings,
 waiting

 is considered to be successful after all events have been fired.
 anyOf:
 \- type: array
 items:
 $ref: '#/definitions/PuppeteerLifeCycleEvent'
 \- enum:
 \- domcontentloaded
 \- load
 \- networkidle0
 \- networkidle2
 type: string
 signal:
 description: A signal object that allows you to cancel the call.
 $ref: '#/definitions/AbortSignal'
 additionalProperties: false
 PuppeteerLifeCycleEvent:
 enum:
 \- domcontentloaded
 \- load
 \- networkidle0
 \- networkidle2
 type: string
 AbortSignal:
 type: object
 properties:
 aborted:
 type: boolean
 onabort:
 anyOf:
 \- type: object
 additionalProperties: false
 \- type: 'null'
 reason: {}
 additionalProperties: false
 required:
 \- aborted
 \- onabort
 \- reason
 Partial:
 type: object
 properties:
 status:
 type: number
 headers:
 description: \|-
 Optional response headers.

 The record values will be converted to string following:
 Arrays' values will be mapped to String
 (Used when you need multiple headers with the same name).
 Non-arrays will be converted to String.
 $ref: '#/definitions/Record'
 contentType:
 type: string
 body:
 anyOf:
 \- type: object
 additionalProperties: false
 patternProperties:
 ^\[0-9\]+$:
 type: number
 properties:
 BYTES\_PER\_ELEMENT:
 type: number
 buffer:
 $ref: '#/definitions/ArrayBufferLike'
 byteLength:
 type: number
 byteOffset:
 type: number
 length:
 type: number
 \_\_@toStringTag@14939:
 type: string
 const: Uint8Array
 required:
 \- BYTES\_PER\_ELEMENT
 \- \_\_@toStringTag@14939
 \- buffer
 \- byteLength
 \- byteOffset
 \- length
 \- type: string
 additionalProperties: false
 Record:
 type: object
 additionalProperties: false
 ArrayBufferLike:
 anyOf:
 \- $ref: '#/definitions/ArrayBuffer'
 \- $ref: '#/definitions/SharedArrayBuffer'
 ArrayBuffer:
 type: object
 properties:
 byteLength:
 type: number
 \_\_@toStringTag@14939:
 type: string
 additionalProperties: false
 required:
 \- \_\_@toStringTag@14939
 \- byteLength
 SharedArrayBuffer:
 type: object
 properties:
 byteLength:
 type: number
 \_\_@species@14977:
 $ref: '#/definitions/SharedArrayBuffer'
 \_\_@toStringTag@14939:
 type: string
 const: SharedArrayBuffer
 additionalProperties: false
 required:
 \- \_\_@species@14977
 \- \_\_@toStringTag@14939
 \- byteLength
 Record:
 type: object
 additionalProperties: false
 Viewport:
 type: object
 properties:
 width:
 description: The page width in CSS pixels.
 type: number
 height:
 description: The page height in CSS pixels.
 type: number
 deviceScaleFactor:
 description: >-
 Specify device scale factor.

 See {@link
 https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio
 devicePixelRatio} for more info.
 type: number
 isMobile:
 description: Whether the \`meta viewport\` tag is taken into account.
 type: boolean
 isLandscape:
 description: Specifies if the viewport is in landscape mode.
 type: boolean
 hasTouch:
 description: Specify if the viewport supports touch events.
 type: boolean
 additionalProperties: false
 required:
 \- height
 \- width
 CDPLaunchOptions:
 type: object
 properties:
 args:
 type: array
 items:
 type: string
 defaultViewport:
 type: object
 properties:
 deviceScaleFactor:
 type: number
 hasTouch:
 type: boolean
 height:
 type: number
 isLandscape:
 type: boolean
 isMobile:
 type: boolean
 width:
 type: number
 additionalProperties: false
 required:
 \- height
 \- width
 devtools:
 type: boolean
 dumpio:
 type: boolean
 headless:
 enum:
 \- false
 \- shell
 \- true
 ignoreDefaultArgs:
 anyOf:
 \- type: array
 items:
 type: string
 \- type: boolean
 ignoreHTTPSErrors:
 type: boolean
 slowMo:
 type: number
 stealth:
 type: boolean
 timeout:
 type: number
 userDataDir:
 type: string
 waitForInitialPage:
 type: boolean
 additionalProperties: false
 BrowserServerOptions:
 type: object
 properties:
 args:
 type: array
 items:
 type: string
 chromiumSandbox:
 type: boolean
 devtools:
 type: boolean
 downloadsPath:
 type: string
 headless:
 type: boolean
 ignoreDefaultArgs:
 anyOf:
 \- type: array
 items:
 type: string
 \- type: boolean
 proxy:
 type: object
 properties:
 bypass:
 type: string
 password:
 type: string
 server:
 type: string
 username:
 type: string
 additionalProperties: false
 required:
 \- server
 timeout:
 type: number
 tracesDir:
 type: string
 additionalProperties: false
 JSONSchema:
 type: object
 properties:
 code:
 type: string
 context:
 $ref: '#/definitions/Record'
 additionalProperties: false
 required:
 \- code
 Record:
 type: object
 additionalProperties: false
 CDPJSONPayload:
 type: object
 properties:
 description:
 description: The description of the target. Generally the page's title.
 type: string
 devtoolsFrontendUrl:
 description: The fully-qualified URL of the Devtools inspector app.
 type: string
 id:
 description: A Unique Id for the underlying target.
 type: string
 title:
 description: The title of the target. For pages this is the page's title.
 type: string
 type:
 description: The type of target, generally "page" or "background\_page".
 type: string
 url:
 description: The current URL the target is consuming or visiting.
 type: string
 webSocketDebuggerUrl:
 description: \|-
 The target or page's WebSocket Debugger URL. Primarily used for legacy
 libraries to connect and inspect or remote automate this target.
 type: string
 additionalProperties: false
 required:
 \- description
 \- devtoolsFrontendUrl
 \- id
 \- title
 \- type
 \- url
 \- webSocketDebuggerUrl
 PDFOptions:
 description: Valid options to configure PDF generation via {@link Page.pdf}.
 type: object
 properties:
 scale:
 description: >-
 Scales the rendering of the web page. Amount must be between \`0.1\` and
 \`2\`.
 type: number
 displayHeaderFooter:
 description: Whether to show the header and footer.
 type: boolean
 headerTemplate:
 description: >-
 HTML template for the print header. Should be valid HTML with the
 following

 classes used to inject values into them:

 \- \`date\` formatted print date

 \- \`title\` document title

 \- \`url\` document location

 \- \`pageNumber\` current page number

 \- \`totalPages\` total pages in the document
 type: string
 footerTemplate:
 description: >-
 HTML template for the print footer. Has the same constraints and
 support

 for special classes as {@link PDFOptions.headerTemplate}.
 type: string
 printBackground:
 description: Set to \`true\` to print background graphics.
 type: boolean
 landscape:
 description: Whether to print in landscape orientation.
 type: boolean
 pageRanges:
 description: Paper ranges to print, e.g. \`1-5, 8, 11-13\`.
 type: string
 format:
 description: All the valid paper format types when printing a PDF.
 enum:
 \- A0
 \- A1
 \- A2
 \- A3
 \- A4
 \- A5
 \- A6
 \- LEDGER
 \- LEGAL
 \- LETTER
 \- Ledger
 \- Legal
 \- Letter
 \- TABLOID
 \- Tabloid
 \- a0
 \- a1
 \- a2
 \- a3
 \- a4
 \- a5
 \- a6
 \- ledger
 \- legal
 \- letter
 \- tabloid
 type: string
 width:
 description: >-
 Sets the width of paper. You can pass in a number or a string with a
 unit.
 type:
 \- string
 \- number
 height:
 description: >-
 Sets the height of paper. You can pass in a number or a string with a
 unit.
 type:
 \- string
 \- number
 preferCSSPageSize:
 description: \|-
 Give any CSS \`@page\` size declared in the page priority over what is
 declared in the \`width\` or \`height\` or \`format\` option.
 type: boolean
 margin:
 description: Set the PDF margins.
 $ref: '#/definitions/PDFMargin'
 path:
 description: The path to save the file to.
 type: string
 omitBackground:
 description: >-
 Hides default white background and allows generating pdfs with
 transparency.
 type: boolean
 tagged:
 description: Generate tagged (accessible) PDF.
 type: boolean
 outline:
 description: Generate document outline.
 type: boolean
 timeout:
 description: >-
 Timeout in milliseconds. Pass \`0\` to disable timeout.

 The default value can be changed by using {@link
 Page.setDefaultTimeout}
 type: number
 waitForFonts:
 description: >-
 If true, waits for \`document.fonts.ready\` to resolve. This might
 require

 activating the page using {@link Page.bringToFront} if the page is in
 the

 background.
 type: boolean
 additionalProperties: false
 PDFMargin:
 type: object
 properties:
 top:
 type:
 \- string
 \- number
 bottom:
 type:
 \- string
 \- number
 left:
 type:
 \- string
 \- number
 right:
 type:
 \- string
 \- number
 additionalProperties: false
 ScrapeDebugOptions:
 type: object
 properties:
 console:
 type: boolean
 cookies:
 type: boolean
 html:
 type: boolean
 network:
 type: boolean
 screenshot:
 type: boolean
 additionalProperties: false
 ScrapeElementSelector:
 type: object
 properties:
 selector:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- selector
 Cookie:
 description: Represents a cookie object.
 type: object
 properties:
 name:
 description: Cookie name.
 type: string
 value:
 description: Cookie value.
 type: string
 domain:
 description: Cookie domain.
 type: string
 path:
 description: Cookie path.
 type: string
 expires:
 description: >-
 Cookie expiration date as the number of seconds since the UNIX epoch.
 Set to \`-1\` for

 session cookies
 type: number
 size:
 description: Cookie size.
 type: number
 httpOnly:
 description: True if cookie is http-only.
 type: boolean
 secure:
 description: True if cookie is secure.
 type: boolean
 session:
 description: True in case of session cookie.
 type: boolean
 sameSite:
 description: Cookie SameSite type.
 enum:
 \- Lax
 \- None
 \- Strict
 type: string
 priority:
 description: Cookie Priority. Supported only in Chrome.
 enum:
 \- High
 \- Low
 \- Medium
 type: string
 sameParty:
 description: True if cookie is SameParty. Supported only in Chrome.
 type: boolean
 sourceScheme:
 description: Cookie source scheme type. Supported only in Chrome.
 enum:
 \- NonSecure
 \- Secure
 \- Unset
 type: string
 partitionKey:
 description: >-
 Cookie partition key. In Chrome, it is the top-level site the

 partitioned cookie is available in. In Firefox, it matches the

 source origin in the

 {@link https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey
 PartitionKey}.
 anyOf:
 \- $ref: '#/definitions/CookiePartitionKey'
 \- type: string
 partitionKeyOpaque:
 description: True if cookie partition key is opaque. Supported only in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- domain
 \- expires
 \- httpOnly
 \- name
 \- path
 \- secure
 \- session
 \- size
 \- value
 InBoundRequest:
 type: object
 properties:
 headers: {}
 status:
 type: number
 url:
 type: string
 additionalProperties: false
 required:
 \- headers
 \- status
 \- url
 OutBoundRequest:
 type: object
 properties:
 headers: {}
 method:
 type: string
 url:
 type: string
 additionalProperties: false
 required:
 \- headers
 \- method
 \- url
 ScreenshotOptions:
 type: object
 properties:
 optimizeForSpeed:
 type: boolean
 type:
 enum:
 \- jpeg
 \- png
 \- webp
 type: string
 quality:
 description: Quality of the image, between 0-100. Not applicable to \`png\` images.
 type: number
 fromSurface:
 description: Capture the screenshot from the surface, rather than the view.
 type: boolean
 fullPage:
 description: When \`true\`, takes a screenshot of the full page.
 type: boolean
 omitBackground:
 description: >-
 Hides default white background and allows capturing screenshots with
 transparency.
 type: boolean
 path:
 description: >-
 The file path to save the image to. The screenshot type will be
 inferred

 from file extension. If path is a relative path, then it is resolved

 relative to current working directory. If no path is provided, the
 image

 won't be saved to the disk.
 type: string
 clip:
 description: Specifies the region of the page/element to clip.
 $ref: '#/definitions/ScreenshotClip'
 encoding:
 description: Encoding of the image.
 enum:
 \- base64
 \- binary
 type: string
 captureBeyondViewport:
 description: Capture the screenshot beyond the viewport.
 type: boolean
 additionalProperties: false
 ScreenshotClip:
 type: object
 properties:
 scale:
 type: number
 width:
 description: the width of the element in pixels.
 type: number
 height:
 description: the height of the element in pixels.
 type: number
 x:
 type: number
 'y':
 type: number
 additionalProperties: false
 required:
 \- height
 \- width
 \- x
 \- 'y'
 import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions:
 type: object
 properties:
 args:
 type: array
 items:
 type: string
 defaultViewport:
 type: object
 properties:
 deviceScaleFactor:
 type: number
 hasTouch:
 type: boolean
 height:
 type: number
 isLandscape:
 type: boolean
 isMobile:
 type: boolean
 width:
 type: number
 additionalProperties: false
 required:
 \- height
 \- width
 devtools:
 type: boolean
 dumpio:
 type: boolean
 headless:
 enum:
 \- false
 \- shell
 \- true
 ignoreDefaultArgs:
 anyOf:
 \- type: array
 items:
 type: string
 \- type: boolean
 ignoreHTTPSErrors:
 type: boolean
 slowMo:
 type: number
 stealth:
 type: boolean
 timeout:
 type: number
 userDataDir:
 type: string
 waitForInitialPage:
 type: boolean
 additionalProperties: false
 CookieSameSite:
 description: \|-
 Represents the cookie's 'SameSite' status:
 https://tools.ietf.org/html/draft-west-first-party-cookies
 enum:
 \- Lax
 \- None
 \- Strict
 type: string
 CookiePriority:
 description: \|-
 Represents the cookie's 'Priority' status:
 https://tools.ietf.org/html/draft-west-cookie-priority-00
 enum:
 \- High
 \- Low
 \- Medium
 type: string
 CookieSourceScheme:
 description: >-
 Represents the source scheme of the origin that originally set the cookie.
 A value of

 "Unset" allows protocol clients to emulate legacy cookie scope for the
 scheme.

 This is a temporary ability and it will be removed in the future.
 enum:
 \- NonSecure
 \- Secure
 \- Unset
 type: string
 PaperFormat:
 description: All the valid paper format types when printing a PDF.
 enum:
 \- A0
 \- A1
 \- A2
 \- A3
 \- A4
 \- A5
 \- A6
 \- LEDGER
 \- LEGAL
 \- LETTER
 \- Ledger
 \- Legal
 \- Letter
 \- TABLOID
 \- Tabloid
 \- a0
 \- a1
 \- a2
 \- a3
 \- a4
 \- a5
 \- a6
 \- ledger
 \- legal
 \- letter
 \- tabloid
 type: string
 import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).BrowserServerOptions:
 type: object
 properties:
 args:
 type: array
 items:
 type: string
 chromiumSandbox:
 type: boolean
 devtools:
 type: boolean
 downloadsPath:
 type: string
 headless:
 type: boolean
 ignoreDefaultArgs:
 anyOf:
 \- type: array
 items:
 type: string
 \- type: boolean
 proxy:
 type: object
 properties:
 bypass:
 type: string
 password:
 type: string
 server:
 type: string
 username:
 type: string
 additionalProperties: false
 required:
 \- server
 timeout:
 type: number
 tracesDir:
 type: string
 additionalProperties: false
info:
 title: Browserless
 version: 2.30.1
 x-logo:
 altText: browserless logo
 url: ./docs/browserless-logo-inline.svg
 description: >
 # Browserless.io

 This service extends the Browserless open-source image with many features
 and enhancements for teams automating at scale. Notable features include:

 \- A Chrome-devtools-protocol based API for extending and enhancing libraries
 in a cross-language way.

 \- A new hybrid-automation toolkit with live session interactivity.

 \- Robust session management: connect, reconnect, kill and limit what a
 browser can do.

 \- Bleeding features like multiplexing numerous clients into a single Chrome
 process in an isolated way.

 \- The ability to upload and run custom extensions.

 \- Run multiple tokens, with access controls on each.

 \- Multi-browser with all the robust capabilities already in the open-source
 images.

 There's a lot to cover here so let's get started!

 # Software Keys

 The Enterprise image supports time-limited software keys that allow usage
 for a specific period without requiring any external connections or
 callbacks. These keys are cryptographically secure and cannot be reverse
 engineered. When a key expires, the container will exit with a semantic
 error code.

 ## Using a Software Key

 To use a software key, set the \`KEY\` environment variable when running the
 container:

 \`\`\`bash

 docker run -e KEY=your-generated-key browserless/enterprise

 \`\`\`

 # Using the Browserless Proxy

 \> The Residential proxy is only available for Enterprise and Cloud plans.

 Browserless comes with a built-in mechanism to proxy to what's called
 "residential" IPs. These are IP addresses are sourced from real-users
 running a proxy server on their home networking machines. Residential
 proxying is especially useful for things like bypassing certain bot
 blockages and more.

 Using a residential proxy is as straightforward as adding a few parameters
 to your library or API calls. Here's the required parameters and the values
 they support:

 \- \`?proxy=residential\`: Specifies that you want to use the residential proxy
 for this request. Data-center coming soon.

 \- \`?proxyCountry=us\`: Specifies a country you wish to use for the request. A
 two-digit ISO code.

 \- \`?proxySticky=true\`: If you want to use the same IP address for the
 entirety of the session. Generally recommended for most cases.

 Simply append these to your connection call, REST API calls, or any library
 call:

 \`wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN&proxy=residential&proxyCountry=us&proxySticky\`

 \`https://production-sfo.browserless.io/chromium/unblock?token=YOUR-API-TOKEN&proxy=residential&proxyCountry=us&proxySticky\`

 Please do note that using a proxy will increase the amount of units
 consumed. Every megabyte of data transferred consumes 6 units.

 # The Browserless CDP API

 In order to enhance the experience with open source libraries like
 Puppeteer, we decided to take a new approach to extending these libraries in
 a language-agnostic way. We call it the Browserless CDP API. Here's a quick
 list of what it can do:

 \- Generate and give back live URLs for hybrid automation.

 \- Solve Captchas.

 \- Return your page's unique identifier created by Chrome.

 \- Way more coming!

 Since most libraries come with a way to issue "raw" CDP commands, it's an
 easy way to drop-in custom behaviors without having to write and maintain a
 library. Plus you can continue to enjoy using the same packages you've
 already come to know.

 Getting started with this API is pretty simple. For instance, if you want to
 use the live viewer for a particular page, simply do the following:

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint = 'wss://production-sfo.browserless.io/chromium';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');
 const { liveURL } = await cdp.send('Browserless.liveURL');

 // liveURL = 'http://localhost:3000/live/?i=98e83bbfd396241a6963425b1feeba2f';
 })();

 \`\`\`

 You can then visit this URL in any browser to interact with the headless
 Chrome running someplace else.

 See more below for a full list of the available APIs and features.

 ## Browserless.liveURL

 \> This API is only available for Enterprise plans. \[Contact us for more\
 information here.\](https://www.browserless.io/contact/)

 Returns a fully-qualified URL to load into a web-browser. This URL allows
 for clicking, typing and other interactions with the underlying page. This
 URL doesn't require an authorization token, so you're free to share it
 externally with your own users or employees. If security is a concern, you
 can set a \`timeout\` parameter to limit the amount of time this URL is valid
 for. By default no \`timeout\` is set and the URL is good as long as the
 underlying browser is open.

 Programmatic control of the session is also available, so you can close the
 live session once your code has detected a selector, network call, or
 whatever else. See the below example for programmatic control.

 \*\*Basic example\*\*

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint =
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');
 const { liveURL } = await cdp.send('Browserless.liveURL');

 // liveURL = 'https://production-sfo.browserless.io/live/?i=98e83bbfd396241a6963425b1feeba2f';
 })();

 \`\`\`

 \*\*Timeout example\*\*

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint =
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');
 const { liveURL } = await cdp.send('Browserless.liveURL', {
 timeout: 10000, // 10 seconds to connect!
 });

 // liveURL = 'https://production-sfo.browserless.io/live/?i=98e83bbfd396241a6963425b1feeba2f';
 })();

 \`\`\`

 \*\*Maintaining the width and height\*\*

 By default, Browserless will dynamically change the width and height of the
 browser to match an end-users screen. This isn't always ideal and can be
 disabled by setting a \`resizable\` value to \`false\`. When this is done, only
 your script can alter the width and height of the browser:

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint =
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();

 // Width and height will always be 1920x1080
 // and the Live URL will maintain this aspect ratio
 await page.setViewport({ width: 1920, height: 1080 });
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');
 const { liveURL } = await cdp.send('Browserless.liveURL', {
 resizable: false,
 });

 // liveURL = 'https://production-sfo.browserless.io/live/?i=98e83bbfd396241a6963425b1feeba2f';
 })();

 \`\`\`

 \*\*Setting a Quality and Type\*\*

 Setting a "quality" and "type" effects the streamed quality of the live
 URL's client-side resolution. By default, Browserless sets these to quality:
 100 and type of "png". You can experiment different settings to get an ideal
 resolutions while keep latency slow. The close to 100 quality is, the
 potential for higher perceived latency.

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint =
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');
 const { liveURL } = await cdp.send('Browserless.liveURL', {
 quality: 100, // Can be 1 - 100
 type: 'png', // Can be 'jpeg' or 'png'
 });

 // liveURL = 'https://production-sfo.browserless.io/live/?i=98e83bbfd396241a6963425b1feeba2f';
 })();

 \`\`\`

 It's also helpful to "wait" until the user is done doing what's needed. For
 that reason, Browserless will fire a custom event when the page is closed as
 well:

 \*\*Wait for close\*\*

 \> Custom CDP Events are not supported in all libraries, including .NET
 Playwright.

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint =
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');

 const { liveURL } = await cdp.send('Browserless.liveURL');

 console.log(liveURL);

 // Wait for the Browserless.liveComplete event when the live page is closed.
 // Please not that not all libraries support custom CDP events.
 await new Promise((r) => cdp.on('Browserless.liveComplete', r));

 console.log('Done!');

 await browser.close();
 })();

 \`\`\`

 \*\*Programmatic Control\*\*

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint =
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');

 // Having the liveURLId is required in order to close it later
 const { liveURL, liveURLId } = await cdp.send('Browserless.liveURL');

 await page.waitForSelector('.my-selector');

 // Calling this CDP API with the "liveURLId" will close the session, and terminate the client
 // further usage of the liveURL will fail and no more human-control is possible
 await cdp.send('Browserless.closeLiveURL', { liveURLId });

 // Continue to process or interact with the browser, then:
 await browser.close();
 })();

 \`\`\`

 It's recommended that you double check the page prior to executing further
 code to make sure the page is where it should be, elements are present, and
 so forth. This approach makes it easy to solve hard things like
 second-factor authentication and more in a trivial fashion.

 \*\*Read-only LiveURL Sessions\*\*

 The \`interactive: false\` option allows you to create read-only LiveURL
 sessions where users can view the browser but cannot interact with it. This
 is useful for monitoring or demonstration purposes without allowing user
 input.

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint =
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');

 // Create a read-only LiveURL session that users can view but not interact with
 const { liveURL } = await cdp.send('Browserless.liveURL', {
 interactive: false,
 });

 console.log('Read-only LiveURL:', liveURL);

 await browser.close();
 })();

 \`\`\`

 ## Browserless.reconnect

 \> This API is only available for Enterprise plans. \[Contact us for more\
 information here.\](https://www.browserless.io/contact/)

 Reconnecting allows for the underlying Chrome or Chromium process to
 continue to run for a specified amount of time, and subsequent reconnecting
 back to it. With this approach you can also "share" this connection URL to
 other clients to connect to the same browser process, allowing you to
 parallelize via a single Browser process.

 Once a reconnection URL is retrieved, Browserless will intercept close-based
 commands and stop them from terminating the browser process itself. This
 prevents clients from accidentally closing the process via \`browser.close\`
 or similar.

 In order to use this API, simply call \`Browserless.reconnect\` as a CDP
 command. You can, optionally, set a \`timeout\` or an \`auth\` property. See the
 below examples for details

 \*\*Basic example with timeout\*\*

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint =
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');

 // Allow this browser to run for 10 seconds, then shut down if nothing connects to it.
 // Defaults to the overall timeout set on the instance, which is 5 minutes if not specified.
 const { error, browserWSEndpoint } = await cdp.send('Browserless.reconnect', {
 timeout: 10000,
 });

 if (error) throw error;

 await browser.close();

 // browserWSEndpoint = 'https://production-sfo.browserless.io/reconnect/98e83bbfd396241a6963425b1feeba2f';
 })();

 \`\`\`

 If you want to enforce authentication, you can pass in an optional \`auth\`
 property that clients will need to use in order to connect with. Similar to
 how authentication works in general, a \`token\` query-string parameter will
 need to be applied.

 \*\*Authentication example\*\*

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint =
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');

 // Set a custom authentication token that clients have to use in order to connect, or otherwise
 // receive a 401 Response.
 const { error, browserWSEndpoint } = await cdp.send('Browserless.reconnect', {
 auth: 'secret-auth-token',
 });

 if (error) throw error;

 await browser.close();

 // NOTE the URL here doesn't include the auth token!
 // browserWSEndpoint = 'https://production-sfo.browserless.io/reconnect/98e83bbfd396241a6963425b1feeba2f';
 })();

 \`\`\`

 \*\*Recursive Example\*\*

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 const job = async (reconnectURL) => {
 const browserWSEndpoint =
 reconnectURL ??
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const \[page\] = await browser.page();
 const cdp = await page.createCDPSession();
 await page.goto('https://example.com');

 // Anytime Browserless.reconnect is called, this restarts the timer back to the provided value,
 // effectively "bumping" the timer forward.
 const res = await cdp.send('Browserless.reconnect', {
 timeout: 30000,
 });

 if (res.error) throw error;

 await browser.close();

 // Continuously reconnect back...
 return job(res.browserWSEndpoint);
 };

 job().catch((e) => console.error(e));

 \`\`\`

 ## Browserless.solveCaptcha

 \> This API is only available for Enterprise and Scale and above plans on
 Cloud. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/). Only the \`/chrome\` and
 \`/chromium\` routes support Captcha solving.

 Browserless comes with built-in captcha solving capabilities. We use a
 variety of techniques to try and mitigate the chances of captchas coming up,
 but if you happen to run into one you can simply call on our API to solve
 it.

 Given the amount of possibilities during a captcha solve, the API returns
 many properties and information in order to help your script be more
 informed as to what happened. See the below code example for all details and
 fields returned by the API.

 Please be aware that solving a captcha can take a few seconds up to several
 minutes, so you'll want to increase your timeouts accordingly for your
 scripts. Captcha's solved, or attempted to solve, cost 10 units.

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browser = await puppeteer.connect({
 browserWSEndpoint:
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN&timeout=300000',
 });

 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 await page.goto('https://www.google.com/recaptcha/api2/demo', {
 waitUntil: 'networkidle0',
 });

 const {
 // A simple boolean indicating whether the script can proceed
 ok,
 // Whether or not a captcha was found
 captchaFound,
 // A human-readable description of what occurred.
 message,
 // Whether a solve was attempted or not
 solveAttempted,
 // If the Captcha was solved, only true if found AND solved
 solved,
 // Any errors during execution are saved here:
 error,
 } = await cdp.send('Browserless.solveCaptcha', {
 // How long to wait for a Captcha to appear to solve.
 // Defaults to 10,000ms, or 10 seconds.
 appearTimeout: 30000,
 });

 console.log(message);

 if (ok) {
 await page.click('#recaptcha-demo-submit');
 } else {
 console.error(\`Error solving captcha!\`);
 }

 await browser.close();
 })().catch((e) => {
 console.error(e);
 process.exit(1);
 });

 \`\`\`

 In general, if an \`ok\` response is sent back from this API, then your script
 is good to proceed with further actions. If a captcha is to suddenly appears
 after an action then you might want to listen for the
 \`Browserless.foundCaptcha\` event (see below) and retry solving.

 ## Browserless.foundCaptcha

 \> This API is only available for Enterprise and Scale and above plans on
 Cloud. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/). Only the \`/chrome\` and
 \`/chromium\` routes support Captcha solving.

 \> Custom CDP Events are not supported in all libraries, including .NET
 Playwright.

 Emitted whenever a captcha widget is found on the page. Useful for checking
 if there's a captcha and deciding whether or not to proceed with solving.

 The example below stops until a captcha is found, which may or may not be
 the case with every website out there.

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 // Recaptcha

 (async () => {
 const browser = await puppeteer.connect({
 browserWSEndpoint:
 'wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN&timeout=300000',
 });

 const page = await browser.newPage();
 const cdp = await page.createCDPSession();

 await page.goto('https://www.google.com/recaptcha/api2/demo', {
 waitUntil: 'networkidle0',
 });

 // Please note that not all libraries support custom CDP events.
 await new Promise((resolve) =>
 cdp.on('Browserless.captchaFound', () => {
 console.log('Found a captcha!');
 return resolve();
 }),
 );

 const { solved, error } = await cdp.send('Browserless.solveCaptcha');
 console.log({
 solved,
 error,
 });

 // Continue...
 await page.click('#recaptcha-demo-submit');
 })().catch((e) => {
 console.error(e);
 process.exit(1);
 });

 \`\`\`

 ## Browserless.heartbeat

 \> This API is only available for Enterprise hosted and Starter and above
 plans on Cloud. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/).

 \> Custom CDP Events are not supported in all libraries, including .NET
 Playwright.

 A custom event emitted every several seconds, signaling a live connection.
 This is useful for a few reasons:

 \- It ensure that your connection with the browser is still good.

 \- Sending data can trigger some load-balancing technologies to not kill the
 connection.

 Today this event is emitted every 30 seconds.

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 const browserWSEndpoint =
 \`wss://production-sfo.browserless.io/chromium?token=YOUR-API-TOKEN\`;

 (async () => {
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 await page.goto('https://example.com/');
 const client = await page.createCDPSession();

 client.on('Browserless.heartbeat', () => {
 console.log('Browserless.heartbeat');
 });
 })();

 \`\`\`

 ## Browserless.pageId

 \> This API is only available for Enterprise hosted and Starter and above
 plans on Cloud. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/).

 A simple helper utility to return the page's unique ID. Since most libraries
 treat this ID as opaque, and some even hide it, knowing the page's ID can be
 of great help when interacting with other parts of Browserless.

 \`\`\`js

 import puppeteer from 'puppeteer-core';

 (async () => {
 const browserWSEndpoint = 'wss://production-sfo.browserless.io/chromium';
 const browser = await puppeteer.connect({ browserWSEndpoint });
 const page = await browser.newPage();
 const cdp = await page.createCDPSession();
 const { pageId } = await cdp.send('Browserless.pageId');

 // pageId = 'ABC12354AFDC123';
 })();

 \`\`\`

 You can, optionally, try and "find" this ID in puppeteer or similar
 libraries. Given that puppeteer has this property underscored, it's likely
 to change or be unavailable in the future, and requires the infamous \`//
 @ts-ignore\` comment to allow TypeScript compilation.

 \`\`\`ts

 const getPageId = (page: Page): string => {
 // @ts-ignore
 return page.target().\_targetId;
 };

 \`\`\`

 # Changelog
openapi: 3.0.0
paths:
 /chrome/content:
 post:
 definitions: {}
 description: >-
 A JSON-based API. Given a "url" or "html" field, runs and returns HTML
 content after the page has loaded and JavaScript has parsed.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 description: Whether or not to allow JavaScript to run on the page.
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 text/html:
 schema:
 description: \|-
 An HTML payload of the website or HTML after JavaScript
 parsing and execution.
 type: string
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 An HTML payload of the website or HTML after JavaScript
 parsing and execution.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/content
 tags:
 \- Browser REST APIs
 /chrome/download:
 post:
 definitions: {}
 description: >-
 A JSON or JavaScript content-type API for returning files Chrome has
 downloaded during

 the execution of puppeteer code, which is ran inside context of the
 browser.

 Browserless sets up a blank page, a fresh download directory, injects
 your puppeteer code, and then executes it.

 You can load external libraries via the "import" syntax, and import
 ESM-style modules

 that are written for execution inside of the browser. Once your script
 is finished, any

 downloaded files from Chromium are returned back with the appropriate
 content-type header.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 $ref: '#/definitions/JSONSchema'
 application/javascript:
 schema:
 type: string
 responses:
 '200':
 content:
 '\*/\*':
 schema:
 description: >-
 Responses are determined by the returned value of the
 downloads

 themselves, so there isn't a static response type for this
 API.
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 Responses are determined by the returned value of the downloads
 themselves, so there isn't a static response type for this API.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/download
 tags:
 \- Browser REST APIs
 /chrome/function:
 post:
 definitions: {}
 description: >-
 A JSON or JavaScript content-type API for running puppeteer code in the
 browser's context.

 Browserless sets up a blank page, injects your puppeteer code, and runs
 it.

 You can optionally load external libraries via the "import" module that
 are meant for browser usage.

 Values returned from the function are checked and an appropriate
 content-type and response is sent back

 to your HTTP call.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 $ref: '#/definitions/JSONSchema'
 application/javascript:
 schema:
 type: string
 responses:
 '200':
 content:
 '\*/\*':
 schema:
 description: >-
 Responses are determined by the returned value of the function

 itself. Binary responses (PDF's, screenshots) are returned
 back

 as binary data, and primitive JavaScript values are returned
 back

 by type (HTML data is "text/html", Objects are
 "application/json")
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 Responses are determined by the returned value of the function
 itself. Binary responses (PDF's, screenshots) are returned back
 as binary data, and primitive JavaScript values are returned back
 by type (HTML data is "text/html", Objects are "application/json")
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/function
 tags:
 \- Browser REST APIs
 /json/list:
 get:
 definitions: {}
 description: >-
 Returns a JSON payload that acts as a pass-through to the DevTools
 /json/list HTTP API in Chromium and Chrome.

 Browserless crafts this payload so that remote clients can connect to
 the underlying "webSocketDebuggerUrl"

 properly, excluding any API tokens in that URL. If under authentication
 be sure to include your authorization.
 parameters: \[\]
 requestBody:
 content: {}
 responses:
 '200':
 content:
 application/json:
 schema:
 type: array
 items:
 $ref: '#/definitions/CDPJSONPayload'
 definitions:
 CDPJSONPayload:
 type: object
 properties:
 description:
 description: >-
 The description of the target. Generally the page's
 title.
 type: string
 devtoolsFrontendUrl:
 description: The fully-qualified URL of the Devtools inspector app.
 type: string
 id:
 description: A Unique Id for the underlying target.
 type: string
 title:
 description: >-
 The title of the target. For pages this is the page's
 title.
 type: string
 type:
 description: >-
 The type of target, generally "page" or
 "background\_page".
 type: string
 url:
 description: The current URL the target is consuming or visiting.
 type: string
 webSocketDebuggerUrl:
 description: >-
 The target or page's WebSocket Debugger URL. Primarily
 used for legacy

 libraries to connect and inspect or remote automate
 this target.
 type: string
 additionalProperties: false
 required:
 \- description
 \- devtoolsFrontendUrl
 \- id
 \- title
 \- type
 \- url
 \- webSocketDebuggerUrl
 $schema: http://json-schema.org/draft-07/schema#
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /json/list
 tags:
 \- Browser REST APIs
 /json/new:
 put:
 definitions: {}
 description: >-
 Returns a JSON payload that acts as a pass-through to the DevTools
 /json/new HTTP API in Chromium.

 Browserless mocks this payload so that remote clients can connect to the
 underlying "webSocketDebuggerUrl"

 which will cause Browserless to start the browser and proxy that request
 into a blank page.
 parameters: \[\]
 requestBody:
 content: {}
 responses:
 '200':
 content:
 application/json:
 schema:
 type: object
 properties:
 description:
 description: The description of the target. Generally the page's title.
 type: string
 devtoolsFrontendUrl:
 description: The fully-qualified URL of the Devtools inspector app.
 type: string
 id:
 description: A Unique Id for the underlying target.
 type: string
 title:
 description: >-
 The title of the target. For pages this is the page's
 title.
 type: string
 type:
 description: The type of target, generally "page" or "background\_page".
 type: string
 url:
 description: The current URL the target is consuming or visiting.
 type: string
 webSocketDebuggerUrl:
 description: >-
 The target or page's WebSocket Debugger URL. Primarily
 used for legacy

 libraries to connect and inspect or remote automate this
 target.
 type: string
 additionalProperties: false
 required:
 \- description
 \- devtoolsFrontendUrl
 \- id
 \- title
 \- type
 \- url
 \- webSocketDebuggerUrl
 $schema: http://json-schema.org/draft-07/schema#
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /json/new
 tags:
 \- Browser REST APIs
 /json/protocol:
 get:
 definitions: {}
 description: Returns Protocol JSON meta-data that Chrome and Chromium come with.
 parameters: \[\]
 requestBody:
 content: {}
 responses:
 '200':
 content:
 application/json:
 schema:
 type: object
 properties: {}
 additionalProperties: true
 $schema: http://json-schema.org/draft-07/schema#
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /json/protocol
 tags:
 \- Browser REST APIs
 /json/version:
 get:
 definitions: {}
 description: >-
 Returns a JSON payload that acts as a pass-through to the DevTools
 /json/version protocol in Chrome and Chromium.
 parameters: \[\]
 requestBody:
 content: {}
 responses:
 '200':
 content:
 application/json:
 schema:
 type: object
 properties:
 description:
 description: The description of the target. Generally the page's title.
 type: string
 devtoolsFrontendUrl:
 description: The fully-qualified URL of the Devtools inspector app.
 type: string
 id:
 description: A Unique Id for the underlying target.
 type: string
 title:
 description: >-
 The title of the target. For pages this is the page's
 title.
 type: string
 type:
 description: The type of target, generally "page" or "background\_page".
 type: string
 url:
 description: The current URL the target is consuming or visiting.
 type: string
 webSocketDebuggerUrl:
 description: >-
 The target or page's WebSocket Debugger URL. Primarily
 used for legacy

 libraries to connect and inspect or remote automate this
 target.
 type: string
 additionalProperties: false
 required:
 \- description
 \- devtoolsFrontendUrl
 \- id
 \- title
 \- type
 \- url
 \- webSocketDebuggerUrl
 $schema: http://json-schema.org/draft-07/schema#
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /json/version
 tags:
 \- Browser REST APIs
 /chrome/pdf:
 post:
 definitions: {}
 description: \|-
 A JSON-based API for getting a PDF binary from either a supplied
 "url" or "html" payload in your request. Many options exist for
 injecting cookies, request interceptors, user-agents and waiting for
 selectors, timers and more.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 options:
 $ref: '#/definitions/PDFOptions'
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 application/pdf:
 schema:
 description: Responds with an application/pdf content-type and a binary PDF
 type: string
 $schema: http://json-schema.org/draft-07/schema#
 description: Responds with an application/pdf content-type and a binary PDF
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/pdf
 tags:
 \- Browser REST APIs
 /chrome/performance:
 post:
 definitions: {}
 description: >-
 Run lighthouse performance audits with a supplied "url" in your JSON
 payload.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 budgets:
 type: array
 items:
 type: object
 properties: {}
 additionalProperties: true
 config:
 type: object
 properties: {}
 additionalProperties: true
 url:
 type: string
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 description: \|-
 The response of the lighthouse stats. Response objects are
 determined by the type of budgets and config in the POST
 JSON body
 type: object
 properties: {}
 additionalProperties: true
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 The response of the lighthouse stats. Response objects are
 determined by the type of budgets and config in the POST
 JSON body
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/performance
 tags:
 \- Browser REST APIs
 /chrome/scrape:
 post:
 definitions: {}
 description: >-
 A JSON-based API that returns text, html, and meta-data from a given
 list of selectors.

 Debugging information is available by sending in the appropriate flags
 in the "debugOpts"

 property. Responds with an array of JSON objects.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 debugOpts:
 $ref: '#/definitions/ScrapeDebugOptions'
 elements:
 type: array
 items:
 $ref: '#/definitions/ScrapeElementSelector'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 description: The JSON response body
 type: object
 properties:
 data:
 anyOf:
 \- type: array
 items:
 type: object
 properties:
 results:
 type: array
 items:
 type: object
 properties:
 attributes:
 description: A list of HTML attributes of the element
 type: array
 items:
 type: object
 properties:
 name:
 description: >-
 The name of the HTML attribute for the
 element
 type: string
 value:
 description: >-
 The value of the HTML attribute for the
 element
 type: string
 additionalProperties: false
 required:
 \- name
 \- value
 height:
 description: The height the element
 type: number
 html:
 description: The HTML the element
 type: string
 left:
 description: >-
 The amount of pixels from the left of the
 page
 type: number
 text:
 description: The text the element
 type: string
 top:
 description: >-
 The amount of pixels from the top of the
 page
 type: number
 width:
 description: The width the element
 type: number
 additionalProperties: false
 required:
 \- attributes
 \- height
 \- html
 \- left
 \- text
 \- top
 \- width
 selector:
 description: The DOM selector of the element
 type: string
 additionalProperties: false
 required:
 \- results
 \- selector
 \- type: 'null'
 debug:
 description: When debugOpts options are present, results are here
 anyOf:
 \- type: object
 properties:
 console:
 description: A list of console messages from the browser
 type: array
 items:
 type: string
 cookies:
 description: List of cookies for the site or null
 anyOf:
 \- type: array
 items:
 $ref: '#/definitions/Cookie'
 \- type: 'null'
 html:
 description: The HTML string of the website or null
 type:
 \- 'null'
 \- string
 network:
 type: object
 properties:
 inbound:
 type: array
 items:
 $ref: '#/definitions/InBoundRequest'
 outbound:
 type: array
 items:
 $ref: '#/definitions/OutBoundRequest'
 additionalProperties: false
 required:
 \- inbound
 \- outbound
 screenshot:
 description: A base64-encoded string of the site or null
 type:
 \- 'null'
 \- string
 additionalProperties: false
 required:
 \- console
 \- cookies
 \- html
 \- network
 \- screenshot
 \- type: 'null'
 additionalProperties: false
 required:
 \- data
 \- debug
 definitions:
 Cookie:
 description: Represents a cookie object.
 type: object
 properties:
 name:
 description: Cookie name.
 type: string
 value:
 description: Cookie value.
 type: string
 domain:
 description: Cookie domain.
 type: string
 path:
 description: Cookie path.
 type: string
 expires:
 description: >-
 Cookie expiration date as the number of seconds since
 the UNIX epoch. Set to \`-1\` for

 session cookies
 type: number
 size:
 description: Cookie size.
 type: number
 httpOnly:
 description: True if cookie is http-only.
 type: boolean
 secure:
 description: True if cookie is secure.
 type: boolean
 session:
 description: True in case of session cookie.
 type: boolean
 sameSite:
 description: Cookie SameSite type.
 enum:
 \- Lax
 \- None
 \- Strict
 type: string
 priority:
 description: Cookie Priority. Supported only in Chrome.
 enum:
 \- High
 \- Low
 \- Medium
 type: string
 sameParty:
 description: True if cookie is SameParty. Supported only in Chrome.
 type: boolean
 sourceScheme:
 description: Cookie source scheme type. Supported only in Chrome.
 enum:
 \- NonSecure
 \- Secure
 \- Unset
 type: string
 partitionKey:
 description: >-
 Cookie partition key. In Chrome, it is the top-level
 site the

 partitioned cookie is available in. In Firefox, it
 matches the

 source origin in the

 {@link
 https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey
 PartitionKey}.
 anyOf:
 \- $ref: '#/definitions/CookiePartitionKey'
 \- type: string
 partitionKeyOpaque:
 description: >-
 True if cookie partition key is opaque. Supported only
 in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- domain
 \- expires
 \- httpOnly
 \- name
 \- path
 \- secure
 \- session
 \- size
 \- value
 CookiePartitionKey:
 description: Represents a cookie partition key in Chrome.
 type: object
 properties:
 sourceOrigin:
 description: >-
 The site of the top-level URL the browser was visiting
 at the start of the request

 to the endpoint that set the cookie.

 In Chrome, maps to the CDP's \`topLevelSite\` partition
 key.
 type: string
 hasCrossSiteAncestor:
 description: >-
 Indicates if the cookie has any ancestors that are
 cross-site to

 the topLevelSite.

 Supported only in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- sourceOrigin
 InBoundRequest:
 type: object
 properties:
 headers: {}
 status:
 type: number
 url:
 type: string
 additionalProperties: false
 required:
 \- headers
 \- status
 \- url
 OutBoundRequest:
 type: object
 properties:
 headers: {}
 method:
 type: string
 url:
 type: string
 additionalProperties: false
 required:
 \- headers
 \- method
 \- url
 $schema: http://json-schema.org/draft-07/schema#
 description: The JSON response body
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/scrape
 tags:
 \- Browser REST APIs
 /chrome/screenshot:
 post:
 definitions: {}
 description: \|-
 A JSON-based API for getting a screenshot binary from either a supplied
 "url" or "html" payload in your request. Many options exist including
 cookies, user-agents, setting timers and network mocks.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 options:
 $ref: '#/definitions/ScreenshotOptions'
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 scrollPage:
 type: boolean
 selector:
 type: string
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 image/png:
 schema:
 type: text
 image/jpeg:
 schema:
 type: text
 text/plain:
 schema:
 type: text
 description: \|-
 Response can either be a text/plain base64 encoded body
 or a binary stream with png/jpeg as a content-type
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/screenshot
 tags:
 \- Browser REST APIs
 /chromium/content:
 post:
 definitions: {}
 description: >-
 A JSON-based API. Given a "url" or "html" field, runs and returns HTML
 content after the page has loaded and JavaScript has parsed.

 \*\*Note:\*\* This endpoint is also available at: \`/content\` for backwards
 compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 description: Whether or not to allow JavaScript to run on the page.
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 text/html:
 schema:
 description: \|-
 An HTML payload of the website or HTML after JavaScript
 parsing and execution.
 type: string
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 An HTML payload of the website or HTML after JavaScript
 parsing and execution.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/content
 tags:
 \- Browser REST APIs
 /chromium/download:
 post:
 definitions: {}
 description: >-
 A JSON or JavaScript content-type API for returning files Chrome has
 downloaded during

 the execution of puppeteer code, which is ran inside context of the
 browser.

 Browserless sets up a blank page, a fresh download directory, injects
 your puppeteer code, and then executes it.

 You can load external libraries via the "import" syntax, and import
 ESM-style modules

 that are written for execution inside of the browser. Once your script
 is finished, any

 downloaded files from Chromium are returned back with the appropriate
 content-type header.

 \*\*Note:\*\* This endpoint is also available at: \`/download\` for backwards
 compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 $ref: '#/definitions/JSONSchema'
 application/javascript:
 schema:
 type: string
 responses:
 '200':
 content:
 '\*/\*':
 schema:
 description: >-
 Responses are determined by the returned value of the
 downloads

 themselves, so there isn't a static response type for this
 API.
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 Responses are determined by the returned value of the downloads
 themselves, so there isn't a static response type for this API.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/download
 tags:
 \- Browser REST APIs
 /chromium/function:
 post:
 definitions: {}
 description: >-
 A JSON or JavaScript content-type API for running puppeteer code in the
 browser's context.

 Browserless sets up a blank page, injects your puppeteer code, and runs
 it.

 You can optionally load external libraries via the "import" module that
 are meant for browser usage.

 Values returned from the function are checked and an appropriate
 content-type and response is sent back

 to your HTTP call.

 \*\*Note:\*\* This endpoint is also available at: \`/function\` for backwards
 compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 $ref: '#/definitions/JSONSchema'
 application/javascript:
 schema:
 type: string
 responses:
 '200':
 content:
 '\*/\*':
 schema:
 description: >-
 Responses are determined by the returned value of the function

 itself. Binary responses (PDF's, screenshots) are returned
 back

 as binary data, and primitive JavaScript values are returned
 back

 by type (HTML data is "text/html", Objects are
 "application/json")
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 Responses are determined by the returned value of the function
 itself. Binary responses (PDF's, screenshots) are returned back
 as binary data, and primitive JavaScript values are returned back
 by type (HTML data is "text/html", Objects are "application/json")
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/function
 tags:
 \- Browser REST APIs
 /chromium/pdf:
 post:
 definitions: {}
 description: >-
 A JSON-based API for getting a PDF binary from either a supplied

 "url" or "html" payload in your request. Many options exist for

 injecting cookies, request interceptors, user-agents and waiting for

 selectors, timers and more.

 \*\*Note:\*\* This endpoint is also available at: \`/pdf\` for backwards
 compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 $ref: '#/definitions/Credentials'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 blockConsentModals:
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 options:
 $ref: '#/definitions/PDFOptions'
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 $ref: '#/definitions/Viewport'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/pdf
 tags:
 \- Browser REST APIs
 /chromium/performance:
 post:
 definitions: {}
 description: >-
 Run lighthouse performance audits with a supplied "url" in your JSON
 payload.

 \*\*Note:\*\* This endpoint is also available at: \`/performance\` for
 backwards compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 budgets:
 type: array
 items:
 type: object
 properties: {}
 additionalProperties: true
 config:
 type: object
 properties: {}
 additionalProperties: true
 url:
 type: string
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 description: \|-
 The response of the lighthouse stats. Response objects are
 determined by the type of budgets and config in the POST
 JSON body
 type: object
 properties: {}
 additionalProperties: true
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 The response of the lighthouse stats. Response objects are
 determined by the type of budgets and config in the POST
 JSON body
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/performance
 tags:
 \- Browser REST APIs
 /chromium/scrape:
 post:
 definitions: {}
 description: >-
 A JSON-based API that returns text, html, and meta-data from a given
 list of selectors.

 Debugging information is available by sending in the appropriate flags
 in the "debugOpts"

 property. Responds with an array of JSON objects.

 \*\*Note:\*\* This endpoint is also available at: \`/scrape\` for backwards
 compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 debugOpts:
 $ref: '#/definitions/ScrapeDebugOptions'
 elements:
 type: array
 items:
 $ref: '#/definitions/ScrapeElementSelector'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 description: The JSON response body
 type: object
 properties:
 data:
 anyOf:
 \- type: array
 items:
 type: object
 properties:
 results:
 type: array
 items:
 type: object
 properties:
 attributes:
 description: A list of HTML attributes of the element
 type: array
 items:
 type: object
 properties:
 name:
 description: >-
 The name of the HTML attribute for the
 element
 type: string
 value:
 description: >-
 The value of the HTML attribute for the
 element
 type: string
 additionalProperties: false
 required:
 \- name
 \- value
 height:
 description: The height the element
 type: number
 html:
 description: The HTML the element
 type: string
 left:
 description: >-
 The amount of pixels from the left of the
 page
 type: number
 text:
 description: The text the element
 type: string
 top:
 description: >-
 The amount of pixels from the top of the
 page
 type: number
 width:
 description: The width the element
 type: number
 additionalProperties: false
 required:
 \- attributes
 \- height
 \- html
 \- left
 \- text
 \- top
 \- width
 selector:
 description: The DOM selector of the element
 type: string
 additionalProperties: false
 required:
 \- results
 \- selector
 \- type: 'null'
 debug:
 description: When debugOpts options are present, results are here
 anyOf:
 \- type: object
 properties:
 console:
 description: A list of console messages from the browser
 type: array
 items:
 type: string
 cookies:
 description: List of cookies for the site or null
 anyOf:
 \- type: array
 items:
 $ref: '#/definitions/Cookie'
 \- type: 'null'
 html:
 description: The HTML string of the website or null
 type:
 \- 'null'
 \- string
 network:
 type: object
 properties:
 inbound:
 type: array
 items:
 $ref: '#/definitions/InBoundRequest'
 outbound:
 type: array
 items:
 $ref: '#/definitions/OutBoundRequest'
 additionalProperties: false
 required:
 \- inbound
 \- outbound
 screenshot:
 description: A base64-encoded string of the site or null
 type:
 \- 'null'
 \- string
 additionalProperties: false
 required:
 \- console
 \- cookies
 \- html
 \- network
 \- screenshot
 \- type: 'null'
 additionalProperties: false
 required:
 \- data
 \- debug
 definitions:
 Cookie:
 description: Represents a cookie object.
 type: object
 properties:
 name:
 description: Cookie name.
 type: string
 value:
 description: Cookie value.
 type: string
 domain:
 description: Cookie domain.
 type: string
 path:
 description: Cookie path.
 type: string
 expires:
 description: >-
 Cookie expiration date as the number of seconds since
 the UNIX epoch. Set to \`-1\` for

 session cookies
 type: number
 size:
 description: Cookie size.
 type: number
 httpOnly:
 description: True if cookie is http-only.
 type: boolean
 secure:
 description: True if cookie is secure.
 type: boolean
 session:
 description: True in case of session cookie.
 type: boolean
 sameSite:
 description: Cookie SameSite type.
 enum:
 \- Lax
 \- None
 \- Strict
 type: string
 priority:
 description: Cookie Priority. Supported only in Chrome.
 enum:
 \- High
 \- Low
 \- Medium
 type: string
 sameParty:
 description: True if cookie is SameParty. Supported only in Chrome.
 type: boolean
 sourceScheme:
 description: Cookie source scheme type. Supported only in Chrome.
 enum:
 \- NonSecure
 \- Secure
 \- Unset
 type: string
 partitionKey:
 description: >-
 Cookie partition key. In Chrome, it is the top-level
 site the

 partitioned cookie is available in. In Firefox, it
 matches the

 source origin in the

 {@link
 https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey
 PartitionKey}.
 anyOf:
 \- $ref: '#/definitions/CookiePartitionKey'
 \- type: string
 partitionKeyOpaque:
 description: >-
 True if cookie partition key is opaque. Supported only
 in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- domain
 \- expires
 \- httpOnly
 \- name
 \- path
 \- secure
 \- session
 \- size
 \- value
 CookiePartitionKey:
 description: Represents a cookie partition key in Chrome.
 type: object
 properties:
 sourceOrigin:
 description: >-
 The site of the top-level URL the browser was visiting
 at the start of the request

 to the endpoint that set the cookie.

 In Chrome, maps to the CDP's \`topLevelSite\` partition
 key.
 type: string
 hasCrossSiteAncestor:
 description: >-
 Indicates if the cookie has any ancestors that are
 cross-site to

 the topLevelSite.

 Supported only in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- sourceOrigin
 InBoundRequest:
 type: object
 properties:
 headers: {}
 status:
 type: number
 url:
 type: string
 additionalProperties: false
 required:
 \- headers
 \- status
 \- url
 OutBoundRequest:
 type: object
 properties:
 headers: {}
 method:
 type: string
 url:
 type: string
 additionalProperties: false
 required:
 \- headers
 \- method
 \- url
 $schema: http://json-schema.org/draft-07/schema#
 description: The JSON response body
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/scrape
 tags:
 \- Browser REST APIs
 /chromium/screenshot:
 post:
 definitions: {}
 description: >-
 A JSON-based API for getting a screenshot binary from either a supplied

 "url" or "html" payload in your request. Many options exist including

 cookies, user-agents, setting timers and network mocks.

 \*\*Note:\*\* This endpoint is also available at: \`/screenshot\` for
 backwards compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 $ref: '#/definitions/Credentials'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 blockConsentModals:
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 options:
 $ref: '#/definitions/ScreenshotOptions'
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 scrollPage:
 type: boolean
 selector:
 type: string
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 $ref: '#/definitions/Viewport'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/screenshot
 tags:
 \- Browser REST APIs
 /edge/content:
 post:
 definitions: {}
 description: >-
 A JSON-based API. Given a "url" or "html" field, runs and returns HTML
 content after the page has loaded and JavaScript has parsed.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 description: Whether or not to allow JavaScript to run on the page.
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 text/html:
 schema:
 description: \|-
 An HTML payload of the website or HTML after JavaScript
 parsing and execution.
 type: string
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 An HTML payload of the website or HTML after JavaScript
 parsing and execution.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /edge/content
 tags:
 \- Browser REST APIs
 /edge/download:
 post:
 definitions: {}
 description: >-
 A JSON or JavaScript content-type API for returning files Chrome has
 downloaded during

 the execution of puppeteer code, which is ran inside context of the
 browser.

 Browserless sets up a blank page, a fresh download directory, injects
 your puppeteer code, and then executes it.

 You can load external libraries via the "import" syntax, and import
 ESM-style modules

 that are written for execution inside of the browser. Once your script
 is finished, any

 downloaded files from Chromium are returned back with the appropriate
 content-type header.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 $ref: '#/definitions/JSONSchema'
 application/javascript:
 schema:
 type: string
 responses:
 '200':
 content:
 '\*/\*':
 schema:
 description: >-
 Responses are determined by the returned value of the
 downloads

 themselves, so there isn't a static response type for this
 API.
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 Responses are determined by the returned value of the downloads
 themselves, so there isn't a static response type for this API.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /edge/download
 tags:
 \- Browser REST APIs
 /edge/function:
 post:
 definitions: {}
 description: >-
 A JSON or JavaScript content-type API for running puppeteer code in the
 browser's context.

 Browserless sets up a blank page, injects your puppeteer code, and runs
 it.

 You can optionally load external libraries via the "import" module that
 are meant for browser usage.

 Values returned from the function are checked and an appropriate
 content-type and response is sent back

 to your HTTP call.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 $ref: '#/definitions/JSONSchema'
 application/javascript:
 schema:
 type: string
 responses:
 '200':
 content:
 '\*/\*':
 schema:
 description: >-
 Responses are determined by the returned value of the function

 itself. Binary responses (PDF's, screenshots) are returned
 back

 as binary data, and primitive JavaScript values are returned
 back

 by type (HTML data is "text/html", Objects are
 "application/json")
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 Responses are determined by the returned value of the function
 itself. Binary responses (PDF's, screenshots) are returned back
 as binary data, and primitive JavaScript values are returned back
 by type (HTML data is "text/html", Objects are "application/json")
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /edge/function
 tags:
 \- Browser REST APIs
 /edge/pdf:
 post:
 definitions: {}
 description: \|-
 A JSON-based API for getting a PDF binary from either a supplied
 "url" or "html" payload in your request. Many options exist for
 injecting cookies, request interceptors, user-agents and waiting for
 selectors, timers and more.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 options:
 $ref: '#/definitions/PDFOptions'
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 application/pdf:
 schema:
 description: Responds with an application/pdf content-type and a binary PDF
 type: string
 $schema: http://json-schema.org/draft-07/schema#
 description: Responds with an application/pdf content-type and a binary PDF
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /edge/pdf
 tags:
 \- Browser REST APIs
 /edge/performance:
 post:
 definitions: {}
 description: >-
 Run lighthouse performance audits with a supplied "url" in your JSON
 payload.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 budgets:
 type: array
 items:
 type: object
 properties: {}
 additionalProperties: true
 config:
 type: object
 properties: {}
 additionalProperties: true
 url:
 type: string
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 description: \|-
 The response of the lighthouse stats. Response objects are
 determined by the type of budgets and config in the POST
 JSON body
 type: object
 properties: {}
 additionalProperties: true
 $schema: http://json-schema.org/draft-07/schema#
 description: \|-
 The response of the lighthouse stats. Response objects are
 determined by the type of budgets and config in the POST
 JSON body
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /edge/performance
 tags:
 \- Browser REST APIs
 /edge/scrape:
 post:
 definitions: {}
 description: >-
 A JSON-based API that returns text, html, and meta-data from a given
 list of selectors.

 Debugging information is available by sending in the appropriate flags
 in the "debugOpts"

 property. Responds with an array of JSON objects.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 debugOpts:
 $ref: '#/definitions/ScrapeDebugOptions'
 elements:
 type: array
 items:
 $ref: '#/definitions/ScrapeElementSelector'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 description: The JSON response body
 type: object
 properties:
 data:
 anyOf:
 \- type: array
 items:
 type: object
 properties:
 results:
 type: array
 items:
 type: object
 properties:
 attributes:
 description: A list of HTML attributes of the element
 type: array
 items:
 type: object
 properties:
 name:
 description: >-
 The name of the HTML attribute for the
 element
 type: string
 value:
 description: >-
 The value of the HTML attribute for the
 element
 type: string
 additionalProperties: false
 required:
 \- name
 \- value
 height:
 description: The height the element
 type: number
 html:
 description: The HTML the element
 type: string
 left:
 description: >-
 The amount of pixels from the left of the
 page
 type: number
 text:
 description: The text the element
 type: string
 top:
 description: >-
 The amount of pixels from the top of the
 page
 type: number
 width:
 description: The width the element
 type: number
 additionalProperties: false
 required:
 \- attributes
 \- height
 \- html
 \- left
 \- text
 \- top
 \- width
 selector:
 description: The DOM selector of the element
 type: string
 additionalProperties: false
 required:
 \- results
 \- selector
 \- type: 'null'
 debug:
 description: When debugOpts options are present, results are here
 anyOf:
 \- type: object
 properties:
 console:
 description: A list of console messages from the browser
 type: array
 items:
 type: string
 cookies:
 description: List of cookies for the site or null
 anyOf:
 \- type: array
 items:
 $ref: '#/definitions/Cookie'
 \- type: 'null'
 html:
 description: The HTML string of the website or null
 type:
 \- 'null'
 \- string
 network:
 type: object
 properties:
 inbound:
 type: array
 items:
 $ref: '#/definitions/InBoundRequest'
 outbound:
 type: array
 items:
 $ref: '#/definitions/OutBoundRequest'
 additionalProperties: false
 required:
 \- inbound
 \- outbound
 screenshot:
 description: A base64-encoded string of the site or null
 type:
 \- 'null'
 \- string
 additionalProperties: false
 required:
 \- console
 \- cookies
 \- html
 \- network
 \- screenshot
 \- type: 'null'
 additionalProperties: false
 required:
 \- data
 \- debug
 definitions:
 Cookie:
 description: Represents a cookie object.
 type: object
 properties:
 name:
 description: Cookie name.
 type: string
 value:
 description: Cookie value.
 type: string
 domain:
 description: Cookie domain.
 type: string
 path:
 description: Cookie path.
 type: string
 expires:
 description: >-
 Cookie expiration date as the number of seconds since
 the UNIX epoch. Set to \`-1\` for

 session cookies
 type: number
 size:
 description: Cookie size.
 type: number
 httpOnly:
 description: True if cookie is http-only.
 type: boolean
 secure:
 description: True if cookie is secure.
 type: boolean
 session:
 description: True in case of session cookie.
 type: boolean
 sameSite:
 description: Cookie SameSite type.
 enum:
 \- Lax
 \- None
 \- Strict
 type: string
 priority:
 description: Cookie Priority. Supported only in Chrome.
 enum:
 \- High
 \- Low
 \- Medium
 type: string
 sameParty:
 description: True if cookie is SameParty. Supported only in Chrome.
 type: boolean
 sourceScheme:
 description: Cookie source scheme type. Supported only in Chrome.
 enum:
 \- NonSecure
 \- Secure
 \- Unset
 type: string
 partitionKey:
 description: >-
 Cookie partition key. In Chrome, it is the top-level
 site the

 partitioned cookie is available in. In Firefox, it
 matches the

 source origin in the

 {@link
 https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey
 PartitionKey}.
 anyOf:
 \- $ref: '#/definitions/CookiePartitionKey'
 \- type: string
 partitionKeyOpaque:
 description: >-
 True if cookie partition key is opaque. Supported only
 in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- domain
 \- expires
 \- httpOnly
 \- name
 \- path
 \- secure
 \- session
 \- size
 \- value
 CookiePartitionKey:
 description: Represents a cookie partition key in Chrome.
 type: object
 properties:
 sourceOrigin:
 description: >-
 The site of the top-level URL the browser was visiting
 at the start of the request

 to the endpoint that set the cookie.

 In Chrome, maps to the CDP's \`topLevelSite\` partition
 key.
 type: string
 hasCrossSiteAncestor:
 description: >-
 Indicates if the cookie has any ancestors that are
 cross-site to

 the topLevelSite.

 Supported only in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- sourceOrigin
 InBoundRequest:
 type: object
 properties:
 headers: {}
 status:
 type: number
 url:
 type: string
 additionalProperties: false
 required:
 \- headers
 \- status
 \- url
 OutBoundRequest:
 type: object
 properties:
 headers: {}
 method:
 type: string
 url:
 type: string
 additionalProperties: false
 required:
 \- headers
 \- method
 \- url
 $schema: http://json-schema.org/draft-07/schema#
 description: The JSON response body
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /edge/scrape
 tags:
 \- Browser REST APIs
 /edge/screenshot:
 post:
 definitions: {}
 description: \|-
 A JSON-based API for getting a screenshot binary from either a supplied
 "url" or "html" payload in your request. Many options exist including
 cookies, user-agents, setting timers and network mocks.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 addScriptTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddScriptTagOptions'
 addStyleTag:
 type: array
 items:
 $ref: '#/definitions/FrameAddStyleTagOptions'
 authenticate:
 anyOf:
 \- $ref: '#/definitions/Credentials'
 \- type: 'null'
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 cookies:
 type: array
 items:
 $ref: '#/definitions/CookieParam'
 emulateMediaType:
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 html:
 type: string
 options:
 $ref: '#/definitions/ScreenshotOptions'
 rejectRequestPattern:
 type: array
 items:
 type: string
 rejectResourceTypes:
 type: array
 items:
 enum:
 \- cspviolationreport
 \- document
 \- eventsource
 \- fetch
 \- font
 \- image
 \- manifest
 \- media
 \- other
 \- ping
 \- prefetch
 \- preflight
 \- script
 \- signedexchange
 \- stylesheet
 \- texttrack
 \- websocket
 \- xhr
 type: string
 requestInterceptors:
 type: array
 items:
 description: >-
 An array of patterns (using \`req.url().match(r.pattern)\`
 to match) and their

 corresponding responses to use in order to fulfill those
 requests.
 type: object
 properties:
 pattern:
 description: >-
 An array of patterns (using
 \`req.url().match(r.pattern)\` to match) and their

 corresponding responses to use in order to fulfill
 those requests.
 type: string
 response:
 $ref: '#/definitions/Partial'
 additionalProperties: false
 required:
 \- pattern
 \- response
 scrollPage:
 type: boolean
 selector:
 type: string
 setExtraHTTPHeaders:
 $ref: '#/definitions/Record'
 setJavaScriptEnabled:
 type: boolean
 url:
 type: string
 userAgent:
 type: string
 viewport:
 anyOf:
 \- $ref: '#/definitions/Viewport'
 \- type: 'null'
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 image/png:
 schema:
 type: text
 image/jpeg:
 schema:
 type: text
 text/plain:
 schema:
 type: text
 description: \|-
 Response can either be a text/plain base64 encoded body
 or a binary stream with png/jpeg as a content-type
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /edge/screenshot
 tags:
 \- Browser REST APIs
 /active:
 get:
 definitions: {}
 description: >-
 Returns a simple "204" HTTP code, with no response, indicating that the
 service itself is up and running.

 Useful for liveliness probes or other external checks.
 parameters: \[\]
 requestBody:
 content: {}
 responses:
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /active
 tags:
 \- Management REST APIs
 /kill/+(\[0-9a-zA-Z-\_\]):
 get:
 definitions: {}
 description: Kill running sessions based on BrowserId or TrackingId.
 parameters:
 \- in: query
 name: token
 required: true
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: blockAds
 required: false
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: browserId
 required: false
 schema:
 type: string
 \- in: query
 name: launch
 required: false
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- $ref: '#/definitions/BrowserServerOptions'
 \- type: string
 \- in: query
 name: timeout
 required: false
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: trackingId
 required: false
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /kill/+(\[0-9a-zA-Z-\_\])
 tags:
 \- Management REST APIs
 /meta:
 get:
 definitions: {}
 description: >-
 Returns a JSON payload of the current system versions, including the
 core API version.
 parameters: \[\]
 requestBody:
 content: {}
 responses:
 '200':
 content:
 application/json:
 schema:
 type: object
 properties:
 version:
 description: The semantic version of the Browserless API
 type: string
 chromium:
 description: >-
 The version of Chromium installed, or null if not
 installed
 type:
 \- 'null'
 \- string
 webkit:
 description: The version of Webkit installed, or null if not installed
 type:
 \- 'null'
 \- string
 firefox:
 description: The version of Firefox installed, or null if not installed
 type:
 \- 'null'
 \- string
 playwright:
 description: The supported version(s) of puppeteer
 type: array
 items:
 type: string
 puppeteer:
 description: The supported version(s) of playwright
 type: array
 items:
 type: string
 additionalProperties: false
 required:
 \- chromium
 \- firefox
 \- playwright
 \- puppeteer
 \- version
 \- webkit
 $schema: http://json-schema.org/draft-07/schema#
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /meta
 tags:
 \- Management REST APIs
 /:
 get:
 definitions: {}
 description: >-
 Serves static files inside of this "static" directory. Content-types
 will vary depending on the type =of file being returned.
 parameters: \[\]
 requestBody:
 content: {}
 responses:
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /
 tags:
 \- Management REST APIs
 /devtools/browser/\*:
 get:
 definitions: {}
 description: \|-
 Connect to an already-running Chromium process with a library like
 puppeteer, or others, that work over chrome-devtools-protocol. Chromium
 must already be launched in order to not return a 404.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /devtools/browser/\*
 tags:
 \- Browser WebSocket APIs
 /chrome:
 get:
 definitions: {}
 description: >-
 Launch and connect to Chromium with a library like puppeteer or others
 that work over chrome-devtools-protocol.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: record
 schema:
 type: boolean
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome
 tags:
 \- Browser WebSocket APIs
 /devtools/page/\*:
 get:
 definitions: {}
 description: \|-
 Connect to an existing page in Chromium with a library like
 chrome-remote-interface or others that work the page websocketDebugger
 URL. You can get this unique URL by calling the /json/list API
 or by finding the page's unique ID from your library of choice.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /devtools/page/\*
 tags:
 \- Browser WebSocket APIs
 /chrome/playwright:
 get:
 definitions: {}
 description: Connect to Chromium with any playwright style library.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/BrowserServerOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/playwright
 tags:
 \- Browser WebSocket APIs
 /chromium:
 get:
 definitions: {}
 description: >-
 Launch and connect to Chromium with a library like puppeteer or others
 that work over chrome-devtools-protocol.

 \*\*Note:\*\* This endpoint is also available at: \`\` for backwards
 compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: record
 schema:
 type: boolean
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium
 tags:
 \- Browser WebSocket APIs
 /playwright/chromium:
 get:
 definitions: {}
 description: >-
 Connect to Chromium with any playwright style library.

 \*\*Note:\*\* This endpoint is also available at: \`/chromium/playwright\` for
 backwards compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/BrowserServerOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /playwright/chromium
 tags:
 \- Browser WebSocket APIs
 /edge:
 get:
 definitions: {}
 description: >-
 Launch and connect to Chromium with a library like puppeteer or others
 that work over chrome-devtools-protocol.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/CDPLaunchOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /edge
 tags:
 \- Browser WebSocket APIs
 /edge/playwright:
 get:
 definitions: {}
 description: Connect to Chromium with any playwright style library.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/BrowserServerOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /edge/playwright
 tags:
 \- Browser WebSocket APIs
 /playwright/firefox:
 get:
 definitions: {}
 description: >-
 Connect to Firefox with any playwright-compliant library.

 \*\*Note:\*\* This endpoint is also available at: \`/firefox/playwright\` for
 backwards compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 additionalProperties: false
 type: object
 properties:
 args:
 type: array
 items:
 type: string
 chromiumSandbox:
 type: boolean
 devtools:
 type: boolean
 downloadsPath:
 type: string
 headless:
 type: boolean
 ignoreDefaultArgs:
 anyOf:
 \- type: array
 items:
 type: string
 \- type: boolean
 proxy:
 type: object
 properties:
 bypass:
 type: string
 password:
 type: string
 server:
 type: string
 username:
 type: string
 additionalProperties: false
 required:
 \- server
 timeout:
 type: number
 tracesDir:
 type: string
 firefoxUserPrefs:
 type: object
 additionalProperties:
 type:
 \- string
 \- number
 \- boolean
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /playwright/firefox
 tags:
 \- Browser WebSocket APIs
 /playwright/webkit:
 get:
 definitions: {}
 description: >-
 Connect to Webkit with any playwright-compliant library.

 \*\*Note:\*\* This endpoint is also available at: \`/webkit/playwright\` for
 backwards compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: '#/definitions/BrowserServerOptions'
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /playwright/webkit
 tags:
 \- Browser WebSocket APIs
 /chrome/export:
 post:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise, hosted and self-hosted
 plans. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/)

 Exports a webpage to a PDF or image format. This API is useful for
 generating reports, screenshots, or PDFs of web pages.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 url:
 description: The URL of the site you want to archive.
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 description: >-
 An optional goto parameter object for considering when the
 page is done loading.
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 headers:
 $ref: '#/definitions/Record'
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 type: object
 properties:
 html:
 description: The HTML content of the page.
 type: string
 additionalProperties: false
 required:
 \- html
 $schema: http://json-schema.org/draft-07/schema#
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/export
 tags:
 \- Browser REST APIs
 /chrome/unblock:
 post:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise and Cloud-unit plans.
 \[Contact us for more information\
 here.\](https://www.browserless.io/contact/), or \[sign-up\
 here\](https://www.browserless.io/pricing/).

 Unblocks the provided URL from being blocked due to bot detection.

 Returns a payload of Cookies, HTML, a base64 encoded screenshot,

 and a "browserWSEndpoint" to allow connecting to the browser when

 specified in the JSON Payload. Only supports CDP or Puppeteer

 like libraries when connecting to the "browserWSEndpoint".
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 url:
 description: The URL of the site you want to unblock.
 type: string
 browserWSEndpoint:
 description: >-
 Whether or not to keep the underlying browser alive and
 around for

 future reconnects. Defaults to false.
 type: boolean
 cookies:
 description: >-
 Whether or not to to return cookies for the site, defaults
 to true.
 type: boolean
 content:
 description: >-
 Whether or not to to return content for the site, defaults
 to true.
 type: boolean
 screenshot:
 description: >-
 Whether or not to to return a full-page screenshot for the
 site, defaults to true.
 type: boolean
 ttl:
 description: \|-
 When the browserWSEndpoint is requested this tells
 browserless how long to keep this browser alive for
 re-connection until shutting it down completely.
 Maximum of 30000 for 30 seconds (30,000ms).
 type: number
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 description: >-
 An optional goto parameter object for considering when the
 page is done loading.
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 type: object
 properties:
 cookies:
 description: >-
 A list of cookies which can be used for new connections or
 for usage elsewhere.

 Value is "null" when the request body specifies cookies:
 false.
 type: array
 items:
 $ref: '#/definitions/Cookie'
 content:
 description: >-
 The HTML content of the page once it is passed bot
 detection.

 Value is "null" when the request body specifies cookies:
 false.
 type: string
 browserWSEndpoint:
 description: >-
 The browserWSEndpoint of the response when the POST body
 contains a

 browserWSEndpoint: true property
 type: string
 ttl:
 description: >-
 The time the browser will remain alive until it is
 shutdown. Zero

 when browserWSEndpoint: false is set in the request
 payload. The limit

 is 30000 or 30 seconds, which is the maximum allowed time.
 type: number
 screenshot:
 description: A base64 encoded JPEG of the of the final site page.
 type: string
 additionalProperties: false
 required:
 \- browserWSEndpoint
 \- content
 \- cookies
 \- screenshot
 \- ttl
 definitions:
 Cookie:
 description: Represents a cookie object.
 type: object
 properties:
 name:
 description: Cookie name.
 type: string
 value:
 description: Cookie value.
 type: string
 domain:
 description: Cookie domain.
 type: string
 path:
 description: Cookie path.
 type: string
 expires:
 description: >-
 Cookie expiration date as the number of seconds since
 the UNIX epoch. Set to \`-1\` for

 session cookies
 type: number
 size:
 description: Cookie size.
 type: number
 httpOnly:
 description: True if cookie is http-only.
 type: boolean
 secure:
 description: True if cookie is secure.
 type: boolean
 session:
 description: True in case of session cookie.
 type: boolean
 sameSite:
 $ref: '#/definitions/CookieSameSite'
 description: Cookie SameSite type.
 priority:
 $ref: '#/definitions/CookiePriority'
 description: Cookie Priority. Supported only in Chrome.
 sameParty:
 description: True if cookie is SameParty. Supported only in Chrome.
 type: boolean
 sourceScheme:
 $ref: '#/definitions/CookieSourceScheme'
 description: Cookie source scheme type. Supported only in Chrome.
 partitionKey:
 description: >-
 Cookie partition key. In Chrome, it is the top-level
 site the

 partitioned cookie is available in. In Firefox, it
 matches the

 source origin in the

 {@link
 https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey
 PartitionKey}.
 anyOf:
 \- $ref: '#/definitions/CookiePartitionKey'
 \- type: string
 partitionKeyOpaque:
 description: >-
 True if cookie partition key is opaque. Supported only
 in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- domain
 \- expires
 \- httpOnly
 \- name
 \- path
 \- secure
 \- session
 \- size
 \- value
 CookieSameSite:
 description: \|-
 Represents the cookie's 'SameSite' status:
 https://tools.ietf.org/html/draft-west-first-party-cookies
 enum:
 \- Lax
 \- None
 \- Strict
 type: string
 CookiePriority:
 description: \|-
 Represents the cookie's 'Priority' status:
 https://tools.ietf.org/html/draft-west-cookie-priority-00
 enum:
 \- High
 \- Low
 \- Medium
 type: string
 CookieSourceScheme:
 description: >-
 Represents the source scheme of the origin that originally
 set the cookie. A value of

 "Unset" allows protocol clients to emulate legacy cookie
 scope for the scheme.

 This is a temporary ability and it will be removed in the
 future.
 enum:
 \- NonSecure
 \- Secure
 \- Unset
 type: string
 CookiePartitionKey:
 description: Represents a cookie partition key in Chrome.
 type: object
 properties:
 sourceOrigin:
 description: >-
 The site of the top-level URL the browser was visiting
 at the start of the request

 to the endpoint that set the cookie.

 In Chrome, maps to the CDP's \`topLevelSite\` partition
 key.
 type: string
 hasCrossSiteAncestor:
 description: >-
 Indicates if the cookie has any ancestors that are
 cross-site to

 the topLevelSite.

 Supported only in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- sourceOrigin
 $schema: http://json-schema.org/draft-07/schema#
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/unblock
 tags:
 \- Browser REST APIs
 /chromium/export:
 post:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise, hosted and self-hosted
 plans. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/)

 Exports a webpage to a PDF or image format. This API is useful for
 generating reports, screenshots, or PDFs of web pages.

 \*\*Note:\*\* This endpoint is also available at: \`/export\` for backwards
 compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 url:
 description: The URL of the site you want to archive.
 type: string
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 description: >-
 An optional goto parameter object for considering when the
 page is done loading.
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 headers:
 $ref: '#/definitions/Record'
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 type: object
 properties:
 html:
 description: The HTML content of the page.
 type: string
 additionalProperties: false
 required:
 \- html
 $schema: http://json-schema.org/draft-07/schema#
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/export
 tags:
 \- Browser REST APIs
 /chromium/unblock:
 post:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise and Cloud-unit plans.
 \[Contact us for more information\
 here.\](https://www.browserless.io/contact/), or \[sign-up\
 here\](https://www.browserless.io/pricing/).

 Unblocks the provided URL from being blocked due to bot detection.

 Returns a payload of Cookies, HTML, a base64 encoded screenshot,

 and a "browserWSEndpoint" to allow connecting to the browser when

 specified in the JSON Payload. Only supports CDP or Puppeteer

 like libraries when connecting to the "browserWSEndpoint".

 \*\*Note:\*\* This endpoint is also available at: \`/unblock\` for backwards
 compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 bestAttempt:
 description: >-
 When bestAttempt is set to true, browserless attempt to
 proceed

 when "awaited" events fail or timeout. This includes things
 like

 goto, waitForSelector, and more.
 type: boolean
 url:
 description: The URL of the site you want to unblock.
 type: string
 browserWSEndpoint:
 description: >-
 Whether or not to keep the underlying browser alive and
 around for

 future reconnects. Defaults to false.
 type: boolean
 cookies:
 description: >-
 Whether or not to to return cookies for the site, defaults
 to true.
 type: boolean
 content:
 description: >-
 Whether or not to to return content for the site, defaults
 to true.
 type: boolean
 screenshot:
 description: >-
 Whether or not to to return a full-page screenshot for the
 site, defaults to true.
 type: boolean
 ttl:
 description: \|-
 When the browserWSEndpoint is requested this tells
 browserless how long to keep this browser alive for
 re-connection until shutting it down completely.
 Maximum of 30000 for 30 seconds (30,000ms).
 type: number
 gotoOptions:
 $ref: '#/definitions/GoToOptions'
 description: >-
 An optional goto parameter object for considering when the
 page is done loading.
 waitForEvent:
 type: object
 properties:
 event:
 type: string
 timeout:
 type: number
 additionalProperties: false
 required:
 \- event
 waitForFunction:
 type: object
 properties:
 fn:
 description: >-
 The function, or statement, to be evaluated in browser
 context
 type: string
 polling:
 description: >-
 An interval at which the pageFunction is executed,
 defaults to raf.

 If polling is a number, then it is treated as an
 interval in milliseconds

 at which the function would be executed. If polling is a
 string,

 then it can be one of the following values: "raf" or
 "mutation"
 type:
 \- string
 \- number
 timeout:
 description: >-
 Maximum time to wait for in milliseconds. Defaults to
 30000 (30 seconds).

 Pass 0 to disable timeout.
 type: number
 additionalProperties: false
 required:
 \- fn
 waitForSelector:
 type: object
 properties:
 hidden:
 type: boolean
 selector:
 type: string
 timeout:
 type: number
 visible:
 type: boolean
 additionalProperties: false
 required:
 \- selector
 waitForTimeout:
 type: number
 type: object
 responses:
 '200':
 content:
 application/json:
 schema:
 type: object
 properties:
 cookies:
 description: >-
 A list of cookies which can be used for new connections or
 for usage elsewhere.

 Value is "null" when the request body specifies cookies:
 false.
 type: array
 items:
 $ref: '#/definitions/Cookie'
 content:
 description: >-
 The HTML content of the page once it is passed bot
 detection.

 Value is "null" when the request body specifies cookies:
 false.
 type: string
 browserWSEndpoint:
 description: >-
 The browserWSEndpoint of the response when the POST body
 contains a

 browserWSEndpoint: true property
 type: string
 ttl:
 description: >-
 The time the browser will remain alive until it is
 shutdown. Zero

 when browserWSEndpoint: false is set in the request
 payload. The limit

 is 30000 or 30 seconds, which is the maximum allowed time.
 type: number
 screenshot:
 description: A base64 encoded JPEG of the of the final site page.
 type: string
 additionalProperties: false
 required:
 \- browserWSEndpoint
 \- content
 \- cookies
 \- screenshot
 \- ttl
 definitions:
 Cookie:
 description: Represents a cookie object.
 type: object
 properties:
 name:
 description: Cookie name.
 type: string
 value:
 description: Cookie value.
 type: string
 domain:
 description: Cookie domain.
 type: string
 path:
 description: Cookie path.
 type: string
 expires:
 description: >-
 Cookie expiration date as the number of seconds since
 the UNIX epoch. Set to \`-1\` for

 session cookies
 type: number
 size:
 description: Cookie size.
 type: number
 httpOnly:
 description: True if cookie is http-only.
 type: boolean
 secure:
 description: True if cookie is secure.
 type: boolean
 session:
 description: True in case of session cookie.
 type: boolean
 sameSite:
 $ref: '#/definitions/CookieSameSite'
 description: Cookie SameSite type.
 priority:
 $ref: '#/definitions/CookiePriority'
 description: Cookie Priority. Supported only in Chrome.
 sameParty:
 description: True if cookie is SameParty. Supported only in Chrome.
 type: boolean
 sourceScheme:
 $ref: '#/definitions/CookieSourceScheme'
 description: Cookie source scheme type. Supported only in Chrome.
 partitionKey:
 description: >-
 Cookie partition key. In Chrome, it is the top-level
 site the

 partitioned cookie is available in. In Firefox, it
 matches the

 source origin in the

 {@link
 https://w3c.github.io/webdriver-bidi/#type-storage-PartitionKey
 PartitionKey}.
 anyOf:
 \- $ref: '#/definitions/CookiePartitionKey'
 \- type: string
 partitionKeyOpaque:
 description: >-
 True if cookie partition key is opaque. Supported only
 in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- domain
 \- expires
 \- httpOnly
 \- name
 \- path
 \- secure
 \- session
 \- size
 \- value
 CookieSameSite:
 description: \|-
 Represents the cookie's 'SameSite' status:
 https://tools.ietf.org/html/draft-west-first-party-cookies
 enum:
 \- Lax
 \- None
 \- Strict
 type: string
 CookiePriority:
 description: \|-
 Represents the cookie's 'Priority' status:
 https://tools.ietf.org/html/draft-west-cookie-priority-00
 enum:
 \- High
 \- Low
 \- Medium
 type: string
 CookieSourceScheme:
 description: >-
 Represents the source scheme of the origin that originally
 set the cookie. A value of

 "Unset" allows protocol clients to emulate legacy cookie
 scope for the scheme.

 This is a temporary ability and it will be removed in the
 future.
 enum:
 \- NonSecure
 \- Secure
 \- Unset
 type: string
 CookiePartitionKey:
 description: Represents a cookie partition key in Chrome.
 type: object
 properties:
 sourceOrigin:
 description: >-
 The site of the top-level URL the browser was visiting
 at the start of the request

 to the endpoint that set the cookie.

 In Chrome, maps to the CDP's \`topLevelSite\` partition
 key.
 type: string
 hasCrossSiteAncestor:
 description: >-
 Indicates if the cookie has any ancestors that are
 cross-site to

 the topLevelSite.

 Supported only in Chrome.
 type: boolean
 additionalProperties: false
 required:
 \- sourceOrigin
 $schema: http://json-schema.org/draft-07/schema#
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/unblock
 tags:
 \- Browser REST APIs
 /chrome/bql?(/\*):
 post:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise, hosted and self-hosted
 plans. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/)

 Parses and executes BrowserQL requests, powered by the BrowserQL Editor
 or by other API integrations. See the BrowserQL Editor for more
 documentation on this API.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: blockConsentModals
 schema:
 type: boolean
 \- in: query
 name: humanlike
 schema:
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 query:
 type: string
 operationName:
 type: string
 variables:
 type: object
 additionalProperties: {}
 type: object
 responses:
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/bql?(/\*)
 tags:
 \- Browser REST APIs
 /chromium/bql?(/\*):
 post:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise, hosted and self-hosted
 plans. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/)

 Parses and executes BrowserQL requests, powered by the BrowserQL Editor
 or by other API integrations. See the BrowserQL Editor for more
 documentation on this API.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: blockConsentModals
 schema:
 type: boolean
 \- in: query
 name: humanlike
 schema:
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content:
 application/json:
 schema:
 properties:
 query:
 type: string
 operationName:
 type: string
 variables:
 type: object
 additionalProperties: {}
 type: object
 responses:
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/bql?(/\*)
 tags:
 \- Browser REST APIs
 /chrome/live/\*:
 get:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise plans and self-hosted
 Enterprise plans. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/), or \[sign-up\
 here\](https://www.browserless.io/pricing/).

 Websocket back-end that powers the live session experience.
 parameters: \[\]
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/live/\*
 tags:
 \- Browser WebSocket APIs
 /chrome/stealth:
 get:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise and Cloud-unit plans.
 \[Contact us for more information\
 here.\](https://www.browserless.io/contact/), or \[sign-up\
 here\](https://www.browserless.io/pricing/).

 Launch and connect to Stealthy Chromium with a library like puppeteer or
 others that work over chrome-devtools-protocol for scraping in a more
 stealth-like fashion.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chrome/stealth
 tags:
 \- Browser WebSocket APIs
 /chromium/live/\*:
 get:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise plans and self-hosted
 Enterprise plans. \[Contact us for more information\
 here.\](https://www.browserless.io/contact/), or \[sign-up\
 here\](https://www.browserless.io/pricing/).

 Websocket back-end that powers the live session experience.

 \*\*Note:\*\* This endpoint is also available at: \`/live/\*\` for backwards
 compatibility.
 parameters: \[\]
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/live/\*
 tags:
 \- Browser WebSocket APIs
 /chromium/stealth:
 get:
 definitions: {}
 description: >-
 \> This API is only available for Enterprise and Cloud-unit plans.
 \[Contact us for more information\
 here.\](https://www.browserless.io/contact/), or \[sign-up\
 here\](https://www.browserless.io/pricing/).

 Launch and connect to Stealthy Chromium with a library like puppeteer or
 others that work over chrome-devtools-protocol for scraping in a more
 stealth-like fashion.

 \*\*Note:\*\* This endpoint is also available at: \`/stealth\` for backwards
 compatibility.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /chromium/stealth
 tags:
 \- Browser WebSocket APIs
 /reconnect/\*:
 get:
 definitions: {}
 description: >-
 Reconnect to an existing Chromium or Chrome session with a library like
 puppeteer or others that work over chrome-devtools-protocol.
 parameters:
 \- in: query
 name: blockAds
 schema:
 description: \|-
 Whether or nor to load ad-blocking extensions for the session.
 This currently uses uBlock-Lite and may cause certain sites
 to not load properly.
 type: boolean
 \- in: query
 name: launch
 schema:
 description: \|-
 Launch options, which can be either an object
 of puppeteer.launch options or playwright.launchServer
 options, depending on the API. Must be either JSON
 object, or a base64-encoded JSON object.
 anyOf:
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).CDPLaunchOptions
 \- $ref: >-
 #/definitions/import("/home/runner/work/enterprise/enterprise/node\_modules/@browserless.io/browserless/build/types",{with:{"resolution-mode":"import"}}).BrowserServerOptions
 \- type: string
 \- in: query
 name: timeout
 schema:
 description: \|-
 Override the system-level timeout for this request.
 Accepts a value in milliseconds.
 type: number
 \- in: query
 name: token
 schema:
 description: The authorization token
 type: string
 \- in: query
 name: trackingId
 schema:
 description: Custom session identifier
 type: string
 requestBody:
 content: {}
 responses:
 '101':
 description: Indicates successful WebSocket upgrade.
 '400':
 code: 400
 description: The request contains errors or didn't properly encode content.
 message: HTTP/1.1 400 Bad Request
 '401':
 code: 401
 description: The request is missing, or contains bad, authorization credentials.
 message: HTTP/1.1 401 Unauthorized
 '404':
 code: 404
 description: Resource couldn't be found.
 message: HTTP/1.1 404 Not Found
 '408':
 code: 408
 description: The request took has taken too long to process.
 message: HTTP/1.1 408 Request Timeout
 '429':
 code: 429
 description: Too many requests are currently being processed.
 message: HTTP/1.1 429 Too Many Requests
 '500':
 code: 500
 description: An internal error occurred when handling the request.
 message: HTTP/1.1 500 Internal Server Error
 summary: /reconnect/\*
 tags:
 \- Browser WebSocket APIs
servers: \[\]
components: {}