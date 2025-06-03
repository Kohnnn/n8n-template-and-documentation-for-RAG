---
url: "https://qdrant.tech/articles/gridstore-key-value-storage/"
title: "Introducing Gridstore: Qdrant's Custom Key-Value Store - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Introducing Gridstore: Qdrant's Custom Key-Value Store

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)

# Introducing Gridstore: Qdrant's Custom Key-Value Store

Luis Cossio, Arnaud Gourlay & David Myriel

·

February 05, 2025

![Introducing Gridstore: Qdrant's Custom Key-Value Store](https://qdrant.tech/articles_data/gridstore-key-value-storage/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#why-we-built-our-own-storage-engine) Why We Built Our Own Storage Engine

Databases need a place to store and retrieve data. That’s what Qdrant’s [**key-value storage**](https://en.wikipedia.org/wiki/Key%e2%80%93value_database) does—it links keys to values.

When we started building Qdrant, we needed to pick something ready for the task. So we chose [**RocksDB**](https://rocksdb.org/) as our embedded key-value store.

![RocksDB](https://qdrant.tech/articles_data/gridstore-key-value-storage/rocksdb.jpg)

It is mature, reliable, and well-documented.

Over time, we ran into issues. Its architecture required compaction (uses [LSMT](https://en.wikipedia.org/wiki/Log-structured_merge-tree)), which caused random latency spikes. It handles generic keys, while we only use it for sequential IDs. Having lots of configuration options makes it versatile, but accurately tuning it was a headache. Finally, interoperating with C++ slowed us down (although we will still support it for quite some time 😭).

While there are already some good options written in Rust that we could leverage, we needed something custom. Nothing out there fit our needs in the way we wanted. We didn’t require generic keys. We wanted full control over when and which data was written and flushed. Our system already has crash recovery mechanisms built-in. Online compaction isn’t a priority, we already have optimizers for that. Debugging misconfigurations was not a great use of our time.

So we built our own storage. As of [**Qdrant Version 1.13**](https://qdrant.tech/blog/qdrant-1.13.x/), we are using Gridstore for **payload and sparse vector storages**.

![Gridstore](https://qdrant.tech/articles_data/gridstore-key-value-storage/gridstore.png)

Simple, efficient, and designed just for Qdrant.

#### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#in-this-article-youll-learn-about) In this article, you’ll learn about:

- **How Gridstore works** – a deep dive into its architecture and mechanics.
- **Why we built it this way** – the key design decisions that shaped it.
- **Rigorous testing** – how we ensured the new storage is production-ready.
- **Performance benchmarks** – official metrics that demonstrate its efficiency.

**Our first challenge?** Figuring out the best way to handle sequential keys and variable-sized data.

## [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#gridstore-architecture-three-main-components) Gridstore Architecture: Three Main Components

![gridstore](https://qdrant.tech/articles_data/gridstore-key-value-storage/gridstore-2.png)

Gridstore’s architecture is built around three key components that enable fast lookups and efficient space management:

| Component | Description |
| --- | --- |
| The Data Layer | Stores values in fixed-sized blocks and retrieves them using a pointer-based lookup system. |
| The Mask Layer | Uses a bitmask to track which blocks are in use and which are available. |
| The Gaps Layer | Manages block availability at a higher level, allowing for quick space allocation. |

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#1-the-data-layer-for-fast-retrieval) 1\. The Data Layer for Fast Retrieval

At the core of Gridstore is **The Data Layer**, which is designed to store and retrieve values quickly based on their keys. This layer allows us to do efficient reads and lets us store variable-sized data. The main two components of this layer are **The Tracker** and **The Data Grid**.

Since internal IDs are always sequential integers (0, 1, 2, 3, 4, …), the tracker is an array of pointers, where each pointer tells the system exactly where a value starts and how long it is.

![The Data Layer](https://qdrant.tech/articles_data/gridstore-key-value-storage/data-layer.png)

The Data Layer uses an array of pointers to quickly retrieve data.

This makes lookups incredibly fast. For example, finding key 3 is just a matter of jumping to the third position in the tracker, and following the pointer to find the value in the data grid.

However, because values are of variable size, the data itself is stored separately in a grid of fixed-sized blocks, which are grouped into larger page files. The fixed size of each block is usually 128 bytes. When inserting a value, Gridstore allocates one or more consecutive blocks to store it, ensuring that each block only holds data from a single value.

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#2-the-mask-layer-reuses-space) 2\. The Mask Layer Reuses Space

**The Mask Layer** helps Gridstore handle updates and deletions without the need for expensive data compaction. Instead of maintaining complex metadata for each block, Gridstore tracks usage with a bitmask, where each bit represents a block, with 1 for used, 0 for free.

![The Mask Layer](https://qdrant.tech/articles_data/gridstore-key-value-storage/mask-layer.png)

The bitmask efficiently tracks block usage.

This makes it easy to determine where new values can be written. When a value is removed, it gets soft-deleted at its pointer, and the corresponding blocks in the bitmask are marked as available. Similarly, when updating a value, the new version is written elsewhere, and the old blocks are freed at the bitmask.

This approach ensures that Gridstore doesn’t waste space. As the storage grows, however, scanning for available blocks in the entire bitmask can become computationally expensive.

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#3-the-gaps-layer-for-effective-updates) 3\. The Gaps Layer for Effective Updates

To further optimize update handling, Gridstore introduces **The Gaps Layer**, which provides a higher-level view of block availability.

Instead of scanning the entire bitmask, Gridstore splits the bitmask into regions and keeps track of the largest contiguous free space within each region, known as **The Region Gap**. By also storing the leading and trailing gaps of each region, the system can efficiently combine multiple regions when needed for storing large values.

![The Gaps Layer](https://qdrant.tech/articles_data/gridstore-key-value-storage/architecture.png)

The complete architecture of Gridstore

This layered approach allows Gridstore to locate available space quickly, scaling down the work required for scans while keeping memory overhead minimal. With this system, finding storage space for new values requires scanning only a tiny fraction of the total metadata, making updates and insertions highly efficient, even in large segments.

Given the default configuration, the gaps layer is scoped out in a millionth fraction of the actual storage size. This means that for each 1GB of data, the gaps layer only requires scanning 6KB of metadata. With this mechanism, the other operations can be executed in virtually constant-time complexity.

## [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#gridstore-in-production-maintaining-data-integrity) Gridstore in Production: Maintaining Data Integrity

![gridstore](https://qdrant.tech/articles_data/gridstore-key-value-storage/gridstore-1.png)

Gridstore’s architecture introduces multiple interdependent structures that must remain in sync to ensure data integrity:

- **The Data Layer** holds the data and associates each key with its location in storage, including page ID, block offset, and the size of its value.
- **The Mask Layer** keeps track of which blocks are occupied and which are free.
- **The Gaps Layer** provides an indexed view of free blocks for efficient space allocation.

Every time a new value is inserted or an existing value is updated, all these components need to be modified in a coordinated way.

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#when-things-break-in-real-life) When Things Break in Real Life

Real-world systems don’t operate in a vacuum. Failures happen: software bugs cause unexpected crashes, memory exhaustion forces processes to terminate, disks fail to persist data reliably, and power losses can interrupt operations at any moment.

_The critical question is: what happens if a failure occurs while updating these structures?_

If one component is updated but another isn’t, the entire system could become inconsistent. Worse, if an operation is only partially written to disk, it could lead to orphaned data, unusable space, or even data corruption.

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#stability-through-idempotency-recovering-with-wal) Stability Through Idempotency: Recovering With WAL

To guard against these risks, Qdrant relies on a [**Write-Ahead Log (WAL)**](https://qdrant.tech/documentation/concepts/storage/). Before committing an operation, Qdrant ensures that it is at least recorded in the WAL. If a crash happens before all updates are flushed, the system can safely replay operations from the log.

This recovery mechanism introduces another essential property: [**idempotence**](https://en.wikipedia.org/wiki/Idempotence).

The storage system must be designed so that reapplying the same operation after a failure leads to the same final state as if the operation had been applied just once.

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#the-grand-solution-lazy-updates) The Grand Solution: Lazy Updates

To achieve this, **Gridstore completes updates lazily**, prioritizing the most critical part of the write: the data itself.

|  |
| --- |
| 👉 Instead of immediately updating all metadata structures, it writes the new value first while keeping lightweight pending changes in a buffer. |
| 👉 The system only finalizes these updates when explicitly requested, ensuring that a crash never results in marking data as deleted before the update has been safely persisted. |
| 👉 In the worst-case scenario, Gridstore may need to write the same data twice, leading to a minor space overhead, but it will never corrupt the storage by overwriting valid data. |

## [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#how-we-tested-the-final-product) How We Tested the Final Product

![gridstore](https://qdrant.tech/articles_data/gridstore-key-value-storage/gridstore-3.png)

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#first-model-testing) First… Model Testing

Gridstore can be tested efficiently using model testing, which compares its behavior to a simple in-memory hash map. Since Gridstore should function like a persisted hash map, this method quickly detects inconsistencies.

The process is straightforward:

1. Initialize a Gridstore instance and an empty hash map.
2. Run random operations (put, delete, update) on both.
3. Verify that results match after each operation.
4. Compare all keys and values to ensure consistency.

This approach provides high test coverage, exposing issues like incorrect persistence or faulty deletions. Running large-scale model tests ensures Gridstore remains reliable in real-world use.

Here is a naive way to generate operations in Rust.

```rust

enum Operation {
    Put(PointOffset, Payload),
    Delete(PointOffset),
    Update(PointOffset, Payload),
}

impl Operation {
    fn random(rng: &mut impl Rng, max_point_offset: u32) -> Self {
        let point_offset = rng.random_range(0..=max_point_offset);
        let operation = rng.gen_range(0..3);
        match operation {
            0 => {
                let size_factor = rng.random_range(1..10);
                let payload = random_payload(rng, size_factor);
                Operation::Put(point_offset, payload)
            }
            1 => Operation::Delete(point_offset),
            2 => {
                let size_factor = rng.random_range(1..10);
                let payload = random_payload(rng, size_factor);
                Operation::Update(point_offset, payload)
            }
            _ => unreachable!(),
        }
    }
}

```

Model testing is a high-value way to catch bugs, especially when your system mimics a well-defined component like a hash map. If your component behaves the same as another one, using model testing brings a lot of value for a bit of effort.

We could have tested against RocksDB, but simplicity matters more. A simple hash map lets us run massive test sequences quickly, exposing issues faster.

For even sharper debugging, Property-Based Testing adds automated test generation and shrinking. It pinpoints failures with minimalized test cases, making bug hunting faster and more effective.

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#crash-testing-can-gridstore-handle-the-pressure) Crash Testing: Can Gridstore Handle the Pressure?

Designing for crash resilience is one thing, and proving it works under stress is another. To push Qdrant’s data integrity to the limit, we built [**Crasher**](https://github.com/qdrant/crasher), a test bench that brutally kills and restarts Qdrant while it handles a heavy update workload.

Crasher runs a loop that continuously writes data, then randomly crashes Qdrant. On each restart, Qdrant replays its [**Write-Ahead Log (WAL)**](https://qdrant.tech/documentation/concepts/storage/), and we verify if data integrity holds. Possible anomalies include:

- Missing data (points, vectors, or payloads)
- Corrupt payload values

This aggressive yet simple approach has uncovered real-world issues when run for extended periods. While we also use chaos testing for distributed setups, Crasher excels at fast, repeatable failure testing in a local environment.

## [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#testing-gridstore-performance-benchmarks) Testing Gridstore Performance: Benchmarks

![gridstore](https://qdrant.tech/articles_data/gridstore-key-value-storage/gridstore-4.png)

To measure the impact of our new storage engine, we used [**Bustle, a key-value storage benchmarking framework**](https://github.com/jonhoo/bustle), to compare Gridstore against RocksDB. We tested three workloads:

| Workload Type | Operation Distribution |
| --- | --- |
| Read-heavy | 95% reads |
| Insert-heavy | 80% inserts |
| Update-heavy | 50% updates |

#### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#the-results-speak-for-themselves) The results speak for themselves:

Average latency for all kinds of workloads is lower across the board, particularly for inserts.

![image.png](https://qdrant.tech/articles_data/gridstore-key-value-storage/1.png)

This shows a clear boost in performance. As we can see, the investment in Gridstore is paying off.

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#end-to-end-benchmarking) End-to-End Benchmarking

Now, let’s test the impact on a real Qdrant instance. So far, we’ve only integrated Gridstore for [**payloads**](https://qdrant.tech/documentation/concepts/payload/) and [**sparse vectors**](https://qdrant.tech/documentation/concepts/vectors/#sparse-vectors), but even this partial switch should show noticeable improvements.

For benchmarking, we used our in-house [**bfb tool**](https://github.com/qdrant/bfb) to generate a workload. Our configuration:

```json
bfb -n 2000000 --max-id 1000000 \
    --sparse-vectors 0.02 \
    --set-payload \
    --on-disk-payload \
    --dim 1 \
    --sparse-dim 5000 \
    --bool-payloads \
    --keywords 100 \
    --float-payloads true \
    --int-payloads 100000 \
    --text-payloads \
    --text-payload-length 512 \
    --skip-field-indices \
    --jsonl-updates ./rps.jsonl

```

This benchmark upserts 1 million points twice. Each point has:

- A medium to large payload
- A tiny dense vector (dense vectors use a different storage type)
- A sparse vector

* * *

#### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#additional-configuration) Additional configuration:

1. The test we conducted updated payload data separately in another request.

2. There were no payload indices, which ensured we measured pure ingestion speed.

3. Finally, we gathered request latency metrics for analysis.


* * *

We ran this against Qdrant 1.12.6, toggling between the old and new storage backends.

### [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#final-result) Final Result

Data ingestion is **twice as fast and with a smoother throughput** — a massive win! 😍

![image.png](https://qdrant.tech/articles_data/gridstore-key-value-storage/2.png)

We optimized for speed, and it paid off—but what about storage size?

- Gridstore: 2333MB
- RocksDB: 2319MB

Strictly speaking, RocksDB is slightly smaller, but the difference is negligible compared to the 2x faster ingestion and more stable throughput. A small trade-off for a big performance gain!

## [Anchor](https://qdrant.tech/articles/gridstore-key-value-storage/\#trying-out-gridstore) Trying Out Gridstore

Gridstore represents a significant advancement in how Qdrant manages its **key-value storage** needs. It offers great performance and streamlined updates tailored specifically for our use case. We have managed to achieve faster, more reliable data ingestion while maintaining data integrity, even under heavy workloads and unexpected failures. It is already used as a storage backend for on-disk payloads and sparse vectors.

👉 It’s important to note that Gridstore remains tightly integrated with Qdrant and, as such, has not been released as a standalone crate.

Its API is still evolving, and we are focused on refining it within our ecosystem to ensure maximum stability and performance. That said, we recognize the value this innovation could bring to the wider Rust community. In the future, once the API stabilizes and we decouple it enough from Qdrant, we will consider publishing it as a contribution to the community ❤️.

For now, Gridstore continues to drive improvements in Qdrant, demonstrating the benefits of a custom-tailored storage engine designed with modern demands in mind. Stay tuned for further updates and potential community releases as we keep pushing the boundaries of performance and reliability.

![Gridstore](https://qdrant.tech/articles_data/gridstore-key-value-storage/gridstore.png)

Simple, efficient, and designed just for Qdrant.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/gridstore-key-value-storage.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/gridstore-key-value-storage.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=23b71bd9-8992-4325-837b-a7cf417d5ecc&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ee46b310-a501-44fd-ad99-058f1449bcd5&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fgridstore-key-value-storage%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573935631&cv=11&fst=1748573935631&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fgridstore-key-value-storage%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Gridstore%3A%20Qdrant's%20Custom%20Key-Value%20Store%20-%20Qdrant&npa=0&pscdl=noapi&auid=480884409.1748573935&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573935612&cv=11&fst=1748573935612&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fgridstore-key-value-storage%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Gridstore%3A%20Qdrant's%20Custom%20Key-Value%20Store%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=480884409.1748573935&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573935789&cv=11&fst=1748573935789&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fgridstore-key-value-storage%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Introducing%20Gridstore%3A%20Qdrant's%20Custom%20Key-Value%20Store%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=480884409.1748573935&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=23b71bd9-8992-4325-837b-a7cf417d5ecc&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ee46b310-a501-44fd-ad99-058f1449bcd5&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fgridstore-key-value-storage%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)