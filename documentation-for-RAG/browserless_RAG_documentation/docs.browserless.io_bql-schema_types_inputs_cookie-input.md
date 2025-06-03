---
url: "https://docs.browserless.io/bql-schema/types/inputs/cookie-input"
title: "CookieInput | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/types/inputs/cookie-input#__docusaurus_skipToContent_fallback)

On this page

The cookie to be sent to the page

```codeBlockLines_p187
input CookieInput {
  domain: String
  expires: Float
  httpOnly: Boolean
  name: String!
  path: String
  sameSite: CookieSameSite
  secure: Boolean
  url: String
  value: String!
}

```

### Fields [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#fields "Direct link to Fields")

#### [`CookieInput.domain`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#cookieinputdomainstring- "Direct link to cookieinputdomainstring-")

Cookie domain

#### [`CookieInput.expires`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#) ● [`Float`](https://docs.browserless.io/bql-schema/types/scalars/float) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#cookieinputexpiresfloat- "Direct link to cookieinputexpiresfloat-")

Cookie expiration date, session cookie if not set

#### [`CookieInput.httpOnly`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#cookieinputhttponlyboolean- "Direct link to cookieinputhttponlyboolean-")

True if cookie is http-only

#### [`CookieInput.name`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#cookieinputnamestring-- "Direct link to cookieinputnamestring--")

Cookie name

#### [`CookieInput.path`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#cookieinputpathstring- "Direct link to cookieinputpathstring-")

Cookie path

#### [`CookieInput.sameSite`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#) ● [`CookieSameSite`](https://docs.browserless.io/bql-schema/types/enums/cookie-same-site) enum [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#cookieinputsamesitecookiesamesite- "Direct link to cookieinputsamesitecookiesamesite-")

Cookie SameSite type

#### [`CookieInput.secure`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#cookieinputsecureboolean- "Direct link to cookieinputsecureboolean-")

True if cookie is secure

#### [`CookieInput.url`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#cookieinputurlstring- "Direct link to cookieinputurlstring-")

The request-URI to associate with the setting of the cookie. This value can affect the default domain, path, source port, and source scheme values of the created cookie

#### [`CookieInput.value`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#) ● [`String!`](https://docs.browserless.io/bql-schema/types/scalars/string) non-nullscalar [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#cookieinputvaluestring-- "Direct link to cookieinputvaluestring--")

Cookie value

### Member Of [​](https://docs.browserless.io/bql-schema/types/inputs/cookie-input\#member-of "Direct link to Member Of")

[`cookies`](https://docs.browserless.io/bql-schema/operations/mutations/cookies) mutation

- [Fields](https://docs.browserless.io/bql-schema/types/inputs/cookie-input#fields)
- [Member Of](https://docs.browserless.io/bql-schema/types/inputs/cookie-input#member-of)