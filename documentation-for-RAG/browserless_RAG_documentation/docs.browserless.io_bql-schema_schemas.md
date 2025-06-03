---
url: "https://docs.browserless.io/bql-schema/schemas"
title: "Schemas | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/schemas#__docusaurus_skipToContent_fallback)

On this page

This page presents reference for all remaining schemas.

## `CaptchaTypes` [​](https://docs.browserless.io/bql-schema/schemas\#captchatypes "Direct link to captchatypes")

Represents an enumeration of supported captcha types.

| **Enum Value** | **Description** |
| --- | --- |
| `hcaptcha` | Represents the hCaptcha type. |
| `recaptcha` | Represents the reCaptcha type. |

## `CookieInput` [​](https://docs.browserless.io/bql-schema/schemas\#cookieinput "Direct link to cookieinput")

Represents the structure for defining cookie input properties.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `name` | `String!` | The cookie's name. |
| `value` | `String!` | The cookie's value. |
| `url` | `String` | The request-URI to associate with the cookie, affecting default domain, path, source port, and scheme. |
| `domain` | `String` | The domain associated with the cookie. |
| `path` | `String` | The path associated with the cookie. |
| `secure` | `Boolean` | Indicates if the cookie is secure. |
| `httpOnly` | `Boolean` | Indicates if the cookie is HTTP-only. |
| `sameSite` | `CookieSameSite` | Specifies the `SameSite` policy for the cookie. |
| `expires` | `Float` | The expiration date of the cookie as a timestamp. Session cookie if not set. |

## `CookieSameSite` [​](https://docs.browserless.io/bql-schema/schemas\#cookiesamesite "Direct link to cookiesamesite")

Represents an enumeration of supported `SameSite` cookie policies.

| **Enum Value** | **Description** |
| --- | --- |
| `Strict` | Strict `SameSite` policy. |
| `Lax` | Lax `SameSite` policy. |
| `None` | No `SameSite` policy enforced. |

## `Method` [​](https://docs.browserless.io/bql-schema/schemas\#method "Direct link to method")

Represents an enumeration of supported HTTP methods for waiting.

| **Enum Value** | **Description** |
| --- | --- |
| `GET` | HTTP GET method. |
| `HEAD` | HTTP HEAD method. |
| `POST` | HTTP POST method. |
| `PUT` | HTTP PUT method. |
| `DELETE` | HTTP DELETE method. |
| `CONNECT` | HTTP CONNECT method. |
| `OPTIONS` | HTTP OPTIONS method. |
| `TRACE` | HTTP TRACE method. |
| `PATCH` | HTTP PATCH method. |

## `PDFPageFormat` [​](https://docs.browserless.io/bql-schema/schemas\#pdfpageformat "Direct link to pdfpageformat")

Represents an enumeration of supported PDF page formats.

| **Enum Value** | **Dimensions** |
| --- | --- |
| `letter` | 8.5in x 11in |
| `legal` | 8.5in x 14in |
| `tabloid` | 11in x 17in |
| `ledger` | 17in x 11in |
| `a0` | 33.1102in x 46.811in |
| `a1` | 23.3858in x 33.1102in |
| `a2` | 16.5354in x 23.3858in |
| `a3` | 11.6929in x 16.5354in |
| `a4` | 8.2677in x 11.6929in |
| `a5` | 5.8268in x 8.2677in |
| `a6` | 4.1339in x 5.8268in |

## `RequestInput` [​](https://docs.browserless.io/bql-schema/schemas\#requestinput "Direct link to requestinput")

Represents the structure for specifying input for HTTP request monitoring.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `url` | `String` | The pattern of the request URL to wait for, using glob-style pattern-matching. |
| `method` | `Method` | The HTTP method of the request. |

## `ResponseInput` [​](https://docs.browserless.io/bql-schema/schemas\#responseinput "Direct link to responseinput")

Represents the structure for specifying input for HTTP response monitoring.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `url` | `String` | The pattern of the response URL to wait for, using glob-style pattern-matching. |
| `codes` | `[Int]` | The HTTP response code(s) to wait for. Can be a single HTTP code or a list of desired codes. |

## `ScreenshotClip` [​](https://docs.browserless.io/bql-schema/schemas\#screenshotclip "Direct link to screenshotclip")

