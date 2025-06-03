---
url: "https://qdrant.tech/articles/vector-similarity-beyond-search/"
title: "Vector Similarity: Going Beyond Full-Text Search | Qdrant - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Vector Similarity: Going Beyond Full-Text Search \| Qdrant

[Back to Data Exploration](https://qdrant.tech/articles/data-exploration/)

# Vector Similarity: Going Beyond Full-Text Search \| Qdrant

Luis Cossío

·

August 08, 2023

![Vector Similarity: Going Beyond Full-Text Search | Qdrant](https://qdrant.tech/articles_data/vector-similarity-beyond-search/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#vector-similarity-unleashing-data-insights-beyond-traditional-search) Vector Similarity: Unleashing Data Insights Beyond Traditional Search

When making use of unstructured data, there are traditional go-to solutions that are well-known for developers:

- **Full-text search** when you need to find documents that contain a particular word or phrase.
- **[Vector search](https://qdrant.tech/documentation/overview/vector-search/)** when you need to find documents that are semantically similar to a given query.

Sometimes people mix those two approaches, so it might look like the vector similarity is just an extension of full-text search. However, in this article, we will explore some promising new techniques that can be used to expand the use-case of unstructured data and demonstrate that vector similarity creates its own stack of data exploration tools.

## [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#what-is-vector-similarity-search) What is vector similarity search?

Vector similarity offers a range of powerful functions that go far beyond those available in traditional full-text search engines. From dissimilarity search to diversity and recommendation, these methods can expand the cases in which vectors are useful.

Vector Databases, which are designed to store and process immense amounts of vectors, are the first candidates to implement these new techniques and allow users to exploit their data to its fullest.

## [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#vector-similarity-search-vs-full-text-search) Vector similarity search vs. full-text search

While there is an intersection in the functionality of these two approaches, there is also a vast area of functions that is unique to each of them.
For example, the exact phrase matching and counting of results are native to full-text search, while vector similarity support for this type of operation is limited.
On the other hand, vector similarity easily allows cross-modal retrieval of images by text or vice-versa, which is impossible with full-text search.

This mismatch in expectations might sometimes lead to confusion.
Attempting to use a vector similarity as a full-text search can result in a range of frustrations, from slow response times to poor search results, to limited functionality.
As an outcome, they are getting only a fraction of the benefits of vector similarity.

![Full-text search and Vector Similarity Functionality overlap](https://qdrant.tech/articles_data/vector-similarity-beyond-search/venn-diagram.png)

Full-text search and Vector Similarity Functionality overlap

Below we will explore why the vector similarity stack deserves new interfaces and design patterns that will unlock the full potential of this technology, which can still be used in conjunction with full-text search.

## [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#new-ways-to-interact-with-similarities) New ways to interact with similarities

Having a vector representation of unstructured data unlocks new ways of interacting with it.
For example, it can be used to measure semantic similarity between words, to cluster words or documents based on their meaning, to find related images, or even to generate new text.
However, these interactions can go beyond finding their nearest neighbors (kNN).

There are several other techniques that can be leveraged by vector representations beyond the traditional kNN search. These include dissimilarity search, diversity search, recommendations, and discovery functions.

## [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#dissimilarity-ssearch) Dissimilarity ssearch

The Dissimilarity —or farthest— search is the most straightforward concept after the nearest search, which can’t be reproduced in a traditional full-text search.
It aims to find the most un-similar or distant documents across the collection.

![Dissimilarity Search](https://qdrant.tech/articles_data/vector-similarity-beyond-search/dissimilarity.png)

Dissimilarity Search

Unlike full-text match, Vector similarity can compare any pair of documents (or points) and assign a similarity score.
It doesn’t rely on keywords or other metadata.
With vector similarity, we can easily achieve a dissimilarity search by inverting the search objective from maximizing similarity to minimizing it.

The dissimilarity search can find items in areas where previously no other search could be used.
Let’s look at a few examples.

### [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#case-mislabeling-detection) Case: mislabeling detection

For example, we have a dataset of furniture in which we have classified our items into what kind of furniture they are: tables, chairs, lamps, etc.
To ensure our catalog is accurate, we can use a dissimilarity search to highlight items that are most likely mislabeled.

To do this, we only need to search for the most dissimilar items using the
embedding of the category title itself as a query.
This can be too broad, so, by combining it with filters —a [Qdrant superpower](https://qdrant.tech/articles/filtrable-hnsw/)—, we can narrow down the search to a specific category.

![Mislabeling Detection](https://qdrant.tech/articles_data/vector-similarity-beyond-search/mislabelling.png)

Mislabeling Detection

The output of this search can be further processed with heavier models or human supervision to detect actual mislabeling.

### [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#case-outlier-detection) Case: outlier detection

In some cases, we might not even have labels, but it is still possible to try to detect anomalies in our dataset.
Dissimilarity search can be used for this purpose as well.

![Anomaly Detection](https://qdrant.tech/articles_data/vector-similarity-beyond-search/anomaly-detection.png)

Anomaly Detection

The only thing we need is a bunch of reference points that we consider “normal”.
Then we can search for the most dissimilar points to this reference set and use them as candidates for further analysis.

## [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#diversity-search) Diversity search

Even with no input provided vector, (dis-)similarity can improve an overall selection of items from the dataset.

The naive approach is to do random sampling.
However, unless our dataset has a uniform distribution, the results of such sampling might be biased toward more frequent types of items.

![Example of random sampling](https://qdrant.tech/articles_data/vector-similarity-beyond-search/diversity-random.png)

Example of random sampling

The similarity information can increase the diversity of those results and make the first overview more interesting.
That is especially useful when users do not yet know what they are looking for and want to explore the dataset.

![Example of similarity-based sampling](https://qdrant.tech/articles_data/vector-similarity-beyond-search/diversity-force.png)

Example of similarity-based sampling

The power of vector similarity, in the context of being able to compare any two points, allows making a diverse selection of the collection possible without any labeling efforts.
By maximizing the distance between all points in the response, we can have an algorithm that will sequentially output dissimilar results.

![Diversity Search](https://qdrant.tech/articles_data/vector-similarity-beyond-search/diversity.png)

Diversity Search

Some forms of diversity sampling are already used in the industry and are known as [Maximum Margin Relevance](https://python.langchain.com/docs/integrations/vectorstores/qdrant#maximum-marginal-relevance-search-mmr) (MMR). Techniques like this were developed to enhance similarity on a universal search API.
However, there is still room for new ideas, particularly regarding diversity retrieval.
By utilizing more advanced vector-native engines, it could be possible to take use cases to the next level and achieve even better results.

## [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#vector-similarity-recommendations) Vector similarity recommendations

Vector similarity can go above a single query vector.
It can combine multiple positive and negative examples for a more accurate retrieval.
Building a recommendation API in a vector database can take advantage of using already stored vectors as part of the queries, by specifying the point id.
Doing this, we can skip query-time neural network inference, and make the recommendation search faster.

There are multiple ways to implement recommendations with vectors.

### [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#vector-features-recommendations) Vector-features recommendations

The first approach is to take all positive and negative examples and average them to create a single query vector.
In this technique, the more significant components of positive vectors are canceled out by the negative ones, and the resulting vector is a combination of all the features present in the positive examples, but not in the negative ones.

![Vector-Features Based Recommendations](https://qdrant.tech/articles_data/vector-similarity-beyond-search/feature-based-recommendations.png)

Vector-Features Based Recommendations

This approach is already implemented in Qdrant, and while it works great when the vectors are assumed to have each of their dimensions represent some kind of feature of the data, sometimes distances are a better tool to judge negative and positive examples.

### [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#relative-distance-recommendations) Relative distance recommendations

Another approach is to use the distance between negative examples to the candidates to help them create exclusion areas.
In this technique, we perform searches near the positive examples while excluding the points that are closer to a negative example than to a positive one.

![Relative Distance Recommendations](https://qdrant.tech/articles_data/vector-similarity-beyond-search/relative-distance-recommendations.png)

Relative Distance Recommendations

The main use-case of both approaches —of course— is to take some history of user interactions and recommend new items based on it.

## [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#discovery) Discovery

In many exploration scenarios, the desired destination is not known in advance.
The search process in this case can consist of multiple steps, where each step would provide a little more information to guide the search in the right direction.

To get more intuition about the possible ways to implement this approach, let’s take a look at how similarity modes are trained in the first place:

The most well-known loss function used to train similarity models is a [triplet-loss](https://en.wikipedia.org/wiki/Triplet_loss).
In this loss, the model is trained by fitting the information of relative similarity of 3 objects: the Anchor, Positive, and Negative examples.

![Triplet Loss](https://qdrant.tech/articles_data/vector-similarity-beyond-search/triplet-loss.png)

Triplet Loss

Using the same mechanics, we can look at the training process from the other side.
Given a trained model, the user can provide positive and negative examples, and the goal of the discovery process is then to find suitable anchors across the stored collection of vectors.

![Reversed triplet loss](https://qdrant.tech/articles_data/vector-similarity-beyond-search/discovery.png)

Reversed triplet loss

Multiple positive-negative pairs can be provided to make the discovery process more accurate.
Worth mentioning, that as well as in NN training, the dataset may contain noise and some portion of contradictory information, so a discovery process should be tolerant of this kind of data imperfections.

![Sample pairs](https://qdrant.tech/articles_data/vector-similarity-beyond-search/discovery-noise.png)

Sample pairs

The important difference between this and the recommendation method is that the positive-negative pairs in the discovery method don’t assume that the final result should be close to positive, it only assumes that it should be closer than the negative one.

![Discovery vs Recommendation](https://qdrant.tech/articles_data/vector-similarity-beyond-search/discovery-vs-recommendations.png)

Discovery vs Recommendation

In combination with filtering or similarity search, the additional context information provided by the discovery pairs can be used as a re-ranking factor.

## [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#a-new-api-stack-for-vector-databases) A new API stack for vector databases

When you introduce vector similarity capabilities into your text search engine, you extend its functionality.
However, it doesn’t work the other way around, as the vector similarity as a concept is much broader than some task-specific implementations of full-text search.

[Vector databases](https://qdrant.tech/), which introduce built-in full-text functionality, must make several compromises:

- Choose a specific full-text search variant.
- Either sacrifice API consistency or limit vector similarity functionality to only basic kNN search.
- Introduce additional complexity to the system.

Qdrant, on the contrary, puts vector similarity in the center of its API and architecture, such that it allows us to move towards a new stack of vector-native operations.
We believe that this is the future of vector databases, and we are excited to see what new use-cases will be unlocked by these techniques.

## [Anchor](https://qdrant.tech/articles/vector-similarity-beyond-search/\#key-takeaways) Key takeaways:

- Vector similarity offers advanced data exploration tools beyond traditional full-text search, including dissimilarity search, diversity sampling, and recommendation systems.
- Practical applications of vector similarity include improving data quality through mislabeling detection and anomaly identification.
- Enhanced user experiences are achieved by leveraging advanced search techniques, providing users with intuitive data exploration, and improving decision-making processes.

Ready to unlock the full potential of your data? [Try a free demo](https://qdrant.tech/contact-us/) to explore how vector similarity can revolutionize your data insights and drive smarter decision-making.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/vector-similarity-beyond-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/vector-similarity-beyond-search.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=039b5139-4a34-456d-8f90-7cea8710937e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1bf6a81e-a395-483e-b007-75205c071a7e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fvector-similarity-beyond-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574354471&cv=11&fst=1748574354471&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694~104612245~104612247&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fvector-similarity-beyond-search%2F&hn=www.googleadservices.com&frm=0&tiba=Vector%20Similarity%3A%20Going%20Beyond%20Full-Text%20Search%20%7C%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=2044916331.1748574354&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574354455&cv=11&fst=1748574354455&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694~104612245~104612247&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fvector-similarity-beyond-search%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Vector%20Similarity%3A%20Going%20Beyond%20Full-Text%20Search%20%7C%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2044916331.1748574354&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=039b5139-4a34-456d-8f90-7cea8710937e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1bf6a81e-a395-483e-b007-75205c071a7e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fvector-similarity-beyond-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)