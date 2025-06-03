---
url: "https://qdrant.tech/articles/rag-is-dead/"
title: "Is RAG Dead? The Role of Vector Databases in Vector Search | Qdrant - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Is RAG Dead? The Role of Vector Databases in Vector Search \| Qdrant

[Back to RAG & GenAI](https://qdrant.tech/articles/rag-and-genai/)

# Is RAG Dead? The Role of Vector Databases in Vector Search \| Qdrant

David Myriel

·

February 27, 2024

![Is RAG Dead? The Role of Vector Databases in Vector Search | Qdrant](https://qdrant.tech/articles_data/rag-is-dead/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/rag-is-dead/\#is-rag-dead-the-role-of-vector-databases-in-ai-efficiency-and-vector-search) Is RAG Dead? The Role of Vector Databases in AI Efficiency and Vector Search

When Anthropic came out with a context window of 100K tokens, they said: “ _[Vector search](https://qdrant.tech/solutions/) is dead. LLMs are getting more accurate and won’t need RAG anymore._”

Google’s Gemini 1.5 now offers a context window of 10 million tokens. [Their supporting paper](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf) claims victory over accuracy issues, even when applying Greg Kamradt’s [NIAH methodology](https://twitter.com/GregKamradt/status/1722386725635580292).

_It’s over. [RAG](https://qdrant.tech/articles/what-is-rag-in-ai/) (Retrieval Augmented Generation) must be completely obsolete now. Right?_

No.

Larger context windows are never the solution. Let me repeat. Never. They require more computational resources and lead to slower processing times.

The community is already stress testing Gemini 1.5:

![RAG and Gemini 1.5](https://qdrant.tech/articles_data/rag-is-dead/rag-is-dead-1.png)

This is not surprising. LLMs require massive amounts of compute and memory to run. To cite Grant, running such a model by itself “would deplete a small coal mine to generate each completion”. Also, who is waiting 30 seconds for a response?

## [Anchor](https://qdrant.tech/articles/rag-is-dead/\#context-stuffing-is-not-the-solution) Context stuffing is not the solution

> Relying on context is expensive, and it doesn’t improve response quality in real-world applications. Retrieval based on [vector search](https://qdrant.tech/solutions/) offers much higher precision.

If you solely rely on an [LLM](https://qdrant.tech/articles/what-is-rag-in-ai/) to perfect retrieval and precision, you are doing it wrong.

A large context window makes it harder to focus on relevant information. This increases the risk of errors or hallucinations in its responses.

Google found Gemini 1.5 significantly more accurate than GPT-4 at shorter context lengths and “a very small decrease in recall towards 1M tokens”. The recall is still below 0.8.

![Gemini 1.5 Data](https://qdrant.tech/articles_data/rag-is-dead/rag-is-dead-2.png)

We don’t think 60-80% is good enough. The LLM might retrieve enough relevant facts in its context window, but it still loses up to 40% of the available information.

> The whole point of vector search is to circumvent this process by efficiently picking the information your app needs to generate the best response. A [vector database](https://qdrant.tech/) keeps the compute load low and the query response fast. You don’t need to wait for the LLM at all.

Qdrant’s benchmark results are strongly in favor of accuracy and efficiency. We recommend that you consider them before deciding that an LLM is enough. Take a look at our [open-source benchmark reports](https://qdrant.tech/benchmarks/) and [try out the tests](https://github.com/qdrant/vector-db-benchmark) yourself.

## [Anchor](https://qdrant.tech/articles/rag-is-dead/\#vector-search-in-compound-systems) Vector search in compound systems

The future of AI lies in careful system engineering. As per [Zaharia et al.](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/), results from Databricks find that “60% of LLM applications use some form of RAG, while 30% use multi-step chains.”

Even Gemini 1.5 demonstrates the need for a complex strategy. When looking at [Google’s MMLU Benchmark](https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf), the model was called 32 times to reach a score of 90.0% accuracy. This shows us that even a basic compound arrangement is superior to monolithic models.

As a retrieval system, a [vector database](https://qdrant.tech/) perfectly fits the need for compound systems. Introducing them into your design opens the possibilities for superior applications of LLMs. It is superior because it’s faster, more accurate, and much cheaper to run.

> The key advantage of RAG is that it allows an LLM to pull in real-time information from up-to-date internal and external knowledge sources, making it more dynamic and adaptable to new information. - Oliver Molander, CEO of IMAGINAI

## [Anchor](https://qdrant.tech/articles/rag-is-dead/\#qdrant-scales-to-enterprise-rag-scenarios) Qdrant scales to enterprise RAG scenarios

People still don’t understand the economic benefit of vector databases. Why would a large corporate AI system need a standalone vector database like [Qdrant](https://qdrant.tech/)? In our minds, this is the most important question. Let’s pretend that LLMs cease struggling with context thresholds altogether.

**How much would all of this cost?**

If you are running a RAG solution in an enterprise environment with petabytes of private data, your compute bill will be unimaginable. Let’s assume 1 cent per 1K input tokens (which is the current GPT-4 Turbo pricing). Whatever you are doing, every time you go 100 thousand tokens deep, it will cost you $1.

That’s a buck a question.

> According to our estimations, vector search queries are **at least** 100 million times cheaper than queries made by LLMs.

Conversely, the only up-front investment with vector databases is the indexing (which requires more compute). After this step, everything else is a breeze. Once setup, Qdrant easily scales via [features like Multitenancy and Sharding](https://qdrant.tech/articles/multitenancy/). This lets you scale up your reliance on the vector retrieval process and minimize your use of the compute-heavy LLMs. As an optimization measure, Qdrant is irreplaceable.

Julien Simon from HuggingFace says it best:

> RAG is not a workaround for limited context size. For mission-critical enterprise use cases, RAG is a way to leverage high-value, proprietary company knowledge that will never be found in public datasets used for LLM training. At the moment, the best place to index and query this knowledge is some sort of vector index. In addition, RAG downgrades the LLM to a writing assistant. Since built-in knowledge becomes much less important, a nice small 7B open-source model usually does the trick at a fraction of the cost of a huge generic model.

## [Anchor](https://qdrant.tech/articles/rag-is-dead/\#get-superior-accuracy-with-qdrants-vector-database) Get superior accuracy with Qdrant’s vector database

As LLMs continue to require enormous computing power, users will need to leverage vector search and [RAG](https://qdrant.tech/rag/rag-evaluation-guide/).

Our customers remind us of this fact every day. As a product, [our vector database](https://qdrant.tech/) is highly scalable and business-friendly. We develop our features strategically to follow our company’s Unix philosophy.

We want to keep Qdrant compact, efficient and with a focused purpose. This purpose is to empower our customers to use it however they see fit.

When large enterprises release their generative AI into production, they need to keep costs under control, while retaining the best possible quality of responses. Qdrant has the [vector search solutions](https://qdrant.tech/solutions/) to do just that. Revolutionize your vector search capabilities and get started with [a Qdrant demo](https://qdrant.tech/contact-us/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/rag-is-dead.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/rag-is-dead.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574284472&cv=11&fst=1748574284472&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Frag-is-dead%2F&hn=www.googleadservices.com&frm=0&tiba=Is%20RAG%20Dead%3F%20The%20Role%20of%20Vector%20Databases%20in%20Vector%20Search%20%7C%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=1477635149.1748574284&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574284450&cv=11&fst=1748574284450&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Frag-is-dead%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Is%20RAG%20Dead%3F%20The%20Role%20of%20Vector%20Databases%20in%20Vector%20Search%20%7C%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1477635149.1748574284&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5ef34a91-8cff-470e-bd27-3e43b8af1b60&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c3abceef-892e-4bcc-bfa5-2acb6d5bc1a0&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Frag-is-dead%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=5ef34a91-8cff-470e-bd27-3e43b8af1b60&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c3abceef-892e-4bcc-bfa5-2acb6d5bc1a0&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Frag-is-dead%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574285435&cv=11&fst=1748574285435&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Frag-is-dead%2F&hn=www.googleadservices.com&frm=0&tiba=Is%20RAG%20Dead%3F%20The%20Role%20of%20Vector%20Databases%20in%20Vector%20Search%20%7C%20Qdrant%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1477635149.1748574284&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)