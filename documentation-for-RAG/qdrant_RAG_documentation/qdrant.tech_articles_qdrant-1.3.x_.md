---
url: "https://qdrant.tech/articles/qdrant-1.3.x/"
title: "Introducing Qdrant 1.3.0 - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Introducing Qdrant 1.3.0

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# Introducing Qdrant 1.3.0

David Sertic

·

June 26, 2023

![Introducing Qdrant 1.3.0](https://qdrant.tech/articles_data/qdrant-1.3.x/preview/title.jpg)

A brand-new [Qdrant 1.3.0 release](https://github.com/qdrant/qdrant/releases/tag/v1.3.0) comes packed with a plethora of new features, performance improvements and bux fixes:

1. Asynchronous I/O interface: Reduce overhead by managing I/O operations asynchronously, thus minimizing context switches.
2. Oversampling for Quantization: Improve the accuracy and performance of your queries while using Scalar or Product Quantization.
3. Grouping API lookup: Storage optimization method that lets you look for points in another collection using group ids.
4. Qdrant Web UI: A convenient dashboard to help you manage data stored in Qdrant.
5. Temp directory for Snapshots: Set a separate storage directory for temporary snapshots on a faster disk.
6. Other important changes

Your feedback is valuable to us, and are always tying to include some of your feature requests into our roadmap. Join [our Discord community](https://qdrant.to/discord) and help us build Qdrant!.

## [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#new-features) New features

### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#asychronous-io-interface) Asychronous I/O interface

Going forward, we will support the `io_uring` asychnronous interface for storage devices on Linux-based systems. Since its introduction, `io_uring` has been proven to speed up slow-disk deployments as it decouples kernel work from the IO process.

This interface uses two ring buffers to queue and manage I/O operations asynchronously, avoiding costly context switches and reducing overhead. Unlike mmap, it frees the user threads to do computations instead of waiting for the kernel to complete.

![io_uring](https://qdrant.tech/articles_data/qdrant-1.3.x/io-uring.png)

#### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#enable-the-interface-from-your-config-file) Enable the interface from your config file:

```yaml
storage:
	# enable the async scorer which uses io_uring
	async_scorer: true

```

You can return to the mmap based backend by either deleting the `async_scorer` entry or setting the value to `false`.

This optimization will mainly benefit workloads with lots of disk IO (e.g. querying on-disk collections with rescoring).
Please keep in mind that this feature is experimental and that the interface may change in further versions.

### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#oversampling-for-quantization) Oversampling for quantization

We are introducing [oversampling](https://qdrant.tech/documentation/guides/quantization/#oversampling) as a new way to help you improve the accuracy and performance of similarity search algorithms. With this method, you are able to significantly compress high-dimensional vectors in memory and then compensate the accuracy loss by re-scoring additional points with the original vectors.

You will experience much faster performance with quantization due to parallel disk usage when reading vectors. Much better IO means that you can keep quantized vectors in RAM, so the pre-selection will be even faster. Finally, once pre-selection is done, you can use parallel IO to retrieve original vectors, which is significantly faster than traversing HNSW on slow disks.

#### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#set-the-oversampling-factor-via-query) Set the oversampling factor via query:

Here is how you can configure the oversampling factor - define how many extra vectors should be pre-selected using the quantized index, and then re-scored using original vectors.

httppython

```http
POST /collections/{collection_name}/points/search
{
  "params": {
    "quantization": {
      "ignore": false,
      "rescore": true,
      "oversampling": 2.4
    }
  },
  "vector": [0.2, 0.1, 0.9, 0.7],
  "limit": 100
}

```

```python
from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient("localhost", port=6333)

client.search(
    collection_name="{collection_name}",
    query_vector=[0.2, 0.1, 0.9, 0.7],
    search_params=models.SearchParams(
        quantization=models.QuantizationSearchParams(
            ignore=False,
            rescore=True,
            oversampling=2.4
        )
    )
)

```

In this case, if `oversampling` is 2.4 and `limit` is 100, then 240 vectors will be pre-selected using quantized index, and then the top 100 points will be returned after re-scoring with the unquantized vectors.

As you can see from the example above, this parameter is set during the query. This is a flexible method that will let you tune query accuracy. While the index is not changed, you can decide how many points you want to retrieve using quantized vectors.

### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#grouping-api-lookup) Grouping API lookup

In version 1.2.0, we introduced a mechanism for requesting groups of points. Our new feature extends this functionality by giving you the option to look for points in another collection using the group ids. We wanted to add this feature, since having a single point for the shared data of the same item optimizes storage use, particularly if the payload is large.

This has the extra benefit of having a single point to update when the information shared by the points in a group changes.

![Group Lookup](https://qdrant.tech/articles_data/qdrant-1.3.x/group-lookup.png)

For example, if you have a collection of documents, you may want to chunk them and store the points for the chunks in a separate collection, making sure that you store the point id from the document it belongs in the payload of the chunk point.

#### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#adding-the-parameter-to-grouping-api-request) Adding the parameter to grouping API request:

When using the grouping API, add the `with_lookup` parameter to bring the information from those points into each group:

httppython

```http
POST /collections/chunks/points/search/groups
{
    // Same as in the regular search API
    "vector": [1.1],
    ...,

    // Grouping parameters
    "group_by": "document_id",
    "limit": 2,
    "group_size": 2,

    // Lookup parameters
    "with_lookup": {
        // Name of the collection to look up points in
        "collection_name": "documents",

        // Options for specifying what to bring from the payload
        // of the looked up point, true by default
        "with_payload": ["title", "text"],

        // Options for specifying what to bring from the vector(s)
        // of the looked up point, true by default
        "with_vectors: false,
    }
}

```

```python
client.search_groups(
    collection_name="chunks",

    # Same as in the regular search() API
    query_vector=[1.1],
    ...,

    # Grouping parameters
    group_by="document_id", # Path of the field to group by
    limit=2,                # Max amount of groups
    group_size=2,           # Max amount of points per group

    # Lookup parameters
    with_lookup=models.WithLookup(
        # Name of the collection to look up points in
        collection_name="documents",

        # Options for specifying what to bring from the payload
        # of the looked up point, True by default
        with_payload=["title", "text"]

        # Options for specifying what to bring from the vector(s)
        # of the looked up point, True by default
        with_vectors=False,
    )
)

```

### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#qdrant-web-user-interface) Qdrant web user interface

We are excited to announce a more user-friendly way to organize and work with your collections inside of Qdrant. Our dashboard’s design is simple, but very intuitive and easy to access.

Try it out now! If you have Docker running, you can [quickstart Qdrant](https://qdrant.tech/documentation/quick-start/) and access the Dashboard locally from [http://localhost:6333/dashboard](http://localhost:6333/dashboard). You should see this simple access point to Qdrant:

![Qdrant Web UI](https://qdrant.tech/articles_data/qdrant-1.3.x/web-ui.png)

### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#temporary-directory-for-snapshots) Temporary directory for Snapshots

Currently, temporary snapshot files are created inside the `/storage` directory. Oftentimes `/storage` is a network-mounted disk. Therefore, we found this method suboptimal because `/storage` is limited in disk size and also because writing data to it may affect disk performance as it consumes bandwidth. This new feature allows you to specify a different directory on another disk that is faster. We expect this feature to significantly optimize cloud performance.

To change it, access `config.yaml` and set `storage.temp_path` to another directory location.

## [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#important-changes) Important changes

The latest release focuses not only on the new features but also introduces some changes making
Qdrant even more reliable.

### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#optimizing-group-requests) Optimizing group requests

Internally, `is_empty` was not using the index when it was called, so it had to deserialize the whole payload to see if the key had values or not. Our new update makes sure to check the index first, before confirming with the payload if it is actually `empty`/ `null`, so these changes improve performance only when the negated condition is true (e.g. it improves when the field is not empty). Going forward, this will improve the way grouping API requests are handled.

### [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#faster-read-access-with-mmap) Faster read access with mmap

If you used mmap, you most likely found that segments were always created with cold caches. The first request to the database needed to request the disk, which made startup slower despite plenty of RAM being available. We have implemeneted a way to ask the kernel to “heat up” the disk cache and make initialization much faster.

The function is expected to be used on startup and after segment optimization and reloading of newly indexed segment. So far this is only implemented for “immutable” memmaps.

## [Anchor](https://qdrant.tech/articles/qdrant-1.3.x/\#release-notes) Release notes

As usual, [our release notes](https://github.com/qdrant/qdrant/releases/tag/v1.3.0) describe all the changes
introduced in the latest version.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.3.x.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qdrant-1.3.x.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575292469&cv=11&fst=1748575292469&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.3.x%2F&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Qdrant%201.3.0%20-%20Qdrant&npa=0&pscdl=noapi&auid=1882727275.1748575292&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575292443&cv=11&fst=1748575292443&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.3.x%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Qdrant%201.3.0%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1882727275.1748575292&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7074aa9f-38a7-41f7-8a31-5232f4a292c3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4222cbf7-ed5a-4e01-a572-e13091ab1131&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.3.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7074aa9f-38a7-41f7-8a31-5232f4a292c3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4222cbf7-ed5a-4e01-a572-e13091ab1131&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.3.x%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575293558&cv=11&fst=1748575293558&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fqdrant-1.3.x%2F&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Qdrant%201.3.0%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1882727275.1748575292&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)