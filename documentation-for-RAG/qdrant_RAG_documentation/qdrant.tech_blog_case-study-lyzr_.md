---
url: "https://qdrant.tech/blog/case-study-lyzr/"
title: "How Lyzr Supercharged AI Agent Performance with Qdrant - Qdrant"
---

0

# How Lyzr Supercharged AI Agent Performance with Qdrant

Daniel Azoulai

·

April 15, 2025

![How Lyzr Supercharged AI Agent Performance with Qdrant](https://qdrant.tech/blog/case-study-lyzr/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-lyzr%2F&text=How%20Lyzr%20Supercharged%20AI%20Agent%20Performance%20with%20Qdrant "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-lyzr%2F "LinkedIn")

# [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#how-lyzr-supercharged-ai-agent-performance-with-qdrant) How Lyzr Supercharged AI Agent Performance with Qdrant

![How Lyzr Supercharged AI Agent Performance with Qdrant](https://qdrant.tech/blog/case-study-lyzr/case-study-lyzr-summary-dark.png)

## [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#scaling-intelligent-agents-how-lyzr-supercharged-performance-with-qdrant) Scaling Intelligent Agents: How Lyzr Supercharged Performance with Qdrant

As AI agents become more capable and pervasive, the infrastructure behind them must evolve to handle rising concurrency, low-latency demands, and ever-growing knowledge bases. At Lyzr Agent Studio—where over 100 agents are deployed across industries—these challenges arrived quickly and at scale.

When their existing vector database infrastructure began to buckle under pressure, the engineering team needed a solution that could do more than just keep up. It had to accelerate them forward.

This is how they rethought their stack and adopted Qdrant as the foundation for fast, scalable agent performance.

## [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#the-scaling-limits-of-early-stack-choices) The Scaling Limits of Early Stack Choices

![Lyzr-architecture](https://qdrant.tech/blog/case-study-lyzr/lyzr-architecture.jpg)

Lyzr’s architecture used Weaviate, with additional benchmarking on Pinecone. Initially, this setup was fine for development and controlled testing. The system managed around 1,500 vector entries, with a small number of agents issuing moderate query loads in a steady pattern.

### [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#initial-setup) Initial setup:

| Parameter | Details |
| --- | --- |
| Deployment Type | Single-node or small-cluster (Weaviate and other vector db) |
| Embedding Model | Sentence-transformer (768 dimensions) |
| Concurrent Agents | 10 to 20 knowledge search agents |
| Query Rate per Agent | 5-10 queries per minute |
| Traffic Pattern | Steady, no significant spikes |

Under these conditions, both databases performed adequately. Query latency hovered between 80 and 150 milliseconds. Indexing operations completed within a few hours. Overall performance was predictable and stable.

But as the platform expanded—with a larger corpus, more complex workflows, and significantly more concurrency—these systems began to falter.

## [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#growth-brings-latency-timeouts-and-resource-bottlenecks) Growth Brings Latency, Timeouts, and Resource Bottlenecks

Once the knowledge base exceeded 2,500 entries and live agent concurrency grew past 100, the platform began to strain.

Query latency increased nearly 4x to 300-500 milliseconds. During peak usage, agents sometimes timed out waiting for vector results, which impacted downstream decision logic. Indexing operations slowed as well, consuming excess CPU and memory, and introducing bottlenecks during data updates.

These issues created real friction in production environments—and made it clear that a more scalable, performant vector database was needed.

## [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#evaluation-of-alternative-vector-databases) Evaluation of Alternative Vector Databases

With growing data volume and rising agent concurrency, Lyzr needed a more scalable and efficient vector database.

They needed something that could handle heavier loads while maintaining fast response times and reducing operational overhead. They evaluated alternatives based on the below criteria:

| Criteria | Focus Area | Impact on System |
| --- | --- | --- |
| Scalability & Distributed Computing | Horizontal scaling, clustering | Support growing datasets and high agent concurrency |
| Indexing Performance | Ingestion speed, update efficiency | Reduce downtime and enable faster bulk data updates |
| Query Latency & Throughput | Search response under load | Ensure agents maintain fast, real-time responses |
| Consistency & Reliability | Handling concurrency & failures | Avoid timeouts and failed queries during peak usage |
| Resource Efficiency | CPU, memory, and storage usage | Optimize infrastructure costs while scaling workload |
| Benchmark Results | Real-world load simulation | Validate sustained performance under >1,000 QPM loads |

## [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#qdrant-speeds-up-queries-by-90-indexes-2x-faster-and-reduces-infra-costs-by-30) Qdrant speeds up queries by >90%, indexes 2x faster, and reduces infra costs by 30%.

That shift came with Qdrant, which quickly surpassed expectations across every critical metric.

With Qdrant, query latency dropped to just **20–50 milliseconds**, a **>90% improvement** over Weaviate and Pinecone. Even with hundreds of concurrent agents generating over 1,000 queries per minute, performance remained consistent.

Indexing operations improved dramatically. Ingestion times for large datasets were **2x faster**, and the system required significantly fewer compute and memory resources to complete them. This enabled the team to reduce infrastructure costs by approximately **30%**.

Qdrant also demonstrated greater consistency. While Weaviate and Pinecone both encountered performance degradation at scale, Qdrant remained stable under 1,000+ queries per minute—supporting over 100 concurrent agents without latency spikes or slowdowns. Most notably, Lyzr sustained **throughput of more than 250 queries per second**, across distributed agents, without compromising speed or stability.

| Metric | Weaviate | Pinecone | Qdrant |
| --- | --- | --- | --- |
| Avg Query Latency at 100 agents (ms) | 300-500 | 250-450 | 20-50 (P99) |
| Indexing Hours (2,500+ entries) | ~3 | ~2.5 | ~1.5 |
| Query Throughput (QPS) | ~80 | ~100 | >250 |
| Resource Utilization (CPU/Memory) | High | Medium-High | Low-Medium |
| Horizontal Scalability | Moderate | Moderate | Highly Scalable |

Qdrant’s HNSW-based indexing allowed the system to handle live updates without downtime or reindexing—eliminating one of the biggest sources of friction in the previous setup.

## [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#use-case-spotlight-ntt-data-improves-retrieval-accuracy) Use Case Spotlight: NTT Data improves retrieval accuracy

One deployment, built for NTT Data, focused on automating IT change request workflows. The agent initially ran on Cosmos DB within Azure. While integration was smooth, vector search performance was limited. Indexing precision was inadequate, and the system struggled to surface relevant results as data volume grew.

After migrating to Qdrant, the difference was immediate. Retrieval accuracy improved substantially, even for long-tail queries. The system maintained high responsiveness under concurrent loads, and horizontal scaling became simpler—ensuring consistent performance as project demands evolved.

![NTT Architecture](https://qdrant.tech/blog/case-study-lyzr/ntt-visual.jpg)

* * *

## [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#use-case-spotlight-npd-supports-accurate-low-latency-retrieval-for-agents) Use Case Spotlight: NPD supports accurate, low-latency retrieval for Agents

Another example involved NPD, which deployed customer-facing agents across six websites. These agents were tasked with answering product questions and guiding users to the correct URLs based on a dynamic, site-wide knowledge base.

Qdrant’s vector search enabled accurate, low-latency retrieval across thousands of entries. Even under increasing user traffic, the platform delivered consistent performance, eliminating the latency spikes experienced with previous solutions.

![NPD Architecture](https://qdrant.tech/blog/case-study-lyzr/npd-visual.jpeg)

## [Anchor](https://qdrant.tech/blog/case-study-lyzr/\#final-thoughts) Final Thoughts

The lesson from Lyzr’s experience is clear: a production-grade AI platform demands a production-grade vector database.

Qdrant delivered on that requirement. It allowed Lyzr to dramatically reduce latency, scale query throughput, simplify data ingestion, and lower infrastructure costs—all while maintaining system stability at scale.

As the AI ecosystem evolves, the performance of the vector database will increasingly dictate the performance of the agent itself. With Qdrant, Lyzr gained the infrastructure it needed to keep its agents fast, intelligent, and reliable—even under real-world production loads.

* * *

**Want to see how Lyzr Agent Studio and Qdrant can work in your stack?**

Explore [Lyzr Agent Studio](https://studio.lyzr.ai/) or learn more about [Qdrant](https://qdrant.tech/).

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=b2d5ec53-2b3d-466b-a68a-9f50e173e611)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574476093&cv=11&fst=1748574476093&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-lyzr%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=How%20Lyzr%20Supercharged%20AI%20Agent%20Performance%20with%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=2034925366.1748574476&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574476052&cv=11&fst=1748574476052&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308615&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-lyzr%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=How%20Lyzr%20Supercharged%20AI%20Agent%20Performance%20with%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2034925366.1748574476&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ff8c62a9-052a-428a-a1d7-cb013cad4dea&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e7c700ff-6a92-4852-ae1a-8ccb50434f68&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-lyzr%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ff8c62a9-052a-428a-a1d7-cb013cad4dea&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e7c700ff-6a92-4852-ae1a-8ccb50434f68&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-lyzr%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=8c13e44c389d8d04174424a1c738be32&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574477107&cv=11&fst=1748574477107&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-lyzr%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=How%20Lyzr%20Supercharged%20AI%20Agent%20Performance%20with%20Qdrant%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2034925366.1748574476&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)