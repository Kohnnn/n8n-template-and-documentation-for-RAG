---
url: "https://docs.browserless.io/baas/v1/recipes/using-a-proxy"
title: "Using a proxy in Puppeteer | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/recipes/using-a-proxy#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/proxies) or [BrowserQL](https://docs.browserless.io/browserql/start).

success

We now have our own built-in residential proxy! [See this document here for how to use it.](https://docs.browserless.io/baas/proxies)

Both browserless, and Chrome itself, support the usage of external proxies. Paid cloud-unit plans have access to a built-in proxy which requires no additional work on your part. [See more about that here.](https://docs.browserless.io/baas/proxies).

If you want to use an external, or 3rd party proxy, please continue to read below. In general there's two things you'll have to do:

- Specify the address of where the proxy is with the `--proxy-server` switch.
- Optionally, you'll also need to send in your username and password if the proxy is authenticated.

## Specifying the proxy [​](https://docs.browserless.io/baas/v1/recipes/using-a-proxy\#specifying-the-proxy "Direct link to Specifying the proxy")

Regardless of whether or not you're using our REST API's or the puppeteer integration, you'll need to specify _where_ the proxy is. Chrome has a command-line flag to do this, and we support this in browserless via the following query-string parameter:

```codeBlockLines_p187
?--proxy-server=https://YOUR-PROXY-SERVER-DOMAIN:PORT

```

You can set this parameter in our [live debugger](https://chrome.browserless.io/) by clicking on the gear icon on the left panel and modifying the Browser URL field.

If you're using a proxy that doesn't require a password (maybe just an IP address filter), then that's it! You're free to now use this proxy going forward! Otherwise read on.

## Using username and password [​](https://docs.browserless.io/baas/v1/recipes/using-a-proxy\#using-username-and-password "Direct link to Using username and password")

### Method 1: page.authenticate [​](https://docs.browserless.io/baas/v1/recipes/using-a-proxy\#method-1-pageauthenticate "Direct link to Method 1: page.authenticate")

Most proxies will require some means of authentication. There's generally two ways you can do this in Puppeteer, and also in browserless. The first more common method is the `page.authenticate`:

```codeBlockLines_p187
await page.authenticate({
  username: 'joel',
  password: 'browserless-rocks',
});

```

Doing this will apply these parameters to your network requests going forward.

In our REST API's you can specify these fields with the following in your POST JSON body. These parameters work for the `pdf`, `content` and `screenshot` APIs:

```codeBlockLines_p187
{
  "authenticate": {
    "username": "joel",
    "password": "browserless-rocks"
  }
}

```

### Method 2: page.setExtraHTTPHeaders [​](https://docs.browserless.io/baas/v1/recipes/using-a-proxy\#method-2-pagesetextrahttpheaders "Direct link to Method 2: page.setExtraHTTPHeaders")

The other mechanism is to use HTTP headers to send in extra authorization information. Puppeteer makes this pretty easy by allowing us to send in new HTTP headers via `page.setExtraHTTPHeaders`:

> NOTE: This is deprecated in most libraries now, so it's worth keeping in mind that using authentication methods in each library is now the standard.

```codeBlockLines_p187
// Remember to base64 encode your username:password!
await page.setExtraHTTPHeaders({
  'Proxy-Authorization': 'Basic username:password',
  // OR
  Authorization: 'Basic username:password',
});

```

Refer to your libraries documentation on what the name of the headers is, and how to properly encode it.

We also allow this in our REST APIs as well, via the `setExtraHTTPHeaders` property:

```codeBlockLines_p187
{
  "setExtraHTTPHeaders": {
    "Proxy-Authorization": "Basic username:password",
    // OR
    "Authorization": "Basic username:password"
  }
}

```

This will allow your REST APIs to utilize the prior provided proxy!

- [Specifying the proxy](https://docs.browserless.io/baas/v1/recipes/using-a-proxy#specifying-the-proxy)
- [Using username and password](https://docs.browserless.io/baas/v1/recipes/using-a-proxy#using-username-and-password)
  - [Method 1: page.authenticate](https://docs.browserless.io/baas/v1/recipes/using-a-proxy#method-1-pageauthenticate)
  - [Method 2: page.setExtraHTTPHeaders](https://docs.browserless.io/baas/v1/recipes/using-a-proxy#method-2-pagesetextrahttpheaders)