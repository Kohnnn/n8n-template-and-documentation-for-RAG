---
url: "https://qdrant.tech/articles/batch-vector-search-with-qdrant/"
title: "Mastering Batch Search for Vector Optimization - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Mastering Batch Search for Vector Optimization

[Back to Vector Search Manuals](https://qdrant.tech/articles/vector-search-manuals/)

# Mastering Batch Search for Vector Optimization

Kacper Łukawski

·

September 26, 2022

![Mastering Batch Search for Vector Optimization](https://qdrant.tech/articles_data/batch-vector-search-with-qdrant/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/batch-vector-search-with-qdrant/\#how-to-optimize-vector-search-using-batch-search-in-qdrant-0100) How to Optimize Vector Search Using Batch Search in Qdrant 0.10.0

The latest release of Qdrant 0.10.0 has introduced a lot of functionalities that simplify some common tasks. Those new possibilities come with some slightly modified interfaces of the client library. One of the recently introduced features is the possibility to query the collection with [multiple vectors](https://qdrant.tech/blog/storing-multiple-vectors-per-object-in-qdrant/) at once — a batch search mechanism.

There are a lot of scenarios in which you may need to perform multiple non-related tasks at the same time. Previously, you only could send several requests to Qdrant API on your own. But multiple parallel requests may cause significant network overhead and slow down the process, especially in case of poor connection speed.

Now, thanks to the new batch search, you don’t need to worry about that. Qdrant will handle multiple search requests in just one API call and will perform those requests in the most optimal way.

## [Anchor](https://qdrant.tech/articles/batch-vector-search-with-qdrant/\#an-example-of-using-batch-search-to-optimize-vector-search) An example of using batch search to optimize vector search

We’ve used the official Python client to show how the batch search might be integrated with your application. Since there have been some changes in the interfaces of Qdrant 0.10.0, we’ll go step by step.

### [Anchor](https://qdrant.tech/articles/batch-vector-search-with-qdrant/\#step-1-creating-the-collection) Step 1: Creating the collection

The first step is to create a collection with a specified configuration — at least vector size and the distance function used to measure the similarity between vectors.

```python
from qdrant_client import QdrantClient
from qdrant_client.conversions.common_types import VectorParams

client = QdrantClient("localhost", 6333)
if not client.collection_exists('test_collection'):
    client.create_collection(
        collection_name="test_collection",
        vectors_config=VectorParams(size=4, distance=Distance.EUCLID),
)

```

## [Anchor](https://qdrant.tech/articles/batch-vector-search-with-qdrant/\#step-2-loading-the-vectors) Step 2: Loading the vectors

With the collection created, we can put some vectors into it. We’re going to have just a few examples.

```python
vectors = [\
    [.1, .0, .0, .0],\
    [.0, .1, .0, .0],\
    [.0, .0, .1, .0],\
    [.0, .0, .0, .1],\
    [.1, .0, .1, .0],\
    [.0, .1, .0, .1],\
    [.1, .1, .0, .0],\
    [.0, .0, .1, .1],\
    [.1, .1, .1, .1],\
]

client.upload_collection(
    collection_name="test_collection",
    vectors=vectors,
)

```

## [Anchor](https://qdrant.tech/articles/batch-vector-search-with-qdrant/\#step-3-batch-search-in-a-single-request) Step 3: Batch search in a single request

Now we’re ready to start looking for similar vectors, as our collection has some entries. Let’s say we want to find the distance between the selected vector and the most similar database entry and at the same time find the two most similar objects for a different vector query. Up till 0.9, we would need to call the API twice. Now, we can send both requests together:

```python
results = client.search_batch(
    collection_name="test_collection",
    requests=[\
        SearchRequest(\
            vector=[0., 0., 2., 0.],\
            limit=1,\
        ),\
        SearchRequest(\
            vector=[0., 0., 0., 0.01],\
            with_vector=True,\
            limit=2,\
        )\
    ]
)

# Out: [\
#   [ScoredPoint(id=2, version=0, score=1.9,\
#                payload=None, vector=None)],\
#   [ScoredPoint(id=3, version=0, score=0.09,\
#                payload=None, vector=[0.0, 0.0, 0.0, 0.1]),\
#    ScoredPoint(id=1, version=0, score=0.10049876,\
#                payload=None, vector=[0.0, 0.1, 0.0, 0.0])]\
# ]

```

Each instance of the SearchRequest class may provide its own search parameters, including vector query but also some additional filters. The response will be a list of individual results for each request. In case any of the requests is malformed, there will be an exception thrown, so either all of them pass or none of them.

And that’s it! You no longer have to handle the multiple requests on your own. Qdrant will do it under the hood.

## [Anchor](https://qdrant.tech/articles/batch-vector-search-with-qdrant/\#batch-search-benchmarks) Batch Search Benchmarks

The batch search is fairly easy to be integrated into your application, but if you prefer to see some numbers before deciding to switch, then it’s worth comparing four different options:

1. Querying the database sequentially.
2. Using many threads/processes with individual requests.
3. Utilizing the batch search of Qdrant in a single request.
4. Combining parallel processing and batch search.

In order to do that, we’ll create a richer collection of points, with vectors from the _glove-25-angular_ dataset, quite a common choice for ANN comparison. If you’re interested in seeing some more details of how we benchmarked Qdrant, let’s take a [look at the Gist](https://gist.github.com/kacperlukawski/2d12faa49e06a5080f4c35ebcb89a2a3).

## [Anchor](https://qdrant.tech/articles/batch-vector-search-with-qdrant/\#the-results) The results

We launched the benchmark 5 times on 10000 test vectors and averaged the results. Presented numbers are the mean values of all the attempts:

1. Sequential search: 225.9 seconds
2. Batch search: 208.0 seconds
3. Multiprocessing search (8 processes): 194.2 seconds
4. Multiprocessing batch search (8 processes, batch size 10): 148.9 seconds

The results you may achieve on a specific setup may vary depending on the hardware, however, at the first glance, it seems that batch searching may save you quite a lot of time.

Additional improvements could be achieved in the case of distributed deployment, as Qdrant won’t need to make extensive inter-cluster requests. Moreover, if your requests share the same filtering condition, the query optimizer would be able to reuse it among batch requests.

## [Anchor](https://qdrant.tech/articles/batch-vector-search-with-qdrant/\#summary) Summary

Batch search allows packing different queries into a single API call and retrieving the results in a single response. If you ever struggled with sending several consecutive queries into Qdrant, then you can easily switch to the new batch search method and simplify your application code. As shown in the benchmarks, that may almost effortlessly speed up your interactions with Qdrant even by over 30%, even not considering the spare network overhead and possible reuse of filters!

Ready to unlock the potential of batch search and optimize your vector search with Qdrant 0.10.0? Contact us today to learn how we can revolutionize your search capabilities!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/batch-vector-search-with-qdrant.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/batch-vector-search-with-qdrant.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574892805&cv=11&fst=1748574892805&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbatch-vector-search-with-qdrant%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Mastering%20Batch%20Search%20for%20Vector%20Optimization%20-%20Qdrant&npa=0&pscdl=noapi&auid=985744264.1748574893&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574892788&cv=11&fst=1748574892788&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbatch-vector-search-with-qdrant%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Mastering%20Batch%20Search%20for%20Vector%20Optimization%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=985744264.1748574893&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=14204cea-9182-4258-8f46-a75a166f9461&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3ba5e92c-ad63-4d96-9176-4e90e4881c7d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbatch-vector-search-with-qdrant%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=14204cea-9182-4258-8f46-a75a166f9461&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3ba5e92c-ad63-4d96-9176-4e90e4881c7d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbatch-vector-search-with-qdrant%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574893672&cv=11&fst=1748574893672&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbatch-vector-search-with-qdrant%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Mastering%20Batch%20Search%20for%20Vector%20Optimization%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=985744264.1748574893&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)