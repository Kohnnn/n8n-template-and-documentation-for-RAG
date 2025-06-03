---
url: "https://qdrant.tech/articles/qdrant-0-10-release/"
title: "Qdrant 0.10 released - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Qdrant 0.10 released

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# Qdrant 0.10 released

Kacper Łukawski

·

September 19, 2022

![Qdrant 0.10 released](https://qdrant.tech/articles_data/qdrant-0-10-release/preview/title.jpg)

[Qdrant 0.10 is a new version](https://github.com/qdrant/qdrant/releases/tag/v0.10.0) that brings a lot of performance
improvements, but also some new features which were heavily requested by our users. Here is an overview of what has changed.

## [Anchor](https://qdrant.tech/articles/qdrant-0-10-release/\#storing-multiple-vectors-per-object) Storing multiple vectors per object

Previously, if you wanted to use semantic search with multiple vectors per object, you had to create separate collections
for each vector type. This was even if the vectors shared some other attributes in the payload. With Qdrant 0.10, you can
now store all of these vectors together in the same collection, which allows you to share a single copy of the payload.
This makes it easier to use semantic search with multiple vector types, and reduces the amount of work you need to do to
set up your collections.

## [Anchor](https://qdrant.tech/articles/qdrant-0-10-release/\#batch-vector-search) Batch vector search

Previously, you had to send multiple requests to the Qdrant API to perform multiple non-related tasks. However, this
can cause significant network overhead and slow down the process, especially if you have a poor connection speed.
Fortunately, the [new batch search feature](https://qdrant.tech/documentation/concepts/search/#batch-search-api) allows
you to avoid this issue. With just one API call, Qdrant will handle multiple search requests in the most efficient way
possible. This means that you can perform multiple tasks simultaneously without having to worry about network overhead
or slow performance.

## [Anchor](https://qdrant.tech/articles/qdrant-0-10-release/\#built-in-arm-support) Built-in ARM support

To make our application accessible to ARM users, we have compiled it specifically for that platform. If it is not
compiled for ARM, the device will have to emulate it, which can slow down performance. To ensure the best possible
experience for ARM users, we have created Docker images specifically for that platform. Keep in mind that using
a limited set of processor instructions may affect the performance of your vector search. Therefore, we have tested
both ARM and non-ARM architectures using similar setups to understand the potential impact on performance.

## [Anchor](https://qdrant.tech/articles/qdrant-0-10-release/\#full-text-filtering) Full-text filtering

Qdrant is a vector database that allows you to quickly search for the nearest neighbors. However, you may need to apply
additional filters on top of the semantic search. Up until version 0.10, Qdrant only supported keyword filters. With the
release of Qdrant 0.10, [you can now use full-text filters](https://qdrant.tech/documentation/concepts/filtering/#full-text-match)
as well. This new filter type can be used on its own or in combination with other filter types to provide even more
flexibility in your searches.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-0-10-release.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-0-10-release.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573648604&cv=11&fst=1748573648604&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-0-10-release%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%200.10%20released%20-%20Qdrant&npa=0&pscdl=noapi&auid=505907617.1748573649&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573648582&cv=11&fst=1748573648582&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308614&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-0-10-release%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%200.10%20released%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=505907617.1748573649&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=21ecd50d-62bd-4f48-941b-9c43be58d1e1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3ba0024a-7ce8-4044-95c1-0046bb4cdbea&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-0-10-release%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=21ecd50d-62bd-4f48-941b-9c43be58d1e1&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3ba0024a-7ce8-4044-95c1-0046bb4cdbea&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-0-10-release%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573649609&cv=11&fst=1748573649609&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-0-10-release%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%200.10%20released%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=505907617.1748573649&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)