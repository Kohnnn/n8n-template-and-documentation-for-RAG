---
url: "https://qdrant.tech/benchmarks/single-node-speed-benchmark/"
title: "Single node benchmarks - Qdrant"
---

# Single node benchmarks

August 23, 2022

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

## [Anchor](https://qdrant.tech/benchmarks/single-node-speed-benchmark/\#observations) Observations

Most of the engines have improved since [our last run](https://qdrant.tech/benchmarks/single-node-speed-benchmark-2022/). Both life and software have trade-offs but some clearly do better:

- **`Qdrant` achives highest RPS and lowest latencies in almost all the scenarios, no matter the precision threshold and the metric we choose.** It has also shown 4x RPS gains on one of the datasets.
- `Elasticsearch` has become considerably fast for many cases but it’s very slow in terms of indexing time. It can be 10x slower when storing 10M+ vectors of 96 dimensions! (32mins vs 5.5 hrs)
- `Milvus` is the fastest when it comes to indexing time and maintains good precision. However, it’s not on-par with others when it comes to RPS or latency when you have higher dimension embeddings or more number of vectors.
- `Redis` is able to achieve good RPS but mostly for lower precision. It also achieved low latency with single thread, however its latency goes up quickly with more parallel requests. Part of this speed gain comes from their custom protocol.
- `Weaviate` has improved the least since our last run.

## [Anchor](https://qdrant.tech/benchmarks/single-node-speed-benchmark/\#how-to-read-the-results) How to read the results

- Choose the dataset and the metric you want to check.
- Select a precision threshold that would be satisfactory for your usecase. This is important because ANN search is all about trading precision for speed. This means in any vector search benchmark, **two results must be compared only when you have similar precision**. However most benchmarks miss this critical aspect.
- The table is sorted by the value of the selected metric (RPS / Latency / p95 latency / Index time), and the first entry is always the winner of the category 🏆

### [Anchor](https://qdrant.tech/benchmarks/single-node-speed-benchmark/\#latency-vs-rps) Latency vs RPS

In our benchmark we test two main search usage scenarios that arise in practice.

- **Requests-per-Second (RPS)**: Serve more requests per second in exchange of individual requests taking longer (i.e. higher latency). This is a typical scenario for a web application, where multiple users are searching at the same time.
To simulate this scenario, we run client requests in parallel with multiple threads and measure how many requests the engine can handle per second.
- **Latency**: React quickly to individual requests rather than serving more requests in parallel. This is a typical scenario for applications where server response time is critical. Self-driving cars, manufacturing robots, and other real-time systems are good examples of such applications.
To simulate this scenario, we run client in a single thread and measure how long each request takes.

### [Anchor](https://qdrant.tech/benchmarks/single-node-speed-benchmark/\#tested-datasets) Tested datasets

Our [benchmark tool](https://github.com/qdrant/vector-db-benchmark) is inspired by [github.com/erikbern/ann-benchmarks](https://github.com/erikbern/ann-benchmarks/). We used the following datasets to test the performance of the engines on ANN Search tasks:

| Datasets | \# Vectors | Dimensions | Distance |
| --- | --- | --- | --- |
| [dbpedia-openai-1M-angular](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M) | 1M | 1536 | cosine |
| [deep-image-96-angular](http://sites.skoltech.ru/compvision/noimi/) | 10M | 96 | cosine |
| [gist-960-euclidean](http://corpus-texmex.irisa.fr/) | 1M | 960 | euclidean |
| [glove-100-angular](https://nlp.stanford.edu/projects/glove/) | 1.2M | 100 | cosine |

### [Anchor](https://qdrant.tech/benchmarks/single-node-speed-benchmark/\#setup) Setup

![Benchmarks configuration](https://qdrant.tech/benchmarks/client-server.png)

Benchmarks configuration

- This was our setup for this experiment:
  - Client: 8 vcpus, 16 GiB memory, 64GiB storage ( `Standard D8ls v5` on Azure Cloud)
  - Server: 8 vcpus, 32 GiB memory, 64GiB storage ( `Standard D8s v3` on Azure Cloud)
- The Python client uploads data to the server, waits for all required indexes to be constructed, and then performs searches with configured number of threads. We repeat this process with different configurations for each engine, and then select the best one for a given precision.
- We ran all the engines in docker and limited their memory to 25GB. This was used to ensure fairness by avoiding the case of some engine configs being too greedy with RAM usage. This 25 GB limit is completely fair because even to serve the largest `dbpedia-openai-1M-1536-angular` dataset, one hardly needs `1M * 1536 * 4bytes * 1.5 = 8.6GB` of RAM (including vectors + index). Hence, we decided to provide all the engines with ~3x the requirement.

Please note that some of the configs of some engines crashed on some datasets because of the 25 GB memory limit. That’s why you might see fewer points for some engines on choosing higher precision thresholds.

Share this article

[x](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fsingle-node-speed-benchmark%2F&text=Single%20node%20benchmarks "x")[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fsingle-node-speed-benchmark%2F "LinkedIn")

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574597956&cv=11&fst=1748574597956&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fsingle-node-speed-benchmark%2F&hn=www.googleadservices.com&frm=0&tiba=Single%20node%20benchmarks%20-%20Qdrant&npa=0&pscdl=noapi&auid=3848212.1748574598&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574597888&cv=11&fst=1748574597888&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fsingle-node-speed-benchmark%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Single%20node%20benchmarks%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=3848212.1748574598&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c8547194-eb08-4485-8d55-f7e79a6c18b4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7afbe35a-7708-48c5-b754-1c8bd78c955f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fsingle-node-speed-benchmark%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c8547194-eb08-4485-8d55-f7e79a6c18b4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7afbe35a-7708-48c5-b754-1c8bd78c955f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fsingle-node-speed-benchmark%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574599189&cv=11&fst=1748574599189&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fsingle-node-speed-benchmark%2F&hn=www.googleadservices.com&frm=0&tiba=Single%20node%20benchmarks%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=3848212.1748574598&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)