---
url: "https://qdrant.tech/benchmarks/filtered-search-intro/"
title: "Filtered search benchmark - Qdrant"
---

# Filtered search benchmark

February 13, 2023

# [Anchor](https://qdrant.tech/benchmarks/filtered-search-intro/\#filtered-search-benchmark) Filtered search benchmark

Applying filters to search results brings a whole new level of complexity.
It is no longer enough to apply one algorithm to plain data. With filtering, it becomes a matter of the _cross-integration_ of the different indices.

To measure how well different search engines perform in this scenario, we have prepared a set of **Filtered ANN Benchmark Datasets** -
[https://github.com/qdrant/ann-filtering-benchmark-datasets](https://github.com/qdrant/ann-filtering-benchmark-datasets)

It is similar to the ones used in the [ann-benchmarks project](https://github.com/erikbern/ann-benchmarks/) but enriched with payload metadata and pre-generated filtering requests. It includes synthetic and real-world datasets with various filters, from keywords to geo-spatial queries.

### [Anchor](https://qdrant.tech/benchmarks/filtered-search-intro/\#why-filtering-is-not-trivial) Why filtering is not trivial?

Not many ANN algorithms are compatible with filtering.
HNSW is one of the few of them, but search engines approach its integration in different ways:

- Some use **post-filtering**, which applies filters after ANN search. It doesn’t scale well as it either loses results or requires many candidates on the first stage.
- Others use **pre-filtering**, which requires a binary mask of the whole dataset to be passed into the ANN algorithm. It is also not scalable, as the mask size grows linearly with the dataset size.

On top of it, there is also a problem with search accuracy.
It appears if too many vectors are filtered out, so the HNSW graph becomes disconnected.

Qdrant uses a different approach, not requiring pre- or post-filtering while addressing the accuracy problem.
Read more about the Qdrant approach in our [Filtrable HNSW](https://qdrant.tech/articles/filtrable-hnsw/) article.

Share this article

[x](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-intro%2F&text=Filtered%20search%20benchmark "x")[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-intro%2F "LinkedIn")

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574194288&cv=11&fst=1748574194288&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-intro%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Filtered%20search%20benchmark%20-%20Qdrant&npa=0&pscdl=noapi&auid=1104284924.1748574194&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574194265&cv=11&fst=1748574194265&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-intro%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Filtered%20search%20benchmark%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1104284924.1748574194&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1b60df3a-a9fe-4bc7-b535-3ee9fdd43592&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1188993f-571e-4671-b7a4-b4c16f8103cb&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-intro%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574194795&cv=11&fst=1748574194795&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-intro%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Filtered%20search%20benchmark%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1104284924.1748574194&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1b60df3a-a9fe-4bc7-b535-3ee9fdd43592&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1188993f-571e-4671-b7a4-b4c16f8103cb&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Ffiltered-search-intro%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)