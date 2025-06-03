---
url: "https://docs.browserless.io/baas/v1/hosted-service/worker-settings"
title: "Worker settings | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/enterprise/private-deployment/worker-settings) or [BrowserQL](https://docs.browserless.io/browserql/start).

info

This information applies for users that have Dedicated or Enterprise worker(s) in the capacity-based plan.

To customize your worker settings, log in to your [browserless account](https://cloud.browserless.io/account/) and click on the the gear icon in the Production Workers tab.
There are several settings that you can tweak for your dedicated workers in the popup that appears.

## Puppeteer version and global timeout [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#puppeteer-version-and-global-timeout "Direct link to Puppeteer version and global timeout")

The first two dropdown fields will allow you to pick the chrome/puppeteer version and the global timeout.

### Supported chrome/puppeteer versions [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#supported-chromepuppeteer-versions "Direct link to Supported chrome/puppeteer versions")

By default, you will have the latest version. If a newer version is released, we notify through email and your workers will update automatically the next time your workers are relaunched or restarted. If you want to pin your workers to a specific version, you'll have to select one of these versions from the dropdown.

### Global timeout [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#global-timeout "Direct link to Global timeout")

Once the duration of your session reaches the global timeout, it will be terminated.

If your session runs into an exception and your script doesn't handle it properly, your browser process might not exit properly, causing it to hang and remain open, which leads to consuming unnecessary resources, until it reaches the global timeout. It's always a best practice to [implement exception handling in your scripts](https://hackernoon.com/7-tips-to-making-your-puppeteer-scripts-more-bulletproof) to avoid this.

## Concurrency and Queue [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#concurrency-and-queue "Direct link to Concurrency and Queue")

The max concurrency and queue can be modified by using the slider.

### Concurrency tips [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#concurrency-tips "Direct link to Concurrency tips")

If you experience many timeouts/errors and rarely see queued sessions, your worker may be running out of resources and your worker is getting gridlocked. You can limit the max concurrency so that sessions don't run out of resources and hit the queue faster.

### Queue tips [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#queue-tips "Direct link to Queue tips")

If you use an external queueing system, you'll want to set your queue to 0, so that we return an error immediately after your concurrency limit has been reached. Bear in mind this feature may not be 100% flawless, due to the async implementation, a request may slip through the cracks if two requests are being received by the server exactly at the same time, so don't panic if a request gets queued even when set to 0.

## Session health checks [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#session-health-checks "Direct link to Session health checks")

If this feature is checked on, your worker will check the health of your worker before a session connects, be it an api call or library call; if the load balancer determines your worker(s) can't handle another request, it will throw a 5xx response code. Disabling this will send the requests to your worker blindly, forcing it to take the request independently of the health of the worker.

## Stealth mode [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#stealth-mode "Direct link to Stealth mode")

This feature implements puppeteer-extra-plugin-stealth, which injects user behavior to your page, helping your sessions avoid basic bot detecting techniques.

## Experimental features [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#experimental-features "Direct link to Experimental features")

The following features are experimental, which means they are to be used with caution, since they can have caveats you should consider before enabling them.

### Pre-boot chrome [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#pre-boot-chrome "Direct link to Pre-boot chrome")

This feature will launch browser instances and keep them in a pool of instances in order to cut-down on the boot time. Read more about [pre-booting chrome](https://www.browserless.io/docs/docker.html#pre-booting-chrome).

The caveat to this feature is that it may impact performance, since there will be more browsers open than necessary at a given point, which take up resources, hence reducing the available resources for your sessions that are actually running.

### Enable GET APIs [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#enable-get-apis "Direct link to Enable GET APIs")

This feature allows you to enable special /GET handlers for our APIs. This is handy for cases where you need to directly call our services from a cache-layer like a CDN. Read more information on the [/GET APIs](https://www.browserless.io/docs/api-get).

Please do not call the hosted service from the browser as it will reveal your secret token!

### Automatic health restarts [​](https://docs.browserless.io/baas/v1/hosted-service/worker-settings\#automatic-health-restarts "Direct link to Automatic health restarts")

This feature will restart your worker automatically when CPU or Memory usage are above 100% for a period of time (by default 5 minutes). Read more about [exiting on health failure](https://www.browserless.io/docs/docker.html#exit-on-health-failure)

- [Puppeteer version and global timeout](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#puppeteer-version-and-global-timeout)
  - [Supported chrome/puppeteer versions](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#supported-chromepuppeteer-versions)
  - [Global timeout](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#global-timeout)
- [Concurrency and Queue](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#concurrency-and-queue)
  - [Concurrency tips](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#concurrency-tips)
  - [Queue tips](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#queue-tips)
- [Session health checks](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#session-health-checks)
- [Stealth mode](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#stealth-mode)
- [Experimental features](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#experimental-features)
  - [Pre-boot chrome](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#pre-boot-chrome)
  - [Enable GET APIs](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#enable-get-apis)
  - [Automatic health restarts](https://docs.browserless.io/baas/v1/hosted-service/worker-settings#automatic-health-restarts)