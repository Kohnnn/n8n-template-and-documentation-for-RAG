---
url: "https://qdrant.tech/blog/open-source-vector-search-engine-vector-database/"
title: "Optimizing an Open Source Vector Database with Andrey Vasnetsov - Qdrant"
---

0

# Optimizing an Open Source Vector Database with Andrey Vasnetsov

Demetrios Brinkmann

·

January 10, 2024

![Optimizing an Open Source Vector Database with Andrey Vasnetsov](https://qdrant.tech/blog/open-source-vector-search-engine-vector-database/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fopen-source-vector-search-engine-vector-database%2F&text=Optimizing%20an%20Open%20Source%20Vector%20Database%20with%20Andrey%20Vasnetsov "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fopen-source-vector-search-engine-vector-database%2F "LinkedIn")

# [Anchor](https://qdrant.tech/blog/open-source-vector-search-engine-vector-database/\#optimizing-open-source-vector-search-strategies-from-andrey-vasnetsov-at-qdrant) Optimizing Open Source Vector Search: Strategies from Andrey Vasnetsov at Qdrant

> _“For systems like Qdrant, scalability and performance in my opinion, is much more important than transactional consistency, so it should be treated as a search engine rather than database.”_
>
> – Andrey Vasnetsov

Discussing core differences between search engines and databases, Andrey underlined the importance of application needs and scalability in database selection for vector search tasks.

Andrey Vasnetsov, CTO at Qdrant is an enthusiast of [Open Source](https://qdrant.tech/), machine learning, and vector search. He works on Open Source projects related to [Vector Similarity Search](https://qdrant.tech/articles/vector-similarity-beyond-search/) and Similarity Learning. He prefers practical over theoretical, working demo over arXiv paper.

_**You can watch this episode on [YouTube](https://www.youtube.com/watch?v=bU38Ovdh3NY).**_

Qdrant: Open Source Vector Search Engine and Vector Database (Andrey Vasnetsov) - YouTube

CMU Database Group

78.4K subscribers

[Qdrant: Open Source Vector Search Engine and Vector Database (Andrey Vasnetsov)](https://www.youtube.com/watch?v=bU38Ovdh3NY)

CMU Database Group

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

More videos

## More videos

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=bU38Ovdh3NY&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 1:02:38
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=bU38Ovdh3NY "Watch on YouTube")

_**This episode is part of the [ML⇄DB Seminar Series](https://db.cs.cmu.edu/seminar2023/#) (Machine Learning for Databases + Databases for Machine Learning) of the Carnegie Mellon University Database Research Group.**_

## [Anchor](https://qdrant.tech/blog/open-source-vector-search-engine-vector-database/\#top-takeaways)**Top Takeaways:**

Dive into the intricacies of [vector databases](https://qdrant.tech/articles/what-is-a-vector-database/) with Andrey as he unpacks Qdrant’s approach to combining filtering and vector search, revealing how in-place filtering during graph traversal optimizes precision without sacrificing search exactness, even when scaling to billions of vectors.

5 key insights you’ll learn:

- 🧠 **The Strategy of Subgraphs:** Dive into how overlapping intervals and geo hash regions can enhance the precision and connectivity within vector search indices.

- 🛠️ **Engine vs Database:** Discover the differences between search engines and relational databases and why considering your application’s needs is crucial for scalability.

- 🌐 **Combining Searches with Relational Data:** Get insights on integrating relational and vector search for improved efficiency and performance.

- 🚅 **Speed and Precision Tactics:** Uncover the techniques for controlling search precision and speed by tweaking the beam size in HNSW indices.

- 🔗 **Connected Graph Challenges:** Learn about navigating the difficulties of maintaining a connected graph while filtering during search operations.


> Fun Fact: [The Qdrant system](https://qdrant.tech/) is capable of in-place filtering during graph traversal, which is a novel approach compared to traditional post-filtering methods, ensuring the correct quantity of results that meet the filtering conditions.

## [Anchor](https://qdrant.tech/blog/open-source-vector-search-engine-vector-database/\#timestamps) Timestamps:

00:00 Search professional with expertise in vectors and engines.

09:59 Elasticsearch: scalable, weak consistency, prefer vector search.

12:53 Optimize data structures for faster processing efficiency.

21:41 Vector indexes require special treatment, like HNSW’s proximity graph and greedy search.

23:16 HNSW index: approximate, precision control, CPU intensive.

30:06 Post-filtering inefficient, prefiltering costly.

34:01 Metadata-based filters; creating additional connecting links.

41:41 Vector dimension impacts comparison speed, indexing complexity high.

46:53 Overlapping intervals and subgraphs for precision.

53:18 Postgres limits scalability, additional indexing engines provide faster queries.

59:55 Embedding models for time series data explained.

01:02:01 Cheaper system for serving billion vectors.

## [Anchor](https://qdrant.tech/blog/open-source-vector-search-engine-vector-database/\#more-quotes-from-andrey) More Quotes from Andrey:

_“It allows us to compress vector to a level where a single dimension is represented by just a single bit, which gives total of 32 times compression for the vector.”_

– Andrey Vasnetsov on vector compression in AI

_“We build overlapping intervals and we build these subgraphs with additional links for those intervals. And also we can do the same with, let’s say, location data where we have geocoordinates, so latitude, longitude, we encode it into geo hashes and basically build this additional graph for overlapping geo hash regions.”_

– Andrey Vasnetsov

_“We can further compress data using such techniques as delta encoding, as variable byte encoding, and so on. And this total effect, total combined effect of this optimization can make immutable data structures order of minute more efficient than mutable ones.”_

– Andrey Vasnetsov

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=8c308dc4-0c7d-481e-99a0-672b373989fd)

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d58e460d-81a6-4dcc-bd0b-93cd499f9c90&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4c934bc0-a639-4460-9c86-dcac6878d08d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fopen-source-vector-search-engine-vector-database%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d58e460d-81a6-4dcc-bd0b-93cd499f9c90&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4c934bc0-a639-4460-9c86-dcac6878d08d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fopen-source-vector-search-engine-vector-database%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)