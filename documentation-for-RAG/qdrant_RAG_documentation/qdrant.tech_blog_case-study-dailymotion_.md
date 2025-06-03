---
url: "https://qdrant.tech/blog/case-study-dailymotion/"
title: "Dailymotion's Journey to Crafting the Ultimate Content-Driven Video Recommendation Engine with Qdrant Vector Database - Qdrant"
---

0

# Dailymotion's Journey to Crafting the Ultimate Content-Driven Video Recommendation Engine with Qdrant Vector Database

Atita Arora

·

February 27, 2024

![Dailymotion's Journey to Crafting the Ultimate Content-Driven Video Recommendation Engine with Qdrant Vector Database](https://qdrant.tech/blog/case-study-dailymotion/preview/title.jpg)

On this page:

- [Share on X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dailymotion%2F&text=Dailymotion%27s%20Journey%20to%20Crafting%20the%20Ultimate%20Content-Driven%20Video%20Recommendation%20Engine%20with%20Qdrant%20Vector%20Database "x")
- [Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dailymotion%2F "LinkedIn")

## [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#dailymotions-journey-to-crafting-the-ultimate-content-driven-video-recommendation-engine-with-qdrant-vector-database) Dailymotion’s Journey to Crafting the Ultimate Content-Driven Video Recommendation Engine with Qdrant Vector Database

In today’s digital age, the consumption of video content has become ubiquitous, with an overwhelming abundance of options available at our fingertips. However, amidst this vast sea of videos, the challenge lies not in finding content, but in discovering the content that truly resonates with individual preferences and interests and yet is diverse enough to not throw users into their own filter bubble. As viewers, we seek meaningful and relevant videos that enrich our experiences, provoke thought, and spark inspiration.

Dailymotion is not just another video application; it’s a beacon of curated content in an ocean of options. With a steadfast commitment to providing users with meaningful and ethical viewing experiences, Dailymotion stands as the bastion of videos that truly matter.

They aim to boost a dynamic visual dialogue, breaking echo chambers and fostering discovery.

### [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#scale) Scale

- **420 million+ videos**
- **2k+ new videos / hour**
- **13 million+ recommendations / day**
- **300+ languages in videos**
- **Required response time < 100 ms**

### [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#challenge) Challenge

- **Improve video recommendations** across all 3 applications of Dailymotion (mobile app, website and embedded video player on all major French and International sites) as it is the main driver of audience engagement and revenue stream of the platform.
- Traditional [collaborative recommendation model](https://en.wikipedia.org/wiki/Collaborative_filtering) tends to recommend only popular videos, fresh and niche videos suffer due to zero or minimal interaction
- Video content based recommendation system required processing all the video embedding at scale and in real time, as soon as they are added to the platform
- Exact neighbor search at the scale and keeping them up to date with new video updates in real time at Dailymotion was unreasonable and unrealistic
- Precomputed [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) would be expensive and may not work due to video updates every hour
- Platform needs fast recommendations ~ < 100ms
- Needed fast ANN search on a vector search engine which could support the scale and performance requirements of the platform

### [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#background--journey) Background / Journey

The quest of Dailymotion to deliver an intelligent video recommendation engine providing a curated selection of videos to its users started with a need to present more relevant videos to the first-time users of the platform (cold start problem) and implement an ideal home feed experience to allow users to watch videos that are expected to be relevant, diverse, explainable, and easily tunable.

This goal accounted for their efforts focused on [Optimizing Video Recommender for Dailymotion’s Home Feed](https://medium.com/dailymotion/optimizing-video-feed-recommendations-with-diversity-machine-learning-first-steps-4cf9abdbbffd) back in the time.

They continued their work in [Optimising the recommender engine with vector databases and opinion mining](https://medium.com/dailymotion/reinvent-your-recommender-system-using-vector-database-and-opinion-mining-a4fadf97d020) later with emphasis on ranking videos based on features like freshness, real views ratio, watch ratio, and aspect ratio to enhance user engagement and optimise watch time per user on the home feed. Furthermore, the team continued to focus on diversifying user interests by grouping videos based on interest and using stratified sampling to ensure a balanced experience for users.

By now it was clear to the Dailymotion team that the future initiatives will involve overcoming obstacles related to data processing, sentiment analysis, and user experience to provide meaningful and diverse recommendations. The main challenge stayed at the candidate generation process, textual embeddings, opinion mining, along with optimising the efficiency and accuracy of these processes and tackling the complexities of large-scale content curation.

### [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#solution-at-glance) Solution at glance

![solution-at-glance](https://qdrant.tech/case-studies/dailymotion/solution-at-glance.png)

The solution involved implementing a content based Recommendation System leveraging Qdrant to power the similar videos, with the following characteristics.

**Fields used to represent each video** -

Title , Tags , Description , Transcript (generated by [OpenAI whisper](https://openai.com/research/whisper))

**Encoding Model used** \- [MUSE - Multilingual Universal Sentence Encoder](https://www.tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa)

- Supports - 16 languages

### [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#why-qdrant) Why Qdrant?

![quote-from-Samuel](https://qdrant.tech/case-studies/dailymotion/Dailymotion-Quote.jpg)

Looking at the complexity, scale and adaptability of the desired solution, the team decided to leverage Qdrant’s vector database to implement a content-based video recommendation that undoubtedly offered several advantages over other methods:

**1\. Efficiency in High-Dimensional Data Handling:**

Video content is inherently high-dimensional, comprising various features such as audio, visual, textual, and contextual elements.

Qdrant excels in efficiently handling high-dimensional data and out-of-the-box support for all the models with up to 65536 dimensions, making it well-suited for representing and processing complex video features with choice of any embedding model.

**2\. Scalability:**

As the volume of video content and user interactions grows, scalability becomes paramount. Qdrant is meticulously designed to scale vertically as well as horizontally, allowing for seamless expansion to accommodate large volumes of data and user interactions without compromising performance.

**3\. Fast and Accurate Similarity Search:**

Efficient video recommendation systems rely on identifying similarities between videos to make relevant recommendations. Qdrant leverages advanced HNSW indexing and similarity search algorithms to support fast and accurate retrieval of similar videos based on their feature representations nearly instantly (20ms for this use case)

**4\. Flexibility in vector representation with metadata through payloads:**

Qdrant offers flexibility in storing vectors with metadata in form of payloads and offers support for advanced metadata filtering during the similarity search to incorporate custom logic.

**5\. Reduced Dimensionality and Storage Requirements:**

Vector representations in Qdrant offer various Quantization and memory mapping techniques to efficiently store and retrieve vectors, leading to reduced storage requirements and computational overhead compared to alternative methods such as content-based filtering or collaborative filtering.

**6\. Impressive Benchmarks:**

[Qdrant’s benchmarks](https://qdrant.tech/benchmarks/) has definitely been one of the key motivations for the Dailymotion’s team to try the solution and the team comments that the performance has been only better than the benchmarks.

**7\. Ease of usage:**

Qdrant API’s have been immensely easy to get started with as compared to Google Vertex Matching Engine (which was Dailymotion’s initial choice) and the support from the team has been of a huge value to us.

**8\. Being able to fetch data by id**

Qdrant allows to retrieve vector point / videos by ids while the Vertex Matching Engine requires a vector input to be able to search for other vectors which was another really important feature for Dailymotion

### [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#data-processing-pipeline) Data Processing pipeline

![data-processing](https://qdrant.tech/case-studies/dailymotion/data-processing-pipeline.png)

Figure shows the streaming architecture of the data processing pipeline that processes everytime a new video is uploaded or updated (Title, Description, Tags, Transcript), an updated embedding is computed and fed directly into Qdrant.

### [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#results) Results

![before-qdrant-results](https://qdrant.tech/case-studies/dailymotion/before-qdrant.png)

There has been a big improvement in the recommended content processing time and quality as the existing system had issues like:

1. Subpar video recommendations due to long processing time ~ 5 hours
2. Collaborative recommender tended to recommend and focused on high signal / popular videos
3. Metadata based recommender focussed only on a very small scope of trusted video sources
4. The recommendations did not take contents of the video into consideration

![after-qdrant-results](https://qdrant.tech/case-studies/dailymotion/after-qdrant.png)

The new recommender system implementation leveraging Qdrant along with the collaborative recommender offered various advantages :

1. The processing time for the new video content reduced significantly to a few minutes which enabled the fresh videos to be part of recommendations.
2. The performant & scalable scope of video recommendation currently processes 22 Million videos and can provide recommendation for videos with fewer interactions too.
3. The overall huge performance gain on the low signal videos has contributed to more than 3 times increase on the interaction and CTR ( number of clicks) on the recommended videos.
4. Seamlessly solved the initial cold start and low performance problems with the fresh content.

### [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#outlook--future-plans) Outlook / Future plans

The team is very excited with the results they achieved on their recommender system and wishes to continue building with it.

They aim to work on Perspective feed next and say

> ”We’ve recently integrated this new recommendation system into our mobile app through a feature called Perspective. The aim of this feature is to disrupt the vertical feed algorithm, allowing users to discover new videos. When browsing their feed, users may encounter a video discussing a particular movie. With Perspective, they have the option to explore different viewpoints on the same topic. Qdrant plays a crucial role in this feature by generating candidate videos related to the subject, ensuring users are exposed to diverse perspectives and preventing them from being confined to an echo chamber where they only encounter similar viewpoints.”
>
> Gladys Roch - Machine Learning Engineer

![perspective-feed-with-qdrant](https://qdrant.tech/case-studies/dailymotion/perspective-feed-qdrant.jpg)

The team is also interested in leveraging advanced features like [Qdrant’s Discovery API](https://qdrant.tech/documentation/concepts/explore/#recommendation-api) to promote exploration of content to enable finding not only similar but dissimilar content too by using positive and negative vectors in the queries and making it work with the existing collaborative recommendation model.

### [Anchor](https://qdrant.tech/blog/case-study-dailymotion/\#references) References

**2024 -** [https://www.youtube.com/watch?v=1ULpLpWD0Aw](https://www.youtube.com/watch?v=1ULpLpWD0Aw)

**2023 -** [https://medium.com/dailymotion/reinvent-your-recommender-system-using-vector-database-and-opinion-mining-a4fadf97d020](https://medium.com/dailymotion/reinvent-your-recommender-system-using-vector-database-and-opinion-mining-a4fadf97d020)

**2022 -** [https://medium.com/dailymotion/optimizing-video-feed-recommendations-with-diversity-machine-learning-first-steps-4cf9abdbbffd](https://medium.com/dailymotion/optimizing-video-feed-recommendations-with-diversity-machine-learning-first-steps-4cf9abdbbffd)

### Get Started with Qdrant Free

[Get Started](https://cloud.qdrant.io/signup?ajs_anonymous_id=393c86f6-384b-40f1-88d7-f411752562d7)

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

[iframe](https://139603372.hs-sites-eu1.com/hs-web-interactive-139603372-237919561943?utk=669eb1d9b386418b48e0801197fc9b68&enableResponsiveStyles=true)

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ee58eef4-8130-4327-aba1-4f140f1a0745&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b4606e0b-ef38-46d8-8b9d-cdfeed1c9868&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dailymotion%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574578659&cv=11&fst=1748574578659&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dailymotion%2F&hn=www.googleadservices.com&frm=0&tiba=Dailymotion's%20Journey%20to%20Crafting%20the%20Ultimate%20Content-Driven%20Video%20Recommendation%20Engine%20with%20Qdrant%20Vector%20Database%20-%20Qdrant&npa=0&pscdl=noapi&auid=1351751218.1748574578&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574578647&cv=11&fst=1748574578647&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dailymotion%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Dailymotion's%20Journey%20to%20Crafting%20the%20Ultimate%20Content-Driven%20Video%20Recommendation%20Engine%20with%20Qdrant%20Vector%20Database%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1351751218.1748574578&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574578821&cv=11&fst=1748574578821&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dailymotion%2F&hn=www.googleadservices.com&frm=0&tiba=Dailymotion's%20Journey%20to%20Crafting%20the%20Ultimate%20Content-Driven%20Video%20Recommendation%20Engine%20with%20Qdrant%20Vector%20Database%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1351751218.1748574578&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ee58eef4-8130-4327-aba1-4f140f1a0745&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b4606e0b-ef38-46d8-8b9d-cdfeed1c9868&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fblog%2Fcase-study-dailymotion%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)