---
url: "https://docs.browserless.io/browserql/bot-detection/proxies"
title: "Proxies | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/bot-detection/proxies#__docusaurus_skipToContent_fallback)

On this page

Proxies act as intermediaries between your device and the internet, enhancing privacy, security, and geographic flexibility by masking your IP address. This page covers the built-in proxy features in BrowserQL, tips for optimizing bandwidth usage with the reject API, and support for third-party proxies for more advanced configurations.

- [Built-in Proxies](https://docs.browserless.io/browserql/bot-detection/proxies#built-in-proxies)
- [External Proxies](https://docs.browserless.io/browserql/bot-detection/proxies#external-proxies)

## Built-In Proxies [​](https://docs.browserless.io/browserql/bot-detection/proxies\#built-in-proxies "Direct link to Built-In Proxies")

BrowserQL supports **residential proxies** to enhance privacy, security, and geographic flexibility in browser automation. These proxies help bypass location-specific restrictions, improve stealth, and avoid IP-based detection mechanisms. With built-in proxying, you can configure:

- **Proxy Country**: Route requests through a specific country.
- **Sticky Proxying**: Reuse the same proxy for multiple requests.

### How to Enable Built-In Proxies [​](https://docs.browserless.io/browserql/bot-detection/proxies\#how-to-enable-built-in-proxies "Direct link to How to Enable Built-In Proxies")

1. Open the **Session Settings Panel**.
2. Toggle **Residential Proxying** to `On`.
3. Configure your settings:
   - **Sticky Proxying**: Use the same IP for consecutive requests.
   - **Proxy Country**: Select the desired country for proxy routing.

warning

Using a proxy consumes **6 units per MB**.

Watch the video below to learn how to turn on proxy:

Your browser does not support the video tag.

### Optimizing Proxy Usage with the Reject Mutation [​](https://docs.browserless.io/browserql/bot-detection/proxies\#optimizing-proxy-usage-with-the-reject-mutation "Direct link to Optimizing Proxy Usage with the Reject Mutation")

The **reject mutation** optimizes your proxy usage by filtering unnecessary requests. This can help reduce bandwidth consumption and improve efficiency when using proxies. The reject mutation allows you to block requests based on:

- **URL patterns**: Use glob-style patterns to match specific domains or paths.
- **HTTP methods**: Reject specific request methods (e.g., GET, POST).
- **Resource types**: Filter by resource types, such as images, media, or scripts.
- **Operators**: Define whether conditions should be combined using "and" (all must match) or "or" (any match).

Behavior

The reject mutation only takes effect during query execution. For instance, scripts that return quickly might still see assets loading in the editor since rejections occur only while mutations are actively running.

The following example rejects image and media requests, helping save bandwidth:

- Rejecting Images and Media
- Rejecting Media from a Specific Domain

```codeBlockLines_p187
mutation RejectImages {
  reject(type: [image, media]) {
    enabled
    time
  }
  goto(url: "https://cnn.com", waitUntil: firstContentfulPaint) {
    status
    time
  }
}

```

To reject media requests originating from the `google.com` domain, use the `and` operator:

```codeBlockLines_p187
mutation Reject {
  reject(
    operator: and
    type: image
    url: "*google.com*"
  ) {
    enabled
    time
  }
  goto(url: "https://cnn.com", waitUntil: firstContentfulPaint) {
    status
    time
  }
}

```

## External Proxies [​](https://docs.browserless.io/browserql/bot-detection/proxies\#external-proxies "Direct link to External Proxies")

Alongside the Browserless residential proxy, you can also use an external proxy as well. This is done via the `proxy` mutation, which takes several options with regards to how and when to proxy.

The first requirement is to specify the server's URI to proxy through. This takes the format of `${protocol}://${username}:${password}@${host}:${port}`. For instance, if you have a username of `john` and a password of `1337code` and a URL of `myproxy.com` and a port of `1234`, the server argument would look like: `http://john:1337@myproxy.com:1234`. If you don't have a username or password you can simply omit those fields in the URI. Most proxy servers will also have simple generation widgets that can help build these URI's out for you.

Here's the full snippet in BrowserQL:

```codeBlockLines_p187
mutation ExternalProxy {
  # Proxy to this server for all requests
  proxy(server: "http://john:1337@myproxy.com:1234" url: "*") {
    time
  }
  goto(url: "https://nordvpn.com/what-is-my-ip/", waitUntil: load) {
    status
  }
  waitForTimeout(time: 5000) {
    time
  }
}

```

The second important part of the `proxy` mutation is deciding which requests need to be proxied. BrowserQL supports this by allowing you make patterns of the type of requests you'd like to proxy. You can proxy based upon URL pattern, request methods, and even request types. To proxy _all_ requests, simply use `url: "*"` which will match all requests being sent by BrowserQL.

If you want to proxy only the Document requests (typically what most pages are), then you'd set the `type: document` for this. Here's an example of proxying for Document and XHR requests:

```codeBlockLines_p187
mutation ProxyDocumentAndXHR {
  proxy(server: "http://john:1337@myproxy.com:1234" type: [document, xhr]) {
    time
  }
  goto(url: "https://nordvpn.com/what-is-my-ip/", waitUntil: load) {
    status
  }
  waitForTimeout(time: 5000) {
    time
  }
}

```

Finally, you can mix and match proxies as well with this API. The first proxy that matches the request will be the chosen proxy for that request, so ordering can be important if you want to mix and match proxies for various types of requests.

For instance, you can proxy `document` and `xhr` requests through a residential proxy querying that first, and all other requests through a data-center proxy. Here's how that'd look by specifying the residential proxy _first_, then matching all others via the greedy `url: "*"` pattern:

```codeBlockLines_p187
mutation ProxyDocumentAndXHR {
  # Proxy document and xhr through residential
  residential: proxy(server: "http://john:1337@residential.proxy.com:1234" type: [document, xhr]) {
    time
  }
  # Proxy all else through datacenter
  datacenter: proxy(server: "http://john:1337@datacenter.proxy.com:1234" url: "*") {
    time
  }
  goto(url: "https://nordvpn.com/what-is-my-ip/", waitUntil: load) {
    status
  }
  waitForTimeout(time: 5000) {
    time
  }
}

```

- [Built-In Proxies](https://docs.browserless.io/browserql/bot-detection/proxies#built-in-proxies)
  - [How to Enable Built-In Proxies](https://docs.browserless.io/browserql/bot-detection/proxies#how-to-enable-built-in-proxies)
  - [Optimizing Proxy Usage with the Reject Mutation](https://docs.browserless.io/browserql/bot-detection/proxies#optimizing-proxy-usage-with-the-reject-mutation)
- [External Proxies](https://docs.browserless.io/browserql/bot-detection/proxies#external-proxies)