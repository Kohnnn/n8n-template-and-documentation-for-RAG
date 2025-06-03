# n8n Documentation


## Advanced

### Awesome use-case #4,510: How to get notified when Hetzner servers and products are available | changedetection.io
Original URL: https://changedetection.io/tutorial/awesome-use-case-4510-how-get-notified-when-hetzner-servers-and-products-are-available

[Skip to main content](https://changedetection.io/tutorial/awesome-use-case-4510-how-get-notified-when-hetzner-servers-and-products-are-available#main-content)

# Awesome use-case \#4,510: How to get notified when Hetzner servers and products are available

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 24 September, 2023



Topic

[How-To](https://changedetection.io/topic/how)

[Use-case](https://changedetection.io/topic/use-case)

We all love [Hetzner](https://www.hetzner.com/) for their excellent pricing and solid offers - but how to get a notification when one of their amazing servers comes back in stock?

[Hetzner](https://www.hetzner.com/) is a well-regarded hosting and cloud service provider known for offering reliable and high-quality hosting solutions. There are several reasons why Hetzner servers are often praised for their great service, Cost-effective pricing, robust infrastructure, multiple data-centres, incredible network performance and great customer service.

But the real heartbreak is when you are hunting for your dream [Hetzner Dedicated Server](https://www.hetzner.com/dedicated-rootserver?) only to find out that it's not available and that there's no good way to get alerts or notifications when Hetzner effectively "restock" that type of server.

Changedetection.io to the rescue :)

![Screenshot of Hetzner website as an example for change detection](https://changedetection.io/sites/changedetection.io/files/inline-images/image_18.png)

## How to get notifications or alerts when Hetzner servers are available to buy

Fortunately, Hetzner are super internet-friendly and make it easy to copy the link to the filters, you will need this link, place this link into changedetection.io

_**First**_, search for your **Dedicated Server** at **Hetzner**, you should see a _**"No server found"**_ message on the _Hetzner server listing page_, this may also work for other servers at Hetzner. In our example we searched for a AMD based server, at the time of writing this tutorial, there were no AMD based servers available.

_**Second**_, copy and paste the Filter URL into changedetection.io and hit **Watch**

![Adding the website to the change detection monitoring list](https://changedetection.io/sites/changedetection.io/files/inline-images/image_19.png)

_**Third and final**_, that's it!

![List of websites ready for change monitoring](https://changedetection.io/sites/changedetection.io/files/inline-images/image_20.png)

**Extra points!**

And ofcourse, you can jump over to to the **\[edit\]** tab and setup your **notifications**, remember, changedetection.io is not just about sending an email, but more useful is to trigger a message to your **Discord** channel and let your whole team know that the server you guys are hunting for is now available at **Hetzner**!

And ofcourse, through the magic of Apprise, changedetection.io supports more than 80 different kinds of notifications, including Slack, MS Teams, RockChat and more. PLUS you can also attach a screenshot!

![Notifications for website change monitoring](https://changedetection.io/sites/changedetection.io/files/inline-images/image_21.png)

( See our docs links and tutorials for getting your Discord API link :) )

**Extra extra points!**

Want to be MORE specific? You can even use the **Visual Selector** or **Browser Steps** tabs to click on items, and/or specifically focus on parts of the page - ensuring you get only the relevant notifications when Hetzner update their product availability :)

thanks for reading!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Email notification when a web page changes - How To | changedetection.io
Original URL: https://changedetection.io/tutorial/email-notification-when-web-page-changes-how

[Skip to main content](https://changedetection.io/tutorial/email-notification-when-web-page-changes-how#main-content)

# Email notification when a web page changes - How To

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 17 October, 2024



Topic

[How-To](https://changedetection.io/topic/how)

### How to Set Up Changedetection.io to Monitor a Web Page and Send Email Notifications

Changedetection.io is an excellent tool for monitoring changes to websites. Whether you're tracking stock prices, checking for product availability, or keeping an eye on any important web content, Changedetection.io can notify you when something changes. In this tutorial, weâ€™ll walk you through how to set up a web page monitor and configure email notifications for any updatesâ€”all using the subscription version of Changedetection.io.

#### Step 1: Log In (or Sign Up)

To begin, visit the [changedetection front page](https://changedetection.io/) and either sign up for a new account or log in if you already have one.

- After signing in, you will be directed to your dashboard, where you can see all your monitored web pages (if youâ€™ve already added any) or begin setting up new ones.
- If you just joined us, simply follow the instructions in the welcome email, the email will include the login information, passwords etc


#### Step 2: Configure the email address for notifications

Now that you are happily logged in, click **SETTINGS** in the top bar, and then the **NOTIFICATIONS** tab, by default we dont assume you will use email alerts because we Â support 95+ other notification systems such as Discord, Slack, MS-Teams, etc, so now you can simply add your email address here.

Click the **"ADD EMAIL"** button (located below the " _Notification URL list_" box), and fill in the email address you wish to notification when the web page changes, click **OK**

Then click **SAVE**(at the bottom of the page)

![How to add an email address for web page change alerts](https://changedetection.io/sites/changedetection.io/files/inline-images/image_89.png)

**Tip:** Once you have added your email address, you can also click _**"Send test notification"**_ to send a test email, so that you can be sure that you entered your information correctly

#### Step 3: Add a New Web Page to Monitor

1. Back the home page (click the "changedetection.io" text on the top left to return anytime) Add the website page URL in the box under the _"Add a new change detection watch"_ text, in this example we're adding `https://mycompany.com/news`
2. Then click **"Watch"** This will add the webpage to your list of watched pages, the system will begin rechecking the page at the default intervals (but you can change this anytime)


![Adding a web page URL for detecting changes](https://changedetection.io/sites/changedetection.io/files/inline-images/image_90.png)

We encourage you to explore the various settings and possibilities that can be achieved with changedetection.io, but in this tutorial we want to give you just the very easiest overview of how to start monitoring a webpage and receive alerts via email when ever a change to the website page occurs.

You can also click "EDIT" and explore other options such as the recheck interval time, the _Visual Selector_ for choosing which elements/parts of the web page to monitor and the _Browser Steps_ option for interacting with the page (such as logging in, performing searches etc), you can also choose to include a screenshot with the email.

All the best and have fun monitoring web pages for changes!

_**Update December 2024!**\-_ You can now also temporarily "Comment out" a notification, simply place a " `#`" before the address/notification, that way you can still store the notification for future use but it's not used / processed, see below :)

![Commented out, temporarily disabled web page change notification email address](https://changedetection.io/sites/changedetection.io/files/inline-images/image_92.png)

So for example " `#mailto://other@home.com`" is stored but never used, so it's easy to find it in the future if you wish to re-enable that notification, but `mailto://me@home.com` is always used when sending notifications of web page changes.

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Scrape and Extract data from websites and draw charts - How to gain valuable long-term insights | changedetection.io
Original URL: https://changedetection.io/tutorial/extract-data-websites-and-draw-charts-how-gain-valuable-long-term-insights

[Skip to main content](https://changedetection.io/tutorial/extract-data-websites-and-draw-charts-how-gain-valuable-long-term-insights#main-content)

# Scrape and Extract data from websites and draw charts - How to gain valuable long-term insights

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 27 December, 2023



Topic

[How-To](https://changedetection.io/topic/how)

Visualising long-term insights can lead to a lot of interesting and valuable realisations.

The web is always changing, but how does that information look across a week? a month? a year?

What if you wanted to draw a graph to show the number of properties advertised over a week? a month? a year?

![](https://changedetection.io/sites/changedetection.io/files/2023-12/changedet-line-chart-extract-data.png)

Using the **Extract Data** feature you can easily build a report (scrape data) based on specific text on a website, some examples;

- Number of real-estate results for a given search
- Number of google results for a given search
- Airbnb advertised apartments in a city
- Temperature or other climate information
- Scrape and graph prices, availability and more

Basically, any web page where it contains a number - can be used to build valuable reports.

## Example - Graph the number of results returned for a real-estate search over time

_**Scenario**_: You're watching a local real-estate website, and want to visualise trends over time for the number of search results, you've already setup your watch.

Here, we can see that the text says **"We found** _**473**_ **properties for you"**, so let's **Extract Data** on that text, receive the number only component as CSV and then draw a graph.

( In other words, let's build a graph over time of that " **473**" results word )

![Screenshot of the text from the real estate website we want to extract](https://changedetection.io/sites/changedetection.io/files/inline-images/image_48.png)

Head on over to your watch over-view list, click on **DIFF** to bring up the differences inspector, then click Â the **Extract Data** tab

![Text 'difference'](https://changedetection.io/sites/changedetection.io/files/inline-images/image_49.png)

So here's how to tell changedetection to extract that "473" over time, from all previous change snapshots and build a nice CSV report (of which we can easily import into Google Sheets and draw pretty graphs! )

![Showing how to extract given text](https://changedetection.io/sites/changedetection.io/files/inline-images/image_50.png)

The trick here is that we ONLY want to include the "473" text, not the whole "We found 473...", otherwise the spreadsheet will not understand the value as it would contain a mix of numbers and text.

So to ONLY include the "473" text we can use a simple [Regular Expression](https://en.wikipedia.org/wiki/Regular_expression) (A simple rule that tells it exactly what text to be interested in), using round brackets "()" we can tell changedetection to just use any digits that come after "We found..."

In our case, the best is to use `([0-9]+)` as the rule (any number 0-9 that is repeated), because its wrapped in "()" it means it will only pull that text/digits

So go ahead and enter Â `We found ([0-9]+)`

Then click **Extract as CSV,** in a few moments the system will look over all previous change snapshots, extract the text, and send you a CSV with the Time/date, time (in epoch format), and the number in the brackets from the Regular Expression.

And here we have it :-) after Importing to Google Sheets, then follow the steps to [how to create a chart in google sheets](https://support.google.com/docs/answer/63824?hl=en)

![Google graph chart spreadsheet of extracted data](https://changedetection.io/sites/changedetection.io/files/inline-images/image_51.png)

More fine examples to come (feel free to contact us and ask for a recipe!), but here is just one basic way to gather super interesting visualised line/chart data from website pages over time.

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### How to get alerts when certain keywords appear on PR Newswire? | changedetection.io
Original URL: https://changedetection.io/tutorial/how-get-alerts-when-certain-keywords-appear-pr-newswire

[Skip to main content](https://changedetection.io/tutorial/how-get-alerts-when-certain-keywords-appear-pr-newswire#main-content)

# How to get alerts when certain keywords appear on PR Newswire?

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 13 June, 2023



Topic

[How-To](https://changedetection.io/topic/how)

[PR Newswire](https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100) is a news distribution service. By monitoring keywords on PR Newswire, you gain insights, track brand reputation, discover media opportunities, make informed investments, and identify crisis risks.

By monitoring specific keywords on the PR Newswire website, you can achieve the following:

1. **Market Trends and Competitor Analysis**: If you're a business operating in a particular industry, you can track relevant keywords related to your products or services. This helps you stay informed about market trends, monitor your competitors' activities, and identify emerging opportunities or threats in the industry.
2. **Brand Reputation Management**: Monitoring your brand name and related keywords allows you to track mentions and sentiments about your company. This way, you can proactively manage your brand reputation, address any negative feedback or misconceptions, and leverage positive news to enhance your brand image.
3. **Media Outreach and Public Relations**: For PR professionals, tracking keywords relevant to their clients or industry can help in identifying potential media opportunities. By keeping an eye on relevant news stories and trends, they can reach out to journalists and influencers at the right time, increasing the chances of media coverage.
4. **Investment and Financial Insights**: Investors can monitor keywords related to financial results, mergers, acquisitions, or industry-specific terms. This helps them stay updated on the financial health of companies they are interested in, assess potential investment opportunities, and make informed decisions.
5. **Content Discovery and Story Ideas**: Journalists and content creators can track trending keywords to discover emerging news stories and topics that are gaining traction. This allows them to develop timely and relevant content, keeping their audience engaged.
6. **Crisis Management and Risk Assessment**: Monitoring keywords associated with crises or potential risks in your industry enables you to respond quickly to adverse events, mitigate potential damage, and communicate effectively with stakeholders.

Overall, monitoring specific keywords on PR Newswire offers valuable insights and opportunities to stay ahead in the competitive landscape, engage with your audience effectively, and make well-informed business decisions.

So in this article, I'll show you a quick recipe for a scenario where we want a track when a list of our favourite stock exchange codes has appeared in the news, this could mean that something interesting is happening and that we may need to buy or sell (for example)

So let's setup a simple watch to know when our favourite stock codes have appeared in the news, they are;

- _GOOGL_
- _AMZN_
- _NVDA_

#### Step 1. Â Add the PR Newswire page that contains the list of news as a watch

We will watch the URL [https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100](https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100), this page usually contains all the latest news, however you could choose a different page if you like, but in this page there is plenty of fresh content which could include the Â important keywords we are after.

Add the URL to the top input box, then click **Edit > Watch**

![Image removed.](https://changedetection.io/sites/changedetection.io/files/inline-images/image_2.png)

#### Step 2. Â Configure the keyword rules

Another super cool feature of changedetection.io is its ability to monitor for keywords, either that have been **added** or **removed**\- In our case we want to know when certain keywords appear in the text (not when they have been removed)

Simply click on over to **Filters & Triggers,** then scroll down to **Text filtering**

![Image removed.](https://changedetection.io/sites/changedetection.io/files/inline-images/image_3.png)

Down at **Text filtering**, it's important to select only **"Added lines"** and **"Replaced/changed lines"** this means that you will only get notifications when the page has new content matching the list of keywords you added.

Sometimes content can be regarded as "changed" when it's moved down a list of articles for example.

#### ![Image removed.](https://changedetection.io/sites/changedetection.io/files/inline-images/image_5.png)

Then ofcourse, click **Save**

And that's it! super easy keyword notification!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less) | changedetection.io
Original URL: https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less

[Skip to main content](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less#main-content)

# How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 17 April, 2025



Topic

[How-To](https://changedetection.io/topic/how)

**How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)**

If you've been trying to get your hands on Ubiquiti gearâ€”like the Power Distribution Pro, Cloud Gateway Fiber, or that elusive Dream Machine Proâ€”you know the story: blink, and it's sold out. Hitting refresh all day just doesnâ€™t cut it anymore. But thereâ€™s a smarter way to shopâ€”and it takes less than five minutes to set up.

With **ChangeDetection.io's Restock and Price Detection mode**, you can monitor any Ubiquiti product page and get notified instantly when it _comes back in stoc_ k. No complicated setup, no fiddling with page elementsâ€”just copy the product link, enable restock mode, and you're covered.

This guide will show you exactly how to do that. Whether you're new to this or already tracking a few items, you'll be up and running fast. And if you're serious about not missing restocks, you might want to consider upgradingâ€”faster checks mean you're first in line when stock drops.

With a bonus at the end - How to connect all of this to your favourite Discord channel

Letâ€™s get started.

_**First, grab a**_ [_**quick cheap subscription**_](https://changedetection.io/checkout) _**or**_ [_**install the changedetection.io software locally**_](https://github.com/dgtlmoon/changedetection.io) _**, in the case you grab a subscription you can be up and running in just a few seconds.**_

Not convinced? check out what other people are saying about _**changedetection.io for ubiquiti store Â restock detection**_!

- [https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks\_changedetectionio/](https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks_changedetectionio/)
- [https://www.reddit.com/r/Ubiquiti/comments/1hs6kzk/a\_better\_way\_for\_me\_to\_get\_instock\_alerts\_follow/](https://www.reddit.com/r/Ubiquiti/comments/1hs6kzk/a_better_way_for_me_to_get_instock_alerts_follow/?tl=pt-pt)

So let's go!

## Step 1. Â Add the link to the item you want restock or price changes for from the UI Ubiquity store

There's two ways todo this, both are super easy, first way is to Â add the URL directly to dashboard

Enter the URL of the product that you wish to monitor for restock or price change alerts directly in the dashboard

![Ubiquity add restock URL](https://changedetection.io/sites/changedetection.io/files/inline-images/image_115.png)

**Or** simply click on the browser extension to add the current product to your changedetection.io automatically Â [using the browser extension - simply set "restock" mode](https://chromewebstore.google.com/detail/changedetectionio-website/kefcfmgmlhmankjmnbijimhofdjekbop)

Your browser does not support the video tag.


## Step 2. Your favorite Ubiquity products are now monitored for restock / back in stock and price changes.

Back at your dashboard you can now see the status of all the products you're interested in, Green for "in stock" grey for "out of stock", as well as price.

Changedetection.io will recheck the items based on any schedule you prefer, you can even limit it by days of the week, hours of the day.

![Ubiquity UI store restock status overview with prices](https://changedetection.io/sites/changedetection.io/files/inline-images/image_120.png)

### Step 3 - Optionally set price conditions

This step is **completely optional** but if you prefer you can also limit the notifications of price / restock changes by whatever amount you like, so you could perhaps limit the notification to price drops on Ubiquity products (Set the "Threshold % change" box)

Or an absolute price, perhaps you want to know if the product drops to below $10 when it's normally $12. (Discount / end of product line / special sales notifications)

![Ubiquity configure price sales notifcations](https://changedetection.io/sites/changedetection.io/files/inline-images/image_123.png)

## Step 4 - Setup your notifications including email, Discord and many others

One of the best parts of using ChangeDetection.io is how it supports **virtually every notification service you can think of**â€”thanks to its integration with Apprise. Whether you want alerts on **Discord**, **SMS**, **Telegram**, **Slack**, **Microsoft Teams**, **Pushover**, **Gotify**, or even **email**, itâ€™s all built in and ready to go. You can set it up to ping your phone, your team, or even your smart home system the instant something changes. No more FOMOâ€”just instant, reliable alerts exactly where you want them. Whether you're at your desk or on the go, youâ€™ll never miss a restock again.

Head on over to the **"Notifications"** Â and setup which ever you prefer for you and your team!

Bonus points - Connect your Ubiquiti restock notifications to Discord! just follow this link [https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord](https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord#discord)

As always, have fun!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Kmart Shopping - Easily monitor prices and get restock alerts via email, discord, and others. | changedetection.io
Original URL: https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others

[Skip to main content](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others#main-content)

# Kmart Shopping - Easily monitor prices and get restock alerts via email, discord, and others.

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 20 January, 2025



Topic

[How-To](https://changedetection.io/topic/how)

![kmart.jpg (554Ã—397)](https://changedetection.io/sites/changedetection.io/files/2025-01/kmart.jpg)

Kmart is a great place to shop for every day needs, but what is even better is getting alerts when items come back in stock or when they are on sale (price reduced!)

In this quick tutorial I'll show you how to setup changedetection.io to notify you when items are re-stocked or have a price change.

So let's say for example we want to monitor the prices and restock situation with Feminine Hygiene products over at the Kmart website

![Restock and price change alerts feminine hygiene products](https://changedetection.io/sites/changedetection.io/files/inline-images/image_96.png)

### Adding the Kmart products for monitoring price and restock.

Simply access each page, and copy+paste the URL/web address of the product into your changedetection.io monitoring page, for example, the first product would be [https://www.kmart.com.au/product/u-by-kotex-14-pack-ultrathin-regular-pads-with-wings-43158805/](https://www.kmart.com.au/product/u-by-kotex-14-pack-ultrathin-regular-pads-with-wings-43158805/)

![Kmart product web page address](https://changedetection.io/sites/changedetection.io/files/inline-images/image_97.png)

Copy+paste this address into the "Add a webpage" box at the top of the changedetection.io monitoring page and select the Â " **Re-stock & Price detection for single product pages"** option.

( Pro tip: You can also use our [Web page change and price change detection Chrome plugin](https://chromewebstore.google.com/detail/changedetectionio-website/kefcfmgmlhmankjmnbijimhofdjekbop) )

![Kmart product - adding page for detecting price and restock changes](https://changedetection.io/sites/changedetection.io/files/inline-images/image_98.png)

Now on the front page of the application, you can see the restock status and pricing of your products that you're interested in

![Kmart products overview of prices and changes](https://changedetection.io/sites/changedetection.io/files/inline-images/image_100.png)

What's really nice here is that you can see the price and restock status of all your favourite products in one view, green = instock :)

The system will recheck all the items at the default recheck interval. There are many other options to explore such as increasing or decreasing the product page recheck schedule, checking between dates (maybe you only want to check on a weekday?) as well as setting "high" and "low" price thresholds - So you can get an alert when the product drops below $4 AUD for example.

### Setting up the alerts / notifications

There are 90+ different ways that you can be notified, such as email (the most classic way), Discord, MS-Teams and others, in the easiest way just visit " **Settings**" and " **Notifications**" then click " **Add** **email**"

![Kmart set up alerts for restock](https://changedetection.io/sites/changedetection.io/files/inline-images/image_99.png)

When the product is restocked OR has a price change you will then receive an alert to your email box :)

Happy shopping and we hope we saved you a few dollars :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### What are the main types of anti-robot mechanisms? | changedetection.io
Original URL: https://changedetection.io/tutorial/what-are-main-types-anti-robot-mechanisms

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

> _**"TLS and itâ€™s predecessor, SSL, I will refer to both as â€œSSLâ€ for simplicity, are used to encrypt communication for both common applications, to keep your data secure, and malware, so it can hide in the noise. To initiate a SSL session, a client will send a SSL Client Hello packet following the TCP 3-way handshake. This packet and the way in which it is generated is dependant on packages and methods used when building the client application. The server, if accepting SSL connections, will respond with a SSL Server Hello packet that is formulated based on server-side libraries and configurations as well as details in the Client Hello. Because SSL negotiations are transmitted in the clear, itâ€™s possible to fingerprint and identify client applications using the details in the SSL Client Hello packet."**_
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

---


## Other

### Website change detection, monitoring, alerts, notifications, restock alerts | changedetection.io
Original URL: https://changedetection.io/

[Skip to main content](https://changedetection.io/#main-content)

# Website ChangeDetection  ...For clever people

## _Page change monitoring with alerts a breeze._   The best way to monitor website changes.

Loved by smart-shoppers, bargain-hunters, data-journalists and more.

_Now with intelligent product restock detection!_

- [Continue with\\
    and](https://changedetection.io/checkout)

[Learn More](https://changedetection.io/#subscription)

$8.99/Month Easy Subscription


Cancel anytime â€ 5,000 URL watches included

Receive your private cloud based web login details immediately after signup, let us watch web-pages for you in our browsers, nothing to install.


85+ Notification formats supported!


![shape](https://changedetection.io/themes/cdio/assets/images/hero/dotted-shape.svg)![shape](https://changedetection.io/themes/cdio/assets/images/hero/dotted-shape.svg)

Features

Monitor web pages for changes - (such as watching prices, restock notification), to deep inspection such as PDF text support, JSON and XML monitoring and extensive text triggers.


Get notifications when a website updates.

### Notification Support

We work with as [many](https://github.com/caronc/apprise) notification formats as possible;


- Discord
- Slack
- Telegram
- Rocket.Chat
- Email
- Matrix
- NTFY
- Office 365

Unlimited notifications, including unlimited email notifications. All based on how many built in Chrome browsers you have setup.

### Target Elements

Select only what you need, easily choose elements to monitor.


### Browser Steps

Perform searches, Log in with username and password, Add to cart, Interact with fields, buttons and many more possibilities.



### Re-stock alerts

Monitor out-of-stock products and get alerts when those products are back in stock, get restock alerts via Discord, slack, email and many other platforms.


Perfect for finally getting that pair of shoes that's sold out or that RaspberryPi that's been unavailable!


Easy Subscription

## Start watching immediately!

Follow that price! Get restock notifications! Know when something changed, don't miss out!

We monitor web page changes for you in the cloud, nothing to install.

**Every subscription includes** - Login and Password sent to your email.
- Up to 5,000 URLs.
- Re-check times from 5~ minutes (per runner - with the ability to easily add more Chrome Browsers).

- Automatic updates, get new features continuously.
- Includes one real **Chrome Browser** for Javascript websites, bolt-on more browsers as required.
- Choose a virtual location - access to European , USA and Tor proxies included.
- Over 85 different notification types (Slack, Email, Discord and more)
- Includes Trigger Text, CSS/xPath Rules, Ignore Text and many more filters
- Import URLs as a list
- **Official provider** of the [changedetection.io opensource project](https://github.com/dgtlmoon/changedetection.io)

_Only **$8.99/mo**_ [Continue with Stripe\\
and](https://changedetection.io/checkout)

Safe secure payment, cancel anytime.

After signing up, you will receive an email from us with your login details, be sure to check your spam folders!

![about-image](https://changedetection.io/themes/cdio/assets/images/about/about-image.svg)

About the changedetection.io project

Changedetection.io is a fully opensource project, we rely on and financially support the libraries that we build on .


Our vision is to be the most dynamic and feature-filled way to monitor website changes, change notification and restock alert system, this can only be done with the help of the opensource community.

We are simply the best way to monitor website changes.

We believe in sustainable opensource development by supporting our project with a **fantastic** subscription product.


CONTACT US

## Need Support?    Got a Business Enquiry?

##### How can we help?

Contact us via the contact form and we will do our best to help!

Existing and new customers - Please always check your spam folders and always include your
login URL when contacting us for faster service.

### Send us a Message

Email\*

Existing Login URL

Message\*

Send Message

---

### As featured in | changedetection.io
Original URL: https://changedetection.io/as-featured-in

[Skip to main content](https://changedetection.io/as-featured-in#main-content)

# As featured in!

Find out what other people are saying about our service and project!

Let us watch the pages for changes automatically for you with our **official cloud subscription, nothing to install.**

- [Continue with\\
    and](https://changedetection.io/checkout) [Learn More](https://changedetection.io/#subscription)

- 12 December, 2024





##### Linux Magazine print edition \#289 - changedetection.io







Linux magazine print edition #289 covering changedetection.io and its wonderful uses!









[https://www.sparkhaus-shop.com/eu/eh30289.html](https://www.sparkhaus-shop.com/eu/eh30289.html)







[![linux magazine changedetection.io web page change](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/cover_289_lm_shop.png?itok=KbHMos_j)](https://www.sparkhaus-shop.com/eu/eh30289.html)

- 21 June, 2024





##### Technotim - Track Changes Online with ChangeDetection, a Self-Hosted Docker Container!







Techno Tim covers some great information for those who choose to self-host, read more!









[https://technotim.live/posts/change-detection-docker/](https://technotim.live/posts/change-detection-docker/)







[![changedetection with techno-tim](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/techno-tim-changedetection.jpeg?itok=FnyBefxb)](https://technotim.live/posts/change-detection-docker/)

- 5 January, 2025





##### YouTube @DanievanderMerwe gives an amazing overview of how to use and enjoy changedetection.io







Checkout YouTube @DanievanderMerwe's wonderful and insightful demonstration video of how to use changedetection.io









[https://www.youtube.com/watch?v=p2XuD\_pr\_6w&ab\_channel=DanievanderMerwe](https://www.youtube.com/watch?v=p2XuD_pr_6w&ab_channel=DanievanderMerwe)







[![Changedetection.io opensource youtube](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/Screenshot_2025-01-20_18-34-08.jpg?itok=Ssl8JwSX)](https://www.youtube.com/watch?v=p2XuD_pr_6w&ab_channel=DanievanderMerwe)

- 2 May, 2025





##### Techradar - Pro - changedetection.io







TechRadar Pro calls _Change Detection_ a top pick for beginners and small businesses, praising its ability to track 5,000 URLs affordably. The review adds weight, as TechRadar Pro is a trusted source for evaluating tech tools.









[TechRadar pro - Best website page change detection](https://www.techradar.com/pro/change%2Ddetection%2Dweb%2Dcontent%2Dmonitoring%2Dreview)







[![Techradar pro - website page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/techradar.jpg?itok=jPK1FfwA)](https://changedetection.io/TechRadar%20pro%20-%20Best%20website%20page%20change%20detection)

- 3 April, 2022





##### How to Track Changes on Websites without RSS or Mail Subscription







How to track changes on web sites which do not offer RSS feeds or email subscriptions.









[https://www.ajfriesen.com/how-to-track-changes-on-websites/](https://www.ajfriesen.com/how-to-track-changes-on-websites/)







[![track-changes-websites-without-rss](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/track-changes-websites-without-rss.png?itok=zKKHmDNh)](https://www.ajfriesen.com/how-to-track-changes-on-websites/)

- 5 April, 2025





##### r/ubuiqity







[https://www.reddit.com/r/Ubiquiti](https://changedetection.io/Ubiquiti%20restock%20alert) _"I was finally able to order a power distribution pro thanks to the changedetection.io docker container I finally got around to setting up."_



Check out more how you can monitor the Ubiquiti store for restock / back in stock and price changes here [https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)









[https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks\_changedetectionio/](https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks_changedetectionio/)







[![ubiquiti restock](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/ubiquiti-thanks.png?itok=6u8BjQCP)](https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks_changedetectionio/)

- 2 February, 2025





##### xTom covers changedetection.io!







xTom write a great small review of changedetection.io and how to monitor web pages for changes.









[https://xtom.com/blog/changedetection-io-website-change-monitorin](https://xtom.com/blog/changedetection-io-website-change-monitorin)







[![monitor web pages for changes](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/xtom-changedetectionio.jpeg?itok=Kv4gCAn7)](https://xtom.com/blog/changedetection-io-website-change-monitorin)

- 22 January, 2025





##### WebShare Proxies with changedetection.io







Integrating Webshare proxies with Changedetection allows you to overcome regional restrictions, avoid IP bans, and scale monitoring tasks seamlessly. By combining Webshare's reliable proxy services with Changedetection's powerful change-tracking features, you can ensure accurate, uninterrupted and efficient website monitoring.









[https://www.webshare.io/blog/changedetection-io-proxy](https://www.webshare.io/blog/changedetection-io-proxy)







[![WebShare proxies](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/webshare-proxies.jpeg?itok=1uxuq-UM)](https://www.webshare.io/blog/changedetection-io-proxy)

- 14 February, 2025





##### Leak allegedly reveals DOGE list of â€žwasteful projectsâ€œ







[Markus Reuter](https://netzpolitik.org/author/markusr/) over at the fantastic [netzpolitik.org](https://netzpolitik.org/) uses changedetection.io to monitor possible leaks of "wasteful spending" lists over at US government websites, read more!









[https://netzpolitik.org/2025/u-s-government-leak-allegedly-reveals-doge-list-of-wasteful-projects/](https://netzpolitik.org/2025/u-s-government-leak-allegedly-reveals-doge-list-of-wasteful-projects/)







[![DEI Website screenshot from Markus - detected changes](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/dei-webseite-screenshot-2-860x484.jpeg?itok=e2D3TlT0)](https://netzpolitik.org/2025/u-s-government-leak-allegedly-reveals-doge-list-of-wasteful-projects/)

- 13 September, 2024





##### Stoeps.de - Make Mastodon announcements from RSS feeds!







How to setup Mastodon notifications from changedetection.io and toot when your favourite RSS updates!



_"Here are the steps to get the information from the RSS feed. I run this once or twice a day and just grep the latest entry of the RSS feed because I normally do not post more than once a week"_









[https://stoeps.de/posts/2024/toot-new-blogposts/](https://stoeps.de/posts/2024/toot-new-blogposts/)







[![Mastodon toots ](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/mastodon.jpg?itok=4hN9JdHZ)](https://stoeps.de/posts/2024/toot-new-blogposts/)

- 23 October, 2023





##### The Web Scraping club - On changedetection.io !







Co Founder of [Databoutique.com](http://databoutique.com/), web scraper with 10+ years of experience, writing The Web Scraping Club - read his coverage of our tool right here.









[https://substack.thewebscraping.club/p/change-detection-for-web-scraping](https://substack.thewebscraping.club/p/change-detection-for-web-scraping)







[![Web Scraping Club and Change Detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/scraping-changedetection.jpg?itok=WUveRol3)](https://substack.thewebscraping.club/p/change-detection-for-web-scraping)

- 6 April, 2023





##### Make Use Of Blog - Changedetection.io with RaspberryPi for monitoring web page changes







Whatever the reason, there's often a need to monitor a web page for changes, and by running Changedetection.io on your Raspberry Pi, you can monitor as many sites as you like and receive notifications through services such as Discord, email, Slack, and Telegram. It's an incredibly useful tool.









[https://www.makeuseof.com/raspberry-pi-changedetection-webpage-updates/](https://www.makeuseof.com/raspberry-pi-changedetection-webpage-updates/)







[![make use of (MUO) web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/muo-changedetection.jpg?itok=WNxvmO9H)](https://www.makeuseof.com/raspberry-pi-changedetection-webpage-updates/)

- 23 November, 2024





##### Chris hutchins with Steph Smith - Use the Internet Better: The Tools and Tactics You Need







Whether youâ€™re a seasoned researcher or a casual browser, youâ€™ll gain practical strategies to unlock the internetâ€™s full potential.









[https://www.chrishutchins.com/steph-smith-navigating-the-internet-pipes/](https://www.chrishutchins.com/steph-smith-navigating-the-internet-pipes/)







[![detect web page changes with chris hutchins](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/chrishutchins.jpg?itok=wW8BmDgV)](https://www.chrishutchins.com/steph-smith-navigating-the-internet-pipes/)

- 8 March, 2023





##### Noted blog - detailed overview of ChangeDetection







In this article, Noted will provide a detailed overview of ChangeDetection, including its features, benefits, and how it works.









[https://noted.lol/changedetection/](https://noted.lol/changedetection/)







[![Noted blog web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/noted.jpg?itok=n9uNXeEF)](https://noted.lol/changedetection/)

- 15 September, 2024





##### Formable YouTube blogs - Some great ways to use change detection













[https://www.youtube.com/watch?v=YT419N0iRHc&ab\_channel=Formable](https://www.youtube.com/watch?v=YT419N0iRHc&ab_channel=Formable)







[![Formable web page changedetection.io](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/formable.jpg?itok=wcO3XR5E)](https://www.youtube.com/watch?v=YT419N0iRHc&ab_channel=Formable)

- 2 January, 2023





##### AlternativeTo - Changedetection.io is the best alternative for web page change detection







Feel the love over at AlternativeTo, find out why we are the best! ( Not according to us, but by everyone else :-) )









[https://alternativeto.net/software/changedetection-io/](https://alternativeto.net/software/changedetection-io/)







[![VisualPing alternative Changedetection.io](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/changedetection-alternative-to.jpg?itok=JV6jiBMx)](https://alternativeto.net/software/changedetection-io/)

- 3 January, 2022





##### First time we hit the front page on YC Hacker news







A proud moment, first time we made it to the front page on YC invest's hacker news!









[https://news.ycombinator.com/item?id=29779618](https://news.ycombinator.com/item?id=29779618)







[![YC Hacker News front page - page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/hackernews.jpg?itok=Ihhsbgy-)](https://news.ycombinator.com/item?id=29779618)

- 20 April, 2024





##### What Website and Webpage Changes Easily with this amazing App: ChangeDetection













[https://medevel.com/changedetection-io/](https://medevel.com/changedetection-io/)







[![amazing web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/medevel-amazing-application.jpg?itok=o-BsE0Hz)](https://medevel.com/changedetection-io/)

- 22 September, 2022





##### OpenSource.com - Supported by RedHat - About changedetection.io







Read this indepth tutorial from OpenSource.com - Supported by RedHat - Use changedetection.io to get alerts when a website makes changes or updates.











[https://opensource.com/article/22/9/changedetection-io-open-source-website-changes](https://opensource.com/article/22/9/changedetection-io-open-source-website-changes)







[![web page change detection redhat opensource](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/redhat-change-detection.jpg?itok=7adZEJgD)](https://opensource.com/article/22/9/changedetection-io-open-source-website-changes)

- 12 April, 2022





##### @buf0rd - A walk through of Changedetection.io







A walk through of Changedetection.io. A python app allowing a person to maintain a self hosted website monitor. Great for catching website deals and news updates.













[https://www.youtube.com/watch?v=oqMpMM\_nuDU](https://www.youtube.com/watch?v=oqMpMM_nuDU)







[![Web page changes](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/websitechanges-youtube.jpg?itok=kJkL9RNM)](https://www.youtube.com/watch?v=oqMpMM_nuDU)

- 19 January, 2025





##### NMAAS EU - Using changedetection.io mini tutorial







NMAAS EU gives a great short overview of getting updates via email when a text change is detected.









[https://docs.nmaas.eu/nmaas-applications/tutorials/changedetectionio/](https://docs.nmaas.eu/nmaas-applications/tutorials/changedetectionio/)







[![NMAAS EU Web page change detection screenshot](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/nmaas-changedetectionio.jpg?itok=AAH2lOqL)](https://docs.nmaas.eu/nmaas-applications/tutorials/changedetectionio/)

- 8 January, 2025





##### YouTube @scottibyte shows how he uses changedetection to monitor software updates







YouTube @scottibyte shows how he uses changedetection to monitor software updates, product restock/price monitoring and notifications.







Text version also here https://discussion.scottibyte.com/t/change-detection-for-websites/526









[https://youtu.be/CIh695Z4LVs?si=qtiv1gh46ARItBvQ&t=141](https://youtu.be/CIh695Z4LVs?si=qtiv1gh46ARItBvQ&t=141)







[![scottybytes-web-page-change-detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/scottybytes-web-page-change-detection.jpg?itok=FcpcVKjl)](https://youtu.be/CIh695Z4LVs?si=qtiv1gh46ARItBvQ&t=141)

- 24 January, 2023





##### @Destroy43 gives a quick demo on watching prices with changedetection.io













[https://www.youtube.com/watch?v=gL\_DBHk0-Vo&ab\_channel=destroy43](https://www.youtube.com/watch?v=gL_DBHk0-Vo&ab_channel=destroy43)







[![gives a quick demo on watching prices with changedetection.io](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/changedetection-web-page-basics.jpg?itok=EhLD3YuI)](https://www.youtube.com/watch?v=gL_DBHk0-Vo&ab_channel=destroy43)

- 1 December, 2022





##### @DBTech YouTube - changedetection.io demonstration







@DbTech Gives a great overview of text filters and notifications with changedetection.io!









[https://www.youtube.com/watch?v=SmUDirCSaoE&ab\_channel=DBTech](https://www.youtube.com/watch?v=SmUDirCSaoE&ab_channel=DBTech)







[![web page change detection youtube - DBTech](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/dbtech-changedetection-web-page-change.jpg?itok=UQIkoxp-)](https://www.youtube.com/watch?v=SmUDirCSaoE&ab_channel=DBTech)


Did we miss something cool here? Please fill in the [contact form](https://changedetection.io/#contact) on the front page and let us know :)

---

### As featured in | changedetection.io
Original URL: https://changedetection.io/as-featured-in?page=0

[Skip to main content](https://changedetection.io/as-featured-in?page=0#main-content)

- 12 December, 2024





##### Linux Magazine print edition \#289 - changedetection.io







Linux magazine print edition #289 covering changedetection.io and its wonderful uses!









[https://www.sparkhaus-shop.com/eu/eh30289.html](https://www.sparkhaus-shop.com/eu/eh30289.html)







[![linux magazine changedetection.io web page change](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/cover_289_lm_shop.png?itok=KbHMos_j)](https://www.sparkhaus-shop.com/eu/eh30289.html)

- 21 June, 2024





##### Technotim - Track Changes Online with ChangeDetection, a Self-Hosted Docker Container!







Techno Tim covers some great information for those who choose to self-host, read more!









[https://technotim.live/posts/change-detection-docker/](https://technotim.live/posts/change-detection-docker/)







[![changedetection with techno-tim](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/techno-tim-changedetection.jpeg?itok=FnyBefxb)](https://technotim.live/posts/change-detection-docker/)

- 5 January, 2025





##### YouTube @DanievanderMerwe gives an amazing overview of how to use and enjoy changedetection.io







Checkout YouTube @DanievanderMerwe's wonderful and insightful demonstration video of how to use changedetection.io









[https://www.youtube.com/watch?v=p2XuD\_pr\_6w&ab\_channel=DanievanderMerwe](https://www.youtube.com/watch?v=p2XuD_pr_6w&ab_channel=DanievanderMerwe)







[![Changedetection.io opensource youtube](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/Screenshot_2025-01-20_18-34-08.jpg?itok=Ssl8JwSX)](https://www.youtube.com/watch?v=p2XuD_pr_6w&ab_channel=DanievanderMerwe)

- 2 May, 2025





##### Techradar - Pro - changedetection.io







TechRadar Pro calls _Change Detection_ a top pick for beginners and small businesses, praising its ability to track 5,000 URLs affordably. The review adds weight, as TechRadar Pro is a trusted source for evaluating tech tools.









[TechRadar pro - Best website page change detection](https://www.techradar.com/pro/change%2Ddetection%2Dweb%2Dcontent%2Dmonitoring%2Dreview)







[![Techradar pro - website page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/techradar.jpg?itok=jPK1FfwA)](https://changedetection.io/TechRadar%20pro%20-%20Best%20website%20page%20change%20detection)

- 3 April, 2022





##### How to Track Changes on Websites without RSS or Mail Subscription







How to track changes on web sites which do not offer RSS feeds or email subscriptions.









[https://www.ajfriesen.com/how-to-track-changes-on-websites/](https://www.ajfriesen.com/how-to-track-changes-on-websites/)







[![track-changes-websites-without-rss](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/track-changes-websites-without-rss.png?itok=zKKHmDNh)](https://www.ajfriesen.com/how-to-track-changes-on-websites/)

- 5 April, 2025





##### r/ubuiqity







[https://www.reddit.com/r/Ubiquiti](https://changedetection.io/Ubiquiti%20restock%20alert) _"I was finally able to order a power distribution pro thanks to the changedetection.io docker container I finally got around to setting up."_



Check out more how you can monitor the Ubiquiti store for restock / back in stock and price changes here [https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)









[https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks\_changedetectionio/](https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks_changedetectionio/)







[![ubiquiti restock](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/ubiquiti-thanks.png?itok=6u8BjQCP)](https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks_changedetectionio/)

- 2 February, 2025





##### xTom covers changedetection.io!







xTom write a great small review of changedetection.io and how to monitor web pages for changes.









[https://xtom.com/blog/changedetection-io-website-change-monitorin](https://xtom.com/blog/changedetection-io-website-change-monitorin)







[![monitor web pages for changes](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/xtom-changedetectionio.jpeg?itok=Kv4gCAn7)](https://xtom.com/blog/changedetection-io-website-change-monitorin)

- 22 January, 2025





##### WebShare Proxies with changedetection.io







Integrating Webshare proxies with Changedetection allows you to overcome regional restrictions, avoid IP bans, and scale monitoring tasks seamlessly. By combining Webshare's reliable proxy services with Changedetection's powerful change-tracking features, you can ensure accurate, uninterrupted and efficient website monitoring.









[https://www.webshare.io/blog/changedetection-io-proxy](https://www.webshare.io/blog/changedetection-io-proxy)







[![WebShare proxies](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/webshare-proxies.jpeg?itok=1uxuq-UM)](https://www.webshare.io/blog/changedetection-io-proxy)

- 14 February, 2025





##### Leak allegedly reveals DOGE list of â€žwasteful projectsâ€œ







[Markus Reuter](https://netzpolitik.org/author/markusr/) over at the fantastic [netzpolitik.org](https://netzpolitik.org/) uses changedetection.io to monitor possible leaks of "wasteful spending" lists over at US government websites, read more!









[https://netzpolitik.org/2025/u-s-government-leak-allegedly-reveals-doge-list-of-wasteful-projects/](https://netzpolitik.org/2025/u-s-government-leak-allegedly-reveals-doge-list-of-wasteful-projects/)







[![DEI Website screenshot from Markus - detected changes](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/dei-webseite-screenshot-2-860x484.jpeg?itok=e2D3TlT0)](https://netzpolitik.org/2025/u-s-government-leak-allegedly-reveals-doge-list-of-wasteful-projects/)

- 13 September, 2024





##### Stoeps.de - Make Mastodon announcements from RSS feeds!







How to setup Mastodon notifications from changedetection.io and toot when your favourite RSS updates!



_"Here are the steps to get the information from the RSS feed. I run this once or twice a day and just grep the latest entry of the RSS feed because I normally do not post more than once a week"_









[https://stoeps.de/posts/2024/toot-new-blogposts/](https://stoeps.de/posts/2024/toot-new-blogposts/)







[![Mastodon toots ](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/mastodon.jpg?itok=4hN9JdHZ)](https://stoeps.de/posts/2024/toot-new-blogposts/)

- 23 October, 2023





##### The Web Scraping club - On changedetection.io !







Co Founder of [Databoutique.com](http://databoutique.com/), web scraper with 10+ years of experience, writing The Web Scraping Club - read his coverage of our tool right here.









[https://substack.thewebscraping.club/p/change-detection-for-web-scraping](https://substack.thewebscraping.club/p/change-detection-for-web-scraping)







[![Web Scraping Club and Change Detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/scraping-changedetection.jpg?itok=WUveRol3)](https://substack.thewebscraping.club/p/change-detection-for-web-scraping)

- 6 April, 2023





##### Make Use Of Blog - Changedetection.io with RaspberryPi for monitoring web page changes







Whatever the reason, there's often a need to monitor a web page for changes, and by running Changedetection.io on your Raspberry Pi, you can monitor as many sites as you like and receive notifications through services such as Discord, email, Slack, and Telegram. It's an incredibly useful tool.









[https://www.makeuseof.com/raspberry-pi-changedetection-webpage-updates/](https://www.makeuseof.com/raspberry-pi-changedetection-webpage-updates/)







[![make use of (MUO) web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/muo-changedetection.jpg?itok=WNxvmO9H)](https://www.makeuseof.com/raspberry-pi-changedetection-webpage-updates/)

- 23 November, 2024





##### Chris hutchins with Steph Smith - Use the Internet Better: The Tools and Tactics You Need







Whether youâ€™re a seasoned researcher or a casual browser, youâ€™ll gain practical strategies to unlock the internetâ€™s full potential.









[https://www.chrishutchins.com/steph-smith-navigating-the-internet-pipes/](https://www.chrishutchins.com/steph-smith-navigating-the-internet-pipes/)







[![detect web page changes with chris hutchins](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/chrishutchins.jpg?itok=wW8BmDgV)](https://www.chrishutchins.com/steph-smith-navigating-the-internet-pipes/)

- 8 March, 2023





##### Noted blog - detailed overview of ChangeDetection







In this article, Noted will provide a detailed overview of ChangeDetection, including its features, benefits, and how it works.









[https://noted.lol/changedetection/](https://noted.lol/changedetection/)







[![Noted blog web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/noted.jpg?itok=n9uNXeEF)](https://noted.lol/changedetection/)

- 15 September, 2024





##### Formable YouTube blogs - Some great ways to use change detection













[https://www.youtube.com/watch?v=YT419N0iRHc&ab\_channel=Formable](https://www.youtube.com/watch?v=YT419N0iRHc&ab_channel=Formable)







[![Formable web page changedetection.io](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/formable.jpg?itok=wcO3XR5E)](https://www.youtube.com/watch?v=YT419N0iRHc&ab_channel=Formable)

- 2 January, 2023





##### AlternativeTo - Changedetection.io is the best alternative for web page change detection







Feel the love over at AlternativeTo, find out why we are the best! ( Not according to us, but by everyone else :-) )









[https://alternativeto.net/software/changedetection-io/](https://alternativeto.net/software/changedetection-io/)







[![VisualPing alternative Changedetection.io](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/changedetection-alternative-to.jpg?itok=JV6jiBMx)](https://alternativeto.net/software/changedetection-io/)

- 3 January, 2022





##### First time we hit the front page on YC Hacker news







A proud moment, first time we made it to the front page on YC invest's hacker news!









[https://news.ycombinator.com/item?id=29779618](https://news.ycombinator.com/item?id=29779618)







[![YC Hacker News front page - page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/hackernews.jpg?itok=Ihhsbgy-)](https://news.ycombinator.com/item?id=29779618)

- 20 April, 2024





##### What Website and Webpage Changes Easily with this amazing App: ChangeDetection













[https://medevel.com/changedetection-io/](https://medevel.com/changedetection-io/)







[![amazing web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/medevel-amazing-application.jpg?itok=o-BsE0Hz)](https://medevel.com/changedetection-io/)

- 22 September, 2022





##### OpenSource.com - Supported by RedHat - About changedetection.io







Read this indepth tutorial from OpenSource.com - Supported by RedHat - Use changedetection.io to get alerts when a website makes changes or updates.











[https://opensource.com/article/22/9/changedetection-io-open-source-website-changes](https://opensource.com/article/22/9/changedetection-io-open-source-website-changes)







[![web page change detection redhat opensource](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/redhat-change-detection.jpg?itok=7adZEJgD)](https://opensource.com/article/22/9/changedetection-io-open-source-website-changes)

- 12 April, 2022





##### @buf0rd - A walk through of Changedetection.io







A walk through of Changedetection.io. A python app allowing a person to maintain a self hosted website monitor. Great for catching website deals and news updates.













[https://www.youtube.com/watch?v=oqMpMM\_nuDU](https://www.youtube.com/watch?v=oqMpMM_nuDU)







[![Web page changes](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/websitechanges-youtube.jpg?itok=kJkL9RNM)](https://www.youtube.com/watch?v=oqMpMM_nuDU)

- 19 January, 2025





##### NMAAS EU - Using changedetection.io mini tutorial







NMAAS EU gives a great short overview of getting updates via email when a text change is detected.









[https://docs.nmaas.eu/nmaas-applications/tutorials/changedetectionio/](https://docs.nmaas.eu/nmaas-applications/tutorials/changedetectionio/)







[![NMAAS EU Web page change detection screenshot](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/nmaas-changedetectionio.jpg?itok=AAH2lOqL)](https://docs.nmaas.eu/nmaas-applications/tutorials/changedetectionio/)

- 8 January, 2025





##### YouTube @scottibyte shows how he uses changedetection to monitor software updates







YouTube @scottibyte shows how he uses changedetection to monitor software updates, product restock/price monitoring and notifications.







Text version also here https://discussion.scottibyte.com/t/change-detection-for-websites/526









[https://youtu.be/CIh695Z4LVs?si=qtiv1gh46ARItBvQ&t=141](https://youtu.be/CIh695Z4LVs?si=qtiv1gh46ARItBvQ&t=141)







[![scottybytes-web-page-change-detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/scottybytes-web-page-change-detection.jpg?itok=FcpcVKjl)](https://youtu.be/CIh695Z4LVs?si=qtiv1gh46ARItBvQ&t=141)

- 24 January, 2023





##### @Destroy43 gives a quick demo on watching prices with changedetection.io













[https://www.youtube.com/watch?v=gL\_DBHk0-Vo&ab\_channel=destroy43](https://www.youtube.com/watch?v=gL_DBHk0-Vo&ab_channel=destroy43)







[![gives a quick demo on watching prices with changedetection.io](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/changedetection-web-page-basics.jpg?itok=EhLD3YuI)](https://www.youtube.com/watch?v=gL_DBHk0-Vo&ab_channel=destroy43)

- 1 December, 2022





##### @DBTech YouTube - changedetection.io demonstration







@DbTech Gives a great overview of text filters and notifications with changedetection.io!









[https://www.youtube.com/watch?v=SmUDirCSaoE&ab\_channel=DBTech](https://www.youtube.com/watch?v=SmUDirCSaoE&ab_channel=DBTech)







[![web page change detection youtube - DBTech](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/dbtech-changedetection-web-page-change.jpg?itok=UQIkoxp-)](https://www.youtube.com/watch?v=SmUDirCSaoE&ab_channel=DBTech)


Did we miss something cool here? Please fill in the [contact form](https://changedetection.io/#contact) on the front page and let us know :)

---

### As featured in | changedetection.io
Original URL: https://changedetection.io/as-featured-in?page=1

[Skip to main content](https://changedetection.io/as-featured-in?page=1#main-content)

- 22 October, 2022





##### Using changedetection.io to get the latest Azure Networking updates







Check out this wonderful video tutorial from Adam Stuart over on his channel!









[https://www.youtube.com/watch?v=eKZGqPL8Lws](https://www.youtube.com/watch?v=eKZGqPL8Lws)







[![changedetection tutorial with Adam Stuart on YouTube](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/Screenshot_2025-01-20_20-50-30.jpg?itok=Q4wtrKuo)](https://www.youtube.com/watch?v=eKZGqPL8Lws)

- 19 April, 2023





##### Ship-yard covers changedetection.io







Welcome to Shipyardâ€™s Docker Compose Community Spotlight series! During this series, weâ€™ll feature a new Docker Compose-enabled open source project every week, show you how to run it on Shipyard, and how to contribute. This week, weâ€™ll be featuring [changedetection.io](https://github.com/dgtlmoon/changedetection.io) by GitHub user [dgtlmoon](https://github.com/dgtlmoon).









[https://shipyard.build/blog/docker-compose-community-spotlight-changedetection-io/](https://shipyard.build/blog/docker-compose-community-spotlight-changedetection-io/)







[![Shipyard covers changedetection.io](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/Callback-changedetection.png?itok=HW6OyhJO)](https://shipyard.build/blog/docker-compose-community-spotlight-changedetection-io/)

- 17 December, 2021





##### Episode 60 of the Selfhosted show







60: Someone Else's Computer









[https://pca.st/vru02iw3](https://pca.st/vru02iw3)







[![Self Hosted show all about changedetection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/featured/2025/cover_medium.jpg?itok=8zUYxKcp)](https://pca.st/vru02iw3)


Did we miss something cool here? Please fill in the [contact form](https://changedetection.io/#contact) on the front page and let us know :)

---

### Untitled
Original URL: https://changedetection.io/CHANGELOG.txt

```
    _                          _     _          _   _            _
 __| |_  __ _ _ _  __ _ ___ __| |___| |_ ___ __| |_(_)___ _ _   (_)___
/ _| ' \/ _` | ' \/ _` / -_) _` / -_)  _/ -_) _|  _| / _ \ ' \ _| / _ \
\__|_||_\__,_|_||_\__, \___\__,_\___|\__\___\__|\__|_\___/_||_(_)_\___/
                  |___/

HEAD / 2025-05-28 14:11:11 +0200:
 - Code - Fix dep warning (#3221)
 - Realtime UI - Reducing log output
 - UI - Reword restock detector plugin description
 - UI - Remove incorrect error text

0.49.18 / 2025-05-26 20:35:46 +0200:
 - 0.49.18
 - Realtime UI updates via WebSocket (#3183)
 - Update to Apprise 1.9.3 - BlueSky, Resend support (#3216)
 - UI - Update 'Browser Steps' UI text
 - Code - Remove unused f-strings (#3209)
 - Use logger.debug for playwright console logs (#3201)

0.49.17 / 2025-05-12 10:47:27 +0200:
 - 0.49.17
 - Resolve warnings of bs4 library (#3187)
 - Revert memory strategy change for html_to_text (Was hanging under high concurrency setups)

0.49.16 / 2025-05-03 16:43:04 +0200:
 - 0.49.16
 - Fixes to ensure proxy errors are handled correctly (#3168)
 - UI - Custom headers should have validation (#3172)
 - Update selenium library (#3170)
 - Restock detection - adding new string
 - Conditions - Levenshtein text similarity plugin - adding test, fixing import, fixing check for watches with 1 snapshot history (#3161)
 - Restock detection - Use cleaner logic for limiting elements to scan, refactor, improve tests (#3158)
 - pyppeteer fast puppeteer fetch - be sure viewport is set to --window-size if --window-size is set (#3157)
 - Improved global ignore test (#3140)
 - Update docker-compose.yml (#3149)
 - Small fix for xpath element scraper (#3145)
 - Plugins for conditions (and include Similarity / Levenshtein, wordcount conditions) Re #3108
 - Browser Steps - <Select> by Option Text - #1224, #1228 (#3138)
 - Browser Steps - error reporting and session shutdown improvements (#3137)

0.49.15 / 2025-04-18 14:57:28 +0200:
 - 0.49.15
 - Visual Selector & Browser Steps - Always recheck if the data/screenshot is ready under "Visual Selector" tab after using Browser Steps (#3130)
 - App logs - Send TRACE and INFO logs to stdout (#3051)
 - Development: introduce Ruff as linter/formatter (#3039)
 - Updating restock texts (#3124)
 - Only add screenshot warning if capture was greater than trim size (#3123)

0.49.14 / 2025-04-16 23:23:18 +0200:
 - 0.49.14
 - Small fix for multiprocessing start on Mac OS (#3121 #3115)
 - docs: Update reference URL (#3119)
 - UI - Fix to edit and groups template
 - Updating API documentation
 - Undo forced selenium headless mode, small refactor (#3112)
 - Playwright + Puppeteer fix for when page is taller than viewport but less than screenshot step_size (#3113)
 - Memory management -  Run HTML to text in sub process, a few more cleanups  to playwright (#3110)
 - UI Edit/Stats - Add levenshtein distance info, explains how "different" the last two snapshot are (#3109)

0.49.13 / 2025-04-11 13:46:58 +0200:
 - 0.49.13
 - API - Added notifications API endpoints (#3103)
 - Fetcher - Use bigger screenshot chunks to speed up page screenshot (#3107)
 - App memory - Apprise import only when needed - saves ~50Mb RAM if you dont have any notifications enabled (#3106)
 - Fetching - Small improvement memory handling in detecting price information (saves ~10Mb)
 - Refactor image saving with forked process to reduce memory usage, improvements to xpath scraper handling (#3099)
 - Update other methods to use updated screenshot handler (#3098)
 - Memory fixes for large playwright screenshots (#3092)
 - Filters - Support multi line regex  (#2889)
 - UI - Add UI options tab and setting to disable opening diff in a new tab (#3071)
 - README.md update - Including blurb about 'conditions'
 - Requests fetcher - Remove old screenshot when watch was in a different fetcher type (#3097)
 - Make chrome browser headless when checking the site with selenium (#3095)
 - UI - Field name update - Keyword triggers - Trigger/wait for text (#3088)
 - UI - "Recheck all" should also queue most overdue first  (same like automatic scheduler) (#3087)
 - Groups - Including "Extract text", "Text to ignore", "Trigger text" and "Text that should not be present" filters

0.49.12 / 2025-04-04 09:30:24 +0200:
 - 0.49.12

0.49.11 / 2025-04-03 18:54:20 +0200:
 - 0.49.11

0.49.10 / 2025-04-03 11:17:14 +0200:
 - 0.49.10
 - Update README.md
 - UI - "Conditions" section, making the Conditions setup table work better on mobile/responsive
 - Adding a GC memory cleanup (releases cached libxml memory and others) (#3079)
 - Python 3.11 container base (#3077)
 - Use lowercase static asset filenames
 - Restock detection - Add Indonesian phrases for out-of-stock detection (#3075)
 - Regession - Shared history/diff page with anonymous access turned on should allow screenshot access (#3076)
 - Update edit.html - linking to tutorial
 - Code - Tidy up lint errors (#3074)
 - UI - Update edit.html- xPath support text for 1 & 2
 - Text/fetching - Small fix for when last fetched was zero bytes and special options (removals/additions/changes) was set (#3065)
 - Notifications backend - Refactor + tests for Apprise custom integration (#3057)
 - UI - Watch edit - "Clone" Should be "Clone & Edit" without watch history, redirect to the new edit page (#3063 #2782)
 - UI - Conditions - Offer some information about what the filter/condition/trigger saw (#3062)
 - UI - Tidy up support links
 - UI - Set a graph % of ETA time completed of checking the watch (#3060)

0.49.9 / 2025-03-26 16:30:08 +0100:
 - 0.49.9
 - RSS Fixes and improvements - Ability to set "RSS Color HTML Format" in Settings, detect and filter content with bad content that could break RSS (#3055)

0.49.8 / 2025-03-25 22:59:56 +0100:
 - 0.49.8
 - Server - Path blueprint fixes and moving code blueprint to fix RSS forward slash on url (#3054)
 - API - Adding "Search" API (#3052)
 - Fetching - Upgrading to pyppeteer-ng 2.0.0rc8 (more modern pyee requirements)

0.49.7 / 2025-03-23 16:50:21 +0100:
 - 0.49.7
 - Adding Tags/Groups API (#3049)

0.49.6 / 2025-03-23 02:01:32 +0100:
 - 0.49.6
 - API Access should still work even when UI Password is enabled (#3046) #3045

0.49.5 / 2025-03-22 22:51:33 +0100:
 - 0.49.5
 - Template tidyup & UI Fixes (#3044)
 - Watch history -  Ensure atomic/safe history data disk writes (#3042 #3041)
 - Testing - Replace Linux only 'resource' library with cross-platform 'psutil' library (#3037)
 - Refactor code layout, add extra tests
 - New major functionality CONDITIONS - Compare values, check numbers within range, etc

0.49.4 / 2025-03-13 12:06:50 +0100:
 - 0.49.4
 - Datastore - Always use utf-8 encoding for error text output storage
 -  Restock detection - Adding french keywords for out of stock items
 - Browser Steps - Should use the Watch URL/link after any Jinja2 type templates are applied
 - BrowserSteps - Speed up scraping, refactor screenshot handling for very long pages (#2999)
 - Browser Steps - Added new "Make all child elements visible" action
 - Browser Steps - Added new "Remove elements" action
 - UI - Browser Steps - "Click X,Y" should focus on the input field also
 - UI - Browser Steps - Improving Browser Steps usability on mobile

0.49.3 / 2025-02-22 10:24:44 +0100:
 - 0.49.3
 - UI - Reverting JS change to tabs (the better fix was the W3C HTML validation)

0.49.2 / 2025-02-19 16:01:01 +0100:
 - 0.49.2
 - UI - Make the setup and error messages for Visual Selector and Browser Steps a lot more meaningful (#2977)
 - Update docker-compose.yml
 - UI - More W3C HTML validation fixes
 - UI - More W3C validation fixes (#2973)
 - UI - Tweaks for HTML validation
 - Filter - "Unique lines" could possibly crash if history was empty or cleared on the disk
 - UI - Sometimes the DOM wasnt ready when tab selection triggered via CSS, which displayed empty tabs on some browsers
 - Removing deprecated docker-compose.yml version attribute (#2967)
 - Update settings.html
 - Browser Steps - Increasing timeout for actions and unifying timeout values
 - Browser Steps - Fixing 'Uncheck checkbox' #2958
 - UI - "Browser Steps" tab should be always available with helpful info (evenwhen playwright is not configured) (#2955)
 - Adding `browser_steps` JSON Schema rule for API updates (#2957)
 - UI - Fix mute/unmute alt/title label alt/title text in watch overview (#2951)

0.49.1 / 2025-02-08 10:14:19 +0100:
 - 0.49.1
 - Update stock-not-in-stock.js - Italian (#2948)
 - Re #2945 - Handle/Strip UTF-8 ByteOrderMark in JSON strings correctly (fixes `"Exception: No parsable JSON found in this document" ` error) (#2947)
 - Add major and minor tags for Docker release workflow (#2938)
 - Adding jinja2/browsersteps test (#2915)
 - Header handling - Fix header parsing to split on the first colon only (headers where the value contained :// type may have been broken) (#2929)

0.49.0 / 2025-01-21 13:40:01 +0100:
 - 0.49.00
 - Update README.md
 - Build/Libraries - Pin `referencing` library which breaks due to out-dated flask_expects_json, remove pip upgrade in test(#2912)
 - Notifications - Custom POST:// GET:// etc endpoints - returning 204 and other 20x responses are OK (don't show an error was detected)(#2897)

0.48.06 / 2025-01-09 23:02:29 +0100:
 - 0.48.06
 - Restock -  Add test for new lower/higher price notification Re #2715 (#2892)
 - Update integration test for "linuxserver" test build (#2891)
 - Notifications - Update Apprise to 1.9.2 - Fixes custom posts:// gets:// etc URL's being double-encoded, fixes chantify:// notifications (#2868) (#2875)  (#2870)
 - Custom posts:// get:// notifications etc - Be sure our custom extensions are imported (#2890)
 - "Send test notification" button - Easier to understand test send results, Improved error handling, code refactor (#2888)
 - Improve `last_checked` vs `last_changed` time information precision (#2883)
 - Update Apprise to 1.9.1 (#2876)
 - Builder/Docker - Remove PUID and PGID ( they were not used ) (#2852)
 - UI - Fix diff not starting from last viewed snapshot (#2744) (#2856)

0.48.05 / 2024-12-27 11:24:56 +0100:
 - 0.48.05
 - Fixing test for CVE-2024-56509 (#2864)
 - CVE-2024-56509 - Stricter file protocol checking pre-check ( Improper Input Validation Leading to LFR/Path Traversal when fetching file:.. )

0.48.04 / 2024-12-16 21:50:53 +0100:
 - 0.48.04
 - Windows was sometimes missing timezone data (#2845 #2826)

0.48.03 / 2024-12-16 16:14:03 +0100:
 - 0.48.03
 - 0.48.02
 - 0.48.02
 - Notifications - "Send test" was not always following "System default notification format" (#2844)
 - Notifications - "Send test" was not always following "System default notification format"

0.48.02 / 2024-12-16 16:07:11 +0100:
 - 0.48.02
 - Notifications - "Send test" was not always following "System default notification format"
 - Notifications - Default notification format (for new installs) now "HTML color" (#2843)
 - Notification - `HTML Color` format notification colors should be same as UI, `{{diff_full}}` token should also get HTML colors ( #2842 #2554 )
 - Notifcations - Adding "HTML Color" notification format option (#2837)
 - UI - Make 'tag' sticky - redirect to current tag on edit or add watch (#2824 #2785)
 - Notifications - Support for commented out notification URLs (#2825 #2769)
 - Docs - Adding information to README.md about the new scheduler

0.48.01 / 2024-12-03 18:44:20 +0100:
 - 0.48.01
 - UI - Fixing scheduler options

0.48.00 / 2024-12-03 14:26:01 +0100:
 - 0.48.00
 - Fix HIDE_REFERER env option for hiding changedetection.io from referer headers (#2787)
 - New functionality - Time (weekday + time) scheduler / duration (#2802)
 - Add Turkish phrases for out-of-stock detection (#2809)
 - UI - Always use UTC timezone for storing data, show local timezone (#2799)
 - Update stock-not-in-stock.js
 - Python 3.13 compatibility (#2791)
 - Code - Update .gitignore and .dockerignore (#2797)
 - VisualSelector - Use 'deflate' for storing elements.json, 90% file size reduction (#2794)
 - UI - Show local timezone info in settings (for future functionality) #2793
 - Notification - Locking paho-mqtt:// version fix
 - Update COMMERCIAL_LICENCE.md
 - Ability to disable version check (set `DISABLE_VERSION_CHECK=true`) Re #2773 (#2775)
 - Minor improvement for queue management
 - Update bug_report.md

0.47.06 / 2024-11-07 20:10:02 +0100:
 - Security - Fix test
 - Security check - improve test
 - 0.47.06
 - CVE-2024-51998 - file:/ path traversal access should not be allowed to access a file without ALLOW_FILE_URI set
 - Update docker-compose.yml (#2767)
 - Price tracker - fix for sites that supply an empty additional price (#2758)
 - Testing - Pinning werkzeug (#2757)

0.47.05 / 2024-10-31 22:51:03 +0100:
 - 0.47.05
 - CVE-2024-51483 - Fix for limiting access to file:// via source:file:///tmp/file.txt when using webdriver/playwright
 - Backups - Hide incomplete/running backups from being downloaded
 - Backups - Backups now operate in the background, provide a nice UI to access/download previous backups (#2755)
 - Filters - Process all CSS and XPath 'subtract' selectors in a single pass to prevent index shifting and reference loss during DOM manipulation. (#2754)

0.47.04 / 2024-10-29 08:25:05 +0100:
 - 0.47.04
 - Do not recheck 'paused' watches on edit/save (Re #2747 #2750)
 - Notification post:// get:// etc - Fixing URL encoding of headers so that '+' in URL is correctly parsed as ' ' (and other url-encodings) (#2745)
 - #2502 - Add jinja2 template handling to request body and headers (#2740)
 - Restock detection - Add additional out-of-stock detection for PT language (#2738)
 - "Send test notification" in "Restock" mode was not working correclty when restock tokens "{{restock.price}}" were in the notification body (#2737)
 - #2727 Notifications - Fix "send test notification" on empty list, includes test (#2731)
 - UI - Fix mobile styling inconsistencies and resolve diff page overflow issue (#2716)
 - Filters - "Block change detection when text exists" should not trigger a change when the original text returns
 - UI - More work on tab buttons hiding behind menu/header  :-)

0.47.03 / 2024-10-11 17:33:00 +0200:
 - 0.47.03
 - Remove same checksum skip check - saved a little CPU but added a lot of complexity (#2700)
 - UI - Fix scroll offset / tab buttons hiding behind menu/header
 - 0.47.02
 - UI - Fix scroll offset / tab buttons hiding behind menu/header

0.47.02 / 2024-10-11 15:35:36 +0200:
 - 0.47.02
 - UI - Fix scroll offset / tab buttons hiding behind menu/header

0.47.01 / 2024-10-11 15:02:17 +0200:
 - 0.47.01
 - Adding missing `apprise_plugin` for pypi/pip based installs

0.47.00 / 2024-10-11 13:04:56 +0200:
 - 0.47.00
 - Restock multiprice improvements (#2698)
 - Test - Simple test for live preview
 - Adding test for proxy checker/scanner (#2697)
 - Fixing proxy checker (#2696)
 - UTF-8 handling fixes, Improvements to whitespace filtering (#2691)
 - Testing - Tidyup (#2693)
 - Filters & Text - Preview refactor/improvements (#2689)
 - Build - Add image source label to Dockerfile (Better Renovate and others support) (#2690)
 - Custom JSON/POST Notifications - Log when it could not apply the application/json content-type header
 - UI - Filters live preview - improvements to layout
 - Restock - Use the scraped 'Not in stock' product status over the metadata version (many website lie in the metadata) (#2684)
 - UI - Better 40x error message (#2685)
 - Visual Selector - Including <button> (#2686)
 - Stock/not-in-stock scraper - slight reliability improvement (#2687)
 - Code - Small improvements in logging
 - UI - CSS - Fix on sorting row wrapping issue (#2680)
 - UI - Live filters preview - Better handling of watch preferences
 - UI - "Diff" button in overview list is now "History" button (#2679)
 - UI - Improve error handling when a module is missing when editing a URL/link (#2678)
 - UI - Live filters preview - Make it sticky in the viewport so its easier to build nice filters
 - UI - Live filters preview - dark mode improvements
 - UI - Improvements to text preview on mobile
 - UI - Improvements to live preview of Filters text
 - UI - Misc fixes for mobile styling (#2669)
 - Update docker-compose.yml - Adding example for enabling change detection on local files
 - UI - Live preview - misc improvements (Adding test, fixes to filters) (#2663)
 - UI - "Filters & Triggers" - Live preview of text filters (Preview the output of the filters section in realtime) (#2612)
 - Reversing subprocess execution - saved a little memory but used a LOT more CPU (#2659)
 - [test] Use local data instead of reaching out to changedetection when testing (#2660)
 - Restock monitor - Only try to process restock information (like scraping for "out of stock" keywords) if the page was actually rendered correctly. (#2645)
 - Text filters - Adding filters "Trim whitespace" and "Remove duplicate lines"
 - Browser Steps - UI - Use a better flexbox layout
 - Filters - Add support for also removing HTML elements using XPath selectors (#2632)
 - Update AppRise notification library to 1.9.0 (#2624)
 - browser_steps: add "click element containing text if exists" (#2629)
 - Testing - Fixing Restock test #2641
 - Testing - Fix false filter missing check alerts
 - Restock/Price detection - Fix duplicated prices with different data type on single page product #2636 (#2638)
 - Memory management improvements - LXML and other libraries can leak allocation, wrap in a sub-process (#2626)
 - Small memory allocation fixes (#2625)
 - Testing - locale fix for test (#2623)
 - Testing/Code - Improving test reliability (#2617)
 - UI - Hiding noisy info under 'show advanced help' button (#2609)

0.46.04 / 2024-09-04 13:55:18 +0200:
 - 0.46.04
 - Fixing restock monitor tests and tweaking docker default config example,
 - Container name should be 'sockpuppetbrowser' because its not just playwright that uses it
 - Restock/Price detection - Better catching of errors when parsing metadata documents for restock/price check (#2602)
 - Restock - updating texts and text offsets
 - Build - Unpin jsonschema for faster builds (#2583)
 - Price detection/scraping - Adding extra element training data (#2582)

0.46.03 / 2024-08-19 17:22:13 +0200:
 - 0.46.03
 - Watch 'Download last snapshot' link/button should give last, not first snapshot (#2576)
 - Price and restock scraping - small price fix scraper (#2575)
 - Browser Steps UI - Interactive UI wasn't sending headers but was when the check ran  (#2551)
 - Set encoding type for scraper script reader (#2574 #2568)
 - Handle zero-byte/empty content responses with "`[ ] Empty pages are a change`" option, the same as when the HTML doesnt render any useful text (#2530)

0.46.02 / 2024-07-27 20:28:04 +0200:
 - 0.46.02
 - Adding test for #1995 UTF-8 encoding in POST request body and post:// notifications (#2525)
 - Updating Apprise notification library , Splunk/VictorOps, Africas Talking, Microsoft Power Automate / Workflows, SociÃƒÂ©tÃƒÂ© FranÃƒÂ§aise du RadiotÃƒÂ©lÃƒÂ©phone (SFR) Support (#2524)
 - Encode POST style requests and notifications as UTF-8 if it has no encoding/basic string (#2523)
 - VisualSelector+BrowserSteps - When scraping elements, check for null results (#2517)
 - Use #!/usr/bin/env to support virtualenv (#2518)
 - Update README.md
 - UI - Adding "Download latest HTML snapshot" from Edit Watch > Stats page for easier debugging (#2513)

0.46.01 / 2024-07-19 13:53:00 +0200:
 - 0.46.01
 - UI - Fixing up 'test notification' bug from main settings and tag settings pages #2510 (#2511)

0.46.00 / 2024-07-18 14:13:06 +0200:
 - 0.46.00
 - Restock/Price detection - Improving text information snapshot value
 - Restock - Tweaking storage of "original price"
 - Fixing file:// file pickup  - for change detection of local files (#2505)
 - Adding Apple M1 Pro type arm64/v8 support docker image (#2507)
 - Dropping older ARM v6 support due to dependencies not having support (#2506)
 - Ability to use restock and price amounts in notifications as tokens (for example {{restock.price}} ) (#2503)
 - Restock & Price detection - Ability to set up a tag/group that applies to all watches with price + restock limits
 - Fixing problematic tag assigning via UI which caused watches to not accept new settings
 - Fixing first history/preview save issue (First version after an error, on the first check, wasnt available) (#2494)
 - UI - Restock/price following text cleanups
 - UI - Extract <title> as title should work on all processors (#2490)
 - Restock & Price monitor -  Huge refactor, set upper and lower price alert limits, set % change, follow the prices and restock amounts directly in the watch-overview list
 - Product checks - Just a basic string check is far more efficient for suggestion price/restock check plugin (#2488)
 - Update COMMERCIAL_LICENCE.md
 - Update README.md - Adding link to COMMERCIAL_LICENCE.md for those interested in reselling the software
 - Adding COMMERCIAL_LICENCE.md
 - Testing - Adding simple memory usage test (#2483)
 - Bugfix - Watches with BrowserSteps should recreate the data-dir if it was missing (in the case that you deleted/migrated) (#2484)

0.45.26 / 2024-07-11 13:52:13 +0200:
 - 0.45.26
 - Code - Fixing deprecation warning (#2477)
 - UI - Visual Selector should still update when elements were not found (#2476)
 - Code - Update/modernise diff.py (#2471)
 - UI - Visual Selector - Multiple selections (refactor) (#2475)
 - UI - Visual Selector now supports Shift+Click for multiple selections!
 - UI - Visual Selector - Show/visualise all/any matching filter elements from all filters in "CSS/JSONPath/JQ/XPath Filters" include filters (#2440)
 - UI - Visual Selector graphics should be centred
 -  Snapshot count from history was not updated in watch after using [clear history] (#2459)
 - Fixing 'tags'' field from old installs (0.43.0+) could have wrong data-type causing crash

0.45.25 / 2024-07-03 19:27:23 +0200:
 - 0.45.25
 - UI - Fixing preview/diff "ignore text" highlight button (refactor, didnt work in "preview" mode) (#2455)
 - Restock detection - Updating detection texts
 - UI - Mobile - Hiding empty columns
 - UI - Mobile - Watch overview table - Sort/order buttons were not being shown correctly
 - Update docker-compose.yml - fix indentation re #2447
 - Restock detection - Added extra out-of-stock phrases for DE (#2442)
 - Restock detection - updating texts
 - UI - Fixing double punctuation in 'unpaused' message #2435
 - Build - Bump docker/build-push-action from 5 to 6 in the all group (#2436)
 - Now saving last two HTML snapshots for future reference, refactor, dont write screenshots and xpath to disk when no change detected (saves disk IO) (#2431)
 - Filters - Implement jqraw: filter  (use this to output nicer JSON format when selecting/filtering by JSON) (#2430)
 - Build - fixing build warnings
 - Upgrade to Python 3.11 from 3.10, add faster prebuilt "wheels" for rPi devices, upgrade cryptography security library
 - Prefer pythons built in "importlib" over pkg_resources+setuptools (#2424)
 - Security/dependabot - Bump urllib3 from 1.26.18 to 1.26.19 (#2423)

0.45.24 / 2024-06-17 13:27:11 +0200:
 - 0.45.24
 - Update eventlet ( Fixes SSL error on Python 3.12 ) (#2419)
 - Filter failure/not found notification threshold - Counter should be reset when editing a watch, clear watch errors on 'save' (#2413)
 - Bump dnspython from 2.3.0 to 2.6.1 (#2306)
 - Improve testing for Python 3.10, 3.11 and 3.12
 - UI - Add space around checkbox operation buttons so they work better in mobile #2393
 - RSS - Setting to hide muted watches in RSS feed (default ON) (#2411)
 - Fetching/Requests - Fixing  user agent header overrides per-watch of global settings (#2409)
 - Code - improving unique key fix for history database handler (#2402)
 - UI - 'Mark all viewed' button should not show when all viewed (#2399)
 - Fixing build test - Adding small delay (#2397)
 - Code - Bump eventlet from 0.33.3 to 0.35.2 (#2305)
 - UI - Mobile CSS/layout fix wrapping on empty list text #2393
 - UI - Preview single snapshot - Date and button fixes (#2389)
 - Build - PIL/pillow package not used, probably shouldnt be installed/required (#2382)

0.45.23 / 2024-05-22 00:01:50 +0200:
 - 0.45.23
 - RSS - Only insert feed header if app_rss_token is set (should be only shown in index/overview page) (#2381)
 - Fetcher - Using pyppeteerstealth with puppeteer fetcher (#2203)
 - Fix overflowing text
 - RSS and tags/groups - Fixes use active_tag_uuid, fixes broken RSS link in page html (#2379)
 - Ability to set default User-Agent for either fetching types directly in the UI (#2375)
 - Testing - Fixing JSON test
 - UI - Mobile - quick watch form element fixes
 - UI - CSS - Remove gradient border, it did not add much to the design #2377
 - RSS - Muted watches should not show in RSS feed (#2374 #2304)
 - Notifications -  Fixing truncated notifications when tgram:// or discord:// is used with other notification methods (#2372 #2299)
 - UI - Ability to preview/view single changes by timestamp using keyboard or select box(#1916)
 - Browser Steps - Fixing "goto site" step #2330 #2337 (#2364)
 - Crash on older CPU -  Setting LXML version to any version without the known modern-CPU-only CPU flags (#2365 #2328 )
 - Notifications - Update Apprise notification library to 1.8.0 (#2363 #2324) fixes mailto:// with IP as server endpoint
 - UI - Refactor of the Recheck Time Settings, Added "Use default recheck time" checkbox and refactor/simplify system handling (#2362)
 - UI - Search should scan/search error messages (#2353)
 - UI - 'stats' tab should show what the server-type detected is ( #2348 )
 - Update README.md
 - Notifications - Setting set minimum version for mqtt:// library notifications (#2334 / #2333)

0.45.22 / 2024-05-02 12:09:45 +0200:
 - 0.45.22

0.45.21 / 2024-04-25 22:29:38 +0200:
 - 0.45.21
 - UI - Wrap tag names in solid background to make it easier to read when theres multiple tags
 - UI - Error text on exception should contain the word Exception (#2322)

0.45.20 / 2024-04-18 11:55:46 +0200:
 - 0.45.20
 - Bug fix - further work on  lxml filter extract (#2313 #2312 #2317)

0.45.19 / 2024-04-17 20:01:35 +0200:
 - 0.45.19
 - Bug fix for newer lxml module - module 'lxml.etree' has no attribute '_ElementStringResult' - reimplement _ElementStringResult (#2313 #2312)

0.45.18 / 2024-04-16 18:50:14 +0200:
 - 0.45.18
 - UI - Adding UI notice if watch has group options set (#2311 #2307)
 - dependabot - automatically follow apprise
 - "Send Test Notification" - In "Group" settings form it should not fallback to the system wide notifications when sending a test if nothing is set.
 - "Send Test Notification" - Now provides better feedback and works with the actual values in system settings form
 - Code - Getting ready for newer python versions - packing our own strtobool (#2291)
 - UI - BrowserSteps - Show step screenshot/pic should use absolute URL #2243
 - UI - Remove unique check for URLs entered on the "quick watch add" form ( #2286 #2292 )
 - UI - Improvements to tag/groups page, show number of watches under each group, link group name to list (#2290)
 - "Send Test Notification" button  from watch form edit should respect global settings and tag/group settings ( #2289, #2263 )

0.45.17 / 2024-03-31 16:35:44 +0200:
 - 0.45.17
 - UI - Add helper note
 - UI Text - Adding helper text to VisualSelector to explain what the connection is with the CSS/xPath filters
 - Update contributing documentation for discontinuation of `dev` branch (#2272)
 - Updating pyppeteer-ng (mainly newer pillow release) (#2247)
 - Notifications - Updating apprise version, pinning  mqtt:// to compatible version (#2242)

0.45.16 / 2024-03-08 21:07:08 +0100:
 - 0.45.16
 - Pip build - content fetchers package was missing

0.45.15 / 2024-03-08 19:00:37 +0100:
 - 0.45.15
 - Updating restock detection texts
 - Adding CORS module - Solves Chrome extension API connectivity (#2236)
 - UI - Overview list shortcut button - Ability to reset any previous errors
 - Chrome Extension - Adding link and install information from the API page
 - Chrome Extension - Adding link in README.md to the webstore
 - Chrome Extension - Adding callout to UI
 - Import - Fixed "Include filters" option (fixed typo on select) (#2232)
 - Updating restock detection texts
 - Restock detection - Improving test for restock IN STOCK -> OUT OF STOCK (#2219)
 - Puppeteer - remove debug hook
 - Custom headers fix in Browser Steps and Playwright/Puppeteer fetchers ( #2197 )
 - text_json_diff/fix: Keep an order of filter and remove duplicated filters. 2 (#2178)
 - Fetching - restock detecting and visual selector scraper - Fixes scraping of elements that are not visible
 - BrowserSteps UI - Avoid selecting very large elements that are likely to be the page wrapper
 - Fetching - Puppeteer - Adding more debug/diagnostic information
 - Update stock-not-in-stock.js
 - UI - Sorted alphabetical tag list and list of tags in groups setting (#2205)
 - Code - Remove whitespaces in visual selector elements config
 - Build fix - Pinning package versions and Custom browser endpoints should not have a proxy set (#2204)
 - Update stock-not-in-stock.js
 - Fetching pages - Custom browser endpoints should not have default proxy info added
 - Puppeteer - fixing wait times
 - Puppeteer - more improvements to proxy and authentication
 - Puppeteer - client fixes for proxy and caching (#2181)
 - dependabot - Bump the all group with 1 update (artifact store) (#2180)
 - Puppeteer fetch - fixing exception names
 - Code - Split content fetcher code up (playwright, puppeteer and requests), fix puppeteer direct chrome support (#2169)
 - Alpine linux build - adding JPEG development headers to fix build errors
 - Plawright content fetcher - Fixes for status codes and screenshot info (#2168)
 - Fetching - Prefer to use SockPuppetBrowser (#2163)

0.45.14 / 2024-02-07 12:43:23 +0100:
 - 0.45.14
 - Bug fix -  fix missing default var (#2162/ #2118/ #2122 )
 - Fix - Pinning elementpath xPath filter library to 4.1.5 (#2164)
 - Restock detection - Update stock-not-in-stock.js (NL)
 - New text filter - Sort text alphabetically filter (#2153)
 - Filtering - include_filters in group and watch settings should not duplicate (#2151 #1845)
 - Record notification count and show in [stats] tab (#2150)
 - Restock - Update stock-not-in-stock.js Italian translation (#2149)
 - UI - Show error/warning when trying to compare the same version
 - Fetching - Make an obvious error when using BrowserSteps with the simple text fetcher (#2145)
 - Fix for switching to price-data-follower mode (when page has JSON price data), only needs to be queued once. Re #1565
 - Fetching - Always record `server` software reply headers (will be used in the future) (#2143)
 - Testing - General test workflow improvements (#2144)
 - RSS - Include link to the watched URL in the feed (#2139 #2131 and #327)
 - Notifications - skip empty notification URLs from being processed (#2138)
 - UI - Filters & Triggers - Adding example for keyword matching in a line
 - RSS - Adding performance stats
 - Notification - logging - adding performance information for processing time of notifications #327
 - UI - Adding icon to show which watch has Browser Steps enabled (#2137)
 - Logging - Adding extra debug logging to change detection (#2136)
 - Fetcher -  Improve status_code logging (#2130 #2122)
 - Notifications - Bugfix: Notification format not being set correct (HTML emails being sent as plaintext and other problems) (#2129)
 - Restock tweaks - use a single regex, tidy up height detection (#2125)
 - Notification - Templates - Adding an example of how to use URL encoding with tokens
 - Notification - Templates - Adding an example of how to use |tojson for JSON payloads
 - Build maintenance  - dependabot - Bump the all build helpers (#2121)
 - Enable dependabot for github-actions (#2119)
 - Update docker-compose.yml

0.45.13 / 2024-01-19 10:24:47 +0100:
 - 0.45.13
 - Security update - Adding API token secure check for API endpoint `/api/v1/watch/<uuid>/history` @rozpuszczalny
 - Test - tidy up backup test (#2117)
 - Adding contributors section (#2116)
 - Logging loguru output tweaks (#2112)
 - Support Loguru as a logger (#2036)
 - Update stock-not-in-stock.js texts
 - Test - Adding extra test for HTML output in emails ( #2103 )
 - Update README.md
 - Restock detection - Check all elements for text to get stock status from, only consider elements inside the viewport, only consider elements more than 100px from the top (avoid menu) , trim any text returned (#2040)
 - Notifications - When any in a list of notifications fails, the others should still work (#2106)
 - Browser Steps - Fixing "'Response' object is not subscriptable" where quotes were used in connection URL   - Quote wrapped URL for browserstep url was breaking the connection #1627 #1823 #2099 (#2100)
 - Added OPTIONS HTTP method (#2094)
 - API Docs - Examples should use port 5000 (same as the docker-compose default installation and other documentation)

0.45.12 / 2024-01-05 20:17:14 +0100:
 - 0.45.12
 - 0.45.11
 - Notification fixes - error on mailto:// when no format was specified, fixing default body and title of notifications to respect global settings (#2085)
 - Update README.md
 - Removing heroku support as its no longer free
 - PyPi package build fixes (#2084)
 - Adding PyPi pip package publisher script

0.45.10 / 2024-01-05 14:51:35 +0100:
 - 0.45.10
 - Update README.md - Remove deprecated docker-compose (now docker compose)
 - Browser Steps - General error handling improvements (#2083)
 - Browser Steps - Fix for correct tokens/information in browser step failure notification (#2066)
 - UI - [Send test notification] - Refactor to use all tokens  like a real watch and Notification Body+Title from UI value (#2079)
 - Notifications upgrade - Upgrade to Apprise 1.7.1 - Emojis support, Telegram topics support, Discord support for user and role @ping support.  (#2075)
 - Restock detection - "In stock" should be None/"Not yet checked" by default (#2069)
 - Restock detection - updating texts
 - Fetching - Custom browser on experimental/puppeteer fetcher - Don't switch to custom puppeteer mode if external browser URL is active (#2068)

0.45.9 / 2023-12-20 15:30:58 +0100:
 - 0.45.9
 - Restock detection - Update stock-not-in-stock.js strings (Dutch translations)
 - Testing: Improve application signal handling test coverage (#2052)
 - Update docker-compose.yml
 - Restock detection - Update stock-not-in-stock.js strings (#2032)
 - API - Updating documentation
 - Update README.md
 - API - Ability to add/import bulk list of watches as a line-feed separated list (#2021)
 - Notifications - Fixing support for headers in custom post://, posts:// notifications, ability to include HTTP headers when making custom notifications (#2018)
 - Improve handling of SIGTERM shutdown in containers, remove unnecessary multi-process handler for pip installs, tidy up modules (#2014)
 - UI - Extra Browsers - Adding links and more resources on how to connect a fingerprint/scraping browser

0.45.8.1 / 2023-11-30 20:01:40 +0100:
 - 0.45.8.1
 - PDF Fetcher for change detection - Always use plain requests for PDF because otherwise we cant access the embed PDF in the browser (#2020)
 - UI - Fix - Edit Watch 'Show advanced options' should fire at page load to show you whats possible

0.45.8 / 2023-11-29 10:25:11 +0100:
 - 0.45.8
 - Restock detector - adding more detection strings
 - UI - remove incorrect label
 - UI - "Add new watch" URL at main input box should always grow to match the viewport
 - UI - Tidy-up for advanced settings under watch edit, HTML validation fixes (#2011)
 - UI - 'Request body' section disappears after switching from 'Playwright' to 'System settings default' and back on 'Request' tab - Fixed #1449
 - Browser Steps - Adding validation for "Click X,Y" step
 - API - Make sure the watch "is viewed" attribute is correctly represented in the API output (#2009)
 - Update playwright fetcher library and API calls
 - Testing - Improve PDF text change detection tests (#1992)
 - UI - Clicking the "[Diff]" link should take you to the difference starting at the relative time to when you last viewed the difference page (#1989)
 - Visual Selector - xPath handling misc fixes (#1976)
 - Fix build issue
 - feature: Support XPath2.0 to 3.1 (#1774)
 - New functionanlity - Selectable browser / ability to add extra browser connections (good for using "scraping browsers"/  etc) (#1943)
 - API/UI - Button to regenerate API key (#1975 / #1967)
 - Code refactor for fetchers (#1941)

0.45.7.3 / 2023-11-12 12:05:54 +0100:
 - 0.45.7.3
 - Build - update docker container cache setup

0.45.7.2 / 2023-11-12 00:29:35 +0100:
 - 0.45.7.2
 - UI - Cleanup fonts better display in firefox, request CSS according to version (#1968)
 - Revert "Build - Add piwheels support for ARMv6 and ARMv7 machines (rPi etc) (#1814)" (#1964)

0.45.7.1 / 2023-11-11 20:42:16 +0100:
 - 0.45.7.1
 - Build: python libraries - pinning more libraries (#1962)
 - Build: python libraries - eventlet + dnspython dep problems were fixed (#1963)
 - Pip builder - ignore proxy test data if it exists

0.45.7 / 2023-11-10 17:39:49 +0100:
 - 0.45.7
 - UI - Fixing issue where search box JS interfered with page render when logged out

0.45.6 / 2023-11-10 17:32:21 +0100:
 - 0.45.6
 - UI - Adding support-us widget <3 (#1956)
 - Visual Selector - Small fix, Improving elements fetcher reliability (#1947)
 - Update README.md - Adding import information
 - Upgrade playwright browser library (#1942)
 - Update docker-compose.yml - playwright version should be the same as in the automated tests
 - Import - Improved Wachete Excel XLS import support for "dynamic wachet" (sets correct state of using chrome browser or not) column (#1934)
 - Refactor Excel / wachete import, extend tests (#1931)
 - Build - Upgrading pip packages (#1915)
 - Ability to Import from Wachete XLSX (or any XLSX) - Wachete alternative made easy (#1921)
 - Docker build - upgrade image to "bookworm" debian version - fix glibc mismatch (#1918)
 - Fetcher - experimental puppeteer fetch - dont rewrite the proxy protocol (fixes socks5 bug)
 - Nice format stats (comma sep)
 - Selenium fetcher - Test was on `4.14.1` but documentation was not, change both to `4` (#1912)

0.45.5 / 2023-10-28 20:20:24 +0200:
 - 0.45.5
 - BrowserSteps - Wrong text taken from browser steps  (#1911)

0.45.4 / 2023-10-28 16:48:10 +0200:
 - 0.45.4
 - Code cleanup - Browser Steps
 - Fetching - Browser Step enabled watches should also identify 404/non-200 status situations (#1907)
 - Text Filters - "Extract Text" filter was not being error checked properly when using a RegEx (#1902)
 - Fetching/BrowserSteps - Going to a page was using slightly logic to the main way - make them use the same methods (#1890)
 - UI - "With errors" tag/button should always show the current tag error count
 - Build - Add piwheels support for ARMv6 and ARMv7 machines (rPi etc) (#1814)
 - Upgrade selenium to 4.14.0 (latest) (#1783)
 - UI - Don't show search icon when logged out (#1896)
 - UI - Adding handy "limit to watches with errors" button (#1886)
 - UI - Viewing text differences - Tweaks to "Jump to next change" button
 - UI - BrowserSteps - Show the screenshot of an error if it happened on a step, highlight which step had the error to make it easier to find out why the step didnt work, minor fixes to timeouts(#1883)
 - UI - Visual Selector should be the same page-size as Browser Steps (fit inside the browser viewport)
 - Packaging - Enable jq query for filters package installation for darwin (mac) #1868
 - UI - Adding [stats] tab to watch Edit page (#1880)
 - Bugfix - [Clear history] button was not clearing all metadata (#1881)
 - RSS fetch - RSS field <title> was not rendering as text correctly, added workaround #1879
 - PDF Fetching - Handle when the PDF is given as inline content without a proper mime header (#1875)
 - Notification library - Bump Apprise notification library to 1.6.0 (#1867)
 - RSS Fetching - Handle CDATA (commented out text) in RSS correctly, generally handle RSS better (#1866)
 - UI - Adding mouseover/title to show absolute date/time of a last-change or last-checked date #1860
 - UI - Difference text viewer - fixing jump to new difference on changing word/line/etc style
 - Testing - Improve xPath tests (#1863)
 - UI - Fixing jump to next difference button after refactor
 - UI - Updating proxy tip link
 - UI - Adding watch label/title to [edit] page title (#1858)
 - Documentation - Add note that playwright is not supported on ARM type devices #1856
 - UI - Difference page - added 'title' to each change for nice mouse-over information about when the change occured
 - UI - Difference page - Tweak 'preview' page invite text
 - UI - Ability to select between any difference date ( from / to ) and minor UI cleanup for differences page (#1855)
 - UI - Difference page, make the button to find the preview page for triggers and ignored text easier to find
 - System - No need to run updates on fresh installs (#1854)
 - UI - Proxy configuration helper notes improvements
 - Preview/Difference page - When sharing the preview/difference page, highlight-to-ignore should login should be required (#1852)
 - Fetching - Clarifying how fetchers work with SOCKS5 proxies

0.45.3 / 2023-10-05 12:29:59 +0200:
 - 0.45.3
 - Update README-pip.md
 - Update README.md
 - LD JSON Price followers - Handle incorrectly created LD-JSON price structures better (#1837)
 - Dockerfile/fix: Update builder and runner to Python 3.11 (#1781)
 - Backend - Regular expression / string filtering refactor for Python 3.11 and deprecation warnings since Python 3.6 (#1786)
 - Update README.md
 - UI - BrowserSteps - Browser Steps interface screen should resize relative to the browser
 - BrowserSteps - <input> of type 'number' should use 'enter text in field'
 - Restock detect - bumping texts for restock detection
 - UI - Proxy Scanner tool should also understand when a filter is empty or contains only an image
 - UI + Fetching - Improving helper message when filter contains only an image (adding link to more help)
 - UI + Fetching - Be more helpful when a filter contains no text, suggest ways to deal with images in filters (#1819)
 - Building application - Upgrade test workflows to latest versions (#1817)
 - Page fetching - Fixed possible incorrect browser user-agent header in playwright/puppeteer/browserless fetchers (#1811)
 - UI - Add extra validation help for notification body with Jinja2 markup (#1810)
 - UI - More precise text to describe "current_snapshot" notification token

0.45.2 / 2023-09-22 09:45:55 +0200:
 - 0.45.2
 - Code/Test - Improve testing for creating backups
 - UI - Re-order notification field settings
 - UI - Notifications - Tidyup - Hide the notification tokens but show with a button/link
 - UI - Notifications - Tweak discord help text
 - RSS feeds - Fixing broken links from RSS index in some environments, refactor code (#152, #148, #1684, #1798)
 - UI - "recheck all" button should ignore blank/empty "tag" setting when set
 - Update README.md
 - UI - Fix spelling error
 - UI - Make tgram:// and discord:// examples in notification settings link to how-to pages (#1785)
 - Catch possible crash scenario for listing watches - `date_created` was missing on add (#1787)
 - Ability to select "No proxy" for a watch when you have proxy's configured
 - Updating notification library - Adds support for Pushy, PushDeer, PushMe and Matrix attachment support (screenshots)
 - Update README.md
 - UI - Fixing update for sort by "date created" or "#" in watch overview table ( #1775 )
 - Add 'diff_patch' notification body token - This will allow the diff to be generated in the "unified patch format." (#1765)
 - README/docs: Clarifying xpath version changedetection.io uses (#1773)

0.45.1 / 2023-09-06 12:27:56 +0200:
 - 0.45.1
 - UI - Fixing open/broken HTML which was causing some buttons to not display

0.45 / 2023-09-06 09:46:27 +0200:
 - 0.45
 - Adding Oxylabs proxy recommendation to proxy config page (#1756)
 - Fix - Link in the RSS feed was showing the path twice (when used in reverse proxy)
 - Fix - Regular Expression text in  `ignore` and `trigger` were not processing correctly, also refactored for lower CPU usage (#1747)
 - Fix typo in README.md (#1759)
 - UI - "Test notification" button in "Group Tag" settings page was broken due to missing variable #1753
 - UI - Clicking 'ignore text' when highlighting text should clear the preview text button/area. #1754
 - Update documentation - How to set number of concurrent fetchers

0.44.2 / 2023-08-28 19:01:59 +0200:
 - 0.44.2
 - UI - Ability to highlight text and have it offered as a ignore-text option, really nice easy way to set ignores on changing text (#1746)
 - Update README.md
 - Enable ARMv8 builds (for RaspberryPi and other portable devices) (#1733)
 - Updating in app links
 - Updating URL validation library, ability to block access to simple (no dot) hostnames like "localhost" with BLOCK_SIMPLEHOSTS setting (#1732)
 - Re-enable ARMv6 builds (for Raspberry and other portable devices) (#1724)

0.44.1 / 2023-08-02 08:55:07 +0200:
 - 0.44.1
 - Re-enable ARMv7 builds (for Raspberry and other portable devices)
 - UI - Fixing darkmode switch icon

0.44 / 2023-07-17 18:03:42 +0200:
 - 0.44
 - Updating AppRise notification library, Improved pover, ntfy support, whatsapp updates, Pagertree support, Voip.ms support, Misskey support, plus many fixes and improvements.
 - API - Updating API description for handling a single watch
 - Removing docker build for RaspberryPi (armv6/armv7) for now due to packaging problems
 - Proxy scan improvements - handle custom proxies, dont restart when a scan is already running (#1689)
 - Browser Steps - When cleaning up old screenshots, check the file exists
 - Scan/Recheck proxies - Report filter not found as "OK" but with warning
 - Bug fix - Previously encountered fetch errors were sometimes not being cleared (#1687)
 - New feature - Helper button to trigger a scan/access test of all proxies for a particular watch (#1685)

0.43.2 / 2023-06-30 22:57:05 +0200:
 - 0.43.2
 - Bug - SMTP mailto:// Notification content-type (HTML/Text) fix and add CI tests (#1660)
 - Fix - Watches werent falling back to global default formats correctly when required (#1656)

0.43.1 / 2023-06-27 18:28:18 +0200:
 - 0.43.1
 - Bug fix - Notification settings were not cascading from global -> tags -> watch correctly in some cases (#1654)
 - Bug - Fix watch clone (#1647)
 - UI - Dont allow empty tag names (#1641)

0.43 / 2023-06-21 14:35:08 +0200:
 - 0.43
 - UI - Watch Table - Clicking anywhere on the watch list row table also activates the operations buttons and checkbox
 - UI/Functionality - Ability to manage/apply filters and notifications across tags/groups
 - UI - Fixes to dark mode toggle (#1629)
 - Docker container updates - use specific debian version (libssl1 vs libssl3) (#1630)
 - Code - Adding CI test for search (#1626)

0.42.3 / 2023-06-12 15:28:51 +0200:
 - 0.42.3
 - Bug fix - Fixed crash when deleting watch from UI when watch was already manually deleted from datadir (#1623)
 - README - Update links to new website
 - Fetcher / Parser - Automatically attempt to extract JSON from document when document contains JSON but could be wrapped in HTML (#1593)
 - Test improvement - Also test that custom request headers works with Playwright/Browserless (#1607)
 - Fetching - Be sure that content-type detection works when the headers are a mixed case (#1604)
 - UI/Fetching - Update "Filter not found" message to be more explanatory/helpful (#1602)
 - Restock monitor - Updating texts for tickets available/unavailable restock detection
 - Docs - Update README.md (Changed LXML re:math reference to re:match) (#1594)

0.42.2 / 2023-05-25 16:47:30 +0200:
 - 0.42.2
 - UI - Configurable pager size #1599 #1598
 - Fetcher - Ability to specify headers from a textfile per watch, global or per tag ( https://github.com/dgtlmoon/changedetection.io/wiki/Adding-headers-from-an-external-file )
 - Restock detection - Better reporting when it fails (#1584)
 - Fetcher - Puppeteer experimental fetcher wasn't returning the status-code (#1585)
 - Update README.md

0.42.1 / 2023-05-21 14:20:23 +0200:
 - 0.42.1
 - Fetcher fix - Clear any fetch error when the fetched document was the same (clear any error that occurred between fetching a document that was the same)

0.42 / 2023-05-18 22:10:10 +0200:
 - 0.42
 - UI - "Search List" also works for 'Title' field
 - UI - New "Search List" icon and functionality (#1580)
 - VisualSelector - Add message when first version cannot be found
 - UI - update link to official project page
 - BrowserSteps - Dont highlight elements that are the full page width (body, wrappers etc)
 - BrowserSteps - Support for float seconds (0.5 etc)
 - BrowserSteps - Session keep alive timer countdown fix
 - BrowserSteps - adding setup check
 - BrowserSteps - Refactored to re-use playwright context which should solve some errors
 - BrowserSteps - Be sure to select the most appropriate input/button/a when an input element is wrapped in a <div> or other
 - Fetcher - Experimental fetcher - dont cache embedded data URLs
 - Fetcher - Experimental fetcher improvements (Code TidyUp, Improve tests, revert to old playwright when using BrowserSteps for now) (#1564)
 - BrowserSteps - Include nice big start button SVG
 - BrowserSteps - Remove unreliable method for detecting if the element has a "click" listener and default to click (switch to 'Click X,Y' will return the right co-ords anyway)
 - Puppeteer fetcher, adding disk cache and other fixes (#1563)
 - UI - Adding shortcut list select button for "clear/reset history"
 - Fetcher - Experimental fetcher fixes, now only enabled with 'USE_EXPERIMENTAL_PUPPETEER_FETCH' env var (default off) (#1561)
 - UI - Adding shortcut list select button for "clear/reset history"
 - Element scraper - wrap offset detection in try/catch
 - BrowserSteps - BrowserSteps was not always following proxy information
 - BrowserSteps - remove minor delay
 - Fetcher - playwright/browserless - Use builtin node puppeteer handler in browserless, scales way better, and is faster (#1559)
 - UI - Fix back navigation / browser history (#1556)
 - UI - HTML validation improvements for edit forms (#1553)
 - UI - Various minor HTML validation fixes
 - UI - pagination - use count including tag filter for pagination display
 - UI - Notifications - Adding icon to "Add Email" button
 - UI - Adding pagination to watch list (#1549)
 - UI - Set selected watches as 'viewed' (#1550)
 - UI - Fix missing </span> in watch list when using restock detection
 - UI - Make sort order and type sticky in cookies, ability to sort by watch created time (#1519)
 - Notifications - Send test notification should use system defaults for body and title if not set in watch (#1547 #1503)
 - Adding generic changedetection.io SVG icon #1527
 - Tests - error test - be sure to clear results from other test parts
 - Update README.md
 - Tests - Add test to check that low level fetch errors are cleared on next check
 - Restock alerts - adding extra detection texts
 - Restock monitor - Identify the cases where the product is also definitely in stock (#1489)
 - Automated CI test for ensuring pypi package was built correctly (#1488)

0.41.1 / 2023-03-22 10:40:49 +0100:
 - GitHub container build - 'provenance' was disabled
 - 0.41.1
 - Fix for pip installations

0.41 / 2023-03-21 20:30:21 +0100:
 - 0.41
 - Notifications - Include triggered text token as  `{{triggered_text}}` in notifications, so you can send just the content that matches. (#1485)
 - Notification tokens - add comment that the {{tokens}} can be used in the URLs also
 - Quick add form - adjust font size and rename stock recheck
 - Ability to set which text to process triggers on (added, removed, changed) according to the difference (#1483)
 - Restock / stock / out of stock monitor - bumping detection texts
 - Use brotli for reducing the size of the text snapshots (#1482)
 - Notification screenshots - now PNG only for now to save disk space (no point creating two images) (#1481)
 - New feature - Restock / stock / out of stock monitor option/mode
 - UI - Clone/copy watch - A paused watch should not be checked when copied/cloned #1471.
 - Update README.md
 - Code - Abstract out the diff fetch types to make it easier to integrate new ones (#1467)
 - BrowserSteps - Adding `Goto URL` step
 - Fixing bad linebreak definition `</br>` in notifications and UI (#1465)
 - Notification Improvements - New tokens `{{diff_added}}` and  `{{diff_removed}}`, removed whitespace around `added` and `into`  ( Issue #905 ) (#1454)
 - Update README.md

0.40.3 / 2023-02-28 18:04:58 +0100:
 - Bug - False change alerts - code cleanups Re #962 (#1444)
 - Update README.md
 - Be sure that `process_changedetection_results` is off after PageUnloadable and EmptyReply exceptions from fetcher - Re #962 (#1439)
 - False change alerts fix - Don't reset watch checksum when a fetch error happens, adjust test to not test for fluctuating filter (#1437)
 - Library update - Replace bs4 with beautifulsoup4 (#1433)
 - API - Including `last_changed` timestamp in watch API info (#1436)
 - Update apprise to 1.3.0 (#1430)
 - API documentation - improving example for list watches
 - API documentation - improving example for snapshot history
 - API - Adding current version to 'System Information' endpoint, bumping API docs, Re #1429
 - Further improving API documentation Re #1426
 - Improving API documentation Re #1426
 - Browser Steps - Adding "Wait for text" and "Wait for text in element" Re #1427
 - Re #1382 - UI fix - sorting now works with selected tag
 - Dont rewrite/resave snapshot when its the same data, just bump the history index, saves disk space. (#1414)
 - Fetching - False alerts issue #962 - be sure to avoid triggering changedetection when checksums were the same  (#1410)
 - Deleting a watch now removes the entire watch storage directory (#1408)
 - Use year/date in the backup snapshot zip filename instead of epoch seconds (#1377 #1407)
 - PDF text conversion - fix bug where it detected a site as a PDF file incorrectly Re #1392 #1393
 - Remove unused code (#1394)
 - UI - preview page - Fix bug where playwright/chrome was system default and [preview] didnt show snapshot
 - Adding example docker-compose.yml config to ignore errors from self-signed certs #1389

0.40.2 / 2023-02-03 19:20:13 +0100:
 - 0.40.2
 - Code cleanup - remove unused import
 - UI fix - Fix logic for showing screenshot on diff page (#1379)
 - Re #1365 - Playwright - Browser "Service Workers" should be enabled by default but unset via env var PLAYWRIGHT_SERVICE_WORKERS=block (#1367)
 - New setting to allow passwordless access to your 'diff' page - perfect for sharing your diff page securely, refactored login code (#1357)
 - Security - Possible stored XSS in watch list - Only permit HTTP/HTTP/FTP by default - override with env var `SAFE_PROTOCOL_REGEX` (#1359)
 - Playwright - Removing old bug fix where playwright needed screenshot called twice to make the full screen screenshot be actually fullscreen (#1356)
 - Fetch backend UI default fixes for VisualSelector and BrowserSteps (#1344)
 - Fix fetch UI default fetch backend option icon (#1343)
 - Docker container build - docker container buildx version change causing errors with watchtower and others (#1336)

0.40.1.1 / 2023-01-22 13:03:15 +0100:
 - 0.40.1.1
 - Re #1328 - add `-6` flag to enable IPv6 (#1329)

0.40.1.0 / 2023-01-21 15:38:54 +0100:
 - 0.40.1.0
 - Update README.md
 - Setting docker-compose.yml version to 3.2 so it works with portainer and others #1306 #1144 #1079
 - UI - Fix wrong logic when dealing with webdriver/playwright watch screenshot settings (#1325)
 - Ability for watch to use a more obvious system default fetcher (#1320)
 - Update README.md
 - pip - eventlet doesnt support dnspython >=2.3.0 (Fixes build error)
 - Reliability fix - Remove loop that could cause app to stop checking if data changes (#1313)
 - API - Improvements, support PUT for updating existing watch, set muted state, set paused state, see https://changedetection.io/docs/api_v1/index.html (#1213)
 - Data storage - Don't recreate DB if its corrupt, exit with error cleanly so operator can look into the problem (#1296)
 - UI: Updating queued success message (#1285)
 - README.md - Fix release link (#1277)
 - Notifications: updating apprise (slack notification fixes and others) (#1272)
 - Remove docker-compose version so it works on any modern version #1144 (#1268)
 - Update the docker compose file to any version (#1079) (#1144)
 - IPv6 support for listening on (#1267)
 - Test improvements (#1264)

0.40.0.4 / 2022-12-25 18:25:45 +0100:
 - 0.40.0.4
 - UI - Suggest adding proxy for watch when 403 access denied is reached (#1260)
 - Filters & Notifications - fixed tokens in filter not found notification
 - UI - Fix broken html tags in settings page
 - Proxy Settings in UI - TidyUp BrightData text
 - Ability to configure extra proxies via the UI (#1235)
 - Docker container updates - use Python 3.10, remove unused packages
 - Tidy up list icons a bit (#1250)
 - PDF File change detection - Initial PDF fetcher support with basic text extraction (#1244)
 - Testing - Run test as fully built docker container (#1245)
 - Dark mode - system setting var is not required (its cookie based)

0.40.0.3 / 2022-12-19 12:41:52 +0100:
 - 0.40.0.3
 - Visual Selector - Select smallest/most precise element first, better filtering of zero size elements
 - Fetching - Check the most overdue watch first (#1242)
 - Overview list - Checkbox action "Recheck"
 - Playwright - Better error reporting and re-try fetch on fail once (#1238)
 - Fetching - Always sort the key order of JSON content for less false alerts  (May cause an alert on upgrade, but will be better going forwards) #1219
 - Fetcher + VisualSelector - xPath filter with attribute filter was breaking the element finder
 - Fetcher - CPU usage - Skip processing if the previous checksum and the just fetched one was the same (#925)
 - Playwright+BrowserSteps - Fetch changes - Fetch simply after page starts rendering + delay seconds, disable service workers
 - Improve ARM/rust build comment
 - README.md - Improving JSONPath example for LD+JSON product data

0.40.0.2 / 2022-12-08 22:36:59 +0100:
 - 0.40.0.2
 - Price follower - Dont scan for ldjson data when 'no' was clicked on the suggestion (#1207)
 - Adding missing parts for pip build Re #1206

0.40.0 / 2022-12-08 20:09:42 +0100:
 - 0.40.0
 - VisualSelector - Exclude items that are not interactable or visible
 - Automatically offer to track LD+JSON product price data (#1204)
 - UI - favicon callback no longer needed
 - Test cleanups (#1196)
 - Update runtime.txt (#1198)
 - Dark mode - HTML template tidy up (#1197)
 - UI - watch tags also known as watch tag / label
 - Notification templates - bug in update, was updating the main system instead of the watch notification_title incorrectly
 - Extract data - minor improvement to example
 - Darkmode - Pause/Mute notification colour fix, re #1195
 - Notification - Support for standard API calls post:// posts:// get:// gets:// delete:// deletes:// put:// puts:// (#1194)
 - Notifications - tokens/jinja2 templating (#1184)
 - Dark mode - more colour fixes
 - Test improvement - improving notification error network test
 - Extract text as CSV - Extra validation (#1192)
 - Dark mode - make watch list easier to read when theres 'unviewed' entries
 - New feature - Simple extract data by regex from all historical watch text into CSV (#1191)
 - UI - Cursor over labels should be pointer
 - Dark mode - Make watches with errors easier to read
 - Dark mode - cookie path should be all site
 - Tweaks - adding hover/title to dark mode button
 - UI - Dark Mode (#1187)
 - docker-compose - Add playwright/selenium container dependencies example (#1178)
 - BrowserSteps - Can be shared by the watch share link
 - UI - Make tabs hoverable
 - Favicon multiplatform and path fix/update (#1176)
 - BrowserSteps - Cleanup interface on shutdown
 - BrowserSteps - More work on cleaner shutdowns of browser session
 - BrowserSteps - Forcefully shutdown playwright to prevent any race-conditions waiting for it to shutdown
 - BrowserSteps - Make the UI require an extra step so it doesnt slow down the experience when clicking through the tabs (#1175)
 - BrowserSteps - Use correct mimetype for screenshot update
 - BrowserSteps - Faster screenshot updates and enable gzip compression for all content replies in the UI (#1171)
 - BrowserSteps - Add 'Execute JS' step
 - BrowserSteps - Also try to find clickable div/spans
 - Update README.md
 - Update README.md
 - BrowserSteps - Element finder filter (offpage) should also calculate top scroll offset
 - Visual Selector and BrowserSteps - More accurate element detection when the page auto-scrolls on load Re #1169
 - Extra validation for URLs with template markup (#1166)
 - Browser Steps - adding 'please wait' text while loading
 - Re #1163 psutil missing from pip requirements
 - Update README.md
 - Update README.md
 - VisualSelector & BrowserSteps - Scraper improvements, remove duplicate code
 - Bumping VisualSelector example animation
 - Remove dupe xpath finder prep code
 - Browsersteps 'Beta' label image path fix
 - Configurable "Browser Steps" when Playwright/Chrome is configured  (enter text, scroll, wait for text, click button etc) (#478)
 - Update README.md -  Make docker instructions easier to follow on Windows  (#1158)

0.39.22.1 / 2022-11-22 18:09:25 +0100:
 - 0.39.22.1
 - Notification screenshot/JPEG was not being regenerated correctly (#1149)
 - Re #1148 - Notification screenshot/JPEG was not being regenerated correctly
 - Update README.md
 - Update README.md

0.39.22 / 2022-11-20 16:29:16 +0100:
 - 0.39.22
 - Fix dangling HTML tag from screenshot notification
 - Notification screenshot option should only be available to webdriver/playwright watches, screenshot sent as JPEG to save bandwidth, Simplify the logic around screenshot,  (#1140)
 - Minor test improvements
 - Option to attach screenshot to notification (#1127)
 - VisualFilter - check previously set filters were set before highlighting
 - Add diff view option for JSON compare (comparing the fields defined on each. The order of fields, etc does not matter in this comparison.)
 - Update visual text difference library, add option to ignore whitespace when viewing diff (#1137)
 - Make VisualSelector show first available multiple selector, refactor to make more maintainable (#1132)
 - Make link to notification debug log easier to find (#1130)
 - Bump notification library (#1128)
 - Re #1126 HIDE_REFERER setting had wrong default
 - Test: Re-test under HIDE_REFERER condition, use strtobool so you can use 'False' (#1121)
 - Stability fix related to the new watch check count (#1113)
 - Use deepcopy to stop possible data corruption (#1108)
 - Code- Use dict .get instead of key
 - Adding a check counter to watch fetching (#1099)
 - Update README.md
 - HIDE_REFERER incompatible with password based login, added comment to code #996
 - Update README.md
 - Filters can now accept a list/multiple filters (#1064) #623

0.39.21.1 / 2022-11-02 23:48:10 +0100:
 - 0.39.21.1
 - Playwright extension added back to Dockerfile to resolve conditional fix Alpine (musl) based systems (#1087)

0.39.21 / 2022-11-02 15:12:33 +0100:
 - 0.39.21
 - Disable version check when pytest is running (#1084)
 - Removing unused code (#1070)
 - Docker & python - Jq conditional pip requirements.txt include (Don't install in Windows because theres no Windows library/wheel)
 - Docker & python - Use pip conditional requirements to not install playwright for ARM (unsupported on ARM) (#1067)
 - UI - Make fetch error more readable (#1038)
 - Update README.md
 - Re #1052 - Watch 'open' link should use any dynamic/template info (#1063)
 - Remove accidental files
 - Backups and Snapshots - Data directory now fully portable, (all paths are relative) , refactored backup zip export creation
 - Re #1052 - Dynamic URLs, use variables in the URL (such as the current date, the date in a month, and other logic see https://github.com/dgtlmoon/changedetection.io/wiki/Handling-variables-in-the-watched-URL ) (#1057)
 - API - system info - allow 5 minutes grace before watch is considered 'overdue'
 - API - Adding basic system info/system state API (#1051)
 - Build - Fix syntax in container build test (#1050)
 - Building - Test container build on PR
 - Testing - Use same version of playwright while running tests as in production builds (#1047)
 - update path for validation in the CONTRIBUTING.md (#1046)
 - History index safety check - Be sure that only valid history index lines are read (#1042)
 - Option to Hide the Referer header from monitored websites. (#996)

0.39.20.4 / 2022-10-17 18:36:47 +0200:
 - 0.39.20.4
 - Better cross platform file handling in diff and preview (#1034)

0.39.20.3 / 2022-10-17 17:43:35 +0200:
 - 0.39.20.3
 - Windows - diff file handling improvements (#1031)
 - Also include tests in pip build
 - Update README.md

0.39.20.2 / 2022-10-12 09:53:59 +0200:
 - 0.39.20.2
 - Windows - JQ - Make library optional so it doesnt break Windows pip installs (#1009)
 - Adding test - Test the 'execute JS before changedetection' (#1006)

0.39.20.1 / 2022-10-09 23:05:35 +0200:
 - 0.39.20.1
 - Code - check containers build when Dockerfile or requirements.txt changes (#1005)
 - Adding `make` to Dockerfile build as required by jq for ARM devices
 - Dont use default Requests `user-agent` and `accept` headers in playwright+selenium requests, breaks sites such as united.com. (#1004)

0.39.20 / 2022-10-09 16:13:32 +0200:
 - 0.39.20
 - Adds support for jq JSON path querying engine (#1001)
 - Adding link to BrightData Proxy info (#1003)
 - Remove quotationspage default watch
 - Notification library: Bump apprise to 1.1.0 (signal, opsgenie, pagerduty, bark and mailto fixes, adds support for BulkSMS and SMSEagle) (#1002)
 - Selenium fetcher - screenshot should be taken after 'wait' time, not before #873
 - Upgrade Playwright to 1.26
 - Render Extract Configurable Delay Seconds should also apply after executing any JS #958
 - Re #958 - remove change screensize, should be in 1280x720 default, was causing "Unable to retrieve content because the page is navigating and changing the content." on some sites
 - Tidy up proxies.json logic, adding tests (#955)
 - Update README.md - Include BrightData suggestion
 - Improve Proxy minimum time debug output
 - Default proxy settings fixes
 - Use proxies.json instead of proxies.txt - see wiki Proxies section (#945)
 - Upgrade Playwright to 1.25
 - Update README.md

0.39.19.1 / 2022-09-11 09:23:43 +0200:
 - 0.39.19.1
 - Notification - code tidyup
 - Watch list & notification - Adding extra list batch operations for Mute, Unmute, Reset-to-default
 - Notification - Reset defaults button should be on edit page only
 - Notification watch settings - add button to make watch use defaults (empties the settings)
 - Notification system update - set watch to use defaults if it is the same as the default
 - Fix typo (#924)

0.39.19 / 2022-09-08 20:16:35 +0200:
 - 0.39.19
 - Update README.md
 - Tweaks to python PIP readme
 - Use play and pause separate icons (#919)
 - Further notification settings refinement (#910)
 - Reliability improvement - Check watch UUID exists when reporting missing path (#915)
 - repair pip readme
 - Test improvement - Visual selector data loads as JSON (#895)
 - Cleaner separation of watch/global notification settings (#894)
 - Code maintenance - Removing old function (#875)
 - Show screenshot age in [preview]
 - Update README.md
 - Update README.md
 - Update README.md
 - Update bug_report.md
 - Update bug_report.md
 - Update README.md

0.39.18 / 2022-08-19 11:37:26 +0200:
 - 0.39.18
 - More data saving pre-checks (#863)
 - Update screenshot
 - Checkbox operations - reorder buttons for safety
 - UI feature - Basic checkbox/group operations (#861)
 - Bug fix - automatically queued watch checks weren't always being processed sequentially
 - Playwright - Support proxy auth mechanisms (#859)
 - Update README.md
 - Update README.md
 - Skip processing when watch was deleted
 - Playwright fetcher didn't report low level HTTP errors correctly (like Connection Refused) (#852)
 - Be sure visual-selector data is set when xPath/CSS filter is not yet found (#851)
 - Visual selector data not being saved by refactor
 - 'Save chrome screenshot' checkbox never used, removing, we always save the screenshot. (#844)
 - Crash fix: Data store sub-directories werent always being created when needed (#842)
 - Make the table header easier to understand when sorting (#840)
 - Column sorting (#838)
 - Update README.md
 - Revert "don't process paused entries after queue", so we can still manually recheck a paused watch
 - Remove 'last-changed' from url-watches.json and always calculate from history index (#835)
 - Massive improvements to error handling - show separate output for non HTTP 200 status replies
 - Execute JS should happen after waiting seconds
 - Upgrade playwright python driver (#834)
 - Crash protection - handle the case where watch was deleted while being checked (#833)
 - Don't process a watch if it was paused after being queued (#825)
 - Notification Library Update (fixes for Home Assistant) - update requirements.txt (#818)
 - Remove social links for now

0.39.17.2 / 2022-08-05 15:53:09 +0200:
 - 0.39.17.2
 - Test fix - Remove debug from test
 - Security update -  Password could be unset from settings form unexpectedly (#808)
 - Disable SIGCHLD Handler for now - keeping SIGTERM for DB writes
 - Handle SIGTERM for cleaner shutdowns (#737)
 - Remove [save & preview] button, the preview is not updated live so it can lead to confusion (#801)
 - Feature - priority queue - edited and added watches should get checked before automatically queued watches (#799)
 - [preview current] cleanup code and add test
 - Feature - mute notifications (#791)
 - Test improvement - remove unnecessary step

0.39.17.1 / 2022-07-29 10:13:29 +0200:
 - 0.39.17.1
 - Bug fix: Filter failure detection notification was interfering with change-detection results, added test case (#786)
 - README.md - new Discord invite link

0.39.17 / 2022-07-28 13:07:51 +0200:
 - 0.39.17
 - Add https://discord.com/api notification hook to the automatic truncation due to Discords 2000 char limit
 - UI Feature - Add watch in "paused" state, saving then unpauses (#779)
 - Enhancement - support xPath text() function filter, for example "//title/text()" in RSS feeds (#778)
 - Bug fix - Filter "Only trigger when new lines appear" should check all history, not only the first item (#777)
 - Visual Selector direct element finder fix
 - Update README.md
 - Update README.md links
 - Filter failure notification send default enable now controlled by setting Env var
 - Refactor of extract text filter - Regex, support Regex (groups) and all python regex flags via /something/aiLmsux (#773)
 - Update README.md - adding LinkedIn link
 - Update README.md - Adding Discord and YouTube links
 - Bug fix for alerting when xPath based filters are no longer present (#772)
 - Send notification when CSS/xPath filter is missing after more than 6 (configurable) attempts (#771)
 - mailto plaintext handling fix for 'plaintext' apprise integration
 - Minor code cleanups
 - Notifications - email - Correctly send plaintext notification email with plaintext header (#767)
 - Form text tweak - Regex clarification (#766)
 - Update README.md
 - Handle simple obfuscations - HomeDepot.com style price obfuscation (#764)
 - Fixing docker-compose.yml PLAYWRIGHT_DRIVER_URL example URL
 - Notifications fix - Discord - added discord webhook base url to truncation rules (#753)
 - Update Playwright URI Env example with stealth setting and CORS workaround (more reliable fetching)
 - remove extra file
 - removing package-lock.json - not required to be in git
 - Share-icon cleanups
 - Test improvement: Extract text should return all matches
 - Bug fix: RSS Feed should also announce utf-8 charset
 - Regex extract filter: Return all regex results instead of first match (#730)
 - Ability to specify JS before running change-detection (#744)
 - Playwright - log console errors to output
 - UI Improvement - Clarifying "Visual Filter" tool as "Visual Selector Filter"
 - Use environment variables to override new watch settings defaults (user-agent, timeout, workers) (#742)
 - Update docker-compose.yml  - Remove duplicate environment variables from playwright-chrome sample config in docker-compose.yml (#738)

0.39.16 / 2022-07-05 16:14:57 +0200:
 - 0.39.16
 - Fix notification apprise application name to changedetection.io #731
 - Update README.md
 - [new filter] Filter option - Trigger only when NEW content (lines) are detected ( compared to earlier text snapshots ) (#685)
 - Playwright - Use HTTP Request Headers override (Cookie, etc)
 - lang: prefer 'clear (snap) history' to 'scrub' (#721)
 - Minor diff page improvements - list should be sorted 'newest first' and no need to include the current version to compare against (#716)
 - bug fix: `last_changed` was being set on the first fetch, should only be set on the change after the first fetch #705
 - Update README.md
 - Improve docker-compose.yml browserless docker container example, add env var for STEALTH and BLOCK_ADS (#701)
 - New filter - Block change-detection if text matches - for example, block change-detection while the text "out of stock" is on the page, know when the text is no longer on the page (#698)
 - Docker containers - :latest is now stable release, :dev is now master/nightly
 - Trigger filters improvement- it's possible some changes weren't getting detected because the previous checksum only recorded when an event occurred (#697)
 - Some changes werent getting triggered because the previous checksum only recorded when an event occured
 - Notifications regression bug in 0.39.15 - only sent the first notification URL
 - Playwright screenshots - no need for high-res "bug workaround" screenshot, use lower quality/faster configurable image quality env var
 - Adding extra check when updating DB on ReplyWithContentButNoText
 - Notifications log - log what was sent after applying all cleanups
 - Re #555 - tgram:// notifications - strip added HTML tag which is not supported by Telegram
 - Give more helpful error message when a page doesnt load
 - Tweaks to playwright fetch code - better timeout handling
 - Re #580 - New functionality - Random "jitter" delay to requests (#681)

0.39.15 / 2022-06-12 14:05:34 +0200:
 - 0.39.15
 - Watch overview list - adding spinner to make it easier to see whats currently being 'Checked'
 - Preview section - add helpful check
 - Send test notification - improved handling of errors
 - Notification log - also log normal requests and make the log easier to find
 - Update bug_report.md
 - Use correct RSS CDATA handling (#662)
 - Improve logging (#671)
 - New [scrub] button when editing a watch - scrub single watch history (#672)
 - Diff + Preview - Hide date selector widget when viewing screenshots as its not yet possible to compare screenshots (but will be soon!)
 - Diff + Preview - Fixing screenshot behaviour after preference change
 - Screenshot handling on the diff/preview section refactor (#630)
 - Shared watches - include "Extract text" filter
 - Improve error message when filter not found in page result (#666)
 - "Extract text" filter - improve placeholder example
 - Visual selector - 'clear selection' button should clear the filter also
 - New feature - "Extract text" filter ability (#624)
 - Fixing RSS feed HTML content formatting (#662)
 - Update notification library - Improving telegram support
 - 'Mark all viewed' button was missing in this version, added test also. (#652)
 - Content fetcher - Handle when a page doesnt load properly
 - Playwright - Correctly close browser context/sessions on exceptions
 - Move history data to a textfile, improves memory handling (#638)
 - Update feature_request.md
 - Remove UK Covid news
 - Visual Selector fix: Firefox compatibility - Visual Selector (#646)
 - Remove group tag arbitrary length limit (#645)
 - Distill.io import bug fix when no tags assigned to a watch (#557)
 - Ignore whitespace on by default
 - Visual Selector - clear events when changing tabs
 - Minor code cleanup
 - Re #616 - content trigger - adding extra test (#620)
 - README.md update Visual Selector tool - tidy up screenshots, improve text
 - Playwright - ByPass CSP for more reliable JS scraping, disable accept downloads
 - VisualSelector - Better handling of filter targets that are no longer available in the HTML
 - Update bug_report.md
 - 0.39.14.1

0.39.14.1 / 2022-05-24 00:21:30 +0200:
 - 0.39.14.1
 - pip build fix - include API module
 - Visual Selector - be more resilient when sites interfere with the xPath scraping
 - Adding new Visual Selector for choosing the area of the webpage to monitor - playwright/browserless only (#566)

0.39.14 / 2022-05-23 14:40:26 +0200:
 - 0.39.14
 - Fix encoding errors with XPath filters from UTF-8 responses (#619)
 - API Interface (#617)
 - Add note that changedetection is not performed on the screenshot just yet (WIP https://github.com/dgtlmoon/changedetection.io/pull/419 )
 - Fixing edit template HTML
 - Proxy settings on watch should have a "[ ] default" option (#610)
 - Input field tidyup (#611)
 - Update wiki link for 'More info' about sharing a watch and its configuration
 - Option to control if pages with no renderable content are a change (example: JS webapps that dont render any text sometimes) (#608)
 - Playwright - raise EmptyReply on empty reply, no need to process further
 - Re #214 - configurable wait extra seconds for webdriver requests before extracting text (#606)
 - Fix PLAYWRIGHT_DRIVER_URL default value (cf. #587) (#599)
 - Update PIP readme.md

0.39.13.1 / 2022-05-10 22:45:08 +0200:
 - Fixing Pip install problem - Update MANIFEST to include model/ subdir, improving imports (#593)

0.39.13 / 2022-05-10 17:24:38 +0200:
 - 0.39.13
 - Distill.io JSON export file importer (#592)
 - Ability to specify a list of proxies to choose from, always using the first one by default, See wiki (#591)
 - Improving Playwright docs (#588)
 - Playwright - code fix
 - Playwright fetcher - more reliable by just waiting arbitrary seconds after the last network IO
 - Make proxy configuration more consistent - see https://github.com/dgtlmoon/changedetection.io/wiki/Proxy-configuration (#585)
 - Playwright fetcher - use the correct default User-Agent
 - Toggle visibility of extra requests options/settings when not in use (#584)
 - Add new fetch method: Playwright Chromium (Selenium/WebDriver alternative)  (#489)
 - Simplify scrub operation (simply cleans all) (#575)
 - Bugfix - dont update record when deleted during check
 - Improving support info in README.md
 - Handle deletions better (#570)
 - Data storage bug fix #569
 - Upgrade notifications library - fixing marketup in email subject
 - Ability to 'Share' a watch by a generated link, this will include all filters and triggers - see Wiki (#563)
 - Upgrade notifications library Re #555 - fixing telegram HTML markup in notification title
 - Unify MINIMUM_SECONDS_RECHECK_TIME env var variable to 60 seconds
 - Seconds/minutes/hours/days between checks form field upgrade from 'minutes' only (#512)
 - Form styling improvements
 - Form field handling improvements - fixing field list handler for empty lines
 - Fix "Add email" button in main global notification settings
 - Test notification button fixed in main settings (#556)
 - tgram:// be sure total notification size is always under their 4096 size limit
 - Shows which items are already in the queue, disables adding to the queue if already in the recheck queue (#552)
 - Notifications - Signal API support, Ntfy support, hotmail, matrix, Gotify API fixes
 - Discord:// notification size limit - also includes the notification title
 - Fix spelling errors
 - Update README.md
 - Update README.md
 - Import speed improvements, and adding an import URL batch size of 5,000 to stop accidental CPU overload (#549)
 - Ability to set the default fetch mode via the DEFAULT_FETCH_BACKEND variable
 - Refactor form handling (#548)
 - Adding support for change detection of HTML source-code via "source:https://website.com" prefix (#540)
 - Re-label the quick-add widget placeholder 'tag' to 'watch group'
 - HTTP Fetcher code improvements
 - Adding RSS metadata auto-discovery
 - Upgrade WTforms form handler to v3 (#523)

0.39.12 / 2022-04-09 14:16:30 +0200:
 - 0.39.12
 - Miscellaneous settings form visual improvements (#535)
 - Option to render links as [Some Text ](/link), adds the ability to change-detect on hyperlink changes
 - Specify our Discord avatar_url as default avatar_url
 - Minor git updates
 - Fix screenshot tab name
 - Discord:// notifications should be cut to 2000 chars or Discord will not process them. (#531 + #323)
 - Make long reports in the notification error log easier to read
 - [Add email] button in notification settings with a prefix set from NOTIFICATION_MAIL_BUTTON_PREFIX env variable when defined. (#528)
 - Update README.md
 - Skip processing a watch into the RSS feed if there's not enough data to examine (fixes Internal Server Error when accessing the RSS feed) (#521)
 - Introduce an AJAX button for sending test notifications instead of the checkbox (#519)
 - Make text tab always available at default
 - When fetching a snapshot via Chrome, make the most recent screenshot available on the Diff and Preview pages (#516)
 - Remove 'unviewed' status in watch table when Diff link clicked (#514)
 - RSS feed CDATA should contain difference output
 - Fix - {diff} and {diff_full} notifications tokens were not always including the full output
 - Update README.md
 - Update README.md
 - Minor UI cleanups (mobile tabs, font sizing) (#503)
 - Fix typo in Filters & Triggers settings. (#495)
 - Add autofocus attribute to password login field (#496)

0.39.11 / 2022-03-23 09:42:51 +0100:
 - 0.39.11
 - Microsoft Windows installation fixes (#492)
 - GitHub tweak - container tags should be CSV list (Fix ghcr.io not building)
 - GitHub tweak - build containers also on push to master
 - Allow changedetector to ignore status codes as a per-site setting (#479) (#485)
 - Security update - Use CSRF token protection for forms, make "remove password" use HTTP Post (#484)
 - Security update - Protect against file:/// type access by webdriver/chrome. (#483)
 - Only build container on GitHub releases, not tests
 - Also change container names to help stop some DNS issues
 - Detect byte-encoding when the server mishandles the content-type header reply (#472)
 - Improving form/edit example markup
 - JSON diff/preview should use utf-8 encoding where possible (#465)
 - Fix typo in settings form
 - Add python venv to .gitignore

0.39.10 / 2022-03-12 17:28:30 +0100:
 - 0.39.10
 - Add filter to remove elements by CSS rule from HTML before change detection is run (#445)
 - Minor updates to filters form text
 - Re #448 - Dont use changedetection.io as the container name and hostname, fix problems fetching from the real changedetection.io webserver :)
 - Testing - Refactor HTTP Request Type test (#453)
 - Make table header font size the same as content
 - Adjust background colours
 - Handle the case where the visitor is already logged-in and tries to login again (#447)
 - Make the Request Override settings easier to understand
 - Minor tweak to notification token table
 - Style tweak to watch form
 - Login form style fixes
 - Upgrade apprise notification engine to 0.9.7 (important telegram fixes)
 - Remove pytest from production release pip requirements
 - Style fix for background image relative to X-Forwarded-Prefix when running via reverse proxy subdirectory
 - Re-arranging primary links so the important ones are easier to find on mobile
 - Set authentication cookie path relative to X-Forwarded-Prefix when running via reverse proxy subdirectory (#446)
 - Upgrade inscriptis HTML converter to version 2.2~ (#434)
 - Better text/plain detection and refactor tests (#443)
 - Tweak support tabs and text (#440)
 - Include link to changedetection.io hosted option (#439)
 -  Improved CPU usage around the loop responsible for what sites needs to be checked
 - Update README.md with hosting options

0.39.9 / 2022-02-24 17:02:50 +0100:
 - 0.39.9
 - Minor reliability upgrade for large datasets - retry deepcopy (#436)
 - "Recheck" button should work when entry is in paused state
 - Better file exception handling on saving index JSON
 - Fix small issue in highlight trigger/ignore preview page with setting the background colours, add test
 - Ensure string matching on the ignore filter is always case-INsensitive
 - Ability to visualise trigger and filter rules against the current snapshot on the preview page
 - Update README.md
 - XPath RegularExpression support
 - better checking of JSON type
 - Make system level errors from the HTTP fetchers easier to find (#421)
 - Bump node-sass from 6.0.1 to 7.0.0 in /changedetectionio/static/styles (#415)
 - Dont allow redirect on login, it's safer and more reliable this way (#414)
 - When using Env. FETCH_WORKERS or WEBDRIVER_DELAY_BEFORE_CONTENT_READY , it should be type int

0.39.8 / 2022-02-08 18:56:10 +0100:
 - 0.39.8
 - Number of fetching workers can be overriden by Env "FETCH_WORKERS" (#413)
 - Adding Env var "WEBDRIVER_DELAY_BEFORE_CONTENT_READY" to wait n seconds before extracting the text from the browser
 - Language fix "watches are rechecking." it actually puts them into an internal queue "watches are QUEUED for rechecking"
 - Use flask url_for() for webdriver chrome icon instead of relative path
 - Fix typo in the startup create-directory command suggestion (#405)
 - Introduce -h option to allow listening not on 0.0.0.0. (#406)
 - Refactor tests for notification error log handler (#404)
 - Notification error log handler (#403)
 - Add notification note - tgram:// bots cant send messages to other bots, so you should specify chat ID of non-bot user.
 - fixed the reference to wiki for rpi section (#402)
 - /preview format doesnt need <pre> - fixing too many returnlines in content on diff/preview page
 - Update README.md
 - Update README - Fix docker section
 - Update README - Tidy up sections
 - Offer instance on Lemonade Tidy README
 - Ability to use a generated salted password in deployments as env var SALTED_PASS (#397)
 - #323 Adding note about discord:// 2000 char limit (#392)
 - plaintext mime type fix - Don't attempt to extract HTML content from plaintext, this will remove lines and break changedetection (#391)
 - .add_watch() can accept empty tag Use https://changedetection.io/CHANGELOG.txt as a nice default page to watch
 - Add option for tags on import (#377)
 - Update CONTRIBUTING.md
 - Update README.md
 - Fix bug where diff and diff_full were switched in notification templates. (#380)
 - Closes #378

0.39.7 / 2022-01-15 23:21:06 +0100:
 - 0.39.7
 - Scrub watch snapshot fixes
 - Simple HTTP auth (#372)
 - Adding note about JS pages
 - Notification settings defaults and validation (#361)
 - Filters settings helper text tidy-up
 - Add test for low-level network error text handling
 - Add API endpoint for current snapshot (#359)
 - Clarify notice/messages around changing ignore text

0.39.6 / 2022-01-05 19:13:42 +0100:
 - 0.39.6
 - Heroku tweaks (backup download) (#356)
 - XPath support (#355)
 - Better handling of EmptyReply exception, always bump 'last_checked' in the case of an error (#354)
 - Adding note in comments for working arm64 chrome with rPi-4 (#336)
 - fix typo in README.md (#350)
 - Re #348 - Add test for backup, use proper datastore path
 - Update README.md
 - Be sure that documents returned with a application/json header are not parsed with inscriptis (#337)
 - Re #340 - snapshot should not be modified by ignore text (#344)
 - Re #133 Option for ignoring whitespacing (#345)
 - Re #342 notification encoding (#343)
 - Update README.md
 - Adding global ignore text (#339)
 - Adding new proxyType to selenium mappings
 - Use selenium 4.1.0
 - Bumping selenium version re https://github.com/dgtlmoon/changedetection.io/pull/331#issuecomment-1003323594
 - Add socksVersion mapping (#331)
 - Fix broken RSS link fields
 - RSS Link links you back to the difference UI/JS page, RSS Description is the page you're watching, and RSS Title is the page you're watching
 - Unify Filters and Triggers tabs into a single tab
 - Move 'request type' field to the new 'Requests' tab
 - Aligning call signatures #325
 - Extend Request Parameters to add Body & Method (#325)
 - Update README.md
 - Create CONTRIBUTING.md
 - Update README.md
 - Re #267 - Pass settings for the proxy setup for webdriver (#326)
 - Update README.md
 - Update README.md
 - Update README.md

0.39.5 / 2021-12-27 23:46:29 +0100:
 - 0.39.5
 - Update feature_request.md
 - Update issue templates
 - Update bug_report.md
 - Update issue templates
 - W3C HTML validation issue around RSS icon
 - Closes #323 adds link to wiki
 - Update README.md
 - Update README.md
 - improve theming docs
 - Update README.md
 - Update README.md
 - Closes #315 - Include library apprise Notify_mqtt
 - Re #80, sets SECLEVEL=1 in openssl.conf to allow monitoring sites with weak/old cipher suites (#312)
 - Go back to docker hub
 - RSS allow access via token (#310)
 - Adding deploy to Heroku button
 - Adding heroku app.json app
 - Tweak runtime Heroku version
 - Tweaking heroku Procfile
 - Adjust buildpacks on Heroku
 - Adding heroku python3 runtime config
 - Try simpler heroku recipe
 - -C option to create a datadir if it doesnt exist
 - Re #308 - Adding test and including settings in clone operation (#309)
 - fixing too small font in diff UI (#260)
 - Update README.md
 - Send diff in notifications (#296)
 - Fix scrub form theme
 - Scrub dates: Fix date regex limit handler parsing
 - Wait 60 seconds or until stop_thread is set
 - Check that a notification URL is set when sending the test notification (#300)
 - Flask 2 (#299)
 - Re #269 - Show current/correct BASE_URL information (#271)
 - Re #269 - Fix env var comment name
 - Enable Markdown and HTML notifications. (#288)

0.39.4 / 2021-12-02 22:54:38 +0100:
 - 0.39.4 release
 - Re #286 - Solving lost data/corrupted data - Tweak timing and try to write to a temp file first (#292)
 - Fix element paths when using reverse proxy subfolder (#272)

0.39.3 / 2021-10-28 11:32:33 +0200:
 - 0.39.3 release
 - Re #264 - fixing clone watch operation
 - Re #265 - extended jsonpath support (#266)
 - Re #265 - wasnt catching the jsonpath exception due to invalid jsonpath expressions properly
 - Re #257 - Handle bool val of json path better (#263)
 - Re #249 - Add EXPOSE 5000 to Dockerfile
 - Provide better combination of chardet and urllib3
 - Prefer GHCR.io over DockerHub (#245)
 - Limit branches/tags of container build
 - Re #213 - Adding screensize examples to selenium container
 - Be more specific about tagged release builds
 - Fix :latest release worflow syntax check
 - Form helper - explain where the webdriver setting comes from
 - Rename workflow name
 - Just 'published' and 'edited' package release is enough (remove 'created')

0.39.2 / 2021-10-06 08:49:33 +0200:
 - Fixing workflow tag syntax issues
 - fix broken workflow syntax
 - add step for metadata debug, see if it runs by checking workflow tag name
 - Container build/push doesnt need to be so specific
 - Oops on/release was in the wrong block
 - release also on edited, published
 - Run workflow on release
 - Use a better switch mechanism for build type
 - version 0.39.2
 - Configurable BASE_URL (#228)
 - Split python pip builder to its own release based workflow
 - remove accidental syntax add
 - Re #242 - app was treating notification field defaults as the field value (#244)
 - attempt to re-enable docker layer cache
 - Forgot GHCR tag with version
 - Limit container build to releases and master
 - Fix GHCR login
 - Use the same workflow for tag and release
 - Drop redundant build workflow
 - try :latest and :tag in same workflow run
 - Separate workflows
 - Docker image build issues (#243)
 - Re #239 - Individual GUID for watch+changeevent (#241)
 - Update README.md
 - Re #232 - Use a copy of the datastore incase it changes while we iterate through it (#234)
 - Setting for Extract <title> as title option on individual watches (#229)
 - GitHub repo build platforms: linux/amd64,linux/arm64,linux/arm/v6,linux/arm/v7
 - GitHub container repo (#227)
 - Remove extra build step
 - push github container master also
 - Tidy up workflow names
 - Attempt to setup GitHub Container Registry

0.39.1 / 2021-09-17 18:40:16 +0200:
 - v0.39.1
 - Re #185 - [feature] Custom notifications templates per watch (#226)
 - Bump tar from 6.1.6 to 6.1.9 in /changedetectionio/static/styles (#209)
 - Re #225 - Notifications refactor token replacement fix possible missing value for watch_title
 - Re #42 - Notifications refactor token replacement fix possible missing value for watch_title
 - Bump tar from 6.1.6 to 6.1.9 in /changedetectionio/static/styles (#209)
 - Adds 'Create Copy' feature to clone a watch (#184)
 - adding specific test (#205)
 - New notification tokens - watch_uuid, watch_title, watch_tag, (#201)
 - Re #203 - validate tokens (#204)
 - No point hiding the notifications customisation area because it's now in its own tab
 - Update README.md
 - Test - prove that notifications are not being sent when content does not change
 - remove quotes from env vars
 - Re https://github.com/dgtlmoon/changedetection.io/discussions/189 A note to not use quotes in env parts
 - WebDriver fetcher - settings - when an alternative one is configured, show it in the label
 - Update README.md

0.39 / 2021-08-16 15:24:37 +0200:
 - Installation via pip (#186)
 - Update README.md
 - Trigger text/wait (#187)
 - Reword group tag - more obvious name
 - Fix img alt/title accesibility for pause icon
 - Let the fetcher throw an exception which will be caught and handed to the operator anyway
 - Example placeholder was pushed out
 - Move fetcher tab back to general - save space on mobile
 - WebDriver test fetch should use environment var too
 - Add fetch option to each watch
 - Chrome/Webdriver support for Javascript websites (#114)
 - Fixing tar npm security issue npm install  "tar@>=6.1.2"

0.38.2 / 2021-08-07 14:18:28 +0200:
 - tag 0.38.2
 - Re #172 - be sure that we are non-greedy matching the first : when splitting the headers so we dont break "Cookie" header (#175)
 - Update heroku.yml
 - Re #156 - PORT should always be an Integer
 - Re #159 - Adding env var example to docker-config.yml
 - Add Heroku Deployment Support (#159)
 - Re #154 - Handle missing JSON better
 - high res
 - higher res screenshot
 - Update screenshot
 - Assert that html_tools.JSONNotFound is correctly raised
 - Re #154 Ldjson extract parse (#158)
 - Responsive fix for input field on mobile
 - Re #148 - Always set something for {base_url} so we dont send possibly an empty body/title notification which could break some services.
 - Add medium-size-desktop class to notification custom title
 - Notification default: Make sure to use atleast some text here, a blank notification body could be problematic for some services
 - Re #150 - stop using 'size' across all elements and rely on CSS for a better mobile experience (stops fields from pushing out)
 - fix: setting overflow in mobile view (#150)
 - Re #121, #123 - Show the current base_url value
 - Re #149 - allow empty timestamp limit for scrub operation
 - Dont show "new version available" message when password is enabled and user is logged out
 - test fix - dont trigger notifications in header test
 - Strengthen the notification tests
 - Re #137 - Adding test to confirm that headers are not repeated
 - Add debug output to notify loop
 - Add note to field
 - Cleanup test helper data before and after running
 - Improve debug info

0.38.1 / 2021-07-20 17:57:27 +1000:
 - 0.38.1 tag
 - Re #143 - Remove old notification test code, fix form handler (#145)
 - Update README.md
 - Re #135 - refactor the quick add widget (#136)
 - Partially revert 47e5a7cf0990bc958061ce57de8ae88f3fbd39aa (#138)

0.38 / 2021-07-16 16:24:01 +1000:
 - use a github action for getting the tag
 - rename tag build runner
 - fix tag
 - build and push tag
 - Re #76 - Fixing links
 - Cleaner is to let flexbox overflow and scroll on the X where needed
 - #76 app path prefix when behind proxy_pass (#91)
 - Settings: Remove password link fix
 - Make sure right menu is still visible when URL is long
 - 0.38 release
 - Re #132 - Make a list of the JSONpath results instead of using only the first value
 - Customisable notifications (#123)
 - Re #117 - dont re-encode single value types, looks better in the diff
 - Usability tweak - [edit] on diff page should go back to diff page
 - Update README.md
 - Adding text about JSON API Monitoring
 - Re #117 Jsonpath based JSON change detection filter (#125)
 - Update README.md
 - Update README.md
 - Use right sticky for version
 - Re #118 - Make 'show current version' more obvious
 - Diff page - use the document title in <title> for better bookmarking
 - node-sass 6.0.1 works with node-sass watch way better
 - Updating inscriptis/text/html library to 1.2
 - Update readme with the branch link for javascript support
 - Updating trim-newlines packages

0.37 / 2021-07-02 20:19:26 +1000:
 - 0.37 release
 - #110 global recheck time (#113)
 - Re #106 - handling empty title with gettr cleanup (#107)
 - Update README.md
 - Auto extract html title as title (#102)
 - Bug fix - Check 'minutes_between_check' is set
 - tweak <pre> text wrapping when displaying diff
 - CSS Filter - Smarter is to just extract the HTML blob and continue with inscriptus, so we have almost the same output as not using the filter
 - CSS Filter - restore nicer linefeeds
 - @todo Comment - BS4's element.get_text() seems to lose the indentation format no-matter what
 - CSS Filter - strip text of whitespacing, preserve new lines where applicable, remove extra newlines
 - Include statistics for number of watches
 - Set edit-form for settings+watch to always be wide

0.36 / 2021-06-22 10:33:27 +1000:
 - Update README.md
 - 0.36
 - Re #42 - dont use blank titles
 - Re #100 - Fixing storage of minutes_between_check and adding automated test for field storage

0.35 / 2021-06-22 00:28:41 +1000:
 - 0.35
 - Time between rechecks is always stored as minutes
 - Ability to reset app password by placing a file called removepassword.lock into your data directory and restarting the instance
 - Adding tests for password control handling
 - Remove unused field (removepassword is actually a link)

0.34 / 2021-06-21 22:13:14 +1000:
 - 0.34
 - Be sure not to use blank passwords as the password
 - Re #42 - custom title (#98)
 - Re #92 - Re-use existing [preview] function for viewing current (#97)

0.33 / 2021-06-21 20:07:04 +1000:
 - 0.33
 - #81 - Regex support (#90)
 - Use wtforms handler (#96)
 - Re #95 - Include PUID/PGID example
 - re-enable tests
 - On settings submit, display saved message
 - Use flasks' built in 'flash' method instead of a custom message/notices (#94)
 - Adding rPi support info
 - Re #92 Adding link to CSS selector help in wiki
 - Re #93 - tweak build packages
 - Re #93, #79 - docker image multistage build lost the packages required for rPi etc
 - Strip surrounding whitespace from elements (#89)
 - Queue an entry for immediate recheck after [edit]
 - Adding helper method to remove text files that are not in the index
 - Fix typo
 - Re #88 - placeholder text on CSS rule
 - Re #86 - fix typo

0.32 / 2021-06-15 09:50:24 +1000:
 - 0.32 release
 - Sassify the diff page
 - "Sassify" the theme, easier to manage
 - Mobile fixes (#87)
 - Re #86 - Refactor scrub date limit code
 - Tweak comments
 - Re #77 - Repair and refactor time threshold check code
 - Modifies Dockerfile to use multistage builds (#79)
 - Bumping to 0.31

0.31 / 2021-06-03 10:51:18 +1000:
 - Re #75 - Adding test to confirm watched URL appears in RSS feed
 - CSS selector filter (#73)
 - Fixing var name
 - Include release metadata during github build
 - Update README.md
 - Re #40 Ability to set individual timers (#72)
 - Update README.md
 - Improvements for backup (#70)
 - Update README.md
 - Disable image layer cache service
 - Re-enable ARM v6/v7 builds
 - Install requirements, remove rust and dev packages that are no longer needed, hopefully for a smaller docker layer size
 - Remove rust build comments
 - Arm build fixes (#68)
 - Re #65 - Append BASE_URL env var to the notification if it is set (#66)
 - Update README.md
 - Adding BTC support instructions
 - Switch to just amd64 for now due to apprise not building on ARM
 - Fixing syntax
 - Re #49 Re #60 - Adding more information about proxy setup to README.md
 - Add socks proxy support (#60)
 - Created docker-compose file (#55)
 - Re #58 - reduce to 1 minute (a small rewrite is required to change the backend to store in 'seconds' instead of minutes)
 - 56 - Fix notification test
 - Update README.md
 - Update README.md
 - Adding rust compiler :(
 - trying without libssl and only libffi
 - Adding extra libs required for build
 - Cleanup docs
 - Tweak workflow (tests)

0.30 / 2021-05-08 11:33:46 +1000:
 - Security update
 - Apprise notifications (#43)
 - Fixing security update
 - Also detect pytest in the environ (for local debug)
 - Prepend 'test-' when runnning under pytest to guid
 - - Relabel login button - misc test cleanup
 - Re #46 - Add note to README.md about Javascript support
 - Bumping version
 - Re #45 - Set datastore path in app.config
 - Re #44 - Broke the menu by accident, adding tests and fixing.
 - bump to 0.29

0.29 / 2021-04-30 16:54:07 +1000:
 - docker-compose for dev not needed (use venv etc)
 - Password protection / login support (#34)
 - Update FUNDING.yml
 - Skip using tag limit on pause when no tag is being viewed
 - Pause/Unpause should respect limit tag on redirect
 - Validate duplicate URLs
 - Chdir is not needed because we add the file from the full path, but make it 'relative' in the Zip
 - Fix backup generation on relative paths (like when run outside docker, under venv, etc)
 - Adding noopener per CodeQL, stop pages from knowing the referer etc
 - Create codeql-analysis.yml
 - yarl not needed, lock requests version
 - dev packages needed, drop apt cache
 - See if we get a clean buildx without dev packages
 - Tweaking build size thanks to https://github.com/hadolint/hadolint
 - Adding dockerignore
 - Re #18 - Show "preview" of the page when only one revision exists (#33)
 - Update README.md
 - Update README.md
 - Also check that the watch is not paused before putting it into the checking queuex
 - revert c60be562718d23972d7d43821bb6b87f2add3256
 - remove extra packages (#32)

0.28 / 2021-04-01 14:43:46 +0200:
 - Bumping version to 0.28
 - Docker push amd64 rpi etc (#28)
 - Open [diff] links into their own window
 - Fix auto jump on viewing the diff
 - Re #30 - Delete history watch snapshots (#31)
 - Slow down the DB write interval and catch the case that it changed during write
 - Immediately 'jump' to the change
 - Tweak to hover pause icon
 - Stop runtime error on dict changing during write/init at start (#27)
 - Re #22 - ability to pause
 - Re #23 - always check value of interval time, not just on start
 - Update README.md
 - Use absolute image links so the screenshots work from docker hub
 - Update README.md
 - Updating screenshot
 - Reuse the GUID if we have one

0.27 / 2021-03-01 15:50:25 +0100:
 - Dont show 'empty' tag, it will be in the [ALL] list
 - Adding RSS feed icon
 - Generic object sync should use private method
 - Add missing urllib3
 - Add missing pytz
 - Check for new version
 - Fix import form flow logic
 - Code tidy/lint
 - Tidy up thread logic and version check
 - Add missing dep
 - Remove todos
 - Add icon for RSS, RSS should show only unviewed entries
 - Issue #7 - RSS feeds
 - Always override tag version (load from disk in future, so we can add it at build time)
 - next dev is 0.27
 - Tweak to tests
 - Move logic
 - Remove erroneous extra liveserver setup
 - When new ignore text is specified, reprocess the checksum
 - Adding filter and log output to pytest
 - Fix edit action link
 - Minor lint cleanup
 - Clean up after test case
 - Remove liveserver, doesnt belong here
 - Fix syntax, Triggers the workflow on push or pull request events
 - Activate workflow on all branches
 - Issue #14 - Tweaks to edit, create ignore text, tests for ignore text, integrate ignore text
 - Validation of added headers, should contain key/val (2 parts)
 - Issue #12 include version for easy reference.
 - Bring dev environment inline
 - Tidying up requirements.txt

0.26 / 2021-02-24 09:56:29 +0100:
 - Handle the case of someone supplying a bad link
 - Adding jump to next change diff widget
 - Moving nice screenshot to above the fold :)
 - Adding docker hub badge for tag information

0.25 / 2021-02-22 08:53:04 +0100:
 - Bumping schema tag to 0.25
 - Issue #5 - Remove arbitrary '600' minutes limit
 - Add test delay for github action test
 - Add wait for threads in test
 - Extending tests to cover resetting the diff/unviewed status correctly
 - Tidy up return logic
 - Code tidy
 - Fix docker app files paths
 - Tweaking Dockerfile for new eventlet wrapper
 - Create LICENSE
 - Adding docker pulls counter badge
 - Use master branch for badge
 - Removing unused import
 - Fixing a few more easy lint wins
 - Linting fixups
 - Update README.md
 - Add badge under pytest branch
 - Create python-app.yml
 - Create the test datastore
 - Minor cleanup
 - Just use the current/previous md5
 - Finalse pytest methods
 - Port should be an integer
 - Tweaking client
 - remove unused imports
 - Use session/client fixture
 - Addingmissing files
 - hack of pytest implementation - doesnt work yet
 - Tidy up a few broken datastore paths
 - WIP, separate out the Flask from everything else, get pytest working
 - Make records in the overview that have a difference that have not been viewed in the [diff] tab bold

0.24 / 2021-02-05 18:46:00 +0100:
 - Adding 0.24 tag
 - Avoid accidently using Python's objects that are copied - but land as a 'soft reference', need to use a better dict struct in the future #6
 - Minor fix to 'last changed' field, simplify template and logic
 - Remove debug print

0.23 / 2021-02-04 12:38:48 +0100:
 - Use a thread locker and cleaner separation of concerns between main thread and site status fetch

0.22 / 2021-02-03 22:28:37 +0100:
 - Adding tag to json
 - Adding SEND_FILE_MAX_AGE_DEFAULT to ensure backups etc dont get old
 - Minor fix - load extra stylesheet only once
 - Minor tweaks for development setup
 - Provide named containers and remove all existing
 - Adding new [Scrub All Version History] button under [settings] (But keep your URL list)
 - Flag for immediate sync of index after adding new watch
 - Sometimes it seems .update wasnt thread safe and isnt used here, just add a clean new dict member
 - Adding ARG to Dockerfile
 - Include the triggered build SHA as part of the backup info, when built in docker hub.
 - Add cache busting var to style sheets
 - Slightly more bulletproof instructions
 - Updating screenshot
 - Push newly created watches directly into the update check Queue.
 - Adding checkall
 - Easily download a full backup
 - Show the date/time of the current/most up to date version
 - Use a pool of thread workers, better for huge lists of watchers
 - Code cleanup edit submit handler can be the same function
 - Add update howto
 - Refactor slightly confusing difference build function
 - Version comparison had the wrong order
 - https://github.com/psf/requests/issues/4525 - brotli compression is not yet supported in requests, be sure that users cant accidently use this content type encoding in the headers

0.21 / 2021-02-01 21:56:18 +0100:
 - Include the current URL in the page when viewing the version diff
 - Include a selfcheck/diagnosis routine
 - On manual recheck request, redirect to same tag listing
 - Set default diff type to 'lines', faster for starters.
 - Supply different versions to browse
 - Fix heading
 - Update README.md
 - Adding diff screenshot
 - Add more start-up examples
 - Tweak theming
 - Use a even simpler run command
 - improve the wording
 - Add basic settings page (so far just recheck time in minutes)
 - Updating README
 - Updating screenshot (new diff button)
 - Trigger write index after edit of a watch
 - Add [diff] mechanism
 - Use a single thread for writing the sync json
 - Use existing tag
 - When all items showed, show which tag it belongs to
 - Sort tag list
 - Set active tag selection
 - Support for comma separated tags
 - Tweak styling for 'new watch' form
 - Remove import for old lib
 - Switch to inscriptis prepare config backend struct
 - Support for custom headers per watch
 - Going back to larger PNG screenshot, looks better in Github :)
 - Fix alt text in markup
 - Adding new screenshot binary
 - Updating screenshot
 - Moving start text to a more visible part
 - Tweak messages
 - Change message text
 - Fixing messages styling
 - Basic tag browse buttons
 - Bulk import
 - Tidy up 'last_checked' date handling
 - Dev environment setup
 - Dev docker tweaks
 - Remove messy text
 - Tweaking text
 - Fixing checkall hook
 - Use requests's r.text so we dont have to deal with charsets
 - Add note
 - Fix bad copy command
 - Oops left out the image name

0.12 / 2021-01-29 12:33:42 +0100:
 - Fix build setup for the docker hub image https://hub.docker.com/r/dgtlmoon/changedetection.io
 - Update screenshot

0.11 / 2021-01-29 10:49:05 +0100:
 - Add more start-up examples
 - Tweak theming
 - Use a even simpler run command
 - improve the wording
 - Add basic settings page (so far just recheck time in minutes)
 - Updating README
 - Updating screenshot (new diff button)
 - Trigger write index after edit of a watch
 - Add [diff] mechanism
 - Use a single thread for writing the sync json
 - Use existing tag
 - When all items showed, show which tag it belongs to
 - Sort tag list
 - Set active tag selection
 - Support for comma separated tags
 - Tweak styling for 'new watch' form
 - Remove import for old lib
 - Switch to inscriptis prepare config backend struct
 - Support for custom headers per watch
 - Going back to larger PNG screenshot, looks better in Github :)
 - Fix alt text in markup
 - Adding new screenshot binary
 - Updating screenshot
 - Moving start text to a more visible part
 - Tweak messages
 - Change message text
 - Fixing messages styling
 - Basic tag browse buttons
 - Bulk import
 - Tidy up 'last_checked' date handling
 - Dev environment setup
 - Dev docker tweaks
 - Remove messy text
 - Tweaking text
 - Fixing checkall hook
 - Use requests's r.text so we dont have to deal with charsets
 - Add note
 - Fix bad copy command
 - Oops left out the image name
 - Fix build setup for the docker hub image https://hub.docker.com/r/dgtlmoon/changedetection.io
 - Update screenshot

0.2 / 2021-02-01 10:24:29 +0100:
 - Add more start-up examples
 - Tweak theming
 - Use a even simpler run command
 - improve the wording
 - Add basic settings page (so far just recheck time in minutes)
 - Updating README
 - Updating screenshot (new diff button)
 - Trigger write index after edit of a watch
 - Add [diff] mechanism
 - Use a single thread for writing the sync json
 - Use existing tag
 - When all items showed, show which tag it belongs to
 - Sort tag list
 - Set active tag selection
 - Support for comma separated tags
 - Tweak styling for 'new watch' form
 - Remove import for old lib
 - Switch to inscriptis prepare config backend struct
 - Support for custom headers per watch
 - Going back to larger PNG screenshot, looks better in Github :)
 - Fix alt text in markup
 - Adding new screenshot binary
 - Updating screenshot
 - Moving start text to a more visible part
 - Tweak messages
 - Change message text
 - Fixing messages styling
 - Basic tag browse buttons
 - Bulk import
 - Tidy up 'last_checked' date handling
 - Dev environment setup
 - Dev docker tweaks
 - Remove messy text
 - Tweaking text
 - Fixing checkall hook
 - Use requests's r.text so we dont have to deal with charsets
 - Add note
 - Fix bad copy command
 - Oops left out the image name
 - Fix build setup for the docker hub image https://hub.docker.com/r/dgtlmoon/changedetection.io
 - Update screenshot
 - Add edit UI Move to keyed structure instead of list
 - Fixes to CSS
 - Add method to launch a full recheck of all @note - needs to be converted to a python Queue threads
 - Tweaks to docker layout
 - Remove actual :// links, dont consider these as part of the changes, often they include variables/trackingscript ref etc
 - Create FUNDING.yml

0.1 / 2021-01-28 11:17:12 +0100:
 - Specify image name in docker files to avoid a confusing build/run
 - Tidy up devel docker
 - Tweak comments
 - Avoid recasting the type
 - Store a history of changes, used for future lookup/diff/explore changes UI
 - Update README.md
 - Show the backend error in the table if there is one
 - Include screenshot
 - Fix branch name
 - Tweak todo
 - Adding README amd docker info
 - Add missing file
 - Primitive support for extra headers
 - remove debug
 - Handle titles and links
 - Fix base definition of the watcher
 - sort by last changed
 - fix button size
 - Store the html2text version too
 - fix favicon
 - small fixes
 - Handle errors better, use the plaintext output
 - Workon threads
 - WIP
 - Remove nocache experimental
 - Initial commit

```

---

### changedetection.io API
Original URL: https://changedetection.io/docs/api_v1/

# changedetection.io API

## Manage your changedetection.io watches via API, requires the \`x-api-key\` header which is found in the settings UI.

**0.1.0**

- [Compare all with predecessor](https://changedetection.io/docs/api_v1/#)
- [show up to version:](https://changedetection.io/docs/api_v1/#)
- [0.1.0](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

# Notifications

# Notifications\| Create Notification URLs

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Add one or more notification URLs from the configuration

post

```http
/api/v1/notifications
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Notifications-CreateBatch-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/notifications/batch -H"x-api-key:813031b16330fe25e3780cf0325daa45" -H "Content-Type: application/json" -d '{"notification_urls": ["url1", "url2"]}'
```

## 201

| Field | Type | Description |
| --- | --- | --- |
| notification\_urls | Object\[\] | List of added notification URLs |

## 400

| Name | Type | Description |
| --- | --- | --- |
| Invalid | String | input |

# Notifications\| Delete Notification URLs

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Deletes one or more notification URLs from the configuration

delete

```http
/api/v1/notifications
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Notifications-Delete-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/notifications -X DELETE -H"x-api-key:813031b16330fe25e3780cf0325daa45" -H "Content-Type: application/json" -d '{"notification_urls": ["url1", "url2"]}'
```

## Parameter

| Field | Type | Description |
| --- | --- | --- |
| notification\_urls | String\[\] | The notification URLs to delete. |

## 204

| Field | Type | Description |
| --- | --- | --- |
| OK | String | Deleted |

## 400

| Name | Type | Description |
| --- | --- | --- |
| No | String | matching notification URLs found. |

# Notifications\| Replace Notification URLs

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Replace all notification URLs with the provided list (can be empty)

put

```http
/api/v1/notifications
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Notifications-Replace-0_0_0-0)

```curl
curl -X PUT http://localhost:5000/api/v1/notifications -H"x-api-key:813031b16330fe25e3780cf0325daa45" -H "Content-Type: application/json" -d '{"notification_urls": ["url1", "url2"]}'
```

## 200

| Field | Type | Description |
| --- | --- | --- |
| notification\_urls | Object\[\] | List of current notification URLs |

## 400

| Name | Type | Description |
| --- | --- | --- |
| Invalid | String | input |

# Notifications\| Return Notification URL List

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Return the Notification URL List from the configuration

get

```http
/api/v1/notifications
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Notifications-Get-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/notifications -H"x-api-key:813031b16330fe25e3780cf0325daa45"
HTTP/1.0 200
{
    'notification_urls': ["notification-urls-list"]
}
```

# System Information

# System Information\| Return system info

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Return some info about the current system state

get

```http
/api/v1/systeminfo
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-System_Information-Get_Info-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/systeminfo -H"x-api-key:813031b16330fe25e3780cf0325daa45"
HTTP/1.0 200
{
    'queue_size': 10 ,
    'overdue_watches': ["watch-uuid-list"],
    'uptime': 38344.55,
    'watch_count': 800,
    'version': "0.40.1"
}
```

# Tag

# Tag\| Create a single tag

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

post

```http
/api/v1/watch
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Tag-Create-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/watch -H"x-api-key:813031b16330fe25e3780cf0325daa45" -H "Content-Type: application/json" -d '{"name": "Work related"}'
```

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | Was created |

## 500

| Field | Type | Description |
| --- | --- | --- |
| ERR | String | Some other error |

# Tag\| Delete a tag and remove it from all watches

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

delete

```http
/api/v1/tag/:uuid
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Tag-DeleteTag-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/tag/cc0cfffa-f449-477b-83ea-0caafd1dc091 -X DELETE -H"x-api-key:813031b16330fe25e3780cf0325daa45"
```

## Parameter

| Field | Type | Description |
| --- | --- | --- |
| uuid | uuid | Tag unique ID. |

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | Was deleted |

# Tag\| Single tag - get data or toggle notification muting.

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Retrieve tag information and set notification\_muted status

get

```http
/api/v1/tag/:uuid
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Tag-Tag-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/tag/cc0cfffa-f449-477b-83ea-0caafd1dc091 -H"x-api-key:813031b16330fe25e3780cf0325daa45"
curl "http://localhost:5000/api/v1/tag/cc0cfffa-f449-477b-83ea-0caafd1dc091?muted=muted" -H"x-api-key:813031b16330fe25e3780cf0325daa45"
```

## Parameter

| Field | Type | Description |
| --- | --- | --- |
| uuid | uuid | Tag unique ID. |

## Query Parameter(s)

| Field | Type | Description |
| --- | --- | --- |
| mutedÂ Â <br> optional | String | = `muted` or = `unmuted` , Sets the MUTE NOTIFICATIONS state |

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | When muted operation OR full JSON object of the tag |
| TagJSON | JSON | JSON Full JSON object of the tag |

# Tag\| Update tag information

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Updates an existing tag using JSON

put

```http
/api/v1/tag/:uuid
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Tag-UpdateTag-0_0_0-0)

```curl
Update (PUT)
curl http://localhost:5000/api/v1/tag/cc0cfffa-f449-477b-83ea-0caafd1dc091 -X PUT -H"x-api-key:813031b16330fe25e3780cf0325daa45" -H "Content-Type: application/json" -d '{"title": "New Tag Title"}'
```

## Parameter

| Field | Type | Description |
| --- | --- | --- |
| uuid | uuid | Tag unique ID. |

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | Was updated |

## 500

| Field | Type | Description |
| --- | --- | --- |
| ERR | String | Some other error |

# Tag Management

# Tag Management\| List tags

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Return list of available tags

get

```http
/api/v1/tags
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Tag_Management-ListTags-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/tags -H"x-api-key:813031b16330fe25e3780cf0325daa45"
{
    "cc0cfffa-f449-477b-83ea-0caafd1dc091": {
        "title": "Tech News",
        "notification_muted": false,
        "date_created": 1677103794
    },
    "e6f5fd5c-dbfe-468b-b8f3-f9d6ff5ad69b": {
        "title": "Shopping",
        "notification_muted": true,
        "date_created": 1676662819
    }
}
```

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | JSON dict |

# Watch

# Watch\| Create a single watch

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Requires atleast `url` set, can accept the same structure as [get single watch information](https://changedetection.io/docs/api_v1/#api-Watch-Watch) to create.

post

```http
/api/v1/watch
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Watch-Create-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/watch -H"x-api-key:813031b16330fe25e3780cf0325daa45" -H "Content-Type: application/json" -d '{"url": "https://my-nice.com" , "tag": "nice list"}'
```

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | Was created |

## 500

| Field | Type | Description |
| --- | --- | --- |
| ERR | String | Some other error |

# Watch\| Delete a watch and related history

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

delete

```http
/api/v1/watch/:uuid
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Watch-Delete-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/watch/cc0cfffa-f449-477b-83ea-0caafd1dc091 -X DELETE -H"x-api-key:813031b16330fe25e3780cf0325daa45"
```

## Parameter

| Field | Type | Description |
| --- | --- | --- |
| uuid | uuid | Watch unique ID. |

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | Was deleted |

# Watch\| Import a list of watched URLs

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Accepts a line-feed separated list of URLs to import, additionally with ?tag\_uuids=(tag id), ?tag=(name), ?proxy={key}, ?dedupe=true (default true) one URL per line.

post

```http
/api/v1/import
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Watch-Import-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/import --data-binary @list-of-sites.txt -H"x-api-key:8a111a21bc2f8f1dd9b9353bbd46049a"
```

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | List | List of watch UUIDs added |

## 500

| Field | Type | Description |
| --- | --- | --- |
| ERR | String | Some other error |

# Watch\| Single watch - get data, recheck, pause, mute.

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Retrieve watch information and set muted/paused status

get

```http
/api/v1/watch/:uuid
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Watch-Watch-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/watch/cc0cfffa-f449-477b-83ea-0caafd1dc091  -H"x-api-key:813031b16330fe25e3780cf0325daa45"
curl "http://localhost:5000/api/v1/watch/cc0cfffa-f449-477b-83ea-0caafd1dc091?muted=unmuted"  -H"x-api-key:813031b16330fe25e3780cf0325daa45"
curl "http://localhost:5000/api/v1/watch/cc0cfffa-f449-477b-83ea-0caafd1dc091?paused=unpaused"  -H"x-api-key:813031b16330fe25e3780cf0325daa45"
```

## Parameter

| Field | Type | Description |
| --- | --- | --- |
| uuid | uuid | Watch unique ID. |

## Query Parameter(s)

| Field | Type | Description |
| --- | --- | --- |
| recheckÂ Â <br> optional | Boolean | Recheck this watch `recheck=1` |
| pausedÂ Â <br> optional | String | = `paused` or = `unpaused` , Sets the PAUSED state |
| mutedÂ Â <br> optional | String | = `muted` or = `unmuted` , Sets the MUTE NOTIFICATIONS state |

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | When paused/muted/recheck operation OR full JSON object of the watch |
| WatchJSON | JSON | JSON Full JSON object of the watch |

# Watch\| Update watch information

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Updates an existing watch using JSON, accepts the same structure as returned in [get single watch information](https://changedetection.io/docs/api_v1/#api-Watch-Watch)

put

```http
/api/v1/watch/:uuid
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Watch-Update_a_watch-0_0_0-0)

```curl
Update (PUT)
curl http://localhost:5000/api/v1/watch/cc0cfffa-f449-477b-83ea-0caafd1dc091 -X PUT -H"x-api-key:813031b16330fe25e3780cf0325daa45" -H "Content-Type: application/json" -d '{"url": "https://my-nice.com" , "tag": "new list"}'
```

## Parameter

| Field | Type | Description |
| --- | --- | --- |
| uuid | uuid | Watch unique ID. |

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | Was updated |

## 500

| Field | Type | Description |
| --- | --- | --- |
| ERR | String | Some other error |

# Watch History

# Watch History\| Get a list of all historical snapshots available for a watch

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Requires `uuid`, returns list

get

```http
/api/v1/watch/<string:uuid>/history
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Watch_History-Get_list_of_available_stored_snapshots_for_watch-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/watch/cc0cfffa-f449-477b-83ea-0caafd1dc091/history -H"x-api-key:813031b16330fe25e3780cf0325daa45" -H "Content-Type: application/json"
{
    "1676649279": "/tmp/data/6a4b7d5c-fee4-4616-9f43-4ac97046b595/cb7e9be8258368262246910e6a2a4c30.txt",
    "1677092785": "/tmp/data/6a4b7d5c-fee4-4616-9f43-4ac97046b595/e20db368d6fc633e34f559ff67bb4044.txt",
    "1677103794": "/tmp/data/6a4b7d5c-fee4-4616-9f43-4ac97046b595/02efdd37dacdae96554a8cc85dc9c945.txt"
}
```

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String |  |

## 404

| Field | Type | Description |
| --- | --- | --- |
| ERR | String | Not found |

# Watch History\| Get single snapshot from watch

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Requires watch `uuid` and `timestamp`. `timestamp` of " `latest`" for latest available snapshot, or [use the list returned here](https://changedetection.io/docs/api_v1/#api-Watch_History-Get_list_of_available_stored_snapshots_for_watch)

get

```http
/api/v1/watch/<string:uuid>/history/<int:timestamp>
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Watch_History-Get_single_snapshot_content-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/watch/cc0cfffa-f449-477b-83ea-0caafd1dc091/history/1677092977 -H"x-api-key:813031b16330fe25e3780cf0325daa45" -H "Content-Type: application/json"
```

## Parameter

| Field | Type | Description |
| --- | --- | --- |
| html<br> optional | String | Optional Set to =1 to return the last HTML (only stores last 2 snapshots, use `latest` as timestamp) |

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String |  |

## 404

| Field | Type | Description |
| --- | --- | --- |
| ERR | String | Not found |

# Watch Management

# Watch Management\| List watches

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Return concise list of available watches and some very basic info

get

```http
/api/v1/watch
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Watch_Management-ListWatches-0_0_0-0)

```curl
curl http://localhost:5000/api/v1/watch -H"x-api-key:813031b16330fe25e3780cf0325daa45"
{
    "6a4b7d5c-fee4-4616-9f43-4ac97046b595": {
        "last_changed": 1677103794,
        "last_checked": 1677103794,
        "last_error": false,
        "title": "",
        "url": "http://www.quotationspage.com/random.php"
    },
    "e6f5fd5c-dbfe-468b-b8f3-f9d6ff5ad69b": {
        "last_changed": 0,
        "last_checked": 1676662819,
        "last_error": false,
        "title": "QuickLook",
        "url": "https://github.com/QL-Win/QuickLook/tags"
    }
}
```

## Parameter

| Field | Type | Description |
| --- | --- | --- |
| recheck\_all<br> optional | String | Optional Set to =1 to force recheck of all watches |
| tag<br> optional | String | Optional name of tag to limit results |

## 200

| Field | Type | Description |
| --- | --- | --- |
| OK | String | JSON dict |

# Watch Management\| Search for watches

**0.0.0**

- [compare changes to:](https://changedetection.io/docs/api_v1/#)
- [0.0.0](https://changedetection.io/docs/api_v1/#)

Search watches by URL or title text

get

```http
/api/v1/search
```

- [Example usage:](https://changedetection.io/docs/api_v1/#examples-Watch_Management-Search-0_0_0-0)

```curl
curl "http://localhost:5000/api/v1/search?q=https://example.com/page1" -H"x-api-key:813031b16330fe25e3780cf0325daa45"
curl "http://localhost:5000/api/v1/search?q=https://example.com/page1?tag=Favourites" -H"x-api-key:813031b16330fe25e3780cf0325daa45"
curl "http://localhost:5000/api/v1/search?q=https://example.com?partial=true" -H"x-api-key:813031b16330fe25e3780cf0325daa45"
```

## Query Parameter(s)

| Field | Type | Description |
| --- | --- | --- |
| q | String | Search query to match against watch URLs and titles |
| tagÂ Â <br> optional | String | Optional name of tag to limit results (name not UUID) |
| partialÂ Â <br> optional | String | Allow partial matching of URL query |

## 200

| Field | Type | Description |
| --- | --- | --- |
| JSON | Object | Object containing matched watches |

Generated with [apidoc](https://apidocjs.com/) 0.54.0 - Sun Apr 13 2025 21:49:13 GMT+0200 (Central European Summer Time)

---

### Privacy Statement | changedetection.io
Original URL: https://changedetection.io/privacy-statement.html

[Skip to main content](https://changedetection.io/privacy-statement.html#main-content)

### Privacy Statement

# Changedetection.io Privacy Policy

Please read this document carefully. It is the Changedetection.io Policy (the â€œPrivacy Policyâ€) and explains how personal information is collected, used and disclosed by Changedetection.io with respect to your access and use of this web site (located at changedetection.io and any subdomains related) (the â€œSiteâ€).

Changedetection.io Â reserves the right to change or modify this Privacy Policy from time to time, and we will notify users (â€œyouâ€) of material changes on the Site before they take effect. We will occasionally update this Privacy Policy to reflect changes in our practices. If we make any material changes in the way we collect, use, and/or share your personal information, we will notify you by sending an email to the email address you most recently provided us in your account, profile or registration (unless we do not have such an email address), and/or by posting notice of the changes on the Site. Your use of the Site and any of the information, products or various services, if any (collectively, the â€œServicesâ€) provided by us will be subject to the most current version of this Privacy Policy posted on the Site at the time of your use. We recommend that you check the site from time to time to inform yourself of any changes in this Privacy Policy or any of our other policies.

## What Is Personal Information?

â€œPersonal informationâ€ means information that specifically identifies an individual (such as a name, address, telephone number, mobile number or email address, website links etc) or information about that individual that is directly linked to personally identifiable information. Personal information does not include â€œaggregateâ€ information, which is data we collect about the use of the Site and the Services. Our Privacy Policy does not restrict or limit our collection and use of aggregate information.

* * *

## What Personal Information Do We Collect?

We collect certain information you voluntarily provide to us including, without limitation, the information you enter when you create an account and profile, send us an email, request user support or submit or post any other content to the Site or use the Services.

### Generally

We automatically collect certain information when you use the Site and the Services including, without limitation, your Internet Protocol (IP) address, your operating system, the browser type, the address of a referring site and your activity on the Site. We also collect information from mobile phone users in a similar manner to optimize the mobile experience.

The Site also stores data that is entered by its Users to facilitate its functionality such as URLs in the Watch section and/or steps in the BrowserSteps, the data you enter here is solely your own responsibility and Changedetection.io has no responsibility for the data you choose to enter.

Changedetection.io may from time to time access your data without notification while it is stored to facilitate account support, fine tune settings and perform analyses. By using Changedetection.io Site you agree to this usage of your data.

We may also receive personal information from third parties about their users, and may combine this information with other personal information we maintain about you. If we do so, this Privacy Policy will govern the combined information.

Even after you remove information from your profile, request account deletion or allow your subscription to lapse, Â If you post any of your information to a public area of the Site or the Services, please be aware that it is no longer â€œpersonal informationâ€ for purposes of this policy, and we or anyone else may use such information without restriction. If you provide access to personal or other information, including your email address or name, to other users through the application of any of our privacy controls or other settings, you hereby acknowledge and agree that Changedetection.io has no control over how others may collect, use or disclose such information.

## What Aggregated and Non-Personal Information Do We Collect?

We may use standard Internet technology, such as web beacons and other similar technologies, to track your use of the Site and the Services. We also may include web beacons in promotional email messages or newsletters to determine whether messages have been opened and acted upon. The information we obtain in this manner enables us to customize the services we offer visitors to our Site to deliver targeted advertisements and to measure the overall effectiveness of our online advertising, content, programming or other activities.

When you visit the Site, we may assign your computer one or more cookies, to facilitate access to the Site and to personalize your online experience. Through the use of a cookie, we also may automatically collect information about your online activity on the Site, such as the web pages you visit, the links you click, and the searches you conduct on the Site. Most browsers automatically accept cookies, but you can usually modify your browser setting to decline cookies. If you choose to decline cookies, please note that you may not be able to log in or use some of the interactive features offered on the Site.

## Children

The Site is not directed at children. Consistent with the Federal Childrenâ€™s Online Privacy Protection Act of 1998 (COPPA), Changedetection.io will not knowingly request or collect personally identifiable information from any child under age 13 without requiring parental consent. Any person who provides his or her personal information to use through the Site or the Services represents that he or she is older than 12 years of age.

## How Do We Use the Personal Information We Collect?

In General. We may use information that we collect about you to:

- Deliver the products and services that you have requested;
- Manage your account and provide you with customer support;
- Perform research and analysis about your use of, or interest in, our products, services or content, or products, services or content offered by others;
- Communicate with you by email, postal mail, telephone and/or mobile devices about products or services that may be of interest to you either from us or other third parties;
- Tailor your user experience;
- Develop and display third-party content and advertising tailored to your interests on the Site and other sites;
- Enforce our Terms and Conditions;
- Manage our business; and
- Perform functions as otherwise described to you at the time of collection.
- Financial Information. We may use financial information or payment method to process payment for any purchases, subscriptions or sales made on the Site or through the Services, to protect against or identify possible fraudulent transactions, and otherwise as needed to manage our business.

Please review â€œYour Choices About Collection and Use of Your Informationâ€ below.

## What Personal Information Do We Share With Third Parties?

We want you to understand when and with whom we may share personal or other information we have collected about you or your activities on the Site or while using the Services.

Personal Information. We do not share your personal information with others except as indicated below or when we inform you and give you an opportunity to opt out of having your personal information shared. We may share personal information with:

Authorized service providers: We may share your personal information with our authorized service providers that perform certain services on our behalf. These services may include fulfilling orders, processing credit card payments, providing customer service and marketing assistance, performing business analysis, supporting the functionality of the Site and the Services, and supporting surveys and other features offered through the Site. These service providers may have access to personal information needed to perform their functions but are not permitted to share or use such information for any other purposes.

- Other Situations. We also may disclose your information:

In response to a subpoena or similar investigative demand, a court order, or a request for cooperation from a law enforcement or other government agency; to establish or exercise our legal rights; to defend against legal claims; or as otherwise required by law. In such cases, we may raise or waive any legal objection or right available to us, in our sole discretion.

- When we believe disclosure is appropriate in connection with efforts to investigate, prevent, report or take other action regarding illegal activity, suspected fraud or other wrongdoing; to protect and defend the rights, property or safety of our company, our users, our employees, or others; to comply with applicable law or cooperate with law enforcement; or to enforce our website terms and conditions or other agreements or policies.
- In connection with a substantial corporate transaction, such as the sale of our business, a divestiture, merger, consolidation, or asset sale, or in the unlikely event of bankruptcy.

Any third parties to whom we may disclose personal information may have their own privacy policies which describe how they use and disclose personal information. Those policies will govern use, handling and disclosure of your personal information once we have shared it with those third parties as described in this Privacy Policy. If you want to learn more about their privacy practices, we encourage you to visit the websites of those third parties. These entities or their servers may be located either inside or outside the United States.

Aggregated and Non-Personal Information. We may share aggregated and non-personal information we collect under any of the above circumstances. We may also share it with third parties to develop and deliver targeted advertising on the Site, through the Services and on websites of third parties. We may combine non-personal information we collect with additional non-personal information collected from other sources. We also may share aggregated information with third parties, including advisors, advertisers and investors, for the purpose of conducting general business analysis. For example, we may tell our advertisers the number of visitors to our website and the most popular features or services accessed. This information does not contain any personal information and may be used to develop website content and services that we hope you and other users will find of interest and to target content and advertising.

## Your Control

You can choose not to provide us with certain information, but that may result in you being unable to use certain features of the Site and the Services because such information may be required in order for you to register as a member; purchase products or services; participate in a survey; ask a question; or initiate other transactions on the Site or through the Services.

At any time you can choose to no longer receive commercial or promotional emails or newsletters from us by using the email address associated with your account to send an email to contact@changedetection.io with the word â€œUnsubscribeâ€ in the subject line. You also will be given the opportunity, in any commercial email that we send to you, to opt out of receiving such messages in the future. It may take up to 10 days for us to process an opt-out request. We may send you other types of transactional and relationship email communications, such as service announcements, administrative notices, and surveys, without offering you the opportunity to opt out of receiving them. Please note that, changing information in your account, or otherwise opting out of receipt of promotional email communications will only affect future activities or communications from us. If we have already provided your information to a third party (such as a credit card processing partner) before you have changed your preferences or updated your information, you may have to change you preferences directly with that third party.

Upon request, the user is able to delete their account and delete their account data. Once a customer cancels their Changedetection.io account, they can contact support through email to request that their personal information be forgotten. We respect those wishes and will irrevocably anonymize their Changedetection.io data.

## Links to Other Sites

The Site and the Services may contain links to other sites. Any personal information you provide on the linked pages is provided directly to that third party and is subject to that third partyâ€™s privacy policy. This Privacy Policy does not apply to such linked sites, and we are not responsible for the content or privacy and security practices and policies of these sites or any other sites that are linked to from our Site.

## What Steps Do We Take To Protect Your Information Online?

We take reasonable measures to protect your personal information in an effort to prevent loss, misuse and unauthorized access, disclosure, alteration and destruction. Please be aware, however, that despite our efforts, no security measures are perfect or impenetrable and no method of data transmission can be guaranteed against any interception or other type of misuse. If we become aware of a security systems breach, we may attempt to notify you electronically so that you can take appropriate protective steps. Changedetection.io may post a notice through the Services if a security breach occurs. If this happens, you will need a web browser enabling you to access the Services. We may also send an email to you at the email address you have provided to use in these circumstances. Depending on where you live, you may have a legal right to receive notice of a security breach in writing.

Users should also be aware of how they handle and disclose their personal information and should avoid sending personal information through insecure email. Please refer to the Federal Trade Commissionâ€™s website at [http://www.ftc.gov/bcp/menus/consumer/data.shm](https://www.google.com/url?q=http://www.ftc.gov/bcp/menus/consumer/data.shm&sa=D&source=editors&ust=1687794061343235&usg=AOvVaw2RzeONONtFOOk37EqEFs14)Â for information about how to protect yourself against identity theft.

Users should not enter any data into the Changedetection.io Site which is personally identifiable or contains login and/or non-public links to third party websites.

## International Visitors

The Site and the Services are hosted in and provided from Canada. If you use the Site or the Services from the European Union or other regions with laws governing data collection and use that may differ from Canadian law, please note that you are transferring your personal data to Canada. Canada does not have the same data protection laws as the EU and some other regions. By providing your personal information, you consent to the transfer of your personal data to Canada and the use of your personal information, in accordance with this Privacy Policy.

## Information Retention and Disposal

We may retain personal information for as long as we have a business need for it or as applicable laws or regulations or government orders require us to retain it. Additionally, the Site and/or the Services may enable you (or other users) to save information including information that you have made public or allowed certain users to access or see.

## What Choices Do You Have Regarding the Use of Your Information?

You may â€œopt outâ€ of receiving marketing or promotional emails from us by following the instructions in those emails or by emailing us at contact@changedetection.io. If you opt out, we may still send you non-promotional emails, such as emails about your accounts or our ongoing business relations.

Changedetection.io is an equal opportunity data service provider, a conduit, just like an Internet Service Provider (AT&T, Verizon, Comcast). We just gather and store publicly available data on behalf of our users responsibly and sensibly. We do not resell data. We only provide the technology and data pipes to monitor changes of publicly available websites. Like other good bots such as Google, Amazon Alexa and others, Changedetection.io abides to current US and international guidelines and regulations on accessing websites at low frequency intervals to protect bandwidth and infrastructure of the websites we monitor.

The Site is an automated hosting platform for the changedetection.io opensource project.

---

### Notifications
Original URL: https://changedetection.io/taxonomy/term/1/feed

Notificationshttps://changedetection.io/
 en-gbHow to get alerts on new KeePass releaseshttps://changedetection.io/tutorial/how-get-alerts-new-keepass-releases
 <span class="field field--name-title field--type-string field--label-hidden">How to get alerts on new KeePass releases</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2023-07-01T16:36:04+02:00" title="Saturday, July 1, 2023 - 16:36" class="datetime">Sat, 07/01/2023 - 16:36</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 <div class="field\_\_item"><a href="/topic/notifications" hreflang="en-gb">Notifications</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>KeePass is vital for online security as it securely stores passwords. Getting update notifications is crucial to stay protected from potential vulnerabilities and cyber threats.</p><p>In this short article I'll show you how to setup changedetection.io to send you an alert as soon as a new (and often important) KeePass release is made, whilst minimizing false alerts.</p><p>&nbsp;</p><h4>Step 1, Add the URL</h4><p>Here we add the URL of <a href="https://keepass.info/download.html"><em>https://keepass.info/download.html</em></a><em> </em>simply add the URL to the top part of the page and simply click <strong>Watch</strong></p><img src="/sites/changedetection.io/files/inline-images/image.png" data-entity-uuid="486bdcbf-7f9a-4254-a676-e4bb964e2186" data-entity-type="file" width="1168" height="275" loading="lazy"><p>&nbsp;</p><h4>Step 2, Select the part of the page that contains the text we are interested in</h4><p>For example, we don't want false alerts when the header, footer or menu changes, so we use the <strong>Visual Selector</strong> to choose the content we are only interested in. The selected area will show with a <strong>red border</strong> and the rest will be greyed-out to make it easier to see what you selected.</p><img src="/sites/changedetection.io/files/inline-images/image\_0.png" data-entity-uuid="fb1bf898-39ae-40df-a815-f74721b28359" data-entity-type="file" width="1129" height="599" loading="lazy"><p>&nbsp;</p><h4>Step 3, Setup your favourite notification</h4><p>In the last step, click on the <strong>Notifications </strong>tab, click <strong>'Add email' , </strong>here you can enter in the preferred email address to send notifications to.</p><p>changedetection.io (for subscribers) will automatically choose our mail server to send your emails to, so you don't need to setup anything further.</p><p>You can also choose to attach the screenshot to the email by clicking <strong>Attach screenshot to notification</strong></p><img src="/sites/changedetection.io/files/inline-images/image\_1.png" data-entity-uuid="6d6551d1-c851-41a9-b63c-d0c4ec640900" data-entity-type="file" width="1130" height="469" loading="lazy"><p>&nbsp;</p><p>Don't forget that you can also send notifications via Discord, Telegram and over 90 other different methods</p><p>Then simply click <strong>Save</strong></p></div>
 Sat, 01 Jul 2023 14:36:04 +0000Stephen7 at https://changedetection.io

---

### How-To
Original URL: https://changedetection.io/taxonomy/term/4/feed

How-Tohttps://changedetection.io/
 en-gbHow to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less
 <span class="field field--name-title field--type-string field--label-hidden">How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2025-04-17T15:08:26+02:00" title="Thursday, April 17, 2025 - 15:08" class="datetime">Thu, 04/17/2025 - 15:08</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p><strong>How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)</strong></p><p>If you've been trying to get your hands on Ubiquiti gearâ€”like the Power Distribution Pro, Cloud Gateway Fiber, or that elusive Dream Machine Proâ€”you know the story: blink, and it's sold out. Hitting refresh all day just doesnâ€™t cut it anymore. But thereâ€™s a smarter way to shopâ€”and it takes less than five minutes to set up.</p><p>With <strong>ChangeDetection.io's Restock and Price Detection mode</strong>, you can monitor any Ubiquiti product page and get notified instantly when it <em>comes back in stoc</em>k. No complicated setup, no fiddling with page elementsâ€”just copy the product link, enable restock mode, and you're covered.</p><p>This guide will show you exactly how to do that. Whether you're new to this or already tracking a few items, you'll be up and running fast. And if you're serious about not missing restocks, you might want to consider upgradingâ€”faster checks mean you're first in line when stock drops.</p><p>With a bonus at the end - How to connect all of this to your favourite Discord channel</p><p>Letâ€™s get started.</p><p>&nbsp;</p><p><em><strong>First, grab a </strong></em><a href="https://changedetection.io/checkout"><em><strong>quick cheap subscription</strong></em></a><em><strong> or </strong></em><a href="https://github.com/dgtlmoon/changedetection.io"><em><strong>install the changedetection.io software locally</strong></em></a><em><strong>, in the case you grab a subscription you can be up and running in just a few seconds.</strong></em></p><p>&nbsp;</p><p>Not convinced? check out what other people are saying about <em><strong>changedetection.io for ubiquiti store &nbsp;restock detection</strong></em>!</p><ul><li><a href="https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks\_changedetectionio/">https://www.reddit.com/r/Ubiquiti/comments/1js4s7l/thanks\_changedetectionio/</a></li><li><a href="https://www.reddit.com/r/Ubiquiti/comments/1hs6kzk/a\_better\_way\_for\_me\_to\_get\_instock\_alerts\_follow/?tl=pt-pt">https://www.reddit.com/r/Ubiquiti/comments/1hs6kzk/a\_better\_way\_for\_me\_to\_get\_instock\_alerts\_follow/</a></li></ul><p>&nbsp;</p><p>So let's go!</p><p>&nbsp;</p><h2>Step 1. &nbsp;Add the link to the item you want restock or price changes for from the UI Ubiquity store</h2><p>&nbsp;</p><p>There's two ways todo this, both are super easy, first way is to &nbsp;add the URL directly to dashboard</p><p>Enter the URL of the product that you wish to monitor for restock or price change alerts directly in the dashboard</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_115.png" data-entity-uuid="1f53c487-ab3a-485e-9fdd-5914f62af3fa" data-entity-type="file" alt="Ubiquity add restock URL" width="796" height="466" loading="lazy"><p>&nbsp;</p><p><strong>Or</strong> simply click on the browser extension to add the current product to your changedetection.io automatically &nbsp;<a href="https://chromewebstore.google.com/detail/changedetectionio-website/kefcfmgmlhmankjmnbijimhofdjekbop">using the browser extension - simply set "restock" mode</a></p><p>&nbsp;</p><p><video style="max-width:80%;" autoplay loop muted playsinline controls>
 <source src="/sites/changedetection.io/files/2025-04/add-UI-store-restock-extension.webm" type="video/webm">
 Your browser does not support the video tag.
 </video></p><p>&nbsp;</p><h2>Step 2. Your favorite Ubiquity products are now monitored for restock / back in stock and price changes.</h2><p>&nbsp;</p><p>Back at your dashboard you can now see the status of all the products you're interested in, Green for "in stock" grey for "out of stock", as well as price.</p><p>Changedetection.io will recheck the items based on any schedule you prefer, you can even limit it by days of the week, hours of the day.</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_120.png" data-entity-uuid="a3663ed9-3c14-4985-8285-35c723833bc9" data-entity-type="file" alt="Ubiquity UI store restock status overview with prices" width="1429" height="573" loading="lazy"><h3>&nbsp;</h3><h3>Step 3 - Optionally set price conditions</h3><p>&nbsp;</p><p>This step is <strong>completely optional</strong> but if you prefer you can also limit the notifications of price / restock changes by whatever amount you like, so you could perhaps limit the notification to price drops on Ubiquity products (Set the "Threshold % change" box)</p><p>Or an absolute price, perhaps you want to know if the product drops to below $10 when it's normally $12. (Discount / end of product line / special sales notifications)</p><p><img src="/sites/changedetection.io/files/inline-images/image\_123.png" data-entity-uuid="a6433cdc-8594-4670-ad99-7455502e0a7c" data-entity-type="file" alt="Ubiquity configure price sales notifcations" width="956" height="611" loading="lazy"></p><h2>&nbsp;</h2><h2>Step 4 - Setup your notifications including email, Discord and many others</h2><p>&nbsp;</p><p>One of the best parts of using ChangeDetection.io is how it supports <strong data-start="235" data-end="292">virtually every notification service you can think of</strong>â€”thanks to its integration with Apprise. Whether you want alerts on <strong data-start="401" data-end="412">Discord</strong>, <strong data-start="414" data-end="421">SMS</strong>, <strong data-start="423" data-end="435">Telegram</strong>, <strong data-start="437" data-end="446">Slack</strong>, <strong data-start="448" data-end="467">Microsoft Teams</strong>, <strong data-start="469" data-end="481">Pushover</strong>, <strong data-start="483" data-end="493">Gotify</strong>, or even <strong data-start="503" data-end="512">email</strong>, itâ€™s all built in and ready to go. You can set it up to ping your phone, your team, or even your smart home system the instant something changes. No more FOMOâ€”just instant, reliable alerts exactly where you want them. Whether you're at your desk or on the go, youâ€™ll never miss a restock again.</p><p>Head on over to the <strong>"Notifications"</strong> &nbsp;and setup which ever you prefer for you and your team!</p><p>&nbsp;</p><p>Bonus points - Connect your Ubiquiti restock notifications to Discord! just follow this link <a href="https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord#discord">https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord</a></p><p>&nbsp;</p><p>As always, have fun!</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p></div>
 Thu, 17 Apr 2025 13:08:26 +0000Stephen73 at https://changedetection.ioFind the best proxy to beat "403 access denied" with our proxy scannerhttps://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner
 <span class="field field--name-title field--type-string field--label-hidden">Find the best proxy to beat &quot;403 access denied&quot; with our proxy scanner</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2025-04-13T18:07:43+02:00" title="Sunday, April 13, 2025 - 18:07" class="datetime">Sun, 04/13/2025 - 18:07</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>Using a proxy scanner to determine which proxies can bypass <strong>403 Access Denied</strong> errors is crucial when monitoring websites for product prices or other changes with tools like Changedetection.io. Some websites restrict access based on geographic location or traffic patterns, leading to blocked requests and incomplete monitoring. A proxy scanner helps identify working proxies that successfully retrieve pages without being denied, ensuring consistent access to accurate data.</p><p>&nbsp;</p><p>Fortunately changedetection.io has a <strong>proxy scanner</strong> built in - so take for example this common situation where we have a few proxies configured but we get the error <strong>403 access denied</strong> on our default proxy</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_119.png" data-entity-uuid="e8869e6c-2acb-448b-8cfe-dc1698031ae0" data-entity-type="file" alt="403 access denied" width="1020" height="167" loading="lazy"><p>&nbsp;</p><p>If we jump over to <strong>Edit</strong> &gt; then <strong>Requests</strong> tab we can then find the <strong>Proxy Scanner tool</strong> which will help us find the proxy (or location) that will let us by-pass the 403 Access Denied error.</p><p>&nbsp;</p><p><strong>First you need to add your proxies</strong></p><p>Jump on over to <strong>Settings</strong> &gt; <strong>CAPTCHA &amp; Proxies</strong> and add your "Extra proxies", in the hosted/subscription version we call these "locations" however they are the same thing. I recommend BrightData or Oxylabs here, they are both fantastic.</p><p>&nbsp;</p><img data-entity-uuid="624ee05b-114d-4af5-bf05-5a6d2ee6d82a" data-entity-type="file" src="/sites/changedetection.io/files/inline-images/image\_124.png" width="1146" height="459" alt="Adding Proxies" loading="lazy"><p>&nbsp;</p><p>Then go back to your "watch", and click "<strong>EDIT</strong>" and "<strong>Request</strong>"</p><p>&nbsp;</p><p>Then we click on <strong>Check / Scan All </strong>to activate the scanner on all proxy connections and find the one which will not give the 403 access denied message.</p><p>&nbsp;</p><p>(other options like <em>request method</em> removed here for the sake of brevity)&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_121.png" data-entity-uuid="65474950-9b93-43a5-b39c-e1e4b06d7e9c" data-entity-type="file" alt="403 access denied - start proxy scanner / check all" width="986" height="464" loading="lazy"><p>&nbsp;</p><p>Once we click on that <strong>Check / Scan All</strong> the proxy scanner will then get to work!</p><p>&nbsp;</p><p><video style="max-width:80%;" autoplay loop muted playsinline controls>
 <source src="/sites/changedetection.io/files/2025-04/403-access-denied-proxy-scanner.webm" type="video/webm">
 Your browser does not support the video tag.
 </video></p><p>&nbsp;</p><p>Within a few seconds we can see the results, that 4 of our proxies gave Access Denied, but 4 were ready to rock! &nbsp;As well as some basic timing information (seconds for the request), any non-200 errors (error 500, error 403 etc) will show here.</p><p>&nbsp;</p><p>So here we simply selected <strong>Europe / Frankfurt</strong> and then clicked <strong>Save</strong></p><p>&nbsp;</p><p>And then we wait a few seconds and see that the 403 access denied message is now gone</p><img src="/sites/changedetection.io/files/inline-images/image\_122.png" data-entity-uuid="bd044248-3593-401c-9830-58c91032701d" data-entity-type="file" alt="403 access denied solved" width="791" height="130" loading="lazy"><p>&nbsp;</p><p>&nbsp;</p><p>So there you have it, just another great little tool in changedetection - the <strong>proxy scanner</strong> which helps you beat <strong>403 access denied</strong> errors by find the best proxy for you!</p><p>&nbsp;</p><p>As always, happy change detecting!</p><p>&nbsp;</p></div>
 Sun, 13 Apr 2025 16:07:43 +0000Stephen71 at https://changedetection.ioHow To Monitor Keywords On Any Websitehttps://changedetection.io/tutorial/how-monitor-keywords-any-website
 <span class="field field--name-title field--type-string field--label-hidden">How To Monitor Keywords On Any Website</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2025-04-04T23:21:54+02:00" title="Friday, April 4, 2025 - 23:21" class="datetime">Fri, 04/04/2025 - 23:21</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><h2><strong>How to Use Changedetection.io to Monitor Specific Keywords</strong></h2><p><img src="/sites/changedetection.io/files/inline-images/keyword.png" data-entity-uuid="a3eb0727-cd45-4ac3-afac-52df49b46886" data-entity-type="file" width="213" height="213" class="align-right" loading="lazy"><br>In the world of breaking news and rapid financial updates, staying ahead of key developments is critical. Changedetection.io helps you to get <strong>notifications of specific keywords</strong> on just about any webpageâ€”whether it's a news outlet, financial report, or investor relations page. Get instant alerts when important terms appear, such as company names, stock tickers, or economic indicators, so you never miss a crucial update.</p><p><em><strong>With changedetection.io you can monitor thousands of web pages for important keywords.</strong></em></p><p>&nbsp;</p><h3>Step 1: Add the URL to your changedetection.io dashboard</h3><p>Simply copy and paste the URL of the page you wish to monitor for keywords, then click <strong>EDIT &gt; WATCH</strong>, this will take us directly to the page to add the keywords</p><img src="/sites/changedetection.io/files/inline-images/keyword-setup\_0.jpg" data-entity-uuid="2ef284ad-f285-411e-8cd2-658e3a866f02" data-entity-type="file" alt="Add page for keyword monitoring" width="1081" height="279" loading="lazy"><p>&nbsp;</p><h3>Step 2: Add the keywords to monitor - this will create a trigger for alerts</h3><p>&nbsp;</p><p>Click on <strong>Filters &amp; Triggers</strong> and scroll down to "<strong>Keyword triggers</strong>", here you can setup the keywords to trigger on, they will be processed case-insensitive.</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/adding-notification-keywords.jpeg" data-entity-uuid="49a2932e-1544-464a-9ceb-1e83367d25d1" data-entity-type="file" alt="Adding keyword triggers" width="1107" height="726" loading="lazy"><p>&nbsp;</p><p>Super easy! Now every time the web page is checked (even according to your custom schedule if you prefer!) the text content will be compared against your list of keywords, if those keywords are found in the text of the webpage, and there was a change in the webpage, you will get a notification!&nbsp;</p><p>Be sure to click on the <strong>Notifications</strong> tab and configure your favourite alerts, don't forget we support email, Discord, Slack, MS-Teams and 85+ others! The best way to keep your team informed.</p><p>&nbsp;</p><h3>Step 3: Sit back and relax, let changedetection.io do the work!</h3><p>&nbsp;</p><h3>Extra points</h3><p>&nbsp;</p><p>What if you want to monitor keywords on a webpage every day at 0900?<a href="https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule"> You could use the scheduler and combine it with your keyword alert</a></p><p>&nbsp;</p><p>From here you can also get more advanced and setup <a href="https://changedetection.io/tutorial/conditional-actions-web-page-changes">Conditions</a>, (perhaps you want to also add a rule that the page should NOT include certain keywords at the same time, the possibilities are endless!)</p><p>&nbsp;</p><p>Take it even further with <strong>Group Watches </strong>, you could even assign hundreds of web-pages to the same <strong>Group</strong> and then simply add the <strong>Keywords to Monitor</strong> as a single <strong>Group</strong> setting, saving you time and making it a lot easier to manage large lists of web-pages that should be checked for the same keywords.</p><p>I encourage you to check it out, have a play, and see just what is possible with <strong>Web Page Keyword Monitoring</strong> with changedetection.io</p><p>&nbsp;</p><p>&nbsp;</p><p>All the best, have fun, and happy changedetecting!</p></div>
 Fri, 04 Apr 2025 21:21:54 +0000Stephen70 at https://changedetection.ioConditional actions on web page changes!https://changedetection.io/tutorial/conditional-actions-web-page-changes
 <span class="field field--name-title field--type-string field--label-hidden">Conditional actions on web page changes!</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2025-03-31T15:20:27+02:00" title="Monday, March 31, 2025 - 15:20" class="datetime">Mon, 03/31/2025 - 15:20</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>Starting with version <strong>v0.49.9</strong>, Changedetection.io introduces one of its most powerful features yet: <strong>conditional actions</strong>. This opens the door to much more precise and flexible monitoring.</p><p>Itâ€™s no longer just about detecting when content changes â€” now you can define exactly <em>what kind</em> of change matters to you. For example, trigger an alert only when a productâ€™s price drops below a certain threshold, or when a keyword appears in the updated content.</p><p>With full support for logic operators, you can create rich, rule-based conditions using logic like â€œgreater than,â€ â€œless than,â€, "contains", "not contains" and more.</p><p>&nbsp;</p><p>So let's get on with a really great example - Monitor when temperatures in Berlin are "extreme" (less than -20c or greater than +38c)<br>&nbsp;</p><h3>Let's add the web page we want to monitor for changes (Berlin Weather)</h3><p><br><img src="/sites/changedetection.io/files/inline-images/image\_109.png" data-entity-uuid="70cd2519-a0cb-47e8-b459-07f339b8bf95" data-entity-type="file" alt="Web page for conditional actions" width="955" height="245" loading="lazy"><br><br>&nbsp;</p><h3>Let's set-up our conditional change detection filter</h3><p>Let the page fetch, then click <strong>\[EDIT\]</strong></p><img src="/sites/changedetection.io/files/inline-images/image\_112.png" data-entity-uuid="ff7487bd-51cb-4608-ab07-4aaa33cf9b64" data-entity-type="file" width="893" height="319" loading="lazy"><p>&nbsp;</p><p>Then, using the <strong>Visual Filter Selector</strong> tab, choose the number, in this case we will click on the current temperature, a balmy 9.2Â°C. &nbsp;When the element is selected and click a <strong>red border</strong> will appear.</p><p>&nbsp;</p><p>It's important to choose the right part of the web-page for change-detection, otherwise the number extractor wont know exactly which number is important to you.</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_113.png" data-entity-uuid="f3edea26-f116-407c-91f6-8dc7b2222391" data-entity-type="file" alt="Web page for conditional actions, setting the actual content" width="1097" height="601" loading="lazy"><p>&nbsp;</p><p>Then, hop on over to the <strong>CONDITIONS </strong>tab</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_114.png" data-entity-uuid="7572885f-f21d-434d-8cc1-dcc3fabf5fa0" data-entity-type="file" alt="Setting up rules / conditions for web page changes" width="977" height="433" loading="lazy"><p>&nbsp;</p><p>Let's explain a little what we see here</p><ul><li><strong>"Match any of the following" - </strong>This acts as 'OR', so <em>any</em> rule will trigger on change</li><li><strong>"Extracted number after 'Filters &amp; Triggers" </strong>- We only want to look for a number inside of any filters we specified (This could be the Visual Selector, Text filters from other tabs etc)</li><li>Using these two buttons we can then <strong>add an extra</strong> <strong>\[ &nbsp;+ &nbsp;\]</strong> &nbsp;rule after this one, or <strong>remove it &nbsp; &nbsp;\[ &nbsp;- &nbsp;\]</strong></li></ul><p>&nbsp;</p><p>&nbsp;</p><h5><em><strong>Testing the rules!</strong></em></h5><p>Since the page is already fetched, It's nice to know if the rule currently will pass or fail, for this we can press the "tick" button, this will verify that rule row only and report if it PASSES or FAILS.</p><p>If you look closely you can see that after pressing the "verify" tick button you can see the text <strong>"extracted number value was 9.2"</strong> below the rules, this lets us know what the situation is and so we know if the right value is being extracted</p><p>&nbsp;</p><p>&nbsp;</p><h5>Other interesting checks</h5><ul><li>Text contains (or does not contain)</li><li>Text length is greater than (or shorter than)</li><li>Text begins with (or doesnt begin with)</li><li>Text equal (or does not equal)</li><li>plus more!</li></ul><p>&nbsp;</p><h4>Wrapping up</h4><p>&nbsp;</p><p>Of course now you can head over to the <strong>Notifications</strong> tab and setup your slack, email, discord or which ever format you and your team love the most.</p><p>This is how you can simply setup Conditional changes, this is just a simple example but there are so many other amazing ways to use this functionality, we encourage you to explore and play with this new tool :)</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p></div>
 Mon, 31 Mar 2025 13:20:27 +0000Stephen69 at https://changedetection.ioNÃ¼rburgring racing passion - Get notified of news updates today from NÃ¼rburgring!https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring
 <span class="field field--name-title field--type-string field--label-hidden">NÃ¼rburgring racing passion - Get notified of news updates today from NÃ¼rburgring!</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2025-03-07T08:54:44+01:00" title="Friday, March 7, 2025 - 08:54" class="datetime">Fri, 03/07/2025 - 08:54</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>The NÃ¼rburgring, or "Green Hell," is the ultimate test of skill and endurance, beloved for its intense racing and unpredictable conditions. Recent updates include the NÃ¼rburgring 24 Hours joining the Intercontinental GT Challenge, with Ravenol as the new title sponsor. The 2024 race, shortened by heavy fog, saw Scherer Sport PHX take a historic seventh win - Find out how to get notified when the official NÃ¼rburgring website updates its news section! stay informed! <strong>Get daily NÃ¼rburgring news updates to your inbox.</strong></p><p><img src="/sites/changedetection.io/files/2025-03/N%C3%BCrburgring-updates-today.png" alt="NÃ¼rburgring updates today" width="349" height="202" class="align-right" loading="lazy"></p><p>&nbsp;</p><p>Let's setup a simple monitor to send a notification via email when the NÃ¼rburgring website has an update today.</p><p>You could use this same method for many other similar Motorsport websites.</p><p>Fortunately we can very simply setup changedetection.io to recheck their website at a regular interview and send an update.</p><p>So, start your engines, let's go!</p><p>&nbsp;</p><h3>Step 1. Start your engines!</h3><p>Log into your changedetection.io account and add the link to the NÃ¼rburgring news section <strong>https://nuerburgring.de/news/</strong></p><img src="/sites/changedetection.io/files/inline-images/image\_104.png" data-entity-uuid="5820aa0b-236b-4b64-81e0-5a80a9c8cfca" data-entity-type="file" alt="nuerburgring news update link" width="1294" height="279" loading="lazy"><p>&nbsp;</p><p>You will then see that changedetection.io is automatically checking the news section, this should take 10-15 seconds.</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_105.png" data-entity-uuid="2f73b445-d8d2-4c79-a91f-21a5b0163d01" data-entity-type="file" alt="NÃ¼rburgring website updates checking news" width="798" height="343" loading="lazy"><p>&nbsp;</p><p>Fantastic!</p><p>&nbsp;</p><h3>Step 2. Select just the "news section" from the web page.</h3><p>NÃ¼rburgring website has a LOT of fantastic information, some of it might not be important to you, for example in the header they have the current temperature :) so lets just select the news block</p><ul><li>Click <strong>EDIT</strong> then visit the <strong>Visual Selector</strong> tab.</li><li><p>Click on the news grid, it will add a <strong>red box</strong> to signify that only that area will be used for web page change detections.</p><p>&nbsp;</p></li></ul><img src="/sites/changedetection.io/files/inline-images/image\_106.png" data-entity-uuid="7d0d84de-5c93-4298-a55f-c2e3493fb1d9" data-entity-type="file" alt="News updates today section" width="1149" height="740" loading="lazy"><h3>&nbsp;</h3><h3>Step 3. Add your email in the notifications tab</h3><p>After selecting the news section of the website, simply click on the <strong>Notifications</strong> tab. click the <strong>Add email</strong> button below the textbox, Add your email then click <strong>SAVE</strong></p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_110.png" data-entity-uuid="52fba731-96ef-43f1-8d46-7a3b2bf8bb98" data-entity-type="file" alt="NÃ¼rburgring updates to email setup" width="1154" height="549" loading="lazy"><p>&nbsp;</p><p>Sit back, relax, we will re-check the website and email you when ever there is a news update - we also encourage you to explore the other features of the service!<br>&nbsp;</p><p>&nbsp;</p><p>We'll leave you with this one heartfelt message :)</p><p><br><img data-entity-uuid="9e7f2e86-d4ec-49dd-b27d-427e110b0613" data-entity-type="file" src="/sites/changedetection.io/files/inline-images/image\_111.png" width="487" height="332" alt="news updates today" loading="lazy"></p><p>&nbsp;</p><p>&nbsp;</p></div>
 Fri, 07 Mar 2025 07:54:44 +0000Stephen66 at https://changedetection.ioBestBuy restock alerts - GeForce RTX 5090 & GeForce RTX 5080 are out!https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out
 <span class="field field--name-title field--type-string field--label-hidden">BestBuy restock alerts - GeForce RTX 5090 &amp; GeForce RTX 5080 are out!</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2025-01-31T18:37:34+01:00" title="Friday, January 31, 2025 - 18:37" class="datetime">Fri, 01/31/2025 - 18:37</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>The NVIDIA GeForce RTX 5090 and RTX 5080 are finally here, and they are absolute game-changers! Powered by the revolutionary Blackwell RTX architecture, these GPUs deliver mind-blowing performance, doubling frame rates, slashing workflow times in creative apps, and supercharging AI generation.<img src="/sites/changedetection.io/files/inline-images/image\_103.png" data-entity-uuid="20dd0b19-5a1e-4914-b4a7-57991cc8a683" data-entity-type="file" width="320" height="247" class="align-right" loading="lazy"> With DLSS 4â€™s Multi Frame Generation, you can experience ultra-smooth, ray-traced 4K gaming at unprecedented frame ratesâ€”think <em>Cyberpunk 2077</em> maxed out at 290 FPS and <em>Alan Wake 2</em> at 230 FPS. Whether you're gaming, streaming, or pushing the limits of creative work, the RTX 50 Series is built for the future.</p><p>But hereâ€™s the catchâ€”these cards are selling out <strong>fast</strong>! With stock-clocked and factory-overclocked models from ASUS, MSI, GIGABYTE, and more, plus limited Founders Edition cards from Best Buy, demand is through the roof. If you donâ€™t want to miss out, <strong>Changedetection.io</strong> is your secret weapon. Set up instant restock alerts so you can grab one the moment it becomes available. Donâ€™t get left behindâ€”stay ahead of the crowd and secure your RTX 5090 or RTX 5080 before they vanish!&nbsp;</p><p>&nbsp;</p><p>Here's how!</p><p>&nbsp;</p><h3>Step 1. Setup your changedetection.io account</h3><p>&nbsp;</p><p>Simply register here (click signup) or deploy your own locally run software, see <a href>https://github.com/dgtlmoon/changedetection.io</a></p><p>&nbsp;</p><h3>Step 2. &nbsp;Visit the product page page at BestBuy</h3><p>&nbsp;</p><p>For example <a href>https://www.bestbuy.com/site/nvidia-geforce-rtx-5090-32gb-gddr7-graphics-card-dark-gun-metal/6614151.p?skuId=6614151</a></p><p>This link is what you will use to "watch" in changedetection.io</p><img src="/sites/changedetection.io/files/inline-images/bestbuy-geforce-rtx.jpg" data-entity-uuid="b1650c5a-59e4-4ae7-b7c1-19965f20850a" data-entity-type="file" alt="Bestbuy restock RTX" width="1111" height="733" loading="lazy"><p>&nbsp;</p><h3>&nbsp;</h3><h3>Step 3. &nbsp;Use the link in changedetection.io and set the restock mode!</h3><p>&nbsp;</p><ul><li><p>Be sure to set the "<strong> Re-stock &amp; Price detection for single product pages " </strong>mode for restock magic!</p><p>&nbsp;</p></li></ul><img src="/sites/changedetection.io/files/inline-images/image\_101.png" data-entity-uuid="ca67fa09-ed01-4cb8-96de-0a668a0c2768" data-entity-type="file" alt="Add RTX BestBuy for restock monitoring" width="1091" height="305" loading="lazy"><h3>&nbsp;</h3><h3>Step 4. Setup your notifications</h3><p>By default, we don't assume that you prefer email as a notification - infact many people are using Discord, NTFY, MSTeams and other communication methods, so simply visit <strong>Settings</strong> &gt; <strong>Notifications</strong> and follow the prompts :)</p><p>&nbsp;</p><h3>Step 5. Enjoy restock monitoring of the GeForce RTX 5090 / 5080 product page!</h3><p>&nbsp;</p><p>Now changedetection.io will recheck the BestBuy RTX 5090 / 5080 page at a preset interval, you can add for example all of the RTX range and see which ones come back in stock - or which ones have a price change</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_102.png" data-entity-uuid="00564dca-aab9-44f8-94ae-b1ec91d7a66b" data-entity-type="file" alt="BestBuy RTX" width="1255" height="554" loading="lazy"><h3>&nbsp;</h3><p>&nbsp;</p><p>All the best and happy gaming with your new RTX 5090 / RTX 5080 !</p></div>
 Fri, 31 Jan 2025 17:37:34 +0000Stephen64 at https://changedetection.ioKmart Shopping - Easily monitor prices and get restock alerts via email, discord, and others.https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others
 <span class="field field--name-title field--type-string field--label-hidden">Kmart Shopping - Easily monitor prices and get restock alerts via email, discord, and others.</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2025-01-20T15:14:15+01:00" title="Monday, January 20, 2025 - 15:14" class="datetime">Mon, 01/20/2025 - 15:14</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p><img src="/sites/changedetection.io/files/2025-01/kmart.jpg" alt="kmart.jpg (554Ã—397)" width="264" height="189" class="align-right" loading="lazy"></p><p>Kmart is a great place to shop for every day needs, but what is even better is getting alerts when items come back in stock or when they are on sale (price reduced!)</p><p>In this quick tutorial I'll show you how to setup changedetection.io to notify you when items are re-stocked or have a price change.</p><p>&nbsp;</p><p>So let's say for example we want to monitor the prices and restock situation with Feminine Hygiene products over at the Kmart website</p><p>&nbsp;</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_96.png" data-entity-uuid="c6965e26-6d3e-4394-9448-0bed213ac214" data-entity-type="file" alt="Restock and price change alerts feminine hygiene products" width="882" height="520" loading="lazy"><p>&nbsp;</p><h3>Adding the Kmart products for monitoring price and restock.</h3><p>&nbsp;</p><p>Simply access each page, and copy+paste the URL/web address of the product into your changedetection.io monitoring page, for example, the first product would be <a href="https://www.kmart.com.au/product/u-by-kotex-14-pack-ultrathin-regular-pads-with-wings-43158805/">https://www.kmart.com.au/product/u-by-kotex-14-pack-ultrathin-regular-pads-with-wings-43158805/</a></p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_97.png" data-entity-uuid="6f7564c6-16ad-46ec-b2b7-a0851479867f" data-entity-type="file" alt="Kmart product web page address" width="1039" height="50" loading="lazy"><p>&nbsp;</p><p>Copy+paste this address into the "Add a webpage" box at the top of the changedetection.io monitoring page and select the &nbsp;"<strong>Re-stock &amp; Price detection for single product pages"</strong> option.</p><p>( Pro tip: You can also use our <a href="https://chromewebstore.google.com/detail/changedetectionio-website/kefcfmgmlhmankjmnbijimhofdjekbop">Web page change and price change detection Chrome plugin</a> )&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_98.png" data-entity-uuid="95bf46fb-2997-4027-ae55-84908ccd9661" data-entity-type="file" alt="Kmart product - adding page for detecting price and restock changes" width="1126" height="242" loading="lazy"><p>&nbsp;</p><p>Now on the front page of the application, you can see the restock status and pricing of your products that you're interested in</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_100.png" data-entity-uuid="a7db24b9-ce5e-48fd-9ddb-30dbcd34c9ae" data-entity-type="file" alt="Kmart products overview of prices and changes" width="1292" height="502" loading="lazy"><p>What's really nice here is that you can see the price and restock status of all your favourite products in one view, green = instock :)</p><p>The system will recheck all the items at the default recheck interval. There are many other options to explore such as increasing or decreasing the product page recheck schedule, checking between dates (maybe you only want to check on a weekday?) as well as setting "high" and "low" price thresholds - So you can get an alert when the product drops below $4 AUD for example.</p><p>&nbsp;</p><h3>Setting up the alerts / notifications&nbsp;</h3><p>There are 90+ different ways that you can be notified, such as email (the most classic way), Discord, MS-Teams and others, in the easiest way just visit "<strong>Settings</strong>" and "<strong>Notifications</strong>" then click "<strong>Add</strong> <strong>email</strong>"</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_99.png" data-entity-uuid="213dabce-8e7a-4dd9-a1f0-33557192dc08" data-entity-type="file" alt="Kmart set up alerts for restock" width="926" height="257" loading="lazy"><p>&nbsp;</p><p>When the product is restocked OR has a price change you will then receive an alert to your email box :)</p><p>&nbsp;</p><p>Happy shopping and we hope we saved you a few dollars :)</p><p>&nbsp;</p><p><br>&nbsp;</p></div>
 Mon, 20 Jan 2025 14:14:15 +0000Stephen42 at https://changedetection.ioPre-fill dynamic form "date" fields and get web page change alertshttps://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts
 <span class="field field--name-title field--type-string field--label-hidden">Pre-fill dynamic form &quot;date&quot; fields and get web page change alerts</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2025-01-20T12:15:53+01:00" title="Monday, January 20, 2025 - 12:15" class="datetime">Mon, 01/20/2025 - 12:15</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>A common situation is when you need to pre-fill / fill-in some data in a web page form such as the "current date", this an example would be when booking a trailor or reserving a car-parking space.</p><p>&nbsp;</p><p><img src="/sites/changedetection.io/files/inline-images/image\_95.png" data-entity-uuid="cabb01f8-6e77-45c1-ad6c-63909e1fc6a0" data-entity-type="file" alt="Pre-fill date field before web page change detection" width="400" height="305" class="align-right" loading="lazy"></p><p>Obviously, entering the current date directly is going to be a lot more easier to configure than using the calendar that the web page comes with (which are often really hard to navigate, even by humans!)</p><p>One really great feature of changedetection.io is that we try to support "Jinja2" macros where-ever possible, so this means you can insert the current date/time in whatever format you like using Browser Steps</p><p>&nbsp;</p><p>&nbsp;</p><p>So let's get to it!</p><p>&nbsp;</p><h2>&nbsp;</h2><h2>Automatically enter he current date in an input box</h2><p>&nbsp;</p><ul><li>Activate the <strong>Browser Steps</strong> for the webpage you are monitoring for changes, give it a few moments to connect.</li><li>Mouse over the input field (highlighted in red) and click it.</li><li><p>The software will identify the element as an input/text box and ask you to enter some text, this is where the magic happens.</p><p>&nbsp;</p></li></ul><img src="/sites/changedetection.io/files/inline-images/image\_93.png" data-entity-uuid="36647537-f0b3-4977-b925-f6a604fdebd8" data-entity-type="file" alt="Setting the current date in a field before web page change detection" width="1007" height="650" loading="lazy"><p>&nbsp;</p><p>&nbsp;</p><p>Now the website automatically prefills the date with next months date, but we want to be sure we enter todays date when ever the web page change detection runs, so that we could perhaps see if any car parking places are available today.</p><ul><li>Enter <code>{% now &nbsp;'Europe/Berlin', '%d-%m-%Y' %}</code> &nbsp;in the "<em><strong>value</strong></em>" field under the "<strong>Enter text in field</strong>" box on the right.</li><li>Click <strong>Apply</strong> to see the changes take affect.</li></ul><p>&nbsp;</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_94.png" data-entity-uuid="d5748b94-ed9f-4b1a-bf0c-35d2a8a053c3" data-entity-type="file" alt="Automatically set the date on web page change detection form" width="1129" height="496" loading="lazy"><p>&nbsp;</p><p>&nbsp;</p><p>Now you can see that the field is correctly set to today's date ( <em>20-1-2025)</em> According to the "Europe/Berlin" timezone)</p><p>&nbsp;</p><p>Entering a timezone is super important, because the server may run in a different timezone than yourself, you can choose any timezone from <a href="https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones">https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones</a></p><p>&nbsp;</p><p>&nbsp;</p><p>As always, Happy web page change detection :)</p><p>&nbsp;</p></div>
 Mon, 20 Jan 2025 11:15:53 +0000Stephen41 at https://changedetection.ioWeb page change monitoring with Webshare proxieshttps://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies
 <span class="field field--name-title field--type-string field--label-hidden">Web page change monitoring with Webshare proxies</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2024-12-27T09:34:13+01:00" title="Friday, December 27, 2024 - 09:34" class="datetime">Fri, 12/27/2024 - 09:34</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>Integrating proxies with Changedetection takes website monitoring to a professional level by addressing challenges like regional restrictions, IP bans, and task scalability. Hereâ€™s how <a href="https://www.webshare.io/">Webshare proxies</a> enhance Changedetection:</p><ul><li><strong>Access Geo-Restricted Websites: </strong>Webshare proxies allow you to bypass regional restrictions by routing your requests through servers in specific locations. For example, if a website is accessible only to users in the US, using a proxy with a US IP address enables Changedetection to monitor that site seamlessly. This feature is invaluable for tracking region-specific content like local promotions, regional news updates, or country-specific pricing changes.</li><li><strong>Avoid IP Restrictions:</strong> Monitoring websites often involves sending frequent or repetitive requests, which may lead to your IP address being flagged or blocked. Webshare proxies mitigate this risk by rotating IP addresses, simulating requests from different users. This approach reduces the likelihood of detection and ensures uninterrupted monitoring, even on sites with strict anti-scraping measures.</li><li><strong>Scale Monitoring Across Multiple Sites: </strong>Tracking multiple web pages simultaneously can overload a single IP address, triggering rate limits or temporary blocks. Webshare proxies distribute these requests across multiple IPs, allowing you to monitor a higher number of pages without disruptions.</li><li><strong>Enhanced Privacy and Security: </strong>Webshare proxies mask your actual IP address, providing an added layer of anonymity and safeguarding your monitoring activities. This protection is crucial when tracking sensitive content, such as competitor websites or exclusive data, where you donâ€™t want your actions to be easily traceable.</li><li><strong>Improved Speed and Reliability: </strong>High-quality Webshare proxies often provide faster and more stable connections than your regular network. This reduces delays in fetching updates and ensures that Changedetection performs consistently, even under heavy monitoring workloads or network fluctuations.</li><li><strong>Ensure Legal and Ethical Compliance: </strong>Webshare proxies enable monitoring activities to comply with regional laws and website policies. By ensuring access through approved regional proxies or adhering to site-specific terms of use, you can conduct ethical monitoring without violating restrictions.</li></ul><p>&nbsp;</p><p>&nbsp;</p><h2>Proxy setup method for beginners</h2><p>When integrating Changedetection with Webshare proxies, we'll cover a general beginner-friendly proxy setup first, followed by an advanced setup using rotating proxies.</p><p>&nbsp;</p><h3>1. Subscribe to Changedetection.io</h3><p>Begin by subscribing to <a href="https://changedetection.io/">Changedetection.io</a>. Once youâ€™ve successfully created an account, youâ€™ll receive your credentials via email. Use these credentials to login and launch the web application in your browser.</p><img src="/sites/changedetection.io/files/inline-images/1-setup\_0.png" data-entity-uuid="d422f7da-0fd4-4ad6-a0e1-e4db6548e4ae" data-entity-type="file" alt="join and setup" width="1179" height="656" class="align-center" loading="lazy"><h3>&nbsp;</h3><h3>2. Access the SETTINGS menu</h3><p>After logging in, navigate to the top menu bar and click on <strong>SETTINGS </strong>to access the configuration options.</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/2-settings.png" data-entity-uuid="043b3d23-99ea-4442-94b7-7ebe0e1fc026" data-entity-type="file" alt="access settings" width="1600" height="427" class="align-center" loading="lazy"><h3>&nbsp;</h3><h3>3. Select the CAPTCHA &amp; Proxies tab</h3><p>Within the settings menu, locate and click on the <strong>CAPTCHA &amp; Proxies</strong> tab. This section allows you to add and manage proxy configurations for your monitoring tasks.</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/3-select.png" data-entity-uuid="d5f15372-9581-474b-bcb6-c11b5a008433" data-entity-type="file" alt="Visit the proxies tab" width="1600" height="682" class="align-center" loading="lazy"><h3>&nbsp;</h3><h3>4. Webshare proxy credentials</h3><p>For Webshare proxies, <a href="https://www.webshare.io/?referral\_code=0yb98y7xwmku">sign up for the free plan</a> to access 10 free datacenter proxies. These proxies are shared, limited to 1GB of bandwidth per month, and include options for both rotating and static configurations. Youâ€™ll find the necessary proxy details (username, password, host, and port) in your Webshare account dashboard.</p><p>Next, we will cover instructions for two different types of proxies - residential and datacenter. Pick one whichever you have subscribed for. The free proxy server plan is using datacenter proxies.</p><h3>&nbsp;</h3><h3>5. Configure residential proxies</h3><p>To configure residential proxies, enter the proxy URL in the recommended format:</p><p><strong>http://username:password@host:port</strong></p><p>For example:</p><p><strong>http://username:password@p.webshare.io:80</strong></p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/5-proxies.png" data-entity-uuid="7e28e711-0758-4ff7-83ff-98b497be1c56" data-entity-type="file" alt="List of residential proxies for web page change detection" width="1061" height="810" loading="lazy"><p>â€</p><p>Replace username, password, host, and port with the details provided by Webshare. Once added, click <strong>Save </strong>to confirm the settings.</p><h3>&nbsp;</h3><h3>6. Configure datacenter proxies</h3><p>To configure datacenter proxies, use the same URL format as above. As an example, hereâ€™s how you can configure a Webshare datacenter proxy:</p><p><strong>http://username:password@198.23.239.134:6540&nbsp;</strong></p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/6a.png" data-entity-uuid="3614be41-180e-4c38-89ca-bd49a49cfb74" data-entity-type="file" alt="Setup datacenter proxies in Webshare" width="1528" height="303" class="align-center" loading="lazy"><p>â€</p><p>Replace the placeholders with your datacenter proxy credentials.&nbsp;</p><h2>&nbsp;</h2><h2>Advanced proxy setup - rotating proxies</h2><p>Hereâ€™s how to set up Webshare rotating proxies in Changedetection:</p><p><strong>Access Webshare Dashboard: </strong>Log in to your Webshare account and navigate to the <strong>Proxy List </strong>section.</p><p><strong>Select Connection and Authentication Method: </strong>Under Connection Method, select <strong>Rotating Proxy Endpoint</strong>. This option ensures a new proxy IP is assigned with each request. For authentication, choose <strong>Username/Password</strong>.</p><img src="/sites/changedetection.io/files/inline-images/6a\_0.png" data-entity-uuid="83e6b01f-c3b0-487f-9188-3e1e5f95fd67" data-entity-type="file" alt="Setup rotating proxies" width="1528" height="303" class="align-center" loading="lazy"><p>&nbsp;</p><p><strong>Copy Proxy Details:</strong> Use the provided details from your Webshare dashboard:</p><p><strong>Domain Name, Proxy Port</strong>, <strong>Proxy Username</strong>, and <strong>Proxy Password.</strong></p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/6b.png" data-entity-uuid="9f5db2c9-ffec-4c49-824f-d80d82288592" data-entity-type="file" alt="Rotating proxies part 2" width="930" height="398" class="align-center" loading="lazy"><p><strong>Add the Proxy URL to Changedetection: </strong>Create the proxy url in the same format as discussed above, enter it under the <strong>Proxy URL</strong> field and click <strong>Save</strong>.</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/6d.png" data-entity-uuid="cf73c8db-1705-470b-a868-097da7e5cc4d" data-entity-type="file" alt="Adding the proxy to changedetection.io" width="1180" height="454" class="align-center" loading="lazy"><p>&nbsp;</p><p>&nbsp;</p><p><strong>Enable Proxies in General Settings</strong></p><ul><li>Go back to the <strong>General </strong>Settings section.</li><li>Scroll down to the Proxy Configuration area.</li><li>Choose your newly added proxies to be used for change detection tasks.</li></ul><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/6e.png" data-entity-uuid="0060e092-94a9-401c-b2c5-ec81813e97d7" data-entity-type="file" alt="Enabling the proxy in changedetection" width="597" height="494" class="align-center" loading="lazy"><p>&nbsp;</p><p>You are now ready to monitor website content changes seamlessly, without geo-restrictions.</p><h2>&nbsp;</h2><h2>Wrapping up</h2><p>Integrating Webshare proxies with Changedetection allows you to overcome regional restrictions, avoid IP bans, and scale monitoring tasks seamlessly. By combining Webshare's reliable proxy services with Changedetection's powerful change-tracking features, you can ensure accurate, uninterrupted and efficient website monitoring.&nbsp;</p></div>
 Fri, 27 Dec 2024 08:34:13 +0000Stephen39 at https://changedetection.ioHow to Monitor Government Agency News, Resources â€” A Legal Professionalâ€™s Perspectivehttps://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective
 <span class="field field--name-title field--type-string field--label-hidden">How to Monitor Government Agency News, Resources â€” A Legal Professionalâ€™s Perspective</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2024-12-20T18:27:52+01:00" title="Friday, December 20, 2024 - 18:27" class="datetime">Fri, 12/20/2024 - 18:27</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>&nbsp;</p><p><strong>Leverage changedetection.io for Timely, Accurate Intelligence</strong></p><p>As a legal professional, you understand that staying on top of regulatory updates isnâ€™t just a matter of convenience; itâ€™s integral to offering informed guidance to your team and clients. Missing a crucial regulatory shift can quickly transform a well-prepared argument or strategy into outdated advice. Government agencies roll out changes with an almost dizzying frequency, and itâ€™s not always easy to catch every subtle tweak or new bulletin.</p><p>But who has time to constantly refresh a dozen agency websites? Hunting down these changes manually is inefficient, and relying on broad email newsletters often means wading through irrelevant noise. Instead, let changedetection.io be your digital â€œassociateâ€â€”quietly monitoring the pages you care about, and reporting back only when something meaningful happens.</p><p>&nbsp;</p><h3>How Does changedetection.io Work?</h3><p>&nbsp;</p><p><strong>Simple, Targeted Website Change Monitoring</strong></p><p>changedetection.io automates the entire process of staying updated. Think of it as an online watchdog that scans your chosen websites at set intervals and flags even the smallest adjustments. Whenever a change is detected, you receive a clear, concise alertâ€”with any new text or removed language highlightedâ€”so you can review it at a glance and understand how it might impact your practice.</p><p>For legal professionals, this can mean:</p><ul><li>Quickly identifying new guidelines issued by regulatory bodies.</li><li>Spotting changes to statutes, administrative rules, and compliance mandates.</li><li>Interpreting updates in real-time, so you can advise your clients or partners without delay.</li></ul><p>You can also refine your monitoring with keyword alerts, ensuring youâ€™re alerted only when specific terms related to your practice area appear or disappear.</p><p>&nbsp;</p><h3>What Web Pages Can I Track with changedetection.io?</h3><p>The beauty of changedetection.io is its flexibility. You can track almost any publicly accessible webpage, including (but certainly not limited to):</p><ul><li>Federal agency newsrooms and press release pages.</li><li>State-level regulatory boards and commissions.</li><li>Agency â€œWhatâ€™s New?â€ or â€œUpdatesâ€ sections, from environmental guidelines to health policy changes.</li><li>Government licensing boards and professional standards portals.</li></ul><p>In other words, if itâ€™s an authoritative online source for legal or regulatory content, changedetection.io can almost certainly keep an eye on it for you.</p><p>&nbsp;</p><h3>How can changedetection.io can help my team? Can it communicate with Slack or Microsoft teams?<br>&nbsp;</h3><p>You can also step up your notification game by integrating changedetection.io alerts with various third-party platforms for real-time updates. We support just about every notification service imaginableâ€”your legal team can get notified directly through preferred channels, such as Microsoft Teams, Slack, or even SMS. This means the instant changedetection.io spots a legislative update that affects your practice area, your whole team can be pinged in the collaboration hub they already use every day, ensuring no one misses a beat and making rapid, well-informed decision-making easier than ever.</p><p>Keeping the information in your communication platform helps to keep your team working smoother - together. No more hiding or losing updates in one persons email.</p><p>What's more, you can keep the noise to a minimum and only<a href="https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule"> recheck important webpages for a change according to a schedule (say you just want an overview at 0900h every work day morning)</a>.</p><p>&nbsp;</p><h3>Legislative Changes are Endless, but Manageable â€“ With changedetection.io</h3><p>In a world where the regulatory landscape can pivot with little notice, having a digital ally to keep you informed is a game-changer. Instead of missing updates because you were tied up in a deposition or sifting through irrelevant newsletters, changedetection.io frees you to focus on applying the lawâ€”not chasing it.</p><p>By automating the watch for agency announcements, new rules, and policy adjustments, changedetection.io provides the timely intelligence you need to confidently advise your clients and maintain a competitive edge. Itâ€™s like having an extra pair of eyes dedicated solely to scanning the horizon for any shift that could matter to your practice.</p><p>&nbsp;</p><p><strong>Ready to Keep Pace with Change?</strong><br>Sign up for changedetection.io, and get the updates you needâ€”exactly when you need themâ€”straight from the sources you trust.</p><p>&nbsp;</p></div>
 Fri, 20 Dec 2024 17:27:52 +0000Stephen38 at https://changedetection.io

---

### Proxies
Original URL: https://changedetection.io/taxonomy/term/5/feed

Proxieshttps://changedetection.io/
 en-gbUsing Bright Data's "Scraping Browser" to by-pass CAPTCHA's and other protection when monitoring pageshttps://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring
 <span class="field field--name-title field--type-string field--label-hidden">Using Bright Data&#039;s &quot;Scraping Browser&quot; to by-pass CAPTCHA&#039;s and other protection when monitoring pages</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2024-11-16T17:39:50+01:00" title="Saturday, November 16, 2024 - 17:39" class="datetime">Sat, 11/16/2024 - 17:39</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 <div class="field\_\_item"><a href="/topic/proxies" hreflang="en-gb">Proxies</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>For many websites - simply using a proxy is not enough, the website is using much more complex anti-robot software to detect the actual browser that is being used, not just the IP connection or headers (including common headers such as user-agent and others)</p><p>You need a better way to simulate a real browser - A scraping browser is different to a proxy, a proxy just tunnels your connection but the Browser still looks the same, with a scraping browsers you are also simulating a real browser hidden away in Bright Data's infrastructure.</p><p>As it turns out, many websites are probing much deeper into your browser - analysing the response from your 2D and 3D/GPU videocard is just one of the tactics they use.</p><p>Unfortunately for many headless Chrome sessions it means they stand out all too easy - their "fingerprint" is just too obvious, they dont have anything that resembles a real video card or other hardware attached.</p><p>The result is - you get pushed to enter a CAPTCHA or other similar anti-robot mechanism.</p><p><em><strong>But there is a solution, </strong></em>whilst not guaranteed - it definitely helps a lot!&nbsp;</p><p>The clever people over at Bright Data have added a "Scraping Browser" to their offers, which more precisely simulates a real browser than just about anything you can try to run yourself.</p><p>(note: this functionality in changedetection.io will be released late November 2023, but you can try it now under the current<em> master </em>tag from our <a href="https://github.com/dgtlmoon/changedetection.io">GitHub</a> or <a href="https://hub.docker.com/layers/dgtlmoon/changedetection.io/dev/images/sha256-2397ad50a81527514492e859da685dada3863659b1e233f8e8f020eb08af0da0?context=explore">dev tag from our Docker Hub</a>)<br>&nbsp;</p><p>More information about <a href="https://brightdata.com/products/scraping-browser">Bright Data's scraping browser can be found here.</a></p><h4>&nbsp;</h4><h4><em><strong>Here's how to setup Bright Data's "Scraping Browser" with changedetection.io</strong></em></h4><p>&nbsp;</p><p>Head on over to your Bright Data <em><strong>control panel</strong></em> - When you sign up using this link - &nbsp;<a href="https://brightdata.grsm.io/n0r16zf7eivq">https://brightdata.grsm.io/n0r16zf7eivq</a> - BrightData will match any first deposit up to $150.</p><p>Once logged in - click on <em><strong>"Scraping Browser"</strong></em></p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_28.png" data-entity-uuid="30783e83-19fa-4607-ba8e-b03f3c5b7512" data-entity-type="file" alt="The Bright Data control panel - where to find the Scraping Browser link" width="690" height="650" loading="lazy"><p>&nbsp;</p><p>Now we will copy the special "Connection address" so changedetection.io knows how to find the Scraping Browser, click on <strong>Check out code and integration examples o</strong>n the bottom right.</p><p>It's also worth considering here that you can add on extra residential proxies , residential proxies also greatly increase your chance of skipping past any potential CAPTCHA issues, but for now we will continue with the default setup.</p><p><br><img src="/sites/changedetection.io/files/inline-images/image\_33.png" data-entity-uuid="5e39f204-0e15-464b-af15-eeb285f708ce" data-entity-type="file" alt="The Bright Data control panel - where to find the Scraping Browser link" width="1153" height="720" loading="lazy"></p><p>&nbsp;</p><p>Copy the text from the next page into your clipboard, it will start with <strong>wss://</strong>, be sure to not include any quotes or other text, copy the whole text which is marked in blue below.</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_34.png" data-entity-uuid="d90064d8-1c18-428b-a0f3-0dbc1af510f9" data-entity-type="file" alt="The Bright Data control panel - where to find the Scraping Browser wss:// link for changedetection" width="708" height="577" loading="lazy"><p>&nbsp;</p><p>Now for the fun part, jump over to &nbsp;your changedetection.io login and click on <strong>Settings &gt; CAPTCHA &amp; Proxies, </strong>scroll down to the <em><strong>"Extra Browsers" </strong></em>section, give your browser a name (in this case just <strong>BrightData Scraping Browser</strong> and paste the <strong>wss://... </strong>type URL into the <strong>Connection URL</strong> box</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_37.png" data-entity-uuid="36d00f7f-75c1-4ea3-8f69-932860d716ea" data-entity-type="file" alt="Adding a scraping browser to changedetection.io - step 1 adding the browser link" width="988" height="608" loading="lazy"><p>&nbsp;</p><p>Now to use your new Scraping Browser with any website you are watching for changes, simply click <strong>Edit</strong> in your overview list and select the new browser&nbsp;</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_39.png" data-entity-uuid="03bf5840-30f9-41ef-92dc-34770ba222da" data-entity-type="file" alt="list of websites with changes overview" width="860" height="155" loading="lazy"><p>&nbsp;</p><p>Choose the new browser <strong>Bright Data Scraping Browser</strong> that we setup in the previous step.</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_40.png" data-entity-uuid="36c2bac5-dc00-4125-8278-57e55d5cd53a" data-entity-type="file" alt="Setting a single website to use a particular scraping browsers" width="814" height="386" loading="lazy"><p>&nbsp;</p><p>And there you have it - <em>how to setup a scraping browser to get a much better success rate (say goodbye CAPTCHA!) when watching websites for changes.</em></p><p>&nbsp;</p><p><em>Some extra tips -</em></p><p>When you setup additional Residential Proxies - Bright Data will present you with a new "wss://.." type connection URL, so you can then setup multiple proxy networks with multiple scraping browsers.</p><p>Sign up with Bright Data using <a href="https://brightdata.grsm.io/n0r16zf7eivq">https://brightdata.grsm.io/n0r16zf7eivq</a> BrightData will match any first deposit up to $150</p><p>&nbsp;</p><h3>Troubleshooting&nbsp;</h3><p>If you see the error &nbsp;"<code>Overriding accept-language, user-agent headers forbidden</code>" - &nbsp;You may need to enable "<em>Custom headers</em>" - In your Brightdata dashboard - under the <code>Proxy Settings</code> &gt; <code>Configuration</code> &gt; <code>Advanced Settings</code> &gt; <code>Custom headers &amp; cookies</code> this option needs to be activated. (changedetection.io may send its own custom User-Agent and other headers)<br><br>If you receive an error like <code>"WebSocket error: wss://brd-customer..... 403 wrong\_auth"</code> then try whitelisting the IP of our server (or your local connection) from inside the BrightData control panel at the "Scraping Browser" settings - as an alternative to username+password (But still keep the username+password in the <code>wss://.. </code>connection URL)</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_52.png" data-entity-uuid="941c5e34-0be0-4861-8e65-fa61d518fb7e" data-entity-type="file" alt="Example of adding a white-list IP access in BrightData for the scraping browser" width="400" height="363" loading="lazy"><p>Happy changedetecting!</p><p>&nbsp;</p><p><strong>extra points! </strong>You can now use the built-in proxy scanner to see which websites still give the 403 access denied error, check it out here <a href="https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner">https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner</a></p><p><video style="max-width:80%;" autoplay loop muted playsinline>
 <source src="/sites/changedetection.io/files/2025-04/403-access-denied-proxy-scanner.webm" type="video/webm">
 Your browser does not support the video tag.
 </video></p><p>&nbsp;</p></div>
 Sat, 16 Nov 2024 16:39:50 +0000Stephen24 at https://changedetection.ioHow to - Bright Data Proxies and changedetection.iohttps://changedetection.io/tutorial/how-bright-data-proxies-and-changedetectionio
 <span class="field field--name-title field--type-string field--label-hidden">How to - Bright Data Proxies and changedetection.io</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2023-08-02T17:36:12+02:00" title="Wednesday, August 2, 2023 - 17:36" class="datetime">Wed, 08/02/2023 - 17:36</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 <div class="field\_\_item"><a href="/topic/proxies" hreflang="en-gb">Proxies</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><img src="/sites/changedetection.io/files/inline-images/image\_4\_0.png" data-entity-uuid="f5cb04c0-6de0-461b-b245-cde99e52b47a" data-entity-type="file" width="588" height="753" loading="lazy"><p><br>Using Bright Data proxies with changedetection.io is super beneficial for accessing web pages from different countries and bypassing blocking rules for several reasons:</p><ol><li><strong>Geographical Location</strong>: Proxies allow you to route your web requests through servers located in different countries. By doing so, you can effectively appear as if you are accessing the web from that specific country. This is useful for accessing geo-restricted content or services that are only available to users in certain regions.</li><li><strong>Bypassing IP Restrictions</strong>: Some websites implement IP-based restrictions to limit access to their content or prevent excessive requests from the same IP address. Proxies help you overcome these restrictions by changing your IP address, so you can access the website as if you were coming from a different IP.</li><li><strong>Overcoming Censorship</strong>: In regions with strict internet censorship, certain websites and online services may be blocked by the government or internet service providers. Proxies can help users bypass such censorship and access blocked content.</li><li><strong>Anonymity and Privacy</strong>: Proxies provide an extra layer of anonymity by masking your original IP address. This can be valuable for users who want to protect their online privacy and avoid being tracked by websites or third parties.</li><li><strong>Load Distribution</strong>: When accessing websites through proxies, the load is distributed across multiple servers. This can help prevent server overload and improve the overall performance and speed of web scraping or data collection activities.</li><li><strong>Scalability</strong>: Proxies allow you to scale your web scraping or data collection efforts by making multiple requests from different IP addresses. This helps avoid getting blocked by websites that have rate-limiting or anti-scraping measures in place.</li><li><strong>Legal and Ethical Compliance</strong>: Proxies can be used to access websites in a manner that is compliant with their terms of service and legal regulations. By rotating IP addresses and not overloading servers, you can ensure responsible data collection practices.</li></ol><p>&nbsp;</p><p><em>It's super easy to connect Bright Data proxies to your changedetection.io account or installation, head on over to </em><a href="https://brightdata.com/integration/changedetection"><em><strong>https://brightdata.com/integration/changedetection</strong></em></a><em> to find out more!</em></p><p>&nbsp;</p></div>
 Wed, 02 Aug 2023 15:36:12 +0000Stephen13 at https://changedetection.io

---

### Browser Steps
Original URL: https://changedetection.io/taxonomy/term/6/feed

Browser Stepshttps://changedetection.io/
 en-gbWebsite content change detection from behind logins - easyhttps://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy
 <span class="field field--name-title field--type-string field--label-hidden">Website content change detection from behind logins - easy</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2023-08-13T18:46:53+02:00" title="Sunday, August 13, 2023 - 18:46" class="datetime">Sun, 08/13/2023 - 18:46</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 <div class="field\_\_item"><a href="/topic/browser-steps" hreflang="en-gb">Browser Steps</a></div>
 <div class="field\_\_item"><a href="/topic/use-case" hreflang="en-gb">Use-case</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>Another great feature of changedetection.io is that you can interact with websites to compare their content.</p><p>Often you need to enter in some search query or need to access a page that's only available from behind a login/password form.</p><p>Or maybe perform change detection from behind password protected websites?</p><p><em><strong>Note: &nbsp;Only use this on websites where you have permission todo so, and always "recheck" with the maximum realistic time between rechecks, logging-in every minute could get you blocked from the site you are viewing.</strong></em></p><p>Some examples where this is super handy could be</p><ul><li>Get an alert when a new invoice is available</li><li>Get an alert when your school publishes new important information.</li><li>Accept cookie popup forms</li><li>Log in to a website to be able to scrape data for other uses (for example you could now make a nice Discord bot that reports new articles that appear from behind a login)</li></ul><p>&nbsp;</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_12.png" data-entity-uuid="d50b6058-ec1c-4e35-af93-8fd11531545b" data-entity-type="file" alt="Screenshot for supplying login details to perform change detection from behind a login" width="766" height="785" loading="lazy"><p>&nbsp;</p><p>Changedetection.io makes this super easy by providing an easy to use setup page where you can click on individual elements on the page and then enter in the kind of event you want to happen, changedetection.io will automatically detect which action is best for whatever element you selected (for example, enter text in field, click buttons etc)</p><p>&nbsp;</p><p>You could even use this to perform realestate searches, searching for your dream job and more, it's all up to your imagination!&nbsp;</p><p>&nbsp;</p><p>I recommend that you explore this feature, it's so super helpful!</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p></div>
 Sun, 13 Aug 2023 16:46:53 +0000Stephen17 at https://changedetection.io

---

### RegTech
Original URL: https://changedetection.io/taxonomy/term/7/feed

RegTechhttps://changedetection.io/
 en-gbGot RegTech? Using website change detection to monitor for changes in regulations.https://changedetection.io/tutorial/got-regtech-using-website-change-detection-monitor-changes-regulations
 <span class="field field--name-title field--type-string field--label-hidden">Got RegTech? Using website change detection to monitor for changes in regulations.</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2023-08-21T23:05:04+02:00" title="Monday, August 21, 2023 - 23:05" class="datetime">Mon, 08/21/2023 - 23:05</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 <div class="field\_\_item"><a href="/topic/regtech" hreflang="en-gb">RegTech</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>&nbsp;</p><p><a href="https://www.mas.gov.sg/development/fintech/technologies---regtech"><em>RegTech</em></a> is the use of technology to enhance risk management and regulatory compliance in financial institutions.</p><p><br>Website change detection is a crucial component of a regulatory intelligence solution, helping you stay ahead of regulatory changes and inform your clients before they become aware of these changes. Here's how website change detection can specifically assist in achieving this goal:</p><p>&nbsp;</p><ol><li><strong>Real-time Monitoring:</strong> Website change detection tools continuously monitor regulatory websites, government portals, and industry-specific sites in real-time. This ensures that any updates, amendments, or new regulations are promptly identified.</li><li><strong>Early Detection:</strong> By instantly identifying changes on relevant websites, website change detection allows the regulatory intelligence solution to detect regulatory updates as soon as they are published. This enables the solution to act faster than clients who might rely on periodic checks.</li><li><strong>Instant Alerts:</strong> When a change is detected, the website change detection solution can immediately send automated alerts and notifications to clients. This provides clients with early awareness of regulatory changes and enables them to take proactive measures.</li><li><strong>Competitive Advantage:</strong> Informing clients about regulatory changes before they discover them themselves can provide your solution users with a competitive advantage. They can adjust their strategies, operations, and compliance efforts ahead of competitors, positioning themselves as leaders in their industries.</li><li><strong>Customized Monitoring:</strong> Website change detection tools can be configured to monitor specific regulatory websites, keywords, or topics relevant to your clients' industries. This customization ensures that clients receive tailored information that directly impacts their operations.</li><li><strong>Comprehensive Coverage:</strong> Regulatory information might be scattered across numerous websites. Website change detection tools ensure comprehensive coverage by monitoring a wide range of sources simultaneously, reducing the risk of missing critical updates.</li><li><strong>Data Accuracy:</strong> Website change detection tools employ advanced algorithms to accurately identify changes, eliminating the risk of human error that might occur during manual monitoring. This ensures that clients receive accurate and reliable information, however this depends on many factors.</li><li><strong>Risk Mitigation:</strong> By notifying clients about regulatory changes early, the regulatory intelligence solution helps them mitigate risks associated with non-compliance or outdated practices. Clients can address these changes proactively and avoid potential penalties.</li><li><strong>Enhanced Client Relationships:</strong> Providing clients with early and valuable insights into regulatory changes enhances your solution's value proposition. It builds trust and strengthens your client relationships as they rely on your solution to keep them well-informed.</li><li><strong>Strategic Decision-Making:</strong> Clients armed with early knowledge of regulatory changes can make informed strategic decisions. They can align their business plans, resource allocation, and compliance strategies with the evolving regulatory landscape.</li><li><strong>Efficiency and Time Savings:</strong> Website change detection automates the monitoring process, saving clients time and resources that would otherwise be spent manually tracking regulatory websites. This efficiency allows them to focus on more strategic tasks.</li><li><strong>Continuous Compliance:</strong> The proactive nature of the regulatory intelligence solution, powered by website change detection, helps clients maintain continuous compliance with regulatory changes, reducing the risk of sudden disruptions to their operations.</li></ol><p>&nbsp;</p><p>Incorporating website change detection into your regulatory intelligence solution transforms it into a proactive tool that empowers clients with timely and actionable regulatory insights. This proactive approach enhances their regulatory preparedness and fosters a strong partnership between your solution and your clients.</p></div>
 Mon, 21 Aug 2023 21:05:04 +0000Stephen18 at https://changedetection.io

---

### Use-case
Original URL: https://changedetection.io/taxonomy/term/8/feed

Use-casehttps://changedetection.io/
 en-gbAwesome use-case #4,510: How to get notified when Hetzner servers and products are availablehttps://changedetection.io/tutorial/awesome-use-case-4510-how-get-notified-when-hetzner-servers-and-products-are-available
 <span class="field field--name-title field--type-string field--label-hidden">Awesome use-case #4,510: How to get notified when Hetzner servers and products are available</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2023-09-24T17:17:51+02:00" title="Sunday, September 24, 2023 - 17:17" class="datetime">Sun, 09/24/2023 - 17:17</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 <div class="field\_\_item"><a href="/topic/use-case" hreflang="en-gb">Use-case</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>We all love <a href="https://www.hetzner.com/">Hetzner</a> for their excellent pricing and solid offers - but how to get a notification when one of their amazing servers comes back in stock?</p><p><a href="https://www.hetzner.com/">Hetzner</a> is a well-regarded hosting and cloud service provider known for offering reliable and high-quality hosting solutions. There are several reasons why Hetzner servers are often praised for their great service, Cost-effective pricing, robust infrastructure, multiple data-centres, incredible network performance and great customer service.</p><p>But the real heartbreak is when you are hunting for your dream <a href="https://www.hetzner.com/dedicated-rootserver?">Hetzner Dedicated Server</a> only to find out that it's not available and that there's no good way to get alerts or notifications when Hetzner effectively "restock" that type of server.</p><p>Changedetection.io to the rescue :)</p><img src="/sites/changedetection.io/files/inline-images/image\_18.png" data-entity-uuid="7493c00b-6581-4032-8475-12dbc59234f6" data-entity-type="file" alt="Screenshot of Hetzner website as an example for change detection" width="780" height="585" loading="lazy"><p>&nbsp;</p><p>&nbsp;</p><h2>How to get notifications or alerts when Hetzner servers are available to buy</h2><p>Fortunately, Hetzner are super internet-friendly and make it easy to copy the link to the filters, you will need this link, place this link into changedetection.io</p><p>&nbsp;</p><p><em><strong>First</strong></em>, search for your <strong>Dedicated Server </strong>at <strong>Hetzner</strong>, you should see a <em><strong>"No server found"</strong></em> message on the <em>Hetzner server listing page</em>, this may also work for other servers at Hetzner. In our example we searched for a AMD based server, at the time of writing this tutorial, there were no AMD based servers available.&nbsp;</p><p><em><strong>Second</strong></em>, copy and paste the Filter URL into changedetection.io and hit <strong>Watch</strong></p><img src="/sites/changedetection.io/files/inline-images/image\_19.png" data-entity-uuid="c804adbf-fc72-420e-9577-f9531708d012" data-entity-type="file" alt="Adding the website to the change detection monitoring list" width="938" height="212" loading="lazy"><p>&nbsp;</p><p><em><strong>Third and final</strong></em>, that's it!</p><img src="/sites/changedetection.io/files/inline-images/image\_20.png" data-entity-uuid="01c3ba88-2ae0-4a51-9b22-5d447064e1de" data-entity-type="file" alt="List of websites ready for change monitoring" width="1055" height="187" loading="lazy"><p>&nbsp;</p><p><strong>Extra points!</strong>&nbsp;</p><p>And ofcourse, you can jump over to to the <strong>\[edit\]</strong> tab and setup your <strong>notifications</strong>, remember, changedetection.io is not just about sending an email, but more useful is to trigger a message to your <strong>Discord</strong> channel and let your whole team know that the server you guys are hunting for is now available at <strong>Hetzner</strong>!</p><p>And ofcourse, through the magic of Apprise, changedetection.io supports more than 80 different kinds of notifications, including Slack, MS Teams, RockChat and more. PLUS you can also attach a screenshot!</p><img src="/sites/changedetection.io/files/inline-images/image\_21.png" data-entity-uuid="fe784237-24b3-448c-89bd-97b56ded9272" data-entity-type="file" alt="Notifications for website change monitoring" width="1071" height="362" loading="lazy"><p>( See our docs links and tutorials for getting your Discord API link :) )</p><p><br><strong>Extra extra points!</strong><br>&nbsp;</p><p>Want to be MORE specific? You can even use the <strong>Visual Selector</strong> or <strong>Browser Steps</strong> tabs to click on items, and/or specifically focus on parts of the page - ensuring you get only the relevant notifications when Hetzner update their product availability :)</p><p>&nbsp;</p><p>thanks for reading!<br>&nbsp;</p></div>
 Sun, 24 Sep 2023 15:17:51 +0000Stephen19 at https://changedetection.ioWebsite content change detection from behind logins - easyhttps://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy
 <span class="field field--name-title field--type-string field--label-hidden">Website content change detection from behind logins - easy</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2023-08-13T18:46:53+02:00" title="Sunday, August 13, 2023 - 18:46" class="datetime">Sun, 08/13/2023 - 18:46</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/how" hreflang="en-gb">How-To</a></div>
 <div class="field\_\_item"><a href="/topic/browser-steps" hreflang="en-gb">Browser Steps</a></div>
 <div class="field\_\_item"><a href="/topic/use-case" hreflang="en-gb">Use-case</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>Another great feature of changedetection.io is that you can interact with websites to compare their content.</p><p>Often you need to enter in some search query or need to access a page that's only available from behind a login/password form.</p><p>Or maybe perform change detection from behind password protected websites?</p><p><em><strong>Note: &nbsp;Only use this on websites where you have permission todo so, and always "recheck" with the maximum realistic time between rechecks, logging-in every minute could get you blocked from the site you are viewing.</strong></em></p><p>Some examples where this is super handy could be</p><ul><li>Get an alert when a new invoice is available</li><li>Get an alert when your school publishes new important information.</li><li>Accept cookie popup forms</li><li>Log in to a website to be able to scrape data for other uses (for example you could now make a nice Discord bot that reports new articles that appear from behind a login)</li></ul><p>&nbsp;</p><p>&nbsp;</p><img src="/sites/changedetection.io/files/inline-images/image\_12.png" data-entity-uuid="d50b6058-ec1c-4e35-af93-8fd11531545b" data-entity-type="file" alt="Screenshot for supplying login details to perform change detection from behind a login" width="766" height="785" loading="lazy"><p>&nbsp;</p><p>Changedetection.io makes this super easy by providing an easy to use setup page where you can click on individual elements on the page and then enter in the kind of event you want to happen, changedetection.io will automatically detect which action is best for whatever element you selected (for example, enter text in field, click buttons etc)</p><p>&nbsp;</p><p>You could even use this to perform realestate searches, searching for your dream job and more, it's all up to your imagination!&nbsp;</p><p>&nbsp;</p><p>I recommend that you explore this feature, it's so super helpful!</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p></div>
 Sun, 13 Aug 2023 16:46:53 +0000Stephen17 at https://changedetection.io

---

### Knowledge base
Original URL: https://changedetection.io/taxonomy/term/9/feed

Knowledge basehttps://changedetection.io/
 en-gbWhat are the main types of anti-robot mechanisms?https://changedetection.io/tutorial/what-are-main-types-anti-robot-mechanisms
 <span class="field field--name-title field--type-string field--label-hidden">What are the main types of anti-robot mechanisms?</span>
<span class="field field--name-uid field--type-entity-reference field--label-hidden"><a title="View user profile." href="/tech-writer/stephen" class="username">Stephen</a></span>
<span class="field field--name-created field--type-created field--label-hidden"><time datetime="2024-05-20T14:48:57+02:00" title="Monday, May 20, 2024 - 14:48" class="datetime">Mon, 05/20/2024 - 14:48</time>
</span>

 <div class="field field--name-field-topic field--type-entity-reference field--label-above">
 <div class="field\_\_label">Topic</div>
 <div class='field\_\_items'>
 <div class="field\_\_item"><a href="/topic/knowledge-base" hreflang="en-gb">Knowledge base</a></div>
 </div>
 </div>

 <div class="clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field\_\_item"><p>You may have read a lot about some tricks to defeat scraping such as changing your scraping browser's "User Agent" settings, however that's only the start of the story.</p><p><img src="/sites/changedetection.io/files/inline-images/image\_80.png" data-entity-uuid="c5e1bef5-4dc4-46a7-98de-fb8979ace16f" data-entity-type="file" width="204" height="207" alt="anti-robot blocker" class="align-right" loading="lazy"></p><p>In reality there are multiple ways that a service can detect your scraping attempts, changing the user-agent is just a small trick that may or may not help.</p><p>&nbsp;</p><p>It's important to look at the whole session not with just "am I detected or not" perspective, but as a<em><strong> score between 1 and 10</strong></em>, with 10 being "looks like a robot!" and 1 being "hey nice browser and pretty human!"</p><p>&nbsp;</p><p>So let's break it down a bit further, what are the main factors?</p><h3>&nbsp;</h3><h3>Browser fingerprinting</h3><p><em>Anti-robot score importance: <strong>High</strong></em></p><p>This is a tricky subject, as it's probably the fastest evolving part of anti-robot technologies, so we'll break it down into a few parts.</p><p>&nbsp;</p><h5>Browser headers - User Agent</h5><p><em>Anti-robot score importance: <strong>Medium/Low</strong></em></p><p>Headers such as "User agent" are sent on request, and may identify you as a robot, the problem is that since Chrome 89 there's a <strong>new subset of headers </strong>that are sent...</p><p><a href="https://developer.chrome.com/docs/privacy-security/user-agent-client-hints">https://developer.chrome.com/docs/privacy-security/user-agent-client-hints</a></p><p>Browsers also emit such headers as "<code>Sec-CH-UA</code>", not just simple old school "User agent" headers.<br>&nbsp;</p><p>For example;</p><p><code>Sec-CH-UA: "Chromium";v="93", "Google Chrome";v="93", " Not;A Brand";v="99"</code><br><code>Sec-CH-UA-Mobile: ?0</code><br><code>Sec-CH-UA-Platform: "macOS"</code></p><p>Fortunately these can be turned off with the Chrome flag <code>--disable-features=UserAgentClientHint</code><br>&nbsp;</p><p>So just overriding the "User-agent" header without disabling this increases the chances of being detected as a robot, but so does disabling the feature altogether..</p><h5>&nbsp;</h5><h5>Browser TLS/SSL/TCP-IP fingerprinting</h5><p>&nbsp;</p><p><em>Anti-robot score importance: <strong>Medium/High</strong></em></p><p>There also exists a few methods to fingerprint the actual connection "pattern" that the browser makes when performing the SSL connection with the webserver, JA3 and now JA4+ are just one of many libraries/methods out there that perform this.</p><p>Because the browser is compiled with a certain set/versions of SSL libraries, the connection itself from the browser can be fingerprinted</p><p>More here <a href="https://github.com/salesforce/ja3">https://github.com/salesforce/ja3</a></p><blockquote><p><em><strong>"TLS and itâ€™s predecessor, SSL, I will refer to both as â€œSSLâ€ for simplicity, are used to encrypt communication for both common applications, to keep your data secure, and malware, so it can hide in the noise. To initiate a SSL session, a client will send a SSL Client Hello packet following the TCP 3-way handshake. This packet and the way in which it is generated is dependant on packages and methods used when building the client application. The server, if accepting SSL connections, will respond with a SSL Server Hello packet that is formulated based on server-side libraries and configurations as well as details in the Client Hello. Because SSL negotiations are transmitted in the clear, itâ€™s possible to fingerprint and identify client applications using the details in the SSL Client Hello packet."</strong></em><br><br><strong>"With JA3S it is possible to fingerprint the entire cryptographic negotiation between client and it's server by combining JA3 + JA3S. That is because servers will respond to different clients differently but will always respond to the same client the same."</strong></p></blockquote><p>We're not aware of an easy work-around for this case, however perhaps using a specialist proxy service or other could help, this espicially affects Puppeteer type browsers that are all shipped with similar SSL/chrome libraries</p><h5>&nbsp;</h5><h5>Browser fingerprinting in general</h5><p>&nbsp;</p><p><em>Anti-robot score importance: <strong>Medium</strong></em></p><p>There are many technologies here, for example some anti-robot services will attempt to detect the actual hardware you're running on and compare that against a database of known configurations, if it looks "weird" it will increase your robot rating</p><p>&nbsp;</p><h3>The IP address that you're calling from</h3><p><em>Anti-robot score importance: <strong>Medium</strong></em></p><p><em>IP address</em> plays a fairly important role, many services such as Cloudflare protect their customers by rating the IP address you are calling from, if you are calling from a cheap data-centre proxy for example (the most common kind of paid proxy), they already know their IP ranges and will rate the possibility higher that you're a robot.</p><p>Use quality residential proxies, preferably via a "SOCKS" connection so that it does not relay to the remote end that you're even using a proxy.</p><p>&nbsp;</p><h3>Scraping behaviour in general</h3><p><em>Anti-robot score importance: <strong>Low</strong></em></p><p>With computing power being quite high and costs cheap, this is not as important as it used to be, but many services will block you if you scrape too many pages concurrently or too fast sequentially, always be a "good internet scraper" and limit your scraping methods.</p><p>&nbsp;</p><h3>Deny-at-start and allow-later</h3><p><em>Anti-robot score importance: <strong>Hard to say</strong></em></p><p>Some services assume EVERYONE is a robot, and block you at the start then use some fingerprinting to identify you going forwards, this is usually some kind of CAPTCHA or other process, then the browser is fingerprinted and you're allowed in there on.</p><p>&nbsp;</p></div>
 Mon, 20 May 2024 12:48:57 +0000Stephen33 at https://changedetection.io

---

### Page not found | changedetection.io
Original URL: https://changedetection.io/TechRadar%20pro%20-%20Best%20website%20page%20change%20detection

[Skip to main content](https://changedetection.io/TechRadar%20pro%20-%20Best%20website%20page%20change%20detection#main-content)

# 404

But don't give up hope, keep exploring :)

Never stop monitoring the web for changes.

---

### Stephen | changedetection.io
Original URL: https://changedetection.io/tech-writer/stephen

[Skip to main content](https://changedetection.io/tech-writer/stephen#main-content)

![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)

About

Meet Stephen Mercer, our valued technical blog writer with an impressive 25 years of hands-on experience in the open source technology landscape. Stephen's wealth of practical knowledge and down-to-earth approach make him an invaluable member of our team. His writing not only reflects his technical expertise but also his ability to break down complex concepts in a clear and accessible manner, fostering a deeper understanding among readers.

Beyond the tech world, Stephen has a passion for exploration and sunny escapades, particularly in destinations like Las Palmas. His knack for finding inspiration in diverse experiences adds a unique and refreshing perspective to his writing. Stephen Mercer's commitment to making technology more approachable and his cool and collected demeanor make him a standout contributor to our technical blog, ensuring that readers not only grasp the intricacies of open source but also find enjoyment in the journey.

## Articles

[How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)

[Find the best proxy to beat "403 access denied" with our proxy scanner](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)

[How To Monitor Keywords On Any Website](https://changedetection.io/tutorial/how-monitor-keywords-any-website)

[Conditional actions on web page changes!](https://changedetection.io/tutorial/conditional-actions-web-page-changes)

[NÃ¼rburgring racing passion - Get notified of news updates today from NÃ¼rburgring!](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring)

[BestBuy restock alerts - GeForce RTX 5090 & GeForce RTX 5080 are out!](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)

[Kmart Shopping - Easily monitor prices and get restock alerts via email, discord, and others.](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others)

[Pre-fill dynamic form "date" fields and get web page change alerts](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts)

[Web page change monitoring with Webshare proxies](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies)

[How to Monitor Government Agency News, Resources â€” A Legal Professionalâ€™s Perspective](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective)

[Checking web pages for changes according to a schedule](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule)

[Using Bright Data's "Scraping Browser" to by-pass CAPTCHA's and other protection when monitoring pages](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring)

[Email notification when a web page changes - How To](https://changedetection.io/tutorial/email-notification-when-web-page-changes-how)

[Monitoring HTML "SELECT" drop down for changes to options](https://changedetection.io/tutorial/monitoring-html-select-drop-down-changes-options)

[Vevor Tools - easily monitor restock and get alerts on discounts!](https://changedetection.io/tutorial/vevor-tools-easily-monitor-restock-and-get-alerts-discounts)

[What are the main types of anti-robot mechanisms?](https://changedetection.io/tutorial/what-are-main-types-anti-robot-mechanisms)

[Synology NAS - How to get alerts on new software updates via Discord!](https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord)

---

### Browser Steps | changedetection.io
Original URL: https://changedetection.io/topic/browser-steps

[Skip to main content](https://changedetection.io/topic/browser-steps#main-content)

# Changedetection.io Tutorials - Browser Steps

- [![Login box](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/login-box.jpg?itok=VQ8duH9Z)](https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy)





[Website content change detection from behind logins - easy](https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy)







Another great feature of changedetection.io is that you can interact with websites to compare their content.



Often you need to enter in some search query or need to access a page that's only available from behind a login/password form.



Or maybe perform change detection from behind password protected websites?



_**Note: Â Only use this on websites where you have permission todo so, and always "recheck" with the maximum realistic time between rechecks, logging-in every minute could get you blocked from the site you are viewing.**_


[Subscribe to Browser Steps](https://changedetection.io/taxonomy/term/6/feed)

---

### How-To | changedetection.io
Original URL: https://changedetection.io/topic/how

[Skip to main content](https://changedetection.io/topic/how#main-content)

# Changedetection.io Tutorials - How-To

How-To section, find out more, get inspiration!

- [![Ubiquity store - How to get restock / back in stock notifications ](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/ubiquiti-store-restock.png?itok=vrrfSIXG)](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)





[How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)





If you've been trying to get your hands on Ubiquiti gearâ€”like the Power Distribution Pro, Cloud Gateway Fiber, or that elusive Dream Machine Proâ€”you know the story: blink, and it's sold out. Hitting refresh all day just doesnâ€™t cut it anymore. But thereâ€™s a smarter way to shopâ€”and it takes less than five minutes to set up.

- [![beating 403 access denied - proxy scanner](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/403-access-denied-proxy-scanner.png?itok=ZgdFG2vE)](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)





[Find the best proxy to beat "403 access denied" with our proxy scanner](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)





A proxy scanner helps identify working proxies that successfully retrieve pages without being denied, ensuring consistent access to accurate data - Fortunately changedetection.io has a proxy scanner built in!

- [![How to Use Changedetection.io to Monitor Specific Keywords](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/keyword.png?itok=z2tS8Gs3)](https://changedetection.io/tutorial/how-monitor-keywords-any-website)





[How To Monitor Keywords On Any Website](https://changedetection.io/tutorial/how-monitor-keywords-any-website)





In the world of breaking news and rapid financial updates, staying ahead of key developments is critical. Changedetection.io helps you to get notifications of specific keywords on just about any webpage - Here's how to setup keyword monitoring in a snap!

- [![Conditional web page change alerts!](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-03/image_114.png?itok=byv9o-pd)](https://changedetection.io/tutorial/conditional-actions-web-page-changes)





[Conditional actions on web page changes!](https://changedetection.io/tutorial/conditional-actions-web-page-changes)





Changedetection.io introduces one of its most powerful features yet: conditional actions. This opens the door to much more precise and flexible monitoring.

Itâ€™s no longer just about detecting when content changes â€” now you can define exactly what kind of change matters to you. For example, trigger an alert only when a productâ€™s price drops below a certain threshold, or when a keyword appears in the updated content.

- [![NÃ¼rburgring updates today](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-03/N%C3%BCrburgring-updates-today.png?itok=nfDcrZ-E)](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring)





[NÃ¼rburgring racing passion - Get notified of news updates today from NÃ¼rburgring!](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring)







The NÃ¼rburgring, or "Green Hell," is the ultimate test of skill and endurance, beloved for its intense racing and unpredictable conditions. Recent updates include the NÃ¼rburgring 24 Hours joining the Intercontinental GT Challenge, with Ravenol as the new title sponsor. The 2024 race, shortened by heavy fog, saw Scherer Sport PHX take a historic seventh win - Find out how to get notified when the official NÃ¼rburgring website updates its news section! stay informed! **Get daily NÃ¼rburgring news updates to your inbox.**

- [![GeForce RTX 5090 5080 restock alert](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/geforce-rtx-5090-learn-more-og-1200x630.jpg?itok=cKsJOwqr)](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)





[BestBuy restock alerts - GeForce RTX 5090 & GeForce RTX 5080 are out!](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)





The NVIDIA GeForce RTX 5090 and RTX 5080 have arrived, delivering unprecedented power with next-gen AI, lightning-fast frame rates, and jaw-dropping ray tracing. These GPUs are selling out fast, but with Changedetection.io, you can stay ahead of the rush and grab one the moment they restock!

- [![Kmart restock alerts](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/kmart.jpg?itok=rRRrxTTZ)](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others)





[Kmart Shopping - Easily monitor prices and get restock alerts via email, discord, and others.](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others)





Kmart is a great place to shop for every day needs, but what is even better is getting alerts when items come back in stock or when they are on sale (price reduced!)

In this quick tutorial I'll show you how to setup changedetection.io to notify you when items are re-stocked or have a price change.

- [![Dynamic form - Prefill date value before web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/dynamic-form-set-value-page-change-detection.jpg?itok=ZOUKiiAz)](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts)





[Pre-fill dynamic form "date" fields and get web page change alerts](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts)







A common situation is when you need to pre-fill / fill-in some data in a web page form such as the "current date", this an example would be when booking a trailor or reserving a car-parking space.







![Pre-fill date field before web page change detection](https://changedetection.io/sites/changedetection.io/files/inline-images/image_95.png)

- [![Webshare proxies with  web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-12/webshare-changedetection-page-changes.jpg?itok=pWkOgmsq)](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies)





[Web page change monitoring with Webshare proxies](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies)







Integrating proxies with Changedetection takes website monitoring to a professional level by addressing challenges like regional restrictions, IP bans, and task scalability. Hereâ€™s how [Webshare proxies](https://www.webshare.io/) enhance Changedetection:

- [![](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/default_images/temp.png?itok=0vsexsQ8)](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective)





[How to Monitor Government Agency News, Resources â€” A Legal Professionalâ€™s Perspective](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective)





As a legal professional, you understand that staying on top of regulatory updates isnâ€™t just a matter of convenience; itâ€™s integral to offering informed guidance to your team and clients. Missing a crucial regulatory shift can quickly transform a well-prepared argument or strategy into outdated advice.


[Subscribe to How-To](https://changedetection.io/taxonomy/term/4/feed)

---

### How-To | changedetection.io
Original URL: https://changedetection.io/topic/how?page=0

[Skip to main content](https://changedetection.io/topic/how?page=0#main-content)

# Changedetection.io Tutorials - How-To

How-To section, find out more, get inspiration!

- [![Ubiquity store - How to get restock / back in stock notifications ](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/ubiquiti-store-restock.png?itok=vrrfSIXG)](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)





[How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)





If you've been trying to get your hands on Ubiquiti gearâ€”like the Power Distribution Pro, Cloud Gateway Fiber, or that elusive Dream Machine Proâ€”you know the story: blink, and it's sold out. Hitting refresh all day just doesnâ€™t cut it anymore. But thereâ€™s a smarter way to shopâ€”and it takes less than five minutes to set up.

- [![beating 403 access denied - proxy scanner](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/403-access-denied-proxy-scanner.png?itok=ZgdFG2vE)](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)





[Find the best proxy to beat "403 access denied" with our proxy scanner](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)





A proxy scanner helps identify working proxies that successfully retrieve pages without being denied, ensuring consistent access to accurate data - Fortunately changedetection.io has a proxy scanner built in!

- [![How to Use Changedetection.io to Monitor Specific Keywords](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/keyword.png?itok=z2tS8Gs3)](https://changedetection.io/tutorial/how-monitor-keywords-any-website)





[How To Monitor Keywords On Any Website](https://changedetection.io/tutorial/how-monitor-keywords-any-website)





In the world of breaking news and rapid financial updates, staying ahead of key developments is critical. Changedetection.io helps you to get notifications of specific keywords on just about any webpage - Here's how to setup keyword monitoring in a snap!

- [![Conditional web page change alerts!](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-03/image_114.png?itok=byv9o-pd)](https://changedetection.io/tutorial/conditional-actions-web-page-changes)





[Conditional actions on web page changes!](https://changedetection.io/tutorial/conditional-actions-web-page-changes)





Changedetection.io introduces one of its most powerful features yet: conditional actions. This opens the door to much more precise and flexible monitoring.

Itâ€™s no longer just about detecting when content changes â€” now you can define exactly what kind of change matters to you. For example, trigger an alert only when a productâ€™s price drops below a certain threshold, or when a keyword appears in the updated content.

- [![NÃ¼rburgring updates today](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-03/N%C3%BCrburgring-updates-today.png?itok=nfDcrZ-E)](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring)





[NÃ¼rburgring racing passion - Get notified of news updates today from NÃ¼rburgring!](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring)







The NÃ¼rburgring, or "Green Hell," is the ultimate test of skill and endurance, beloved for its intense racing and unpredictable conditions. Recent updates include the NÃ¼rburgring 24 Hours joining the Intercontinental GT Challenge, with Ravenol as the new title sponsor. The 2024 race, shortened by heavy fog, saw Scherer Sport PHX take a historic seventh win - Find out how to get notified when the official NÃ¼rburgring website updates its news section! stay informed! **Get daily NÃ¼rburgring news updates to your inbox.**

- [![GeForce RTX 5090 5080 restock alert](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/geforce-rtx-5090-learn-more-og-1200x630.jpg?itok=cKsJOwqr)](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)





[BestBuy restock alerts - GeForce RTX 5090 & GeForce RTX 5080 are out!](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)





The NVIDIA GeForce RTX 5090 and RTX 5080 have arrived, delivering unprecedented power with next-gen AI, lightning-fast frame rates, and jaw-dropping ray tracing. These GPUs are selling out fast, but with Changedetection.io, you can stay ahead of the rush and grab one the moment they restock!

- [![Kmart restock alerts](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/kmart.jpg?itok=rRRrxTTZ)](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others)





[Kmart Shopping - Easily monitor prices and get restock alerts via email, discord, and others.](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others)





Kmart is a great place to shop for every day needs, but what is even better is getting alerts when items come back in stock or when they are on sale (price reduced!)

In this quick tutorial I'll show you how to setup changedetection.io to notify you when items are re-stocked or have a price change.

- [![Dynamic form - Prefill date value before web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/dynamic-form-set-value-page-change-detection.jpg?itok=ZOUKiiAz)](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts)





[Pre-fill dynamic form "date" fields and get web page change alerts](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts)







A common situation is when you need to pre-fill / fill-in some data in a web page form such as the "current date", this an example would be when booking a trailor or reserving a car-parking space.







![Pre-fill date field before web page change detection](https://changedetection.io/sites/changedetection.io/files/inline-images/image_95.png)

- [![Webshare proxies with  web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-12/webshare-changedetection-page-changes.jpg?itok=pWkOgmsq)](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies)





[Web page change monitoring with Webshare proxies](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies)







Integrating proxies with Changedetection takes website monitoring to a professional level by addressing challenges like regional restrictions, IP bans, and task scalability. Hereâ€™s how [Webshare proxies](https://www.webshare.io/) enhance Changedetection:

- [![](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/default_images/temp.png?itok=0vsexsQ8)](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective)





[How to Monitor Government Agency News, Resources â€” A Legal Professionalâ€™s Perspective](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective)





As a legal professional, you understand that staying on top of regulatory updates isnâ€™t just a matter of convenience; itâ€™s integral to offering informed guidance to your team and clients. Missing a crucial regulatory shift can quickly transform a well-prepared argument or strategy into outdated advice.


[Subscribe to How-To](https://changedetection.io/taxonomy/term/4/feed)

---

### How-To | changedetection.io
Original URL: https://changedetection.io/topic/how?page=1

[Skip to main content](https://changedetection.io/topic/how?page=1#main-content)

# Changedetection.io Tutorials - How-To

How-To section, find out more, get inspiration!

- [![How to check web pages for changes according to schedule](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-12/scheduler.jpg?itok=x-8CIMbB)](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule)





[Checking web pages for changes according to a schedule](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule)





One fantastic example is when you want to check for new headlines at your favourite finance news website every day at 0900h, explore how to easily set this up, and more!

- [![How to get past CAPTCHA](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-11/defeating-captcha.jpeg?itok=eF7uw84r)](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring)





[Using Bright Data's "Scraping Browser" to by-pass CAPTCHA's and other protection when monitoring pages](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring)





For many websites - simply using a proxy is not enough, the website is using much more complex anti-robot software to detect the actual browser that is being used, not just the IP connection or headers (including common headers such as user-agent and others)

You need a better way to simulate a real browser.

- [![Simple email alerts for web page changes - how to](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-10/email-alert.jpg?itok=upKV_Erz)](https://changedetection.io/tutorial/email-notification-when-web-page-changes-how)





[Email notification when a web page changes - How To](https://changedetection.io/tutorial/email-notification-when-web-page-changes-how)





In this tutorial, weâ€™ll walk you through how to set up a web page monitor and configure email notifications for any updates or changes to that webpage.

- [![How to monitor a <select> dropdown for changes and get alerts](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-10/dropdown-select-monitor-change.jpeg?itok=8WQ4ajBg)](https://changedetection.io/tutorial/monitoring-html-select-drop-down-changes-options)





[Monitoring HTML "SELECT" drop down for changes to options](https://changedetection.io/tutorial/monitoring-html-select-drop-down-changes-options)





changedetection.io can automatically show any changes to values, infact it renders them out ready for change detection on the fly, learn more

- [![vevor tool restock and price discount change](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-09/vevor-tool-m100-1.2-3829748392_0.jpg?itok=FRvHYTI7)](https://changedetection.io/tutorial/vevor-tools-easily-monitor-restock-and-get-alerts-discounts)





[Vevor Tools - easily monitor restock and get alerts on discounts!](https://changedetection.io/tutorial/vevor-tools-easily-monitor-restock-and-get-alerts-discounts)







If you're a fan of [Vevor tools](https://vevor.com/), you can buy them directly from their website. But even better than that is catching those irresistible clearance sales, restocks, and deep discounts on their products.



With changedetection.io, you can effortlessly set up alerts for price drops and restocks, ensuring you never miss a deal or the chance to grab a tool as soon as it's back in stock.



## How to setup alerts when a Vevor Tools product changes price or has a discount.

- [![Synology NAS Discord changedetection.io](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-01/synology-discord-changedetectionio.png?itok=XKgktvQ0)](https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord)





[Synology NAS - How to get alerts on new software updates via Discord!](https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord)







In this quick tutorial I'll show you how easy it is in to monitor a website for new software version releases and connect Discord for push notifications.



We will use Synology NAS in our little example, Synology have been continuously releasing great features and super stable software in recent years.

- [![Alert if HTML element exists or not](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-01/image_67.png?itok=hvmoSEwT)](https://changedetection.io/tutorial/change-detection-if-html-element-exists-or-not)





[Change detection if a HTML element exists or not](https://changedetection.io/tutorial/change-detection-if-html-element-exists-or-not)







Sometimes you are not quite interested in content change notifications for the entire web page, and maybe not even content change notification for a element on the website - _**actually you want to know if an element exists at all or not.**_







So in this quick tutorial I'll show you how to setup changedetection.io to alert if you a HTML element exists or not







Using "xPath" (Like CSS selectors except different :) ) we can simply write the filter rule

- [![Monitor a site for new content and get notifications](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-01/new-content-notification.png?itok=6V0-7zKX)](https://changedetection.io/tutorial/how-monitor-website-new-content)





[How to monitor a website for NEW content](https://changedetection.io/tutorial/how-monitor-website-new-content)





How to monitor a site for new content ? How can you configure changedetection.io to only show NEW content from a site and send you a notification? What if you only want to know about new and unique content?

- [![Gears showing that new links can be added automatically](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-01/gears.jpg?itok=lkxft_Jg)](https://changedetection.io/tutorial/automatically-adding-new-pages-watch-existing-results)





[Automatically adding new pages to watch from existing results](https://changedetection.io/tutorial/automatically-adding-new-pages-watch-existing-results)







Think of the situation where you are watching your favourite ecommerce website, and you want to start automatically watching any NEW pages for changes.



For example, you might be interested in a list of search results for a product, but then you also want to follow/watch those product pages for changes (maybe price changes, availability etc)

- [![Extract data line chart from website example picture](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-12/changedet-line-chart-extract-data.png?itok=_Gr8i5c2)](https://changedetection.io/tutorial/extract-data-websites-and-draw-charts-how-gain-valuable-long-term-insights)





[Scrape and Extract data from websites and draw charts - How to gain valuable long-term insights](https://changedetection.io/tutorial/extract-data-websites-and-draw-charts-how-gain-valuable-long-term-insights)





Visualising long-term insights can lead to a lot of interesting and valuable realisations.

The web is always changing, but how does that information look across a week? a month? a year?


[Subscribe to How-To](https://changedetection.io/taxonomy/term/4/feed)

---

### How-To | changedetection.io
Original URL: https://changedetection.io/topic/how?page=2

[Skip to main content](https://changedetection.io/topic/how?page=2#main-content)

# Changedetection.io Tutorials - How-To

How-To section, find out more, get inspiration!

- [![](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/default_images/temp.png?itok=0vsexsQ8)](https://changedetection.io/tutorial/source-code-monitor-how-get-alerts-changes-html-source-code)





[Source code monitor - How to get alerts on changes to HTML source code](https://changedetection.io/tutorial/source-code-monitor-how-get-alerts-changes-html-source-code)





How to get alerts on changes to HTML source code? Sometimes you need to know when a very specific part of the HTML changes, for example you're watching a competitor and want to know when they change their shops metatags

- [![Best Buy  - "Coming Soon" how to get notifications and alerts](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-12/unavailable-sold-out.png?itok=IsQGVSxf)](https://changedetection.io/tutorial/bestbuy-get-coming-soon-product-stock-notifications-using-restock-detection)





[BestBuy - Get "Coming Soon" product in stock notifications using the restock detection!](https://changedetection.io/tutorial/bestbuy-get-coming-soon-product-stock-notifications-using-restock-detection)





Best Buy excels in providing a comprehensive array of electronics and tech gadgets, offering a diverse range of products both in-store and online. Their stores provide an immersive experience, often staffed with knowledgeable experts who assist customers in making informed decisions.

It's all perfect except for one thing - "COMING SOON" on a product that you really want!

- [![Detecting restock / back in stock](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-11/restock.png?itok=w8RnSkvV)](https://changedetection.io/tutorial/how-get-product-re-stock-or-back-stock-alerts-and-notifications)





[How to get product re-stock or "back in stock" alerts and notifications ?](https://changedetection.io/tutorial/how-get-product-re-stock-or-back-stock-alerts-and-notifications)





Is that product or event ticket sold out? unavailable?
Need to get notified when something is back in stock?

There is a solution - You can simply add your website monitor and select the "Re-stock detection for single product pages" option.

Read on!

- [![Excel list of websites to monitor](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-11/Import-List-Of-websites-to-monitor-from-excel.png?itok=u7kQR1z9)](https://changedetection.io/tutorial/how-import-your-website-change-detection-lists-excel)





[How to import your website change detection lists from Excel?](https://changedetection.io/tutorial/how-import-your-website-change-detection-lists-excel)





In this quick article I'll show you how to import your website URL lists from Microsoft Excel into changedetection.io

This can be super handy when you've managed to filter down your lists of websites to something really specific that you're interested in, or another way to manage your list of websites to check for changes.

It's super easy with changedetection.io.

- [![How to detect changes in an RSS feed and get push notifications?](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-10/Screenshot_2023-10-17_14-11-04.png?itok=v748XCo3)](https://changedetection.io/tutorial/how-get-push-notifications-rss-feed-detect-changes-rss-feed)





[How to get push notifications from a RSS Feed ? Detect changes in the RSS Feed!](https://changedetection.io/tutorial/how-get-push-notifications-rss-feed-detect-changes-rss-feed)





Do you love RSS? But wish you could get notifications when certain keywords appear on your favourite RSS streams sent as a push notification to Discord, Telegram, Email, Slack and more? Read on!

- [![hetzner](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-09/hetzner.jpg?itok=SqgdkGOV)](https://changedetection.io/tutorial/awesome-use-case-4510-how-get-notified-when-hetzner-servers-and-products-are-available)





[Awesome use-case #4,510: How to get notified when Hetzner servers and products are available](https://changedetection.io/tutorial/awesome-use-case-4510-how-get-notified-when-hetzner-servers-and-products-are-available)





But the real heartbreak is when you are hunting for your dream Hetzner Dedicated Server only to find out that it's not available in your preferred architecture and that there's no good way to get alerts or notifications when Hetzner effectively "restock" that type of server.

Changedetection.io to the rescue - get notifications when Hetzner restock their server offers!

- [![Using website change detection to monitor for changes in regulations.](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/regs.jpeg?itok=7qN5lKiQ)](https://changedetection.io/tutorial/got-regtech-using-website-change-detection-monitor-changes-regulations)





[Got RegTech? Using website change detection to monitor for changes in regulations.](https://changedetection.io/tutorial/got-regtech-using-website-change-detection-monitor-changes-regulations)





Website change detection is a crucial component of a regulatory intelligence solution, helping it stay ahead of regulatory changes and inform your clients before they become aware of these changes. Here's how website change detection can specifically assist in achieving this goal.

- [![Login box](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/login-box.jpg?itok=VQ8duH9Z)](https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy)





[Website content change detection from behind logins - easy](https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy)







Another great feature of changedetection.io is that you can interact with websites to compare their content.



Often you need to enter in some search query or need to access a page that's only available from behind a login/password form.



Or maybe perform change detection from behind password protected websites?



_**Note: Â Only use this on websites where you have permission todo so, and always "recheck" with the maximum realistic time between rechecks, logging-in every minute could get you blocked from the site you are viewing.**_

- [![BrightData](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/bright.png?itok=kxk1sDeO)](https://changedetection.io/tutorial/how-bright-data-proxies-and-changedetectionio)





[How to - Bright Data Proxies and changedetection.io](https://changedetection.io/tutorial/how-bright-data-proxies-and-changedetectionio)





Using proxies is beneficial for accessing web pages from different countries and bypassing blocking rules for several reasons, read on to find out the advantage of using Bright Data Proxies with changedetection.io!

- [![realestate vacancies](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/image_9.png?itok=HzVUwhxk)](https://changedetection.io/tutorial/four-tips-help-you-your-apartment-or-house-search)





[Four tips to help you in your apartment or house search.](https://changedetection.io/tutorial/four-tips-help-you-your-apartment-or-house-search)







Monitoring real estate pages and receiving notifications on changes to website content is highly advantageous when searching for an apartment. By doing so, you can be among the first to discover newly listed properties, price reductions, or updates on available apartments.


[Subscribe to How-To](https://changedetection.io/taxonomy/term/4/feed)

---

### How-To | changedetection.io
Original URL: https://changedetection.io/topic/how?page=3

[Skip to main content](https://changedetection.io/topic/how?page=3#main-content)

# Changedetection.io Tutorials - How-To

How-To section, find out more, get inspiration!

- [![keepass screenshot](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/main_big.png?itok=lczIgYVC)](https://changedetection.io/tutorial/how-get-alerts-new-keepass-releases)





[How to get alerts on new KeePass releases](https://changedetection.io/tutorial/how-get-alerts-new-keepass-releases)





KeePass is vital for online security as it securely stores passwords. Getting update notifications is crucial to stay protected from potential vulnerabilities and cyber threats.

- [![PR Newswire cision logo](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/prn_cision_logo_desktop.png?itok=ivh2LMd6)](https://changedetection.io/tutorial/how-get-alerts-when-certain-keywords-appear-pr-newswire)





[How to get alerts when certain keywords appear on PR Newswire?](https://changedetection.io/tutorial/how-get-alerts-when-certain-keywords-appear-pr-newswire)





PR Newswire is a news distribution service. By monitoring keywords on PR Newswire, you gain insights, track brand reputation, discover media opportunities, make informed investments, and identify crisis risks.

- [![Decathlon shopping - decathlon price tracker](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/dec.jpg?itok=BFW3bYDc)](https://changedetection.io/tutorial/decathlon-sport-how-monitor-prices)





[Decathlon Sport - How to monitor prices - decathlon price tracker](https://changedetection.io/tutorial/decathlon-sport-how-monitor-prices)





Decathlon is a global sporting goods retailer offering a wide range of products. Monitoring their webpage for low prices is beneficial as it helps you save money by identifying discounts and special offers. By staying vigilant, you can seize cost-saving opportunities and make informed purchases, maximizing the value of your shopping experience.

Keep an eye on your favourite item!


[Subscribe to How-To](https://changedetection.io/taxonomy/term/4/feed)

---

### Knowledge base | changedetection.io
Original URL: https://changedetection.io/topic/knowledge-base

[Skip to main content](https://changedetection.io/topic/knowledge-base#main-content)

# Changedetection.io Tutorials - Knowledge base

- [![No web spiders!](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-05/no-spider.png?itok=QPELSmrc)](https://changedetection.io/tutorial/what-are-main-types-anti-robot-mechanisms)





[What are the main types of anti-robot mechanisms?](https://changedetection.io/tutorial/what-are-main-types-anti-robot-mechanisms)







You may have read a lot about some tricks to defeat scraping such as changing your scraping browser's "User Agent" settings, however that's only the start of the story.



![anti-robot blocker](https://changedetection.io/sites/changedetection.io/files/inline-images/image_80.png)



In reality there are multiple ways that a service can detect your scraping attempts, changing the user-agent is just a small trick that may or may not help.


[Subscribe to Knowledge base](https://changedetection.io/taxonomy/term/9/feed)

---

### Notifications | changedetection.io
Original URL: https://changedetection.io/topic/notifications

[Skip to main content](https://changedetection.io/topic/notifications#main-content)

# Changedetection.io Tutorials - Notifications

- [![keepass screenshot](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/main_big.png?itok=lczIgYVC)](https://changedetection.io/tutorial/how-get-alerts-new-keepass-releases)





[How to get alerts on new KeePass releases](https://changedetection.io/tutorial/how-get-alerts-new-keepass-releases)





KeePass is vital for online security as it securely stores passwords. Getting update notifications is crucial to stay protected from potential vulnerabilities and cyber threats.


[Subscribe to Notifications](https://changedetection.io/taxonomy/term/1/feed)

---

### Proxies | changedetection.io
Original URL: https://changedetection.io/topic/proxies

[Skip to main content](https://changedetection.io/topic/proxies#main-content)

# Changedetection.io Tutorials - Proxies

- [![How to get past CAPTCHA](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-11/defeating-captcha.jpeg?itok=eF7uw84r)](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring)





[Using Bright Data's "Scraping Browser" to by-pass CAPTCHA's and other protection when monitoring pages](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring)





For many websites - simply using a proxy is not enough, the website is using much more complex anti-robot software to detect the actual browser that is being used, not just the IP connection or headers (including common headers such as user-agent and others)

You need a better way to simulate a real browser.

- [![BrightData](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/bright.png?itok=kxk1sDeO)](https://changedetection.io/tutorial/how-bright-data-proxies-and-changedetectionio)





[How to - Bright Data Proxies and changedetection.io](https://changedetection.io/tutorial/how-bright-data-proxies-and-changedetectionio)





Using proxies is beneficial for accessing web pages from different countries and bypassing blocking rules for several reasons, read on to find out the advantage of using Bright Data Proxies with changedetection.io!


[Subscribe to Proxies](https://changedetection.io/taxonomy/term/5/feed)

---

### RegTech | changedetection.io
Original URL: https://changedetection.io/topic/regtech

[Skip to main content](https://changedetection.io/topic/regtech#main-content)

# Changedetection.io Tutorials - RegTech

- [![Using website change detection to monitor for changes in regulations.](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/regs.jpeg?itok=7qN5lKiQ)](https://changedetection.io/tutorial/got-regtech-using-website-change-detection-monitor-changes-regulations)





[Got RegTech? Using website change detection to monitor for changes in regulations.](https://changedetection.io/tutorial/got-regtech-using-website-change-detection-monitor-changes-regulations)





Website change detection is a crucial component of a regulatory intelligence solution, helping it stay ahead of regulatory changes and inform your clients before they become aware of these changes. Here's how website change detection can specifically assist in achieving this goal.


[Subscribe to RegTech](https://changedetection.io/taxonomy/term/7/feed)

---

### Use-case | changedetection.io
Original URL: https://changedetection.io/topic/use-case

[Skip to main content](https://changedetection.io/topic/use-case#main-content)

# Changedetection.io Tutorials - Use-case

- [![hetzner](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-09/hetzner.jpg?itok=SqgdkGOV)](https://changedetection.io/tutorial/awesome-use-case-4510-how-get-notified-when-hetzner-servers-and-products-are-available)





[Awesome use-case #4,510: How to get notified when Hetzner servers and products are available](https://changedetection.io/tutorial/awesome-use-case-4510-how-get-notified-when-hetzner-servers-and-products-are-available)





But the real heartbreak is when you are hunting for your dream Hetzner Dedicated Server only to find out that it's not available in your preferred architecture and that there's no good way to get alerts or notifications when Hetzner effectively "restock" that type of server.

Changedetection.io to the rescue - get notifications when Hetzner restock their server offers!

- [![Login box](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/login-box.jpg?itok=VQ8duH9Z)](https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy)





[Website content change detection from behind logins - easy](https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy)







Another great feature of changedetection.io is that you can interact with websites to compare their content.



Often you need to enter in some search query or need to access a page that's only available from behind a login/password form.



Or maybe perform change detection from behind password protected websites?



_**Note: Â Only use this on websites where you have permission todo so, and always "recheck" with the maximum realistic time between rechecks, logging-in every minute could get you blocked from the site you are viewing.**_


[Subscribe to Use-case](https://changedetection.io/taxonomy/term/8/feed)

---

### Automatically adding new pages to watch from existing results | changedetection.io
Original URL: https://changedetection.io/tutorial/automatically-adding-new-pages-watch-existing-results

[Skip to main content](https://changedetection.io/tutorial/automatically-adding-new-pages-watch-existing-results#main-content)

# Automatically adding new pages to watch from existing results

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 3 January, 2024



Topic

[How-To](https://changedetection.io/topic/how)

Think of the situation where you are watching your favourite ecommerce website, and you want to start automatically watching any NEW pages for changes.

For example, you might be interested in a list of search results for a product, but then you also want to follow/watch those product pages for changes (maybe price changes, availability etc)

Since version `0.45.11` it is possible to use the built in API to ask changedetection.io to insert a new link into its database, as a plaintext list of links (with a tag/group as an optional argument), we can use the 'notifications' tab to tell changedetection.io to notify itself to add a new link :)

Here's how! In this example we will use CashConverters as our example.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_59.png)

## Step 1 - Add the website URL and configure the filters

Using the current URL, copied and paste from your browser, as the URL in changedetection to watch.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_53.png)

Now in this case, the VisualSelector is not quite what we want, because we are only interested in _all_ of the links to the products, additionally we are interested in the "HREF" part of the "A HREF" part of the link so that we can see what the products link is.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_55.png)

Fortunately, they make it super easy for us, the link is clearly marked with the CSS class name Â `product-item__price`

So then to get a list of URLs for products, we can use xPath to ask it to extract the "href" part for us, and only return that list.

We " _simply_" use the Filter Rule Â `//a[@class="product-item__title"]/@href`

_**Ah but wait!** We need to be sure we have the full link, including https:// and the domain name/website URL._

Change to use the Filter Rule Â `xpath:for-each(//a[@class="product-item__title"]/@href, function($a) { concat("https://cashconverters.co.uk", $a) })`

( We will make this easier in the future with some plugins that will support easily appending text to each line of results )

![Showing how the filter looks for adding the domain to automatically discovered links](https://changedetection.io/sites/changedetection.io/files/inline-images/image_56.png)

Now we check out the **Preview** or **Difference Page** output, and we can see a nice list of links

![List of links discovered for automatic following](https://changedetection.io/sites/changedetection.io/files/inline-images/image_57.png)

## Step 2 - Automatically importing the URLs via the API

The built-in [API supports importing a list (plain-text) of URLs with an option organisational tag/group](https://changedetection.io/docs/api_v1/index.html#api-Watch-Import)

Using that, we will make changedetection.io "notify" its own API of any changes to that URL list

Make sure your API access is turned on, and you have the key ready (Visit Â Settings > API )

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_58.png)

We will use that [API key in our notification URL](https://github.com/dgtlmoon/changedetection.io/wiki/Notification-configuration-notes#postposts), So the URL to notify (to automatically import the list of URLS) would be (careful to include the + at the start, this signifies that it should be a "http header")

`post://localhost:5000/api/v1/import?tag=CashConverters&+x-api-key=dfb4d69efdec620e30edcd916c545efc`

or in the case that you're using [our beloved subscription service](https://changedetection.io/#subscription)

`posts://lemonade.changedetection.io/your-loginURL/api/v1/import?tag=CashConverters&+x-api-key=dfb4d69efdec620e30edcd916c545efc`

Use " **post://**" for non-SSL and " **posts://**" if your installation lives on a HTTPS protected address.

And set the **Notification Body** to only " `{{current_snapshot}}`" then you can press **Send test notification**, this will send all of those URLs for population in changedetection.io

![Showing how to configure the API to automatically add links](https://changedetection.io/sites/changedetection.io/files/inline-images/image_61.png)

Once you click **"send test notifcation"** with **{{current\_snapshot}}**, you should then see all those links in Â your watch list

![List of automatically added links from website](https://changedetection.io/sites/changedetection.io/files/inline-images/image_68.png)

By default, it will only add "new" links

Have fun, and experiment! Happy change detecting :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### BestBuy - Get \
Original URL: https://changedetection.io/tutorial/bestbuy-get-coming-soon-product-stock-notifications-using-restock-detection

[Skip to main content](https://changedetection.io/tutorial/bestbuy-get-coming-soon-product-stock-notifications-using-restock-detection#main-content)

# BestBuy - Get "Coming Soon" product in stock notifications using the restock detection!

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 29 November, 2023



Topic

[How-To](https://changedetection.io/topic/how)

_**Best Buy**_ excels in providing a comprehensive array of electronics and tech gadgets, offering a diverse range of products both in-store and online. Their stores provide an immersive experience, often staffed with knowledgeable experts who assist customers in making informed decisions.

It's all perfect except for one thing - **"COMING SOON**"on a product that you really want!

![Best Buy "Coming soon" alerts status](https://changedetection.io/sites/changedetection.io/files/inline-images/image_44.png)

So just like we learned over at the ["How to get product restock alerts" tutorial](https://changedetection.io/tutorial/how-get-product-re-stock-or-back-stock-alerts-and-notifications) , the restock detector will work perfectly fine with BestBuy because it can automatically recognise the _**"Coming Soon"**_ text.

_**( Follow the 2 easy steps in that tutorial ! )**_

But over at our hosted/subscription offer, we have a special workaround for you - if you receive the "Hello Choose a country!" message, you can simply appear from a different proxy/location.

Changedetection.io subscription offers many unique locations to 'appear' to call from, this can be super handy if you're watching a website thats not in your own country or if your IP is detected incorrectly.

![If you get blocked, try this](https://changedetection.io/sites/changedetection.io/files/inline-images/image_42.png)

So if you get this "Choose a country" message you can choose a new location to watch your products on BestBuy from.

We offer several different locations that are included as part of the simple flat monthly pricing that we offer.

![Best Buy "Choose a country" work around for getting alerts](https://changedetection.io/sites/changedetection.io/files/inline-images/image_45.png)

So simply click on "Edit" and then "Request" and choose the **USA #1** location.

Then, let the system recheck the BestBuys product page that contains the "COMING SOON" text, and you should be all set :)

Once everything is working, and the product comes available and is no longer "coming soon" your list of website watches will now contain a happy green tag " **In stock**".

![product is detected as being back in stock and restocked (has no out-of-stock text)](https://changedetection.io/sites/changedetection.io/files/inline-images/image_41.png)Happy green icon when the Best Buy product is no longer "Coming Soon" !

Ofcourse dont, forget to add all your favourite notifications to your Best Buy "Coming soon" alerts - email, Discord and more!

Good luck and have fun!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### BestBuy restock alerts - GeForce RTX 5090 & GeForce RTX 5080 are out! | changedetection.io
Original URL: https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out

[Skip to main content](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out#main-content)

# BestBuy restock alerts - GeForce RTX 5090 & GeForce RTX 5080 are out!

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 31 January, 2025



Topic

[How-To](https://changedetection.io/topic/how)

The NVIDIA GeForce RTX 5090 and RTX 5080 are finally here, and they are absolute game-changers! Powered by the revolutionary Blackwell RTX architecture, these GPUs deliver mind-blowing performance, doubling frame rates, slashing workflow times in creative apps, and supercharging AI generation.![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_103.png) With DLSS 4â€™s Multi Frame Generation, you can experience ultra-smooth, ray-traced 4K gaming at unprecedented frame ratesâ€”think _Cyberpunk 2077_ maxed out at 290 FPS and _Alan Wake 2_ at 230 FPS. Whether you're gaming, streaming, or pushing the limits of creative work, the RTX 50 Series is built for the future.

But hereâ€™s the catchâ€”these cards are selling out **fast**! With stock-clocked and factory-overclocked models from ASUS, MSI, GIGABYTE, and more, plus limited Founders Edition cards from Best Buy, demand is through the roof. If you donâ€™t want to miss out, **Changedetection.io** is your secret weapon. Set up instant restock alerts so you can grab one the moment it becomes available. Donâ€™t get left behindâ€”stay ahead of the crowd and secure your RTX 5090 or RTX 5080 before they vanish!

Here's how!

### Step 1. Setup your changedetection.io account

Simply register here (click signup) or deploy your own locally run software, see [https://github.com/dgtlmoon/changedetection.io](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)

### Step 2. Â Visit the product page page at BestBuy

For example [https://www.bestbuy.com/site/nvidia-geforce-rtx-5090-32gb-gddr7-graphics-card-dark-gun-metal/6614151.p?skuId=6614151](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)

This link is what you will use to "watch" in changedetection.io

![Bestbuy restock RTX](https://changedetection.io/sites/changedetection.io/files/inline-images/bestbuy-geforce-rtx.jpg)

### Step 3. Â Use the link in changedetection.io and set the restock mode!

- Be sure to set the " **Re-stock & Price detection for single product pages "** mode for restock magic!


![Add RTX BestBuy for restock monitoring](https://changedetection.io/sites/changedetection.io/files/inline-images/image_101.png)

### Step 4. Setup your notifications

By default, we don't assume that you prefer email as a notification - infact many people are using Discord, NTFY, MSTeams and other communication methods, so simply visit **Settings** \> **Notifications** and follow the prompts :)

### Step 5. Enjoy restock monitoring of the GeForce RTX 5090 / 5080 product page!

Now changedetection.io will recheck the BestBuy RTX 5090 / 5080 page at a preset interval, you can add for example all of the RTX range and see which ones come back in stock - or which ones have a price change

![BestBuy RTX](https://changedetection.io/sites/changedetection.io/files/inline-images/image_102.png)

All the best and happy gaming with your new RTX 5090 / RTX 5080 !

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Change detection if a HTML element exists or not | changedetection.io
Original URL: https://changedetection.io/tutorial/change-detection-if-html-element-exists-or-not

[Skip to main content](https://changedetection.io/tutorial/change-detection-if-html-element-exists-or-not#main-content)

# Change detection if a HTML element exists or not

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 8 January, 2024



Topic

[How-To](https://changedetection.io/topic/how)

Sometimes you are not quite interested in content change notifications for the entire web page, and maybe not even content change notification for a element on the website - _**actually you want to know if an element exists at all or not.**_

So in this quick tutorial I'll show you how to setup changedetection.io to alert if you a HTML element exists or not

Using "xPath" (Like CSS selectors except different :) ) we can simply write the filter rule

`xpath:if (count(//item) >0 ) then "Yes it exists!" else "no sorry not here"`

![Setting alert if an element exists or not](https://changedetection.io/sites/changedetection.io/files/inline-images/image_66.png)

So then the change difference would look something like

![Example alert text if the item exists](https://changedetection.io/sites/changedetection.io/files/inline-images/image_67.png)

What is also cool is that because changedetection.io supports xPath2/3 by default, you can also just output the value of **count(),** which means you could get a notification if the number of items changes

`xpath:count(//item)`

Where _**//item**_ is the is the HTML xPath to follow

So perhaps one real world example could be that you want to know if the number of offers listed drops to less than 5

(imagine that the page has a list of special offers, where each **div** is Â ' `<div class="special-offers">`..\`

`xpath:if (count(//div[contains(@class, 'special-offers')) <5 ) then "Less than 5 special offiers" else "All ok, more than 5 offers"`\
\
Simple as that :) The service will let you know/alert you (depending on your notification setup) if less than 5 offers are shown or not.\
\
All the best and have fun!\
\
- [Continue with\\
    and](https://changedetection.io/checkout)\
\
$8.99/Month Easy Subscription\
\
\
Cancel anytime, 5,000 URL watches included.

---

### Checking web pages for changes according to a schedule | changedetection.io
Original URL: https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule

[Skip to main content](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule#main-content)

# Checking web pages for changes according to a schedule

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 19 December, 2024



Topic

[How-To](https://changedetection.io/topic/how)

Recently we added the much requested _Scheduler_ functionality. This extends the _**"Time between recheck"**_ functionality with a schedule that you can limit the checks to.

This has MANY great uses, for example you only want to recheck your favourite news website during office hours (simply click the "Business hours" shortcut to set it up).

![Detecting web page changes according to a schedule](https://changedetection.io/sites/changedetection.io/files/inline-images/image_91.png)

For example, if you combine a _**"Time between recheck"**_ of **1** days, and then click the "BUSINESS HOURS" shortcut, it will automatically configure a time schedule that runs from Â 09:00 for 8 hours (until 17:00h), and since you have "recheck" time set to 1 days, it means it will only check once per day at 09:00.

What if the news website is in another country/timezone? You can also type in the timezone name (for example, I'm in `Europe/Copenhagen`, but the newspaper I want to check every morning in their local time is in New York, I would enter `America/New_York`) , then the recheck schedule would operate in their local time in New York instead of home here in Copenhagen.

_**Another example**-_ _Want to recheck web pages for changes but only on a Sunday?_ Simply only select the " `Sunday`"\- "Start at" checkbox, set the " **Start at**" to `00:00` and **Hours** to " `23`", minutes " `59`". Then it will recheck the webpage only on Sunday from midnight (00:00) until 23:59:59.

So this is another great way to recheck web pages for changes - according to your very own custom schedule.

Many people have also reported that this helps to cut down their proxy provider costs by only checking between the times that is important to them.

We hope you'll love this feature as much as we do!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Conditional actions on web page changes! | changedetection.io
Original URL: https://changedetection.io/tutorial/conditional-actions-web-page-changes

[Skip to main content](https://changedetection.io/tutorial/conditional-actions-web-page-changes#main-content)

# Conditional actions on web page changes!

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 31 March, 2025



Topic

[How-To](https://changedetection.io/topic/how)

Starting with version **v0.49.9**, Changedetection.io introduces one of its most powerful features yet: **conditional actions**. This opens the door to much more precise and flexible monitoring.

Itâ€™s no longer just about detecting when content changes â€” now you can define exactly _what kind_ of change matters to you. For example, trigger an alert only when a productâ€™s price drops below a certain threshold, or when a keyword appears in the updated content.

With full support for logic operators, you can create rich, rule-based conditions using logic like â€œgreater than,â€ â€œless than,â€, "contains", "not contains" and more.

So let's get on with a really great example - Monitor when temperatures in Berlin are "extreme" (less than -20c or greater than +38c)

### Let's add the web page we want to monitor for changes (Berlin Weather)

![Web page for conditional actions](https://changedetection.io/sites/changedetection.io/files/inline-images/image_109.png)

### Let's set-up our conditional change detection filter

Let the page fetch, then click **\[EDIT\]**

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_112.png)

Then, using the **Visual Filter Selector** tab, choose the number, in this case we will click on the current temperature, a balmy 9.2Â°C. Â When the element is selected and click a **red border** will appear.

It's important to choose the right part of the web-page for change-detection, otherwise the number extractor wont know exactly which number is important to you.

![Web page for conditional actions, setting the actual content](https://changedetection.io/sites/changedetection.io/files/inline-images/image_113.png)

Then, hop on over to the **CONDITIONS** tab

![Setting up rules / conditions for web page changes](https://changedetection.io/sites/changedetection.io/files/inline-images/image_114.png)

Let's explain a little what we see here

- **"Match any of the following" -** This acts as 'OR', so _any_ rule will trigger on change
- **"Extracted number after 'Filters & Triggers"**\- We only want to look for a number inside of any filters we specified (This could be the Visual Selector, Text filters from other tabs etc)
- Using these two buttons we can then **add an extra** **\[ Â \+ Â \]** Â rule after this one, or **remove it Â  Â \[ Â - Â \]**

##### _**Testing the rules!**_

Since the page is already fetched, It's nice to know if the rule currently will pass or fail, for this we can press the "tick" button, this will verify that rule row only and report if it PASSES or FAILS.

If you look closely you can see that after pressing the "verify" tick button you can see the text **"extracted number value was 9.2"** below the rules, this lets us know what the situation is and so we know if the right value is being extracted

##### Other interesting checks

- Text contains (or does not contain)
- Text length is greater than (or shorter than)
- Text begins with (or doesnt begin with)
- Text equal (or does not equal)
- plus more!

#### Wrapping up

Of course now you can head over to the **Notifications** tab and setup your slack, email, discord or which ever format you and your team love the most.

This is how you can simply setup Conditional changes, this is just a simple example but there are so many other amazing ways to use this functionality, we encourage you to explore and play with this new tool :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Decathlon Sport - How to monitor prices - decathlon price tracker | changedetection.io
Original URL: https://changedetection.io/tutorial/decathlon-sport-how-monitor-prices

[Skip to main content](https://changedetection.io/tutorial/decathlon-sport-how-monitor-prices#main-content)

# Decathlon Sport - How to monitor prices - decathlon price tracker

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 8 May, 2023



Topic

[How-To](https://changedetection.io/topic/how)

Decathlon is a global sporting goods retailer offering a wide range of products. Monitoring their webpage for low prices is beneficial as it helps you save money by identifying discounts and special offers. By staying vigilant, you can seize cost-saving opportunities and make informed purchases, maximizing the value of your shopping experience.

Fortunately, Decathlon can also talk directly to changedetection.io.

Changedetection.io will automatically detect Decathlon offering its special structured price data (called LD+JSON) and offer you to only follow that data, which means it cuts out all false changes. This is much better than monitoring the whole website.

In this example I'll show you how this works.

#### Step 1. Add the Decathlon product page URL as a new watch

We will add a product URL such as Â [https://www.decathlon.co.uk/p/mp/schwinn/schwinn-mummy-bmx-helmet/\_/R-p-46ccf95d-6770-4865-8165-0026fe63f1c1?c=BLACK](https://www.decathlon.co.uk/p/mp/schwinn/schwinn-mummy-bmx-helmet/_/R-p-46ccf95d-6770-4865-8165-0026fe63f1c1?c=BLACK)

Enter the URL and click **Watch,** then let the system fetch the page.

![Image removed.](https://changedetection.io/sites/changedetection.io/files/inline-images/image_6.png)

#### Step 2. Enable embedded price data following

Some pages offer the ability to only send just the price and stocking data, this way we don't need to care about selecting the region/part of the page of interest, it will give us the raw information about the product instead.

When you see " _**Embedded price data detected, follow only price data?"** click " **YES"**_

![Image removed.](https://changedetection.io/sites/changedetection.io/files/inline-images/image_7.png)

#### Step 3. When the product price or stock changes, examine what changed.

Clicking **Diff** on the watch list will bring you to the **difference** page.

This page shows you what has changed.

Because we are now monitoring the LD+JSON price data automatically, without needing to concern ourselves with the rest of the information on the page, we can now see that the **price** changed from **11.39** to **13.29**

![Image removed.](https://changedetection.io/sites/changedetection.io/files/inline-images/image_8.png)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Find the best proxy to beat \
Original URL: https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner

[Skip to main content](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner#main-content)

# Find the best proxy to beat "403 access denied" with our proxy scanner

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 13 April, 2025



Topic

[How-To](https://changedetection.io/topic/how)

Using a proxy scanner to determine which proxies can bypass **403 Access Denied** errors is crucial when monitoring websites for product prices or other changes with tools like Changedetection.io. Some websites restrict access based on geographic location or traffic patterns, leading to blocked requests and incomplete monitoring. A proxy scanner helps identify working proxies that successfully retrieve pages without being denied, ensuring consistent access to accurate data.

Fortunately changedetection.io has a **proxy scanner** built in - so take for example this common situation where we have a few proxies configured but we get the error **403 access denied** on our default proxy

![403 access denied](https://changedetection.io/sites/changedetection.io/files/inline-images/image_119.png)

If we jump over to **Edit** \> then **Requests** tab we can then find the **Proxy Scanner tool** which will help us find the proxy (or location) that will let us by-pass the 403 Access Denied error.

**First you need to add your proxies**

Jump on over to **Settings** \> **CAPTCHA & Proxies** and add your "Extra proxies", in the hosted/subscription version we call these "locations" however they are the same thing. I recommend BrightData or Oxylabs here, they are both fantastic.

![Adding Proxies](https://changedetection.io/sites/changedetection.io/files/inline-images/image_124.png)

Then go back to your "watch", and click " **EDIT**" and " **Request**"

Then we click on **Check / Scan All** to activate the scanner on all proxy connections and find the one which will not give the 403 access denied message.

(other options like _request method_ removed here for the sake of brevity)

![403 access denied - start proxy scanner / check all](https://changedetection.io/sites/changedetection.io/files/inline-images/image_121.png)

Once we click on that **Check / Scan All** the proxy scanner will then get to work!

Your browser does not support the video tag.


Within a few seconds we can see the results, that 4 of our proxies gave Access Denied, but 4 were ready to rock! Â As well as some basic timing information (seconds for the request), any non-200 errors (error 500, error 403 etc) will show here.

So here we simply selected **Europe / Frankfurt** and then clicked **Save**

And then we wait a few seconds and see that the 403 access denied message is now gone

![403 access denied solved](https://changedetection.io/sites/changedetection.io/files/inline-images/image_122.png)

So there you have it, just another great little tool in changedetection - the **proxy scanner** which helps you beat **403 access denied** errors by find the best proxy for you!

As always, happy change detecting!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Four tips to help you in your apartment or house search. | changedetection.io
Original URL: https://changedetection.io/tutorial/four-tips-help-you-your-apartment-or-house-search

[Skip to main content](https://changedetection.io/tutorial/four-tips-help-you-your-apartment-or-house-search#main-content)

# Four tips to help you in your apartment or house search.

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 1 August, 2023



Topic

[How-To](https://changedetection.io/topic/how)

Monitoring real estate pages and receiving notifications on changes to website content is highly advantageous when searching for an apartment. By doing so, you can be among the first to discover newly listed properties, price reductions, or updates on available apartments.

This proactive approach enables you to swiftly contact landlords or real estate agents, increasing your chances of securing a desirable apartment before others do. It streamlines your apartment hunt, saving you time and ensuring you don't miss out on potential opportunities. Additionally, staying up-to-date with website changes helps you track market trends and adjust your search criteria accordingly, leading to a more efficient and successful apartment search.

Changedetection.io has a couple of little tricks up its sleeve to really optimize your search.

In this article, I'll show you a few small features of changedetection.io which could really help!

![](https://changedetection.io/sites/changedetection.io/files/2023-08/image_9.png)

#### Tip 1. Don't flood their server with checks - use a **SLOWER** recheck time.

This may sound counter-intuitive, but many realestate websites have a lot of protection built in, and don't often update their content every minute, many will 'bulk update' every 15 minutes or so.

So it means there's no need to set a recheck time of "1 minute" for example, it's better to recheck every 10 minutes, this reduces your chance of getting blocked.

#### Tip 2. Use the " **Only trigger when unique lines appear**" text filter

Often, real-estate advertisements will shuffle around in the list, to stop receiving false alerts you should use the filter called " **Only trigger when unique lines appear",** this will compare any new content with all previous content line-by-line, and then only trigger a change when something new was found - in comparison with all history.

For example, this works because new addresses of apartments get listed, but you don't know if they are just being shuffled around in the results or not, so it will check that title/name against all fetched history.

You can find this option under **Edit** \> **Text & Filters** then scroll down to **Text filtering**

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_15.png)

#### Tip 3. Use "Browser Steps" to click on buttons and accept cookies

Just like a real browser, click on buttons and fill in forms, you could even use this for logging in!

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_13.png)

#### Tip 4. Use the **"Visual Filter Selector"** to cut out false alerts and only focus on whats important

Web pages often update the footer, header and menu bars with dates, times, count/number of results which could change and create a false alert. It's super simple to use the **Visual Filter Selector** to choose just the area you want to know about.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_14.png)

Use these four simple tips to increase your chance of grabbing that perfect apartment or house :) Good luck!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Got RegTech? Using website change detection to monitor for changes in regulations. | changedetection.io
Original URL: https://changedetection.io/tutorial/got-regtech-using-website-change-detection-monitor-changes-regulations

[Skip to main content](https://changedetection.io/tutorial/got-regtech-using-website-change-detection-monitor-changes-regulations#main-content)

# Got RegTech? Using website change detection to monitor for changes in regulations.

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 21 August, 2023



Topic

[How-To](https://changedetection.io/topic/how)

[RegTech](https://changedetection.io/topic/regtech)

[_RegTech_](https://www.mas.gov.sg/development/fintech/technologies---regtech) is the use of technology to enhance risk management and regulatory compliance in financial institutions.

Website change detection is a crucial component of a regulatory intelligence solution, helping you stay ahead of regulatory changes and inform your clients before they become aware of these changes. Here's how website change detection can specifically assist in achieving this goal:

01. **Real-time Monitoring:** Website change detection tools continuously monitor regulatory websites, government portals, and industry-specific sites in real-time. This ensures that any updates, amendments, or new regulations are promptly identified.
02. **Early Detection:** By instantly identifying changes on relevant websites, website change detection allows the regulatory intelligence solution to detect regulatory updates as soon as they are published. This enables the solution to act faster than clients who might rely on periodic checks.
03. **Instant Alerts:** When a change is detected, the website change detection solution can immediately send automated alerts and notifications to clients. This provides clients with early awareness of regulatory changes and enables them to take proactive measures.
04. **Competitive Advantage:** Informing clients about regulatory changes before they discover them themselves can provide your solution users with a competitive advantage. They can adjust their strategies, operations, and compliance efforts ahead of competitors, positioning themselves as leaders in their industries.
05. **Customized Monitoring:** Website change detection tools can be configured to monitor specific regulatory websites, keywords, or topics relevant to your clients' industries. This customization ensures that clients receive tailored information that directly impacts their operations.
06. **Comprehensive Coverage:** Regulatory information might be scattered across numerous websites. Website change detection tools ensure comprehensive coverage by monitoring a wide range of sources simultaneously, reducing the risk of missing critical updates.
07. **Data Accuracy:** Website change detection tools employ advanced algorithms to accurately identify changes, eliminating the risk of human error that might occur during manual monitoring. This ensures that clients receive accurate and reliable information, however this depends on many factors.
08. **Risk Mitigation:** By notifying clients about regulatory changes early, the regulatory intelligence solution helps them mitigate risks associated with non-compliance or outdated practices. Clients can address these changes proactively and avoid potential penalties.
09. **Enhanced Client Relationships:** Providing clients with early and valuable insights into regulatory changes enhances your solution's value proposition. It builds trust and strengthens your client relationships as they rely on your solution to keep them well-informed.
10. **Strategic Decision-Making:** Clients armed with early knowledge of regulatory changes can make informed strategic decisions. They can align their business plans, resource allocation, and compliance strategies with the evolving regulatory landscape.
11. **Efficiency and Time Savings:** Website change detection automates the monitoring process, saving clients time and resources that would otherwise be spent manually tracking regulatory websites. This efficiency allows them to focus on more strategic tasks.
12. **Continuous Compliance:** The proactive nature of the regulatory intelligence solution, powered by website change detection, helps clients maintain continuous compliance with regulatory changes, reducing the risk of sudden disruptions to their operations.

Incorporating website change detection into your regulatory intelligence solution transforms it into a proactive tool that empowers clients with timely and actionable regulatory insights. This proactive approach enhances their regulatory preparedness and fosters a strong partnership between your solution and your clients.

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### How to - Bright Data Proxies and changedetection.io | changedetection.io
Original URL: https://changedetection.io/tutorial/how-bright-data-proxies-and-changedetectionio

[Skip to main content](https://changedetection.io/tutorial/how-bright-data-proxies-and-changedetectionio#main-content)

# How to - Bright Data Proxies and changedetection.io

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 2 August, 2023



Topic

[How-To](https://changedetection.io/topic/how)

[Proxies](https://changedetection.io/topic/proxies)

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_4_0.png)

Using Bright Data proxies with changedetection.io is super beneficial for accessing web pages from different countries and bypassing blocking rules for several reasons:

1. **Geographical Location**: Proxies allow you to route your web requests through servers located in different countries. By doing so, you can effectively appear as if you are accessing the web from that specific country. This is useful for accessing geo-restricted content or services that are only available to users in certain regions.
2. **Bypassing IP Restrictions**: Some websites implement IP-based restrictions to limit access to their content or prevent excessive requests from the same IP address. Proxies help you overcome these restrictions by changing your IP address, so you can access the website as if you were coming from a different IP.
3. **Overcoming Censorship**: In regions with strict internet censorship, certain websites and online services may be blocked by the government or internet service providers. Proxies can help users bypass such censorship and access blocked content.
4. **Anonymity and Privacy**: Proxies provide an extra layer of anonymity by masking your original IP address. This can be valuable for users who want to protect their online privacy and avoid being tracked by websites or third parties.
5. **Load Distribution**: When accessing websites through proxies, the load is distributed across multiple servers. This can help prevent server overload and improve the overall performance and speed of web scraping or data collection activities.
6. **Scalability**: Proxies allow you to scale your web scraping or data collection efforts by making multiple requests from different IP addresses. This helps avoid getting blocked by websites that have rate-limiting or anti-scraping measures in place.
7. **Legal and Ethical Compliance**: Proxies can be used to access websites in a manner that is compliant with their terms of service and legal regulations. By rotating IP addresses and not overloading servers, you can ensure responsible data collection practices.

_It's super easy to connect Bright Data proxies to your changedetection.io account or installation, head on over to_ [_**https://brightdata.com/integration/changedetection**_](https://brightdata.com/integration/changedetection) _to find out more!_

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### How to get product re-stock or \
Original URL: https://changedetection.io/tutorial/how-get-product-re-stock-or-back-stock-alerts-and-notifications

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

---

### How to get push notifications from a RSS Feed ? Detect changes in the RSS Feed! | changedetection.io
Original URL: https://changedetection.io/tutorial/how-get-push-notifications-rss-feed-detect-changes-rss-feed

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

Finally, click on the " **Notifications**" tab, here the notifications work by entering one of 85+ Â services as a Â "Notification URL" that will trigger a different push notification when your RSS feed changes.

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

---

### How to import your website change detection lists from Excel? | changedetection.io
Original URL: https://changedetection.io/tutorial/how-import-your-website-change-detection-lists-excel

[Skip to main content](https://changedetection.io/tutorial/how-import-your-website-change-detection-lists-excel#main-content)

# How to import your website change detection lists from Excel?

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 1 November, 2023



Topic

[How-To](https://changedetection.io/topic/how)

In this quick article I'll show you how to import your website URL lists from [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel) into changedetection.io

This can be super handy when you've managed to filter down your lists of websites to something really specific that you're interested in, or another way to manage your list of websites to check for changes.

It's super easy with changedetection.io.

**First**, You must save your excel spreadsheet that contains the list of websites you want to monitor as XLSX format (it will end .xlsx), there are even many old style website change detection providers Â that will let you export in XLSX format (Excel).

_This means that changedetection.io is an excellent alternative to Wachete, and many other "old style" providers that will export in XLSX Excel format._

**Second**, visit the **\[IMPORT\]** tab, here you can assign the columns in your data-set, usually spreadsheets use A, B, C, D type lableing of the columns, but in the watch importer it needs to know the number, so it means A=1, B=2, C=3

changedetection.io supports importing Folder/group/tag name, Filters (CSS or xPath), Name, URL and Recheck interval.

The recheck interval must be in minutes (integers), it will automatically be calculated back into days/hours/minutes in the watch settings.

![How to import a list of websites to watch from Excel](https://changedetection.io/sites/changedetection.io/files/inline-images/image_26.png)

**Third** Click import :)

And there you have it, how to quickly import from excel your list of websites to watch for changes

**Update 29/december/2023:** We will improve the importer so that it offers column letters instead of numbers

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### How to Monitor Government Agency News, Resources â€” A Legal Professionalâ€™s Perspective | changedetection.io
Original URL: https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective

[Skip to main content](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective#main-content)

# How to Monitor Government Agency News, Resources â€” A Legal Professionalâ€™s Perspective

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 20 December, 2024



Topic

[How-To](https://changedetection.io/topic/how)

**Leverage changedetection.io for Timely, Accurate Intelligence**

As a legal professional, you understand that staying on top of regulatory updates isnâ€™t just a matter of convenience; itâ€™s integral to offering informed guidance to your team and clients. Missing a crucial regulatory shift can quickly transform a well-prepared argument or strategy into outdated advice. Government agencies roll out changes with an almost dizzying frequency, and itâ€™s not always easy to catch every subtle tweak or new bulletin.

But who has time to constantly refresh a dozen agency websites? Hunting down these changes manually is inefficient, and relying on broad email newsletters often means wading through irrelevant noise. Instead, let changedetection.io be your digital â€œassociateâ€â€”quietly monitoring the pages you care about, and reporting back only when something meaningful happens.

### How Does changedetection.io Work?

**Simple, Targeted Website Change Monitoring**

changedetection.io automates the entire process of staying updated. Think of it as an online watchdog that scans your chosen websites at set intervals and flags even the smallest adjustments. Whenever a change is detected, you receive a clear, concise alertâ€”with any new text or removed language highlightedâ€”so you can review it at a glance and understand how it might impact your practice.

For legal professionals, this can mean:

- Quickly identifying new guidelines issued by regulatory bodies.
- Spotting changes to statutes, administrative rules, and compliance mandates.
- Interpreting updates in real-time, so you can advise your clients or partners without delay.

You can also refine your monitoring with keyword alerts, ensuring youâ€™re alerted only when specific terms related to your practice area appear or disappear.

### What Web Pages Can I Track with changedetection.io?

The beauty of changedetection.io is its flexibility. You can track almost any publicly accessible webpage, including (but certainly not limited to):

- Federal agency newsrooms and press release pages.
- State-level regulatory boards and commissions.
- Agency â€œWhatâ€™s New?â€ or â€œUpdatesâ€ sections, from environmental guidelines to health policy changes.
- Government licensing boards and professional standards portals.

In other words, if itâ€™s an authoritative online source for legal or regulatory content, changedetection.io can almost certainly keep an eye on it for you.

### How can changedetection.io can help my team? Can it communicate with Slack or Microsoft teams?

You can also step up your notification game by integrating changedetection.io alerts with various third-party platforms for real-time updates. We support just about every notification service imaginableâ€”your legal team can get notified directly through preferred channels, such as Microsoft Teams, Slack, or even SMS. This means the instant changedetection.io spots a legislative update that affects your practice area, your whole team can be pinged in the collaboration hub they already use every day, ensuring no one misses a beat and making rapid, well-informed decision-making easier than ever.

Keeping the information in your communication platform helps to keep your team working smoother - together. No more hiding or losing updates in one persons email.

What's more, you can keep the noise to a minimum and only [recheck important webpages for a change according to a schedule (say you just want an overview at 0900h every work day morning)](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule).

### Legislative Changes are Endless, but Manageable â€“ With changedetection.io

In a world where the regulatory landscape can pivot with little notice, having a digital ally to keep you informed is a game-changer. Instead of missing updates because you were tied up in a deposition or sifting through irrelevant newsletters, changedetection.io frees you to focus on applying the lawâ€”not chasing it.

By automating the watch for agency announcements, new rules, and policy adjustments, changedetection.io provides the timely intelligence you need to confidently advise your clients and maintain a competitive edge. Itâ€™s like having an extra pair of eyes dedicated solely to scanning the horizon for any shift that could matter to your practice.

**Ready to Keep Pace with Change?**

Sign up for changedetection.io, and get the updates you needâ€”exactly when you need themâ€”straight from the sources you trust.

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### How To Monitor Keywords On Any Website | changedetection.io
Original URL: https://changedetection.io/tutorial/how-monitor-keywords-any-website

[Skip to main content](https://changedetection.io/tutorial/how-monitor-keywords-any-website#main-content)

# How To Monitor Keywords On Any Website

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 4 April, 2025



Topic

[How-To](https://changedetection.io/topic/how)

## **How to Use Changedetection.io to Monitor Specific Keywords**

![](https://changedetection.io/sites/changedetection.io/files/inline-images/keyword.png)

In the world of breaking news and rapid financial updates, staying ahead of key developments is critical. Changedetection.io helps you to get **notifications of specific keywords** on just about any webpageâ€”whether it's a news outlet, financial report, or investor relations page. Get instant alerts when important terms appear, such as company names, stock tickers, or economic indicators, so you never miss a crucial update.

_**With changedetection.io you can monitor thousands of web pages for important keywords.**_

### Step 1: Add the URL to your changedetection.io dashboard

Simply copy and paste the URL of the page you wish to monitor for keywords, then click **EDIT > WATCH**, this will take us directly to the page to add the keywords

![Add page for keyword monitoring](https://changedetection.io/sites/changedetection.io/files/inline-images/keyword-setup_0.jpg)

### Step 2: Add the keywords to monitor - this will create a trigger for alerts

Click on **Filters & Triggers** and scroll down to " **Keyword triggers**", here you can setup the keywords to trigger on, they will be processed case-insensitive.

![Adding keyword triggers](https://changedetection.io/sites/changedetection.io/files/inline-images/adding-notification-keywords.jpeg)

Super easy! Now every time the web page is checked (even according to your custom schedule if you prefer!) the text content will be compared against your list of keywords, if those keywords are found in the text of the webpage, and there was a change in the webpage, you will get a notification!

Be sure to click on the **Notifications** tab and configure your favourite alerts, don't forget we support email, Discord, Slack, MS-Teams and 85+ others! The best way to keep your team informed.

### Step 3: Sit back and relax, let changedetection.io do the work!

### Extra points

What if you want to monitor keywords on a webpage every day at 0900? [You could use the scheduler and combine it with your keyword alert](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule)

From here you can also get more advanced and setup [Conditions](https://changedetection.io/tutorial/conditional-actions-web-page-changes), (perhaps you want to also add a rule that the page should NOT include certain keywords at the same time, the possibilities are endless!)

Take it even further with **Group Watches**, you could even assign hundreds of web-pages to the same **Group** and then simply add the **Keywords to Monitor** as a single **Group** setting, saving you time and making it a lot easier to manage large lists of web-pages that should be checked for the same keywords.

I encourage you to check it out, have a play, and see just what is possible with **Web Page Keyword Monitoring** with changedetection.io

All the best, have fun, and happy changedetecting!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### How to monitor a website for NEW content | changedetection.io
Original URL: https://changedetection.io/tutorial/how-monitor-website-new-content

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

---

### Monitoring HTML \
Original URL: https://changedetection.io/tutorial/monitoring-html-select-drop-down-changes-options

[Skip to main content](https://changedetection.io/tutorial/monitoring-html-select-drop-down-changes-options#main-content)

# Monitoring HTML "SELECT" drop down for changes to options

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 11 October, 2024



Topic

[How-To](https://changedetection.io/topic/how)

changedetection.io will automatically show any changes to <select><option> values, infact it renders them out ready for change detection on the fly

_**For example if we had..**_

`<select name="cars" id="cars">Â `

`Â <option value="volvo">Volvo</option>Â `

`Â <option value="saab">Saab</option>Â `

`Â <option value="mercedes">Mercedes</option>Â `

`Â <option value="audi">Audi</option>Â `

`</select>`

So this would appear by default in the " **Preview**"( or notification text ) Â as `"Volve Saab Mercedes Audio"`, however if you really wanted to see what changed you can also switch to _**HTML Source mode**_

changedetection.io can also monitor the HTML source of a web-page by simply prepending the " `source:`" keyword to the start of a page, for example below ;

(more on [monitoring changes to HTML sourcecode here](https://changedetection.io/tutorial/source-code-monitor-how-get-alerts-changes-html-source-code))

![Adding a URL for web page change detection of select element](https://changedetection.io/sites/changedetection.io/files/inline-images/image_86.png)

Then we can skip over to **Filters & Triggers** and add `select`, this way we can just focus on the `<select>` element for monitoring changes

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_87.png)

After a quick recheck, we can now see that "skoda" was added to the dropdown select element list items ( and if we configured notifications, we could get a notification via Discord, slack, email etc)

![HTML Select with changes ready for alerts](https://changedetection.io/sites/changedetection.io/files/inline-images/image_88.png)

Happy change detecting :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### NÃ¼rburgring racing passion - Get notified of news updates today from NÃ¼rburgring! | changedetection.io
Original URL: https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring

[Skip to main content](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring#main-content)

# NÃ¼rburgring racing passion - Get notified of news updates today from NÃ¼rburgring!

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 7 March, 2025



Topic

[How-To](https://changedetection.io/topic/how)

The NÃ¼rburgring, or "Green Hell," is the ultimate test of skill and endurance, beloved for its intense racing and unpredictable conditions. Recent updates include the NÃ¼rburgring 24 Hours joining the Intercontinental GT Challenge, with Ravenol as the new title sponsor. The 2024 race, shortened by heavy fog, saw Scherer Sport PHX take a historic seventh win - Find out how to get notified when the official NÃ¼rburgring website updates its news section! stay informed! **Get daily NÃ¼rburgring news updates to your inbox.**

![NÃ¼rburgring updates today](https://changedetection.io/sites/changedetection.io/files/2025-03/N%C3%BCrburgring-updates-today.png)

Let's setup a simple monitor to send a notification via email when the NÃ¼rburgring website has an update today.

You could use this same method for many other similar Motorsport websites.

Fortunately we can very simply setup changedetection.io to recheck their website at a regular interview and send an update.

So, start your engines, let's go!

### Step 1. Start your engines!

Log into your changedetection.io account and add the link to the NÃ¼rburgring news section **https://nuerburgring.de/news/**

![nuerburgring news update link](https://changedetection.io/sites/changedetection.io/files/inline-images/image_104.png)

You will then see that changedetection.io is automatically checking the news section, this should take 10-15 seconds.

![NÃ¼rburgring website updates checking news](https://changedetection.io/sites/changedetection.io/files/inline-images/image_105.png)

Fantastic!

### Step 2. Select just the "news section" from the web page.

NÃ¼rburgring website has a LOT of fantastic information, some of it might not be important to you, for example in the header they have the current temperature :) so lets just select the news block

- Click **EDIT** then visit the **Visual Selector** tab.
- Click on the news grid, it will add a **red box** to signify that only that area will be used for web page change detections.


![News updates today section](https://changedetection.io/sites/changedetection.io/files/inline-images/image_106.png)

### Step 3. Add your email in the notifications tab

After selecting the news section of the website, simply click on the **Notifications** tab. click the **Add email** button below the textbox, Add your email then click **SAVE**

![NÃ¼rburgring updates to email setup](https://changedetection.io/sites/changedetection.io/files/inline-images/image_110.png)

Sit back, relax, we will re-check the website and email you when ever there is a news update - we also encourage you to explore the other features of the service!

We'll leave you with this one heartfelt message :)

![news updates today](https://changedetection.io/sites/changedetection.io/files/inline-images/image_111.png)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Pre-fill dynamic form \
Original URL: https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts

[Skip to main content](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts#main-content)

# Pre-fill dynamic form "date" fields and get web page change alerts

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 20 January, 2025



Topic

[How-To](https://changedetection.io/topic/how)

A common situation is when you need to pre-fill / fill-in some data in a web page form such as the "current date", this an example would be when booking a trailor or reserving a car-parking space.

![Pre-fill date field before web page change detection](https://changedetection.io/sites/changedetection.io/files/inline-images/image_95.png)

Obviously, entering the current date directly is going to be a lot more easier to configure than using the calendar that the web page comes with (which are often really hard to navigate, even by humans!)

One really great feature of changedetection.io is that we try to support "Jinja2" macros where-ever possible, so this means you can insert the current date/time in whatever format you like using Browser Steps

So let's get to it!

## Automatically enter he current date in an input box

- Activate the **Browser Steps** for the webpage you are monitoring for changes, give it a few moments to connect.
- Mouse over the input field (highlighted in red) and click it.
- The software will identify the element as an input/text box and ask you to enter some text, this is where the magic happens.


![Setting the current date in a field before web page change detection](https://changedetection.io/sites/changedetection.io/files/inline-images/image_93.png)

Now the website automatically prefills the date with next months date, but we want to be sure we enter todays date when ever the web page change detection runs, so that we could perhaps see if any car parking places are available today.

- Enter `{% now Â 'Europe/Berlin', '%d-%m-%Y' %}` Â in the " _**value**_" field under the " **Enter text in field**" box on the right.
- Click **Apply** to see the changes take affect.

![Automatically set the date on web page change detection form](https://changedetection.io/sites/changedetection.io/files/inline-images/image_94.png)

Now you can see that the field is correctly set to today's date ( _20-1-2025)_ According to the "Europe/Berlin" timezone)

Entering a timezone is super important, because the server may run in a different timezone than yourself, you can choose any timezone from [https://en.wikipedia.org/wiki/List\_of\_tz\_database\_time\_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

As always, Happy web page change detection :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Source code monitor - How to get alerts on changes to HTML source code | changedetection.io
Original URL: https://changedetection.io/tutorial/source-code-monitor-how-get-alerts-changes-html-source-code

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

Then, for example let's say we are interesting in getting alerts/notifications when that website changes their `<title>` tag, click **\[edit\]** then head on over to **Filters Â & Triggers**

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

---

### Synology NAS - How to get alerts on new software updates via Discord! | changedetection.io
Original URL: https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord

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

Now your overview list should look something like below (We clicked \[edit\] then Â ticked the "Use <title> as title of the watch" option so it's a little easier to read)

![Synology NAS production URL list](https://changedetection.io/sites/changedetection.io/files/inline-images/image_70.png)

Now the Synology NAS website has a lot of extra information in the footers and headers, using the **Visual Selector** tool available under **\[edit\]** we simply select the actual content area

![Synology NAS Visual Selector tool example](https://changedetection.io/sites/changedetection.io/files/inline-images/image_71.png)

You can see that changedetection.io has correctly identified **//\*\[@id="release\_notes\_content"\]** as the place where the the content lives (this is the area of the web page that would be used for change detection)

Now when Synology NAS release a new version/update you should be able to see the differences

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_72.png)

### Connecting Discord

To have a bot send notifications to your serverâ€™s channel you need to paste in the following "Notification URL" in the notification settings

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

---

### Using Bright Data's \
Original URL: https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring

[Skip to main content](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring#main-content)

# Using Bright Data's "Scraping Browser" to by-pass CAPTCHA's and other protection when monitoring pages

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 16 November, 2024



Topic

[How-To](https://changedetection.io/topic/how)

[Proxies](https://changedetection.io/topic/proxies)

For many websites - simply using a proxy is not enough, the website is using much more complex anti-robot software to detect the actual browser that is being used, not just the IP connection or headers (including common headers such as user-agent and others)

You need a better way to simulate a real browser - A scraping browser is different to a proxy, a proxy just tunnels your connection but the Browser still looks the same, with a scraping browsers you are also simulating a real browser hidden away in Bright Data's infrastructure.

As it turns out, many websites are probing much deeper into your browser - analysing the response from your 2D and 3D/GPU videocard is just one of the tactics they use.

Unfortunately for many headless Chrome sessions it means they stand out all too easy - their "fingerprint" is just too obvious, they dont have anything that resembles a real video card or other hardware attached.

The result is - you get pushed to enter a CAPTCHA or other similar anti-robot mechanism.

_**But there is a solution,**_ whilst not guaranteed - it definitely helps a lot!

The clever people over at Bright Data have added a "Scraping Browser" to their offers, which more precisely simulates a real browser than just about anything you can try to run yourself.

(note: this functionality in changedetection.io will be released late November 2023, but you can try it now under the current _master_ tag from our [GitHub](https://github.com/dgtlmoon/changedetection.io) or [dev tag from our Docker Hub](https://hub.docker.com/layers/dgtlmoon/changedetection.io/dev/images/sha256-2397ad50a81527514492e859da685dada3863659b1e233f8e8f020eb08af0da0?context=explore))

More information about [Bright Data's scraping browser can be found here.](https://brightdata.com/products/scraping-browser)

#### _**Here's how to setup Bright Data's "Scraping Browser" with changedetection.io**_

Head on over to your Bright Data _**control panel**_ \- When you sign up using this link - Â [https://brightdata.grsm.io/n0r16zf7eivq](https://brightdata.grsm.io/n0r16zf7eivq) \- BrightData will match any first deposit up to $150.

Once logged in - click on _**"Scraping Browser"**_

![The Bright Data control panel - where to find the Scraping Browser link](https://changedetection.io/sites/changedetection.io/files/inline-images/image_28.png)

Now we will copy the special "Connection address" so changedetection.io knows how to find the Scraping Browser, click on **Check out code and integration examples o** n the bottom right.

It's also worth considering here that you can add on extra residential proxies , residential proxies also greatly increase your chance of skipping past any potential CAPTCHA issues, but for now we will continue with the default setup.

![The Bright Data control panel - where to find the Scraping Browser link](https://changedetection.io/sites/changedetection.io/files/inline-images/image_33.png)

Copy the text from the next page into your clipboard, it will start with **wss://**, be sure to not include any quotes or other text, copy the whole text which is marked in blue below.

![The Bright Data control panel - where to find the Scraping Browser wss:// link for changedetection](https://changedetection.io/sites/changedetection.io/files/inline-images/image_34.png)

Now for the fun part, jump over to Â your changedetection.io login and click on **Settings > CAPTCHA & Proxies,** scroll down to the _**"Extra Browsers"**_ section, give your browser a name (in this case just **BrightData Scraping Browser** and paste the **wss://...** type URL into the **Connection URL** box

![Adding a scraping browser to changedetection.io - step 1 adding the browser link](https://changedetection.io/sites/changedetection.io/files/inline-images/image_37.png)

Now to use your new Scraping Browser with any website you are watching for changes, simply click **Edit** in your overview list and select the new browser

![list of websites with changes overview](https://changedetection.io/sites/changedetection.io/files/inline-images/image_39.png)

Choose the new browser **Bright Data Scraping Browser** that we setup in the previous step.

![Setting a single website to use a particular scraping browsers](https://changedetection.io/sites/changedetection.io/files/inline-images/image_40.png)

And there you have it - _how to setup a scraping browser to get a much better success rate (say goodbye CAPTCHA!) when watching websites for changes._

_Some extra tips -_

When you setup additional Residential Proxies - Bright Data will present you with a new "wss://.." type connection URL, so you can then setup multiple proxy networks with multiple scraping browsers.

Sign up with Bright Data using [https://brightdata.grsm.io/n0r16zf7eivq](https://brightdata.grsm.io/n0r16zf7eivq) BrightData will match any first deposit up to $150

### Troubleshooting

If you see the error Â " `Overriding accept-language, user-agent headers forbidden`" \- Â You may need to enable " _Custom headers_" \- In your Brightdata dashboard - under the `Proxy Settings` \> `Configuration` \> `Advanced Settings` \> `Custom headers & cookies` this option needs to be activated. (changedetection.io may send its own custom User-Agent and other headers)

If you receive an error like `"WebSocket error: wss://brd-customer..... 403 wrong_auth"` then try whitelisting the IP of our server (or your local connection) from inside the BrightData control panel at the "Scraping Browser" settings - as an alternative to username+password (But still keep the username+password in the `wss://.. ` connection URL)

![Example of adding a white-list IP access in BrightData for the scraping browser](https://changedetection.io/sites/changedetection.io/files/inline-images/image_52.png)

Happy changedetecting!

**extra points!** You can now use the built-in proxy scanner to see which websites still give the 403 access denied error, check it out here [https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)

Your browser does not support the video tag.


- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Vevor Tools - easily monitor restock and get alerts on discounts! | changedetection.io
Original URL: https://changedetection.io/tutorial/vevor-tools-easily-monitor-restock-and-get-alerts-discounts

[Skip to main content](https://changedetection.io/tutorial/vevor-tools-easily-monitor-restock-and-get-alerts-discounts#main-content)

# Vevor Tools - easily monitor restock and get alerts on discounts!

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 5 September, 2024



Topic

[How-To](https://changedetection.io/topic/how)

If you're a fan of [Vevor tools](https://vevor.com/), you can buy them directly from their website. But even better than that is catching those irresistible clearance sales, restocks, and deep discounts on their products.

With changedetection.io, you can effortlessly set up alerts for price drops and restocks, ensuring you never miss a deal or the chance to grab a tool as soon as it's back in stock.

## How to setup alerts when a Vevor Tools product changes price or has a discount.

**Step 1:** Copy+Paste the link (URL) to the [Vevor Tools](https://vevor.com/) page you want to monitor and select "Re-stock & Price detection for single product pages".

Import is to select the **"Re-stock & Price detection for single product pages"** option, this will turn on the various options for following the product price (Such as being able to set limits/thresholds on the price of the product before sending a notification)

![Vevor Tools - Adding a web-page](https://changedetection.io/sites/changedetection.io/files/inline-images/image_81.png)

**Step 2**: Congratulations! By default, changedetection.io will automatically track any price or restock changes on the Vevor tools product URLs you've added. You can see this in the _"Restock & Price"_ column.

![Watching Vevor products for changes in price or restock](https://changedetection.io/sites/changedetection.io/files/inline-images/image_82.png)

### How to setup notifications for discounts of the Vevor tools products and score a bargain?

Simply click **\[EDIT\]** at the list of website watches for the page/product you're interested in, then click **"Restock & Price Detection",** over on this tab is where you can setup alerts based on ;

- Price below $/GBP/EUR (If it goes OVER a certain amount, send alert)
- Price lower $/GBP/EUR (If it goes UNDER a certain amount, send alert)
- Price change by % - Probably the best option, for example you could get an alert if the Vevor product you're interested in goes on sale by more than 5% since the first check.

![Price threshold alerts for vevor products on sale](https://changedetection.io/sites/changedetection.io/files/inline-images/image_83.png)

Perfect!

### How to add Email or Discord notifications to Vevor Tools product price discounts and restocks?

Probably our most asked question, fortunately it's exactly the same as setting up notifications for any other Â web-page change alert. Fortunately it's super simple, just click the \[ **Notifications\]** tab (available on each web-page watch, or under "Settings" to only set it up once for all watches)

Then click **"Add email" ,** it will ask you what email address you prefer and fill in the details automatically for you.

![Email configuration vevor products restock and price change alert](https://changedetection.io/sites/changedetection.io/files/inline-images/image_84.png)

##### What about Discord notifications of Vevor Product price changes?

Super easy, following the same configuration page, paste in your Discord "webhook" URL to your bot/channel (more about [Discord configuration here](https://github.com/caronc/apprise/wiki/Notify_discord))

![Discord Vevor tools product price change webhook](https://changedetection.io/sites/changedetection.io/files/inline-images/image_85.png)

You can add as many notification types as you like, don't forget we support dozens of various Productivity based notification systems, not just email! including but not limited to AWS SES, Discord, Google Chat, Line Mastodon, Matrix, Microsoft teams, [Slack and more!](https://github.com/caronc/apprise?tab=readme-ov-file#productivity-based-notifications)

Happy product hunting :)

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Web page change monitoring with Webshare proxies | changedetection.io
Original URL: https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies

[Skip to main content](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies#main-content)

# Web page change monitoring with Webshare proxies

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 27 December, 2024



Topic

[How-To](https://changedetection.io/topic/how)

Integrating proxies with Changedetection takes website monitoring to a professional level by addressing challenges like regional restrictions, IP bans, and task scalability. Hereâ€™s how [Webshare proxies](https://www.webshare.io/) enhance Changedetection:

- **Access Geo-Restricted Websites:** Webshare proxies allow you to bypass regional restrictions by routing your requests through servers in specific locations. For example, if a website is accessible only to users in the US, using a proxy with a US IP address enables Changedetection to monitor that site seamlessly. This feature is invaluable for tracking region-specific content like local promotions, regional news updates, or country-specific pricing changes.
- **Avoid IP Restrictions:** Monitoring websites often involves sending frequent or repetitive requests, which may lead to your IP address being flagged or blocked. Webshare proxies mitigate this risk by rotating IP addresses, simulating requests from different users. This approach reduces the likelihood of detection and ensures uninterrupted monitoring, even on sites with strict anti-scraping measures.
- **Scale Monitoring Across Multiple Sites:** Tracking multiple web pages simultaneously can overload a single IP address, triggering rate limits or temporary blocks. Webshare proxies distribute these requests across multiple IPs, allowing you to monitor a higher number of pages without disruptions.
- **Enhanced Privacy and Security:** Webshare proxies mask your actual IP address, providing an added layer of anonymity and safeguarding your monitoring activities. This protection is crucial when tracking sensitive content, such as competitor websites or exclusive data, where you donâ€™t want your actions to be easily traceable.
- **Improved Speed and Reliability:** High-quality Webshare proxies often provide faster and more stable connections than your regular network. This reduces delays in fetching updates and ensures that Changedetection performs consistently, even under heavy monitoring workloads or network fluctuations.
- **Ensure Legal and Ethical Compliance:** Webshare proxies enable monitoring activities to comply with regional laws and website policies. By ensuring access through approved regional proxies or adhering to site-specific terms of use, you can conduct ethical monitoring without violating restrictions.

## Proxy setup method for beginners

When integrating Changedetection with Webshare proxies, we'll cover a general beginner-friendly proxy setup first, followed by an advanced setup using rotating proxies.

### 1\. Subscribe to Changedetection.io

Begin by subscribing to [Changedetection.io](https://changedetection.io/). Once youâ€™ve successfully created an account, youâ€™ll receive your credentials via email. Use these credentials to login and launch the web application in your browser.

![join and setup](https://changedetection.io/sites/changedetection.io/files/inline-images/1-setup_0.png)

### 2\. Access the SETTINGS menu

After logging in, navigate to the top menu bar and click on **SETTINGS** to access the configuration options.

![access settings](https://changedetection.io/sites/changedetection.io/files/inline-images/2-settings.png)

### 3\. Select the CAPTCHA & Proxies tab

Within the settings menu, locate and click on the **CAPTCHA & Proxies** tab. This section allows you to add and manage proxy configurations for your monitoring tasks.

![Visit the proxies tab](https://changedetection.io/sites/changedetection.io/files/inline-images/3-select.png)

### 4\. Webshare proxy credentials

For Webshare proxies, [sign up for the free plan](https://www.webshare.io/?referral_code=0yb98y7xwmku) to access 10 free datacenter proxies. These proxies are shared, limited to 1GB of bandwidth per month, and include options for both rotating and static configurations. Youâ€™ll find the necessary proxy details (username, password, host, and port) in your Webshare account dashboard.

Next, we will cover instructions for two different types of proxies - residential and datacenter. Pick one whichever you have subscribed for. The free proxy server plan is using datacenter proxies.

### 5\. Configure residential proxies

To configure residential proxies, enter the proxy URL in the recommended format:

**http://username:password@host:port**

For example:

**http://username:password@p.webshare.io:80**

![List of residential proxies for web page change detection](https://changedetection.io/sites/changedetection.io/files/inline-images/5-proxies.png)

â€

Replace username, password, host, and port with the details provided by Webshare. Once added, click **Save** to confirm the settings.

### 6\. Configure datacenter proxies

To configure datacenter proxies, use the same URL format as above. As an example, hereâ€™s how you can configure a Webshare datacenter proxy:

**http://username:password@198.23.239.134:6540**

![Setup datacenter proxies in Webshare](https://changedetection.io/sites/changedetection.io/files/inline-images/6a.png)

â€

Replace the placeholders with your datacenter proxy credentials.

## Advanced proxy setup - rotating proxies

Hereâ€™s how to set up Webshare rotating proxies in Changedetection:

**Access Webshare Dashboard:** Log in to your Webshare account and navigate to the **Proxy List** section.

**Select Connection and Authentication Method:** Under Connection Method, select **Rotating Proxy Endpoint**. This option ensures a new proxy IP is assigned with each request. For authentication, choose **Username/Password**.

![Setup rotating proxies](https://changedetection.io/sites/changedetection.io/files/inline-images/6a_0.png)

**Copy Proxy Details:** Use the provided details from your Webshare dashboard:

**Domain Name, Proxy Port**, **Proxy Username**, and **Proxy Password.**

![Rotating proxies part 2](https://changedetection.io/sites/changedetection.io/files/inline-images/6b.png)

**Add the Proxy URL to Changedetection:** Create the proxy url in the same format as discussed above, enter it under the **Proxy URL** field and click **Save**.

![Adding the proxy to changedetection.io](https://changedetection.io/sites/changedetection.io/files/inline-images/6d.png)

**Enable Proxies in General Settings**

- Go back to the **General** Settings section.
- Scroll down to the Proxy Configuration area.
- Choose your newly added proxies to be used for change detection tasks.

![Enabling the proxy in changedetection](https://changedetection.io/sites/changedetection.io/files/inline-images/6e.png)

You are now ready to monitor website content changes seamlessly, without geo-restrictions.

## Wrapping up

Integrating Webshare proxies with Changedetection allows you to overcome regional restrictions, avoid IP bans, and scale monitoring tasks seamlessly. By combining Webshare's reliable proxy services with Changedetection's powerful change-tracking features, you can ensure accurate, uninterrupted and efficient website monitoring.

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Website content change detection from behind logins - easy | changedetection.io
Original URL: https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy

[Skip to main content](https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy#main-content)

# Website content change detection from behind logins - easy

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 13 August, 2023



Topic

[How-To](https://changedetection.io/topic/how)

[Browser Steps](https://changedetection.io/topic/browser-steps)

[Use-case](https://changedetection.io/topic/use-case)

Another great feature of changedetection.io is that you can interact with websites to compare their content.

Often you need to enter in some search query or need to access a page that's only available from behind a login/password form.

Or maybe perform change detection from behind password protected websites?

_**Note: Â Only use this on websites where you have permission todo so, and always "recheck" with the maximum realistic time between rechecks, logging-in every minute could get you blocked from the site you are viewing.**_

Some examples where this is super handy could be

- Get an alert when a new invoice is available
- Get an alert when your school publishes new important information.
- Accept cookie popup forms
- Log in to a website to be able to scrape data for other uses (for example you could now make a nice Discord bot that reports new articles that appear from behind a login)

![Screenshot for supplying login details to perform change detection from behind a login](https://changedetection.io/sites/changedetection.io/files/inline-images/image_12.png)

Changedetection.io makes this super easy by providing an easy to use setup page where you can click on individual elements on the page and then enter in the kind of event you want to happen, changedetection.io will automatically detect which action is best for whatever element you selected (for example, enter text in field, click buttons etc)

You could even use this to perform realestate searches, searching for your dream job and more, it's all up to your imagination!

I recommend that you explore this feature, it's so super helpful!

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

### Tutorials | changedetection.io
Original URL: https://changedetection.io/tutorials

[Skip to main content](https://changedetection.io/tutorials#main-content)

# Changedetection.io Tutorials

Want to know more? Need some more inspiration? How do you get the most from changedetection.io ? Read on!

- [![Ubiquity store - How to get restock / back in stock notifications ](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/ubiquiti-store-restock.png?itok=vrrfSIXG)](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)








- How-To

[How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)

17 April, 2025

If you've been trying to get your hands on Ubiquiti gearâ€”like the Power Distribution Pro, Cloud Gateway Fiber, or that elusive Dream Machine Proâ€”you know the story: blink, and it's sold out. Hitting refresh all day just doesnâ€™t cut it anymore. But thereâ€™s a smarter way to shopâ€”and it takes less than five minutes to set up.

- [![beating 403 access denied - proxy scanner](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/403-access-denied-proxy-scanner.png?itok=ZgdFG2vE)](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)








- How-To

[Find the best proxy to beat "403 access denied" with our proxy scanner](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)

13 April, 2025

A proxy scanner helps identify working proxies that successfully retrieve pages without being denied, ensuring consistent access to accurate data - Fortunately changedetection.io has a proxy scanner built in!

- [![How to Use Changedetection.io to Monitor Specific Keywords](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/keyword.png?itok=z2tS8Gs3)](https://changedetection.io/tutorial/how-monitor-keywords-any-website)








- How-To

[How To Monitor Keywords On Any Website](https://changedetection.io/tutorial/how-monitor-keywords-any-website)

4 April, 2025

In the world of breaking news and rapid financial updates, staying ahead of key developments is critical. Changedetection.io helps you to get notifications of specific keywords on just about any webpage - Here's how to setup keyword monitoring in a snap!

- [![Conditional web page change alerts!](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-03/image_114.png?itok=byv9o-pd)](https://changedetection.io/tutorial/conditional-actions-web-page-changes)








- How-To

[Conditional actions on web page changes!](https://changedetection.io/tutorial/conditional-actions-web-page-changes)

31 March, 2025

Changedetection.io introduces one of its most powerful features yet: conditional actions. This opens the door to much more precise and flexible monitoring.

Itâ€™s no longer just about detecting when content changes â€” now you can define exactly what kind of change matters to you. For example, trigger an alert only when a productâ€™s price drops below a certain threshold, or when a keyword appears in the updated content.

- [![NÃ¼rburgring updates today](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-03/N%C3%BCrburgring-updates-today.png?itok=nfDcrZ-E)](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring)








- How-To

[NÃ¼rburgring racing passion - Get notified of news updates today from NÃ¼rburgring!](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring)

7 March, 2025

The NÃ¼rburgring, or "Green Hell," is the ultimate test of skill and endurance, beloved for its intense racing and unpredictable conditions. Recent updates include the NÃ¼rburgring 24 Hours joining the Intercontinental GT Challenge, with Ravenol as the new title sponsor.

- [![GeForce RTX 5090 5080 restock alert](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/geforce-rtx-5090-learn-more-og-1200x630.jpg?itok=cKsJOwqr)](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)








- How-To

[BestBuy restock alerts - GeForce RTX 5090 & GeForce RTX 5080 are out!](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)

31 January, 2025

The NVIDIA GeForce RTX 5090 and RTX 5080 have arrived, delivering unprecedented power with next-gen AI, lightning-fast frame rates, and jaw-dropping ray tracing. These GPUs are selling out fast, but with Changedetection.io, you can stay ahead of the rush and grab one the moment they restock!

- [![Kmart restock alerts](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/kmart.jpg?itok=rRRrxTTZ)](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others)








- How-To

[Kmart Shopping - Easily monitor prices and get restock alerts via email, discord, and others.](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others)

20 January, 2025

Kmart is a great place to shop for every day needs, but what is even better is getting alerts when items come back in stock or when they are on sale (price reduced!)

In this quick tutorial I'll show you how to setup changedetection.io to notify you when items are re-stocked or have a price change.

- [![Dynamic form - Prefill date value before web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/dynamic-form-set-value-page-change-detection.jpg?itok=ZOUKiiAz)](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts)








- How-To

[Pre-fill dynamic form "date" fields and get web page change alerts](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts)

20 January, 2025

A common situation is when you need to pre-fill / fill-in some data in a web page form such as the "current date", this an example would be when booking a trailor or reserving a car-parking space.

- [![Webshare proxies with  web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-12/webshare-changedetection-page-changes.jpg?itok=pWkOgmsq)](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies)








- How-To

[Web page change monitoring with Webshare proxies](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies)

27 December, 2024

Integrating proxies with Changedetection takes website monitoring to a professional level by addressing challenges like regional restrictions, IP bans, and task scalability. Hereâ€™s how [Webshare proxies](https://www.webshare.io/) enhance Changedetection:

- [![](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/default_images/temp.png?itok=0vsexsQ8)](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective)








- How-To

[How to Monitor Government Agency News, Resources â€” A Legal Professionalâ€™s Perspective](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective)

20 December, 2024

As a legal professional, you understand that staying on top of regulatory updates isnâ€™t just a matter of convenience; itâ€™s integral to offering informed guidance to your team and clients. Missing a crucial regulatory shift can quickly transform a well-prepared argument or strategy into outdated advice.

- [![How to check web pages for changes according to schedule](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-12/scheduler.jpg?itok=x-8CIMbB)](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule)








- How-To

[Checking web pages for changes according to a schedule](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule)

19 December, 2024

One fantastic example is when you want to check for new headlines at your favourite finance news website every day at 0900h, explore how to easily set this up, and more!

- [![How to get past CAPTCHA](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-11/defeating-captcha.jpeg?itok=eF7uw84r)](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring)








- How-To
- Proxies

[Using Bright Data's "Scraping Browser" to by-pass CAPTCHA's and other protection when monitoring pages](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring)

16 November, 2024

For many websites - simply using a proxy is not enough, the website is using much more complex anti-robot software to detect the actual browser that is being used, not just the IP connection or headers (including common headers such as user-agent and others)

You need a better way to simulate a real browser.

---

### Tutorials | changedetection.io
Original URL: https://changedetection.io/tutorials?page=0

[Skip to main content](https://changedetection.io/tutorials?page=0#main-content)

# Changedetection.io Tutorials

Want to know more? Need some more inspiration? How do you get the most from changedetection.io ? Read on!

- [![Ubiquity store - How to get restock / back in stock notifications ](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/ubiquiti-store-restock.png?itok=vrrfSIXG)](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)








- How-To

[How to Never Miss a Ubiquiti Restock Again (in 5 Minutes or Less)](https://changedetection.io/tutorial/how-never-miss-ubiquiti-restock-again-5-minutes-or-less)

17 April, 2025

If you've been trying to get your hands on Ubiquiti gearâ€”like the Power Distribution Pro, Cloud Gateway Fiber, or that elusive Dream Machine Proâ€”you know the story: blink, and it's sold out. Hitting refresh all day just doesnâ€™t cut it anymore. But thereâ€™s a smarter way to shopâ€”and it takes less than five minutes to set up.

- [![beating 403 access denied - proxy scanner](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/403-access-denied-proxy-scanner.png?itok=ZgdFG2vE)](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)








- How-To

[Find the best proxy to beat "403 access denied" with our proxy scanner](https://changedetection.io/tutorial/find-best-proxy-beat-403-access-denied-our-proxy-scanner)

13 April, 2025

A proxy scanner helps identify working proxies that successfully retrieve pages without being denied, ensuring consistent access to accurate data - Fortunately changedetection.io has a proxy scanner built in!

- [![How to Use Changedetection.io to Monitor Specific Keywords](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-04/keyword.png?itok=z2tS8Gs3)](https://changedetection.io/tutorial/how-monitor-keywords-any-website)








- How-To

[How To Monitor Keywords On Any Website](https://changedetection.io/tutorial/how-monitor-keywords-any-website)

4 April, 2025

In the world of breaking news and rapid financial updates, staying ahead of key developments is critical. Changedetection.io helps you to get notifications of specific keywords on just about any webpage - Here's how to setup keyword monitoring in a snap!

- [![Conditional web page change alerts!](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-03/image_114.png?itok=byv9o-pd)](https://changedetection.io/tutorial/conditional-actions-web-page-changes)








- How-To

[Conditional actions on web page changes!](https://changedetection.io/tutorial/conditional-actions-web-page-changes)

31 March, 2025

Changedetection.io introduces one of its most powerful features yet: conditional actions. This opens the door to much more precise and flexible monitoring.

Itâ€™s no longer just about detecting when content changes â€” now you can define exactly what kind of change matters to you. For example, trigger an alert only when a productâ€™s price drops below a certain threshold, or when a keyword appears in the updated content.

- [![NÃ¼rburgring updates today](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-03/N%C3%BCrburgring-updates-today.png?itok=nfDcrZ-E)](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring)








- How-To

[NÃ¼rburgring racing passion - Get notified of news updates today from NÃ¼rburgring!](https://changedetection.io/tutorial/nurburgring-racing-passion-get-notified-news-updates-today-nurburgring)

7 March, 2025

The NÃ¼rburgring, or "Green Hell," is the ultimate test of skill and endurance, beloved for its intense racing and unpredictable conditions. Recent updates include the NÃ¼rburgring 24 Hours joining the Intercontinental GT Challenge, with Ravenol as the new title sponsor.

- [![GeForce RTX 5090 5080 restock alert](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/geforce-rtx-5090-learn-more-og-1200x630.jpg?itok=cKsJOwqr)](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)








- How-To

[BestBuy restock alerts - GeForce RTX 5090 & GeForce RTX 5080 are out!](https://changedetection.io/tutorial/bestbuy-restock-alerts-geforce-rtx-5090-geforce-rtx-5080-are-out)

31 January, 2025

The NVIDIA GeForce RTX 5090 and RTX 5080 have arrived, delivering unprecedented power with next-gen AI, lightning-fast frame rates, and jaw-dropping ray tracing. These GPUs are selling out fast, but with Changedetection.io, you can stay ahead of the rush and grab one the moment they restock!

- [![Kmart restock alerts](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/kmart.jpg?itok=rRRrxTTZ)](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others)








- How-To

[Kmart Shopping - Easily monitor prices and get restock alerts via email, discord, and others.](https://changedetection.io/tutorial/kmart-shopping-easily-monitor-prices-and-get-restock-alerts-email-discord-and-others)

20 January, 2025

Kmart is a great place to shop for every day needs, but what is even better is getting alerts when items come back in stock or when they are on sale (price reduced!)

In this quick tutorial I'll show you how to setup changedetection.io to notify you when items are re-stocked or have a price change.

- [![Dynamic form - Prefill date value before web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2025-01/dynamic-form-set-value-page-change-detection.jpg?itok=ZOUKiiAz)](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts)








- How-To

[Pre-fill dynamic form "date" fields and get web page change alerts](https://changedetection.io/tutorial/pre-fill-dynamic-form-date-fields-and-get-web-page-change-alerts)

20 January, 2025

A common situation is when you need to pre-fill / fill-in some data in a web page form such as the "current date", this an example would be when booking a trailor or reserving a car-parking space.

- [![Webshare proxies with  web page change detection](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-12/webshare-changedetection-page-changes.jpg?itok=pWkOgmsq)](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies)








- How-To

[Web page change monitoring with Webshare proxies](https://changedetection.io/tutorial/web-page-change-monitoring-webshare-proxies)

27 December, 2024

Integrating proxies with Changedetection takes website monitoring to a professional level by addressing challenges like regional restrictions, IP bans, and task scalability. Hereâ€™s how [Webshare proxies](https://www.webshare.io/) enhance Changedetection:

- [![](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/default_images/temp.png?itok=0vsexsQ8)](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective)








- How-To

[How to Monitor Government Agency News, Resources â€” A Legal Professionalâ€™s Perspective](https://changedetection.io/tutorial/how-monitor-government-agency-news-resources-legal-professionals-perspective)

20 December, 2024

As a legal professional, you understand that staying on top of regulatory updates isnâ€™t just a matter of convenience; itâ€™s integral to offering informed guidance to your team and clients. Missing a crucial regulatory shift can quickly transform a well-prepared argument or strategy into outdated advice.

- [![How to check web pages for changes according to schedule](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-12/scheduler.jpg?itok=x-8CIMbB)](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule)








- How-To

[Checking web pages for changes according to a schedule](https://changedetection.io/tutorial/checking-web-pages-changes-according-schedule)

19 December, 2024

One fantastic example is when you want to check for new headlines at your favourite finance news website every day at 0900h, explore how to easily set this up, and more!

- [![How to get past CAPTCHA](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-11/defeating-captcha.jpeg?itok=eF7uw84r)](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring)








- How-To
- Proxies

[Using Bright Data's "Scraping Browser" to by-pass CAPTCHA's and other protection when monitoring pages](https://changedetection.io/tutorial/using-bright-datas-scraping-browser-pass-captchas-and-other-protection-when-monitoring)

16 November, 2024

For many websites - simply using a proxy is not enough, the website is using much more complex anti-robot software to detect the actual browser that is being used, not just the IP connection or headers (including common headers such as user-agent and others)

You need a better way to simulate a real browser.

---

### Tutorials | changedetection.io
Original URL: https://changedetection.io/tutorials?page=1

[Skip to main content](https://changedetection.io/tutorials?page=1#main-content)

# Changedetection.io Tutorials

Want to know more? Need some more inspiration? How do you get the most from changedetection.io ? Read on!

- [![Simple email alerts for web page changes - how to](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-10/email-alert.jpg?itok=upKV_Erz)](https://changedetection.io/tutorial/email-notification-when-web-page-changes-how)








- How-To

[Email notification when a web page changes - How To](https://changedetection.io/tutorial/email-notification-when-web-page-changes-how)

17 October, 2024

In this tutorial, weâ€™ll walk you through how to set up a web page monitor and configure email notifications for any updates or changes to that webpage.

- [![How to monitor a <select> dropdown for changes and get alerts](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-10/dropdown-select-monitor-change.jpeg?itok=8WQ4ajBg)](https://changedetection.io/tutorial/monitoring-html-select-drop-down-changes-options)








- How-To

[Monitoring HTML "SELECT" drop down for changes to options](https://changedetection.io/tutorial/monitoring-html-select-drop-down-changes-options)

11 October, 2024

changedetection.io can automatically show any changes to values, infact it renders them out ready for change detection on the fly, learn more

- [![vevor tool restock and price discount change](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-09/vevor-tool-m100-1.2-3829748392_0.jpg?itok=FRvHYTI7)](https://changedetection.io/tutorial/vevor-tools-easily-monitor-restock-and-get-alerts-discounts)








- How-To

[Vevor Tools - easily monitor restock and get alerts on discounts!](https://changedetection.io/tutorial/vevor-tools-easily-monitor-restock-and-get-alerts-discounts)

5 September, 2024

If you're a fan of [Vevor tools](https://vevor.com/), you can buy them directly from their website. But even better than that is catching those irresistible clearance sales, restocks, and deep discounts on their products.

- [![No web spiders!](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-05/no-spider.png?itok=QPELSmrc)](https://changedetection.io/tutorial/what-are-main-types-anti-robot-mechanisms)








- Knowledge base

[What are the main types of anti-robot mechanisms?](https://changedetection.io/tutorial/what-are-main-types-anti-robot-mechanisms)

20 May, 2024

You may have read a lot about some tricks to defeat scraping such as changing your scraping browser's "User Agent" settings, however that's only the start of the story.

- [![Synology NAS Discord changedetection.io](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-01/synology-discord-changedetectionio.png?itok=XKgktvQ0)](https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord)








- How-To

[Synology NAS - How to get alerts on new software updates via Discord!](https://changedetection.io/tutorial/synology-nas-how-get-alerts-new-software-updates-discord)

17 January, 2024

In this quick tutorial I'll show you how easy it is in to monitor a website for new software version releases and connect Discord for push notifications.

- [![Alert if HTML element exists or not](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-01/image_67.png?itok=hvmoSEwT)](https://changedetection.io/tutorial/change-detection-if-html-element-exists-or-not)








- How-To

[Change detection if a HTML element exists or not](https://changedetection.io/tutorial/change-detection-if-html-element-exists-or-not)

8 January, 2024

Sometimes you are not quite interested in content change notifications for the entire web page, and maybe not even content change notification for a element on the website - _**actually you want to know if an element exists at all or not.**_

- [![Monitor a site for new content and get notifications](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-01/new-content-notification.png?itok=6V0-7zKX)](https://changedetection.io/tutorial/how-monitor-website-new-content)








- How-To

[How to monitor a website for NEW content](https://changedetection.io/tutorial/how-monitor-website-new-content)

5 January, 2024

How to monitor a site for new content ? How can you configure changedetection.io to only show NEW content from a site and send you a notification? What if you only want to know about new and unique content?

- [![Gears showing that new links can be added automatically](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2024-01/gears.jpg?itok=lkxft_Jg)](https://changedetection.io/tutorial/automatically-adding-new-pages-watch-existing-results)








- How-To

[Automatically adding new pages to watch from existing results](https://changedetection.io/tutorial/automatically-adding-new-pages-watch-existing-results)

3 January, 2024

Think of the situation where you are watching your favourite ecommerce website, and you want to start automatically watching any NEW pages for changes.

- [![Extract data line chart from website example picture](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-12/changedet-line-chart-extract-data.png?itok=_Gr8i5c2)](https://changedetection.io/tutorial/extract-data-websites-and-draw-charts-how-gain-valuable-long-term-insights)








- How-To

[Scrape and Extract data from websites and draw charts - How to gain valuable long-term insights](https://changedetection.io/tutorial/extract-data-websites-and-draw-charts-how-gain-valuable-long-term-insights)

27 December, 2023

Visualising long-term insights can lead to a lot of interesting and valuable realisations.

The web is always changing, but how does that information look across a week? a month? a year?

- [![](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/default_images/temp.png?itok=0vsexsQ8)](https://changedetection.io/tutorial/source-code-monitor-how-get-alerts-changes-html-source-code)








- How-To

[Source code monitor - How to get alerts on changes to HTML source code](https://changedetection.io/tutorial/source-code-monitor-how-get-alerts-changes-html-source-code)

8 December, 2023

How to get alerts on changes to HTML source code? Sometimes you need to know when a very specific part of the HTML changes, for example you're watching a competitor and want to know when they change their shops metatags

- [![Best Buy  - "Coming Soon" how to get notifications and alerts](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-12/unavailable-sold-out.png?itok=IsQGVSxf)](https://changedetection.io/tutorial/bestbuy-get-coming-soon-product-stock-notifications-using-restock-detection)








- How-To

[BestBuy - Get "Coming Soon" product in stock notifications using the restock detection!](https://changedetection.io/tutorial/bestbuy-get-coming-soon-product-stock-notifications-using-restock-detection)

29 November, 2023

Best Buy excels in providing a comprehensive array of electronics and tech gadgets, offering a diverse range of products both in-store and online. Their stores provide an immersive experience, often staffed with knowledgeable experts who assist customers in making informed decisions.

It's all perfect except for one thing - "COMING SOON" on a product that you really want!

- [![Detecting restock / back in stock](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-11/restock.png?itok=w8RnSkvV)](https://changedetection.io/tutorial/how-get-product-re-stock-or-back-stock-alerts-and-notifications)








- How-To

[How to get product re-stock or "back in stock" alerts and notifications ?](https://changedetection.io/tutorial/how-get-product-re-stock-or-back-stock-alerts-and-notifications)

28 November, 2023

Is that product or event ticket sold out? unavailable?
Need to get notified when something is back in stock?

There is a solution - You can simply add your website monitor and select the "Re-stock detection for single product pages" option.

Read on!

---

### Tutorials | changedetection.io
Original URL: https://changedetection.io/tutorials?page=2

[Skip to main content](https://changedetection.io/tutorials?page=2#main-content)

# Changedetection.io Tutorials

Want to know more? Need some more inspiration? How do you get the most from changedetection.io ? Read on!

- [![Excel list of websites to monitor](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-11/Import-List-Of-websites-to-monitor-from-excel.png?itok=u7kQR1z9)](https://changedetection.io/tutorial/how-import-your-website-change-detection-lists-excel)








- How-To

[How to import your website change detection lists from Excel?](https://changedetection.io/tutorial/how-import-your-website-change-detection-lists-excel)

1 November, 2023

In this quick article I'll show you how to import your website URL lists from Microsoft Excel into changedetection.io

This can be super handy when you've managed to filter down your lists of websites to something really specific that you're interested in, or another way to manage your list of websites to check for changes.

It's super easy with changedetection.io.

- [![How to detect changes in an RSS feed and get push notifications?](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-10/Screenshot_2023-10-17_14-11-04.png?itok=v748XCo3)](https://changedetection.io/tutorial/how-get-push-notifications-rss-feed-detect-changes-rss-feed)








- How-To

[How to get push notifications from a RSS Feed ? Detect changes in the RSS Feed!](https://changedetection.io/tutorial/how-get-push-notifications-rss-feed-detect-changes-rss-feed)

17 October, 2023

Do you love RSS? But wish you could get notifications when certain keywords appear on your favourite RSS streams sent as a push notification to Discord, Telegram, Email, Slack and more? Read on!

- [![hetzner](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-09/hetzner.jpg?itok=SqgdkGOV)](https://changedetection.io/tutorial/awesome-use-case-4510-how-get-notified-when-hetzner-servers-and-products-are-available)








- How-To
- Use-case

[Awesome use-case #4,510: How to get notified when Hetzner servers and products are available](https://changedetection.io/tutorial/awesome-use-case-4510-how-get-notified-when-hetzner-servers-and-products-are-available)

24 September, 2023

But the real heartbreak is when you are hunting for your dream Hetzner Dedicated Server only to find out that it's not available in your preferred architecture and that there's no good way to get alerts or notifications when Hetzner effectively "restock" that type of server.

Changedetection.io to the rescue - get notifications when Hetzner restock their server offers!

- [![Using website change detection to monitor for changes in regulations.](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/regs.jpeg?itok=7qN5lKiQ)](https://changedetection.io/tutorial/got-regtech-using-website-change-detection-monitor-changes-regulations)








- How-To
- RegTech

[Got RegTech? Using website change detection to monitor for changes in regulations.](https://changedetection.io/tutorial/got-regtech-using-website-change-detection-monitor-changes-regulations)

21 August, 2023

Website change detection is a crucial component of a regulatory intelligence solution, helping it stay ahead of regulatory changes and inform your clients before they become aware of these changes. Here's how website change detection can specifically assist in achieving this goal.

- [![Login box](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/login-box.jpg?itok=VQ8duH9Z)](https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy)








- Browser Steps
- How-To
- Use-case

[Website content change detection from behind logins - easy](https://changedetection.io/tutorial/website-content-change-detection-behind-logins-easy)

13 August, 2023

Another great feature of changedetection.io is that you can interact with websites to compare their content.

Often you need to enter in some search query or need to access a page that's only available from behind a login/password form.

- [![BrightData](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/bright.png?itok=kxk1sDeO)](https://changedetection.io/tutorial/how-bright-data-proxies-and-changedetectionio)








- How-To
- Proxies

[How to - Bright Data Proxies and changedetection.io](https://changedetection.io/tutorial/how-bright-data-proxies-and-changedetectionio)

2 August, 2023

Using proxies is beneficial for accessing web pages from different countries and bypassing blocking rules for several reasons, read on to find out the advantage of using Bright Data Proxies with changedetection.io!

- [![realestate vacancies](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/image_9.png?itok=HzVUwhxk)](https://changedetection.io/tutorial/four-tips-help-you-your-apartment-or-house-search)








- How-To

[Four tips to help you in your apartment or house search.](https://changedetection.io/tutorial/four-tips-help-you-your-apartment-or-house-search)

1 August, 2023

Monitoring real estate pages and receiving notifications on changes to website content is highly advantageous when searching for an apartment. By doing so, you can be among the first to discover newly listed properties, price reductions, or updates on available apartments.

- [![keepass screenshot](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/main_big.png?itok=lczIgYVC)](https://changedetection.io/tutorial/how-get-alerts-new-keepass-releases)








- How-To
- Notifications

[How to get alerts on new KeePass releases](https://changedetection.io/tutorial/how-get-alerts-new-keepass-releases)

1 July, 2023

KeePass is vital for online security as it securely stores passwords. Getting update notifications is crucial to stay protected from potential vulnerabilities and cyber threats.

- [![PR Newswire cision logo](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/prn_cision_logo_desktop.png?itok=ivh2LMd6)](https://changedetection.io/tutorial/how-get-alerts-when-certain-keywords-appear-pr-newswire)








- How-To

[How to get alerts when certain keywords appear on PR Newswire?](https://changedetection.io/tutorial/how-get-alerts-when-certain-keywords-appear-pr-newswire)

13 June, 2023

PR Newswire is a news distribution service. By monitoring keywords on PR Newswire, you gain insights, track brand reputation, discover media opportunities, make informed investments, and identify crisis risks.

- [![Decathlon shopping - decathlon price tracker](https://changedetection.io/sites/changedetection.io/files/styles/max_325x325/public/2023-08/dec.jpg?itok=BFW3bYDc)](https://changedetection.io/tutorial/decathlon-sport-how-monitor-prices)








- How-To

[Decathlon Sport - How to monitor prices - decathlon price tracker](https://changedetection.io/tutorial/decathlon-sport-how-monitor-prices)

8 May, 2023

Decathlon is a global sporting goods retailer offering a wide range of products. Monitoring their webpage for low prices is beneficial as it helps you save money by identifying discounts and special offers. By staying vigilant, you can seize cost-saving opportunities and make informed purchases, maximizing the value of your shopping experience.

Keep an eye on your favourite item!

---

### Page not found | changedetection.io
Original URL: https://changedetection.io/Ubiquiti%20restock%20alert

[Skip to main content](https://changedetection.io/Ubiquiti%20restock%20alert#main-content)

# 404

But don't give up hope, keep exploring :)

Never stop monitoring the web for changes.

---


## Release Notes

### How to get alerts on new KeePass releases | changedetection.io
Original URL: https://changedetection.io/tutorial/how-get-alerts-new-keepass-releases

[Skip to main content](https://changedetection.io/tutorial/how-get-alerts-new-keepass-releases#main-content)

# How to get alerts on new KeePass releases

[![Profile picture for user Stephen](https://changedetection.io/sites/changedetection.io/files/styles/thumbnail/public/pictures/2023-08/stephen.png?itok=P4ZqxWgD)](https://changedetection.io/tech-writer/stephen)

By Stephen, Updated 1 July, 2023



Topic

[How-To](https://changedetection.io/topic/how)

[Notifications](https://changedetection.io/topic/notifications)

KeePass is vital for online security as it securely stores passwords. Getting update notifications is crucial to stay protected from potential vulnerabilities and cyber threats.

In this short article I'll show you how to setup changedetection.io to send you an alert as soon as a new (and often important) KeePass release is made, whilst minimizing false alerts.

#### Step 1, Add the URL

Here we add the URL of [_https://keepass.info/download.html_](https://keepass.info/download.html) simply add the URL to the top part of the page and simply click **Watch**

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image.png)

#### Step 2, Select the part of the page that contains the text we are interested in

For example, we don't want false alerts when the header, footer or menu changes, so we use the **Visual Selector** to choose the content we are only interested in. The selected area will show with a **red border** and the rest will be greyed-out to make it easier to see what you selected.

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_0.png)

#### Step 3, Setup your favourite notification

In the last step, click on the **Notifications** tab, click **'Add email' ,** here you can enter in the preferred email address to send notifications to.

changedetection.io (for subscribers) will automatically choose our mail server to send your emails to, so you don't need to setup anything further.

You can also choose to attach the screenshot to the email by clicking **Attach screenshot to notification**

![](https://changedetection.io/sites/changedetection.io/files/inline-images/image_1.png)

Don't forget that you can also send notifications via Discord, Telegram and over 90 other different methods

Then simply click **Save**

- [Continue with\\
    and](https://changedetection.io/checkout)

$8.99/Month Easy Subscription


Cancel anytime, 5,000 URL watches included.

---

