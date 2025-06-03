---
url: "https://docs.browserless.io/bql-schema/types/objects/standard-cookie"
title: "StandardCookie | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/objects/standard-cookie#__docusaurus_skipToContent_fallback)

On this page

A standard cookie

```codeBlockLines_p187
type StandardCookie {
  domain: String
  expires: Float
  httpOnly: Boolean
  name: String!
  path: String
  sameSite: CookieSameSite
  secure: Boolean
  value: String!
  url: String
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#fields "Direct link to Fields")

#### [`StandardCookie.domain`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#standardcookiedomainstring- "Direct link to standardcookiedomainstring-")

Cookie domain

#### [`StandardCookie.expires`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#standardcookieexpiresfloat- "Direct link to standardcookieexpiresfloat-")

Cookie expiration date, session cookie if not set

#### [`StandardCookie.httpOnly`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#standardcookiehttponlyboolean- "Direct link to standardcookiehttponlyboolean-")

True if cookie is http-only

#### [`StandardCookie.name`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#standardcookienamestring-- "Direct link to standardcookienamestring--")

Cookie name

#### [`StandardCookie.path`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#standardcookiepathstring- "Direct link to standardcookiepathstring-")

Cookie path

#### [`StandardCookie.sameSite`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#) ● [`CookieSameSite`](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site) enum [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#standardcookiesamesitecookiesamesite- "Direct link to standardcookiesamesitecookiesamesite-")

Cookie SameSite type

#### [`StandardCookie.secure`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#standardcookiesecureboolean- "Direct link to standardcookiesecureboolean-")

True if cookie is secure

#### [`StandardCookie.value`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#standardcookievaluestring-- "Direct link to standardcookievaluestring--")

Cookie value

#### [`StandardCookie.url`](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#standardcookieurlstring- "Direct link to standardcookieurlstring-")

The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, source port, and source scheme values of the created cookie

### Member Of [​](https://docs.browserless.io/bql-schema/types/objects/standard-cookie\#member-of "Direct link to Member Of")

[`CookieResponse`](https://docs.browserless.io/bql-schema/types/objects/cookie-response) object

- [Fields](https://docs.browserless.io/bql-schema/types/objects/standard-cookie#fields)
- [Member Of](https://docs.browserless.io/bql-schema/types/objects/standard-cookie#member-of)