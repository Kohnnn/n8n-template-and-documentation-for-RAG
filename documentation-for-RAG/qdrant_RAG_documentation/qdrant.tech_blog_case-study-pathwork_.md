---
url: "https://qdrant.tech/blog/case-study-pathwork/"
title: "Pathwork Optimizes Life Insurance Underwriting with Precision Vector Search - Qdrant"
---

0

# Pathwork Optimizes Life Insurance Underwriting with Precision Vector Search

Daniel Azoulai

·

April 22, 2025

![Pathwork Optimizes Life Insurance Underwriting with Precision Vector Search](https://qdrant.tech/blog/case-study-pathwork/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pathwork%2F&text=Pathwork%20Optimizes%20Life%20Insurance%20Underwriting%20with%20Precision%20Vector%20Search "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pathwork%2F "LinkedIn")

## [Anchor](https://qdrant.tech/blog/case-study-pathwork/\#pathwork-optimizes-life-insurance-underwriting-with-precision-vector-search)**Pathwork Optimizes Life Insurance Underwriting with Precision Vector Search**

![Pathwork Optimizes Life Insurance Underwriting with Precision Vector Search](https://qdrant.tech/blog/case-study-pathwork/case-study-pathwork-summary-dark-b.jpg)

### [Anchor](https://qdrant.tech/blog/case-study-pathwork/\#about-pathwork)**About Pathwork**

Pathwork is redesigning life and health insurance workflows for the age of AI. Brokerages and insurance carriers utilize Pathwork’s advanced agentic system to automate their underwriting processes and enhance back-office sales operations. Pathwork’s solution drastically reduces errors, completes tasks up to 70 times faster, and significantly conserves human capital.

### [Anchor](https://qdrant.tech/blog/case-study-pathwork/\#the-challenge-accuracy-above-all)**The Challenge: Accuracy Above All**

Life insurance underwriting demands exceptional accuracy. Traditionally, underwriting involves extensive manual input, subjective judgment, and frequent errors. These errors, such as misclassifying risk based on incomplete or misunderstood health data, often result in lost sales and customer dissatisfaction due to sudden premium changes.

“Accuracy is paramount—every error can mean hundreds of dollars per month in difference to customers or waiting months longer for coverage,” explains Blake Butterworth, co-founder of Pathwork.

### [Anchor](https://qdrant.tech/blog/case-study-pathwork/\#pathworks-innovative-solution)**Pathwork’s Innovative Solution**

Pathwork addresses these issues with an AI-powered underwriting tool. The platform uses vector search and retrieval augmented generation (RAG) techniques, enabling brokers to rapidly match customers with precise risk classes and insurance products based on live broker inputs collected during the quoting process via conversation or document upload.

Initially, Pathwork explored various solutions, including Amazon S3, OpenSearch, and other vector databases. However, none provided the necessary combination of performance, ease of use, and reliability. Ultimately, Pathwork chose Qdrant Cloud due to its strong documentation and developer-friendly environment.

### [Anchor](https://qdrant.tech/blog/case-study-pathwork/\#why-pathwork-chose-qdrant)**Why Pathwork Chose Qdrant**

“We landed on Qdrant after extensive trial and error,” Blake shared. “Our engineers found Qdrant’s documentation and support significantly better than other solutions. At critical junctures, Qdrant’s support felt like having an additional principal engineer on our team. Fantastic service through their helpdesk was a standout experience.”

### [Anchor](https://qdrant.tech/blog/case-study-pathwork/\#the-impact-increased-accuracy-and-user-adoption)**The Impact: Increased Accuracy and User Adoption**

After implementing Qdrant, Pathwork rapidly saw significant improvements:

- **Accuracy Improvements:** Pathwork achieved significant precision gains, nearly halving mean squared error (MSE) from 3.5 to 1.8 in February alone. These improvements were driven by enhancements such as scalar quantization, hybrid search, and advanced filter utilization. Accuracy is measured by how closely the predictions match the final risk class assigned by licensed underwriters.
- **Performance Enhancements:** Latency was drastically reduced from 9 seconds to just 2 seconds per query, thanks to optimizations including storing vectors in RAM rather than on disk and improved scaling methods (replicas, shards, nodes).
- **Rapid Growth:** Usage has grown 50% month-over-month, with thousands of insurance cases processed in the last month alone. To maintain low-latency retrieval at scale, Pathwork expanded its Qdrant deployment with additional nodes, implemented sharding to distribute load, and introduced replicas to support high-concurrency read operations. These scaling changes ensured consistent performance as usage surged.
- **User Satisfaction:** Accurate, consistent underwriting results drove significant user adoption. As accuracy surpassed a critical threshold, word-of-mouth recommendations propelled user growth.

“We knew we’d achieved something significant when brokers began confidently testing edge cases live during demos, resulting in immediate adoption,” Blake remarked.

### [Anchor](https://qdrant.tech/blog/case-study-pathwork/\#looking-ahead)**Looking Ahead**

Pathwork aims to become the central hub for life insurance underwriting. Future plans involve deeper integration with insurance carriers, further enhancing underwriting accuracy, scalability, and efficiency. Pathwork’s commitment to precision, supported by Qdrant’s reliable vector search capabilities, is setting a new industry standard for accuracy and efficiency in life insurance underwriting.

**“Every aspect of our system depends on precision, and Qdrant has been instrumental in achieving our goals,” says Blake Butterworth.**

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=c2806cbb-602c-48b9-a77c-75ac398be1b4)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574366300&cv=11&fst=1748574366300&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pathwork%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Pathwork%20Optimizes%20Life%20Insurance%20Underwriting%20with%20Precision%20Vector%20Search%20-%20Qdrant&npa=0&pscdl=noapi&auid=1110503195.1748574366&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574366274&cv=11&fst=1748574366274&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pathwork%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Pathwork%20Optimizes%20Life%20Insurance%20Underwriting%20with%20Precision%20Vector%20Search%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1110503195.1748574366&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=13977f8d-c7ee-4403-aea1-5a84212fbb6c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=55951102-04a7-4858-b4d8-6894b17631a9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pathwork%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=13977f8d-c7ee-4403-aea1-5a84212fbb6c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=55951102-04a7-4858-b4d8-6894b17631a9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pathwork%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=87f0646a8ad0723da638ed5f7dc558dc&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574367332&cv=11&fst=1748574367332&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-pathwork%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Pathwork%20Optimizes%20Life%20Insurance%20Underwriting%20with%20Precision%20Vector%20Search%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1110503195.1748574366&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)