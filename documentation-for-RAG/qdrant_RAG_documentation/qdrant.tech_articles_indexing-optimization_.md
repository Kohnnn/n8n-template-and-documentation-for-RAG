---
url: "https://qdrant.tech/articles/indexing-optimization/"
title: "Optimizing Memory for Bulk Uploads - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Optimizing Memory for Bulk Uploads

[Back to Vector Search Manuals](https://qdrant.tech/articles/vector-search-manuals/)

# Optimizing Memory for Bulk Uploads

Sabrina Aquino

·

February 13, 2025

![Optimizing Memory for Bulk Uploads](https://qdrant.tech/articles_data/indexing-optimization/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/indexing-optimization/\#optimizing-memory-consumption-during-bulk-uploads) Optimizing Memory Consumption During Bulk Uploads

Efficient memory management is a constant challenge when you’re dealing with **large-scale vector data**. In high-volume ingestion scenarios, even seemingly minor configuration choices can significantly impact stability and performance.

Let’s take a look at the best practices and recommendations to help you optimize memory usage during bulk uploads in Qdrant. We’ll cover scenarios with both **dense** and **sparse** vectors, helping your deployments remain performant even under high load and avoiding out-of-memory errors.

## [Anchor](https://qdrant.tech/articles/indexing-optimization/\#indexing-for-dense-vs-sparse-vectors) Indexing for dense vs. sparse vectors

**Dense vectors**

Qdrant employs an **HNSW-based index** for fast similarity search on dense vectors. By default, HNSW is built or updated once the number of **unindexed** vectors in a segment exceeds a set `indexing_threshold`. Although it delivers excellent query speed, building or updating the HNSW graph can be **resource-intensive** if it occurs frequently or across many small segments.

**Sparse vectors**

Sparse vectors use an **inverted index**. This index is updated at the **time of upsertion**, meaning you cannot disable or postpone it for sparse vectors. In most cases, its overhead is smaller than that of building an HNSW graph, but you should still be aware that each upsert triggers a sparse index update.

## [Anchor](https://qdrant.tech/articles/indexing-optimization/\#bulk-upload-configuration-for-dense-vectors) Bulk upload configuration for dense vectors

When performing high-volume vector ingestion, you have **two primary options** for handling indexing overhead. You should choose one depending on your specific workload and memory constraints:

- **Disable HNSW indexing**

To reduce memory and CPU pressure during bulk ingestion, you can **disable HNSW indexing entirely** by setting `"m": 0`.
For dense vectors, the `m` parameter defines how many edges each node in the HNSW graph can have.
This way, no dense vector index will be built, preventing unnecessary CPU usage during ingestion.

**Figure 1:** A description of three key HNSW parameters.

![](https://qdrant.tech/articles_data/indexing-optimization/hnsw-parameters.png)

```json
PATCH /collections/your_collection
{
  "hnsw_config": {
    "m": 0
  }
}

```

**After ingestion is complete**, you can **re-enable HNSW** by setting `m` back to a production value (commonly 16 or 32).
Remember that search won’t use HNSW until the index is built, so search performance may be slower during this period.

- **Disabling optimizations completely**

The `indexing_threshold` tells Qdrant how many unindexed dense vectors can accumulate in a segment before building the HNSW graph. Setting `"indexing_threshold"=0` defers indexing entirely, keeping **ingestion speed at maximum**. However, this means uploaded vectors are not moved to disk while uploading, which can lead to **high RAM usage**.

```json
PATCH /collections/your_collection
{
  "optimizer_config": {
    "indexing_threshold": 0
  }
}

```

After bulk ingestion, set `indexing_threshold` to a positive value to ensure vectors are indexed and searchable via HNSW. **Vectors will not be searchable via HNSW until indexing is performed.**

Small thresholds (e.g., 100) mean more frequent indexing, which can still be costly if many segments exist. Larger thresholds (e.g., 10000) delay indexing to batch more vectors at once, potentially using more RAM at the moment of index build, but fewer builds overall.

Between these two approaches, we generally recommend disabling HNSW ( `"m"=0`) during bulk ingestion to keep memory usage predictable. Using `indexing_threshold=0` can be an alternative, but only if your system has enough memory to accommodate the unindexed vectors in RAM.

* * *

## [Anchor](https://qdrant.tech/articles/indexing-optimization/\#on-disk-storage-in-qdrant) On-Disk storage in Qdrant

By default, Qdrant keeps **vectors**, **payload data**, and **indexes** in memory to ensure low-latency queries. However, in large-scale or memory-constrained scenarios, you can configure some or all of them to be stored on-disk. This helps reduce RAM usage at the cost of potential increases in query latency, particularly for cold reads.

**When to use on-disk**:

- You have **very large** or **rarely used** payload data or indexes, and freeing up RAM is worth potential I/O overhead.
- Your dataset doesn’t fit comfortably in available memory.
- You want to reduce memory pressure.
- You can tolerate slower queries if it ensures the system remains stable under heavy loads.

* * *

## [Anchor](https://qdrant.tech/articles/indexing-optimization/\#memmap-storage-and-segmentation) Memmap storage and segmentation

Qdrant uses **memory-mapped files** (segments) to store data on-disk. Rather than loading all vectors into RAM, Qdrant maps each segment into its address space, paging data in and out on demand. This helps keep the active RAM footprint lower, because data can be paged out if memory pressure is high. But each segment still incurs overhead (metadata, page table entries, etc.).

During **high-volume ingestion**, you can accumulate dozens of small segments. Qdrant’s **optimizer** can later merge these into fewer, larger segments, reducing per-segment overhead and lowering total memory usage.

When you create a collection with `"on_disk": true`, Qdrant will store newly inserted vectors in memmap storage from the start. For example:

```json
PATCH /collections/your_collection
{
    "vectors": {
      "on_disk": true
    }
}

```

This approach immediately places all incoming vectors on disk, which can be very efficient in case of bulk ingestion.

However, **vector data and indexes are stored separately**, so enabling `on_disk` for vectors does not automatically store their indexes on disk. To fully optimize memory usage, you may need to configure **both vector storage and index storage** independently.

For dense vectors, you can enable on-disk storage for both the **vector data** and the **HNSW index**:

```json
PATCH /collections/your_collection
{
    "vectors": {
        "on_disk": true
    },
    "hnsw_config": {
        "on_disk": true
    }
}

```

For sparse vectors, you need to enable `on_disk` for both the vector data and the sparse index separately:

```json
PATCH /collections/your_collection
{
    "sparse_vectors": {
        "text": {
            "on_disk": true,
            "index": {
                "on_disk": true
            }
        }
    }
}

```

* * *

## [Anchor](https://qdrant.tech/articles/indexing-optimization/\#best-practices-for-high-volume-vector-ingestion)**Best practices for high-volume vector ingestion**

Bulk ingestion can lead to high memory consumption and even out-of-memory (OOM) errors. **If you’re experiencing out-of-memory errors with your current setup**, scaling up temporarily (increasing available RAM) will provide a buffer while you adjust Qdrant’s configuration for more a efficient data ingestion.

The key here is to control indexing overhead. Let’s walk through the best practices for high-volume vector ingestion in a constrained-memory environment.

### [Anchor](https://qdrant.tech/articles/indexing-optimization/\#1-store-vector-data-on-disk-immediately) 1\. Store vector data on disk immediately

The most effective way to reduce memory usage is to store vector data on disk right from the start using `on_disk: true`. This prevents RAM from being overloaded with raw vectors before optimization kicks in.

```json
PATCH /collections/your_collection
{
  "vectors": {
    "on_disk": true
  }
}

```

Previously, vector data had to be held in RAM until optimizers could move it to disk, which caused significant memory pressure. Now, by writing vectors to disk directly, memory overhead is significantly reduced, making bulk ingestion much more efficient.

### [Anchor](https://qdrant.tech/articles/indexing-optimization/\#2-disable-hnsw-for-dense-vectors-m0) 2\. Disable HNSW for dense vectors ( `m=0`)

During an **initial bulk load**, you can **disable** dense indexing by setting `"m": 0.` This ensures Qdrant won’t build an HNSW graph for incoming vectors, avoiding unnecessary memory and CPU usage.

```json
PATCH /collections/your_collection
{
  "hnsw_config": {
    "m": 0
  },
  "optimizer_config": {
    "indexing_threshold": 10000
  }
}

```

### [Anchor](https://qdrant.tech/articles/indexing-optimization/\#3-let-the-optimizer-run-after-bulk-uploads) 3\. Let the optimizer run **after** bulk uploads

Qdrant’s optimizers continuously restructure data to improve search efficiency. However, during a bulk upload, this can lead to excessive data movement and overhead as segments are constantly reorganized while new data is still arriving.

To avoid this, **upload all data first**, then allow the optimizer to process everything in one go. This minimizes redundant operations and ensures a more efficient segment structure.

### [Anchor](https://qdrant.tech/articles/indexing-optimization/\#4-wait-for-indexation-to-clear-up-memory)**4\. Wait for indexation to clear up memory**

Before performing additional operations, **allow Qdrant to finish any ongoing indexing**. Large indexing jobs can keep memory usage high until they fully complete.

Monitor Qdrant logs or metrics to confirm when indexing finishes—once that happens, memory consumption should drop as intermediate data structures are freed.

### [Anchor](https://qdrant.tech/articles/indexing-optimization/\#5-re-enable-hnsw-post-ingestion) 5\. Re-enable HNSW post-ingestion

After the ingestion phase is over and memory usage has stabilized, re-enable HNSW for dense vectors by setting `m` back to a production value (commonly `16` or `32`):

```json
PATCH /collections/your_collection
{
  "hnsw_config": {
    "m": 16
  }
}

```

### [Anchor](https://qdrant.tech/articles/indexing-optimization/\#5-enable-quantization) 5\. Enable quantization

If you had planned to store all dense vectors on disk, be aware that searches can slow down drastically due to frequent disk I/O while memory pressure is high. A more balanced approach is **scalar quantization**: compress vectors (e.g., to `int8`) so they fit in RAM without occupying as much space as full floating-point values.

```json
PATCH /collections/your_collection
{
  "quantization_config": {
    "scalar": {
      "type": "int8",
      "always_ram": true
    }
  }
}

```

Quantized vectors remain **in-memory** yet consume less space, preserving much of the performance advantage of RAM-based search. Learn more about [vector quantization](https://qdrant.tech/articles/what-is-vector-quantization/).

### [Anchor](https://qdrant.tech/articles/indexing-optimization/\#conclusion) Conclusion

High-volume vector ingestion can place significant memory demands on Qdrant, especially if dense vectors are indexed in real time. By following these tips, you can substantially reduce the risk of out-of-memory errors and maintain stable performance in a memory-limited environment.

As always, monitor your system’s behavior. Review logs, watch metrics, and keep an eye on memory usage. Each workload is different, so it’s wise to fine-tune Qdrant’s parameters according to your hardware and data scale.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/indexing-optimization.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/indexing-optimization.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574479860&cv=11&fst=1748574479860&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Findexing-optimization%2F&hn=www.googleadservices.com&frm=0&tiba=Optimizing%20Memory%20for%20Bulk%20Uploads%20-%20Qdrant&npa=0&pscdl=noapi&auid=1311853558.1748574480&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574479832&cv=11&fst=1748574479832&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Findexing-optimization%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Optimizing%20Memory%20for%20Bulk%20Uploads%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1311853558.1748574480&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c992f7ed-bae7-466d-84f8-b19b9a2802e8&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0a09f718-c2e5-4174-a8fd-86177f35d6ad&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Findexing-optimization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c992f7ed-bae7-466d-84f8-b19b9a2802e8&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0a09f718-c2e5-4174-a8fd-86177f35d6ad&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Findexing-optimization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574480874&cv=11&fst=1748574480874&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Findexing-optimization%2F&hn=www.googleadservices.com&frm=0&tiba=Optimizing%20Memory%20for%20Bulk%20Uploads%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1311853558.1748574480&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)