---
url: "https://qdrant.tech/articles/immutable-data-structures/"
title: "Qdrant Internals: Immutable Data Structures - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Qdrant Internals: Immutable Data Structures

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)

# Qdrant Internals: Immutable Data Structures

Andrey Vasnetsov

·

August 20, 2024

![Qdrant Internals: Immutable Data Structures](https://qdrant.tech/articles_data/immutable-data-structures/preview/title.jpg)

## [Anchor](https://qdrant.tech/articles/immutable-data-structures/\#data-structures-101) Data Structures 101

Those who took programming courses might remember that there is no such thing as a universal data structure.
Some structures are good at accessing elements by index (like arrays), while others shine in terms of insertion efficiency (like linked lists).

![Hardware-optimized data structure](https://qdrant.tech/articles_data/immutable-data-structures/hardware-optimized.png)

Hardware-optimized data structure

However, when we move from theoretical data structures to real-world systems, and particularly in performance-critical areas such as [vector search](https://qdrant.tech/use-cases/), things become more complex. [Big-O notation](https://en.wikipedia.org/wiki/Big_O_notation) provides a good abstraction, but it doesn’t account for the realities of modern hardware: cache misses, memory layout, disk I/O, and other low-level considerations that influence actual performance.

> From the perspective of hardware efficiency, the ideal data structure is a contiguous array of bytes that can be read sequentially in a single thread. This scenario allows hardware optimizations like prefetching, caching, and branch prediction to operate at their best.

However, real-world use cases require more complex structures to perform various operations like insertion, deletion, and search.
These requirements increase complexity and introduce performance trade-offs.

### [Anchor](https://qdrant.tech/articles/immutable-data-structures/\#mutability) Mutability

One of the most significant challenges when working with data structures is ensuring **mutability — the ability to change the data structure after it’s created**, particularly with fast update operations.

Let’s consider a simple example: we want to iterate over items in sorted order.
Without a mutability requirement, we can use a simple array and sort it once.
This is very close to our ideal scenario. We can even put the structure on disk - which is trivial for an array.

However, if we need to insert an item into this array, **things get more complicated**.
Inserting into a sorted array requires shifting all elements after the insertion point, which leads to linear time complexity for each insertion, which is not acceptable for many applications.

To handle such cases, more complex structures like [B-trees](https://en.wikipedia.org/wiki/B-tree) come into play. B-trees are specifically designed to optimize both insertion and read operations for large data sets. However, they sacrifice the raw speed of array reads for better insertion performance.

Here’s a benchmark that illustrates the difference between iterating over a plain array and a BTreeSet in Rust:

```rust
use std::collections::BTreeSet;
use rand::Rng;

fn main() {
    // Benchmark plain vector VS btree in a task of iteration over all elements
    let mut rand = rand::thread_rng();
    let vector: Vec<_> = (0..1000000).map(|_| rand.gen::<u64>()).collect();
    let btree: BTreeSet<_> = vector.iter().copied().collect();

    {
        let mut sum = 0;
        for el in vector {
            sum += el;
        }
    } // Elapsed: 850.924µs

    {
        let mut sum = 0;
        for el in btree {
            sum += el;
        }
    } // Elapsed: 5.213025ms, ~6x slower

}

```

[Vector databases](https://qdrant.tech/), like Qdrant, have to deal with a large variety of data structures.
If we could make them immutable, it would significantly improve performance and optimize memory usage.

## [Anchor](https://qdrant.tech/articles/immutable-data-structures/\#how-does-immutability-help) How Does Immutability Help?

A large part of the immutable advantage comes from the fact that we know the exact data we need to put into the structure even before we start building it.
The simplest example is a sorted array: we would know exactly how many elements we have to put into the array so we can allocate the exact amount of memory once.

More complex data structures might require additional statistics to be collected before the structure is built.
A Qdrant-related example of this is [Scalar Quantization](https://qdrant.tech/articles/scalar-quantization/#conversion-to-integers): in order to select proper quantization levels, we have to know the distribution of the data.

![Scalar Quantization Quantile](https://qdrant.tech/articles_data/immutable-data-structures/quantization-quantile.png)

Scalar Quantization Quantile

Computing this distribution requires knowing all the data in advance, but once we have it, applying scalar quantization is a simple operation.

Let’s take a look at a non-exhaustive list of data structures and potential improvements we can get from making them immutable:

| Function | Mutable Data Structure | Immutable Alternative | Potential improvements |
| --- | --- | --- | --- |
| Read by index | Array | Fixed chunk of memory | Allocate exact amount of memory |
| Vector Storage | Array or Arrays | Memory-mapped file | Offload data to disk |
| Read sorted ranges | B-Tree | Sorted Array | Store all data close, avoid cache misses |
| Read by key | Hash Map | Hash Map with Perfect Hashing | Avoid hash collisions |
| Get documents by keyword | Inverted Index | Inverted Index with Sorted<br>and BitPacked Postings | Less memory usage, faster search |
| Vector Search | HNSW graph | HNSW graph with<br>payload-aware connections | Better precision with filters |
| Tenant Isolation | Vector Storage | Defragmented Vector Storage | Faster access to on-disk data |

For more info on payload-aware connections in HNSW, read our [previous article](https://qdrant.tech/articles/filtrable-hnsw/).

This time around, we will focus on the latest additions to Qdrant:

- **the immutable hash map with perfect hashing**
- **defragmented vector storage**.

### [Anchor](https://qdrant.tech/articles/immutable-data-structures/\#perfect-hashing) Perfect Hashing

A hash table is one of the most commonly used data structures implemented in almost every programming language, including Rust.
It provides fast access to elements by key, with an average time complexity of O(1) for read and write operations.

There is, however, the assumption that should be satisfied for the hash table to work efficiently: _hash collisions should not cause too much overhead_.
In a hash table, each key is mapped to a “bucket,” a slot where the value is stored.
When different keys map to the same bucket, a collision occurs.

In regular mutable hash tables, minimization of collisions is achieved by:

- making the number of buckets bigger so the probability of collision is lower
- using a linked list or a tree to store multiple elements with the same hash

However, these strategies have overheads, which become more significant if we consider using high-latency storage like disk.

Indeed, every read operation from disk is several orders of magnitude slower than reading from RAM, so we want to know the correct location of the data from the first attempt.

In order to achieve this, we can use a so-called minimal perfect hash function (MPHF).
This special type of hash function is constructed specifically for a given set of keys, and it guarantees no collisions while using minimal amount of buckets.

In Qdrant, we decided to use _fingerprint-based minimal perfect hash function_ implemented in the [ph crate 🦀](https://crates.io/crates/ph) by [Piotr Beling](https://dl.acm.org/doi/10.1145/3596453).
According to our benchmarks, using the perfect hash function does introduce some overhead in terms of hashing time, but it significantly reduces the time for the whole operation:

| Volume | `ph::Function` | `std::hash::Hash` | `HashMap::get` |
| --- | --- | --- | --- |
| 1000 | 60ns | ~20ns | 34ns |
| 100k | 90ns | ~20ns | 220ns |
| 10M | 238ns | ~20ns | 500ns |

Even thought the absolute time for hashing is higher, the time for the whole operation is lower, because PHF guarantees no collisions.
The difference is even more significant when we consider disk read time, which
might up to several milliseconds (10^6 ns).

PHF RAM size scales linearly for `ph::Function`: 3.46 kB for 10k elements, 119MB for 350M elements.
The construction time required to build the hash function is surprisingly low, and we only need to do it once:

| Volume | `ph::Function` (construct) | PHF size | Size of int64 keys (for reference) |
| --- | --- | --- | --- |
| 1M | 52ms | 0.34Mb | 7.62Mb |
| 100M | 7.4s | 33.7Mb | 762.9Mb |

The usage of PHF in Qdrant lets us minimize the latency of cold reads, which is especially important for large-scale multi-tenant systems. With PHF, it is enough to read a single page from a disk to get the exact location of the data.

### [Anchor](https://qdrant.tech/articles/immutable-data-structures/\#defragmentation) Defragmentation

When you read data from a disk, you almost never read a single byte. Instead, you read a page, which is a fixed-size chunk of data.
On many systems, the page size is 4KB, which means that every read operation will read 4KB of data, even if you only need a single byte.

Vector search, on the other hand, requires reading a lot of small vectors, which might create a large overhead.
It is especially noticeable if we use binary quantization, where the size of even large OpenAI 1536d vectors is compressed down to **192 bytes**.

![Overhead when reading a single vector](https://qdrant.tech/articles_data/immutable-data-structures/page-vector.png)

Overhead when reading single vector

That means if the vectors we access during the search are randomly scattered across the disk, we will have to read 4KB for each vector, which is 20 times more than the actual data size.

There is, however, a simple way to avoid this overhead: **defragmentation**.
If we knew some additional information about the data, we could combine all relevant vectors into a single page.

![Defragmentation](https://qdrant.tech/articles_data/immutable-data-structures/defragmentation.png)

Defragmentation

This additional information is available to Qdrant via the [payload index](https://qdrant.tech/documentation/concepts/indexing/#payload-index).

By specifying the payload index, which is going to be used for filtering most of the time, we can put all vectors with the same payload together.
This way, reading a single page will also read nearby vectors, which will be used in the search.

This approach is especially efficient for [multi-tenant systems](https://qdrant.tech/documentation/guides/multiple-partitions/), where only a small subset of vectors is actively used for search.
The capacity of such a deployment is typically defined by the size of the hot subset, which is much smaller than the total number of vectors.

> Grouping relevant vectors together allows us to optimize the size of the hot subset by avoiding caching of irrelevant data.
> The following benchmark data compares RPS for defragmented and non-defragmented storage:

| % of hot subset | Tenant Size (vectors) | RPS, Non-defragmented | RPS, Defragmented |
| --- | --- | --- | --- |
| 2.5% | 50k | 1.5 | 304 |
| 12.5% | 50k | 0.47 | 279 |
| 25% | 50k | 0.4 | 63 |
| 50% | 50k | 0.3 | 8 |
| 2.5% | 5k | 56 | 490 |
| 12.5% | 5k | 5.8 | 488 |
| 25% | 5k | 3.3 | 490 |
| 50% | 5k | 3.1 | 480 |
| 75% | 5k | 2.9 | 130 |
| 100% | 5k | 2.7 | 95 |

**Dataset size:** 2M 768d vectors (~6Gb Raw data), binary quantization, 650Mb of RAM limit.
All benchmarks are made with minimal RAM allocation to demonstrate disk cache efficiency.

As you can see, the biggest impact is on the small tenant size, where defragmentation allows us to achieve **100x more RPS**.
Of course, the real-world impact of defragmentation depends on the specific workload and the size of the hot subset, but enabling this feature can significantly improve the performance of Qdrant.

Please find more details on how to enable defragmentation in the [indexing documentation](https://qdrant.tech/documentation/concepts/indexing/#tenant-index).

## [Anchor](https://qdrant.tech/articles/immutable-data-structures/\#updating-immutable-data-structures) Updating Immutable Data Structures

One may wonder how Qdrant allows updating collection data if everything is immutable.
Indeed, [Qdrant API](https://api.qdrant.tech/) allows the change of any vector or payload at any time, so from the user’s perspective, the whole collection is mutable at any time.

As it usually happens with every decent magic trick, the secret is disappointingly simple: not all data in Qdrant is immutable.
In Qdrant, storage is divided into segments, which might be either mutable or immutable.
New data is always written to the mutable segment, which is later converted to the immutable one by the optimization process.

![Optimization process](https://qdrant.tech/articles_data/immutable-data-structures/optimization.png)

Optimization process

If we need to update the data in the immutable or currenly optimized segment, instead of changing the data in place, we perform a copy-on-write operation, move the data to the mutable segment, and update it there.

Data in the original segment is marked as deleted, and later vacuumed by the optimization process.

## [Anchor](https://qdrant.tech/articles/immutable-data-structures/\#downsides-and-how-to-compensate) Downsides and How to Compensate

While immutable data structures are great for read-heavy operations, they come with trade-offs:

- **Higher update costs:** Immutable structures are less efficient for updates. The amortized time complexity might be the same as mutable structures, but the constant factor is higher.
- **Rebuilding overhead:** In some cases, we may need to rebuild indices or structures for the same data more than once.
- **Read-heavy workloads:** Immutability assumes a search-heavy workload, which is typical for search engines but not for all applications.

In Qdrant, we mitigate these downsides by allowing the user to adapt the system to their specific workload.
For example, changing the default size of the segment might help to reduce the overhead of rebuilding indices.

In extreme cases, multi-segment storage can act as a single segment, falling back to the mutable data structure when needed.

## [Anchor](https://qdrant.tech/articles/immutable-data-structures/\#conclusion) Conclusion

Immutable data structures, while tricky to implement correctly, offer significant performance gains, especially for read-heavy systems like search engines. They allow us to take full advantage of hardware optimizations, reduce memory overhead, and improve cache performance.

In Qdrant, the combination of techniques like perfect hashing and defragmentation brings further benefits, making our vector search operations faster and more efficient. While there are trade-offs, the flexibility of Qdrant’s architecture — including segment-based storage — allows us to balance the best of both worlds.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/immutable-data-structures.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/immutable-data-structures.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575331090&cv=11&fst=1748575331090&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fimmutable-data-structures%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Internals%3A%20Immutable%20Data%20Structures%20-%20Qdrant&npa=0&pscdl=noapi&auid=78873952.1748575331&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575331053&cv=11&fst=1748575331053&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fimmutable-data-structures%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Internals%3A%20Immutable%20Data%20Structures%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=78873952.1748575331&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0b0ecd42-a454-4deb-9be5-e207e97ed138&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=727e3308-36b9-46a4-a058-11a062859e92&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fimmutable-data-structures%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0b0ecd42-a454-4deb-9be5-e207e97ed138&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=727e3308-36b9-46a4-a058-11a062859e92&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fimmutable-data-structures%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575332268&cv=11&fst=1748575332268&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fimmutable-data-structures%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Internals%3A%20Immutable%20Data%20Structures%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=78873952.1748575331&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)