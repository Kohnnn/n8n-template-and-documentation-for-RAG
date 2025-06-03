---
url: "https://docs.browserless.io/bql-schema/responses"
title: "Responses | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/responses#__docusaurus_skipToContent_fallback)

On this page

This page presents reference for all mutations responses.

## `CaptchaResponse` [​](https://docs.browserless.io/bql-schema/responses\#captcharesponse "Direct link to captcharesponse")

Represents the response structure for solving a captcha.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `time` | `Float` | The total time it took to find and solve the captcha. |
| `found` | `Boolean` | Indicates if a captcha was found. |
| `solved` | `Boolean` | Indicates if a captcha was found and solved. |
| `token` | `String` | The solved token of the captcha response, if any is provided. |

## `ClickResponse` [​](https://docs.browserless.io/bql-schema/responses\#clickresponse "Direct link to clickresponse")

Represents the response structure for clicking on an element.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `selector` | `String` | The selector text of the clicked element, if specified. |
| `x` | `Float` | The x-coordinate of the click, in pixels, on the page. |
| `y` | `Float` | The y-coordinate of the click, in pixels, on the page. |
| `time` | `Float` | The amount of time, in milliseconds, elapsed since the start of clicking to completion. |

## `CookieResponse` [​](https://docs.browserless.io/bql-schema/responses\#cookieresponse "Direct link to cookieresponse")

Represents the response structure for setting and retrieving cookies.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `cookies` | `[StandardCookie]` | A standard cookie object with the values of the set cookies. |
| `time` | `Float` | The time it took to set the cookies. |

## `DefaultResponse` [​](https://docs.browserless.io/bql-schema/responses\#defaultresponse "Direct link to defaultresponse")

Represents the default response structure for methods.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `timeout` | `Float` | The default timeout for all methods. |

## `EvaluateResponse` [​](https://docs.browserless.io/bql-schema/responses\#evaluateresponse "Direct link to evaluateresponse")

Represents the response structure for evaluating a script in the browser.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `value` | `String` | The returned value of the script, if any. |
| `time` | `Float` | The time it took for the evaluate call to complete. |

## `HTMLResponse` [​](https://docs.browserless.io/bql-schema/responses\#htmlresponse "Direct link to htmlresponse")

Represents the response structure for retrieving a page's HTML content.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `html` | `String` | The content of the page's HTML. |
| `time` | `Float` | The amount of time, in milliseconds, elapsed since the start of content retrieval to completion. |

## `HTTPResponse` [​](https://docs.browserless.io/bql-schema/responses\#httpresponse "Direct link to httpresponse")

Represents the HTTP response structure for a page load.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `status` | `Int` | The status code of the response from the initial page load. |
| `text` | `String` | The status text of the response from the initial page load, generally `"ok"`. |
| `url` | `String` | The final URL of the page after any potential redirects or URL rewrites. |
| `time` | `Float` | The amount of time, in milliseconds, elapsed since the start of navigation to completion. |

## `HoverResponse` [​](https://docs.browserless.io/bql-schema/responses\#hoverresponse "Direct link to hoverresponse")

Represents the response structure for hovering over an element.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `selector` | `String` | The selector text of the hovered element. |
| `x` | `Float` | The x-coordinate in pixels, on the page. |
| `y` | `Float` | The y-coordinate in pixels, on the page. |
| `time` | `Float` | The amount of time, in milliseconds, elapsed since the start to completion. |

## `JavaScriptResponse` [​](https://docs.browserless.io/bql-schema/responses\#javascriptresponse "Direct link to javascriptresponse")

Represents the response structure for enabling or disabling JavaScript on a page.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `enabled` | `Boolean` | Whether JavaScript is enabled on the page. |
| `time` | `Float` | The time it took to perform this action. |

## `PDFResponse` [​](https://docs.browserless.io/bql-schema/responses\#pdfresponse "Direct link to pdfresponse")

Represents the response structure for generating a PDF.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `base64` | `String` | Base64 encoded PDF content. |
| `size` | `Float` | The size of the resulting PDF in bytes. |
| `time` | `Float` | The time it took to generate the PDF. |

