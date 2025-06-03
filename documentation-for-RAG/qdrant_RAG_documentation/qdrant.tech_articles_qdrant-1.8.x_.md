---
url: "https://qdrant.tech/articles/qdrant-1.8.x/"
title: "Qdrant 1.8.0: Enhanced Search Capabilities for Better Results - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Qdrant 1.8.0: Enhanced Search Capabilities for Better Results

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# Qdrant 1.8.0: Enhanced Search Capabilities for Better Results

David Myriel, Mike Jang

·

March 06, 2024

![Qdrant 1.8.0: Enhanced Search Capabilities for Better Results](https://qdrant.tech/articles_data/qdrant-1.8.x/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#unlocking-next-level-search-exploring-qdrant-180s-advanced-search-capabilities) Unlocking Next-Level Search: Exploring Qdrant 1.8.0’s Advanced Search Capabilities

[Qdrant 1.8.0 is out!](https://github.com/qdrant/qdrant/releases/tag/v1.8.0).
This time around, we have focused on Qdrant’s internals. Our goal was to optimize performance so that your existing setup can run faster and save on compute. Here is what we’ve been up to:

- **Faster [sparse vectors](https://qdrant.tech/articles/sparse-vectors/):** [Hybrid search](https://qdrant.tech/articles/hybrid-search/) is up to 16x faster now!
- **CPU resource management:** You can allocate CPU threads for faster indexing.
- **Better indexing performance:** We optimized text [indexing](https://qdrant.tech/documentation/concepts/indexing/) on the backend.

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#faster-search-with-sparse-vectors) Faster search with sparse vectors

Search throughput is now up to 16 times faster for sparse vectors. If you are [using Qdrant for hybrid search](https://qdrant.tech/articles/sparse-vectors/), this means that you can now handle up to sixteen times as many queries. This improvement comes from extensive backend optimizations aimed at increasing efficiency and capacity.

What this means for your setup:

- **Query speed:** The time it takes to run a search query has been significantly reduced.
- **Search capacity:** Qdrant can now handle a much larger volume of search requests.
- **User experience:** Results will appear faster, leading to a smoother experience for the user.
- **Scalability:** You can easily accommodate rapidly growing users or an expanding dataset.

### [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#sparse-vectors-benchmark) Sparse vectors benchmark

Performance results are publicly available for you to test. Qdrant’s R&D developed a dedicated [open-source benchmarking tool](https://github.com/qdrant/sparse-vectors-benchmark) just to test sparse vector performance.

A real-life simulation of sparse vector queries was run against the [NeurIPS 2023 dataset](https://big-ann-benchmarks.com/neurips23.html). All tests were done on an 8 CPU machine on Azure.

Latency (y-axis) has dropped significantly for queries. You can see the before/after here:

![dropping latency](https://qdrant.tech/articles_data/qdrant-1.8.x/benchmark.png)**Figure 1:** Dropping latency in sparse vector search queries across versions 1.7-1.8.

The colors within both scatter plots show the frequency of results. The red dots show that the highest concentration is around 2200ms (before) and 135ms (after). This tells us that latency for sparse vector queries dropped by about a factor of 16. Therefore, the time it takes to retrieve an answer with Qdrant is that much shorter.

This performance increase can have a dramatic effect on hybrid search implementations. [Read more about how to set this up.](https://qdrant.tech/articles/sparse-vectors/)

FYI, sparse vectors were released in [Qdrant v.1.7.0](https://qdrant.tech/articles/qdrant-1.7.x/#sparse-vectors). They are stored using a different index, so first [check out the documentation](https://qdrant.tech/documentation/concepts/indexing/#sparse-vector-index) if you want to try an implementation.

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#cpu-resource-management) CPU resource management

Indexing is Qdrant’s most resource-intensive process. Now you can account for this by allocating compute use specifically to indexing. You can assign a number CPU resources towards indexing and leave the rest for search. As a result, indexes will build faster, and search quality will remain unaffected.

This isn’t mandatory, as Qdrant is by default tuned to strike the right balance between indexing and search. However, if you wish to define specific CPU usage, you will need to do so from `config.yaml`.

This version introduces a `optimizer_cpu_budget` parameter to control the maximum number of CPUs used for indexing.

> Read more about `config.yaml` in the [configuration file](https://qdrant.tech/documentation/guides/configuration/).

```yaml
# CPU budget, how many CPUs (threads) to allocate for an optimization job.
optimizer_cpu_budget: 0

```

- If left at 0, Qdrant will keep 1 or more CPUs unallocated - depending on CPU size.
- If the setting is positive, Qdrant will use this exact number of CPUs for indexing.
- If the setting is negative, Qdrant will subtract this number of CPUs from the available CPUs for indexing.

For most users, the default `optimizer_cpu_budget` setting will work well. We only recommend you use this if your indexing load is significant.

Our backend leverages dynamic CPU saturation to increase indexing speed. For that reason, the impact on search query performance ends up being minimal. Ultimately, you will be able to strike the best possible balance between indexing times and search performance.

This configuration can be done at any time, but it requires a restart of Qdrant. Changing it affects both existing and new collections.

> **Note:** This feature is not configurable on [Qdrant Cloud](https://qdrant.to/cloud).

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#better-indexing-for-text-data) Better indexing for text data

In order to [minimize your RAM expenditure](https://qdrant.tech/articles/memory-consumption/), we have developed a new way to index specific types of data. Please keep in mind that this is a backend improvement, and you won’t need to configure anything.

> Going forward, if you are indexing immutable text fields, we estimate a 10% reduction in RAM loads. Our benchmark result is based on a system that uses 64GB of RAM. If you are using less RAM, this reduction might be higher than 10%.

Immutable text fields are static and do not change once they are added to Qdrant. These entries usually represent some type of attribute, description or tag. Vectors associated with them can be indexed more efficiently, since you don’t need to re-index them anymore. Conversely, mutable fields are dynamic and can be modified after their initial creation. Please keep in mind that they will continue to require additional RAM.

This approach ensures stability in the [vector search](https://qdrant.tech/documentation/overview/vector-search/) index, with faster and more consistent operations. We achieved this by setting up a field index which helps minimize what is stored. To improve search performance we have also optimized the way we load documents for searches with a text field index. Now our backend loads documents mostly sequentially and in increasing order.

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#minor-improvements-and-new-features) Minor improvements and new features

Beyond these enhancements, [Qdrant v1.8.0](https://github.com/qdrant/qdrant/releases/tag/v1.8.0) adds and improves on several smaller features:

1. **Order points by payload:** In addition to searching for semantic results, you might want to retrieve results by specific metadata (such as price). You can now use Scroll API to [order points by payload key](https://qdrant.tech/documentation/concepts/points/#order-points-by-payload-key).
2. **Datetime support:** We have implemented [datetime support for the payload index](https://qdrant.tech/documentation/concepts/filtering/#datetime-range). Prior to this, if you wanted to search for a specific datetime range, you would have had to convert dates to UNIX timestamps. ( [PR#3320](https://github.com/qdrant/qdrant/issues/3320))
3. **Check collection existence:** You can check whether a collection exists via the `/exists` endpoint to the `/collections/{collection_name}`. You will get a true/false response. ( [PR#3472](https://github.com/qdrant/qdrant/pull/3472)).
4. **Find points** whose payloads match more than the minimal amount of conditions. We included the `min_should` match feature for a condition to be `true` ( [PR#3331](https://github.com/qdrant/qdrant/pull/3466/)).
5. **Modify nested fields:** We have improved the `set_payload` API, adding the ability to update nested fields ( [PR#3548](https://github.com/qdrant/qdrant/pull/3548)).

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#experience-the-power-of-qdrant-180) Experience the Power of Qdrant 1.8.0

Ready to experience the enhanced performance of Qdrant 1.8.0? Upgrade now and explore the major improvements, from faster sparse vectors to optimized CPU resource management and better indexing for text data. Take your search capabilities to the next level with Qdrant’s latest version. [Try a demo today](https://qdrant.tech/demo/) and see the difference firsthand!

## [Anchor](https://qdrant.tech/articles/qdrant-1.8.x/\#release-notes) Release notes

For more information, see [our release notes](https://github.com/qdrant/qdrant/releases/tag/v1.8.0).
Qdrant is an open-source project. We welcome your contributions; raise [issues](https://github.com/qdrant/qdrant/issues), or contribute via [pull requests](https://github.com/qdrant/qdrant/pulls)!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.8.x.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.8.x.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574530293&cv=11&fst=1748574530293&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.8.x%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%201.8.0%3A%20Enhanced%20Search%20Capabilities%20for%20Better%20Results%20-%20Qdrant&npa=0&pscdl=noapi&auid=795761975.1748574530&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574530273&cv=11&fst=1748574530273&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.8.x%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%201.8.0%3A%20Enhanced%20Search%20Capabilities%20for%20Better%20Results%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=795761975.1748574530&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0194ee2e-57f9-4d91-8f58-9e63746633eb&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=caad9cfb-5dbf-4ce6-8c10-b1cd16b67014&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.8.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0194ee2e-57f9-4d91-8f58-9e63746633eb&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=caad9cfb-5dbf-4ce6-8c10-b1cd16b67014&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.8.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574531350&cv=11&fst=1748574531350&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.8.x%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%201.8.0%3A%20Enhanced%20Search%20Capabilities%20for%20Better%20Results%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=795761975.1748574530&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)