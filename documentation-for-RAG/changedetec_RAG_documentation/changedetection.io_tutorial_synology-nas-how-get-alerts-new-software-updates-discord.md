---
url: "https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord"
title: "Synology NAS - How to get alerts on new software updates via Discord! | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord#main-content)

# Synology NAS - How to get alerts on new software updates via Discord!

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 17 January, 2024



Topic

[How-To](https://changedetection.io/topic/how)

In this quick tutorial I'll show you how easy it is in to monitor a website for new software version releases and connect Discord for push notifications.

We will use Synology NAS in our little example, Synology have been continuously releasing great features and super stable software in recent years.

Ofcourse, what is cool is that you should [install changedetection.io on your Synology NAS](https://mariushosting.com/synology-install-changedetection-with-portainer/) (check out the link to Marius's [fantastic article](https://mariushosting.com/synology-install-changedetection-with-portainer/) on setting up changedetection.io on your Synology NAS)

_So let's go!_

Add your favourite Synology product page's software update page URL to monitor, in this example we have the DS723, but the same recipe applies for pretty much all of their range, (we tested with DS723+, DS920+ etc)

![Adding Synology NAS product URLs to monitor for changes](https://changedetection.io/sites/changedetection.io/files/inline-images/image_69.png)

Now your overview list should look something like below (We clicked \[edit\] then  ticked the "Use <title> as title of the watch" option so it's a little easier to read)

![Synology NAS production URL list](https://changedetection.io/sites/changedetection.io/files/inline-images/image_70.png)

Now the Synology NAS website has a lot of extra information in the footers and headers, using the **Visual Selector** tool available under **\[edit\]** we simply select the actual content area

![Synology NAS Visual Selector tool example](https://changedetection.io/sites/changedetection.io/files/inline-images/image_71.png)

You can see that changedetection.io has correctly identified **//\*\[@id="release\_notes\_content"\]** as the place where the the content lives (this is the area of the web page that would be used for change detection)

Now when Synology NAS release a new version/update you should be able to see the differences

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_72.png)

### Connecting Discord

To have a bot send notifications to your server’s channel you need to paste in the following "Notification URL" in the notification settings

`discord://webhook_id/webhook_token`

To get a `webhook_id` and a `webhook_token`. Click the settings icon beside the chat and click `Integrations`.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_74.png)

Then click `View Webhooks`, then `New Webhooks` you can change the name of the bot if you like and copy the `Webhook URL`. It will usually be called by default "Spidey bot"

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_77.png)

![Setup the discord bot](https://changedetection.io/sites/changedetection.io/files/inline-images/image_78.png)

Then "Copy Webhook URL" (This is now the " **Notification URL**" in changedetection.io)

Simply paste that under the **Notification** settings of the watch (or global settings)

![Discord settings changedetection.io notification](https://changedetection.io/sites/changedetection.io/files/inline-images/image_73.png)

We recommend you try the " **Send test notification**" button to confirm everything is working as expected.

And there you have it! Now you'll receive push notifications of the changes/updates in the Synology NAS software releases page via Discord

![Discord notification from changedetection.io bot](https://changedetection.io/sites/changedetection.io/files/inline-images/image_79.png)

Have fun!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.