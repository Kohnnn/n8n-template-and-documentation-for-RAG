---
url: "https://qdrant.tech/articles/qdrant-0-11-release/"
title: "Introducing Qdrant 0.11 - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Introducing Qdrant 0.11

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# Introducing Qdrant 0.11

Kacper Łukawski

·

October 26, 2022

![Introducing Qdrant 0.11](https://qdrant.tech/articles_data/qdrant-0-11-release/preview/title.jpg)

We are excited to [announce the release of Qdrant v0.11](https://github.com/qdrant/qdrant/releases/tag/v0.11.0),
which introduces a number of new features and improvements.

## [Anchor](https://qdrant.tech/articles/qdrant-0-11-release/\#replication) Replication

One of the key features in this release is replication support, which allows Qdrant to provide a high availability
setup with distributed deployment out of the box. This, combined with sharding, enables you to horizontally scale
both the size of your collections and the throughput of your cluster. This means that you can use Qdrant to handle
large amounts of data without sacrificing performance or reliability.

## [Anchor](https://qdrant.tech/articles/qdrant-0-11-release/\#administration-api) Administration API

Another new feature is the administration API, which allows you to disable write operations to the service. This is
useful in situations where search availability is more critical than updates, and can help prevent issues like memory
usage watermarks from affecting your searches.

## [Anchor](https://qdrant.tech/articles/qdrant-0-11-release/\#exact-search) Exact search

We have also added the ability to report indexed payload points in the info API, which allows you to verify that
payload values were properly formatted for indexing. In addition, we have introduced a new `exact` search parameter
that allows you to force exact searches of vectors, even if an ANN index is built. This can be useful for validating
the accuracy of your HNSW configuration.

## [Anchor](https://qdrant.tech/articles/qdrant-0-11-release/\#backward-compatibility) Backward compatibility

This release is backward compatible with v0.10.5 storage in single node deployment, but unfortunately, distributed
deployment is not compatible with previous versions due to the large number of changes required for the replica set
implementation. However, clients are tested for backward compatibility with the v0.10.x service.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-0-11-release.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-0-11-release.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574337702&cv=11&fst=1748574337702&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-0-11-release%2F&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Qdrant%200.11%20-%20Qdrant&npa=0&pscdl=noapi&auid=1530381977.1748574338&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574337668&cv=11&fst=1748574337668&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-0-11-release%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Qdrant%200.11%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1530381977.1748574338&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0dc6031b-4434-4f92-8af6-9a383e49cedb&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8b3fbccf-bde2-4812-b002-d1320494e341&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-0-11-release%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0dc6031b-4434-4f92-8af6-9a383e49cedb&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=8b3fbccf-bde2-4812-b002-d1320494e341&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-0-11-release%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)