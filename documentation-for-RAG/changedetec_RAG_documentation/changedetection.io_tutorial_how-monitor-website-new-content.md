---
url: "https://changedetection.io/tutorial/how-monitor-website-new-content"
title: "How to monitor a website for NEW content | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/how-monitor-website-new-content#main-content)

# How to monitor a website for NEW content

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 5 January, 2024



Topic

[How-To](https://changedetection.io/topic/how)

How to monitor a site or web page for _new_ content ? How can you configure changedetection.io to only show _**NEW**_ content from a site and send you a notification?

Unlike other services, changedetection.io is mostly interested in _**the actual text content of the website**_, this means that we can provide some super cool filters that allow you to really specify exactly what it is that you're interested in.

This can easily be achieved once you have added a website to watch, then set the " **Added or Removed text**" option in the Filters section.

This will allow you to only get alerts and notifications when the website has added new content.

![How to monitor a website for new content - a graphic showing what could be detected](https://changedetection.io/sites/changedetection.io/files/inline-images/image_62.png)

## Where to find the option to monitor a website for NEW content?

Fortunately, all related options are easily discoverable under **Edit >** **Filters & Triggers** then scroll down to " **Text filtering**" under the website page that you are monitoring.

![Set up options for monitoring website for new content screenshot](https://changedetection.io/sites/changedetection.io/files/inline-images/image_65.png)

When the website is checked according to your prefered schedule, the system will compare the previous version with the current version, and while doing that comparison it will use the rules that you have selected.

So in this case, since all options (Added, Replaced, Removed) are selected, then _any_ text change in the website page will trigger a "change" (and optionally send an alert)

However, if you select only " **Added lines**" and " **Replaced/changed lines**" then you will not get an alert if something unrelated is removed, only if something is added new, or removed.

It's important to keep in mind that the exact calculation of " **replaced**" and " **added**" depends on how similar the texts are, so in most cases if you want to get an alert when NEW content is added, it's definitely worth selecting both of those options (and leave **Removed lines** unchecked)

### What about completely new content on the webpage thats never been used before?

In the case that you really really only want completely new content on the web page that has never been seen before by changedetection.io, you can use the " **Only trigger when unique lines appear"** option, this means that every time a new version of web page is detected it will scan all current and old versions of the content and only tell you when _**some completely new and unseen content has appeared.**_

This can be handy when you're scraping a list of links or headlines and you want to be totally sure that they never appear in your alerts again (some websites re-use old articles for example)

Have fun! remember, there's many more options under "Filters & Triggers" and I recommend that you experiment with them all :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.