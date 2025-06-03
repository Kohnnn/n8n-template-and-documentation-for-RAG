---
url: "https://docs.browserless.io/bql-schema/types/objects/cookie-response"
title: "CookieResponse | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/cookie-response#__docusaurus_skipToContent_fallback)

On this page

The response returned after setting or getting cookies

```codeBlockLines_p187
type CookieResponse {
  cookies: [StandardCookie]
  time: Float
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/cookie-response\#fields "Direct link to Fields")

#### [`CookieResponse.cookies`](https://docs.browserless.io/bql-schema/types/objects/cookie-response\#) ● [`[StandardCookie]`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie) listobject [​](https://docs.browserless.io/bql-schema/types/objects/cookie-response\#cookieresponsecookiesstandardcookie-- "Direct link to cookieresponsecookiesstandardcookie--")

A standard cookie object with the values of the set cookies

#### [`CookieResponse.time`](https://docs.browserless.io/bql-schema/types/objects/cookie-response\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/cookie-response\#cookieresponsetimefloat- "Direct link to cookieresponsetimefloat-")

The time it took to set and return the cookies

### Returned By [​](https://docs.browserless.io/bql-schema/types/objects/cookie-response\#returned-by "Direct link to Returned By")

[`cookies`](https://docs.browserless.io/bql-schema/operations/mutations/cookies) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/objects/cookie-response#fields)
- [Returned By](https://docs.browserless.io/bql-schema/types/objects/cookie-response#returned-by)