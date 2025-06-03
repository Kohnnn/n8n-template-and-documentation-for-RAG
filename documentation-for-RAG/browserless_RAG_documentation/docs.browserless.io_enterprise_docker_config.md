---
url: "https://docs.browserless.io/enterprise/docker/config"
title: "Docker Configuration | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/enterprise/docker/config#__docusaurus_skipToContent_fallback)

On this page

The browserless docker container is highly-configurable, and accepts parameters through environment variables when starting. You can set parameters such as port, connection-timeout, queueing and more. Below is a description of each parameter, what they mean, and what they default to.

## Token [​](https://docs.browserless.io/enterprise/docker/config\#token "Direct link to Token")

Browserless is designed to **always** require a token. This means that, if you don't pass a `TOKEN` env variable, **a randomly generated token will be set**. To set a token, you can pass it as env variable this way:

```codeBlockLines_p187
$ docker run -p 3000:3000 -e "TOKEN=6R0W53R135510" ghcr.io/browserless/chromium

```

## Port [​](https://docs.browserless.io/enterprise/docker/config\#port "Direct link to Port")

By default browserless listens on port `3000`. You can configure this in docker by using it's port mapping functionality. As an example, let's say you want to have it listen port `8080`, you would run it like so:

```codeBlockLines_p187
$ docker run -p 8080:3000 ghcr.io/browserless/chromium

```

This should allow you some flexibility in how to run the image.

## Max Concurrent Sessions [​](https://docs.browserless.io/enterprise/docker/config\#max-concurrent-sessions "Direct link to Max Concurrent Sessions")

Since running browsers can be rather resource intensive you'll probably want to limit the number of concurrent sessions. This is, by default, set to 5 when not specified. Once the limit is reached then queueing begins to take place and requests will wait until more workers are ready.

To set this to a different number, say 10, you need to pass the `CONCURRENT` env variable like so:

```codeBlockLines_p187
$ docker run -e "CONCURRENT=10" -p 3000:3000 ghcr.io/browserless/chromium

```

It's best to keep this limit small and grow it over time as it's easy to starve resources when running on restricted hardware.

## Connection Timeout [​](https://docs.browserless.io/enterprise/docker/config\#connection-timeout "Direct link to Connection Timeout")

`TIMEOUT` is a parameter that sets how long any session can run for. This is in place to prevent scripts that don't cleanup properly, or run into errors tha cause them to hang. The value of which can be set in milliseconds, and defaults to `30000`, or 30 seconds.

To allow more time for sessions, simply change it by setting `TIMEOUT` when running.

info

You can opt-out of timers by setting this value to `-1` for _no_ session timer. Be sure to close connections when not in use!

```codeBlockLines_p187
$ docker run -e "TIMEOUT=60000" -p 3000:3000 ghcr.io/browserless/chromium

```

## Max Queue Length [​](https://docs.browserless.io/enterprise/docker/config\#max-queue-length "Direct link to Max Queue Length")

This value determines how many items in the queue are allowed before requests are issued a `429` response code and closed. This mechanism is in place to prevent consumers from accidentally (or purposefully) triggering a denial-of-service. By default the image only allows a queue of 5 requests before beginning to fail more. As an example, if you have a `CONCURRENT` of 5 and a `QUEUED` of 5, then 10 concurrent connections are allowed (5 running then 5 pending).

To adjust this value, simply set it via `QUEUED`.

```codeBlockLines_p187
$ docker run -e "QUEUED=10" -p 3000:3000 ghcr.io/browserless/chromium

```

## Demo Mode [​](https://docs.browserless.io/enterprise/docker/config\#demo-mode "Direct link to Demo Mode")

## Defining a host bind [​](https://docs.browserless.io/enterprise/docker/config\#defining-a-host-bind "Direct link to Defining a host bind")

browserless will, by default, bind to localhost when no host is provided. If you want to bind to another IP, or domain, then pass in a `HOST` variable to do so.

```codeBlockLines_p187
$ docker run -e "HOST=192.168.1.1" -p 3000:3000 ghcr.io/browserless/chromium

```

## Logging [​](https://docs.browserless.io/enterprise/docker/config\#logging "Direct link to Logging")

