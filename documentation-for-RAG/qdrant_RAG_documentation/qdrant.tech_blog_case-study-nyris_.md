---
url: "https://qdrant.tech/blog/case-study-nyris/"
title: "Nyris & Qdrant: How Vectors are the Future of Visual Search - Qdrant"
---

0

# Nyris & Qdrant: How Vectors are the Future of Visual Search

Qdrant

·

September 10, 2024

![Nyris & Qdrant: How Vectors are the Future of Visual Search](https://qdrant.tech/blog/case-study-nyris/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-nyris%2F&text=Nyris%20&%20Qdrant:%20How%20Vectors%20are%20the%20Future%20of%20Visual%20Search "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-nyris%2F "LinkedIn")

![nyris-case-study](https://qdrant.tech/blog/case-study-nyris/nyris-case-study.png)

## [Anchor](https://qdrant.tech/blog/case-study-nyris/\#about-nyris) About Nyris

Founded in 2015 by CTO Markus Lukasson and his sister Anna Lukasson-Herzig, [Nyris](https://www.nyris.io/) offers advanced visual search solutions for companies, positioning itself as the “Google Lens” for corporate data. Their technology powers use cases such as visual search on websites of large retailers and machine manufacturing companies that require visual identification of spare parts. The primary goal is to identify items in a product catalog or spare parts as quickly as possible. With a strong foundation in e-commerce and nearly a decade of experience in vector search, Nyris is at the forefront of visual search innovation.

Beyond visual search, Nyris also provides synthetic data solutions, particularly for manufacturing and engineering sectors. Often, customers in these industries lack sufficient photos of parts to leverage visual search effectively. However, they do possess CAD files for their products. Nyris generates synthetic images from these CAD files, enabling visual search without needing actual product photos in the database.

Prominent clients such as IKEA, Trumpf (a precision laser manufacturer), and DMG Mori rely on Nyris to support their field engineers in maintaining parts.

![nyris-visual-search](https://qdrant.tech/blog/case-study-nyris/nyris-visual-search.png)

## [Anchor](https://qdrant.tech/blog/case-study-nyris/\#overcoming-limitations-in-visual-product-search) Overcoming Limitations in Visual Product Search

During his time at Amazon, Lukasson observed that search engines like Google often outperformed Amazon’s search capabilities for product searches. Recognizing the need for more precise search solutions in industries like e-commerce and spare part management, he identified a significant gap: Traditional keyword-based searches often fail, especially in situations where field engineers struggle to describe parts accurately with keywords. Visual search offers a solution, providing faster and more accurate results by leveraging images, which carry significantly more information than text-based queries.

In their quest for the perfect visual search provider, Nyris ultimately decided to develop their own solution.

## [Anchor](https://qdrant.tech/blog/case-study-nyris/\#the-path-to-vector-based-visual-search) The Path to Vector-Based Visual Search

Initially in 2015, the team explored traditional search algorithms based on key value SIFT (Scale Invariant Feature Transform) features to locate specific elements within images. However, they quickly realized that these methods were imprecise and unreliable. To address this, Nyris began experimenting with the first Convolutional Neural Networks (CNNs) to extract embeddings for vector search.

In the early days of vector search, there were few solutions available. Nyris initially developed their own vector search solution but later transitioned to SingleStore. At that time, SingleStore was the only option that could deliver efficient and fast brute-force vector search at scale. As Nyris’s data grew, the need for rapid scaling became evident. They found that many standard database features, such as real-time analytics and atomicity, were unnecessary for their specific needs. Instead, what Nyris required was a solution focused on fast and efficient vector search capabilities, along with features that would enhance the search experience for their customers.

With the emergence of pure-play, native vector search engines, Nyris conducted extensive research and benchmarks. Ultimately, they chose Qdrant as their vector search engine of choice. Qdrant stood out for its accuracy, speed, and the ability to handle large datasets efficiently, meeting all of Nyris’s requirements for a robust and scalable vector search solution.

### [Anchor](https://qdrant.tech/blog/case-study-nyris/\#the-selection-process) The Selection Process

As part of their selection process, Nyris evaluated several critical factors to ensure they chose the best vector search engine solution:

- **Accuracy and Speed**: These were primary considerations. Nyris needed to understand the performance differences between the [HNSW](https://qdrant.tech/articles/filtrable-hnsw/) graph-based approach and brute-force search. In particular, they examined edge cases that required numerous filters, sometimes necessitating a switch to brute-force search. Even in these scenarios, Qdrant demonstrated impressive speed and reliability, meeting Nyris’s stringent performance requirements.
- **Insert Speed**: Nyris assessed how quickly data could be inserted into the database, including the performance during simultaneous data ingests and query requests. Qdrant excelled in this area, providing the necessary efficiency for their operations.
- **Total Cost of Ownership**: Nyris analyzed the infrastructure costs and licensing fees associated with each solution. Qdrant offered a competitive total cost of ownership, making it an economically viable option.
- **Data Sovereignty**: The ability to deploy Qdrant in their own clusters was a key aspect for Nyris, ensuring they maintained control over their data and complied with relevant data sovereignty requirements.
- **Dedicated Vector Search Engine:** One of the key advantages of Qdrant, as Lukasson highlights, is its specialization as a dedicated, native vector search engine. “Qdrant, being purpose-built for vector search, can introduce relevant features much faster, like [quantization](https://qdrant.tech/documentation/guides/quantization/), integer8 support, and float32 rescoring. These advancements make searches more precise and cost-effective without sacrificing accuracy—exactly what Nyris needs,” said Lukasson. “When optimizing for search accuracy and speed, compromises aren’t an option. Just as you wouldn’t use a truck to race in Formula 1, we needed a solution designed specifically for vector search, not just a general database with vector search tacked on. With every Qdrant release, we gain new, tailored features that directly enhance our use case.”

## [Anchor](https://qdrant.tech/blog/case-study-nyris/\#key-benefits-of-qdrant-in-production) Key Benefits of Qdrant in Production

Nyris has found several aspects of Qdrant particularly beneficial in their production environment:

- **Enhanced Security with JWT**: [JSON Web Tokens](https://qdrant.tech/documentation/guides/security/#granular-access-control-with-jwt) provide enhanced security and performance, critical for safeguarding their data.
- **Seamless Scalability**: Qdrant’s ability to [scale effortlessly across nodes](https://qdrant.tech/documentation/guides/distributed_deployment/) ensures consistent high performance, even as Nyris’s data volume grows.
- **Flexible Search Options**: The availability of both graph-based and brute-force search methods offers Nyris the flexibility to tailor the search approach to specific use case requirements.
- **Versatile Data Handling**: Qdrant imposes almost no restrictions on data types and vector sizes, allowing Nyris to manage diverse and complex datasets effectively.
- **Built with Rust**: The use of [Rust](https://qdrant.tech/articles/why-rust/) ensures superior performance and future-proofing, while its open-source nature allows Nyris to inspect and customize the code as necessary.
- **Cost-Effective High Performance Search**: Qdrant’s efficient search capabilities ensure that Nyris can maintain high performance at a reasonable cost. With Qdrant, Nyris can search through extensive datasets efficiently, making it a crucial part of their technology stack.

By hosting Qdrant on Google Cloud within their Kubernetes Cluster, Nyris benefits from the scalability and reliability essential for their demanding operations, ensuring a robust and efficient visual search solution.

## [Anchor](https://qdrant.tech/blog/case-study-nyris/\#why-pure-vector-search-is-the-future-for-product-search) Why Pure-Vector Search is the Future for Product Search

Nyris’s vision is to identify every single product and spare part within milliseconds, and Qdrant plays an integral role in this. When envisioning the future of product search, Lukasson is convinced that vector representations will be the key to advancing search capabilities. Unlike keyword searches, vector search can seamlessly integrate various modalities, such as text, images, as well as depth or audio. This holistic approach will transform product and spare part searches, allowing for a single vector representation that encompasses a product’s text, visual and geometric descriptions.

“While traditional algorithms like BM25 are fast and cheap and still have a place in the search stack, vectors will replace them in the coming years,” says Lukasson. “Today, we have separate spaces for text search, visual search, and other modalities, but we envision a future with a unified vector representation that encompasses all relevant item data. No matter what input you use for your query, the search results will be accurate. The days of scrolling through thousands of results or encountering ’no results’ pages will soon be over. Every search request will deliver the right product or spare part in milliseconds.”

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=618075ab-7dca-48b9-a004-0ca137e414b5)

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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574450352&cv=11&fst=1748574450352&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-nyris%2F&hn=www.googleadservices.com&frm=0&tiba=Nyris%20%26%20Qdrant%3A%20How%20Vectors%20are%20the%20Future%20of%20Visual%20Search%20-%20Qdrant&npa=0&pscdl=noapi&auid=1031455414.1748574450&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574450307&cv=11&fst=1748574450307&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-nyris%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Nyris%20%26%20Qdrant%3A%20How%20Vectors%20are%20the%20Future%20of%20Visual%20Search%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1031455414.1748574450&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=94ca4b59-ff0f-49ef-9b76-b8bf62785215&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=2e17a3a5-cb7e-4a0a-b8a5-89d8388ab3a4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-nyris%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=94ca4b59-ff0f-49ef-9b76-b8bf62785215&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=2e17a3a5-cb7e-4a0a-b8a5-89d8388ab3a4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-nyris%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=95472ed240137ea54e6bee629da7470f&enableResponsiveStyles=true)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574451478&cv=11&fst=1748574451478&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-nyris%2F&hn=www.googleadservices.com&frm=0&tiba=Nyris%20%26%20Qdrant%3A%20How%20Vectors%20are%20the%20Future%20of%20Visual%20Search%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1031455414.1748574450&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)