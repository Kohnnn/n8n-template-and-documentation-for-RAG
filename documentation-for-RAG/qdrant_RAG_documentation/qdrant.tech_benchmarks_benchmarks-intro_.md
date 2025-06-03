---
url: "https://qdrant.tech/benchmarks/benchmarks-intro/"
title: "How vector search should be benchmarked? - Qdrant"
---

# How vector search should be benchmarked?

January 01, 0001

# [Anchor](https://qdrant.tech/benchmarks/benchmarks-intro/\#benchmarking-vector-databases) Benchmarking Vector Databases

At Qdrant, performance is the top-most priority. We always make sure that we use system resources efficiently so you get the **fastest and most accurate results at the cheapest cloud costs**. So all of our decisions from [choosing Rust](https://qdrant.tech/articles/why-rust/), [io optimisations](https://qdrant.tech/articles/io_uring/), [serverless support](https://qdrant.tech/articles/serverless/), [binary quantization](https://qdrant.tech/articles/binary-quantization/), to our [fastembed library](https://qdrant.tech/articles/fastembed/) are all based on our principle. In this article, we will compare how Qdrant performs against the other vector search engines.

Here are the principles we followed while designing these benchmarks:

- We do comparative benchmarks, which means we focus on **relative numbers** rather than absolute numbers.
- We use affordable hardware, so that you can reproduce the results easily.
- We run benchmarks on the same exact machines to avoid any possible hardware bias.
- All the benchmarks are [open-sourced](https://github.com/qdrant/vector-db-benchmark), so you can contribute and improve them.

Scenarios we tested

1. Upload & Search benchmark on single node [Benchmark](https://qdrant.tech/benchmarks/single-node-speed-benchmark/)
2. Filtered search benchmark - [Benchmark](https://qdrant.tech/benchmarks/#filtered-search-benchmark)
3. Memory consumption benchmark - Coming soon
4. Cluster mode benchmark - Coming soon

Some of our experiment design decisions are described in the [F.A.Q Section](https://qdrant.tech/benchmarks/#benchmarks-faq).
Reach out to us on our [Discord channel](https://qdrant.to/discord) if you want to discuss anything related Qdrant or these benchmarks.

Share this article

[x](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmarks-intro%2F&text=How%20vector%20search%20should%20be%20benchmarked? "x")[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmarks-intro%2F "LinkedIn")

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574454830&cv=11&fst=1748574454830&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmarks-intro%2F&hn=www.googleadservices.com&frm=0&tiba=How%20vector%20search%20should%20be%20benchmarked%3F%20-%20Qdrant&npa=0&pscdl=noapi&auid=1199196164.1748574455&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574454772&cv=11&fst=1748574454772&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmarks-intro%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=How%20vector%20search%20should%20be%20benchmarked%3F%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1199196164.1748574455&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4cbfacad-7b74-4b01-9d54-1d3a21bbfcad&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e63d58b0-5b87-4bae-86e8-96bef35fddce&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmarks-intro%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4cbfacad-7b74-4b01-9d54-1d3a21bbfcad&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e63d58b0-5b87-4bae-86e8-96bef35fddce&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fbenchmarks%2Fbenchmarks-intro%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)