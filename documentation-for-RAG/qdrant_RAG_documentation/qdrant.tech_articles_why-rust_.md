---
url: "https://qdrant.tech/articles/why-rust/"
title: "Why Rust? - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Why Rust?

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# Why Rust?

Andre Bogus

·

May 11, 2023

![Why Rust?](https://qdrant.tech/articles_data/why-rust/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/why-rust/\#building-qdrant-in-rust) Building Qdrant in Rust

Looking at the [github repository](https://github.com/qdrant/qdrant), you can see that Qdrant is built in [Rust](https://rust-lang.org/). Other offerings may be written in C++, Go, Java or even Python. So why does Qdrant chose Rust? Our founder Andrey had built the first prototype in C++, but didn’t trust his command of the language to scale to a production system (to be frank, he likened it to cutting his leg off). He was well versed in Java and Scala and also knew some Python. However, he considered neither a good fit:

**Java** is also more than 30 years old now. With a throughput-optimized VM it can often at least play in the same ball park as native services, and the tooling is phenomenal. Also portability is surprisingly good, although the GC is not suited for low-memory applications and will generally take good amount of RAM to deliver good performance. That said, the focus on throughput led to the dreaded GC pauses that cause latency spikes. Also the fat runtime incurs high start-up delays, which need to be worked around.

**Scala** also builds on the JVM, although there is a native compiler, there was the question of compatibility. So Scala shared the limitations of Java, and although it has some nice high-level amenities (of which Java only recently copied a subset), it still doesn’t offer the same level of control over memory layout as, say, C++, so it is similarly disqualified.

**Python**, being just a bit younger than Java, is ubiquitous in ML projects, mostly owing to its tooling (notably jupyter notebooks), being easy to learn and integration in most ML stacks. It doesn’t have a traditional garbage collector, opting for ubiquitous reference counting instead, which somewhat helps memory consumption. With that said, unless you only use it as glue code over high-perf modules, you may find yourself waiting for results. Also getting complex python services to perform stably under load is a serious technical challenge.

## [Anchor](https://qdrant.tech/articles/why-rust/\#into-the-unknown) Into the Unknown

So Andrey looked around at what younger languages would fit the challenge. After some searching, two contenders emerged: Go and Rust. Knowing neither, Andrey consulted the docs, and found hinself intrigued by Rust with its promise of Systems Programming without pervasive memory unsafety.

This early decision has been validated time and again. When first learning Rust, the compiler’s error messages are very helpful (and have only improved in the meantime). It’s easy to keep memory profile low when one doesn’t have to wrestle a garbage collector and has complete control over stack and heap. Apart from the much advertised memory safety, many footguns one can run into when writing C++ have been meticulously designed out. And it’s much easier to parallelize a task if one doesn’t have to fear data races.

With Qdrant written in Rust, we can offer cloud services that don’t keep us awake at night, thanks to Rust’s famed robustness. A current qdrant docker container comes in at just a bit over 50MB — try that for size. As for performance… have some [benchmarks](https://qdrant.tech/benchmarks/).

And we don’t have to compromise on ergonomics either, not for us nor for our users. Of course, there are downsides: Rust compile times are usually similar to C++’s, and though the learning curve has been considerably softened in the last years, it’s still no match for easy-entry languages like Python or Go. But learning it is a one-time cost. Contrast this with Go, where you may find [the apparent simplicity is only skin-deep](https://fasterthanli.me/articles/i-want-off-mr-golangs-wild-ride).

## [Anchor](https://qdrant.tech/articles/why-rust/\#smooth-is-fast) Smooth is Fast

The complexity of the type system pays large dividends in bugs that didn’t even make it to a commit. The ecosystem for web services is also already quite advanced, perhaps not at the same point as Java, but certainly matching or outcompeting Go.

Some people may think that the strict nature of Rust will slow down development, which is true only insofar as it won’t let you cut any corners. However, experience has conclusively shown that this is a net win. In fact, Rust lets us [ride the wall](https://the-race.com/nascar/bizarre-wall-riding-move-puts-chastain-into-nascar-folklore/), which makes us faster, not slower.

The job market for Rust programmers is certainly not as big as that for Java or Python programmers, but the language has finally reached the mainstream, and we don’t have any problems getting and retaining top talent. And being an open source project, when we get contributions, we don’t have to check for a wide variety of errors that Rust already rules out.

## [Anchor](https://qdrant.tech/articles/why-rust/\#in-rust-we-trust) In Rust We Trust

Finally, the Rust community is a very friendly bunch, and we are delighted to be part of that. And we don’t seem to be alone. Most large IT companies (notably Amazon, Google, Huawei, Meta and Microsoft) have already started investing in Rust. It’s in the Windows font system already and in the process of coming to the Linux kernel (build support has already been included). In machine learning applications, Rust has been tried and proven by the likes of Aleph Alpha and Huggingface, among many others.

To sum up, choosing Rust was a lucky guess that has brought huge benefits to Qdrant. Rust continues to be our not-so-secret weapon.

### [Anchor](https://qdrant.tech/articles/why-rust/\#key-takeaways) Key Takeaways:

- **Rust’s Advantages for Qdrant:** Rust provides memory safety and control without a garbage collector, which is crucial for Qdrant’s high-performance cloud services.

- **Low Overhead:** Qdrant’s Rust-based system offers efficiency, with small Docker container sizes and robust performance benchmarks.

- **Complexity vs. Simplicity:** Rust’s strict type system reduces bugs early in development, making it faster in the long run despite initial learning curves.

- **Adoption by Major Players:** Large tech companies like Amazon, Google, and Microsoft are embracing Rust, further validating Qdrant’s choice.

- **Community and Talent:** The supportive Rust community and increasing availability of Rust developers make it easier for Qdrant to grow and innovate.


##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/why-rust.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/why-rust.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574196232&cv=11&fst=1748574196232&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhy-rust%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Why%20Rust%3F%20-%20Qdrant&npa=0&pscdl=noapi&auid=101671091.1748574196&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574196197&cv=11&fst=1748574196197&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhy-rust%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Why%20Rust%3F%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=101671091.1748574196&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=bef8b404-c922-4aff-b88b-163a94bfc0c6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e65a78cb-00bd-445e-93c9-0c7033283119&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhy-rust%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=bef8b404-c922-4aff-b88b-163a94bfc0c6&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e65a78cb-00bd-445e-93c9-0c7033283119&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhy-rust%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574197053&cv=11&fst=1748574197053&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fwhy-rust%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Why%20Rust%3F%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=101671091.1748574196&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)