Represents the structure for specifying a region to clip in a screenshot.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `x` | `Float` | The x-coordinate to start clipping, in pixels. |
| `y` | `Float` | The y-coordinate to start clipping, in pixels. |
| `width` | `Float` | The width of the clip, in pixels. |
| `height` | `Float` | The height of the clip, in pixels. |
| `scale` | `Float` | The scale factor of the clip. |

## `ScreenshotType` [​](https://docs.browserless.io/bql-schema/schemas\#screenshottype "Direct link to screenshottype")

Represents an enumeration of supported screenshot formats.

| **Enum Value** | **Description** |
| --- | --- |
| `jpeg` | JPEG image format. |
| `png` | PNG image format. |
| `webp` | WEBP image format. |

## `StandardCookie` [​](https://docs.browserless.io/bql-schema/schemas\#standardcookie "Direct link to standardcookie")

Represents the structure of a standard cookie object.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| `name` | `String!` | The cookie's name. |
| `value` | `String!` | The cookie's value. |
| `url` | `String` | The request-URI to associate with the cookie, affecting default domain, path, source port, and scheme. |
| `domain` | `String` | The domain associated with the cookie. |
| `path` | `String` | The path associated with the cookie. |
| `secure` | `Boolean` | Indicates if the cookie is secure. |
| `httpOnly` | `Boolean` | Indicates if the cookie is HTTP-only. |
| `sameSite` | `CookieSameSite` | Specifies the `SameSite` policy for the cookie. |
| `expires` | `Float` | The expiration date of the cookie as a timestamp. Session cookie if not set. |

## `VerifyTypes` [​](https://docs.browserless.io/bql-schema/schemas\#verifytypes "Direct link to verifytypes")

Represents an enumeration of supported verification types.

| **Enum Value** | **Description** |
| --- | --- |
| `cloudflare` | Represents the Cloudflare verification type. |

## `WaitUntilGoto` [​](https://docs.browserless.io/bql-schema/schemas\#waituntilgoto "Direct link to waituntilgoto")

Represents an enumeration of options for determining when the page is considered loaded.

| **Enum Value** | **Description** |
| --- | --- |
| `commit` | Fired when a network response is received and the document starts loading. |
| `domContentLoaded` | Fired when the `DOMContentLoaded` event is fired. |
| `load` | Fired when the `load` event occurs. |
| `firstMeaningfulPaint` | Indicates when the primary content of the page is visible to the user. |
| `firstContentfulPaint` | The render time of the largest image or text block visible in the viewport. |
| `networkIdle` | Fired when there are no network connections for at least 500 ms. Use with caution. |
| `interactiveTime` | Chrome's best guess as to when the page becomes interactable. Use with caution. |

## `WaitUntilHistory` [​](https://docs.browserless.io/bql-schema/schemas\#waituntilhistory "Direct link to waituntilhistory")

Represents an enumeration of options for determining when the history event occurs.

| **Enum Value** | **Description** |
| --- | --- |
| `commit` | Fired when a network response is received and the document starts loading. |
| `domContentLoaded` | Fired when the `DOMContentLoaded` event is fired. |
| `load` | Fired when the `load` event occurs. |
| `networkIdle` | Fired when there are no network connections for at least 500 ms. Use with caution. |

- [`CaptchaTypes`](https://docs.browserless.io/bql-schema/schemas#captchatypes)
- [`CookieInput`](https://docs.browserless.io/bql-schema/schemas#cookieinput)
- [`CookieSameSite`](https://docs.browserless.io/bql-schema/schemas#cookiesamesite)
- [`Method`](https://docs.browserless.io/bql-schema/schemas#method)
- [`PDFPageFormat`](https://docs.browserless.io/bql-schema/schemas#pdfpageformat)
- [`RequestInput`](https://docs.browserless.io/bql-schema/schemas#requestinput)
- [`ResponseInput`](https://docs.browserless.io/bql-schema/schemas#responseinput)
- [`ScreenshotClip`](https://docs.browserless.io/bql-schema/schemas#screenshotclip)
- [`ScreenshotType`](https://docs.browserless.io/bql-schema/schemas#screenshottype)
- [`StandardCookie`](https://docs.browserless.io/bql-schema/schemas#standardcookie)
- [`VerifyTypes`](https://docs.browserless.io/bql-schema/schemas#verifytypes)
- [`WaitUntilGoto`](https://docs.browserless.io/bql-schema/schemas#waituntilgoto)
- [`WaitUntilHistory`](https://docs.browserless.io/bql-schema/schemas#waituntilhistory)