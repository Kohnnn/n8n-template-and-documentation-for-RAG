---
url: "https://qdrant.tech/blog/case-study-dust-v2/"
title: "How Dust Scaled to 5,000+ Data Sources with Qdrant - Qdrant"
---

0

# How Dust Scaled to 5,000+ Data Sources with Qdrant

Daniel Azoulai

·

April 29, 2025

![How Dust Scaled to 5,000+ Data Sources with Qdrant](https://qdrant.tech/blog/case-study-dust-v2/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dust-v2%2F&text=How%20Dust%20Scaled%20to%205,000+%20Data%20Sources%20with%20Qdrant "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dust-v2%2F "LinkedIn")

## [Anchor](https://qdrant.tech/blog/case-study-dust-v2/\#inside-dusts-vector-stack-overhaul-scaling-to-5000-data-sources-with-qdrant) Inside Dust’s Vector Stack Overhaul: Scaling to 5,000+ Data Sources with Qdrant

![How Dust Scaled to 5,000+ Data Sources with Qdrant](https://qdrant.tech/blog/case-study-dust-v2/case-study-dust-v2-v2-bento-dark.jpg)

### [Anchor](https://qdrant.tech/blog/case-study-dust-v2/\#the-challenge-scaling-ai-infrastructure-for-thousands-of-data-sources) The Challenge: Scaling AI Infrastructure for Thousands of Data Sources

Dust, an OS for AI-native companies enabling users to build AI agents powered by actions and company knowledge, faced a set of growing technical hurdles as it scaled its operations. The company’s core product enables users to give AI agents secure access to internal and external data resources, enabling enhanced workflows and faster access to information. However, this mission hit bottlenecks when their infrastructure began to strain under the weight of thousands of data sources and increasingly demanding user queries.

Initially, Dust employed a strategy of creating a separate vector collection per data source, which rapidly became unsustainable. As the number of data sources ballooned beyond 5,000, the platform began experiencing significant performance degradation. RAM consumption skyrocketed, and vector search performance slowed dramatically, especially as the memory-mapped vectors spilled onto disk storage. At one point, they were managing nearly a thousand collections simultaneously and processing over a million vector upsert and delete operations in a single cycle.

### [Anchor](https://qdrant.tech/blog/case-study-dust-v2/\#evaluation-and-selection-why-dust-chose-qdrant) Evaluation and Selection: Why Dust Chose Qdrant

The Dust team explored several popular vector databases. While each had merits, none met all of Dust’s increasingly complex needs. Some providers’ developer experience didn’t align with their workflows, and others lacked the deployment flexibility required. Dust needed a solution capable of handling multi-tenancy at scale, embedding model flexibility, efficient memory usage, and deep configurability.

Qdrant stood out thanks to its open-source Rust foundation, giving Dust the control they needed over memory, performance, and customization. Its intuitive API and strong developer community also made the integration experience more seamless. Critically, Qdrant’s design allowed Dust to consolidate their fragmented architecture—replacing thousands of individual collections with a few shared, multi-tenant ones powered by robust sharding and payload filtering.

### [Anchor](https://qdrant.tech/blog/case-study-dust-v2/\#implementation-highlights-advanced-architecture-with-qdrant) Implementation Highlights: Advanced Architecture with Qdrant

One of the most impactful features Dust adopted was scalar quantization. This reduced vector storage size by a factor of four, enabling the team to keep data in memory rather than falling back to slower disk storage. This shift alone led to dramatic latency improvements. Where queries in large collections once took 5 to 10 seconds, they now returned in under a second. Even in collections with over a million vectors and heavy payloads, search responses consistently clocked in well below the one-second mark.

Dust also built a custom `DustQdrantClient` to manage all vector-related operations. This client abstracted away differences between cluster versions, embedding models, and sharding logic, simplifying ongoing development. Their infrastructure runs in Google Cloud Platform, with Qdrant deployed in isolated VPCs that communicate with Dust’s core APIs using secure authentication. The architecture is replicated across two major regions—US and EU—ensuring both high availability and compliance with data residency laws.

### [Anchor](https://qdrant.tech/blog/case-study-dust-v2/\#results-faster-performance-lower-costs-better-user-experience) Results: Faster Performance, Lower Costs, Better User Experience

The impact of Qdrant was felt immediately. Search latency was slashed from multi-second averages to sub-second responsiveness. Collections that once consumed over 30 GB of RAM were optimized to run efficiently at a quarter of that size. The shift to in-memory quantized vectors, while keeping original vectors on disk for fallback, proved to be the perfect hybrid model for balancing performance and resource usage.

These backend improvements directly translated into user-facing gains. Dust’s AI agents became more responsive and reliable. Even as customers loaded larger and more complex datasets, the system continued to deliver consistent performance. The platform’s ability to scale without degrading UX marked a turning point, empowering Dust to expand its customer base with confidence.

The move to a multi-embedding-model architecture also paid dividends. By grouping data sources by embedder, Dust enabled smoother migrations and more efficient model experimentation. Qdrant’s flexibility let them evolve their architecture without reindexing massive datasets or disrupting end-user functionality.

### [Anchor](https://qdrant.tech/blog/case-study-dust-v2/\#lessons-learned-and-roadmap) Lessons Learned and Roadmap

As they scaled, Dust uncovered a critical insight: users tend to ask more structured, analytical questions when they know a database is involved—queries better suited to SQL than vector search. This prompted the team to pair Qdrant with a text-to-SQL system, blending unstructured and structured query capabilities for a more versatile agent.

Looking forward, Qdrant remains a foundational pillar of Dust’s product roadmap. They’re building multi-region sharding for more granular data residency, scaling their clusters both vertically and horizontally, and supporting newer embedding models from providers like OpenAI and Mistral. Future collections will be organized by embedder, with tenant-aware sharding and index optimizations tailored to each use case.

### [Anchor](https://qdrant.tech/blog/case-study-dust-v2/\#a-new-tier-of-performance-scalability-and-architectural-flexibility) A new tier of performance, scalability, and architectural flexibility

By adopting Qdrant, Dust unlocked a new tier of performance, scalability, and architectural flexibility. Their platform is now equipped to support millions of vectors, operate efficiently across regions, and deliver low-latency search, even at enterprise scale. For teams building sophisticated AI agents, Qdrant provides not just a vector database—but the infrastructure backbone to grow with confidence.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=a6c9886a-5363-4051-8df9-6e28913de3a0)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575299055&cv=11&fst=1748575299055&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dust-v2%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=How%20Dust%20Scaled%20to%205%2C000%2B%20Data%20Sources%20with%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=1628269945.1748575299&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575299011&cv=11&fst=1748575299011&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dust-v2%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=How%20Dust%20Scaled%20to%205%2C000%2B%20Data%20Sources%20with%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1628269945.1748575299&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e2225641-59ee-4c21-895d-deaa8255c979&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=dca45518-686a-4ff0-8063-7f307267e3a1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dust-v2%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e2225641-59ee-4c21-895d-deaa8255c979&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=dca45518-686a-4ff0-8063-7f307267e3a1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dust-v2%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=c45cddabe32eb401a5bdffc6071d6a5d&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575300387&cv=11&fst=1748575300387&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dust-v2%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=How%20Dust%20Scaled%20to%205%2C000%2B%20Data%20Sources%20with%20Qdrant%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1628269945.1748575299&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)