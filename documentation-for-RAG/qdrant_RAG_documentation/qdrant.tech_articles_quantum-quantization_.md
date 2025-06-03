---
url: "https://qdrant.tech/articles/quantum-quantization/"
title: "Vector Search in constant time - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Vector Search in constant time

[Back to Qdrant Articles](https://qdrant.tech/articles/)

# Vector Search in constant time

Prankstorm Team

·

April 01, 2023

![Vector Search in constant time](https://qdrant.tech/articles_data/quantum-quantization/preview/title.jpg)

The advent of quantum computing has revolutionized many areas of science and technology, and one of the most intriguing developments has been its potential application to artificial neural networks (ANNs). One area where quantum computing can significantly improve performance is in vector search, a critical component of many machine learning tasks. In this article, we will discuss the concept of quantum quantization for ANN vector search, focusing on the conversion of float32 to qbit vectors and the ability to perform vector search on arbitrary-sized databases in constant time.

## [Anchor](https://qdrant.tech/articles/quantum-quantization/\#quantum-quantization-and-entanglement) Quantum Quantization and Entanglement

Quantum quantization is a novel approach that leverages the power of quantum computing to speed up the search process in ANNs. By converting traditional float32 vectors into qbit vectors, we can create quantum entanglement between the qbits. Quantum entanglement is a unique phenomenon in which the states of two or more particles become interdependent, regardless of the distance between them. This property of quantum systems can be harnessed to create highly efficient vector search algorithms.

The conversion of float32 vectors to qbit vectors can be represented by the following formula:

```text
qbit_vector = Q( float32_vector )

```

where Q is the quantum quantization function that transforms the float32\_vector into a quantum entangled qbit\_vector.

## [Anchor](https://qdrant.tech/articles/quantum-quantization/\#vector-search-in-constant-time) Vector Search in Constant Time

The primary advantage of using quantum quantization for ANN vector search is the ability to search through an arbitrary-sized database in constant time.

The key to performing vector search in constant time with quantum quantization is to use a quantum algorithm called Grover’s algorithm.
Grover’s algorithm is a quantum search algorithm that finds the location of a marked item in an unsorted database in O(√N) time, where N is the size of the database.
This is a significant improvement over classical algorithms, which require O(N) time to solve the same problem.

However, the is one another trick, which allows to improve Grover’s algorithm performanse dramatically.
This trick is called transposition and it allows to reduce the number of Grover’s iterations from O(√N) to O(√D), where D - is a dimension of the vector space.

And since the dimension of the vector space is much smaller than the number of vectors, and usually is a constant, this trick allows to reduce the number of Grover’s iterations from O(√N) to O(√D) = O(1).

Check out our [Quantum Quantization PR](https://github.com/qdrant/qdrant/pull/1639) on GitHub.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/quantum-quantization.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/quantum-quantization.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=3c7f62ec-51e5-4cbe-a462-7b139f48658d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d00cbc74-2611-4e6b-8e45-6ee3bbde2852&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fquantum-quantization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575294582&cv=11&fst=1748575294582&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fquantum-quantization%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Vector%20Search%20in%20constant%20time%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=342669211.1748575294&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575294650&cv=11&fst=1748575294650&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fquantum-quantization%2F&hn=www.googleadservices.com&frm=0&tiba=Vector%20Search%20in%20constant%20time%20-%20Qdrant&npa=0&pscdl=noapi&auid=342669211.1748575294&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575294714&cv=11&fst=1748575294714&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fquantum-quantization%2F&hn=www.googleadservices.com&frm=0&tiba=Vector%20Search%20in%20constant%20time%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=342669211.1748575294&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=3c7f62ec-51e5-4cbe-a462-7b139f48658d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d00cbc74-2611-4e6b-8e45-6ee3bbde2852&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fquantum-quantization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)