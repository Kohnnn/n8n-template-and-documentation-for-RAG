---
url: "https://docs.browserless.io/bql-schema/operations/mutations/proxy"
title: "proxy | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/bql-schema/operations/mutations/proxy#__docusaurus_skipToContent_fallback)

On this page

Proxies requests, by a specified set of conditions, through either the Browserless residential proxy or through an external proxy. Only requests that match these conditions are proxied and the rest are sent from the instance's own IP address.

Use the "server" argument to specify an external proxy for Browserless to use for requests. For requests with authentication, the username and password should be included in the URL using Basic Authentication. See the examples below for more information on how to format those URLs.

**Using the browserless proxy for all requests and proxy through Brazil**

```codeBlockLines_p187
proxy(
  url: "*"
  country: BR
) {
  time
}

```

**Using an external proxy for all requests**

```codeBlockLines_p187
proxy(
  url: "*"
  server: "http://username:password@my-proxy.com:12321"
) {
  time
}

```

**Using the Browserless proxy for only document requests and proxying through France**

```codeBlockLines_p187
proxy(
  url: "*"
  type: document
  country: FR
) {
  time
}

```

```codeBlockLines_p187
proxy(
  country: CountryType
  city: String
  state: String
  sticky: Boolean
  server: String
  method: [Method]
  operator: OperatorTypes = or
  type: [ResourceType]
  url: [String]
): ProxyResponse

```

### Arguments [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#arguments "Direct link to Arguments")

#### [`proxy.country`](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#) ● [`CountryType`](https://docs.browserless.io/bql-schema/types/enums/country-type) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxycountrycountrytype- "Direct link to proxycountrycountrytype-")

The country you wish to proxy through. Only allowed when using the browserless.io proxy and no `server` argument.

#### [`proxy.city`](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxycitystring- "Direct link to proxycitystring-")

The city you wish to proxy through. Any spaces should be removed and all casing lowercase. For instance, "New York City" should be "newyorkcity"

#### [`proxy.state`](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxystatestring- "Direct link to proxystatestring-")

The state or provence you wish to proxy through. Any spaces should be removed and all casing lowercase. For instance, "Rhode Island" would be "rhodeisland" and "New Brunswick" would be "newbrunswick"

#### [`proxy.sticky`](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#) ● [`Boolean`](https://docs.browserless.io/bql-schema/types/scalars/boolean) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxystickyboolean- "Direct link to proxystickyboolean-")

Whether or not you want the same IP to be used for subsequent requests matching the pattern

#### [`proxy.server`](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#) ● [`String`](https://docs.browserless.io/bql-schema/types/scalars/string) scalar [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxyserverstring- "Direct link to proxyserverstring-")

An external proxy to use for these requests matching the specified patterns set in the other arguments. When this is set then `country`, `city`, `state` and `sticky` options will throw errors as these are only valid for the browserless.io proxy network

#### [`proxy.method`](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#) ● [`[Method]`](https://docs.browserless.io/bql-schema/types/enums/method) listenum [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxymethodmethod-- "Direct link to proxymethodmethod--")

The Method(s) of the request you'd like to proxy

#### [`proxy.operator`](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#) ● [`OperatorTypes`](https://docs.browserless.io/bql-schema/types/enums/operator-types) enum [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxyoperatoroperatortypes- "Direct link to proxyoperatoroperatortypes-")

Whether to "or" conditions together, meaning any condition that matches will be proxied, or "and" them together meaning every condition must match to proxy the request.

#### [`proxy.type`](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#) ● [`[ResourceType]`](https://docs.browserless.io/bql-schema/types/enums/resource-type) listenum [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxytyperesourcetype-- "Direct link to proxytyperesourcetype--")

The content-type of the request you'd like to proxy requests to

#### [`proxy.url`](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#) ● [`[String]`](https://docs.browserless.io/bql-schema/types/scalars/string) listscalar [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxyurlstring-- "Direct link to proxyurlstring--")

A glob-style URL pattern to match requests, and if matched, are proxied through

### Type [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#type "Direct link to Type")

#### [`ProxyResponse`](https://docs.browserless.io/bql-schema/types/objects/proxy-response) object [​](https://docs.browserless.io/bql-schema/operations/mutations/proxy\#proxyresponse- "Direct link to proxyresponse-")

Response returned after setting up the proxy patterns

- [Arguments](https://docs.browserless.io/bql-schema/operations/mutations/proxy#arguments)
- [Type](https://docs.browserless.io/bql-schema/operations/mutations/proxy#type)