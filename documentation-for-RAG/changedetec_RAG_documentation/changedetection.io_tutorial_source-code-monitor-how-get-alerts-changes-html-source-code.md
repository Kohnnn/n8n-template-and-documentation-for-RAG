---
url: "https://changedetection.io/tutorial/source-code-monitor-how-get-alerts-changes-html-source-code"
title: "Source code monitor - How to get alerts on changes to HTML source code | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/source-code-monitor-how-get-alerts-changes-html-source-code#main-content)

# Source code monitor - How to get alerts on changes to HTML source code

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 8 December, 2023



Topic

[How-To](https://changedetection.io/topic/how)

How to get alerts on changes to HTML source code? Sometimes you need to know when a very specific part of the HTML changes, for example you're watching a competitor and want to know when they change their shops metatags.

Or maybe you want to know if certain parts of your HTML have changed without your approval? Perhaps you are being pro-active in monitoring your site for defacement, hacking and more.

Another great feature of changedetection.io is that you can specify that you're interested in following the "source code" as the content change detection.

Just simply prefix the URL you are watching with **"** `source:` **"**

![Following source code for changes and get alerts - set up](https://changedetection.io/sites/changedetection.io/files/inline-images/image_43.png)

Then, for example let's say we are interesting in getting alerts/notifications when that website changes their `<title>` tag, click **\[edit\]** then head on over to **Filters  & Triggers**

![Adding title tag for following HTML changes](https://changedetection.io/sites/changedetection.io/files/inline-images/image_46.png)

Adding `//title` (a simple xPath rule) will now make changedetection.io only follow the `<title>` tag.

Or if you prefer simpler CSS, you can use for example `title` or `div` or `div span.interesting`

Clicking _**Preview**_ after the page has fetched shows us that it is correctly following the HTML for changes, and only that HTML for changes.

![HTML being followed for changes](https://changedetection.io/sites/changedetection.io/files/inline-images/image_47.png)

So when the title tag - in the HTML source changes, you can now get alerts/notifications, this is a super simple example and you can use your wild imagination of what you could do with this :)

You can also specify CSS, so if you wanted to follow changes to a some HTML by their CSS tag, then that is possible too.

**What about defacement monitoring?** that's certainly possible here too, often clever hackers will insert some HTML that is not visible in the browser but can have other affects, so another nice idea is to watch your site for changes in your HTML that you were not aware of.

Have fun!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.