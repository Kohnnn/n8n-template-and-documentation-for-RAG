---
url: "https://qdrant.tech/benchmarks/benchmark-faq/"
title: "Benchmarks F.A.Q. - Qdrant"
---

# Benchmarks F.A.Q.

January 01, 0001

# [Anchor](https://qdrant.tech/benchmarks/benchmark-faq/\#benchmarks-faq) Benchmarks F.A.Q.

## [Anchor](https://qdrant.tech/benchmarks/benchmark-faq/\#are-we-biased) Are we biased?

Probably, yes. Even if we try to be objective, we are not experts in using all the existing vector databases.
We build Qdrant and know the most about it.
Due to that, we could have missed some important tweaks in different vector search engines.

However, we tried our best, kept scrolling the docs up and down, experimented with combinations of different configurations, and gave all of them an equal chance to stand out. If you believe you can do it better than us, our **benchmarks are fully [open-sourced](https://github.com/qdrant/vector-db-benchmark), and contributions are welcome**!

## [Anchor](https://qdrant.tech/benchmarks/benchmark-faq/\#what-do-we-measure) What do we measure?

There are several factors considered while deciding on which database to use.
Of course, some of them support a different subset of functionalities, and those might be a key factor to make the decision.
But in general, we all care about the search precision, speed, and resources required to achieve it.

There is one important thing - **the speed of the vector databases should to be compared only if they achieve the same precision**. Otherwise, they could maximize the speed factors by providing inaccurate results, which everybody would rather avoid. Thus, our benchmark results are compared only at a specific search precision threshold.

## [Anchor](https://qdrant.tech/benchmarks/benchmark-faq/\#how-we-select-hardware) How we select hardware?

In our experiments, we are not focusing on the absolute values of the metrics but rather on a relative comparison of different engines.
What is important is the fact we used the same machine for all the tests.
It was just wiped off between launching different engines.

We selected an average machine, which you can easily rent from almost any cloud provider. No extra quota or custom configuration is required.

## [Anchor](https://qdrant.tech/benchmarks/benchmark-faq/\#why-you-are-not-comparing-with-faiss-or-annoy) Why you are not comparing with FAISS or Annoy?

Libraries like FAISS provide a great tool to do experiments with vector search. But they are far away from real usage in production environments.
If you are using FAISS in production, in the best case, you never need to update it in real-time. In the worst case, you have to create your custom wrapper around it to support CRUD, high availability, horizontal scalability, concurrent access, and so on.

Some vector search engines even use FAISS under the hood, but a search engine is much more than just an indexing algorithm.

We do, however, use the same benchmark datasets as the famous [ann-benchmarks project](https://github.com/erikbern/ann-benchmarks), so you can align your expectations for any practical reasons.

### [Anchor](https://qdrant.tech/benchmarks/benchmark-faq/\#why-we-decided-to-test-with-the-python-client) Why we decided to test with the Python client

There is no consensus when it comes to the best technology to run benchmarks. You’re free to choose Go, Java or Rust-based systems. But there are two main reasons for us to use Python for this:

1. While generating embeddings you’re most likely going to use Python and python based ML frameworks.
2. Based on GitHub stars, python clients are one of the most popular clients across all the engines.

From the user’s perspective, the crucial thing is the latency perceived while using a specific library - in most cases a Python client.
Nobody can and even should redefine the whole technology stack, just because of using a specific search tool.
That’s why we decided to focus primarily on official Python libraries, provided by the database authors.
Those may use some different protocols under the hood, but at the end of the day, we do not care how the data is transferred, as long as it ends up in the target location.

## [Anchor](https://qdrant.tech/benchmarks/benchmark-faq/\#what-about-closed-source-saas-platforms) What about closed-source SaaS platforms?

There are some vector databases available as SaaS only so that we couldn’t test them on the same machine as the rest of the systems.
That makes the comparison unfair. That’s why we purely focused on testing the Open Source vector databases, so everybody may reproduce the benchmarks easily.

This is not the final list, and we’ll continue benchmarking as many different engines as possible.

## [Anchor](https://qdrant.tech/benchmarks/benchmark-faq/\#how-to-reproduce-the-benchmark) How to reproduce the benchmark?

The source code is available on [Github](https://github.com/qdrant/vector-db-benchmark) and has a `README.md` file describing the process of running the benchmark for a specific engine.

## [Anchor](https://qdrant.tech/benchmarks/benchmark-faq/\#how-to-contribute) How to contribute?

We made the benchmark Open Source because we believe that it has to be transparent. We could have misconfigured one of the engines or just done it inefficiently. If you feel like you could help us out, check out our [benchmark repository](https://github.com/qdrant/vector-db-benchmark).

Share this article

[x](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmark-faq%2F&text=Benchmarks%20F.A.Q. "x")[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmark-faq%2F "LinkedIn")

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574251372&cv=11&fst=1748574251372&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmark-faq%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Benchmarks%20F.A.Q.%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=826641174.1748574251&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574251590&cv=11&fst=1748574251590&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmark-faq%2F&hn=www.googleadservices.com&frm=0&tiba=Benchmarks%20F.A.Q.%20-%20Qdrant&npa=0&pscdl=noapi&auid=826641174.1748574251&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7fd5013b-dd39-4408-be7a-f107138521f6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7eda97c4-7a06-44ea-a45e-5bb0cd349110&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmark-faq%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574252485&cv=11&fst=1748574252485&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmark-faq%2F&hn=www.googleadservices.com&frm=0&tiba=Benchmarks%20F.A.Q.%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=826641174.1748574251&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7fd5013b-dd39-4408-be7a-f107138521f6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=7eda97c4-7a06-44ea-a45e-5bb0cd349110&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmark-faq%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)