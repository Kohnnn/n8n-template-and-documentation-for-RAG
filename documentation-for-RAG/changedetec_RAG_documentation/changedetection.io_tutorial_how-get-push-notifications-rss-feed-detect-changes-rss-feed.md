---
url: "https://changedetection.io/tutorial/how-get-push-notifications-rss-feed-detect-changes-rss-feed"
title: "How to get push notifications from a RSS Feed ? Detect changes in the RSS Feed! | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/how-get-push-notifications-rss-feed-detect-changes-rss-feed#main-content)

# How to get push notifications from a RSS Feed ? Detect changes in the RSS Feed!

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 17 October, 2023



Topic

[How-To](https://changedetection.io/topic/how)

When you love [RSS](https://en.wikipedia.org/wiki/RSS) , but there's something missing - you just want push notifications when your favourite RSS feed updates, or even better - if it updates with a keyword you are really interested in!

In this quick article I'll show you how to setup changedetection.io to monitor a RSS feed and send a push notification when that feed contains something new.

This recipe is super simple and can be used to configure your RSS monitoring to alert you via nearly any modern productivity based notification ( Discord, Telegram, Slack, AWS SES, IFTT, Home Assistant, Gotify, Line, Mattermost, Microsoft Teams, MQTT, NTFY, Nextcloud, Pager Duty, Rocket.Chat, SMTP, SMS or even desktop notifications! )

Infact there are [85+ supported notification methods](https://github.com/caronc/apprise#supported-notifications) that can be tied to monitoring an RSS stream

![](https://changedetection.io/sites/changedetection.io/files/inline-images/Screenshot_2023-10-17_14-15-07.png)

So let's go!

## Step 1. Add your RSS feed to changedetection.io

Visit your main overview page, and enter the RSS feed URL in the box above the list of websites that you want to follow, then click **EDIT > WATCH,** this will ensure the checking is paused until we are fully configured.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_16.png)

## Step 2. Setup the RSS filter

Monitoring an RSS feed does not require Chrome, so here in the edit page of the new "watch" you should select " **Basic/fast Plaintext/HTTP Client**" fetcher, this will ensure your RSS fetching is super fast without needing to to use Chrome.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_17.png)

#### _**Optional - RSS push notifications for the "title" only**_

**Optional -** If we want to tell changedetection.io that we are only interested in scanning the "title" field of the RSS feed for changes - so click on **Filters & Triggers** and enter **//item/title**

This simple piece of text/configuration ensures that it only extracts the RSS titles

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_22.png)

**Optional -** Do you want to scan the RSS titles for something special? Maybe you want to only be notified when a certain keyword appears in a new RSS feed title?

On the same " **Filters & Triggers**" tab, scroll down to " **Text filtering**", here there are many useful possibilities for monitoring an RSS feed, you could for example only trigger a notification when a certain keyword is removed from the feed, and/or ignore certain titles containing a particular keyword

I invite you to look around in this section, there's a lot of cool stuff here that can really narrow down your RSS feed monitoring.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_23.png)

## Step 3. Setup the notification

Finally, click on the " **Notifications**" tab, here the notifications work by entering one of 85+  services as a  "Notification URL" that will trigger a different push notification when your RSS feed changes.

In this example I've joined it to my favourite Discord chat webhook so that my team can get a notification when something important appears in the RSS feed

Each " **Notification URL**" should be in the format from [the list available here](https://github.com/caronc/apprise#supported-notifications) \- for example Discord will look like " _**https://discordapp.com/api/webhooks/...**_" and a Slack notification will look like " _**slack://botname@TokenA/TokenB/TokenC/Channel**_ **"**, there are many many possibilities including email/SMTP and much more.

My favourite personally is the [NTFY](https://play.google.com/store/apps/details?id=io.heckel.ntfy&hl=en&gl=US) mobile notification application.

[Full Discord bot setup instructions are here](https://github.com/caronc/apprise/wiki/Notify_discord) simply paste that notification URL for your Discord bot into the " **Notification URL list**"

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_24.png)

## Step 4. Sit back and enjoy your RSS feed notifications!

So now just click **SAVE** and relax :)

I hope this quick tutorial gave you some good inspiration for monitoring your favourite RSS feeds and receiving push notifications with changedetection.io

Don't forget that another built-in feature here is that you can always now go and view differences over time in those RSS feeds too :)

_Improved RSS handling was added in_ [_#1866_](https://github.com/dgtlmoon/changedetection.io/pull/1866)

_All the best and happy change detecting!_

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.