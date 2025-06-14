---
url: "https://qdrant.tech/blog/case-study-bloop/"
title: "Powering Bloop semantic code search - Qdrant"
---

0

# Powering Bloop semantic code search

Qdrant Team

·

February 28, 2023

![Powering Bloop semantic code search](https://qdrant.tech/blog/case-study-bloop/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-bloop%2F&text=Powering%20Bloop%20semantic%20code%20search "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-bloop%2F "LinkedIn")

Founded in early 2021, [bloop](https://bloop.ai/) was one of the first companies to tackle semantic
search for codebases. A fast, reliable Vector Search Database is a core component of a semantic
search engine, and bloop surveyed the field of available solutions and even considered building
their own. They found Qdrant to be the top contender and now use it in production.

This document is intended as a guide for people who intend to introduce semantic search to a novel
field and want to find out if Qdrant is a good solution for their use case.

## [Anchor](https://qdrant.tech/blog/case-study-bloop/\#about-bloop) About bloop

![](https://qdrant.tech/case-studies/bloop/screenshot.png)

[bloop](https://bloop.ai/) is a fast code-search engine that combines semantic search, regex search
and precise code navigation into a single lightweight desktop application that can be run locally. It
helps developers understand and navigate large codebases, enabling them to discover internal libraries,
reuse code and avoid dependency bloat. bloop’s chat interface explains complex concepts in simple
language so that engineers can spend less time crawling through code to understand what it does, and
more time shipping features and fixing bugs.

![](https://qdrant.tech/case-studies/bloop/bloop-logo.png)

bloop’s mission is to make software engineers autonomous and semantic code search is the cornerstone
of that vision. The project is maintained by a group of Rust and Typescript engineers and ML researchers.
It leverages many prominent nascent technologies, such as [Tauri](http://tauri.app/), [tantivy](https://docs.rs/tantivy),
[Qdrant](https://github.com/qdrant/qdrant) and [Anthropic](https://www.anthropic.com/).

## [Anchor](https://qdrant.tech/blog/case-study-bloop/\#about-qdrant) About Qdrant

![](https://qdrant.tech/case-studies/bloop/qdrant-logo.png)

Qdrant is an open-source Vector Search Database written in Rust . It deploys as an API service providing
a search for the nearest high-dimensional vectors. With Qdrant, embeddings or neural network encoders
can be turned into full-fledged applications for matching, searching, recommending, and many more solutions
to make the most of unstructured data. It is easy to use, deploy and scale, blazing fast and is accurate
simultaneously.

Qdrant was founded in 2021 in Berlin by Andre Zayarni and Andrey Vasnetsov with the mission to power the
next generation of AI applications with advanced and high-performant [vector similarity](https://qdrant.tech/articles/vector-similarity-beyond-search/) search technology.
Their flagship product is the vector search database which is available as an open source
[https://github.com/qdrant/qdrant](https://github.com/qdrant/qdrant) or managed cloud solution [https://cloud.qdrant.io/](https://cloud.qdrant.io/?ajs_anonymous_id=13f8a6ce-9b61-4547-932d-be245dd161fc).

## [Anchor](https://qdrant.tech/blog/case-study-bloop/\#the-problem) The Problem

Firstly, what is semantic search? It’s finding relevant information by comparing meaning, rather than
simply measuring the textual overlap between queries and documents. We compare meaning by comparing
_embeddings_ \- these are vector representations of text that are generated by a neural network. Each document’s
embedding denotes a position in a _latent_ space, so to search you embed the query and find its nearest document
vectors in that space.

![](https://qdrant.tech/case-studies/bloop/vector-space.png)

Why is semantic search so useful for code? As engineers, we often don’t know - or forget - the precise terms
needed to find what we’re looking for. Semantic search enables us to find things without knowing the exact
terminology. For example, if an engineer wanted to understand “ _What library is used for payment processing?_”
a semantic code search engine would be able to retrieve results containing “ _Stripe_” or “ _PayPal_”. A traditional
lexical search engine would not.

One peculiarity of this problem is that the **usefulness of the solution increases with the size of the code**
**base** – if you only have one code file, you’ll be able to search it quickly, but you’ll easily get lost in
thousands, let alone millions of lines of code. Once a codebase reaches a certain size, it is no longer
possible for a single engineer to have read every single line, and so navigating large codebases becomes
extremely cumbersome.

In software engineering, we’re always dealing with complexity. Programming languages, frameworks and tools
have been developed that allow us to modularize, abstract and compile code into libraries for reuse. Yet we
still hit limits: Abstractions are still leaky, and while there have been great advances in reducing incidental
complexity, there is still plenty of intrinsic complexity[1](https://qdrant.tech/blog/case-study-bloop/#fn:1) in the problems we solve, and with software eating
the world, the growth of complexity to tackle has outrun our ability to contain it. Semantic code search helps
us navigate these inevitably complex systems.

But semantic search shouldn’t come at the cost of speed. Search should still feel instantaneous, even when
searching a codebase as large as Rust (which has over 2.8 million lines of code!). Qdrant gives bloop excellent
semantic search performance whilst using a reasonable amount of resources, so they can handle concurrent search
requests.

## [Anchor](https://qdrant.tech/blog/case-study-bloop/\#the-upshot) The Upshot

[bloop](https://bloop.ai/) are really happy with how Qdrant has slotted into their semantic code search engine:
it’s performant and reliable, even for large codebases. And it’s written in Rust(!) with an easy to integrate
qdrant-client crate. In short, Qdrant has helped keep bloop’s code search fast, accurate and reliable.

#### [Anchor](https://qdrant.tech/blog/case-study-bloop/\#footnotes) Footnotes:

* * *

1. Incidental complexity is the sort of complexity arising from weaknesses in our processes and tools, whereas
intrinsic complexity is the sort that we face when trying to describe, let alone solve the problem. [↩︎](https://qdrant.tech/blog/case-study-bloop/#fnref:1)


### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=13f8a6ce-9b61-4547-932d-be245dd161fc)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575438288&cv=11&fst=1748575438288&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-bloop%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Powering%20Bloop%20semantic%20code%20search%20-%20Qdrant&npa=0&pscdl=noapi&auid=2104111722.1748575438&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575438163&cv=11&fst=1748575438163&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-bloop%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Powering%20Bloop%20semantic%20code%20search%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2104111722.1748575438&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ac4dd3e7-0a39-4249-9f24-ea963b9a9335&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=af18b978-1e24-40d9-ae91-9d47f54442d7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-bloop%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ac4dd3e7-0a39-4249-9f24-ea963b9a9335&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=af18b978-1e24-40d9-ae91-9d47f54442d7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-bloop%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=af7fd1b22e7656a1656aed79e959139a&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575440313&cv=11&fst=1748575440313&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-bloop%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Powering%20Bloop%20semantic%20code%20search%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2104111722.1748575438&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)