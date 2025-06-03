---
url: "https://qdrant.tech/documentation/overview/"
title: "What is Qdrant? - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- What is Qdrant?

# [Anchor](https://qdrant.tech/documentation/overview/\#introduction) Introduction

Vector databases are a relatively new way for interacting with abstract data representations
derived from opaque machine learning models such as deep learning architectures. These
representations are often called vectors or embeddings and they are a compressed version of
the data used to train a machine learning model to accomplish a task like sentiment analysis,
speech recognition, object detection, and many others.

These new databases shine in many applications like [semantic search](https://en.wikipedia.org/wiki/Semantic_search)
and [recommendation systems](https://en.wikipedia.org/wiki/Recommender_system), and here, we’ll
learn about one of the most popular and fastest growing vector databases in the market, [Qdrant](https://github.com/qdrant/qdrant).

## [Anchor](https://qdrant.tech/documentation/overview/\#what-is-qdrant) What is Qdrant?

[Qdrant](https://github.com/qdrant/qdrant) “is a vector similarity search engine that provides a production-ready
service with a convenient API to store, search, and manage points (i.e. vectors) with an additional
payload.” You can think of the payloads as additional pieces of information that can help you
hone in on your search and also receive useful information that you can give to your users.

You can get started using Qdrant with the Python `qdrant-client`, by pulling the latest docker
image of `qdrant` and connecting to it locally, or by trying out [Qdrant’s Cloud](https://cloud.qdrant.io/?ajs_anonymous_id=023caa08-eb03-4bb5-880e-b7c863b00cc3)
free tier option until you are ready to make the full switch.

With that out of the way, let’s talk about what are vector databases.

## [Anchor](https://qdrant.tech/documentation/overview/\#what-are-vector-databases) What Are Vector Databases?

![dbs](https://raw.githubusercontent.com/ramonpzg/mlops-sydney-2023/main/images/databases.png)

Vector databases are a type of database designed to store and query high-dimensional vectors
efficiently. In traditional [OLTP](https://www.ibm.com/topics/oltp) and [OLAP](https://www.ibm.com/topics/olap)
databases (as seen in the image above), data is organized in rows and columns (and these are
called **Tables**), and queries are performed based on the values in those columns. However,
in certain applications including image recognition, natural language processing, and recommendation
systems, data is often represented as vectors in a high-dimensional space, and these vectors, plus
an id and a payload, are the elements we store in something called a **Collection** within a vector
database like Qdrant.

A vector in this context is a mathematical representation of an object or data point, where elements of
the vector implicitly or explicitly correspond to specific features or attributes of the object. For example,
in an image recognition system, a vector could represent an image, with each element of the vector
representing a pixel value or a descriptor/characteristic of that pixel. In a music recommendation
system, each vector could represent a song, and elements of the vector would capture song characteristics
such as tempo, genre, lyrics, and so on.

Vector databases are optimized for **storing** and **querying** these high-dimensional vectors
efficiently, and they often use specialized data structures and indexing techniques such as
Hierarchical Navigable Small World (HNSW) – which is used to implement Approximate Nearest
Neighbors – and Product Quantization, among others. These databases enable fast similarity
and semantic search while allowing users to find vectors that are the closest to a given query
vector based on some distance metric. The most commonly used distance metrics are Euclidean
Distance, Cosine Similarity, and Dot Product, and these three are fully supported Qdrant.

Here’s a quick overview of the three:

- [**Cosine Similarity**](https://en.wikipedia.org/wiki/Cosine_similarity) \- Cosine similarity
is a way to measure how similar two vectors are. To simplify, it reflects whether the vectors
have the same direction (similar) or are poles apart. Cosine similarity is often used with text representations
to compare how similar two documents or sentences are to each other. The output of cosine similarity ranges
from -1 to 1, where -1 means the two vectors are completely dissimilar, and 1 indicates maximum similarity.
- [**Dot Product**](https://en.wikipedia.org/wiki/Dot_product) \- The dot product similarity metric is another way
of measuring how similar two vectors are. Unlike cosine similarity, it also considers the length of the vectors.
This might be important when, for example, vector representations of your documents are built
based on the term (word) frequencies. The dot product similarity is calculated by multiplying the respective values
in the two vectors and then summing those products. The higher the sum, the more similar the two vectors are.
If you normalize the vectors (so the numbers in them sum up to 1), the dot product similarity will become
the cosine similarity.
- [**Euclidean Distance**](https://en.wikipedia.org/wiki/Euclidean_distance) \- Euclidean
distance is a way to measure the distance between two points in space, similar to how we
measure the distance between two places on a map. It’s calculated by finding the square root
of the sum of the squared differences between the two points’ coordinates. This distance metric
is also commonly used in machine learning to measure how similar or dissimilar two vectors are.

Now that we know what vector databases are and how they are structurally different than other
databases, let’s go over why they are important.

## [Anchor](https://qdrant.tech/documentation/overview/\#why-do-we-need-vector-databases) Why do we need Vector Databases?

Vector databases play a crucial role in various applications that require similarity search, such
as recommendation systems, content-based image retrieval, and personalized search. By taking
advantage of their efficient indexing and searching techniques, vector databases enable faster
and more accurate retrieval of unstructured data already represented as vectors, which can
help put in front of users the most relevant results to their queries.

In addition, other benefits of using vector databases include:

1. Efficient storage and indexing of high-dimensional data.
2. Ability to handle large-scale datasets with billions of data points.
3. Support for real-time analytics and queries.
4. Ability to handle vectors derived from complex data types such as images, videos, and natural language text.
5. Improved performance and reduced latency in machine learning and AI applications.
6. Reduced development and deployment time and cost compared to building a custom solution.

Keep in mind that the specific benefits of using a vector database may vary depending on the
use case of your organization and the features of the database you ultimately choose.

Let’s now evaluate, at a high-level, the way Qdrant is architected.

## [Anchor](https://qdrant.tech/documentation/overview/\#high-level-overview-of-qdrants-architecture) High-Level Overview of Qdrant’s Architecture

![qdrant](https://raw.githubusercontent.com/ramonpzg/mlops-sydney-2023/main/images/qdrant_overview_high_level.png)

The diagram above represents a high-level overview of some of the main components of Qdrant. Here
are the terminologies you should get familiar with.

- [Collections](https://qdrant.tech/documentation/concepts/collections/): A collection is a named set of points (vectors with a payload) among which you can search. The vector of each point within the same collection must have the same dimensionality and be compared by a single metric. [Named vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-multiple-vectors) can be used to have multiple vectors in a single point, each of which can have their own dimensionality and metric requirements.
- [Distance Metrics](https://en.wikipedia.org/wiki/Metric_space): These are used to measure
similarities among vectors and they must be selected at the same time you are creating a
collection. The choice of metric depends on the way the vectors were obtained and, in particular,
on the neural network that will be used to encode new queries.
- [Points](https://qdrant.tech/documentation/concepts/points/): The points are the central entity that
Qdrant operates with and they consist of a vector and an optional id and payload.
  - id: a unique identifier for your vectors.
  - Vector: a high-dimensional representation of data, for example, an image, a sound, a document, a video, etc.
  - [Payload](https://qdrant.tech/documentation/concepts/payload/): A payload is a JSON object with additional data you can add to a vector.
- [Storage](https://qdrant.tech/documentation/concepts/storage/): Qdrant can use one of two options for
storage, **In-memory** storage (Stores all vectors in RAM, has the highest speed since disk
access is required only for persistence), or **Memmap** storage, (creates a virtual address
space associated with the file on disk).
- Clients: the programming languages you can use to connect to Qdrant.

## [Anchor](https://qdrant.tech/documentation/overview/\#next-steps) Next Steps

Now that you know more about vector databases and Qdrant, you are ready to get started with one
of our tutorials. If you’ve never used a vector database, go ahead and jump straight into
the **Getting Started** section. Conversely, if you are a seasoned developer in these
technology, jump to the section most relevant to your use case.

As you go through the tutorials, please let us know if any questions come up in our
[Discord channel here](https://qdrant.to/discord). 😎

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/overview/_index.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/overview/_index.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573799440&cv=11&fst=1748573799440&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Foverview%2F&hn=www.googleadservices.com&frm=0&tiba=What%20is%20Qdrant%3F%20-%20Qdrant&npa=0&pscdl=noapi&auid=1427569798.1748573799&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573799409&cv=11&fst=1748573799409&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Foverview%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=What%20is%20Qdrant%3F%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1427569798.1748573799&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=61b29ffd-69ec-42b7-af0d-bc69a1652f1c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b92208da-67fd-413a-8c1c-5f5f69312e25&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Foverview%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=61b29ffd-69ec-42b7-af0d-bc69a1652f1c&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=b92208da-67fd-413a-8c1c-5f5f69312e25&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Foverview%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573800672&cv=11&fst=1748573800672&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Foverview%2F&hn=www.googleadservices.com&frm=0&tiba=What%20is%20Qdrant%3F%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1427569798.1748573799&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)