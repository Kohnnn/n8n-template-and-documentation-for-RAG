---
url: "https://changedetection.io/tutorial/how-get-product-re-stock-or-back-stock-alerts-and-notifications"
title: "How to get product re-stock or \"back in stock\" alerts and notifications ? | changedetection.io"
---

[Skip to main content](https://changedetection.io/tutorial/how-get-product-re-stock-or-back-stock-alerts-and-notifications#main-content)

# How to get product re-stock or "back in stock" alerts and notifications ?

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 28 November, 2023



Topic

[How-To](https://changedetection.io/topic/how)

One thing we are all used to seeing is the dreaded **"out of stock"** or **"stock expected soon"** status on our favourite e-shop.

Need to get notified when something is back in stock? There is a solution - You can **simply add your website monitor** and select the **"Re-stock detection for single product pages"** option. ![Out of stock? back in stock? example photo](https://changedetection.io/sites/changedetection.io/files/2023-11/restock.png)

This plugin will automatically scrape the page and decide if the product is in stock or not, sending you an alert when the product goes back in-stock _(or you can configure it to send you an alert if it goes to "not in stock" status too!)_

In this short article I'll show you step-by-step how to get the most out of changedetection.io by using the built-in **product** **restock detection** plugin, this is a fantastic plugin because you don't have to worry about any additional filters, wasting time with "CSS" or other tricks to make it work.

So lets go!

## Start monitoring for product restock in a one easy step!

Amazingly, you only need to enter the website address and select the right option :) the plugin will do the rest of the work for you.

### Step 1. Add the website link and select "Re-stock detection for single product pages"

Simply copy and paste the URL into the box and select **"Re-stock detection for single product pages"**, it's important that the product page only contains a single product with "out of stock" or similar text, it will not work where the product contains many different variations of the product that may or may not be in stock.

For example it's not recommended for a shoe website where there is a mix of shoes that are in stock depending on their size, but it is absolutely perfect for getting restock notifications for products like wireless earbuds, bikes that are a specific size, whiskey, food items, etc.

![Adding a website to monitor for product restock](https://changedetection.io/sites/changedetection.io/files/inline-images/image_35.png)

### Step 2. Let the service fetch the page and update the status

Next to the link in the list of websites you are watching you will see the **Not yet checked** status, this may take 20 seconds or so to check.

![Website change detection monitoring product restock getting status](https://changedetection.io/sites/changedetection.io/files/inline-images/image_36.png)

Once this is complete, changedetection.io will decide if the product is in-stock / available or not, in the example below, you can see that the status is **Not in stock**

![Example image when the product is not in stock or not available](https://changedetection.io/sites/changedetection.io/files/inline-images/image_38.png)

When the product finally becomes available for you to buy, the status will change from a grey **Not in stock** to a happy green I **n stock**

![product is detected as being back in stock and restocked (has no out-of-stock text)](https://changedetection.io/sites/changedetection.io/files/inline-images/image_41.png)

#### So how does it work?

The restock detector plugin is basically just a set of rules that we at changedetection.io already setup, it assumes the product is "in stock" and available _unless_ one of a long list of keywords is found, such as 'not currently available', 'not available', 'sold out' or ''out of stock' is found. (A full list of [words that it is checking for is available here](https://github.com/dgtlmoon/changedetection.io/blob/master/changedetectionio/res/stock-not-in-stock.js) )

In the case that one of the "negative" keywords is found, the product stock status is set to "Not in stock"

It's not totally perfect, it can happen that "sold out" appears in a recommended product further down the page, or many other possible but unlikely situations, we believe its about 90% accurate and is improving all the time.

#### Top features of our restock product notification system

- No need to specify additional filters
- Can be configured to notify _**only**_ when it goes "into stock"
- Low percentage of "wrong alerts" because we are not focusing on just any changing content
- Uses a much smarter way to check the content to decide if the product is available or not
- Easily add notifications/alerts for monitoring restock notification into Discord, Slack, Email, NTFY, Matrix, Teams and 85+ more other notification system.


So go ahead! give it a try!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.