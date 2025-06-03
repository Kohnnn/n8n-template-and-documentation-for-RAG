---
url: "https://qdrant.tech/articles/dedicated-service/"
title: "Vector Search as a dedicated service - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Vector Search as a dedicated service

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)

# Vector Search as a dedicated service

Andrey Vasnetsov

·

November 30, 2023

![Vector Search as a dedicated service](https://qdrant.tech/articles_data/dedicated-service/preview/title.jpg)

Ever since the data science community discovered that vector search significantly improves LLM answers,
various vendors and enthusiasts have been arguing over the proper solutions to store embeddings.

Some say storing them in a specialized engine (aka vector database) is better. Others say that it’s enough to use plugins for existing databases.

Here are [just](https://nextword.substack.com/p/vector-database-is-not-a-separate) a [few](https://stackoverflow.blog/2023/09/20/do-you-need-a-specialized-vector-database-to-implement-vector-search-well/) of [them](https://www.singlestore.com/blog/why-your-vector-database-should-not-be-a-vector-database/).

This article presents our vision and arguments on the topic .
We will:

1. Explain why and when you actually need a dedicated vector solution
2. Debunk some ungrounded claims and anti-patterns to be avoided when building a vector search system.

A table of contents:

- _Each database vendor will sooner or later introduce vector capabilities…_ \[ [click](https://qdrant.tech/articles/dedicated-service/#each-database-vendor-will-sooner-or-later-introduce-vector-capabilities-that-will-make-every-database-a-vector-database)\]
- _Having a dedicated vector database requires duplication of data._ \[ [click](https://qdrant.tech/articles/dedicated-service/#having-a-dedicated-vector-database-requires-duplication-of-data)\]
- _Having a dedicated vector database requires complex data synchronization._ \[ [click](https://qdrant.tech/articles/dedicated-service/#having-a-dedicated-vector-database-requires-complex-data-synchronization)\]
- _You have to pay for a vector service uptime and data transfer._ \[ [click](https://qdrant.tech/articles/dedicated-service/#you-have-to-pay-for-a-vector-service-uptime-and-data-transfer-of-both-solutions)\]
- _What is more seamless than your current database adding vector search capability?_ \[ [click](https://qdrant.tech/articles/dedicated-service/#what-is-more-seamless-than-your-current-database-adding-vector-search-capability)\]
- _Databases can support RAG use-case end-to-end._ \[ [click](https://qdrant.tech/articles/dedicated-service/#databases-can-support-rag-use-case-end-to-end)\]

## [Anchor](https://qdrant.tech/articles/dedicated-service/\#responding-to-claims) Responding to claims

###### [Anchor](https://qdrant.tech/articles/dedicated-service/\#each-database-vendor-will-sooner-or-later-introduce-vector-capabilities-that-will-make-every-database-a-vector-database) Each database vendor will sooner or later introduce vector capabilities. That will make every database a Vector Database.

The origins of this misconception lie in the careless use of the term Vector _Database_.
When we think of a _database_, we subconsciously envision a relational database like Postgres or MySQL.
Or, more scientifically, a service built on ACID principles that provides transactions, strong consistency guarantees, and atomicity.

The majority of Vector Database are not _databases_ in this sense.
It is more accurate to call them _search engines_, but unfortunately, the marketing term _vector database_ has already stuck, and it is unlikely to change.

_What makes search engines different, and why vector DBs are built as search engines?_

First of all, search engines assume different patterns of workloads and prioritize different properties of the system. The core architecture of such solutions is built around those priorities.

What types of properties do search engines prioritize?

- **Scalability**. Search engines are built to handle large amounts of data and queries. They are designed to be horizontally scalable and operate with more data than can fit into a single machine.
- **Search speed**. Search engines should guarantee low latency for queries, while the atomicity of updates is less important.
- **Availability**. Search engines must stay available if the majority of the nodes in a cluster are down. At the same time, they can tolerate the eventual consistency of updates.

![Database guarantees compass](https://qdrant.tech/articles_data/dedicated-service/compass.png)

Database guarantees compass

Those priorities lead to different architectural decisions that are not reproducible in a general-purpose database, even if it has vector index support.

###### [Anchor](https://qdrant.tech/articles/dedicated-service/\#having-a-dedicated-vector-database-requires-duplication-of-data) Having a dedicated vector database requires duplication of data.

By their very nature, vector embeddings are derivatives of the primary source data.

In the vast majority of cases, embeddings are derived from some other data, such as text, images, or additional information stored in your system. So, in fact, all embeddings you have in your system can be considered transformations of some original source.

And the distinguishing feature of derivative data is that it will change when the transformation pipeline changes.
In the case of vector embeddings, the scenario of those changes is quite simple: every time you update the encoder model, all the embeddings will change.

In systems where vector embeddings are fused with the primary data source, it is impossible to perform such migrations without significantly affecting the production system.

As a result, even if you want to use a single database for storing all kinds of data, you would still need to duplicate data internally.

###### [Anchor](https://qdrant.tech/articles/dedicated-service/\#having-a-dedicated-vector-database-requires-complex-data-synchronization) Having a dedicated vector database requires complex data synchronization.

Most production systems prefer to isolate different types of workloads into separate services.
In many cases, those isolated services are not even related to search use cases.

For example, databases for analytics and one for serving can be updated from the same source.
Yet they can store and organize the data in a way that is optimal for their typical workloads.

Search engines are usually isolated for the same reason: you want to avoid creating a noisy neighbor problem and compromise the performance of your main database.

_To give you some intuition, let’s consider a practical example:_

Assume we have a database with 1 million records.
This is a small database by modern standards of any relational database.
You can probably use the smallest free tier of any cloud provider to host it.

But if we want to use this database for vector search, 1 million OpenAI `text-embedding-ada-002` embeddings will take **~6GB of RAM** (sic!).
As you can see, the vector search use case completely overwhelmed the main database resource requirements.
In practice, this means that your main database becomes burdened with high memory requirements and can not scale efficiently, limited by the size of a single machine.

Fortunately, the data synchronization problem is not new and definitely not unique to vector search.
There are many well-known solutions, starting with message queues and ending with specialized ETL tools.

For example, we recently released our [integration with Airbyte](https://qdrant.tech/documentation/integrations/airbyte/), allowing you to synchronize data from various sources into Qdrant incrementally.

###### [Anchor](https://qdrant.tech/articles/dedicated-service/\#you-have-to-pay-for-a-vector-service-uptime-and-data-transfer-of-both-solutions) You have to pay for a vector service uptime and data transfer of both solutions.

In the open-source world, you pay for the resources you use, not the number of different databases you run.
Resources depend more on the optimal solution for each use case.
As a result, running a dedicated vector search engine can be even cheaper, as it allows optimization specifically for vector search use cases.

For instance, Qdrant implements a number of [quantization techniques](https://qdrant.tech/documentation/guides/quantization/) that can significantly reduce the memory footprint of embeddings.

In terms of data transfer costs, on most cloud providers, network use within a region is usually free. As long as you put the original source data and the vector store in the same region, there are no added data transfer costs.

###### [Anchor](https://qdrant.tech/articles/dedicated-service/\#what-is-more-seamless-than-your-current-database-adding-vector-search-capability) What is more seamless than your current database adding vector search capability?

In contrast to the short-term attractiveness of integrated solutions, dedicated search engines propose flexibility and a modular approach.
You don’t need to update the whole production database each time some of the vector plugins are updated.
Maintenance of a dedicated search engine is as isolated from the main database as the data itself.

In fact, integration of more complex scenarios, such as read/write segregation, is much easier with a dedicated vector solution.
You can easily build cross-region replication to ensure low latency for your users.

![Read/Write segregation + cross-regional deployment](https://qdrant.tech/articles_data/dedicated-service/region-based-deploy.png)

Read/Write segregation + cross-regional deployment

It is especially important in large enterprise organizations, where the responsibility for different parts of the system is distributed among different teams.
In those situations, it is much easier to maintain a dedicated search engine for the AI team than to convince the core team to update the whole primary database.

Finally, the vector capabilities of the all-in-one database are tied to the development and release cycle of the entire stack.
Their long history of use also means that they need to pay a high price for backward compatibility.

###### [Anchor](https://qdrant.tech/articles/dedicated-service/\#databases-can-support-rag-use-case-end-to-end) Databases can support RAG use-case end-to-end.

Putting aside performance and scalability questions, the whole discussion about implementing RAG in the DBs assumes that the only detail missing in traditional databases is the vector index and the ability to make fast ANN queries.

In fact, the current capabilities of vector search have only scratched the surface of what is possible.
For example, in our recent article, we discuss the possibility of building an [exploration API](https://qdrant.tech/articles/vector-similarity-beyond-search/) to fuel the discovery process - an alternative to kNN search, where you don’t even know what exactly you are looking for.

## [Anchor](https://qdrant.tech/articles/dedicated-service/\#summary) Summary

Ultimately, you do not need a vector database if you are looking for a simple vector search functionality with a small amount of data. We genuinely recommend starting with whatever you already have in your stack to prototype. But you need one if you are looking to do more out of it, and it is the central functionality of your application. It is just like using a multi-tool to make something quick or using a dedicated instrument highly optimized for the use case.

Large-scale production systems usually consist of different specialized services and storage types for good reasons since it is one of the best practices of modern software architecture. Comparable to the orchestration of independent building blocks in a microservice architecture.

When you stuff the database with a vector index, you compromise both the performance and scalability of the main database and the vector search capabilities.
There is no one-size-fits-all approach that would not compromise on performance or flexibility.
So if your use case utilizes vector search in any significant way, it is worth investing in a dedicated vector search engine, aka vector database.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/dedicated-service.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/dedicated-service.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574985539&cv=11&fst=1748574985539&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdedicated-service%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Vector%20Search%20as%20a%20dedicated%20service%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=142851757.1748574985&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574985598&cv=11&fst=1748574985598&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdedicated-service%2F&hn=www.googleadservices.com&frm=0&tiba=Vector%20Search%20as%20a%20dedicated%20service%20-%20Qdrant&npa=0&pscdl=noapi&auid=142851757.1748574985&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=50dc484c-4d90-49f6-94c4-16cbf41263b8&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=347c2455-7cf0-4685-bd13-9ec252e68ee4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdedicated-service%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=50dc484c-4d90-49f6-94c4-16cbf41263b8&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=347c2455-7cf0-4685-bd13-9ec252e68ee4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdedicated-service%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574986665&cv=11&fst=1748574986665&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fdedicated-service%2F&hn=www.googleadservices.com&frm=0&tiba=Vector%20Search%20as%20a%20dedicated%20service%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=142851757.1748574985&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)