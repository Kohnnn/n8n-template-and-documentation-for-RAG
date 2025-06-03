---
url: "https://docs.browserless.io/baas/v1/libraries/go-cdp"
title: "Go (chromedp) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/libraries/go-cdp#__docusaurus_skipToContent_fallback)

Version: v1

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/libraries/chromedp) or [BrowserQL](https://docs.browserless.io/browserql/start).

We're happy to offer beta support of the excellent Go library [chromedp](https://pptr.dev/api/puppeteer.cdpsession)!

Usage of the library remains similar to how you'd run your application locally, simply use the `RemoteAllocator` to connect to browserless API.

An example of navigating to the Example.com site, and getting the title, is listed below as a jumping off point:

```codeBlockLines_p187
package main

import (
    "context"
    "flag"
    "log"

    "github.com/chromedp/chromedp"
)

func main() {
    devtoolsWsURL := flag.String("devtools-ws-url", "wss://chrome.browserless.io?token=****", "DevTools WebSsocket URL")
    flag.Parse()

    allocatorContext, cancel := chromedp.NewRemoteAllocator(context.Background(), *devtoolsWsURL,chromedp.NoModifyURL)
    defer cancel()

    ctx, cancel := chromedp.NewContext(allocatorContext)
    defer cancel()

    var title string
    if err := chromedp.Run(ctx,
        chromedp.Navigate("https://example.com"),
        chromedp.Title(&title),
    ); err != nil {
        log.Fatalf("Failed getting title of example.com: %v", err)
    }

    log.Println("Got title of:", title)
}

```

Be sure to [let us know if you have questions or issues](https://www.browserless.io/contact).