Browserless uses the [`debug`](https://www.npmjs.com/package/debug) npm package to log output. By default, browserless prints a minimal set of logs regarding sessions and other performance characteristics. To turn it off, simply set the `DEBUG` value to nothing:

```codeBlockLines_p187
$ docker run -e "DEBUG=-*" -p 3000:3000 ghcr.io/browserless/chromium

```

Since most other npm packages use this same module, you can set this flag to a wildcard `*` to see nearly everything that's happening internally:

warning

Be careful running with this command as you'll generate a lot of log output.

```codeBlockLines_p187
$ docker run -e "DEBUG=*" -p 3000:3000 ghcr.io/browserless/chromium

```

## Enable CORS [​](https://docs.browserless.io/enterprise/docker/config\#enable-cors "Direct link to Enable CORS")

You can enable cross-origin-resource-sharing with browserless by setting the `CORS=true` variable. This defaults to `false`:

```codeBlockLines_p187
$ docker run -e "CORS=true" -p 3000:3000 ghcr.io/browserless/chromium

```

## Allow CORS methods [​](https://docs.browserless.io/enterprise/docker/config\#allow-cors-methods "Direct link to Allow CORS methods")

When `CORS=true`, by default, all `OPTIONS`, `POST`, and `GET` requests are allowed. To have more control over the methods, you can configure them using the `CORS_ALLOW_METHODS` env variable:

```codeBlockLines_p187
$ docker run \
  -e "CORS=true" \
  -e "CORS_ALLOW_METHODS=POST, DELETE" \
  -p 3000:3000 \
  ghcr.io/browserless/chromium

```

## Allow CORS origins [​](https://docs.browserless.io/enterprise/docker/config\#allow-cors-origins "Direct link to Allow CORS origins")

When `CORS=true`, by default, requests from **all** origins are allowed. To have more control over the origins, you can configure them using the `CORS_ALLOW_ORIGIN` env variable:

```codeBlockLines_p187
$ docker run \
  -e "CORS=true" \
  -e "CORS_ALLOW_ORIGIN=http://localhost" \
  -p 3000:3000 \
  ghcr.io/browserless/chromium

```

## Set CORS maximum cache age [​](https://docs.browserless.io/enterprise/docker/config\#set-cors-maximum-cache-age "Direct link to Set CORS maximum cache age")

When `CORS=true`, by default, CORS responses will have a maximum cache age of `2592000` s. To change this value, you can configure them using the `CORS_MAX_AGE` env variable:

```codeBlockLines_p187
$ docker run \
  -e "CORS=true" \
  -e "CORS_MAX_AGE=300" \
  -p 3000:3000 \
  ghcr.io/browserless/chromium

```

## Persisting Metrics [​](https://docs.browserless.io/enterprise/docker/config\#persisting-metrics "Direct link to Persisting Metrics")

browserless captures metrics while it's running, and exposes them via the `/metrics` endpoint. These, by default, don't persist anywhere _unless_ you tell browserless where to persist them. When provided, the docker image will also attempt to read the metrics on startup and write to it periodically during execution.

warning

In this run command we're mounting the machines `/root` path so that the docker can access it at `/root`, be sure to change this to fit your use-case

```codeBlockLines_p187
$ docker run -e "METRICS_JSON_PATH=/root/metrics.json" -v /root:/root -p 3000:3000 ghcr.io/browserless/chromium

```

## Default User Data Dir [​](https://docs.browserless.io/enterprise/docker/config\#default-user-data-dir "Direct link to Default User Data Dir")

Sets a default directory to cache user data to (cookies, local-storage and more). This will force all sessions to use the same cache unless sessions themselves specify another path, which will override this behavior.

```codeBlockLines_p187
$ docker run -e "DATA_DIR=/tmp/my-profile" -p 3000:3000 ghcr.io/browserless/chromium

```

## Default Downloads Dir [​](https://docs.browserless.io/enterprise/docker/config\#default-downloads-dir "Direct link to Default Downloads Dir")

Sets a default directory to store downloaded files. By default, downloads are stored inside a `browserless-download-dirs` dir inside the OS' temporary dir. To change this, you can use the `DOWNLOAD_DIR` env variable.

```codeBlockLines_p187
$ docker run -e "DOWNLOAD_DIR=/downloads" -p 3000:3000 ghcr.io/browserless/chromium

```

## Enable `GET` APIs [​](https://docs.browserless.io/enterprise/docker/config\#enable-get-apis "Direct link to enable-get-apis")

Allows for enabling HTTP `GET` operations, as opposed to `POST` ing bodies of code to run on our APIs. When enabled, you'll simply need to set a `body` query-string parameter, with a URL-encoded JSON string of the normal API body.

```codeBlockLines_p187
$ docker run -e 'ALLOW_GET=true' -p 3000:3000 ghcr.io/browserless/chromium

```

## Using a proxy [​](https://docs.browserless.io/enterprise/docker/config\#using-a-proxy "Direct link to Using a proxy")

You'll often want to use a load-balancer, or reverse proxy, in front of Browserless for SSL termination or to load balance across a fleet of Browserless instances. In certain cases, Browserless does generate links (like in the `/sessions` API), in which case this link builder needs to be aware of how it should route sessions.

In order to handle this, you can specify three parameters: `PROXY_HOST`, `PROXY_PORT` and `PROXY_SSL` to Browserless. This will tell certain APIs to generate links with the prior information.

```codeBlockLines_p187
$ docker run -e "PROXY_HOST=browserless.my-domain.com" -e PROXY_PORT=443 -e PROXY_SSL=true -p 3000:3000 ghcr.io/browserless/chromium

```

Then, /sessions API calls will return properly formatted JSON resposnes:

```codeBlockLines_p187
[\
  {\
    "description": "",\
    "devtoolsFrontendUrl": "/devtools/inspector.html?wss=browserless.my-domain.com:443/devtools/page/C6962B3428FC8E42CDA6484AB5B57EAC",\
    "id": "C6962B3428FC8E42CDA6484AB5B57EAC",\
    "title": "Example Domain",\
    "type": "page",\
    "url": "https://www.example.com/",\
    "webSocketDebuggerUrl": "wss://browserless.my-domain.com:443/devtools/page/C6962B3428FC8E42CDA6484AB5B57EAC",\
    "browserId": "b519351a-355e-47d5-82cc-7c240cfa40f3",\
    "browserWSEndpoint": "wss://browserless.my-domain.com:443/devtools/browser/b519351a-355e-47d5-82cc-7c240cfa40f3",\
    "port": "42169",\
    "trackingId": null\
  }\
]

```

## Allow `file://` protocol [​](https://docs.browserless.io/enterprise/docker/config\#allow-file-protocol "Direct link to allow-file-protocol")

By default, requests using the `file://` procotol are denied for security reasons. Set `ALLOW_FILE_PROTOCOL=true` in your env params to allow it:

```codeBlockLines_p187
$ docker run -e "ALLOW_FILE_PROTOCOL=true" -p 3000:3000 ghcr.io/browserless/chromium

```

## Check instance health before a session [​](https://docs.browserless.io/enterprise/docker/config\#check-instance-health-before-a-session "Direct link to Check instance health before a session")

You can use the `HEALTH` env variable to check CPU/Memory prior to running a session. If the instance's CPU/Memory are high on any inbound session (HTTP APIs, Puppeteer or Playwright), Browserless will respond with a `503` status code.

```codeBlockLines_p187
$ docker run -e 'HEALTH=true' -p 3000:3000 ghcr.io/browserless/chromium

```

## Setting the maximum memory for health checks [​](https://docs.browserless.io/enterprise/docker/config\#setting-the-maximum-memory-for-health-checks "Direct link to Setting the maximum memory for health checks")

If `HEALTH=true`, by default, it will allow requests as long memory usage is not over `99`. To set the threshold value, you canuse the `MAX_MEMORY_PERCENT` env variable:

```codeBlockLines_p187
$ docker run \
  -e 'HEALTH=true' \
  -e 'MAX_MEMORY_PERCENT=80' \
  -p 3000:3000 \
  ghcr.io/browserless/chromium

```

## Setting the maximum cpu for health checks [​](https://docs.browserless.io/enterprise/docker/config\#setting-the-maximum-cpu-for-health-checks "Direct link to Setting the maximum cpu for health checks")

If `HEALTH=true`, by default, it will allow requests as long cpu usage is not over `99`. To set the threshold value, you canuse the `MAX_CPU_PERCENT` env variable:

```codeBlockLines_p187
$ docker run \
  -e 'HEALTH=true' \
  -e 'MAX_CPU_PERCENT=80' \
  -p 3000:3000 \
  ghcr.io/browserless/chromium

```

- [Token](https://docs.browserless.io/enterprise/docker/config#token)
- [Port](https://docs.browserless.io/enterprise/docker/config#port)
- [Max Concurrent Sessions](https://docs.browserless.io/enterprise/docker/config#max-concurrent-sessions)
- [Connection Timeout](https://docs.browserless.io/enterprise/docker/config#connection-timeout)
- [Max Queue Length](https://docs.browserless.io/enterprise/docker/config#max-queue-length)
- [Demo Mode](https://docs.browserless.io/enterprise/docker/config#demo-mode)
- [Defining a host bind](https://docs.browserless.io/enterprise/docker/config#defining-a-host-bind)
- [Logging](https://docs.browserless.io/enterprise/docker/config#logging)
- [Enable CORS](https://docs.browserless.io/enterprise/docker/config#enable-cors)
- [Allow CORS methods](https://docs.browserless.io/enterprise/docker/config#allow-cors-methods)
- [Allow CORS origins](https://docs.browserless.io/enterprise/docker/config#allow-cors-origins)
- [Set CORS maximum cache age](https://docs.browserless.io/enterprise/docker/config#set-cors-maximum-cache-age)
- [Persisting Metrics](https://docs.browserless.io/enterprise/docker/config#persisting-metrics)
- [Default User Data Dir](https://docs.browserless.io/enterprise/docker/config#default-user-data-dir)
- [Default Downloads Dir](https://docs.browserless.io/enterprise/docker/config#default-downloads-dir)
- [Enable `GET` APIs](https://docs.browserless.io/enterprise/docker/config#enable-get-apis)
- [Using a proxy](https://docs.browserless.io/enterprise/docker/config#using-a-proxy)
- [Allow `file://` protocol](https://docs.browserless.io/enterprise/docker/config#allow-file-protocol)
- [Check instance health before a session](https://docs.browserless.io/enterprise/docker/config#check-instance-health-before-a-session)
- [Setting the maximum memory for health checks](https://docs.browserless.io/enterprise/docker/config#setting-the-maximum-memory-for-health-checks)
- [Setting the maximum cpu for health checks](https://docs.browserless.io/enterprise/docker/config#setting-the-maximum-cpu-for-health-checks)