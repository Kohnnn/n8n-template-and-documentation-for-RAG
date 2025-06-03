---
url: "https://qdrant.tech/blog/case-study-visua/"
title: "Visua and Qdrant: Vector Search in Computer Vision - Qdrant"
---

0

# Visua and Qdrant: Vector Search in Computer Vision

Manuel Meyer

·

May 01, 2024

![Visua and Qdrant: Vector Search in Computer Vision](https://qdrant.tech/blog/case-study-visua/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-visua%2F&text=Visua%20and%20Qdrant:%20Vector%20Search%20in%20Computer%20Vision "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-visua%2F "LinkedIn")

![visua/image1.png](https://qdrant.tech/blog/case-study-visua/image1.png)

For over a decade, [VISUA](https://visua.com/) has been a leader in precise, high-volume computer vision data analysis, developing a robust platform that caters to a wide range of use cases, from startups to large enterprises. Starting with social media monitoring, where it excels in analyzing vast data volumes to detect company logos, VISUA has built a diverse ecosystem of customers, including names in social media monitoring, like **Brandwatch**, cybersecurity like **Mimecast**, trademark protection like **Ebay** and several sports agencies like **Vision Insights** for sponsorship evaluation.

![visua/image3.png](https://qdrant.tech/blog/case-study-visua/image3.png)

## [Anchor](https://qdrant.tech/blog/case-study-visua/\#the-challenge) The Challenge

**Quality Control at Scale**

The accuracy of object detection within images is critical for VISUA ensuring that their algorithms are detecting objects in images correctly. With growing volumes of data processed for clients, the company was looking for a way to enhance its quality control and anomaly detection mechanisms to be more scalable and auditable.

The challenge was twofold. First, VISUA needed a method to rapidly and accurately identify images and the objects within them that were similar, to identify false negatives, or unclear outcomes and use them as inputs for reinforcement learning.

Second, the rapid growth in data volume challenged their previous quality control processes, which relied on a sampling method based on meta-information (like analyzing lower-confidence, smaller, or blurry images), which involved more manual reviews and was not as scalable as needed. In response, the team at VISUA explored vector databases as a solution.

## [Anchor](https://qdrant.tech/blog/case-study-visua/\#the-solution) The Solution

**Accelerating Anomaly Detection and Elevating Quality Control with Vector Search**

In addressing the challenge of scaling and enhancing its quality control processes, VISUA turned to vector databases, with Qdrant emerging as the solution of choice. This technological shift allowed VISUA to leverage vector databases for identifying similarities and deduplicating vast volumes of images, videos, and frames. By doing so, VISUA was able to automatically classify objects with a level of precision that was previously unattainable.

The introduction of vectors allowed VISUA to represent data uniquely and mark frames for closer examination by prioritizing the review of anomalies and data points with the highest variance. Consequently, this technology empowered Visia to scale its quality assurance and reinforcement learning processes tenfold.

> _“Using Qdrant as a vector database for our quality control allowed us to review 10x more data by exploiting repetitions and deduplicating samples and doing that at scale with having a query engine.”_ Alessandro Prest, Co-Founder at VISUA.

![visua/image2.jpg](https://qdrant.tech/blog/case-study-visua/image2.jpg)

## [Anchor](https://qdrant.tech/blog/case-study-visua/\#the-selection-process) The Selection Process

**Finding the Right Vector Database For Quality Analysis and Anomaly Detection**

Choosing the right vector database was a pivotal decision for VISUA, and the team conducted extensive benchmarks. They tested various solutions, including Weaviate, Pinecone, and Qdrant, focusing on the efficient handling of both vector and payload indexes. The objective was to identify a system that excels in managing hybrid queries that blend vector similarities with record attributes, crucial for enhancing their quality control and anomaly detection capabilities.

Qdrant distinguished itself through its:

- **Hybrid Query Capability:** Qdrant enables the execution of hybrid queries that combine payload fields and vector data, allowing for comprehensive and nuanced searches. This functionality leverages the strengths of both payload attributes and vector similarities for detailed data analysis. Prest noted the importance of Qdrant’s hybrid approach, saying, “When talking with the founders of Qdrant, we realized that they put a lot of effort into this hybrid approach, which really resonated with us.”

- **Performance Superiority**: Qdrant distinguished itself as the fastest engine for VISUA’s specific needs, significantly outpacing alternatives with query speeds up to 40 times faster for certain VISUA use cases. Alessandro Prest highlighted, “Qdrant was the fastest engine by a large margin for our use case,” underscoring its significant efficiency and scalability advantages.

- **API Documentation**: The clarity, comprehensiveness, and user-friendliness of Qdrant’s API documentation and reference guides further solidified VISUA’s decision.


This strategic selection enabled VISUA to achieve a notable increase in operational efficiency and scalability in its quality control processes.

## [Anchor](https://qdrant.tech/blog/case-study-visua/\#implementing-qdrant) Implementing Qdrant

Upon selecting Qdrant as their vector database solution, VISUA undertook a methodical approach to integration. The process began in a controlled development environment, allowing VISUA to simulate real-world use cases and ensure that Qdrant met their operational requirements. This careful, phased approach ensured a smooth transition when moving Qdrant into their production environment, hosted on AWS clusters. VISUA is leveraging several specific Qdrant features in their production setup:

1. **Support for Multiple Vectors per Record/Point**: This feature allows for a nuanced and multifaceted analysis of data, enabling VISUA to manage and query complex datasets more effectively.

2. **Quantization**: Quantization optimizes storage and accelerates query processing, improving data handling efficiency and lowering memory use, essential for large-scale operations.


## [Anchor](https://qdrant.tech/blog/case-study-visua/\#the-results) The Results

Integrating Qdrant into VISUA’s quality control operations has delivered measurable outcomes when it comes to efficiency and scalability:

- **40x Faster Query Processing**: Qdrant has drastically reduced the time needed for complex queries, enhancing workflow efficiency.

- **10x Scalability Boost:** The efficiency of Qdrant enables VISUA to handle ten times more data in its quality assurance and learning processes, supporting growth without sacrificing quality.

- **Increased Data Review Capacity:** The increased capacity to review the data allowed VISUA to enhance the accuracy of its algorithms through reinforcement learning.


#### [Anchor](https://qdrant.tech/blog/case-study-visua/\#expanding-qdrants-use-beyond-anomaly-detection) Expanding Qdrant’s Use Beyond Anomaly Detection

While the primary application of Qdrant is focused on quality control, VISUA’s team is actively exploring additional use cases with Qdrant. VISUA’s use of Qdrant has inspired new opportunities, notably in content moderation. “The moment we started to experiment with Qdrant, opened up a lot of ideas within the team for new applications,” said Prest on the potential unlocked by Qdrant. For example, this has led them to actively explore the Qdrant [Discovery API](https://qdrant.tech/documentation/concepts/explore/?q=discovery#discovery-api), with an eye on enhancing content moderation processes.

Beyond content moderation, VISUA is set for significant growth by broadening its copyright infringement detection services. As the demand for detecting a wider range of infringements, like unauthorized use of popular characters on merchandise, increases, VISUA plans to expand its technology capabilities. Qdrant will be pivotal in this expansion, enabling VISUA to meet the complex and growing challenges of moderating copyrighted content effectively and ensuring comprehensive protection for brands and creators.

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=898f0845-6c33-4dab-944d-2fd9ec37b47f)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573619390&cv=11&fst=1748573619390&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-visua%2F&hn=www.googleadservices.com&frm=0&tiba=Visua%20and%20Qdrant%3A%20Vector%20Search%20in%20Computer%20Vision%20-%20Qdrant&npa=0&pscdl=noapi&auid=860187105.1748573619&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573619346&cv=11&fst=1748573619346&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-visua%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Visua%20and%20Qdrant%3A%20Vector%20Search%20in%20Computer%20Vision%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=860187105.1748573619&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=857b2a43-f435-41bb-bfaf-0fe12ec72f43&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=736d55d0-7649-44ae-91bf-84855553c888&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-visua%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=857b2a43-f435-41bb-bfaf-0fe12ec72f43&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=736d55d0-7649-44ae-91bf-84855553c888&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-visua%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=55d890e284d1d98347e29294ff3d9a07&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573620430&cv=11&fst=1748573620430&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-visua%2F&hn=www.googleadservices.com&frm=0&tiba=Visua%20and%20Qdrant%3A%20Vector%20Search%20in%20Computer%20Vision%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=860187105.1748573619&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)