---
url: "https://qdrant.tech/documentation/frameworks/cheshire-cat/"
title: "Cheshire Cat - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Cheshire Cat

# [Anchor](https://qdrant.tech/documentation/frameworks/cheshire-cat/\#cheshire-cat) Cheshire Cat

[Cheshire Cat](https://cheshirecat.ai/) is an open-source framework that allows you to develop intelligent agents on top of many Large Language Models (LLM). You can develop your custom AI architecture to assist you in a wide range of tasks.

![Cheshire cat](https://qdrant.tech/documentation/frameworks/cheshire-cat/cat.jpg)

## [Anchor](https://qdrant.tech/documentation/frameworks/cheshire-cat/\#cheshire-cat-and-qdrant) Cheshire Cat and Qdrant

Cheshire Cat uses Qdrant as the default [Vector Memory](https://cheshire-cat-ai.github.io/docs/faq/llm-concepts/vector-memory/) for ingesting and retrieving documents.

```
# Decide host and port for your Cat. Default will be localhost:1865
CORE_HOST=localhost
CORE_PORT=1865

# Qdrant server
# QDRANT_HOST=localhost
# QDRANT_PORT=6333

```

Cheshire Cat takes great advantage of the following features of Qdrant:

- [Collection Aliases](https://qdrant.tech/documentation/concepts/collections/#collection-aliases) to manage the change from one embedder to another.
- [Quantization](https://qdrant.tech/documentation/guides/quantization/) to obtain a good balance between speed, memory usage and quality of the results.
- [Snapshots](https://qdrant.tech/documentation/concepts/snapshots/) to not miss any information.
- [Community](https://discord.com/invite/tdtYvXjC4h)

![RAG Pipeline](https://qdrant.tech/documentation/frameworks/cheshire-cat/stregatto.jpg)

## [Anchor](https://qdrant.tech/documentation/frameworks/cheshire-cat/\#how-to-use-the-cheshire-cat) How to use the Cheshire Cat

### [Anchor](https://qdrant.tech/documentation/frameworks/cheshire-cat/\#requirements) Requirements

To run the Cheshire Cat, you need to have [Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) already installed on your system.

```shell
docker run --rm -it -p 1865:80 ghcr.io/cheshire-cat-ai/core:latest

```

- Chat with the Cheshire Cat on [localhost:1865/admin](http://localhost:1865/admin).
- You can also interact via REST API and try out the endpoints on [localhost:1865/docs](http://localhost:1865/docs)

Check the [instructions on github](https://github.com/cheshire-cat-ai/core/blob/main/README.md) for a more comprehensive quick start.

### [Anchor](https://qdrant.tech/documentation/frameworks/cheshire-cat/\#first-configuration-of-the-llm) First configuration of the LLM

- Open the Admin Portal in your browser at [localhost:1865/admin](http://localhost:1865/admin).
- Configure the LLM in the `Settings` tab.
- If you don’t explicitly choose it using `Settings` tab, the Embedder follows the LLM.

## [Anchor](https://qdrant.tech/documentation/frameworks/cheshire-cat/\#next-steps) Next steps

For more information, refer to the Cheshire Cat [documentation](https://cheshire-cat-ai.github.io/docs/) and [blog](https://cheshirecat.ai/blog/).

- [Getting started](https://cheshirecat.ai/hello-world/)
- [How the Cat works](https://cheshirecat.ai/how-the-cat-works/)
- [Write Your First Plugin](https://cheshirecat.ai/write-your-first-plugin/)
- [Cheshire Cat’s use of Qdrant - Vector Space](https://cheshirecat.ai/dont-get-lost-in-vector-space/)
- [Cheshire Cat’s use of Qdrant - Aliases](https://cheshirecat.ai/the-drunken-cat-effect/)
- [Cheshire Cat’s use of Qdrant - Quantization](https://cheshirecat.ai/gentle-introduction-to-cheshire-cat-vector-search/)
- [Cheshire Cat at Qdrant vector Space Talks](https://qdrant.tech/blog/meow-with-cheshire-cat/)
- [Discord Community](https://discord.com/invite/bHX5sNFCYU)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/cheshire-cat.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/cheshire-cat.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573659100&cv=11&fst=1748573659100&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcheshire-cat%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Cheshire%20Cat%20-%20Qdrant&npa=0&pscdl=noapi&auid=2145716448.1748573659&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573659082&cv=11&fst=1748573659082&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcheshire-cat%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Cheshire%20Cat%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2145716448.1748573659&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0965f815-6a98-4b50-9613-dc63686bc4a4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=86cf6343-a443-44dc-886e-8e1393e2bfb3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcheshire-cat%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0965f815-6a98-4b50-9613-dc63686bc4a4&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=86cf6343-a443-44dc-886e-8e1393e2bfb3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcheshire-cat%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573660179&cv=11&fst=1748573660179&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcheshire-cat%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Cheshire%20Cat%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2145716448.1748573659&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)