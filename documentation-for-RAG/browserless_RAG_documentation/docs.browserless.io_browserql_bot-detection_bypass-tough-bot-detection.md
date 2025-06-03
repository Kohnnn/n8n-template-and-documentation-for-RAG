---
url: "https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection"
title: "Bypassing Tough Bot Detection - The Right Way | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection#__docusaurus_skipToContent_fallback)

On this page

Some sites are just tougher to bypass, and that's the nature of the game. Most sites are easily tricked to thinking you're a human, but some are just a little more clever. Some site use different bot-detection mecahnisms and require to be fooled just a little bit different than others. BQL has several buttons and switches to turn on and off to get it just right. So if you haven't been able to access your website, don't give up just yet, there's still hope!

## Fingerprints [​](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection\#fingerprints "Direct link to Fingerprints")

There are a few things you can do to change your fingerprint when navigating to sites with BQL. The different combination of your bql session's basic settings makes up your fingerprint, so you'll want to test different combination of them. You can find them under settings in our [BrowserQL tool](https://account.browserless.io/bql), in the icon showing 3 vertical lines.

### Residential Proxying [​](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection\#residential-proxying "Direct link to Residential Proxying")

One of the most important factors at play is what IP address you're navigating to a site from. Sites that have a high interest in not being visited by bots will subscribe to a range of IPs that come from datacenters such as AWS, GCP, DO, etc. and those coming from residential range of IPs. Using a residential proxy will greatly help generate a convincing fingerprint for your session.

The best thing you can do is also geo-locate your proxy in the same country that your target country is in, if you know this information. Some sites will only service browsers requesting from a specific country, so this feature will be useful.

Lastly, declaring if the proxy is sticky or not can make a slight difference. Disclaimer: A common misunderstanding is that a sticky proxy, means it will persist the IP address from one request to another, this is incorrect. Actually, using a sticky proxy means that every request made from that browser will come form the same IP address, which is normally how it works on real human's machines. Having sticky proxy off means that every request may travel through a different IP address, which isn't necessarily a bad thing, so you can try iterating between ON and OFF to see if that makes a difference.

### Browser binaries [​](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection\#browser-binaries "Direct link to Browser binaries")

You can select which browser you want to use, either Chromium or Chrome.
Which is the best? Well, the one that works for you!
Keep in mind that Chrome comes with codecs to render things like streamed videos, or other type of multimedia, so it is typically regarded as a more human-like browsers, however it's not a guarantee, and sometimes Chromium is the way to go!

### Adblock [​](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection\#adblock "Direct link to Adblock")

Everyone hates ads, especially humans. Using this feature basically means you're running an extension that blocks ads, meaning the target site will recognize that you actually have an adblocking extension installed, and this itself will change the fingerprint of your session.

### Human-like behavior [​](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection\#human-like-behavior "Direct link to Human-like behavior")

This will help with sites that track interactions with the website. Using this turned on will make smooth mouse behavior and human-like typing patterns, i.e. it'll make mistakes while typing, vary in speed and the mouse movements will be more erratic and human-like.

## Cloudflare [​](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection\#cloudflare "Direct link to Cloudflare")

Getting past cloudflare is quite a common obstacle, it's also quite easily bypassed with the [Verify](https://docs.browserless.io/browserql/bot-detection/solving-captchas#verify) mutation.

If it's not working properly, take these 3 things into consideration:

- Make sure that you have our residential proxying turned on, as it's a requirement for it to work.
- In rare cases, you'll have to tweak your fingerprint for it to work properly, so go over the aforementioned recommendations to find successful bypassing.
- Even though you're navigating to a site that might have cloudflare with something like waitUntil set to NetworkIdle, in a few cases, probably if there's redirection, it seems like the it's not working properly and you'll have to add a waitForNavigation mutation before the verify mutation, such as the below script:

```codeBlockLines_p187
mutation VerifyCloudflare {
  goto(url: "YOURSITE", waitUntil: networkIdle) {
    status
  }
  waitForNavigation(waitUntil:networkIdle){
    time
  }
  verify(type:cloudflare){
    found
    solved
    time
  }
}

```

## Tough Captchas [​](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection\#tough-captchas "Direct link to Tough Captchas")

[Solving captchas](https://docs.browserless.io/browserql/bot-detection/solving-captchas#solve) is supported in BQL, however it's important to note the current limitations.

Currently, we support recaptchas, hCaptcha and cloudflare turnstiles. If they require interaction such as sliding images, clicking on images, they aren't supported just yet.

There is also passive recaptchas, which pop up on certain sites like a small square with the recaptcha icon. Those are not solved by the solve mutation, rather those are bypassed strictly based on fingerprinting, so using the Solve mutation isn't necessary here.

## Advanced browser fingerprints [​](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection\#advanced-browser-fingerprints "Direct link to Advanced browser fingerprints")

Some sites can detect the underlying operating system that the browser is running on so sometimes, no amount of efforts to enhance your fingerprint may bypass the most complex bot-detecting systems. For these cases, we have a way to have browsers run directly on special hardware, this infrastructure setup is only available on Enterprise plans, so please [contact us](https://www.browserless.io/contact) to discuss this option further.

- [Fingerprints](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection#fingerprints)
  - [Residential Proxying](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection#residential-proxying)
  - [Browser binaries](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection#browser-binaries)
  - [Adblock](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection#adblock)
  - [Human-like behavior](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection#human-like-behavior)
- [Cloudflare](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection#cloudflare)
- [Tough Captchas](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection#tough-captchas)
- [Advanced browser fingerprints](https://docs.browserless.io/browserql/bot-detection/bypass-tough-bot-detection#advanced-browser-fingerprints)