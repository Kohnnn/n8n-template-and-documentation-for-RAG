---
url: "https://qdrant.tech/blog/case-study-mixpeek/"
title: "How Mixpeek Uses Qdrant for Efficient Multimodal Feature Stores - Qdrant"
---

0

# How Mixpeek Uses Qdrant for Efficient Multimodal Feature Stores

Daniel Azoulai

·

April 08, 2025

![How Mixpeek Uses Qdrant for Efficient Multimodal Feature Stores](https://qdrant.tech/blog/case-study-mixpeek/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-mixpeek%2F&text=How%20Mixpeek%20Uses%20Qdrant%20for%20Efficient%20Multimodal%20Feature%20Stores "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-mixpeek%2F "LinkedIn")

# [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#how-mixpeek-uses-qdrant-for-efficient-multimodal-feature-stores) How Mixpeek Uses Qdrant for Efficient Multimodal Feature Stores

![How Mixpeek Uses Qdrant for Efficient Multimodal Feature Stores](https://qdrant.tech/blog/case-study-mixpeek/Case-Study-Mixpeek-Summary-Dark.jpg)

## [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#about-mixpeek) About Mixpeek

[Mixpeek](http://mixpeek.com/) is a multimodal data processing and retrieval platform designed for developers and data teams. Founded by Ethan Steininger, a former MongoDB search specialist, Mixpeek enables efficient ingestion, feature extraction, and retrieval across diverse media types including video, images, audio, and text.

## [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#the-challenge-optimizing-feature-stores-for-complex-retrievers) The Challenge: Optimizing Feature Stores for Complex Retrievers

As Mixpeek’s multimodal data warehouse evolved, their feature stores needed to support increasingly complex retrieval patterns. Initially using MongoDB Atlas’s vector search, they encountered limitations when implementing [**hybrid retrievers**](https://docs.mixpeek.com/retrieval/retrievers) **combining dense and sparse vectors with metadata pre-filtering**.

A critical limitation emerged when implementing **late interaction techniques like ColBERT across video embeddings**, which requires multi-vector indexing. MongoDB’s kNN search could not support these multi-vector representations for this contextual understanding.

Another one of Mixpeek’s customers required **reverse video search** for programmatic ad-serving, where retrievers needed to identify **high-converting video segments** across massive object collections - a task that proved inefficient with MongoDB’s general-purpose database feature stores.

_“We eliminated hundreds of lines of code with what was previously a MongoDB kNN Hybrid search when we replaced it with Qdrant as our feature store.”_ — Ethan Steininger, Mixpeek Founder

![mixpeek-architecture-with-qdrant](https://qdrant.tech/blog/case-study-mixpeek/mixpeek-architecture.jpg)

## [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#why-mixpeek-chose-qdrant-for-feature-stores) Why Mixpeek Chose Qdrant for Feature Stores

After evaluating multiple options including **Postgres with pgvector** and **MongoDB’s kNN search**, Mixpeek selected Qdrant to power [their feature stores](https://docs.mixpeek.com/management/features) due to its specialization in vector search and integration capabilities with their retrieval pipelines. Qdrant’s native support for multi-vector indexing was crucial for implementing late interaction techniques like ColBERT, which MongoDB couldn’t efficiently support.

### [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#simplifying-hybrid-retrievers) Simplifying Hybrid Retrievers

Previously, Mixpeek maintained complex custom logic to merge results from different feature stores. Qdrant’s native support for Reciprocal Rank Fusion (RRF) streamlined their retriever implementations, reducing hybrid search code by **80%**. The multi-vector capabilities also enabled more sophisticated retrieval methods that better captured semantic relationships.

_“Hybrid retrievers with our previous feature stores were challenging. With Qdrant, it just worked.”_

### [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#40-faster-query-times-with-parallel-retrieval) 40% Faster Query Times with Parallel Retrieval

For collections with billions of features, Qdrant’s prefetching capabilities enabled parallel retrieval across multiple feature stores. This cut retriever query times by 40%, dropping from ~2.5s to 1.3-1.6s.

_“Prefetching in Qdrant lets us execute multiple feature store retrievals simultaneously and then combine the results, perfectly supporting our retriever pipeline architecture.”_

### [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#optimizing-sagemaker-feature-extraction-workflows) Optimizing SageMaker Feature Extraction Workflows

Mixpeek uses Amazon SageMaker for [feature extraction](https://docs.mixpeek.com/extraction/scene-splitting), and database queries were a significant bottleneck. By implementing Qdrant as their feature store, they reduced query overhead by 50%, streamlining their ingestion pipelines.

_“We were running inference with SageMaker for feature extraction, and our feature store queries used to be a significant bottleneck. Qdrant shaved off a lot of that time.”_

## [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#supporting-mixpeeks-taxonomy-and-clustering-architecture) Supporting Mixpeek’s Taxonomy and Clustering Architecture

Qdrant proved particularly effective for implementing Mixpeek’s taxonomy and clustering capabilities:

### [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#taxonomies-join-analogue) Taxonomies (JOIN Analogue)

Qdrant’s payload filtering facilitated efficient implementation of both [flat and hierarchical taxonomies](https://docs.mixpeek.com/enrichment/taxonomies), enabling document enrichment through similarity-based “joins” across collections.

### [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#clustering-group-by-analogue) Clustering (GROUP BY Analogue)

The platform’s batch vector search capabilities streamlined [document clustering](https://docs.mixpeek.com/enrichment/clusters) based on feature similarity, providing an effective implementation of the traditional “group by” interface.

## [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#measurable-improvements-after-feature-store-migration) Measurable Improvements After Feature Store Migration

The migration to Qdrant as Mixpeek’s feature store brought significant improvements:

- **40% Faster Retrievers**: Reduced query times from ~2.5s to 1.3-1.6s
- **80% Code Reduction**: Simplified retriever implementations
- **Improved Developer Productivity**: Easier implementation of complex retrieval patterns
- **Optimized Scalability**: Better performance at billion-feature scale
- **Enhanced Multimodal Retrieval**: Better support for combining different feature types

## [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#future-direction-supporting-diverse-multimodal-use-cases) Future Direction: Supporting Diverse Multimodal Use Cases

Mixpeek’s architecture excels by pre-building specialized feature extractors tightly coupled with retriever pipelines, enabling efficient processing across [diverse multimodal use cases.](https://mixpeek.com/solutions)

This architectural approach ensures that features extracted during ingestion are precisely what retrievers need for efficient querying, eliminating translation layers that typically slow down multimodal systems.

_“We’re moving towards sophisticated multimodal ontologies, and Qdrant’s specialized capabilities as a feature store will be essential for these advanced retriever strategies.”_

## [Anchor](https://qdrant.tech/blog/case-study-mixpeek/\#conclusion-specialized-feature-stores-for-multimodal-data-warehousing) Conclusion: Specialized Feature Stores for Multimodal Data Warehousing

Mixpeek’s journey highlights the importance of specialized feature stores in a multimodal data warehouse architecture. Qdrant’s focus on vector search efficiency made it the ideal choice for powering Mixpeek’s feature stores, enabling more efficient retrievers and ingestion pipelines.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=cc5c1a0a-faeb-43b9-9e82-420c523519a0)

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

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?enableResponsiveStyles=true)

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ea83247f-1167-4cd1-a899-5d94ea08be73&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5e25ee3f-a270-4048-a6ba-7910eb337914&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-mixpeek%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574134294&cv=11&fst=1748574134294&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-mixpeek%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=How%20Mixpeek%20Uses%20Qdrant%20for%20Efficient%20Multimodal%20Feature%20Stores%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=140087756.1748574132&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574134306&cv=11&fst=1748574134306&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-mixpeek%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=How%20Mixpeek%20Uses%20Qdrant%20for%20Efficient%20Multimodal%20Feature%20Stores%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=140087756.1748574132&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574134283&cv=11&fst=1748574134283&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-mixpeek%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=How%20Mixpeek%20Uses%20Qdrant%20for%20Efficient%20Multimodal%20Feature%20Stores%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=140087756.1748574132&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ea83247f-1167-4cd1-a899-5d94ea08be73&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5e25ee3f-a270-4048-a6ba-7910eb337914&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-mixpeek%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)