---
url: "https://qdrant.tech/documentation/faq/qdrant-fundamentals/"
title: "Qdrant Fundamentals - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Faq](https://qdrant.tech/documentation/faq/)
- Qdrant Fundamentals

# [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#frequently-asked-questions-general-topics) Frequently Asked Questions: General Topics

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| [Vectors](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#vectors) | [Search](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#search) | [Collections](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#collections) | [Compatibility](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#compatibility) | [Cloud](https://qdrant.tech/documentation/faq/qdrant-fundamentals/#cloud) |

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#vectors) Vectors

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#what-is-the-maximum-vector-dimension-supported-by-qdrant) What is the maximum vector dimension supported by Qdrant?

Qdrant supports up to 65,535 dimensions by default, but this can be configured to support higher dimensions.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#what-is-the-maximum-size-of-vector-metadata-that-can-be-stored) What is the maximum size of vector metadata that can be stored?

There is no inherent limitation on metadata size, but it should be [optimized for performance and resource usage](https://qdrant.tech/documentation/guides/optimize/). Users can set upper limits in the configuration.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#can-the-same-similarity-search-query-yield-different-results-on-different-machines) Can the same similarity search query yield different results on different machines?

Yes, due to differences in hardware configurations and parallel processing, results may vary slightly.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-do-i-choose-the-right-vector-embeddings-for-my-use-case) How do I choose the right vector embeddings for my use case?

This depends on the nature of your data and the specific application. Consider factors like dimensionality, domain-specific models, and the performance characteristics of different embeddings.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-does-qdrant-handle-different-vector-embeddings-from-various-providers-in-the-same-collection) How does Qdrant handle different vector embeddings from various providers in the same collection?

