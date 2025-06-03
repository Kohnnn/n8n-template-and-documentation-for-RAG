---
url: "https://qdrant.tech/documentation/faq/database-optimization/"
title: "Database Optimization - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Faq](https://qdrant.tech/documentation/faq/)
- Database Optimization

# [Anchor](https://qdrant.tech/documentation/faq/database-optimization/\#frequently-asked-questions-database-optimization) Frequently Asked Questions: Database Optimization

### [Anchor](https://qdrant.tech/documentation/faq/database-optimization/\#how-do-i-reduce-memory-usage) How do I reduce memory usage?

The primary source of memory usage is vector data. There are several ways to address that:

- Configure [Quantization](https://qdrant.tech/documentation/guides/quantization/) to reduce the memory usage of vectors.
- Configure on-disk vector storage

The choice of the approach depends on your requirements.
Read more about [configuring the optimal](https://qdrant.tech/documentation/tutorials/optimize/) use of Qdrant.

### [Anchor](https://qdrant.tech/documentation/faq/database-optimization/\#how-do-you-choose-the-machine-configuration) How do you choose the machine configuration?

There are two main scenarios of Qdrant usage in terms of resource consumption:

- **Performance-optimized** – when you need to serve vector search as fast (many) as possible. In this case, you need to have as much vector data in RAM as possible. Use our [calculator](https://cloud.qdrant.io/calculator) to estimate the required RAM.
- **Storage-optimized** – when you need to store many vectors and minimize costs by compromising some search speed. In this case, pay attention to the disk speed instead. More about it in the article about [Memory Consumption](https://qdrant.tech/articles/memory-consumption/).

### [Anchor](https://qdrant.tech/documentation/faq/database-optimization/\#i-configured-on-disk-vector-storage-but-memory-usage-is-still-high-why) I configured on-disk vector storage, but memory usage is still high. Why?

Firstly, memory usage metrics as reported by `top` or `htop` may be misleading. They are not showing the minimal amount of memory required to run the service.
If the RSS memory usage is 10 GB, it doesn’t mean that it won’t work on a machine with 8 GB of RAM.

Qdrant uses many techniques to reduce search latency, including caching disk data in RAM and preloading data from disk to RAM.
As a result, the Qdrant process might use more memory than the minimum required to run the service.

> Unused RAM is wasted RAM

If you want to limit the memory usage of the service, we recommend using [limits in Docker](https://docs.docker.com/config/containers/resource_constraints/#memory) or Kubernetes.

### [Anchor](https://qdrant.tech/documentation/faq/database-optimization/\#my-requests-are-very-slow-or-time-out-what-should-i-do) My requests are very slow or time out. What should I do?

There are several possible reasons for that:

- **Using filters without payload index** – If you’re performing a search with a filter but you don’t have a payload index, Qdrant will have to load whole payload data from disk to check the filtering condition. Ensure you have adequately configured [payload indexes](https://qdrant.tech/documentation/concepts/indexing/#payload-index).
- **Usage of on-disk vector storage with slow disks** – If you’re using on-disk vector storage, ensure you have fast enough disks. We recommend using local SSDs with at least 50k IOPS. Read more about the influence of the disk speed on the search latency in the article about [Memory Consumption](https://qdrant.tech/articles/memory-consumption/).
- **Large limit or non-optimal query parameters** – A large limit or offset might lead to significant performance degradation. Please pay close attention to the query/collection parameters that significantly diverge from the defaults. They might be the reason for the performance issues.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/faq/database-optimization.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/faq/database-optimization.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574007431&cv=11&fst=1748574007431&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffaq%2Fdatabase-optimization%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Database%20Optimization%20-%20Qdrant&npa=0&pscdl=noapi&auid=1753911041.1748574007&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574007383&cv=11&fst=1748574007383&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffaq%2Fdatabase-optimization%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Database%20Optimization%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1753911041.1748574007&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=827631f1-f93c-4a61-99e1-bcac40eccc85&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3dc421ef-cf5b-42e0-867e-2fbfd0ffa28c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffaq%2Fdatabase-optimization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=827631f1-f93c-4a61-99e1-bcac40eccc85&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3dc421ef-cf5b-42e0-867e-2fbfd0ffa28c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffaq%2Fdatabase-optimization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)