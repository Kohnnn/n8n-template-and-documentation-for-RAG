---
url: "https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/"
title: "Measure Search Quality - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Beginner tutorials](https://qdrant.tech/documentation/beginner-tutorials/)
- Measure Search Quality

# [Anchor](https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/\#measure-and-improve-retrieval-quality-in-semantic-search) Measure and Improve Retrieval Quality in Semantic Search

| Time: 30 min | Level: Intermediate |  |  |
| --- | --- | --- | --- |

Semantic search pipelines are as good as the embeddings they use. If your model cannot properly represent input data, similar objects might
be far away from each other in the vector space. No surprise, that the search results will be poor in this case. There is, however, another
component of the process which can also degrade the quality of the search results. It is the ANN algorithm itself.

In this tutorial, we will show how to measure the quality of the semantic retrieval and how to tune the parameters of the HNSW, the ANN
algorithm used in Qdrant, to obtain the best results.

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/\#embeddings-quality) Embeddings quality

The quality of the embeddings is a topic for a separate tutorial. In a nutshell, it is usually measured and compared by benchmarks, such as
[Massive Text Embedding Benchmark (MTEB)](https://huggingface.co/spaces/mteb/leaderboard). The evaluation process itself is pretty
straightforward and is based on a ground truth dataset built by humans. We have a set of queries and a set of the documents we would expect
to receive for each of them. In the [evaluation process](https://qdrant.tech/rag/rag-evaluation-guide/), we take a query, find the most similar documents in the vector space and compare
them with the ground truth. In that setup, **finding the most similar documents is implemented as full kNN search, without any approximation**.
As a result, we can measure the quality of the embeddings themselves, without the influence of the ANN algorithm.

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/\#retrieval-quality) Retrieval quality

Embeddings quality is indeed the most important factor in the semantic search quality. However, vector search engines, such as Qdrant, do not
perform pure kNN search. Instead, they use **Approximate Nearest Neighbors** (ANN) algorithms, which are much faster than the exact search,
but can return suboptimal results. We can also **measure the retrieval quality of that approximation** which also contributes to the overall
search quality.

### [Anchor](https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/\#quality-metrics) Quality metrics

There are various ways of how quantify the quality of semantic search. Some of them, such as [Precision@k](https://en.wikipedia.org/wiki/Evaluation_measures_%28information_retrieval%29#Precision_at_k),
are based on the number of relevant documents in the top-k search results. Others, such as [Mean Reciprocal Rank (MRR)](https://en.wikipedia.org/wiki/Mean_reciprocal_rank),
take into account the position of the first relevant document in the search results. [DCG and NDCG](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)
metrics are, in turn, based on the relevance score of the documents.

If we treat the search pipeline as a whole, we could use them all. The same is true for the embeddings quality evaluation. However, for the
ANN algorithm itself, anything based on the relevance score or ranking is not applicable. Ranking in vector search relies on the distance
between the query and the document in the vector space, however distance is not going to change due to approximation, as the function is
still the same.

Therefore, it only makes sense to measure the quality of the ANN algorithm by the number of relevant documents in the top-k search results,
such as `precision@k`. It is calculated as the number of relevant documents in the top-k search results divided by `k`. In case of testing
just the ANN algorithm, we can use the exact kNN search as a ground truth, with `k` being fixed. It will be a measure on **how well the ANN**
**algorithm approximates the exact search**.

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/\#measure-the-quality-of-the-search-results) Measure the quality of the search results

Let’s build a quality [evaluation](https://qdrant.tech/rag/rag-evaluation-guide/) of the ANN algorithm in Qdrant. We will, first, call the search endpoint in a standard way to obtain
the approximate search results. Then, we will call the exact search endpoint to obtain the exact matches, and finally compare both results
in terms of precision.

Before we start, let’s create a collection, fill it with some data and then start our evaluation. We will use the same dataset as in the
[Loading a dataset from Hugging Face hub](https://qdrant.tech/documentation/tutorials/huggingface-datasets/) tutorial, `Qdrant/arxiv-titles-instructorxl-embeddings`
from the [Hugging Face hub](https://huggingface.co/datasets/Qdrant/arxiv-titles-instructorxl-embeddings). Let’s download it in a streaming
mode, as we are only going to use part of it.

```python
from datasets import load_dataset

dataset = load_dataset(
    "Qdrant/arxiv-titles-instructorxl-embeddings", split="train", streaming=True
)

```

We need some data to be indexed and another set for the testing purposes. Let’s get the first 50000 items for the training and the next 1000
for the testing.

```python
dataset_iterator = iter(dataset)
train_dataset = [next(dataset_iterator) for _ in range(60000)]
test_dataset = [next(dataset_iterator) for _ in range(1000)]

```

Now, let’s create a collection and index the training data. This collection will be created with the default configuration. Please be aware that
it might be different from your collection settings, and it’s always important to test exactly the same configuration you are going to use later
in production.

```python
from qdrant_client import QdrantClient, models

client = QdrantClient("http://localhost:6333")
client.create_collection(
    collection_name="arxiv-titles-instructorxl-embeddings",
    vectors_config=models.VectorParams(
        size=768,  # Size of the embeddings generated by InstructorXL model
        distance=models.Distance.COSINE,
    ),
)

```

We are now ready to index the training data. Uploading the records is going to trigger the indexing process, which will build the HNSW graph.
The indexing process may take some time, depending on the size of the dataset, but your data is going to be available for search immediately
after receiving the response from the `upsert` endpoint. **As long as the indexing is not finished, and HNSW not built, Qdrant will perform**
**the exact search**. We have to wait until the indexing is finished to be sure that the approximate search is performed.

```python
client.upload_points(  # upload_points is available as of qdrant-client v1.7.1
    collection_name="arxiv-titles-instructorxl-embeddings",
    points=[\
        models.PointStruct(\
            id=item["id"],\
            vector=item["vector"],\
            payload=item,\
        )\
        for item in train_dataset\
    ]
)

while True:
    collection_info = client.get_collection(collection_name="arxiv-titles-instructorxl-embeddings")
    if collection_info.status == models.CollectionStatus.GREEN:
        # Collection status is green, which means the indexing is finished
        break

```

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/\#standard-mode-vs-exact-search) Standard mode vs exact search

Qdrant has a built-in exact search mode, which can be used to measure the quality of the search results. In this mode, Qdrant performs a
full kNN search for each query, without any approximation. It is not suitable for production use with high load, but it is perfect for the
evaluation of the ANN algorithm and its parameters. It might be triggered by setting the `exact` parameter to `True` in the search request.
We are simply going to use all the examples from the test dataset as queries and compare the results of the approximate search with the
results of the exact search. Let’s create a helper function with `k` being a parameter, so we can calculate the `precision@k` for different
values of `k`.

```python
def avg_precision_at_k(k: int):
    precisions = []
    for item in test_dataset:
        ann_result = client.query_points(
            collection_name="arxiv-titles-instructorxl-embeddings",
            query=item["vector"],
            limit=k,
        ).points

        knn_result = client.query_points(
            collection_name="arxiv-titles-instructorxl-embeddings",
            query=item["vector"],
            limit=k,
            search_params=models.SearchParams(
                exact=True,  # Turns on the exact search mode
            ),
        ).points

        # We can calculate the precision@k by comparing the ids of the search results
        ann_ids = set(item.id for item in ann_result)
        knn_ids = set(item.id for item in knn_result)
        precision = len(ann_ids.intersection(knn_ids)) / k
        precisions.append(precision)

    return sum(precisions) / len(precisions)

```

Calculating the `precision@5` is as simple as calling the function with the corresponding parameter:

```python
print(f"avg(precision@5) = {avg_precision_at_k(k=5)}")

```

Response:

```text
avg(precision@5) = 0.9935999999999995

```

As we can see, the precision of the approximate search vs exact search is pretty high. There are, however, some scenarios when we
need higher precision and can accept higher latency. HNSW is pretty tunable, and we can increase the precision by changing its parameters.

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/\#tweaking-the-hnsw-parameters) Tweaking the HNSW parameters

HNSW is a hierarchical graph, where each node has a set of links to other nodes. The number of edges per node is called the `m` parameter.
The larger the value of it, the higher the precision of the search, but more space required. The `ef_construct` parameter is the number of
neighbours to consider during the index building. Again, the larger the value, the higher the precision, but the longer the indexing time.
The default values of these parameters are `m=16` and `ef_construct=100`. Let’s try to increase them to `m=32` and `ef_construct=200` and
see how it affects the precision. Of course, we need to wait until the indexing is finished before we can perform the search.

```python
client.update_collection(
    collection_name="arxiv-titles-instructorxl-embeddings",
    hnsw_config=models.HnswConfigDiff(
        m=32,  # Increase the number of edges per node from the default 16 to 32
        ef_construct=200,  # Increase the number of neighbours from the default 100 to 200
    )
)

while True:
    collection_info = client.get_collection(collection_name="arxiv-titles-instructorxl-embeddings")
    if collection_info.status == models.CollectionStatus.GREEN:
        # Collection status is green, which means the indexing is finished
        break

```

The same function can be used to calculate the average `precision@5`:

```python
print(f"avg(precision@5) = {avg_precision_at_k(k=5)}")

```

Response:

```text
avg(precision@5) = 0.9969999999999998

```

The precision has obviously increased, and we know how to control it. However, there is a trade-off between the precision and the search
latency and memory requirements. In some specific cases, we may want to increase the precision as much as possible, so now we know how
to do it.

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/retrieval-quality/\#wrapping-up) Wrapping up

Assessing the quality of retrieval is a critical aspect of [evaluating](https://qdrant.tech/rag/rag-evaluation-guide/) semantic search performance. It is imperative to measure retrieval quality when aiming for optimal quality of.
your search results. Qdrant provides a built-in exact search mode, which can be used to measure the quality of the ANN algorithm itself,
even in an automated way, as part of your CI/CD pipeline.

Again, **the quality of the embeddings is the most important factor**. HNSW does a pretty good job in terms of precision, and it is
parameterizable and tunable, when required. There are some other ANN algorithms available out there, such as [IVF\*](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes#cell-probe-methods-indexivf-indexes),
but they usually [perform worse than HNSW in terms of quality and performance](https://nirantk.com/writing/pgvector-vs-qdrant/#correctness).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/beginner-tutorials/retrieval-quality.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/beginner-tutorials/retrieval-quality.md)
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