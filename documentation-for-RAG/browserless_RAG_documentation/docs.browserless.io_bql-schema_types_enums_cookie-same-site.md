---
url: "https://docs.browserless.io/bql-schema/types/enums/cookie-same-site"
title: "CookieSameSite | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site#__docusaurus_skipToContent_fallback)

On this page

The values a cookie's SameSite attribute can hold

```codeBlockLines_p187
enum CookieSameSite {
  Strict
  Lax
  None
}

```

### Values [​](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site\#values "Direct link to Values")

#### [`CookieSameSite.Strict`](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site\#) [​](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site\#cookiesamesitestrict "Direct link to cookiesamesitestrict")

Cookies are only sent in a first-party context and not sent along with requests initiated by third party websites

#### [`CookieSameSite.Lax`](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site\#) [​](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site\#cookiesamesitelax "Direct link to cookiesamesitelax")

Cookies are withheld on cross-site sub-requests, such as calls to load images or frames, but are sent when a user navigates to the URL from an external site

#### [`CookieSameSite.None`](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site\#) [​](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site\#cookiesamesitenone "Direct link to cookiesamesitenone")

Cookies are sent in all contexts, in responses to both first-party and cross-origin requests

### Member Of [​](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site\#member-of "Direct link to Member Of")

[`CookieInput`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input) input ● [`StandardCookie`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie) object

- [Values](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site#values)
- [Member Of](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site#member-of)