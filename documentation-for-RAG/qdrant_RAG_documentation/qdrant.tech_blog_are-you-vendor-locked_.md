---
url: "https://qdrant.tech/blog/are-you-vendor-locked/"
title: "Are You Vendor Locked? - Qdrant"
---

0

# Are You Vendor Locked?

David Myriel

·

May 05, 2024

![Are You Vendor Locked?](https://qdrant.tech/blog/are-you-vendor-locked/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fare-you-vendor-locked%2F&text=Are%20You%20Vendor%20Locked? "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fare-you-vendor-locked%2F "LinkedIn")

We all are.

> _“There is no use fighting it. Pick a vendor and go all in. Everything else is a mirage.”_
> The last words of a seasoned IT professional

As long as we are using any product, our solution’s infrastructure will depend on its vendors. Many say that building custom infrastructure will hurt velocity. **Is this true in the age of AI?**

It depends on where your company is at. Most startups don’t survive more than five years, so putting too much effort into infrastructure is not the best use of their resources. You first need to survive and demonstrate product viability.

**Sometimes you may pick the right vendors and still fail.**

![gpu-costs](https://qdrant.tech/blog/are-you-vendor-locked/gpu-costs.png)

We have all started to see the results of the AI hardware bottleneck. Running LLMs is expensive and smaller operations might fold to high costs. How will this affect large enterprises?

> If you are an established corporation, being dependent on a specific supplier can make or break a solid business case. For large-scale GenAI solutions, costs are essential to maintenance and dictate the long-term viability of such projects. In the short run, enterprises may afford high costs, but when the prices drop - then it’s time to adjust.

Unfortunately, the long run goal of scalability and flexibility may be countered by vendor lock-in. Shifting operations from one host to another requires expertise and compatibility adjustments. Should businesses become dependent on a single cloud service provider, they open themselves to risks ranging from soaring costs to stifled innovation.

**Finding the best vendor is key; but it’s crucial to stay mobile.**

## [Anchor](https://qdrant.tech/blog/are-you-vendor-locked/\#hardware-is-the-new-vendor-lock)**Hardware is the New Vendor Lock**

> _“We’re so short on GPUs, the less people that use the tool \[ChatGPT\], the better.”_
> OpenAI CEO, Sam Altman

When GPU hosting becomes too expensive, large and exciting Gen AI projects lose their luster. If moving clouds becomes too costly or difficulty to implement - you are vendor-locked. This used to be common with software. Now, hardware is the new dependency.

_Enterprises have many reasons to stay provider agnostic - but cost is the main one._

[Appenzeller, Bornstein & Casado from Andreessen Horowitz](https://a16z.com/navigating-the-high-cost-of-ai-compute/) point to growing costs of AI compute. It is still a vendor’s market for A100 hourly GPUs, largely due to supply constraints. Furthermore, the price differences between AWS, GCP and Azure are dynamic enough to justify extensive cost-benefit analysis from prospective customers.

![gpu-costs-a16z](https://qdrant.tech/blog/are-you-vendor-locked/gpu-costs-a16z.png)

_Source: Andreessen Horowitz_

Sure, your competitors can brag about all the features they can access - but are they willing to admit how much their company has lost to convenience and increasing costs?

As an enterprise customer, one shouldn’t expect a vendor to stay consistent in this market.

## [Anchor](https://qdrant.tech/blog/are-you-vendor-locked/\#how-does-this-affect-qdrant) How Does This Affect Qdrant?

As an open source vector database, Qdrant is completely risk-free. Furthermore, cost savings is one of the many reasons companies use it to augment the LLM. You won’t need to burn through GPU cash for training or inference. A basic instance with a CPU and RAM can easily manage indexing and retrieval.

> _However, we find that many of our customers want to host Qdrant in the same place as the rest of their infrastructure, such as the LLM or other data engineering infra. This can be for practical reasons, due to corporate security policies, or even global political reasons._

One day, they might find this infrastructure too costly. Although vector search will remain cheap, their training, inference and embedding costs will grow. Then, they will want to switch vendors.

What could interfere with the switch? Compatibility? Technologies? Lack of expertise?

In terms of features, cloud service standardization is difficult due to varying features between cloud providers. This leads to custom solutions and vendor lock-in, hindering migration and cost reduction efforts, [as seen with Snapchat and Twitter](https://www.businessinsider.com/snap-google-cloud-aws-reducing-costs-2023-2).

## [Anchor](https://qdrant.tech/blog/are-you-vendor-locked/\#fear-uncertainty-and-doubt)**Fear, Uncertainty and Doubt**

You spend months setting up the infrastructure, but your competitor goes all in with a cheaper alternative and has a competing product out in one month? Does avoiding the lock-in matter if your company will be out of business while you try to setup a fully agnostic platform?

**Problem:** If you’re not locked into a vendor, you’re locked into managing a much larger team of engineers. The build vs buy tradeoff is real and it comes with its own set of risks and costs.

**Acknowledgement:** Any organization that processes vast amounts of data with AI needs custom infrastructure and dedicated resources, no matter the industry. Having to work with expensive services such as A100 GPUs justifies the existence of in-house DevOps crew. Any enterprise that scales up needs to employ vigilant operatives if it wants to manage costs.

> There is no need for **Fear, Uncertainty and Doubt**. Vendor lock is not a futile cause - so let’s dispel the sentiment that all vendors are adversaries. You just need to work with a company that is willing to accommodate flexible use of products.

**The Solution is Kubernetes:** Decoupling your infrastructure from a specific cloud host is currently the best way of staying risk-free. Any component of your solution that runs on Kubernetes can integrate seamlessly with other compatible infrastructure.

This is how you stay dynamic and move vendors whenever it suits you best.

## [Anchor](https://qdrant.tech/blog/are-you-vendor-locked/\#what-about-hybrid-cloud)**What About Hybrid Cloud?**

The key to freedom is to building your applications and infrastructure to run on any cloud. By leveraging containerization and service abstraction using Kubernetes or Docker, software vendors can exercise good faith in helping their customers transition to other cloud providers.

We designed the architecture of Qdrant Hybrid Cloud to meet the evolving needs of businesses seeking unparalleled flexibility, control, and privacy.

This technology integrates Kubernetes clusters from any setting - cloud, on-premises, or edge - into a unified, enterprise-grade managed service.

#### [Anchor](https://qdrant.tech/blog/are-you-vendor-locked/\#take-a-look-its-completely-yours-well-help-you-manage-it) Take a look. It’s completely yours. We’ll help you manage it.

Deploy a Production-Ready Vector Database in 5 Minutes With Qdrant Hybrid Cloud - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Deploy a Production-Ready Vector Database in 5 Minutes With Qdrant Hybrid Cloud](https://www.youtube.com/watch?v=BF02jULGCfo)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=BF02jULGCfo&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 6:44
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=BF02jULGCfo "Watch on YouTube")

[Qdrant Hybrid Cloud](https://qdrant.tech/hybrid-cloud/) marks a significant advancement in vector databases, offering the most flexible way to implement vector search.

You can test out Qdrant Hybrid Cloud today. Sign up or log into your [Qdrant Cloud account](https://cloud.qdrant.io/login?ajs_anonymous_id=6c04f939-d5f3-40e3-ab59-69bf047293ef) and get started in the **Hybrid Cloud** section.

Also, to learn more about Qdrant Hybrid Cloud read our [Official Release Blog](https://qdrant.tech/blog/hybrid-cloud/) or our [Qdrant Hybrid Cloud website](https://qdrant.tech/hybrid-cloud/). For additional technical insights, please read our [documentation](https://qdrant.tech/documentation/hybrid-cloud/).

#### [Anchor](https://qdrant.tech/blog/are-you-vendor-locked/\#try-it-out) Try it out!

[![hybrid-cloud-cta.png](https://qdrant.tech/blog/are-you-vendor-locked/hybrid-cloud-cta.png)](https://qdrant.to/cloud)

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=6c04f939-d5f3-40e3-ab59-69bf047293ef)

![](https://qdrant.tech/img/rocket.svg)

Up!

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=33640ba3-38c0-4360-9997-313bc65ad294&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b50162dd-6526-41d2-a46b-6e4fba872be9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fare-you-vendor-locked%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=33640ba3-38c0-4360-9997-313bc65ad294&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b50162dd-6526-41d2-a46b-6e4fba872be9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fare-you-vendor-locked%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

![Sifted-Announcement-1B](https://139603372.fs1.hubspotusercontent-eu1.net/hub/139603372/hubfs/Sifted-Announcement-1B.jpg?width=567&height=296&name=Sifted-Announcement-1B.jpg)

## Enjoying this blog?

Subscribe to our monthly newsletter to receive the latest resources and updates.

Email\*

By submitting, you agree to subscribe to Qdrant's updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://qdrant.tech/legal/privacy-policy/?webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fare-you-vendor-locked%2F&portalId=139603372&pageTitle=Are+You+Vendor+Locked%3F+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=9306668ffbfbc35da6518154fefb3f0f&hssc=265983056.1.1748574535183&hstc=265983056.9306668ffbfbc35da6518154fefb3f0f.1748574535183.1748574535183.1748574535183.1&hsfp=3707738794).

Submit

## By submitting, you agree to subscribe to Qdrant’s updates. You can withdraw your consent anytime. More details are in the [Privacy Policy](https://cta-eu1.hubspot.com/web-interactives/public/v1/track/click?encryptedPayload=AVxigLK8Tz%2FEDKnDiKMvegOsr1Pu5ZW3Y%2BUmdM4RyrsMZ01kzRaG4iGViyAmaI7I0a6DlEJufA4usCQ%2BxO6TSO%2Bk2FVeACGpI5rvmiWNP%2BBHMuHXSj4KbzGIkv3FQ7k1MC284J7R&portalId=139603372&webInteractiveId=620271994043&webInteractiveContentId=237919561943&containerType=MODAL&pageUrl=https%3A%2F%2Fqdrant.tech%2Fblog%2Fare-you-vendor-locked%2F&pageTitle=Are+You+Vendor+Locked%3F+-+Qdrant&referrer=&userAgent=Mozilla%2F5.0+%28X11%3B+Linux+x86_64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F137.0.0.0+Safari%2F537.36&hutk=9306668ffbfbc35da6518154fefb3f0f&hssc=265983056.1.1748574535183&hstc=265983056.9306668ffbfbc35da6518154fefb3f0f.1748574535183.1748574535183.1748574535183.1&hsfp=3707738794).