## `QuerySelectorResponse` [​](https://docs.browserless.io/bql-schema/responses\#queryselectorresponse "Direct link to queryselectorresponse")

Represents the response structure for querying an element using `querySelector`.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `id` | `String` | The element's identifier, reflecting the `id` global attribute. |
| `childElementCount` | `Float` | The number of child elements of this element. |
| `className` | `String` | The value of the class attribute of the specified element. |
| `innerHTML` | `String` | The HTML or XML markup contained within the element. |
| `innerText` | `String` | The text contained within the element. |
| `localName` | `String` | The local part of the qualified name of the element. |
| `outerHTML` | `String` | The serialized HTML fragment describing the element and its descendants. |

## `ReconnectionResponse` [​](https://docs.browserless.io/bql-schema/responses\#reconnectionresponse "Direct link to reconnectionresponse")

Represents the response structure for reconnecting to a browser session.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `browserQLEndpoint` | `String` | The fully-qualified URL to reconnect future BrowserQL sessions. Token information might be required. |
| `browserWSEndpoint` | `String` | The fully-qualified URL of the browserWSEndpoint for use with libraries like Playwright or Puppeteer. Token information might be required. |
| `devtoolsFrontendUrl` | `String` | The fully-qualified URL of the devtools resources for remotely loading Chrome's developer tools. |
| `webSocketDebuggerUrl` | `String` | The underlying page's WebSocketDebuggerUrl for libraries that operate on a page rather than a browser object. |

## `ScrollResponse` [​](https://docs.browserless.io/bql-schema/responses\#scrollresponse "Direct link to scrollresponse")

Represents the response structure for scrolling to an element or coordinate.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `selector` | `String` | The CSS selector of the element on the page scrolled to. |
| `x` | `Float` | The x-coordinate, in pixels, to scroll to. |
| `y` | `Float` | The y-coordinate, in pixels, to scroll to. |
| `time` | `Float` | The amount of time, in milliseconds, elapsed since the start of scrolling to completion. |

## `ScreenshotResponse` [​](https://docs.browserless.io/bql-schema/responses\#screenshotresponse "Direct link to screenshotresponse")

Represents the response structure for taking a screenshot.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `base64` | `String` | The base64 encoded image of the screenshot. |
| `format` | `String` | The format of the screenshot. |
| `time` | `Float` | The time it took to take the screenshot. |

## `SelectResponse` [​](https://docs.browserless.io/bql-schema/responses\#selectresponse "Direct link to selectresponse")

Represents the response structure for selecting a value from a dropdown or multiple select element.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `selector` | `String` | The selector of the element you selected from. |
| `value` | `StringOrArray` | The value or values you selected from the select element. |
| `time` | `Float` | The amount of time, in milliseconds, elapsed since the start of selecting to completion. |

## `TextResponse` [​](https://docs.browserless.io/bql-schema/responses\#textresponse "Direct link to textresponse")

Represents the response structure for retrieving the textual content of a page.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `text` | `String` | The textual content of the page. |
| `time` | `Float` | The amount of time, in milliseconds, elapsed since the start of text retrieval to completion. |

## `TitleResponse` [​](https://docs.browserless.io/bql-schema/responses\#titleresponse "Direct link to titleresponse")

Represents the response structure for retrieving the title of the current page.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `title` | `String` | The title of the current page. |

## `TypeResponse` [​](https://docs.browserless.io/bql-schema/responses\#typeresponse "Direct link to typeresponse")

Represents the response structure for typing text into an element.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `selector` | `String` | The selector of the element you typed into. |
| `text` | `String` | The textual content that was typed. |
| `x` | `Float` | The x-coordinate of the element, in pixels, on the page. |
| `y` | `Float` | The y-coordinate of the element, in pixels, on the page. |
| `time` | `Float` | The amount of time, in milliseconds, elapsed since the start of typing to completion. |

## `URLResponse` [​](https://docs.browserless.io/bql-schema/responses\#urlresponse "Direct link to urlresponse")

Represents the response structure for retrieving the URL of the current page.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `url` | `String` | The URL of the current page. |

## `VerifyResponse` [​](https://docs.browserless.io/bql-schema/responses\#verifyresponse "Direct link to verifyresponse")

