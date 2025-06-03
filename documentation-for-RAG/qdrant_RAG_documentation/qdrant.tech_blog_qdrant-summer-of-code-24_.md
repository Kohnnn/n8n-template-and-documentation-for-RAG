---
url: "https://qdrant.tech/blog/qdrant-summer-of-code-24/"
title: "Qdrant Summer of Code 24 - Qdrant"
---

0

# Qdrant Summer of Code 24

Andre Zayarni

·

February 21, 2024

![Qdrant Summer of Code 24](https://qdrant.tech/blog/qdrant-summer-of-code-24/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-summer-of-code-24%2F&text=Qdrant%20Summer%20of%20Code%2024 "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-summer-of-code-24%2F "LinkedIn")

Google Summer of Code (#GSoC) is celebrating its 20th anniversary this year with the 2024 program. Over the past 20 years, 19K new contributors were introduced to #opensource through the program under the guidance of thousands of mentors from over 800 open-source organizations in various fields. Qdrant participated successfully in the program last year. Both projects, the UI Dashboard with unstructured data visualization and the advanced Geo Filtering, were completed in time and are now a part of the engine. One of the two young contributors joined the team and continues working on the project.

We are thrilled to announce that Qdrant was 𝐍𝐎𝐓 𝐚𝐜𝐜𝐞𝐩𝐭𝐞𝐝 into the GSoc 2024 program for unknown reasons, but instead, we are introducing our own 𝐐𝐝𝐫𝐚𝐧𝐭 𝐒𝐮𝐦𝐦𝐞𝐫 𝐨𝐟 𝐂𝐨𝐝𝐞 program with a stipend for contributors! To not reinvent the wheel, we follow all the timelines and rules of the official Google program.

## [Anchor](https://qdrant.tech/blog/qdrant-summer-of-code-24/\#our-project-ideas) Our project ideas.

We have prepared some excellent project ideas. Take a look and choose if you want to contribute in Rust or a Python-based project.

➡ _WASM-based dimension reduction viz_ 📊

Implement a dimension reduction algorithm in Rust, compile to WASM and integrate the WASM code with Qdrant Web UI.

➡ _Efficient BM25 and Okapi BM25, which uses the BERT Tokenizer_ 🥇

BM25 and Okapi BM25 are popular ranking algorithms. Qdrant’s FastEmbed supports dense embedding models. We need a fast, efficient, and massively parallel Rust implementation with Python bindings for these.

➡ _ONNX Cross Encoders in Python_ ⚔️

Export a cross-encoder ranking models to operate on ONNX runtime and integrate this model with the Qdrant’s FastEmbed to support efficient re-ranking

➡ _Ranking Fusion Algorithms implementation in Rust_ 🧪

Develop Rust implementations of various ranking fusion algorithms including but not limited to Reciprocal Rank Fusion (RRF). For a complete list, see: [https://github.com/AmenRa/ranx](https://github.com/AmenRa/ranx)
and create Python bindings for the implemented Rust modules.

➡ _Setup Jepsen to test Qdrant’s distributed guarantees_ 💣

Design and write Jepsen tests based on implementations for other Databases and create a report or blog with the findings.

See all details on our Notion page: [https://www.notion.so/qdrant/GSoC-2024-ideas-1dfcc01070094d87bce104623c4c1110](https://www.notion.so/qdrant/GSoC-2024-ideas-1dfcc01070094d87bce104623c4c1110)

Contributor application period begins on March 18th. We will accept applications via email. Let’s contribute and celebrate together!

In open-source, we trust! 🦀🤘🚀

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=228475c0-948f-4769-bc8e-5a62c0ff980e)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574735323&cv=11&fst=1748574735323&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-summer-of-code-24%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Summer%20of%20Code%2024%20-%20Qdrant&npa=0&pscdl=noapi&auid=182452992.1748574735&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574735300&cv=11&fst=1748574735300&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-summer-of-code-24%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Summer%20of%20Code%2024%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=182452992.1748574735&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=2872f78d-b100-44db-a207-a53b6f590e2e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e3850619-2dd5-4ad8-b916-660ffd4604b2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-summer-of-code-24%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=2872f78d-b100-44db-a207-a53b6f590e2e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=e3850619-2dd5-4ad8-b916-660ffd4604b2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-summer-of-code-24%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=c591b9ae8320105aba10042ffc0478c1&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574736352&cv=11&fst=1748574736352&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fqdrant-summer-of-code-24%2F&hn=www.googleadservices.com&frm=0&tiba=Qdrant%20Summer%20of%20Code%2024%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=182452992.1748574735&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)