Qdrant natively [supports multiple vectors per data point](https://qdrant.tech/documentation/concepts/vectors/#multivectors), allowing different embeddings from various providers to coexist within the same collection.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#can-i-migrate-my-embeddings-from-another-vector-store-to-qdrant) Can I migrate my embeddings from another vector store to Qdrant?

Yes, Qdrant supports migration of embeddings from other vector stores, facilitating easy transitions and adoption of Qdrant’s features.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#why-the-amount-of-indexed-vectors-doesnt-match-the-amount-of-vectors-in-the-collection) Why the amount of indexed vectors doesn’t match the amount of vectors in the collection?

Qdrant doesn’t always need to index all vectors in the collection.
It stores data is segments, and if the segment is small enough, it is more efficient to perform a full-scan search on it.

Make sure to check that the collection status is `green` and that the number of unindexed vectors smaller than indexing threshold.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#why-collection-info-shows-inaccurate-number-of-points) Why collection info shows inaccurate number of points?

Collection info API in Qdrant returns an approximate number of points in the collection.
If you need an exact number, you can use the [count](https://qdrant.tech/documentation/concepts/points/#counting-points) API.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#vectors-in-the-collection-dont-match-what-i-uploaded) Vectors in the collection don’t match what I uploaded.

There are two possible reasons for this:

- You used the `Cosine` distance metric in the [collection settings](https://qdrant.tech/concepts/collections/#collections). In this case, Qdrant pre-normalizes your vectors for faster distance computation. If you strictly need the original vectors to be preserved, consider using the `Dot` distance metric instead.
- You used the `uint8` [datatype](https://qdrant.tech/documentation/concepts/vectors/#datatypes) to store vectors. `uint8` requires a special format for input values, which might not be compatible with the typical output of embedding models.

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#search) Search

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-does-qdrant-handle-real-time-data-updates-and-search) How does Qdrant handle real-time data updates and search?

Qdrant supports live updates for vector data, with newly inserted, updated and deleted vectors available for immediate search. The system uses full-scan search on unindexed segments during background index updates.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#my-search-results-contain-vectors-with-null-values-why) My search results contain vectors with null values. Why?

By default, Qdrant tries to minimize network traffic and doesn’t return vectors in search results.
But you can force Qdrant to do so by setting the `with_vector` parameter of the Search/Scroll to `true`.

If you’re still seeing `"vector": null` in your results, it might be that the vector you’re passing is not in the correct format, or there’s an issue with how you’re calling the upsert method.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-can-i-search-without-a-vector) How can I search without a vector?

You are likely looking for the [scroll](https://qdrant.tech/documentation/concepts/points/#scroll-points) method. It allows you to retrieve the records based on filters or even iterate over all the records in the collection.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#does-qdrant-support-a-full-text-search-or-a-hybrid-search) Does Qdrant support a full-text search or a hybrid search?

Qdrant is a vector search engine in the first place, and we only implement full-text support as long as it doesn’t compromise the vector search use case.
That includes both the interface and the performance.

What Qdrant can do:

- Search with full-text filters
- Apply full-text filters to the vector search (i.e., perform vector search among the records with specific words or phrases)
- Do prefix search and semantic [search-as-you-type](https://qdrant.tech/articles/search-as-you-type/)
- Sparse vectors, as used in [SPLADE](https://github.com/naver/splade) or similar models
- [Multi-vectors](https://qdrant.tech/documentation/concepts/vectors/#multivectors), for example ColBERT and other late-interaction models
- Combination of the [multiple searches](https://qdrant.tech/documentation/concepts/hybrid-queries/)

What Qdrant doesn’t plan to support:

- Non-vector-based retrieval or ranking functions
- Built-in ontologies or knowledge graphs
- Query analyzers and other NLP tools

Of course, you can always combine Qdrant with any specialized tool you need, including full-text search engines.
Read more about [our approach](https://qdrant.tech/articles/hybrid-search/) to hybrid search.

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#collections) Collections

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-many-collections-can-i-create) How many collections can I create?

As many as you want, but be aware that each collection requires additional resources.
It is _highly_ recommended not to create many small collections, as it will lead to significant resource consumption overhead.

We consider creating a collection for each user/dialog/document as an antipattern.

Please read more about collections, isolation, and multiple users in our [Multitenancy](https://qdrant.tech/documentation/tutorials/multiple-partitions/) tutorial.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-do-i-upload-a-large-number-of-vectors-into-a-qdrant-collection) How do I upload a large number of vectors into a Qdrant collection?

Read about our recommendations in the [bulk upload](https://qdrant.tech/documentation/tutorials/bulk-upload/) tutorial.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#can-i-only-store-quantized-vectors-and-discard-full-precision-vectors) Can I only store quantized vectors and discard full precision vectors?

No, Qdrant requires full precision vectors for operations like reindexing, rescoring, etc.

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#compatibility) Compatibility

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#is-qdrant-compatible-with-cpus-or-gpus-for-vector-computation) Is Qdrant compatible with CPUs or GPUs for vector computation?

Qdrant primarily relies on CPU acceleration for scalability and efficiency. However, we also support GPU-accelerated indexing on all major vendors.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#do-you-guarantee-compatibility-across-versions) Do you guarantee compatibility across versions?

In case your version is older, we only guarantee compatibility between two consecutive minor versions. This also applies to client versions. Ensure your client version is never more than one minor version away from your cluster version.
While we will assist with break/fix troubleshooting of issues and errors specific to our products, Qdrant is not accountable for reviewing, writing (or rewriting), or debugging custom code.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#do-you-support-downgrades) Do you support downgrades?

We do not support downgrading a cluster on any of our products. If you deploy a newer version of Qdrant, your
data is automatically migrated to the newer storage format. This migration is not reversible.

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#how-do-i-avoid-issues-when-updating-to-the-latest-version) How do I avoid issues when updating to the latest version?

We only guarantee compatibility if you update between consecutive versions. You would need to upgrade versions one at a time: `1.1 -> 1.2`, then `1.2 -> 1.3`, then `1.3 -> 1.4`.

## [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#cloud) Cloud

### [Anchor](https://qdrant.tech/documentation/faq/qdrant-fundamentals/\#is-it-possible-to-scale-down-a-qdrant-cloud-cluster) Is it possible to scale down a Qdrant Cloud cluster?

Yes, it is possible to both vertically and horizontally scale down a Qdrant Cloud cluster.
Note, that during the vertical scaling down, the disk size cannot be reduced.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/faq/qdrant-fundamentals.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/faq/qdrant-fundamentals.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574198773&cv=11&fst=1748574198773&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015665~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffaq%2Fqdrant-fundamentals%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Fundamentals%20-%20Qdrant&npa=0&pscdl=noapi&auid=333224213.1748574199&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574198754&cv=11&fst=1748574198754&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015665~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308615&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffaq%2Fqdrant-fundamentals%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Fundamentals%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=333224213.1748574199&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b43d340e-b8bc-4b14-90a9-9a7187792f2a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=38beda0d-ae25-4ddf-8267-88fd6a8c7add&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffaq%2Fqdrant-fundamentals%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b43d340e-b8bc-4b14-90a9-9a7187792f2a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=38beda0d-ae25-4ddf-8267-88fd6a8c7add&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffaq%2Fqdrant-fundamentals%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574199829&cv=11&fst=1748574199829&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015665~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffaq%2Fqdrant-fundamentals%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Fundamentals%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=333224213.1748574199&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)