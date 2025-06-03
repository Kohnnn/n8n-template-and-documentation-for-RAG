---
url: "https://qdrant.tech/blog/case-study-garden-intel/"
title: "How Garden Scaled Patent Intelligence with Qdrant - Qdrant"
---

0

# How Garden Scaled Patent Intelligence with Qdrant

Daniel Azoulai

·

May 09, 2025

![How Garden Scaled Patent Intelligence with Qdrant](https://qdrant.tech/blog/case-study-garden-intel/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-garden-intel%2F&text=How%20Garden%20Scaled%20Patent%20Intelligence%20with%20Qdrant "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-garden-intel%2F "LinkedIn")

## [Anchor](https://qdrant.tech/blog/case-study-garden-intel/\#garden-accelerates-patent-intelligence-with-qdrants-filterable-vector-search) Garden Accelerates Patent Intelligence with Qdrant’s Filterable Vector Search

![How Garden Unlocked AI Patent Analysis](https://qdrant.tech/blog/case-study-garden/case-study-garden-bento-dark.jpg)

For more than a century, patent litigation has been a slow, people-powered business. Analysts read page after page—sometimes tens of thousands of pages—hunting for the smoking-gun paragraph that proves infringement or invalidity. Garden, a New York-based startup, set out to change that by applying large-scale AI to the entire global patent corpus—more than 200 million patents—in conjunction with terabytes of real world data.

_“Our customers need to compare millions of possible patent–product pairings in seconds, not days,” explains co-founder Justin Mack. “That means vector search that can handle huge data sets and surgical-grade filtering.”_

### [Anchor](https://qdrant.tech/blog/case-study-garden-intel/\#a-data-set-that-breaks-na%C3%AFve-vector-search) A data set that breaks naïve vector search

Each patent can run to 100+ pages and, thanks to decades of revisions, carries roughly 2,000 metadata fields: jurisdiction, grant date, family ID, claim dependencies, and so on. Garden splits every patent into semantically meaningful chunks, producing “many hundreds of millions” of vectors. The same pipeline ingests real-world product data to compare against the patents.

The engineering demands quickly outgrew Garden’s first solution, a fully-managed vector service. They had tens of gigabytes of data already costing ≈ $5,000 / month. And a lack of native filterable-HNSW meant that Garden had to stand up a separate index for every combination of country, date range, and technology tag. Finally, with no infrastructure visibility, troubleshooting was slow and expensive.

A second migration to a self-hosted open-source alternative cut costs but introduced new pains: on-call operations for a two-person team, upgrades during business hours, and—crucially—the same filtering limitations.

### [Anchor](https://qdrant.tech/blog/case-study-garden-intel/\#discovering-qdrant) Discovering Qdrant

When Garden found Qdrant’s blog post on filterable HNSW, the team realized they could get the search semantics they wanted without bolting on bespoke sharding logic.

_“Filterable HNSW was the deal-maker, but Qdrant Cloud’s managed Rust backbone sealed it,” says Mack. “We kept source-level transparency while off-loading 24×7 ops.”_

- **Scalar quantization (8-bit)** keeps hot vectors in RAM while colder, full-precision embeddings sit on disk—perfect for Garden’s read-heavy, bursty workload.

- **SLA-backed sub-100ms latency** meets Garden’s product target even when a user fires off thousands of queries in a single button-click.

- **Pay-for-what-you-use pricing** lets Garden store 10× more data for roughly the same cost it once paid for a fraction of the corpus.


### [Anchor](https://qdrant.tech/blog/case-study-garden-intel/\#migration-in-practice) Migration in practice

Garden already held all vectors in Google Cloud Storage. A weekend of scripted ETL pushed the embeddings into Qdrant Cloud. Because Qdrant’s ingestion API mirrors popular open-source conventions, the team only altered a few lines of an existing migration script. The heaviest lift—GPU-based embedding of 200M patents—was finished months earlier on a 2,000-GPU transient cluster.

### [Anchor](https://qdrant.tech/blog/case-study-garden-intel/\#business-impact)**Business impact**

| KPI | Before Qdrant | After Qdrant |
| --- | --- | --- |
| Addressable patent corpus | ≈ 20M | **200M+** |
| Vector data under management | tens of millions | **hundreds of millions** |
| Typical query latency | 250 – 400ms | **< 100ms p95** |
| Cost per stored GB | baseline | **~ 10× lower** |
| New revenue lines | 0 | **Full infringement-analysis product** |

Filterable HNSW didn’t just speed up existing workflows; it unlocked an entirely new line of business—high-confidence infringement detection. Clients now click a button and receive a claim-chart quality analysis in minutes. For some enterprises that translates into seven-plus-figure licensing wins or decisive defense against patent trolls.

### [Anchor](https://qdrant.tech/blog/case-study-garden-intel/\#looking-ahead) Looking ahead

As Garden’s customer base grows, query-per-second (QPS) requirements will rise faster than data volume. Meanwhile, Garden plans deeper enrichment of every patent—breaking long descriptions into structured facts the vector index can exploit.

_“We don’t have to think about the vector layer anymore,” Mack notes. “Qdrant lets us focus on the IP insights our customers pay for.”_

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=2145f81e-8216-4091-9542-3c6fb59d06a9)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575532916&cv=11&fst=1748575532916&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104611959~104611961&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-garden-intel%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=How%20Garden%20Scaled%20Patent%20Intelligence%20with%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=444620063.1748575533&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575532877&cv=11&fst=1748575532877&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104611959~104611961&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-garden-intel%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=How%20Garden%20Scaled%20Patent%20Intelligence%20with%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=444620063.1748575533&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9ed27590-ba1d-4a24-9423-743a9e22b584&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=38f8512a-2381-46ff-b7f8-545af95f3620&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-garden-intel%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=9ed27590-ba1d-4a24-9423-743a9e22b584&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=38f8512a-2381-46ff-b7f8-545af95f3620&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-garden-intel%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=1988ab02161e6af97a8cd949f5d8f244&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575534010&cv=11&fst=1748575534010&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104611959~104611961&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-garden-intel%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=How%20Garden%20Scaled%20Patent%20Intelligence%20with%20Qdrant%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=444620063.1748575533&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)