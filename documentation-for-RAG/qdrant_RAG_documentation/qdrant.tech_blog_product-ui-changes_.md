---
url: "https://qdrant.tech/blog/product-ui-changes/"
title: "Exploring Qdrant Cloud Just Got Easier - Qdrant"
---

0

# Exploring Qdrant Cloud Just Got Easier

Qdrant

·

May 06, 2025

![Exploring Qdrant Cloud Just Got Easier](https://qdrant.tech/blog/product-ui-changes/new-ui-hero-final.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fproduct-ui-changes%2F&text=Exploring%20Qdrant%20Cloud%20Just%20Got%20Easier "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fproduct-ui-changes%2F "LinkedIn")

# [Anchor](https://qdrant.tech/blog/product-ui-changes/\#exploring-qdrant-cloud-just-got-easier) Exploring Qdrant Cloud just got easier

We always aim to simplify our product for developers, platform teams, and enterprises.

Here’s a quick overview of recent improvements designed to simplify your journey from login, creating your first cluster, prototyping, and going to production.

Exploring Qdrant Cloud just got easier: recent UI improvements - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Exploring Qdrant Cloud just got easier: recent UI improvements](https://www.youtube.com/watch?v=J75pNicPEo8)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Why am I seeing this?](https://support.google.com/youtube/answer/9004474?hl=en)

[Watch on](https://www.youtube.com/watch?v=J75pNicPEo8&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 3:06
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=J75pNicPEo8 "Watch on YouTube")

## [Anchor](https://qdrant.tech/blog/product-ui-changes/\#simplified-login) Simplified Login

We’ve reduced the steps to create and access your account, and also simplified navigation between login and registration.

![JPG of log in page](https://qdrant.tech/blog/product-ui-changes/log-in-page.jpg)

Upon log in, of course you continue to have the option to toggle between dark and light mode, or choose your system default.

![GIF of toggling between dark and light mode](https://qdrant.tech/blog/product-ui-changes/gif-dark-light-mode.gif)

Now for the biggest improvements.

## [Anchor](https://qdrant.tech/blog/product-ui-changes/\#effortless-cluster-creation) Effortless Cluster Creation

When you log in for your first time, it’s incredibly easy to create your first cluster (completely free, no need to share any payment details).

Simply name your first cluster, choose your region, and click “Create.” Your cluster will start spinning up immediately!

The 1 GB free gives you enough storage for approximately 1 million vectors at 768 dimensions and is great for prototyping and learning.

![GIF of the first cluster being created](https://qdrant.tech/blog/product-ui-changes/my-first-cluster.gif)

Don’t forget to create a collection, add vectors, then run your first search.

## [Anchor](https://qdrant.tech/blog/product-ui-changes/\#cluster-overview) Cluster Overview

Now this is probably where you will spend most of your time when building with Qdrant.

When looking at the overview of your cluster, we’ve added new tabs with an improved menu structure.

![Image of cluster overview](https://qdrant.tech/blog/product-ui-changes/my-first-cluster-overview.jpg)

- **Overview**: This has everything you need at a glance, including a visual of your node, disk, RAM, CPU usage so you can see if you are approaching any limits. It’s also easier now to scale your cluster. Once scaled to a paid tier via credit card or marketplace, you can access backup and disaster recovery, a 99.5% uptime SLA, horizontal and vertical scaling, monitoring and log management, and more.
- **API** **keys**: Manage access to your database cluster
- **Metrics**: a visualization of your resources, RAM, CPU, disk and requests over different timeframes
- **Logs**: get a real-time window into what’s happening inside cluste for transparency, diagnostics, and control (especially important during debugging, performance tuning, or infrastructure troubleshooting!)
- **Backups:** View snapshots of your vector data and metadata that can be used to restore your collections in case of data loss, migration, or rollbacks (not available on free clusters)
- **Configuration**: Check your collection defaults and add advanced optimizations (after reading Docs of course)
  - For example, we advise against setting up a ton of different collections. Instead segment with [payloads](https://qdrant.tech/documentation/concepts/payload/).

When viewing the details of your clusters, you can now view the Cluster UI Dashboard regardless of where you are, and also have easier access to tutorials and resources.

We also are making it more seamless to update your cluster to the latest version as well as see GitHub release notes.

![JPG of changing version](https://qdrant.tech/blog/product-ui-changes/change-version.png)

## [Anchor](https://qdrant.tech/blog/product-ui-changes/\#get-started-overview) Get Started Overview

Next we’ve done a major overhaul to the “Get Started” page. Our goal is to make it as easy as possible for you to find the resources you need, whether it’s guides, sample data, or tutorials.

![Image of Get Started webpage](https://qdrant.tech/blog/product-ui-changes/get-started-overview.jpg)

**Explore Your Data or Start with Samples**

You’ll see immediately pertinent information to help you get the most out of Qdrant quickly, including the [Cloud Quickstart guide](https://qdrant.tech/documentation/quickstart-cloud/), and resources to help you get your data into Qdrant, or use sample data.

Learn about the different ways to connect to your cluster, use the Qdrant API, try out sample data, and our personal favorite, use the Qdrant Cluster UI to view your collection data and access tutorials.

**Build World Class Applications**

If you are ready to build an app, but looking for ideas or the best place to start, we have our top three tutorials highlighted for you.

Learn how to:

- [Build a hybrid search service](https://qdrant.tech/documentation/beginner-tutorials/hybrid-search-fastembed/) with [FastEmbed](https://github.com/qdrant/fastembed)
- [Build a RAG app with DeepSeek](https://qdrant.tech/documentation/rag-deepseek/) for semantic query enrichment
- [Connect Qdrant with your data stack](https://qdrant.tech/documentation/data-management/) for seamless workflows

**Pick a Deployment Model**

If you are looking for freedom of choice, [enterprise-readiness](https://qdrant.tech/blog/enterprise-vector-search/), and scalability without [vendor lock-in](https://qdrant.tech/blog/are-you-vendor-locked/), look no further. Here you can learn about the different deployment options we offer.

Whether you want a fully managed experience, complete infrastructure control, or something in between, Qdrant delivers.

**Support, Community, and Docs**

We have robust documentation, as well as a global [community](https://discord.com/invite/qdrant) of users that share projects, advice, and help each other build. If you run into technical issues, our support team is happy to help troubleshoot. Here you can find what you need if you run into roadblocks when building.

## [Anchor](https://qdrant.tech/blog/product-ui-changes/\#see-for-yourself) See for Yourself

If you haven’t tried Qdrant Cloud yet, now is the time to get started.

[**Try now!**](https://cloud.qdrant.io/signup?ajs_anonymous_id=f41d4c5e-e4c3-40dd-acdb-d2523419aba9)

Want to share feedback? Email us at [community@qdrant.com](mailto:community@qdrant.com)

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=f41d4c5e-e4c3-40dd-acdb-d2523419aba9)

![](https://qdrant.tech/img/rocket.svg)

Up!

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=132a787e-7815-435f-b6aa-1624949214e1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9325acfe-aeed-4220-bf39-97dc0543b626&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fproduct-ui-changes%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=132a787e-7815-435f-b6aa-1624949214e1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9325acfe-aeed-4220-bf39-97dc0543b626&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fproduct-ui-changes%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)

## Privacy Preference Center

Cookies used on the site are categorized, and below, you can read about each category and allow or deny some or all of them. When categories that have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser.
Additionally, you can see a list of cookies assigned to each category and detailed information in the cookie declaration.


[More information](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)

Allow All

### Manage Consent Preferences

#### Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Reject AllConfirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

![Sifted-Announcement-1B](https://139603372.fs1.hubspotusercontent-eu1.net/hub/139603372/hubfs/Sifted-Announcement-1B.jpg?width=567&height=296&name=Sifted-Announcement-1B.jpg)

## Enjoying this blog?

Subscribe to our monthly newsletter to receive the latest resources and updates.

Email\*

By submitting, you agree to subscribe to Qdrant's updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://qdrant.tech/legal/privacy-policy/?webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fproduct-ui-changes%2F&portalId=139603372&pageTitle=Exploring+Qdrant+Cloud+Just+Got+Easier+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=9fc887e1417d81ea8d38de6cdf75b7d8&hssc=265983056.1.1748573804789&hstc=265983056.9fc887e1417d81ea8d38de6cdf75b7d8.1748573804789.1748573804789.1748573804789.1&hsfp=3707738794).

Submit

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372&webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fproduct-ui-changes%2F&pageTitle=Exploring+Qdrant+Cloud+Just+Got+Easier+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=9fc887e1417d81ea8d38de6cdf75b7d8&hssc=265983056.1.1748573804789&hstc=265983056.9fc887e1417d81ea8d38de6cdf75b7d8.1748573804789.1748573804789.1748573804789.1&hsfp=3707738794).