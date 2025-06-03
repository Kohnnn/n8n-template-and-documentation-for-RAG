---
url: "https://docs.browserless.io/baas/libraries/chromedp"
title: "Go (chromedp) | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/libraries/chromedp#__docusaurus_skipToContent_fallback)

Version: v2

We offer beta support for the [`chromedp`](https://pptr.dev/api/puppeteer.cdpsession) Go library.

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
    devtoolsWsURL := flag.String("devtools-ws-url", "wss://production-sfo.browserless.io?token=YOUR_API_TOKEN_HERE", "DevTools WebSsocket URL")
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