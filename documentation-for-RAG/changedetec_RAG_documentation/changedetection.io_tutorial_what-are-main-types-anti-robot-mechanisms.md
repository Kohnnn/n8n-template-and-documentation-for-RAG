---
url: "https://changedetection.io/tutorial/what-are-main-types-anti-robot-mechanisms"
title: "What are the main types of anti-robot mechanisms? | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/what-are-main-types-anti-robot-mechanisms#main-content)

# What are the main types of anti-robot mechanisms?

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 20 May, 2024



Topic

[Knowledge base](https://changedetection.io/topic/knowledge-base)

You may have read a lot about some tricks to defeat scraping such as changing your scraping browser's "User Agent" settings, however that's only the start of the story.

![anti-robot blocker](https://changedetection.io/sites/changedetection.io/files/inline-images/image_80.png)

In reality there are multiple ways that a service can detect your scraping attempts, changing the user-agent is just a small trick that may or may not help.

It's important to look at the whole session not with just "am I detected or not" perspective, but as a _**score between 1 and 10**_, with 10 being "looks like a robot!" and 1 being "hey nice browser and pretty human!"

So let's break it down a bit further, what are the main factors?

### Browser fingerprinting

_Anti-robot score importance: **High**_

This is a tricky subject, as it's probably the fastest evolving part of anti-robot technologies, so we'll break it down into a few parts.

##### Browser headers - User Agent

_Anti-robot score importance: **Medium/Low**_

Headers such as "User agent" are sent on request, and may identify you as a robot, the problem is that since Chrome 89 there's a **new subset of headers** that are sent...

[https://developer.chrome.com/docs/privacy-security/user-agent-client-hints](https://developer.chrome.com/docs/privacy-security/user-agent-client-hints)

Browsers also emit such headers as " `Sec-CH-UA`", not just simple old school "User agent" headers.

For example;

`Sec-CH-UA: "Chromium";v="93", "Google Chrome";v="93", " Not;A Brand";v="99"`

`Sec-CH-UA-Mobile: ?0`

`Sec-CH-UA-Platform: "macOS"`

Fortunately these can be turned off with the Chrome flag `--disable-features=UserAgentClientHint`

So just overriding the "User-agent" header without disabling this increases the chances of being detected as a robot, but so does disabling the feature altogether..

##### Browser TLS/SSL/TCP-IP fingerprinting

_Anti-robot score importance: **Medium/High**_

There also exists a few methods to fingerprint the actual connection "pattern" that the browser makes when performing the SSL connection with the webserver, JA3 and now JA4+ are just one of many libraries/methods out there that perform this.

Because the browser is compiled with a certain set/versions of SSL libraries, the connection itself from the browser can be fingerprinted

More here [https://github.com/salesforce/ja3](https://github.com/salesforce/ja3)

> _**"TLS and it’s predecessor, SSL, I will refer to both as “SSL” for simplicity, are used to encrypt communication for both common applications, to keep your data secure, and malware, so it can hide in the noise. To initiate a SSL session, a client will send a SSL Client Hello packet following the TCP 3-way handshake. This packet and the way in which it is generated is dependant on packages and methods used when building the client application. The server, if accepting SSL connections, will respond with a SSL Server Hello packet that is formulated based on server-side libraries and configurations as well as details in the Client Hello. Because SSL negotiations are transmitted in the clear, it’s possible to fingerprint and identify client applications using the details in the SSL Client Hello packet."**_
>
> **"With JA3S it is possible to fingerprint the entire cryptographic negotiation between client and it's server by combining JA3 + JA3S. That is because servers will respond to different clients differently but will always respond to the same client the same."**

We're not aware of an easy work-around for this case, however perhaps using a specialist proxy service or other could help, this espicially affects Puppeteer type browsers that are all shipped with similar SSL/chrome libraries

##### Browser fingerprinting in general

_Anti-robot score importance: **Medium**_

There are many technologies here, for example some anti-robot services will attempt to detect the actual hardware you're running on and compare that against a database of known configurations, if it looks "weird" it will increase your robot rating

### The IP address that you're calling from

_Anti-robot score importance: **Medium**_

_IP address_ plays a fairly important role, many services such as Cloudflare protect their customers by rating the IP address you are calling from, if you are calling from a cheap data-centre proxy for example (the most common kind of paid proxy), they already know their IP ranges and will rate the possibility higher that you're a robot.

Use quality residential proxies, preferably via a "SOCKS" connection so that it does not relay to the remote end that you're even using a proxy.

### Scraping behaviour in general

_Anti-robot score importance: **Low**_

With computing power being quite high and costs cheap, this is not as important as it used to be, but many services will block you if you scrape too many pages concurrently or too fast sequentially, always be a "good internet scraper" and limit your scraping methods.

### Deny-at-start and allow-later

_Anti-robot score importance: **Hard to say**_

Some services assume EVERYONE is a robot, and block you at the start then use some fingerprinting to identify you going forwards, this is usually some kind of CAPTCHA or other process, then the browser is fingerprinted and you're allowed in there on.

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.