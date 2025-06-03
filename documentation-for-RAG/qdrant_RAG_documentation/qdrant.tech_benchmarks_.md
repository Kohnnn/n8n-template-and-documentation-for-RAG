---
url: "https://qdrant.tech/benchmarks/"
title: "Vector Database Benchmarks - Qdrant"
---

# Vector Database Benchmarks

# [Anchor](https://qdrant.tech/benchmarks/\#benchmarking-vector-databases) Benchmarking Vector Databases

At Qdrant, performance is the top-most priority. We always make sure that we use system resources efficiently so you get the **fastest and most accurate results at the cheapest cloud costs**. So all of our decisions from [choosing Rust](https://qdrant.tech/articles/why-rust/), [io optimisations](https://qdrant.tech/articles/io_uring/), [serverless support](https://qdrant.tech/articles/serverless/), [binary quantization](https://qdrant.tech/articles/binary-quantization/), to our [fastembed library](https://qdrant.tech/articles/fastembed/) are all based on our principle. In this article, we will compare how Qdrant performs against the other vector search engines.

Here are the principles we followed while designing these benchmarks:

- We do comparative benchmarks, which means we focus on **relative numbers** rather than absolute numbers.
- We use affordable hardware, so that you can reproduce the results easily.
- We run benchmarks on the same exact machines to avoid any possible hardware bias.
- All the benchmarks are [open-sourced](https://github.com/qdrant/vector-db-benchmark), so you can contribute and improve them.

Scenarios we tested

1. Upload & Search benchmark on single node [Benchmark](https://qdrant.tech/benchmarks/single-node-speed-benchmark/)
2. Filtered search benchmark - [Benchmark](https://qdrant.tech/benchmarks/#filtered-search-benchmark)
3. Memory consumption benchmark - Coming soon
4. Cluster mode benchmark - Coming soon

Some of our experiment design decisions are described in the [F.A.Q Section](https://qdrant.tech/benchmarks/#benchmarks-faq).
Reach out to us on our [Discord channel](https://qdrant.to/discord) if you want to discuss anything related Qdrant or these benchmarks.

## [Anchor](https://qdrant.tech/benchmarks/\#single-node-benchmarks) Single node benchmarks

We benchmarked several vector databases using various configurations of them on different datasets to check how the results may vary. Those datasets may have different vector dimensionality but also vary in terms of the distance function being used. We also tried to capture the difference we can expect while using some different configuration parameters, for both the engine itself and the search operation separately.

**Updated: January/June 2024**

Dataset:dbpedia-openai-1M-1536-angulardeep-image-96-angulargist-960-euclideanglove-100-angular

Search threads:1001

Plot values:

RPS

Latency

p95 latency

Index time

| Engine | Setup | Dataset | Upload Time(m) | Upload + Index Time(m) | Latency(ms) | P95(ms) | P99(ms) | RPS | Precision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| qdrant | qdrant-sq-rps-m-64-ef-512 | dbpedia-openai-1M-1536-angular | 3.51 | 24.43 | 3.54 | 4.95 | 8.62 | 1238.0016 | 0.99 |
| weaviate | latest-weaviate-m32 | dbpedia-openai-1M-1536-angular | 13.94 | 13.94 | 4.99 | 7.16 | 11.33 | 1142.13 | 0.97 |
| elasticsearch | elasticsearch-m-32-ef-128 | dbpedia-openai-1M-1536-angular | 19.18 | 83.72 | 22.10 | 72.53 | 135.68 | 716.80 | 0.98 |
| redis | redis-m-32-ef-256 | dbpedia-openai-1M-1536-angular | 92.49 | 92.49 | 140.65 | 160.85 | 167.35 | 625.27 | 0.97 |
| milvus | milvus-m-16-ef-128 | dbpedia-openai-1M-1536-angular | 0.27 | 1.16 | 393.31 | 441.32 | 576.65 | 219.11 | 0.99 |

_Download raw data: [here](https://qdrant.tech/benchmarks/results-1-100-thread-2024-06-15.json)_

## [Anchor](https://qdrant.tech/benchmarks/\#observations) Observations

Most of the engines have improved since [our last run](https://qdrant.tech/benchmarks/single-node-speed-benchmark-2022/). Both life and software have trade-offs but some clearly do better:

- **`Qdrant` achives highest RPS and lowest latencies in almost all the scenarios, no matter the precision threshold and the metric we choose.** It has also shown 4x RPS gains on one of the datasets.
- `Elasticsearch` has become considerably fast for many cases but it’s very slow in terms of indexing time. It can be 10x slower when storing 10M+ vectors of 96 dimensions! (32mins vs 5.5 hrs)
- `Milvus` is the fastest when it comes to indexing time and maintains good precision. However, it’s not on-par with others when it comes to RPS or latency when you have higher dimension embeddings or more number of vectors.
- `Redis` is able to achieve good RPS but mostly for lower precision. It also achieved low latency with single thread, however its latency goes up quickly with more parallel requests. Part of this speed gain comes from their custom protocol.
- `Weaviate` has improved the least since our last run.

## [Anchor](https://qdrant.tech/benchmarks/\#how-to-read-the-results) How to read the results

- Choose the dataset and the metric you want to check.
- Select a precision threshold that would be satisfactory for your usecase. This is important because ANN search is all about trading precision for speed. This means in any vector search benchmark, **two results must be compared only when you have similar precision**. However most benchmarks miss this critical aspect.
- The table is sorted by the value of the selected metric (RPS / Latency / p95 latency / Index time), and the first entry is always the winner of the category 🏆

### [Anchor](https://qdrant.tech/benchmarks/\#latency-vs-rps) Latency vs RPS

In our benchmark we test two main search usage scenarios that arise in practice.

- **Requests-per-Second (RPS)**: Serve more requests per second in exchange of individual requests taking longer (i.e. higher latency). This is a typical scenario for a web application, where multiple users are searching at the same time.
To simulate this scenario, we run client requests in parallel with multiple threads and measure how many requests the engine can handle per second.
- **Latency**: React quickly to individual requests rather than serving more requests in parallel. This is a typical scenario for applications where server response time is critical. Self-driving cars, manufacturing robots, and other real-time systems are good examples of such applications.
To simulate this scenario, we run client in a single thread and measure how long each request takes.

### [Anchor](https://qdrant.tech/benchmarks/\#tested-datasets) Tested datasets

Our [benchmark tool](https://github.com/qdrant/vector-db-benchmark) is inspired by [github.com/erikbern/ann-benchmarks](https://github.com/erikbern/ann-benchmarks/). We used the following datasets to test the performance of the engines on ANN Search tasks:

| Datasets | \# Vectors | Dimensions | Distance |
| --- | --- | --- | --- |
| [dbpedia-openai-1M-angular](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M) | 1M | 1536 | cosine |
| [deep-image-96-angular](http://sites.skoltech.ru/compvision/noimi/) | 10M | 96 | cosine |
| [gist-960-euclidean](http://corpus-texmex.irisa.fr/) | 1M | 960 | euclidean |
| [glove-100-angular](https://nlp.stanford.edu/projects/glove/) | 1.2M | 100 | cosine |

### [Anchor](https://qdrant.tech/benchmarks/\#setup) Setup

![Benchmarks configuration](https://qdrant.tech/benchmarks/client-server.png)

Benchmarks configuration

- This was our setup for this experiment:
  - Client: 8 vcpus, 16 GiB memory, 64GiB storage ( `Standard D8ls v5` on Azure Cloud)
  - Server: 8 vcpus, 32 GiB memory, 64GiB storage ( `Standard D8s v3` on Azure Cloud)
- The Python client uploads data to the server, waits for all required indexes to be constructed, and then performs searches with configured number of threads. We repeat this process with different configurations for each engine, and then select the best one for a given precision.
- We ran all the engines in docker and limited their memory to 25GB. This was used to ensure fairness by avoiding the case of some engine configs being too greedy with RAM usage. This 25 GB limit is completely fair because even to serve the largest `dbpedia-openai-1M-1536-angular` dataset, one hardly needs `1M * 1536 * 4bytes * 1.5 = 8.6GB` of RAM (including vectors + index). Hence, we decided to provide all the engines with ~3x the requirement.

Please note that some of the configs of some engines crashed on some datasets because of the 25 GB memory limit. That’s why you might see fewer points for some engines on choosing higher precision thresholds.

# [Anchor](https://qdrant.tech/benchmarks/\#filtered-search-benchmark) Filtered search benchmark

Applying filters to search results brings a whole new level of complexity.
It is no longer enough to apply one algorithm to plain data. With filtering, it becomes a matter of the _cross-integration_ of the different indices.

To measure how well different search engines perform in this scenario, we have prepared a set of **Filtered ANN Benchmark Datasets** -
[https://github.com/qdrant/ann-filtering-benchmark-datasets](https://github.com/qdrant/ann-filtering-benchmark-datasets)

It is similar to the ones used in the [ann-benchmarks project](https://github.com/erikbern/ann-benchmarks/) but enriched with payload metadata and pre-generated filtering requests. It includes synthetic and real-world datasets with various filters, from keywords to geo-spatial queries.

### [Anchor](https://qdrant.tech/benchmarks/\#why-filtering-is-not-trivial) Why filtering is not trivial?

Not many ANN algorithms are compatible with filtering.
HNSW is one of the few of them, but search engines approach its integration in different ways:

- Some use **post-filtering**, which applies filters after ANN search. It doesn’t scale well as it either loses results or requires many candidates on the first stage.
- Others use **pre-filtering**, which requires a binary mask of the whole dataset to be passed into the ANN algorithm. It is also not scalable, as the mask size grows linearly with the dataset size.

On top of it, there is also a problem with search accuracy.
It appears if too many vectors are filtered out, so the HNSW graph becomes disconnected.

Qdrant uses a different approach, not requiring pre- or post-filtering while addressing the accuracy problem.
Read more about the Qdrant approach in our [Filtrable HNSW](https://qdrant.tech/articles/filtrable-hnsw/) article.

## [Anchor](https://qdrant.tech/benchmarks/\#)

**Updated: Feb 2023**

Dataset:keyword-100range-100int-2048100-kw-small-vocabkeyword-2048geo-radius-100range-2048geo-radius-2048int-100h-and-m-2048arxiv-titles-384

Plot values:

Regular search

Filter search

_Download raw data: [here](https://qdrant.tech/benchmarks/filter-result-2023-02-03.json)_

## [Anchor](https://qdrant.tech/benchmarks/\#filtered-results) Filtered Results

As you can see from the charts, there are three main patterns:

- **Speed boost** \- for some engines/queries, the filtered search is faster than the unfiltered one. It might happen if the filter is restrictive enough, to completely avoid the usage of the vector index.

- **Speed downturn** \- some engines struggle to keep high RPS, it might be related to the requirement of building a filtering mask for the dataset, as described above.

- **Accuracy collapse** \- some engines are loosing accuracy dramatically under some filters. It is related to the fact that the HNSW graph becomes disconnected, and the search becomes unreliable.


Qdrant avoids all these problems and also benefits from the speed boost, as it implements an advanced [query planning strategy](https://qdrant.tech/documentation/search/#query-planning).

# [Anchor](https://qdrant.tech/benchmarks/\#benchmarks-faq) Benchmarks F.A.Q.

## [Anchor](https://qdrant.tech/benchmarks/\#are-we-biased) Are we biased?

Probably, yes. Even if we try to be objective, we are not experts in using all the existing vector databases.
We build Qdrant and know the most about it.
Due to that, we could have missed some important tweaks in different vector search engines.

However, we tried our best, kept scrolling the docs up and down, experimented with combinations of different configurations, and gave all of them an equal chance to stand out. If you believe you can do it better than us, our **benchmarks are fully [open-sourced](https://github.com/qdrant/vector-db-benchmark), and contributions are welcome**!

## [Anchor](https://qdrant.tech/benchmarks/\#what-do-we-measure) What do we measure?

There are several factors considered while deciding on which database to use.
Of course, some of them support a different subset of functionalities, and those might be a key factor to make the decision.
But in general, we all care about the search precision, speed, and resources required to achieve it.

There is one important thing - **the speed of the vector databases should to be compared only if they achieve the same precision**. Otherwise, they could maximize the speed factors by providing inaccurate results, which everybody would rather avoid. Thus, our benchmark results are compared only at a specific search precision threshold.

## [Anchor](https://qdrant.tech/benchmarks/\#how-we-select-hardware) How we select hardware?

In our experiments, we are not focusing on the absolute values of the metrics but rather on a relative comparison of different engines.
What is important is the fact we used the same machine for all the tests.
It was just wiped off between launching different engines.

We selected an average machine, which you can easily rent from almost any cloud provider. No extra quota or custom configuration is required.

## [Anchor](https://qdrant.tech/benchmarks/\#why-you-are-not-comparing-with-faiss-or-annoy) Why you are not comparing with FAISS or Annoy?

Libraries like FAISS provide a great tool to do experiments with vector search. But they are far away from real usage in production environments.
If you are using FAISS in production, in the best case, you never need to update it in real-time. In the worst case, you have to create your custom wrapper around it to support CRUD, high availability, horizontal scalability, concurrent access, and so on.

Some vector search engines even use FAISS under the hood, but a search engine is much more than just an indexing algorithm.

We do, however, use the same benchmark datasets as the famous [ann-benchmarks project](https://github.com/erikbern/ann-benchmarks), so you can align your expectations for any practical reasons.

### [Anchor](https://qdrant.tech/benchmarks/\#why-we-decided-to-test-with-the-python-client) Why we decided to test with the Python client

There is no consensus when it comes to the best technology to run benchmarks. You’re free to choose Go, Java or Rust-based systems. But there are two main reasons for us to use Python for this:

1. While generating embeddings you’re most likely going to use Python and python based ML frameworks.
2. Based on GitHub stars, python clients are one of the most popular clients across all the engines.

From the user’s perspective, the crucial thing is the latency perceived while using a specific library - in most cases a Python client.
Nobody can and even should redefine the whole technology stack, just because of using a specific search tool.
That’s why we decided to focus primarily on official Python libraries, provided by the database authors.
Those may use some different protocols under the hood, but at the end of the day, we do not care how the data is transferred, as long as it ends up in the target location.

## [Anchor](https://qdrant.tech/benchmarks/\#what-about-closed-source-saas-platforms) What about closed-source SaaS platforms?

There are some vector databases available as SaaS only so that we couldn’t test them on the same machine as the rest of the systems.
That makes the comparison unfair. That’s why we purely focused on testing the Open Source vector databases, so everybody may reproduce the benchmarks easily.

This is not the final list, and we’ll continue benchmarking as many different engines as possible.

## [Anchor](https://qdrant.tech/benchmarks/\#how-to-reproduce-the-benchmark) How to reproduce the benchmark?

The source code is available on [Github](https://github.com/qdrant/vector-db-benchmark) and has a `README.md` file describing the process of running the benchmark for a specific engine.

## [Anchor](https://qdrant.tech/benchmarks/\#how-to-contribute) How to contribute?

We made the benchmark Open Source because we believe that it has to be transparent. We could have misconfigured one of the engines or just done it inefficiently. If you feel like you could help us out, check out our [benchmark repository](https://github.com/qdrant/vector-db-benchmark).

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574742809&cv=11&fst=1748574742809&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2F&hn=www.googleadservices.com&frm=0&tiba=Vector%20Database%20Benchmarks%20-%20Qdrant&npa=0&pscdl=noapi&auid=1634942675.1748574743&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574742778&cv=11&fst=1748574742778&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Vector%20Database%20Benchmarks%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1634942675.1748574743&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b56dd30f-c210-43be-b18f-74f8188dd703&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3bbe9f0c-1100-44a6-b023-c5198bd3c98c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b56dd30f-c210-43be-b18f-74f8188dd703&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3bbe9f0c-1100-44a6-b023-c5198bd3c98c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574743828&cv=11&fst=1748574743828&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2F&hn=www.googleadservices.com&frm=0&tiba=Vector%20Database%20Benchmarks%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1634942675.1748574743&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)