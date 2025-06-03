---
url: "https://docs.browserless.io/bql-schema/operations/mutations/cookies"
title: "cookies | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/cookies#__docusaurus_skipToContent_fallback)

On this page

Sets and gets cookies on the page

Example:

```codeBlockLines_p187
mutation SetCookies {
  # Get the cookies on the page
  getCookies: cookies {
    cookies {
      name
      value
    }
  }

  # Set a cookie on the page
  setCookies: cookies(cookies: [\
      {\
        name: "my-cookie"\
        value: "my-value"\
        url: "https://example.com"\
      }\
  ]) {
    cookies {
      name
      value
    }
  }
}

```

```codeBlockLines_p187
cookies(
  cookies: [CookieInput]
): CookieResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/cookies\#arguments "Direct link to Arguments")

#### [`cookies.cookies`](https://docs.browserless.io/bql-schema/operations/mutations/cookies\#) ● [`[CookieInput]`](https://docs.browserless.io/bql-schema/types/inputs/cookie-input) listinput [​](https://docs.browserless.io/bql-schema/operations/mutations/cookies\#cookiescookiescookieinput-- "Direct link to cookiescookiescookieinput--")

The cookies to set on the page

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/cookies\#type "Direct link to Type")

#### [`CookieResponse`](https://docs.browserless.io/bql-schema/types/objects/cookie-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/cookies\#cookieresponse- "Direct link to cookieresponse-")

The response returned after setting or getting cookies

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/cookies#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/cookies#type)