---
url: "https://qdrant.tech/blog/case-study-sprinklr/"
title: "How Sprinklr Leverages Qdrant to Enhance AI-Driven Customer Experience Solutions - Qdrant"
---

0

# How Sprinklr Leverages Qdrant to Enhance AI-Driven Customer Experience Solutions

Qdrant

·

October 17, 2024

![How Sprinklr Leverages Qdrant to Enhance AI-Driven Customer Experience Solutions](https://qdrant.tech/blog/case-study-sprinklr/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-sprinklr%2F&text=How%20Sprinklr%20Leverages%20Qdrant%20to%20Enhance%20AI-Driven%20Customer%20Experience%20Solutions "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-sprinklr%2F "LinkedIn")

![case-study-sprinklr-1](https://qdrant.tech/blog/case-study-sprinklr/image1.png)

[Sprinklr](https://www.sprinklr.com/), a leader in unified customer experience management (Unified-CXM), helps global brands engage customers meaningfully across more than 30 digital channels. To achieve this, Sprinklr needed a scalable solution for AI-powered search to support their AI applications, particularly in handling the vast data requirements of customer interactions.

Raghav Sonavane, Associate Director of Machine Learning Engineering at Sprinklr, leads the Applied AI team, focusing on Generative AI (GenAI) and Retrieval-Augmented Generation (RAG). His team is responsible for training and fine-tuning in-house models and deploying advanced retrieval and generation systems for customer-facing applications like FAQ bots and other [GenAI-driven services](https://www.sprinklr.com/blog/how-sprinklr-uses-RAG/). The team provides all of these capabilities in a centralized platform to the Sprinklr product engineering teams.

![case-study-sprinklr-2](https://qdrant.tech/blog/case-study-sprinklr/image2.png)

_Figure:_ Sprinklr’s RAG architecture

Sprinklr’s platform is composed of four key product suites - Sprinklr Service, Sprinklr Marketing, Sprinklr Social, and Sprinklr Insights. Each suite is embedded with AI-first features such as assist agents, post-call analysis, and real-time analytics, which are crucial for managing large-scale contact center operations. “These AI-driven capabilities, supported by Qdrant’s advanced vector search, enhance Sprinklr’s customer-facing tools such as FAQ bots, transactional bots, conversational services, and product recommendation engines,” says Sonavane.

These self-serve applications rely heavily on advanced vector search to analyze and optimize community content and refine knowledge bases, ensuring efficient and relevant responses. For customers requiring further assistance, Sprinklr equips support agents with powerful search capabilities, enabling them to quickly access similar cases and draw from past interactions, enhancing the quality and speed of customer support.

## [Anchor](https://qdrant.tech/blog/case-study-sprinklr/\#the-need-for-a-vector-database) The Need for a Vector Database

To support various AI-driven applications, Sprinklr needed an efficient vector database. “The key challenge was to provide the highest quality and fastest search capabilities for retrieval tasks across the board,” explains Sonavane.

Last year, Sprinklr undertook a comprehensive evaluation of its existing search infrastructure. The goals were to identify current capability gaps, benchmark performance for speed and cost, and explore opportunities to improve the developer experience through enhanced scalability and stronger data privacy controls. It became clear that an advanced vector database was essential to meet these needs, and Qdrant emerged as the ideal solution.

### [Anchor](https://qdrant.tech/blog/case-study-sprinklr/\#why-qdrant) Why Qdrant?

After evaluating several options of vector DBs, including Pinecone, Weaviate, and ElasticSearch, Sprinklr chose Qdrant for its:

- **Developer-Friendly Documentation:** “Qdrant’s clear [documentation](https://qdrant.tech/documentation/) enabled our team to integrate it quickly into our workflows,” notes Sonavane.

- **High Customizability:** Qdrant provided Sprinklr with essential flexibility through high-level abstractions that allowed for extensive customizations. The diverse teams at Sprinklr, working on various GenAI applications, needed a solution that could adapt to different workloads. “The ability to fine-tune configurations at the collection level was crucial for our varied AI applications,” says Sonavane. Qdrant met this need by offering:

  - **Configuration for high-speed search** that fine-tunes settings for optimal performance.
  - [**Quantized vectors**](https://qdrant.tech/documentation/guides/quantization/) for high-dimensional data workloads
  - [**Memory map**](https://qdrant.tech/documentation/concepts/storage/#configuring-memmap-storage) for efficient search optimizing memory usage.
- **Speed and Cost Efficiency:** Qdrant provided the best combination of speed and cost, making it the most viable solution for Sprinklr’s needs. “We needed a solution that wouldn’t just meet our performance requirements but also keep costs in check, and Qdrant delivered on both fronts,” says Sonavane.

- **Enhanced Monitoring:** Qdrant’s monitoring tools further boosted system efficiency, allowing Sprinklr to maintain high performance across their platforms.


## [Anchor](https://qdrant.tech/blog/case-study-sprinklr/\#implementation-and-qdrants-performance) Implementation and Qdrant’s Performance

Sprinklr’s transition to Qdrant was carefully managed, starting with 10% of their workloads before gradually scaling up. The transition was seamless, thanks in part to Qdrant’s configurable [Web UI](https://qdrant.tech/documentation/interfaces/web-ui/), which allowed Sprinklr to fully utilize its capabilities within the existing infrastructure.

“Qdrant’s ability to index [multiple vectors](https://qdrant.tech/documentation/concepts/vectors/#multivectors) simultaneously and retrieve and re-rank with precision brought significant improvements to our workflow,” Sonavane remarks. This feature reduced the need for repeated retrieval processes, significantly improving efficiency. Additionally, Qdrant’s [quantization](https://qdrant.tech/documentation/guides/quantization/) and [memory mapping](https://qdrant.tech/documentation/concepts/storage/#configuring-memmap-storage) features enabled Sprinklr to reduce RAM usage, leading to substantial cost savings.

Qdrant now plays a key supportive role in enhancing Sprinklr’s vector search capabilities within its AI-driven applications, which is designed to be cloud- and LLM-agnostic. The platform supports various AI-driven tasks, from retrieval and re-ranking to serving advanced customer experiences. “Retrieval is the foundation of all our AI tasks, and Qdrant’s resilience and speed have made it an integral part of our system,” Sonavane emphasizes. Sprinklr operates [Qdrant as a managed service on AWS](https://qdrant.tech/cloud/), ensuring scalability, reliability, and ease of use.

### [Anchor](https://qdrant.tech/blog/case-study-sprinklr/\#key-outcomes-with-qdrant) Key Outcomes with Qdrant

After rigorous internal evaluation, Sprinklr achieved the following results with Qdrant:

- **30% Cost Reduction**: Internal benchmarking showed Qdrant reduced Sprinklr’s retrieval infrastructure costs by 30%.
- **Improved Developer Efficiency**: Qdrant’s user-friendly environment made it easier to maintain instances, enhancing overall efficiency.

The Sprinklr team conducted a thorough internal benchmark on applications requiring vector search across 10k to over 1M vectors with varying dimensions of vectors depending on the use case. The key results from these benchmarks include:

- **Superior Write Performance**: Qdrant’s write performance excelled in Sprinklr’s benchmark tests, with incremental indexing time for 100k to 1M vectors being less than 10% of Elasticsearch’s, making it highly efficient for handling updates and append queries in high-ingestion use cases.
- **Low Latency for Real-Time Applications:** In Sprinklr’s benchmark, Qdrant delivered a P99 latency of 20ms for searches on 1 million vectors, making it ideal for real-time use cases like live chat, where Elasticsearch and Milvus both exceeded 100ms.
- **High Throughput for Heavy Query Loads**: In Sprinklr’s benchmark, Qdrant handled up to 250 requests per second (RPS) under similar configurations, significantly outperforming Elasticsearch’s 100 RPS, making it ideal for environments with heavy query loads.

“Qdrant is a very fast and high quality retrieval system,” Sonavane points out.

![case-study-sprinklr-3](https://qdrant.tech/blog/case-study-sprinklr/image3.png)

_Figure: P95 Query Time vs Mean Average Precision Benchmark Across Varying Index Sizes_

## [Anchor](https://qdrant.tech/blog/case-study-sprinklr/\#outlook) Outlook

Looking ahead, the Applied AI team at Sprinklr is focused on developing Sprinklr Digital Twin technology for companies, organizations, and employees, aiming to seamlessly integrate AI agents with human workers in business processes. Sprinklr Digital Twins are powered by a process engine that incorporates personas, skills, tasks, and activities, designed to optimize operational efficiency.

![case-study-sprinklr-4](https://qdrant.tech/blog/case-study-sprinklr/image4.png)

_Figure: Sprinklr Digital Twin_

Vector search will play a crucial role, as each AI agent will have its own knowledge base, skill set, and tool set, enabling precise and autonomous task execution. The integration of Qdrant further enhances the system’s ability to manage and utilize large volumes of data effectively.

## [Anchor](https://qdrant.tech/blog/case-study-sprinklr/\#benchmarking-conclusion) Benchmarking Conclusion

_**Configuration Details:**_

- We benchmarked applications requiring search on different sizes ranging from 10k to 1M+ vectors, with varying dimensions of vectors depending on the usage. Our infrastructure mainly consisted of Elasticsearch and in-memory Faiss vector search.

Key Observations:

1. **Indexing Speed**: Qdrant indexes vectors rapidly, making it suitable for applications that require quick data ingestion. Among the alternatives tried, milvus was on par with qdrant in terms of indexing time for a given precision. The latest versions of Elasticsearch offer much improvement compared to previous versions, though not as efficient as Qdrant.
   - **Write Performance:** For some of our use cases, update queries and append queries were significantly higher. For ES, an increase in the number of points had a severe impact on total upload time. For 100k to 1M vector index qdrant incremental indexing time was less than 10% of Elasticsearch.
2. **Low Latency**: Tail latencies are very critical for real-time applications such as live chat, requiring low P95 and P99 latencies. For a workload requiring search on 1 million vectors, qdrant provided inference latency of 20ms P99 whereas ES and Milvus were more than 100ms.
3. **High Throughput**: Qdrant handles a high number of requests per second, making it ideal for environments with heavy query loads. For similar configurations, Qdrant provided a throughput of 250 RPS whereas ES was around 100 RPS.

![case-study-sprinklr-5](https://qdrant.tech/blog/case-study-sprinklr/image3.png)

![case-study-sprinklr-6](https://qdrant.tech/blog/case-study-sprinklr/image6.png)

![case-study-sprinklr-7](https://qdrant.tech/blog/case-study-sprinklr/image7.png)

![case-study-sprinklr-8](https://qdrant.tech/blog/case-study-sprinklr/image8.png)

```json
data = [\
\
{'system': 'Qdrant', 'index_size': '1,000', 'MAP': 0.98, 'P95 Time': 0.22, 'Mean Time': 0.1, 'QPS': 280,\
\
'Upload Time': 1},\
\
{'system': 'Qdrant', 'index_size': '10,000', 'MAP': 0.99, 'P95 Time': 0.16, 'Mean Time': 0.09, 'QPS': 330,\
\
'Upload Time': 5},\
\
{'system': 'Qdrant', 'index_size': '100,000', 'MAP': 0.98, 'P95 Time': 0.3, 'Mean Time': 0.23, 'QPS': 145,\
\
'Upload Time': 100},\
\
{'system': 'Qdrant', 'index_size': '1,000,000', 'MAP': 0.99, 'P95 Time': 0.171, 'Mean Time': 0.162, 'QPS': 596,\
\
'Upload Time': 220},\
\
{'system': 'ElasticSearch', 'index_size': '1,000', 'MAP': 0.99, 'P95 Time': 0.42, 'Mean Time': 0.32, 'QPS': 95,\
\
'Upload Time': 10},\
\
{'system': 'ElasticSearch', 'index_size': '10,000', 'MAP': 0.98, 'P95 Time': 0.3, 'Mean Time': 0.24, 'QPS': 120,\
\
'Upload Time': 50},\
\
{'system': 'ElasticSearch', 'index_size': '100,000', 'MAP': 0.99, 'P95 Time': 0.48, 'Mean Time': 0.42, 'QPS': 80,\
\
'Upload Time': 1100},\
\
{'system': 'ElasticSearch', 'index_size': '1,000,000', 'MAP': 0.99, 'P95 Time': 0.37, 'Mean Time': 0.236,\
\
'QPS': 348, 'Upload Time': 1150}\
\
]

```

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=9eb48518-3af5-4744-9964-f5e5081a0954)

![](https://qdrant.tech/img/rocket.svg)

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

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=4eaea148d1b0560e91b5b740d8e3b37e&enableResponsiveStyles=true)

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=91b043ae-83b8-4b7d-96bb-a94eb9dcb2ea&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=df74f3f6-95d4-4728-9631-156d08b5ca0a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-sprinklr%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573634238&cv=11&fst=1748573634238&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-sprinklr%2F&hn=www.googleadservices.com&frm=0&tiba=How%20Sprinklr%20Leverages%20Qdrant%20to%20Enhance%20AI-Driven%20Customer%20Experience%20Solutions%20-%20Qdrant&npa=0&pscdl=noapi&auid=36733674.1748573634&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573634220&cv=11&fst=1748573634220&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-sprinklr%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=How%20Sprinklr%20Leverages%20Qdrant%20to%20Enhance%20AI-Driven%20Customer%20Experience%20Solutions%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=36733674.1748573634&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573634302&cv=11&fst=1748573634302&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-sprinklr%2F&hn=www.googleadservices.com&frm=0&tiba=How%20Sprinklr%20Leverages%20Qdrant%20to%20Enhance%20AI-Driven%20Customer%20Experience%20Solutions%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=36733674.1748573634&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=91b043ae-83b8-4b7d-96bb-a94eb9dcb2ea&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=df74f3f6-95d4-4728-9631-156d08b5ca0a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-sprinklr%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)