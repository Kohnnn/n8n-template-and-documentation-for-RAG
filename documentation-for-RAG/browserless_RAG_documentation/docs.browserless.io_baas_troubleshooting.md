---
url: "https://docs.browserless.io/baas/troubleshooting"
title: "Long queues | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/troubleshooting#__docusaurus_skipToContent_fallback)

Version: v2

On this page

This doc is intended to help you understand potential causes for excessive queues. They are most often from issues with managing sessions where they are left to idle for too long.

## Closing and disconnecting browsers [​](https://docs.browserless.io/baas/troubleshooting\#closing-and-disconnecting-browsers "Direct link to Closing and disconnecting browsers")

With Browserless, you should call the `close` or `disconnect` method when a task is complete or there is an error. That will shutdown the process and let the next connection in, else it will continue until it hits the default 30s timeout.

This is different from how Puppeteer and Playwright handle idle and new browsers, so let’s look at the differences in more detail.

### What’s the default, and why we don’t do it [​](https://docs.browserless.io/baas/troubleshooting\#whats-the-default-and-why-we-dont-do-it "Direct link to What’s the default, and why we don’t do it")

Puppeteer and Playwright use a fairly blunt approach to starting up browsers.

They don’t care if you already have a browser running in a function/worker, they’ll listen to any command to start a browser and shove it in there. About the only thing that these libraries will check is that the browser-binary itself is present and is executable.

While this type of process can work decently in development, a more nuanced approach is needed for production. Things like machine health, implied dependencies, and more start to come into play.

### Managing browsers with Browserless [​](https://docs.browserless.io/baas/troubleshooting\#managing-browsers-with-browserless "Direct link to Managing browsers with Browserless")

Browserless takes the opposite approach. If a browser is running, it is protected from being pushed aside by a new script.

If a new connection is started, and there’s already browsers running, we “hold” onto that connection until a spot becomes available. That’s why we have things like concurrency, queue, and timeout limits. These are all there to help things flow through Browserless in a streamlined way.

But what about health? If things are in a place where a Browser can start, Browserless does one last check on CPU and Memory to ensure that the browser can be started and run properly. Without it you’re likely to run into other timeouts (like navigation) due to lack of proper resources.

We feel that this has many advantages:

- You can limit via concurrent access.

- You can begin to queue additional access once concurrent slots are full.

- After that we do a quick “pulse check” to see if access is viable.


Of course all of this is optional, but comes at our recommendation of a best practice.

### Deciding when to close browsers [​](https://docs.browserless.io/baas/troubleshooting\#deciding-when-to-close-browsers "Direct link to Deciding when to close browsers")

Switching this priority around means you’ll need to decide when to close a browser, otherwise they’ll stay open until they hit the default timeout of 30s.

Whilst our timeouts are there to help a browser from hogging execution time, the best thing you can do is to quickly (and in the case of errors) call the `close` or `disconnect` method. Browserless will see this, shutdown the process, and let the next connection in.

_Note: It’s hard for us to set a blanket rule of “close them when they’re idle” as idle means different things to different people, so we have to leave it up to each user._

Some options we would suggest are:

- Closing the browser when you’ve got what you came for.

- If an unrecoverable error happens, then shutdown and retry.

- Set a `TIMEOUT` parameter that’s reasonable and within an acceptable range of time.


- [Closing and disconnecting browsers](https://docs.browserless.io/baas/troubleshooting#closing-and-disconnecting-browsers)
  - [What’s the default, and why we don’t do it](https://docs.browserless.io/baas/troubleshooting#whats-the-default-and-why-we-dont-do-it)
  - [Managing browsers with Browserless](https://docs.browserless.io/baas/troubleshooting#managing-browsers-with-browserless)
  - [Deciding when to close browsers](https://docs.browserless.io/baas/troubleshooting#deciding-when-to-close-browsers)