---
url: "https://docs.browserless.io/browserql/scraping/bot-detectors"
title: "Bypassing bot detectors | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/scraping/bot-detectors#__docusaurus_skipToContent_fallback)

On this page

If you're scraping, you're probably coming up against bot detectors. BrowserQL hides most fingerprints, but there's still some settings to be aware.

Note

This information is for bypassing passive bot detectors. For log ins and compulsory CAPTCHAs, check out the [UI Automation](https://docs.browserless.io/ui-automation) section.

## Built-In Proxies [​](https://docs.browserless.io/browserql/scraping/bot-detectors\#built-in-proxies "Direct link to Built-In Proxies")

Use the `proxy` mutation to connect through the Browserless residential proxy to avoid IP-based detection mechanisms.

The example below shows how to use the proxy mutation with browserless's proxy for all requests and proxy through Brazil:

```codeBlockLines_p187
mutation residential_proxy_example{
  proxy(
    url: "*"
    country: BR
  ) {
    time
  }
}

```

Proxy Mutation

You can see detailed information on the proxy mutation [here](https://docs.browserless.io/bql-schema/operations/mutations/proxy).

## External Proxies [​](https://docs.browserless.io/browserql/scraping/bot-detectors\#external-proxies "Direct link to External Proxies")

You can use the `proxy` mutation to connect your own proxies. This mutation can proxy requests by a specified set of conditions, through your external proxy. Only requests that match these conditions are proxies and the rest are sent from the instance's own IP address.

To use your own proxy for all requests, you will use the following query:

```codeBlockLines_p187
mutation external_proxy_example{
  proxy(
    url: "*"
    server: "http://username:password@my-proxy.com:12321"
  ) {
    time
  }
}

```

Where the server parameter takes the following format:

```codeBlockLines_p187
${protocol}://${username}:${password}@${host}:${port}

```

For example, if you have:

- Username: `john`
- Password: `1337code`
- URL: `myproxy.com`
- Port: `1234`

The server argument would look like:

```codeBlockLines_p187
http://john:1337@myproxy.com:1234

```

If you don't have a username or password, you can simply omit those fields in the URI.

## Rejecting Requests [​](https://docs.browserless.io/browserql/scraping/bot-detectors\#rejecting-requests "Direct link to Rejecting Requests")

You can reject unnecessary requests to reduce proxy consumption and improve efficiency. The reject mutation allows you to block requests based on:

- **URL patterns**: Use glob-style patterns to match specific domains or paths.
- **HTTP methods**: Reject specific request methods (e.g., GET, POST).
- **Resource types**: Filter by resource types, such as images, media, or scripts.
- **Operators**: Define whether conditions should be combined using "and" (all must match) or "or" (any match).

For example, you can reject images, media, font and styles as follows:

```codeBlockLines_p187
mutation reject_images{
  reject(type: [image, media, font, stylesheet]) {
    enabled
    time
  }
  goto(url: "https://cnn.com", waitUntil: firstContentfulPaint) {
    status
    time
  }
}

```

## Filtering requests [​](https://docs.browserless.io/browserql/scraping/bot-detectors\#filtering-requests "Direct link to Filtering requests")

You can define which requests need to be proxied, based on URL pattern, request method and request type. To proxy all requests, simply use `url: "*"` to match everything. To proxy only the document requests, set `type: document` as follows:

```codeBlockLines_p187
mutation proxy_filtering{
  proxy(server: "http://john:1337@myproxy.com:1234" type: [document, xhr]) {
    time
  }

  goto(url: "https://nordvpn.com/what-is-my-ip/", waitUntil: load) {
    status
  }
}

```

You can even mix and match proxies, such as a residential proxy for the document and xhr, then the rest through a datacenter proxy.

## Chrome/Chromium Browsers [​](https://docs.browserless.io/browserql/scraping/bot-detectors\#chromechromium-browsers "Direct link to Chrome/Chromium Browsers")

You have a choice of running Chrome or Chromium browsers, which you can change in the session settings. Some detectors will block Chromium, but it's more efficient to run.

- [Built-In Proxies](https://docs.browserless.io/browserql/scraping/bot-detectors#built-in-proxies)
- [External Proxies](https://docs.browserless.io/browserql/scraping/bot-detectors#external-proxies)
- [Rejecting Requests](https://docs.browserless.io/browserql/scraping/bot-detectors#rejecting-requests)
- [Filtering requests](https://docs.browserless.io/browserql/scraping/bot-detectors#filtering-requests)
- [Chrome/Chromium Browsers](https://docs.browserless.io/browserql/scraping/bot-detectors#chromechromium-browsers)