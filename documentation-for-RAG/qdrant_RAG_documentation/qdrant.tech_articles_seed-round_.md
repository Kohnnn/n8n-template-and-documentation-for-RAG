---
url: "https://qdrant.tech/articles/seed-round/"
title: "On Unstructured Data, Vector Databases, New AI Age, and Our Seed Round. - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- On Unstructured Data, Vector Databases, New AI Age, and Our Seed Round.

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# On Unstructured Data, Vector Databases, New AI Age, and Our Seed Round.

Andre Zayarni

·

April 19, 2023

![On Unstructured Data, Vector Databases, New AI Age, and Our Seed Round.](https://qdrant.tech/articles_data/seed-round/preview/title.jpg)

> Vector databases are here to stay. The New Age of AI is powered by vector embeddings, and vector databases are a foundational part of the stack. At Qdrant, we are working on cutting-edge open-source vector similarity search solutions to power fantastic AI applications with the best possible performance and excellent developer experience.
>
> Our 7.5M seed funding – led by [Unusual Ventures](https://www.unusual.vc/), awesome angels, and existing investors – will help us bring these innovations to engineers and empower them to make the most of their unstructured data and the awesome power of LLMs at any scale.

We are thrilled to announce that we just raised our seed round from the best possible investor we could imagine for this stage. Let’s talk about fundraising later – it is a story itself that I could probably write a bestselling book about. First, let’s dive into a bit of background about our project, our progress, and future plans.

## [Anchor](https://qdrant.tech/articles/seed-round/\#a-need-for-vector-databases) A need for vector databases.

Unstructured data is growing exponentially, and we are all part of a huge unstructured data workforce. This blog post is unstructured data; your visit here produces unstructured and semi-structured data with every web interaction, as does every photo you take or email you send. The global datasphere will grow to [165 zettabytes by 2025](https://github.com/qdrant/qdrant/pull/1639), and about 80% of that will be unstructured. At the same time, the rising demand for AI is vastly outpacing existing infrastructure. Around 90% of machine learning research results fail to reach production because of a lack of tools.

![Vector Databases Demand](https://qdrant.tech/articles_data/seed-round/demand.png)

Demand for AI tools

Thankfully there’s a new generation of tools that let developers work with unstructured data in the form of vector embeddings, which are deep representations of objects obtained from a neural network model. A vector database, also known as a vector similarity search engine or approximate nearest neighbour (ANN) search database, is a database designed to store, manage, and search high-dimensional data with an additional payload. Vector Databases turn research prototypes into commercial AI products. Vector search solutions are industry agnostic and bring solutions for a number of use cases, including classic ones like semantic search, matching engines, and recommender systems to more novel applications like anomaly detection, working with time series, or biomedical data. The biggest limitation is to have a neural network encoder in place for the data type you are working with.

![Vector Search Use Cases](https://qdrant.tech/articles_data/seed-round/use-cases.png)

Vector Search Use Cases

With the rise of large language models (LLMs), Vector Databases have become the fundamental building block of the new AI Stack. They let developers build even more advanced applications by extending the “knowledge base” of LLMs-based applications like ChatGPT with real-time and real-world data.

A new AI product category, “Co-Pilot for X,” was born and is already affecting how we work. Starting from producing content to developing software. And this is just the beginning, there are even more types of novel applications being developed on top of this stack.

![New AI Stack](https://qdrant.tech/articles_data/seed-round/ai-stack.png)

New AI Stack

## [Anchor](https://qdrant.tech/articles/seed-round/\#enter-qdrant) Enter Qdrant.

At the same time, adoption has only begun. Vector Search Databases are replacing VSS libraries like FAISS, etc., which, despite their disadvantages, are still used by ~90% of projects out there They’re hard-coupled to the application code, lack of production-ready features like basic CRUD operations or advanced filtering, are a nightmare to maintain and scale and have many other difficulties that make life hard for developers.

The current Qdrant ecosystem consists of excellent products to work with vector embeddings. We launched our managed vector database solution, Qdrant Cloud, early this year, and it is already serving more than 1,000 Qdrant clusters. We are extending our offering now with managed on-premise solutions for enterprise customers.

![Qdrant Vector Database Ecosystem](https://qdrant.tech/articles_data/seed-round/ecosystem.png)

Qdrant Ecosystem

Our plan for the current [open-source roadmap](https://github.com/qdrant/qdrant/blob/master/docs/roadmap/README.md) is to make billion-scale vector search affordable. Our recent release of the [Scalar Quantization](https://qdrant.tech/articles/scalar-quantization/) improves both memory usage (x4) as well as speed (x2). Upcoming [Product Quantization](https://www.irisa.fr/texmex/people/jegou/papers/jegou_searching_with_quantization.pdf) will introduce even another option with more memory saving. Stay tuned.

Qdrant started more than two years ago with the mission of building a vector database powered by a well-thought-out tech stack. Using Rust as the system programming language and technical architecture decision during the development of the engine made Qdrant the leading and one of the most popular vector database solutions.

Our unique custom modification of the [HNSW algorithm](https://qdrant.tech/articles/filtrable-hnsw/) for Approximate Nearest Neighbor Search (ANN) allows querying the result with a state-of-the-art speed and applying filters without compromising on results. Cloud-native support for distributed deployment and replications makes the engine suitable for high-throughput applications with real-time latency requirements. Rust brings stability, efficiency, and the possibility to make optimization on a very low level. In general, we always aim for the best possible results in [performance](https://qdrant.tech/benchmarks/), code quality, and feature set.

Most importantly, we want to say a big thank you to our [open-source community](https://qdrant.to/discord), our adopters, our contributors, and our customers. Your active participation in the development of our products has helped make Qdrant the best vector database on the market. I cannot imagine how we could do what we’re doing without the community or without being open-source and having the TRUST of the engineers. Thanks to all of you!

I also want to thank our team. Thank you for your patience and trust. Together we are strong. Let’s continue doing great things together.

## [Anchor](https://qdrant.tech/articles/seed-round/\#fundraising) Fundraising

The whole process took only a couple of days, we got several offers, and most probably, we would get more with different conditions. We decided to go with Unusual Ventures because they truly understand how things work in the open-source space. They just did it right.

Here is a big piece of advice for all investors interested in open-source: Dive into the community, and see and feel the traction and product feedback instead of looking at glossy pitch decks. With Unusual on our side, we have an active operational partner instead of one who simply writes a check. That help is much more important than overpriced valuations and big shiny names.

Ultimately, the community and adopters will decide what products win and lose, not VCs. Companies don’t need crazy valuations to create products that customers love. You do not need Ph.D. to innovate. You do not need to over-engineer to build a scalable solution. You do not need ex-FANG people to have a great team. You need clear focus, a passion for what you’re building, and the know-how to do it well.

We know how.

PS: This text is written by me in an old-school way without any ChatGPT help. Sometimes you just need inspiration instead of AI ;-)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/seed-round.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/seed-round.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574471658&cv=11&fst=1748574471658&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fseed-round%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=On%20Unstructured%20Data%2C%20Vector%20Databases%2C%20New%20AI%20Age%2C%20and%20Our%20Seed%20Round.%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=651557224.1748574472&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574471705&cv=11&fst=1748574471705&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fseed-round%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=On%20Unstructured%20Data%2C%20Vector%20Databases%2C%20New%20AI%20Age%2C%20and%20Our%20Seed%20Round.%20-%20Qdrant&npa=0&pscdl=noapi&auid=651557224.1748574472&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1996ec7b-8fb2-4241-9b65-2d50148a99dc&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d55f65e6-5ac9-4539-a249-86add3b215d0&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fseed-round%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1996ec7b-8fb2-4241-9b65-2d50148a99dc&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d55f65e6-5ac9-4539-a249-86add3b215d0&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fseed-round%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574472714&cv=11&fst=1748574472714&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fseed-round%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=On%20Unstructured%20Data%2C%20Vector%20Databases%2C%20New%20AI%20Age%2C%20and%20Our%20Seed%20Round.%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=651557224.1748574472&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)