---
url: "https://qdrant.tech/articles/qdrant-1.7.x/"
title: "Qdrant 1.7.0 has just landed! - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Qdrant 1.7.0 has just landed!

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# Qdrant 1.7.0 has just landed!

Kacper Łukawski

·

December 10, 2023

![Qdrant 1.7.0 has just landed!](https://qdrant.tech/articles_data/qdrant-1.7.x/preview/title.jpg)

Please welcome the long-awaited [Qdrant 1.7.0 release](https://github.com/qdrant/qdrant/releases/tag/v1.7.0). Except for a handful of minor fixes and improvements, this release brings some cool brand-new features that we are excited to share!
The latest version of your favorite vector search engine finally supports **sparse vectors**. That’s the feature many of you requested, so why should we ignore it?
We also decided to continue our journey with [vector similarity beyond search](https://qdrant.tech/articles/vector-similarity-beyond-search/). The new Discovery API covers some utterly new use cases. We’re more than excited to see what you will build with it!
But there is more to it! Check out what’s new in **Qdrant 1.7.0**!

1. Sparse vectors: do you want to use keyword-based search? Support for sparse vectors is finally here!
2. Discovery API: an entirely new way of using vectors for restricted search and exploration.
3. User-defined sharding: you can now decide which points should be stored on which shard.
4. Snapshot-based shard transfer: a new option for moving shards between nodes.

Do you see something missing? Your feedback drives the development of Qdrant, so do not hesitate to [join our Discord community](https://qdrant.to/discord) and help us build the best vector search engine out there!

## [Anchor](https://qdrant.tech/articles/qdrant-1.7.x/\#new-features) New features

Qdrant 1.7.0 brings a bunch of new features. Let’s take a closer look at them!

### [Anchor](https://qdrant.tech/articles/qdrant-1.7.x/\#sparse-vectors) Sparse vectors

Traditional keyword-based search mechanisms often rely on algorithms like TF-IDF, BM25, or comparable methods. While these techniques internally utilize vectors, they typically involve sparse vector representations. In these methods, the **vectors are predominantly filled with zeros, containing a relatively small number of non-zero values**.
Those sparse vectors are theoretically high dimensional, definitely way higher than the dense vectors used in semantic search. However, since the majority of dimensions are usually zeros, we store them differently and just keep the non-zero dimensions.

Until now, Qdrant has not been able to handle sparse vectors natively. Some were trying to convert them to dense vectors, but that was not the best solution or a suggested way. We even wrote a piece with [our thoughts on building a hybrid search](https://qdrant.tech/articles/hybrid-search/), and we encouraged you to use a different tool for keyword lookup.

Things have changed since then, as so many of you wanted a single tool for sparse and dense vectors. And responding to this [popular](https://github.com/qdrant/qdrant/issues/1678) [demand](https://github.com/qdrant/qdrant/issues/1135), we’ve now introduced sparse vectors!

If you’re coming across the topic of sparse vectors for the first time, our [Brief History of Search](https://qdrant.tech/documentation/overview/vector-search/) explains the difference between sparse and dense vectors.

Check out the [sparse vectors article](https://qdrant.tech/articles/sparse-vectors/) and [sparse vectors index docs](https://qdrant.tech/documentation/concepts/indexing/#sparse-vector-index) for more details on what this new index means for Qdrant users.

### [Anchor](https://qdrant.tech/articles/qdrant-1.7.x/\#discovery-api) Discovery API

The recently launched [Discovery API](https://qdrant.tech/documentation/concepts/explore/#discovery-api) extends the range of scenarios for leveraging vectors. While its interface mirrors the [Recommendation API](https://qdrant.tech/documentation/concepts/explore/#recommendation-api), it focuses on refining the search parameters for greater precision.
The concept of ‘context’ refers to a collection of positive-negative pairs that define zones within a space. Each pair effectively divides the space into positive or negative segments. This concept guides the search operation to prioritize points based on their inclusion within positive zones or their avoidance of negative zones. Essentially, the search algorithm favors points that fall within multiple positive zones or steer clear of negative ones.

The Discovery API can be used in two ways - either with or without the target point. The first case is called a **discovery search**, while the second is called a **context search**.

#### [Anchor](https://qdrant.tech/articles/qdrant-1.7.x/\#discovery-search) Discovery search

_Discovery search_ is an operation that uses a target point to find the most relevant points in the collection, while performing the search in the preferred areas only. That is basically a search operation with more control over the search space.

![Discovery search visualization](https://qdrant.tech/articles_data/qdrant-1.7.x/discovery-search.png)

Please refer to the [Discovery API documentation on discovery search](https://qdrant.tech/documentation/concepts/explore/#discovery-search) for more details and the internal mechanics of the operation.

#### [Anchor](https://qdrant.tech/articles/qdrant-1.7.x/\#context-search) Context search

The mode of _context search_ is similar to the discovery search, but it does not use a target point. Instead, the `context` is used to navigate the [HNSW graph](https://arxiv.org/abs/1603.09320) towards preferred zones. It is expected that the results in that mode will be diverse, and not centered around one point.
_Context Search_ could serve as a solution for individuals seeking a more exploratory approach to navigate the vector space.

![Context search visualization](https://qdrant.tech/articles_data/qdrant-1.7.x/context-search.png)

### [Anchor](https://qdrant.tech/articles/qdrant-1.7.x/\#user-defined-sharding) User-defined sharding

Qdrant’s collections are divided into shards. A single **shard** is a self-contained store of points, which can be moved between nodes. Up till now, the points were distributed among shards by using a consistent hashing algorithm, so that shards were managing non-intersecting subsets of points.
The latter one remains true, but now you can define your own sharding and decide which points should be stored on which shard. Sounds cool, right? But why would you need that? Well, there are multiple scenarios in which you may want to use custom sharding. For example, you may want to store some points on a dedicated node, or you may want to store points from the same user on the same shard and

While the existing behavior is still the default one, you can now define the shards when you create a collection. Then, you can assign each point to a shard by providing a `shard_key` in the `upsert` operation. What’s more, you can also search over the selected shards only, by providing the `shard_key` parameter in the search operation.

```http
POST /collections/my_collection/points/search
{
    "vector": [0.29, 0.81, 0.75, 0.11],
    "shard_key": ["cats", "dogs"],
    "limit": 10,
    "with_payload": true,
}

```

If you want to know more about the user-defined sharding, please refer to the [sharding documentation](https://qdrant.tech/documentation/guides/distributed_deployment/#sharding).

### [Anchor](https://qdrant.tech/articles/qdrant-1.7.x/\#snapshot-based-shard-transfer) Snapshot-based shard transfer

That’s a really more in depth technical improvement for the distributed mode users, that we implemented a new options the shard transfer mechanism. The new approach is based on the snapshot of the shard, which is transferred to the target node.

Moving shards is required for dynamical scaling of the cluster. Your data can migrate between nodes, and the way you move it is crucial for the performance of the whole system. The good old `stream_records` method (still the default one) transmits all the records between the machines and indexes them on the target node.
In the case of moving the shard, it’s necessary to recreate the HNSW index each time. However, with the introduction of the new `snapshot` approach, the snapshot itself, inclusive of all data and potentially quantized content, is transferred to the target node. This comprehensive snapshot includes the entire index, enabling the target node to seamlessly load it and promptly begin handling requests without the need for index recreation.

There are multiple scenarios in which you may prefer one over the other. Please check out the docs of the [shard transfer method](https://qdrant.tech/documentation/guides/distributed_deployment/#shard-transfer-method) for more details and head-to-head comparison. As for now, the old `stream_records` method is still the default one, but we may decide to change it in the future.

## [Anchor](https://qdrant.tech/articles/qdrant-1.7.x/\#minor-improvements) Minor improvements

Beyond introducing new features, Qdrant 1.7.0 enhances performance and addresses various minor issues. Here’s a rundown of the key improvements:

1. Improvement of HNSW Index Building on High CPU Systems ( [PR#2869](https://github.com/qdrant/qdrant/pull/2869)).

2. Improving [Search Tail Latencies](https://github.com/qdrant/qdrant/pull/2931): improvement for high CPU systems with many parallel searches, directly impacting the user experience by reducing latency.

3. [Adding Index for Geo Map Payloads](https://github.com/qdrant/qdrant/pull/2768): index for geo map payloads can significantly improve search performance, especially for applications involving geographical data.

4. Stability of Consensus on Big High Load Clusters: enhancing the stability of consensus in large, high-load environments is critical for ensuring the reliability and scalability of the system ( [PR#3013](https://github.com/qdrant/qdrant/pull/3013), [PR#3026](https://github.com/qdrant/qdrant/pull/3026), [PR#2942](https://github.com/qdrant/qdrant/pull/2942), [PR#3103](https://github.com/qdrant/qdrant/pull/3103), [PR#3054](https://github.com/qdrant/qdrant/pull/3054)).

5. Configurable Timeout for Searches: allowing users to configure the timeout for searches provides greater flexibility and can help optimize system performance under different operational conditions ( [PR#2748](https://github.com/qdrant/qdrant/pull/2748), [PR#2771](https://github.com/qdrant/qdrant/pull/2771)).


## [Anchor](https://qdrant.tech/articles/qdrant-1.7.x/\#release-notes) Release notes

[Our release notes](https://github.com/qdrant/qdrant/releases/tag/v1.7.0) are a place to go if you are interested in more details. Please remember that Qdrant is an open source project, so feel free to [contribute](https://github.com/qdrant/qdrant/issues)!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.7.x.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.7.x.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574462619&cv=11&fst=1748574462619&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.7.x%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%201.7.0%20has%20just%20landed!%20-%20Qdrant&npa=0&pscdl=noapi&auid=2098622886.1748574463&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574462602&cv=11&fst=1748574462602&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.7.x%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%201.7.0%20has%20just%20landed!%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2098622886.1748574463&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=fc998201-a92a-4de6-97a5-58f8a7cc0ea2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7ca9a103-a796-46b7-b19e-2f39c66a1f00&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.7.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=fc998201-a92a-4de6-97a5-58f8a7cc0ea2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7ca9a103-a796-46b7-b19e-2f39c66a1f00&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.7.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574463694&cv=11&fst=1748574463694&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.7.x%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%201.7.0%20has%20just%20landed!%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2098622886.1748574463&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)