Represents the response structure for a verification action.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `time` | `Float` | The total time it took to find and click the verification. |
| `found` | `Boolean` | Indicates if a verification was found. |
| `solved` | `Boolean` | Indicates if a verification was found and clicked. |

## `WaitForRequest` [​](https://docs.browserless.io/bql-schema/responses\#waitforrequest "Direct link to waitforrequest")

Represents the response structure for waiting for a specific request.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `time` | `Float` | The period of time elapsed, in milliseconds, waited for. |
| `url` | `String` | The URL parameter used to match the response with. |

## `WaitForResponse` [​](https://docs.browserless.io/bql-schema/responses\#waitforresponse "Direct link to waitforresponse")

Represents the response structure for waiting for a specific response.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `time` | `Float` | The period of time elapsed, in milliseconds, waited for. |
| `status` | `Int` | The status code of the response. |
| `url` | `String` | The URL parameter used to match the response with. |

## `WaitForSelector` [​](https://docs.browserless.io/bql-schema/responses\#waitforselector "Direct link to waitforselector")

Represents the response structure for waiting for a selector.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `time` | `Float` | The period of time elapsed, in milliseconds, waited for. |
| `selector` | `String` | The selector waited for. |
| `x` | `Float` | The x-coordinate position, in pixels, left of the viewport. |
| `y` | `Float` | The y-coordinate position, in pixels, top of the viewport. |
| `width` | `Float` | The width, in pixels, of the element. |
| `height` | `Float` | The height, in pixels, of the element. |

## `WaitForTimeout` [​](https://docs.browserless.io/bql-schema/responses\#waitfortimeout "Direct link to waitfortimeout")

Represents the response structure for waiting a specified period.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `time` | `Float` | The period of time elapsed, in milliseconds, waited for. |

- [`CaptchaResponse`](https://docs.browserless.io/bql-schema/responses#captcharesponse)
- [`ClickResponse`](https://docs.browserless.io/bql-schema/responses#clickresponse)
- [`CookieResponse`](https://docs.browserless.io/bql-schema/responses#cookieresponse)
- [`DefaultResponse`](https://docs.browserless.io/bql-schema/responses#defaultresponse)
- [`EvaluateResponse`](https://docs.browserless.io/bql-schema/responses#evaluateresponse)
- [`HTMLResponse`](https://docs.browserless.io/bql-schema/responses#htmlresponse)
- [`HTTPResponse`](https://docs.browserless.io/bql-schema/responses#httpresponse)
- [`HoverResponse`](https://docs.browserless.io/bql-schema/responses#hoverresponse)
- [`JavaScriptResponse`](https://docs.browserless.io/bql-schema/responses#javascriptresponse)
- [`PDFResponse`](https://docs.browserless.io/bql-schema/responses#pdfresponse)
- [`QuerySelectorResponse`](https://docs.browserless.io/bql-schema/responses#queryselectorresponse)
- [`ReconnectionResponse`](https://docs.browserless.io/bql-schema/responses#reconnectionresponse)
- [`ScrollResponse`](https://docs.browserless.io/bql-schema/responses#scrollresponse)
- [`ScreenshotResponse`](https://docs.browserless.io/bql-schema/responses#screenshotresponse)
- [`SelectResponse`](https://docs.browserless.io/bql-schema/responses#selectresponse)
- [`TextResponse`](https://docs.browserless.io/bql-schema/responses#textresponse)
- [`TitleResponse`](https://docs.browserless.io/bql-schema/responses#titleresponse)
- [`TypeResponse`](https://docs.browserless.io/bql-schema/responses#typeresponse)
- [`URLResponse`](https://docs.browserless.io/bql-schema/responses#urlresponse)
- [`VerifyResponse`](https://docs.browserless.io/bql-schema/responses#verifyresponse)
- [`WaitForRequest`](https://docs.browserless.io/bql-schema/responses#waitforrequest)
- [`WaitForResponse`](https://docs.browserless.io/bql-schema/responses#waitforresponse)
- [`WaitForSelector`](https://docs.browserless.io/bql-schema/responses#waitforselector)
- [`WaitForTimeout`](https://docs.browserless.io/bql-schema/responses#waitfortimeout)