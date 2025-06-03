---
url: "https://qdrant.tech/blog/qdrant-benchmarks-2024/"
title: "Qdrant Updated Benchmarks 2024 - Qdrant"
---

0

# Qdrant Updated Benchmarks 2024

Sabrina Aquino

·

January 15, 2024

![Qdrant Updated Benchmarks 2024](https://qdrant.tech/blog/qdrant-benchmarks-2024/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-benchmarks-2024%2F&text=Qdrant%20Updated%20Benchmarks%202024 "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-benchmarks-2024%2F "LinkedIn")

It’s time for an update to Qdrant’s benchmarks!

We’ve compared how Qdrant performs against the other vector search engines to give you a thorough performance analysis. Let’s get into what’s new and what remains the same in our approach.

### [Anchor](https://qdrant.tech/blog/qdrant-benchmarks-2024/\#whats-changed) What’s Changed?

#### [Anchor](https://qdrant.tech/blog/qdrant-benchmarks-2024/\#all-engines-have-improved) All engines have improved

Since the last time we ran our benchmarks, we received a bunch of suggestions on how to run other engines more efficiently, and we applied them.

This has resulted in significant improvements across all engines. As a result, we have achieved an impressive improvement of nearly four times in certain cases. You can view the previous benchmark results [here](https://qdrant.tech/benchmarks/single-node-speed-benchmark-2022/).

#### [Anchor](https://qdrant.tech/blog/qdrant-benchmarks-2024/\#introducing-a-new-dataset) Introducing a New Dataset

To ensure our benchmark aligns with the requirements of serving RAG applications at scale, the current most common use-case of vector databases, we have introduced a new dataset consisting of 1 million OpenAI embeddings.

![rps vs precision benchmark - up and to the right is better](https://qdrant.tech/blog/qdrant-updated-benchmarks-2024/rps-bench.png)

#### [Anchor](https://qdrant.tech/blog/qdrant-benchmarks-2024/\#separation-of-latency-vs-rps-cases) Separation of Latency vs RPS Cases

Different applications have distinct requirements when it comes to performance. To address this, we have made a clear separation between latency and requests-per-second (RPS) cases.

For example, a self-driving car’s object recognition system aims to process requests as quickly as possible, while a web server focuses on serving multiple clients simultaneously. By simulating both scenarios and allowing configurations for 1 or 100 parallel readers, our benchmark provides a more accurate evaluation of search engine performance.

![mean-time vs precision benchmark - down and to the right is better](https://qdrant.tech/blog/qdrant-updated-benchmarks-2024/latency-bench.png)

### [Anchor](https://qdrant.tech/blog/qdrant-benchmarks-2024/\#what-hasnt-changed) What Hasn’t Changed?

#### [Anchor](https://qdrant.tech/blog/qdrant-benchmarks-2024/\#our-principles-of-benchmarking) Our Principles of Benchmarking

At Qdrant all code stays open-source. We ensure our benchmarks are accessible for everyone, allowing you to run them on your own hardware. Your input matters to us, and contributions and sharing of best practices are welcome!

Our benchmarks are strictly limited to open-source solutions, ensuring hardware parity and avoiding biases from external cloud components.

We deliberately don’t include libraries or algorithm implementations in our comparisons because our focus is squarely on vector databases.

Why?

Because libraries like FAISS, while useful for experiments, don’t fully address the complexities of real-world production environments. They lack features like real-time updates, CRUD operations, high availability, scalability, and concurrent access – essentials in production scenarios. A vector search engine is not only its indexing algorithm, but its overall performance in production.

We use the same benchmark datasets as the [ann-benchmarks](https://github.com/erikbern/ann-benchmarks/#data-sets) project so you can compare our performance and accuracy against it.

### [Anchor](https://qdrant.tech/blog/qdrant-benchmarks-2024/\#detailed-report-and-access) Detailed Report and Access

For an in-depth look at our latest benchmark results, we invite you to read the [detailed report](https://qdrant.tech/benchmarks/).

If you’re interested in testing the benchmark yourself or want to contribute to its development, head over to our [benchmark repository](https://github.com/qdrant/vector-db-benchmark). We appreciate your support and involvement in improving the performance of vector databases.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=385ac94f-afd7-43c0-87aa-6d23ef4ef39d)

![](https://qdrant.tech/img/rocket.svg)

Up![iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574467407&cv=11&fst=1748574467407&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-benchmarks-2024%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Updated%20Benchmarks%202024%20-%20Qdrant&npa=0&pscdl=noapi&auid=1976017716.1748574467&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574467364&cv=11&fst=1748574467364&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-benchmarks-2024%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Updated%20Benchmarks%202024%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1976017716.1748574467&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=74fe55b5-f76b-42c4-92c2-e538d81c7a7c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b90fd42f-a7aa-4ff6-aef2-773c9297b101&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-benchmarks-2024%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=74fe55b5-f76b-42c4-92c2-e538d81c7a7c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b90fd42f-a7aa-4ff6-aef2-773c9297b101&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-benchmarks-2024%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

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

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=abc592785b703d7c5ca6e668b994fae3&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574468302&cv=11&fst=1748574468302&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-benchmarks-2024%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Updated%20Benchmarks%202024%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1976017716.1748574467&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)