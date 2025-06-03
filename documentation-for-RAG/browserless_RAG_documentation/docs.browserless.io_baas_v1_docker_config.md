---
url: "https://docs.browserless.io/baas/v1/docker/config"
title: "Docker Configuration | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/docker/config#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/enterprise/docker/configuration) or [BrowserQL](https://docs.browserless.io/browserql/start).

### All Options [​](https://docs.browserless.io/baas/v1/docker/config\#all-options "Direct link to All Options")

- [Chrome information](https://docs.browserless.io/baas/v1/docker/config#chrome-information)
- [Port](https://docs.browserless.io/baas/v1/docker/config#port)
- [Max Concurrent Sessions](https://docs.browserless.io/baas/v1/docker/config#max-concurrent-sessions)
- [Connection Timeout](https://docs.browserless.io/baas/v1/docker/config#connection-timeout)
- [Max Queue Length](https://docs.browserless.io/baas/v1/docker/config#max-queue-length)
- [Pre-booting Chrome](https://docs.browserless.io/baas/v1/docker/config#pre-booting-chrome)
- [Pre-boot quantity](https://docs.browserless.io/baas/v1/docker/config#pre-boot-quantity)
- [Demo Mode](https://docs.browserless.io/baas/v1/docker/config#demo-mode)
- [Defining a host bind](https://docs.browserless.io/baas/v1/docker/config#defining-a-host-bind)
- [Defining a workspace location](https://docs.browserless.io/baas/v1/docker/config#defining-a-workspace-location)
- [Deleting workspace files automatically](https://docs.browserless.io/baas/v1/docker/config#deleting-workspace-files-automatically)
- [Defining a time to delete workspace files](https://docs.browserless.io/baas/v1/docker/config#defining-a-time-to-delete-workspace-files)
- [Disable the Debugger](https://docs.browserless.io/baas/v1/docker/config#disabling-the-debugger)
- [Disable download behavior](https://docs.browserless.io/baas/v1/docker/config#disable-download-behavior)
- [Securing your Instance](https://docs.browserless.io/baas/v1/docker/config#securing-your-instance)
- [Logging](https://docs.browserless.io/baas/v1/docker/config#logging)
- [Enable CORS](https://docs.browserless.io/baas/v1/docker/config#enable-cors)
- [Enable XVFB](https://docs.browserless.io/baas/v1/docker/config#enable-xvfb)
- [Exit on health failure](https://docs.browserless.io/baas/v1/docker/config#exit-on-health-failure)
- [Persisting Metrics](https://docs.browserless.io/baas/v1/docker/config#persisting-metrics)
- [Exposing Built-in Modules for `/function`](https://docs.browserless.io/baas/v1/docker/config#exposing-built-in-modules-to-function)
- [Exposing External Modules for `/function`](https://docs.browserless.io/baas/v1/docker/config#exposing-external-modules-to-function)
- [Keeping Chrome Alive](https://docs.browserless.io/baas/v1/docker/config#keeping-chrome-alive)
- [Chrome Refresh Time](https://docs.browserless.io/baas/v1/docker/config#chrome-refresh-time)
- [Single Run mode](https://docs.browserless.io/baas/v1/docker/config#single-run-mode)
- [Default Block Ads](https://docs.browserless.io/baas/v1/docker/config#default-block-ads)
- [Default Headless](https://docs.browserless.io/baas/v1/docker/config#default-headless)
- [Default Launch Args](https://docs.browserless.io/baas/v1/docker/config#default-launch-args)
- [Default Ignore Default Args](https://docs.browserless.io/baas/v1/docker/config#default-ignore-default-args)
- [Default Ignore HTTPS](https://docs.browserless.io/baas/v1/docker/config#default-ignore-https)
- [Default User Data Dir](https://docs.browserless.io/baas/v1/docker/config#default-user-data-dir)
- [Disabling Routes](https://docs.browserless.io/baas/v1/docker/config#disable-routes)
- [Enable API GET Calls](https://docs.browserless.io/baas/v1/docker/config#enable-api-get)
- [Function Incognito Mode](https://docs.browserless.io/baas/v1/docker/config#function-incognito-mode)
- [Pre-boot Chrome](https://docs.browserless.io/baas/v1/docker/config#pre-booting-chrome)
- [Using a proxy](https://docs.browserless.io/baas/v1/docker/config#using-a-proxy)

The browserless docker container is highly-configurable, and accepts parameters through environment variables when starting. You can set parameters such as port, connection-timeout, queueing and more. Below is a description of each parameter, what they mean, and what they default to.

## Chrome information [​](https://docs.browserless.io/baas/v1/docker/config\#chrome-information "Direct link to Chrome information")

Browserless automatically builds labels with each release regarding important information like the current browser version, the version of puppeteer that's supported, and even the debugger version protocol. You can access this information by running the command below:

```codeBlockLines_p187
$ docker inspect browserless/chrome

```

## Port [​](https://docs.browserless.io/baas/v1/docker/config\#port "Direct link to Port")

By default browserless listens on port `3000`. You can configure this in docker by using it's port mapping functionality. As an example, let's say you want to have it listen port `8080`, you would run it like so:

```codeBlockLines_p187
$ docker run -p 8080:3000 --restart always -d --name browserless browserless/chrome

```

This should allow you some flexibility in how to run the image.

## Max Concurrent Sessions [​](https://docs.browserless.io/baas/v1/docker/config\#max-concurrent-sessions "Direct link to Max Concurrent Sessions")

Since running Chrome can be rather resource intensive you'll probably want to limit the number of concurrent sessions. This is, by default, set to 5 when not specified. Once the limit is reached then queueing begins to take place and requests will wait until more workers are ready.

To set this to a different number, say 10, issue your run like so:

```codeBlockLines_p187
$ docker run -e "MAX_CONCURRENT_SESSIONS=10" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

It's best to keep this limit small and grow it over time as it's easy to starve resources when running on restricted hardware.

## Connection Timeout [​](https://docs.browserless.io/baas/v1/docker/config\#connection-timeout "Direct link to Connection Timeout")

Connection timeout is a parameter that sets how long any session can run for. This is in place to prevent scripts that don't cleanup properly, or run into errors tha cause them to hang. The value of which can be set in milliseconds, and defaults to `30000`, or 30 seconds.

To allow more time for sessions, simply change it by setting `CONNECTION_TIMEOUT` when running.

> You can opt-out of timers by setting this value to `-1` for _no_ session timer. Be sure to close connections when not in use!

```codeBlockLines_p187
$ docker run -e "CONNECTION_TIMEOUT=60000" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Max Queue Length [​](https://docs.browserless.io/baas/v1/docker/config\#max-queue-length "Direct link to Max Queue Length")

This value determines how many items in the queue are allowed before requests are issued a `429` response code and closed. This mechanism is in place to prevent consumers from accidentally (or purposefully) triggering a denial-of-service. By default the image only allows a queue of 5 requests before beginning to fail more. As an example, if you have a `MAX_CONCURRENT_SESSIONS` of 5 and a `MAX_QUEUE_LENGTH` of 5, then 10 concurrent connections are allowed (5 running then 5 pending).

To adjust this value, simply set it via `MAX_QUEUE_LENGTH`.

```codeBlockLines_p187
$ docker run -e "MAX_QUEUE_LENGTH=10" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Pre-booting Chrome [​](https://docs.browserless.io/baas/v1/docker/config\#pre-booting-chrome "Direct link to Pre-booting Chrome")

> Prebooting is an experimental feature, and its usage is generally discouraged if your workers don't have a lot of resources or if you are going to perform resource-intensive tasks (PDF rendering, scrapping JS-heavy webpages, screenshotting).

You can, optionally, pre-boot Chrome and keep it in a pool of instances in order to cut-down on the boot time. To enable this, run your docker command as you normally would plus the `PREBOOT_CHROME=true` flag. Unless specified otherwise using `PREBOOT_QUANTITY`, `PREBOOT_CHROME` will create a swarm of browsers of lenght `MAX_CONCURRENT_SESSIONS`.

```codeBlockLines_p187
$ docker run -e "PREBOOT_CHROME=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Pre-boot quantity [​](https://docs.browserless.io/baas/v1/docker/config\#pre-boot-quantity "Direct link to Pre-boot quantity")

> Prebooting is an experimental feature, and its usage is generally discouraged if your workers don't have a lot of resources or if you are going to perform resource-intensive tasks (PDF rendering, scrapping JS-heavy webpages, screenshotting).

By default, prebooting will create a swarm of browsers of lenght `MAX_CONCURRENT_SESSIONS`. `PREBOOT_QUANTITY` allows better resource management by setting the number of pre-booted and always-open browser instances. This can be useful if your browserless instance has a large ceiling for concurrent connections but doesn't need as many always-open browsers.

If `PREBOOT_QUANTITY` gets evaluated as `0`, browserless is going to use `MAX_CONCURRENT_SESSIONS` instead.

```codeBlockLines_p187
$ docker run -e "PREBOOT_CHROME=true" -e "PREBOOT_QUANTITY=5" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Demo Mode [​](https://docs.browserless.io/baas/v1/docker/config\#demo-mode "Direct link to Demo Mode")

If you want to serve the interactive debugger, but not allow it to handle `puppeteer.connect` calls, you can do so via the `DEMO_MODE` flag.

```codeBlockLines_p187
$ docker run -e "DEMO_MODE=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Defining a host bind [​](https://docs.browserless.io/baas/v1/docker/config\#defining-a-host-bind "Direct link to Defining a host bind")

browserless will, by default, bind to localhost when no host is provided. If you want to bind to another IP, or domain, then pass in a `HOST` variable to do so.

```codeBlockLines_p187
$ docker run -e "HOST=192.168.1.1" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Defining a workspace location [​](https://docs.browserless.io/baas/v1/docker/config\#defining-a-workspace-location "Direct link to Defining a workspace location")

Browserless automatically has downloads from Chromium set to the `/tmp` directory inside the docker image. To change this, simply set the `WORKSPACE_DIR`:

```codeBlockLines_p187
$ docker run -e "WORKSPACE_DIR=~/downloads" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Deleting workspace files automatically [​](https://docs.browserless.io/baas/v1/docker/config\#deleting-workspace-files-automatically "Direct link to Deleting workspace files automatically")

When downloads from Chrome are larger, it's easy for the docker image to fill it's disk-space if you forget to periodically delete files. browserless has a mechanism to do so with `WORKSPACE_DELETE_EXPIRED`:

```codeBlockLines_p187
$ docker run -e "WORKSPACE_DELETE_EXPIRED=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

This will have browserless delete files older than 30 days in the workspace, checking once a day. To change the length, simply set `WORKSPACE_EXPIRE_DAYS`.

## Defining a time to delete workspace files [​](https://docs.browserless.io/baas/v1/docker/config\#defining-a-time-to-delete-workspace-files "Direct link to Defining a time to delete workspace files")

When `WORKSPACE_DELETE_EXPIRED` is `true`, browserless attempts to delete files older than 30 days in the workspace directory. To change this to something else, set a `WORKSPACE_EXPIRE_DAYS`:

```codeBlockLines_p187
$ docker run -e "WORKSPACE_DELETE_EXPIRED=true" -e "WORKSPACE_EXPIRE_DAYS=7" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

The example above will delete files older than 7 days.

## Disabling the debugger [​](https://docs.browserless.io/baas/v1/docker/config\#disabling-the-debugger "Direct link to Disabling the debugger")

If you want to disable the debugger (and all accompnaying HTML) you can set the `ENABLE_DEBUGGER` to `false` to only allow `puppeteer.connect` calls to succeed.

```codeBlockLines_p187
$ docker run -e "ENABLE_DEBUGGER=false" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Disable download behavior [​](https://docs.browserless.io/baas/v1/docker/config\#disable-download-behavior "Direct link to Disable download behavior")

By default, browserless tells chromium to use a special directory in `/tmp` for storing files. If you want opt-out of this behavior, start the docker image with this flag:

```codeBlockLines_p187
$ docker run -e "DISABLE_AUTO_SET_DOWNLOAD_BEHAVIOR=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Securing your instance [​](https://docs.browserless.io/baas/v1/docker/config\#securing-your-instance "Direct link to Securing your instance")

If you're exposing your instance to the world, but don't want anyone to use it, you can optionally apply a `TOKEN` param that will restrict calls without a `token` query-string parameter. When present, browserless will reject any calls that don't have a matching token.

```codeBlockLines_p187
$ docker run -e "TOKEN=2cbc5771-38f2-4dcf-8774-50ad51a971b8" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

Then, in your application use a query-parameter to pass that token in.

```codeBlockLines_p187
const browser = await puppeteer.connect({
  browserWSEndpoint: 'ws://localhost:3000?token=2cbc5771-38f2-4dcf-8774-50ad51a971b8',
});

```

## Logging [​](https://docs.browserless.io/baas/v1/docker/config\#logging "Direct link to Logging")

Browserless uses the `debug` npm package to log output. By default, browserless prints a minimal set of logs regarding sessions and other performance characteristics. To turn it off, simply set the DEBUG value to nothing:

```codeBlockLines_p187
$ docker run -e "DEBUG=-*" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

Since most other npm packages use this same module, you can set this flag to a wildcard `*` to see nearly everything that's happening internally:

NOTE: Be careful running with this command as you'll generate a lot of log output.

```codeBlockLines_p187
$ docker run -e "DEBUG=*" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Enable CORS [​](https://docs.browserless.io/baas/v1/docker/config\#enable-cors "Direct link to Enable CORS")

You can enable cross-origin-resource-sharing with browserless by setting the `ENABLE_CORS=true` variable. This defaults to `false`:

```codeBlockLines_p187
$ docker run -e "ENABLE_CORS=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Enable XVFB [​](https://docs.browserless.io/baas/v1/docker/config\#enable-xvfb "Direct link to Enable XVFB")

By default browserless will take care of XVFB running automatically, which essentially means this is defaulted to `true`. However, in some hosting environments it's not possible to write to the appropriate folders to support XVFB and you should set this parameter to `false`.

> The screencast API depends on this setting to be `true` and will fail when turned off.

```codeBlockLines_p187
$ docker run -e "ENABLE_XVBF=false" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Exit on health failure [​](https://docs.browserless.io/baas/v1/docker/config\#exit-on-health-failure "Direct link to Exit on health failure")

browserless routinely checks on the health of the image as it's running. Sometimes it's helpful to have it restart automatically when CPU or Memory usage are above 100% for a period of time (by default 5 minutes). In order for browserless to restart on health-failure checks, you'll have to set a parameter of `EXIT_ON_HEALTH_FAILURE=true`.

```codeBlockLines_p187
$ docker run -e "EXIT_ON_HEALTH_FAILURE=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Persisting Metrics [​](https://docs.browserless.io/baas/v1/docker/config\#persisting-metrics "Direct link to Persisting Metrics")

browserless captures metrics while it's running, and exposes them via the `/metrics` endpoint. These, by default, don't persist anywhere _unless_ you tell browserless where to persist them. When provided, the docker image will also attempt to read the metrics on startup and write to it periodically during execution.

> In this run command we're mounting the machines `/root` path so that the docker can access it at `/root`, be sure to change this to fit your use-case.

```codeBlockLines_p187
$ docker run -e "METRICS_JSON_PATH=/root/metrics.json" -v /root:/root -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Exposing built-in modules to `/function` [​](https://docs.browserless.io/baas/v1/docker/config\#exposing-built-in-modules-to-function "Direct link to exposing-built-in-modules-to-function")

The `/function` endpoint allows for user-submitted code to be ran inside the docker-image without the need for another compilation step. By default functions are _not_ allowed to require modules (both built-in's or externally). To enable Node's built-in modules you'll need to supply an array of modules available.

Here we're allowing both the `url` and `util` modules.

```codeBlockLines_p187
$ docker run -e "FUNCTION_BUILT_INS=[\"url\", \"util\"]" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Exposing external modules to `/function` [​](https://docs.browserless.io/baas/v1/docker/config\#exposing-external-modules-to-function "Direct link to exposing-external-modules-to-function")

The `/function` endpoint allows for user-submitted code to be ran inside the docker-image without the need for another compilation step. By default functions are _not_ allowed to require modules (both built-in's or externally). To enable external modules you'll need to supply an array of modules available.

Here we're allowing both the `request` and `fetch` modules to be required in the `/function` endpoint.

```codeBlockLines_p187
$ docker run -e "FUNCTION_EXTERNALS=[\"request\", \"fetch\"]" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Keeping Chrome Alive [​](https://docs.browserless.io/baas/v1/docker/config\#keeping-chrome-alive "Direct link to Keeping Chrome Alive")

When the `PREBOOT_CHROME` flag is set, you can optionally keep Chrome "alive" after sessions are complete. This allows you to re-use Chrome instances without having to start and stop them (making for much faster execution). To enable this behavior, set the `PREBOOT_CHROME=true` and `KEEP_ALIVE=true`.

Browserless will close Chrome after 30 minutes to try and mitigate issues with Chrome consuming too many resources. This is configurable as well with the `CHROME_REFRESH_TIME` flag.

> When using KEEP\_ALIVE Chrome will retain information about prior-sessions such as cookies and login contexts. **You'll also need to replace `browser.close()` with `browser.disconnect()` in your puppeteer code.**

```codeBlockLines_p187
$ docker run -e "PREBOOT_CHROME=true" -e "KEEP_ALIVE=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Chrome Refresh Time [​](https://docs.browserless.io/baas/v1/docker/config\#chrome-refresh-time "Direct link to Chrome Refresh Time")

When both `PREBOOT_CHROME` and `KEEP_ALIVE` are `true` browserless keeps track of how long Chrome has been running, and will attempt to close it after a certain period. By default it will try and restart Chrome after 30 minutes. You can configure this behavior with the `CHROME_REFRESH_TIME` flag.

The `CHROME_REFRESH_TIME` flag accepts a value in milliseconds to keep Chrome running before it attempts to close it. Below we set this threshold to one hour.

```codeBlockLines_p187
$ docker run -e "PREBOOT_CHROME=true" -e "KEEP_ALIVE=true" -e "CHROME_REFRESH_TIME=3600000" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Single Run Mode [​](https://docs.browserless.io/baas/v1/docker/config\#single-run-mode "Direct link to Single Run Mode")

Some cloud providers offer a way to run a docker images as a "function", wherein the container is shutdown after all open connections are terminated. In order to make this as seamless as an experience as possible, there's an option call `SINGLE_RUN` which will shutdown the container after a single session completes.

> It's recommended to set MAX\_CONCURRENT\_SESSIONS to 1 and QUEUE\_LENGTH to 0 if you want to run just a single session

```codeBlockLines_p187
$ docker run -e "SINGLE_RUN=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Default Block Ads [​](https://docs.browserless.io/baas/v1/docker/config\#default-block-ads "Direct link to Default Block Ads")

Starts all sessions with the ad-blocker already running (no need to use `?blockAds=true` in your API or puppeteer connect calls). If a session with `?blockAds=false` is started, that preference will take precedence, and the ad-blocker will be turned off.

```codeBlockLines_p187
$ docker run -e "DEFAULT_BLOCK_ADS=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Default Headless [​](https://docs.browserless.io/baas/v1/docker/config\#default-headless "Direct link to Default Headless")

Starts all sessions, that don't include a `?headless` flag in their API or connect call, with a pre-set headless behavior. When not set, browserless sets all sessions to be headless by default.

If a session starts with a different `?headless` flag, that flag will take precedence over the pre-configured behavior.

```codeBlockLines_p187
$ docker run -e "DEFAULT_HEADLESS=false" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Default Launch Args [​](https://docs.browserless.io/baas/v1/docker/config\#default-launch-args "Direct link to Default Launch Args")

Allows for setting default launch args when none are present in an API or puppeteer.connect call. When a call is started with launch-arguments set, they take precedence over this default behavior.

```codeBlockLines_p187
$ docker run -e "DEFAULT_LAUNCH_ARGS=[\"--window-size=1920,1080\"]" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Default Ignore HTTPS [​](https://docs.browserless.io/baas/v1/docker/config\#default-ignore-https "Direct link to Default Ignore HTTPS")

Tells browserless to, by default, ignore or not ignore HTTPS errors on sites. If a sesions or API call comes starts with a different preference set, then it will override this default behavior.

```codeBlockLines_p187
$ docker run -e "DEFAULT_IGNORE_HTTPS_ERRORS=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Default Ignore Default Args [​](https://docs.browserless.io/baas/v1/docker/config\#default-ignore-default-args "Direct link to Default Ignore Default Args")

When set this will override any default arguments set by browserless to Chrome's launch arguments. This can be a list of flags to ignore, or `true`/ `false` to ignore all arguments. When a session is started with this flag set, it takes precedence over this default behavior.

```codeBlockLines_p187
$ docker run -e "DEFAULT_IGNORE_DEFAULT_ARGS=true" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Default User Data Dir [​](https://docs.browserless.io/baas/v1/docker/config\#default-user-data-dir "Direct link to Default User Data Dir")

Sets a default directory to cache user data to (cookies, local-storage and more). This will force all sessions to use the same cache unless sessions themselves specify another path, which will override this behavior.

```codeBlockLines_p187
$ docker run -e "DEFAULT_USER_DATA_DIR=/tmp/my-profile" -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Disable Routes [​](https://docs.browserless.io/baas/v1/docker/config\#disable-routes "Direct link to Disable Routes")

Allows for disabling routes by supplying a list of routes to disable:

```codeBlockLines_p187
$ docker run -e 'DISABLED_FEATURES=["pdfEndpoint", "contentEndpoint"]' -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Enable API GET [​](https://docs.browserless.io/baas/v1/docker/config\#enable-api-get "Direct link to Enable API GET")

Allows for enabling an expiremental GET-style operation, as opposed to POSTing bodies of code to run on our APIs. When enabled, you'll simply need to set a `body` query-string parameter, with a URL-encoded JSON string of the normal API body.

```codeBlockLines_p187
$ docker run -e 'ENABLE_API_GET=true' -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Function Incognito Mode [​](https://docs.browserless.io/baas/v1/docker/config\#function-incognito-mode "Direct link to Function Incognito Mode")

When set, and `PREBOOT_CHROME` and `KEEP_ALIVE` are set, allows for generating a fresh page (incognito page) from a re-used browser. This is useful if you want to reuse a Chrome instance, but don't want to retain the cookies and other browser caches.

```codeBlockLines_p187
$ docker run -e FUNCTION_ENABLE_INCOGNITO_MODE=true -e KEEP_ALIVE=true -e PREBOOT_CHROME=true -p 3000:3000 --restart always -d --name browserless browserless/chrome

```

## Using a proxy [​](https://docs.browserless.io/baas/v1/docker/config\#using-a-proxy "Direct link to Using a proxy")

You'll often want to use a load-balancer, or reverse proxy, in front of browserless for SSL termination or to load balance across a fleet of browserless instances. In certain cases, browserless does generate links (like in the /sessions API), in which case this link builder needs to be aware of how it should route sessions.

In order to handle this, you can specify three parameters: `PROXY_HOST`, `PROXY_PORT` and `PROXY_SSL` to browserless. This will tell certain APIs to generate links with the prior information.

```codeBlockLines_p187
$ docker run -e "PROXY_HOST=browserless.my-domain.com" -e PROXY_PORT=443 -e PROXY_SSL=true -p 3000:3000 --restart always -d --name browserless browserless/chrome

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

- [All Options](https://docs.browserless.io/baas/v1/docker/config#all-options)
- [Chrome information](https://docs.browserless.io/baas/v1/docker/config#chrome-information)
- [Port](https://docs.browserless.io/baas/v1/docker/config#port)
- [Max Concurrent Sessions](https://docs.browserless.io/baas/v1/docker/config#max-concurrent-sessions)
- [Connection Timeout](https://docs.browserless.io/baas/v1/docker/config#connection-timeout)
- [Max Queue Length](https://docs.browserless.io/baas/v1/docker/config#max-queue-length)
- [Pre-booting Chrome](https://docs.browserless.io/baas/v1/docker/config#pre-booting-chrome)
- [Pre-boot quantity](https://docs.browserless.io/baas/v1/docker/config#pre-boot-quantity)
- [Demo Mode](https://docs.browserless.io/baas/v1/docker/config#demo-mode)
- [Defining a host bind](https://docs.browserless.io/baas/v1/docker/config#defining-a-host-bind)
- [Defining a workspace location](https://docs.browserless.io/baas/v1/docker/config#defining-a-workspace-location)
- [Deleting workspace files automatically](https://docs.browserless.io/baas/v1/docker/config#deleting-workspace-files-automatically)
- [Defining a time to delete workspace files](https://docs.browserless.io/baas/v1/docker/config#defining-a-time-to-delete-workspace-files)
- [Disabling the debugger](https://docs.browserless.io/baas/v1/docker/config#disabling-the-debugger)
- [Disable download behavior](https://docs.browserless.io/baas/v1/docker/config#disable-download-behavior)
- [Securing your instance](https://docs.browserless.io/baas/v1/docker/config#securing-your-instance)
- [Logging](https://docs.browserless.io/baas/v1/docker/config#logging)
- [Enable CORS](https://docs.browserless.io/baas/v1/docker/config#enable-cors)
- [Enable XVFB](https://docs.browserless.io/baas/v1/docker/config#enable-xvfb)
- [Exit on health failure](https://docs.browserless.io/baas/v1/docker/config#exit-on-health-failure)
- [Persisting Metrics](https://docs.browserless.io/baas/v1/docker/config#persisting-metrics)
- [Exposing built-in modules to `/function`](https://docs.browserless.io/baas/v1/docker/config#exposing-built-in-modules-to-function)
- [Exposing external modules to `/function`](https://docs.browserless.io/baas/v1/docker/config#exposing-external-modules-to-function)
- [Keeping Chrome Alive](https://docs.browserless.io/baas/v1/docker/config#keeping-chrome-alive)
- [Chrome Refresh Time](https://docs.browserless.io/baas/v1/docker/config#chrome-refresh-time)
- [Single Run Mode](https://docs.browserless.io/baas/v1/docker/config#single-run-mode)
- [Default Block Ads](https://docs.browserless.io/baas/v1/docker/config#default-block-ads)
- [Default Headless](https://docs.browserless.io/baas/v1/docker/config#default-headless)
- [Default Launch Args](https://docs.browserless.io/baas/v1/docker/config#default-launch-args)
- [Default Ignore HTTPS](https://docs.browserless.io/baas/v1/docker/config#default-ignore-https)
- [Default Ignore Default Args](https://docs.browserless.io/baas/v1/docker/config#default-ignore-default-args)
- [Default User Data Dir](https://docs.browserless.io/baas/v1/docker/config#default-user-data-dir)
- [Disable Routes](https://docs.browserless.io/baas/v1/docker/config#disable-routes)
- [Enable API GET](https://docs.browserless.io/baas/v1/docker/config#enable-api-get)
- [Function Incognito Mode](https://docs.browserless.io/baas/v1/docker/config#function-incognito-mode)
- [Using a proxy](https://docs.browserless.io/baas/v1/docker/config#using-a-proxy)