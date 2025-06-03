---
url: "https://qdrant.tech/articles/binary-quantization/"
title: "Binary Quantization - Vector Search, 40x Faster - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Binary Quantization - Vector Search, 40x Faster

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)

# Binary Quantization - Vector Search, 40x Faster

Nirant Kasliwal

·

September 18, 2023

![Binary Quantization - Vector Search, 40x Faster ](https://qdrant.tech/articles_data/binary-quantization/preview/title.jpg)

# [Anchor](https://qdrant.tech/articles/binary-quantization/\#optimizing-high-dimensional-vectors-with-binary-quantization) Optimizing High-Dimensional Vectors with Binary Quantization

Qdrant is built to handle typical scaling challenges: high throughput, low latency and efficient indexing. **Binary quantization (BQ)** is our latest attempt to give our customers the edge they need to scale efficiently. This feature is particularly excellent for collections with large vector lengths and a large number of points.

Our results are dramatic: Using BQ will reduce your memory consumption and improve retrieval speeds by up to 40x.

As is the case with other quantization methods, these benefits come at the cost of recall degradation. However, our implementation lets you balance the tradeoff between speed and recall accuracy at time of search, rather than time of index creation.

The rest of this article will cover:

1. The importance of binary quantization
2. Basic implementation using our Python client
3. Benchmark analysis and usage recommendations

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#what-is-binary-quantization) What is Binary Quantization?

Binary quantization (BQ) converts any vector embedding of floating point numbers into a vector of binary or boolean values. This feature is an extension of our past work on [scalar quantization](https://qdrant.tech/articles/scalar-quantization/) where we convert `float32` to `uint8` and then leverage a specific SIMD CPU instruction to perform fast vector comparison.

![What is binary quantization](https://qdrant.tech/articles_data/binary-quantization/bq-2.png)

**This binarization function is how we convert a range to binary values. All numbers greater than zero are marked as 1. If it’s zero or less, they become 0.**

The benefit of reducing the vector embeddings to binary values is that boolean operations are very fast and need significantly less CPU instructions. In exchange for reducing our 32 bit embeddings to 1 bit embeddings we can see up to a 40x retrieval speed up gain!

One of the reasons vector search still works with such a high compression rate is that these large vectors are over-parameterized for retrieval. This is because they are designed for ranking, clustering, and similar use cases, which typically need more information encoded in the vector.

For example, The 1536 dimension OpenAI embedding is worse than Open Source counterparts of 384 dimension at retrieval and ranking. Specifically, it scores 49.25 on the same [Embedding Retrieval Benchmark](https://huggingface.co/spaces/mteb/leaderboard) where the Open Source `bge-small` scores 51.82. This 2.57 points difference adds up quite soon.

Our implementation of quantization achieves a good balance between full, large vectors at ranking time and binary vectors at search and retrieval time. It also has the ability for you to adjust this balance depending on your use case.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#faster-search-and-retrieval) Faster search and retrieval

Unlike product quantization, binary quantization does not rely on reducing the search space for each probe. Instead, we build a binary index that helps us achieve large increases in search speed.

![Speed by quantization method](https://qdrant.tech/articles_data/binary-quantization/bq-3.png)

HNSW is the approximate nearest neighbor search. This means our accuracy improves up to a point of diminishing returns, as we check the index for more similar candidates. In the context of binary quantization, this is referred to as the **oversampling rate**.

For example, if `oversampling=2.0` and the `limit=100`, then 200 vectors will first be selected using a quantized index. For those 200 vectors, the full 32 bit vector will be used with their HNSW index to a much more accurate 100 item result set. As opposed to doing a full HNSW search, we oversample a preliminary search and then only do the full search on this much smaller set of vectors.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#improved-storage-efficiency) Improved storage efficiency

The following diagram shows the binarization function, whereby we reduce 32 bits storage to 1 bit information.

Text embeddings can be over 1024 elements of floating point 32 bit numbers. For example, remember that OpenAI embeddings are 1536 element vectors. This means each vector is 6kB for just storing the vector.

![Improved storage efficiency](https://qdrant.tech/articles_data/binary-quantization/bq-4.png)

In addition to storing the vector, we also need to maintain an index for faster search and retrieval. Qdrant’s formula to estimate overall memory consumption is:

`memory_size = 1.5 * number_of_vectors * vector_dimension * 4 bytes`

For 100K OpenAI Embedding ( `ada-002`) vectors we would need 900 Megabytes of RAM and disk space. This consumption can start to add up rapidly as you create multiple collections or add more items to the database.

**With binary quantization, those same 100K OpenAI vectors only require 128 MB of RAM.** We benchmarked this result using methods similar to those covered in our [Scalar Quantization memory estimation](https://qdrant.tech/articles/scalar-quantization/#benchmarks).

This reduction in RAM usage is achieved through the compression that happens in the binary conversion. HNSW and quantized vectors will live in RAM for quick access, while original vectors can be offloaded to disk only. For searching, quantized HNSW will provide oversampled candidates, then they will be re-evaluated using their disk-stored original vectors to refine the final results. All of this happens under the hood without any additional intervention on your part.

### [Anchor](https://qdrant.tech/articles/binary-quantization/\#when-should-you-not-use-bq) When should you not use BQ?

Since this method exploits the over-parameterization of embedding, you can expect poorer results for small embeddings i.e. less than 1024 dimensions. With the smaller number of elements, there is not enough information maintained in the binary vector to achieve good results.

You will still get faster boolean operations and reduced RAM usage, but the accuracy degradation might be too high.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#sample-implementation) Sample implementation

Now that we have introduced you to binary quantization, let’s try our a basic implementation. In this example, we will be using OpenAI and Cohere with Qdrant.

#### [Anchor](https://qdrant.tech/articles/binary-quantization/\#create-a-collection-with-binary-quantization-enabled) Create a collection with Binary Quantization enabled

Here is what you should do at indexing time when you create the collection:

1. We store all the “full” vectors on disk.
2. Then we set the binary embeddings to be in RAM.

By default, both the full vectors and BQ get stored in RAM. We move the full vectors to disk because this saves us memory and allows us to store more vectors in RAM. By doing this, we explicitly move the binary vectors to memory by setting `always_ram=True`.

```python
from qdrant_client import QdrantClient

#collect to our Qdrant Server
client = QdrantClient(
    url="http://localhost:6333",
    prefer_grpc=True,
)

#Create the collection to hold our embeddings
# on_disk=True and the quantization_config are the areas to focus on
collection_name = "binary-quantization"
if not client.collection_exists(collection_name):
    client.create_collection(
        collection_name=f"{collection_name}",
        vectors_config=models.VectorParams(
            size=1536,
            distance=models.Distance.DOT,
            on_disk=True,
        ),
        optimizers_config=models.OptimizersConfigDiff(
            default_segment_number=5,
        ),
        hnsw_config=models.HnswConfigDiff(
        m=0,
        ),
        quantization_config=models.BinaryQuantization(
            binary=models.BinaryQuantizationConfig(always_ram=True),
        ),
    )

```

#### [Anchor](https://qdrant.tech/articles/binary-quantization/\#what-is-happening-in-the-hnswconfig) What is happening in the HnswConfig?

We’re setting `m` to 0 i.e. disabling the HNSW graph construction. This allows faster uploads of vectors and payloads. We will turn it back on down below, once all the data is loaded.

#### [Anchor](https://qdrant.tech/articles/binary-quantization/\#next-we-upload-our-vectors-to-this-and-then-enable-the-graph-construction) Next, we upload our vectors to this and then enable the graph construction:

```python
batch_size = 10000
client.upload_collection(
    collection_name=collection_name,
    ids=range(len(dataset)),
    vectors=dataset["openai"],
    payload=[\
        {"text": x} for x in dataset["text"]\
    ],
    parallel=10, # based on the machine
)

```

Enable HNSW graph construction again:

```python
client.update_collection(
    collection_name=f"{collection_name}",
    hnsw_config=models.HnswConfigDiff(
        m=16,
    ,
)

```

#### [Anchor](https://qdrant.tech/articles/binary-quantization/\#configure-the-search-parameters) Configure the search parameters:

When setting search parameters, we specify that we want to use `oversampling` and `rescore`. Here is an example snippet:

```python
client.search(
    collection_name="{collection_name}",
    query_vector=[0.2, 0.1, 0.9, 0.7, ...],
    search_params=models.SearchParams(
        quantization=models.QuantizationSearchParams(
            ignore=False,
            rescore=True,
            oversampling=2.0,
        )
    )
)

```

After Qdrant pulls the oversampled vectors set, the full vectors which will be, say 1536 dimensions for OpenAI will then be pulled up from disk. Qdrant computes the nearest neighbor with the query vector and returns the accurate, rescored order. This method produces much more accurate results. We enabled this by setting `rescore=True`.

These two parameters are how you are going to balance speed versus accuracy. The larger the size of your oversample, the more items you need to read from disk and the more elements you have to search with the relatively slower full vector index. On the other hand, doing this will produce more accurate results.

If you have lower accuracy requirements you can even try doing a small oversample without rescoring. Or maybe, for your data set combined with your accuracy versus speed requirements you can just search the binary index and no rescoring, i.e. leaving those two parameters out of the search query.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#benchmark-results) Benchmark results

We retrieved some early results on the relationship between limit and oversampling using the the DBPedia OpenAI 1M vector dataset. We ran all these experiments on a Qdrant instance where 100K vectors were indexed and used 100 random queries.

We varied the 3 parameters that will affect query time and accuracy: limit, rescore and oversampling. We offer these as an initial exploration of this new feature. You are highly encouraged to reproduce these experiments with your data sets.

> Aside: Since this is a new innovation in vector databases, we are keen to hear feedback and results. [Join our Discord server](https://discord.gg/Qy6HCJK9Dc) for further discussion!

**Oversampling:**
In the figure below, we illustrate the relationship between recall and number of candidates:

![Correct vs candidates](https://qdrant.tech/articles_data/binary-quantization/bq-5.png)

We see that “correct” results i.e. recall increases as the number of potential “candidates” increase (limit x oversampling). To highlight the impact of changing the `limit`, different limit values are broken apart into different curves. For example, we see that the lowest recall for limit 50 is around 94 correct, with 100 candidates. This also implies we used an oversampling of 2.0

As oversampling increases, we see a general improvement in results – but that does not hold in every case.

**Rescore:**
As expected, rescoring increases the time it takes to return a query.
We also repeated the experiment with oversampling except this time we looked at how rescore impacted result accuracy.

![Relationship between limit and rescore on correct](https://qdrant.tech/articles_data/binary-quantization/bq-7.png)

**Limit:**
We experiment with limits from Top 1 to Top 50 and we are able to get to 100% recall at limit 50, with rescore=True, in an index with 100K vectors.

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#recommendations) Recommendations

Quantization gives you the option to make tradeoffs against other parameters:
Dimension count/embedding size
Throughput and Latency requirements
Recall requirements

If you’re working with OpenAI or Cohere embeddings, we recommend the following oversampling settings:

| Method | Dimensionality | Test Dataset | Recall | Oversampling |
| --- | --- | --- | --- | --- |
| OpenAI text-embedding-3-large | 3072 | [DBpedia 1M](https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-large-3072-1M) | 0.9966 | 3x |
| OpenAI text-embedding-3-small | 1536 | [DBpedia 100K](https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-small-1536-100K) | 0.9847 | 3x |
| OpenAI text-embedding-3-large | 1536 | [DBpedia 1M](https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-large-1536-1M) | 0.9826 | 3x |
| OpenAI text-embedding-ada-002 | 1536 | [DbPedia 1M](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M) | 0.98 | 4x |
| Gemini | 768 | No Open Data | 0.9563 | 3x |
| Mistral Embed | 768 | No Open Data | 0.9445 | 3x |

If you determine that binary quantization is appropriate for your datasets and queries then we suggest the following:

- Binary Quantization with always\_ram=True
- Vectors stored on disk
- Oversampling=2.0 (or more)
- Rescore=True

## [Anchor](https://qdrant.tech/articles/binary-quantization/\#whats-next) What’s next?

Binary quantization is exceptional if you need to work with large volumes of data under high recall expectations. You can try this feature either by spinning up a [Qdrant container image](https://hub.docker.com/r/qdrant/qdrant) locally or, having us create one for you through a [free account](https://cloud.qdrant.io/signup?ajs_anonymous_id=9acb3173-87c0-4d2d-a56f-8b399e240337) in our cloud hosted service.

The article gives examples of data sets and configuration you can use to get going. Our documentation covers [adding large datasets to Qdrant](https://qdrant.tech/documentation/tutorials/bulk-upload/) to your Qdrant instance as well as [more quantization methods](https://qdrant.tech/documentation/guides/quantization/).

If you have any feedback, drop us a note on Twitter or LinkedIn to tell us about your results. [Join our lively Discord Server](https://discord.gg/Qy6HCJK9Dc) if you want to discuss BQ with like-minded people!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/binary-quantization.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/binary-quantization.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b0b86fcf-2cc9-4e27-a054-5bb3a4272617&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=eaf69330-e4b7-4b00-aaf3-2445889e99e9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbinary-quantization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575521393&cv=11&fst=1748575521393&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbinary-quantization%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Binary%20Quantization%20-%20Vector%20Search%2C%2040x%20Faster%20-%20Qdrant&npa=0&pscdl=noapi&auid=914410941.1748575521&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575521353&cv=11&fst=1748575521353&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbinary-quantization%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Binary%20Quantization%20-%20Vector%20Search%2C%2040x%20Faster%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=914410941.1748575521&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575521508&cv=11&fst=1748575521508&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbinary-quantization%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Binary%20Quantization%20-%20Vector%20Search%2C%2040x%20Faster%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=914410941.1748575521&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=b0b86fcf-2cc9-4e27-a054-5bb3a4272617&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=eaf69330-e4b7-4b00-aaf3-2445889e99e9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Fbinary-quantization%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)