---
url: "https://docs.browserless.io/baas/v1/recipes/bot-detection"
title: "How to bypass bot detection | Browserless.io"
---

[Skip to main content](https://docs.browserless.io/baas/v1/recipes/bot-detection#__docusaurus_skipToContent_fallback)

Version: v1

On this page

DEPRECATION WARNING

This documentation is for BaaS v1, which is no longer actively supported. If you are a new user, please refer to the updated documentation for [BaaS v2](https://docs.browserless.io/baas/avoid-bot-detection/stealth) or [BrowserQL](https://docs.browserless.io/browserql/start).

Websites can have a different level of anti-bot mechanisms depending on the sensitivity of their data and budget. If your automations about being blocked, setting these three flags will bypass most anti-bot mechanisms.

## Flags to bypass bot detection [​](https://docs.browserless.io/baas/v1/recipes/bot-detection\#flags-to-bypass-bot-detection "Direct link to Flags to bypass bot detection")

### Use the `&headless=false` flag [​](https://docs.browserless.io/baas/v1/recipes/bot-detection\#use-the-headlessfalse-flag "Direct link to use-the-headlessfalse-flag")

Most bot detectors will check your user-agent, which by default explicitly claims you're running headless chrome. This is a dead giveaway. It can be changed by setting a specific user-agent but we highly recommend you use the &headless=false flag instead, which changes your user-agent to a more credible one.

### Use the `&stealth` flag [​](https://docs.browserless.io/baas/v1/recipes/bot-detection\#use-the-stealth-flag "Direct link to use-the-stealth-flag")

The stealth flag implements Puppeteer's puppeteer-extra-plugin-stealth plugin which applies various techniques to make detection of headless puppeteer harder. This flag may backfire and be easily detected by some sites, so consider avoiding it as well.

### Use our [in-built proxy](https://www.browserless.io/docs/proxying) or use a [third-party proxy](https://www.browserless.io/docs/using-a-proxy) [​](https://docs.browserless.io/baas/v1/recipes/bot-detection\#use-our-in-built-proxy-or-use-a-third-party-proxy "Direct link to use-our-in-built-proxy-or-use-a-third-party-proxy")

Finally, the hardest sites to crack down check your IP address; there are two type of bocks that can occur, those based on type of IP, and those based on frequency of requests (rate-limits).

- Sites checking the type of IP address will detect your data-center IP addresses when using Browserless. To overcome this, using a proxy with residential IP addresses will be the best option.
- Sites that work the first few times and then stop working, are probably rate-limiting and it's not the residential part of it that blocks us. For these cases, you don't necessarily need a residential proxy and data-center IP addresses that rotate should be enough.

## Additional strategies [​](https://docs.browserless.io/baas/v1/recipes/bot-detection\#additional-strategies "Direct link to Additional strategies")

If none of these do the trick, get in touch with us at [support@browserless.io](mailto:support@browserless.io) >.

We have more trick up our sleeves we can show you, such as captcha solving and our newest BQL tool on our current v2 build, upgrade to the latest build to learn [new bypassing methods](https://docs.browserless.io/baas/avoid-bot-detection/stealth).

- [Flags to bypass bot detection](https://docs.browserless.io/baas/v1/recipes/bot-detection#flags-to-bypass-bot-detection)
  - [Use the `&headless=false` flag](https://docs.browserless.io/baas/v1/recipes/bot-detection#use-the-headlessfalse-flag)
  - [Use the `&stealth` flag](https://docs.browserless.io/baas/v1/recipes/bot-detection#use-the-stealth-flag)
  - [Use our in-built proxy or use a third-party proxy](https://docs.browserless.io/baas/v1/recipes/bot-detection#use-our-in-built-proxy-or-use-a-third-party-proxy)
- [Additional strategies](https://docs.browserless.io/baas/v1/recipes/bot-detection#additional-strategies)