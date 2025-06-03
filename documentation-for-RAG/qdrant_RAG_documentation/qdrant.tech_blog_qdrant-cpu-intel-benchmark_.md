---
url: "https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/"
title: "Intel’s New CPU Powers Faster Vector Search - Qdrant"
---

0

# Intel’s New CPU Powers Faster Vector Search

David Myriel, Kumar Shivendu

·

May 10, 2024

![Intel’s New CPU Powers Faster Vector Search](https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-cpu-intel-benchmark%2F&text=Intel%e2%80%99s%20New%20CPU%20Powers%20Faster%20Vector%20Search "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-cpu-intel-benchmark%2F "LinkedIn")

#### [Anchor](https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/\#new-generation-silicon-is-a-game-changer-for-aiml-applications) New generation silicon is a game-changer for AI/ML applications

![qdrant cpu intel benchmark report](https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/qdrant-cpu-intel-benchmark.png)

> _Intel’s 5th gen Xeon processor is made for enterprise-scale operations in vector space._

Vector search is surging in popularity with institutional customers, and Intel is ready to support the emerging industry. Their latest generation CPU performed exceptionally with Qdrant, a leading vector database used for enterprise AI applications.

Intel just released the latest Xeon processor ( **codename: Emerald Rapids**) for data centers, a market which is expected to grow to $45 billion. Emerald Rapids offers higher-performance computing and significant energy efficiency over previous generations. Compared to the 4th generation Sapphire Rapids, Emerald boosts AI inference performance by up to 42% and makes vector search 38% faster.

## [Anchor](https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/\#the-cpu-of-choice-for-vector-database-operations) The CPU of choice for vector database operations

The latest generation CPU performed exceptionally in tests carried out by Qdrant’s R&D division. Intel’s CPU was stress-tested for query speed, database latency and vector upload time against massive-scale datasets. Results showed that machines with 32 cores were 1.38x faster at running queries than their previous generation counterparts. In this range, Qdrant’s latency also dropped 2.79x when compared to Sapphire.

Qdrant strongly recommends the use of Intel’s next-gen chips in the 8-64 core range. In addition to being a practical number of cores for most machines in the cloud, this compute capacity will yield the best results with mass-market use cases.

The CPU affects vector search by influencing the speed and efficiency of mathematical computations. As of recently, companies have started using GPUs to carry large workloads in AI model training and inference. However, for vector search purposes, studies show that CPU architecture is a great fit because it can handle concurrent requests with great ease.

> _“Vector search is optimized for CPUs. Intel’s new CPU brings even more performance improvement and makes vector operations blazing fast for AI applications. Customers should consider deploying more CPUs instead of GPU compute power to achieve best performance results and reduce costs simultaneously.”_
>
> - André Zayarni, Qdrant CEO

## [Anchor](https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/\#why-does-vector-search-matter)**Why does vector search matter?**

![qdrant cpu intel benchmark report](https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/qdrant-cpu-intel-benchmark-future.png)

Vector search engines empower AI to look deeper into stored data and retrieve strong relevant responses.

Qdrant’s vector database is key to modern information retrieval and machine learning systems. Those looking to run massive-scale Retrieval Augmented Generation (RAG) solutions need to leverage such semantic search engines in order to generate the best results with their AI products.

Qdrant is purpose-built to enable developers to store and search for high-dimensional vectors efficiently. It easily integrates with a host of AI/ML tools: Large Language Models (LLM), frameworks such as LangChain, LlamaIndex or Haystack, and service providers like Cohere, OpenAI, and Ollama.

## [Anchor](https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/\#supporting-enterprise-scale-aiml) Supporting enterprise-scale AI/ML

The market is preparing for a host of artificial intelligence and machine learning cases, pushing compute to the forefront of the innovation race.

The main strength of a vector database like Qdrant is that it can consistently support the user way past the prototyping and launch phases. Qdrant’s product is already being used by large enterprises with billions of data points. Such users can go from testing to production almost instantly. Those looking to host large applications might only need up to 18GB RAM to support 1 million OpenAI Vectors. This makes Qdrant the best option for maximizing resource usage and data connection.

Intel’s latest development is crucial to the future of vector databases. Vector search operations are very CPU-intensive. Therefore, Qdrant relies on the innovations made by chip makers like Intel to offer large-scale support.

> _“Vector databases are a mainstay in today’s AI/ML toolchain, powering the latest generation of RAG and other Gen AI Applications. In teaming with Qdrant, Intel is helping enterprises deliver cutting-edge Gen-AI solutions and maximize their ROI by leveraging Qdrant’s high-performant and cost-efficient vector similarity search capabilities running on latest Intel Architecture based infrastructure across deployment models.”_
>
> - Arijit Bandyopadhyay, CTO - Enterprise Analytics & AI, Head of Strategy – Cloud and Enterprise, CSV Group, Intel Corporation

## [Anchor](https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/\#advancing-vector-search-and-the-role-of-next-gen-cpus) Advancing vector search and the role of next-gen CPUs

Looking ahead, the vector database market is on the cusp of significant growth, particularly for the enterprise market. Developments in CPU technologies, such as those from Intel, are expected to enhance vector search operations by 1) improving processing speeds and 2) boosting retrieval efficiency and quality. This will allow enterprise users to easily manage large and more complex datasets and introduce AI on a global scale.

As large companies continue to integrate sophisticated AI and machine learning tools, the reliance on robust vector databases is going to increase. This evolution in the market underscores the importance of continuous hardware innovation in meeting the expanding demands of data-intensive applications, with Intel’s contributions playing a notable role in shaping the future of enterprise-scale AI/ML solutions.

## [Anchor](https://qdrant.tech/blog/qdrant-cpu-intel-benchmark/\#next-steps) Next steps

Qdrant is open source and offers a complete SaaS solution, hosted on AWS, GCP, and Azure.

Getting started is easy, either spin up a [container image](https://hub.docker.com/r/qdrant/qdrant) or start a [free Cloud instance](https://cloud.qdrant.io/login?ajs_anonymous_id=91221af5-4d35-4319-b0a2-99bda35f14d2). The documentation covers [adding the data](https://qdrant.tech/documentation/tutorials/bulk-upload/) to your Qdrant instance as well as [creating your indices](https://qdrant.tech/documentation/tutorials/optimize/). We would love to hear about what you are building and please connect with our engineering team on [Github](https://github.com/qdrant/qdrant), [Discord](https://discord.com/invite/tdtYvXjC4h), or [LinkedIn](https://www.linkedin.com/company/qdrant).

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=91221af5-4d35-4319-b0a2-99bda35f14d2)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573582690&cv=11&fst=1748573582690&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-cpu-intel-benchmark%2F&hn=www.googleadservices.com&frm=0&tiba=Intel%E2%80%99s%20New%20CPU%20Powers%20Faster%20Vector%20Search%20-%20Qdrant&npa=0&pscdl=noapi&auid=1472958087.1748573582&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573582616&cv=11&fst=1748573582616&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-cpu-intel-benchmark%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Intel%E2%80%99s%20New%20CPU%20Powers%20Faster%20Vector%20Search%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1472958087.1748573582&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=915b621e-47a0-4889-a9de-22d43411f386&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6c9a348e-2845-41d1-bc17-ce9a805e2168&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-cpu-intel-benchmark%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=915b621e-47a0-4889-a9de-22d43411f386&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6c9a348e-2845-41d1-bc17-ce9a805e2168&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-cpu-intel-benchmark%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)