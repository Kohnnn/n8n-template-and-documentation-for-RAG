---
url: "https://qdrant.tech/articles/late-interaction-models/"
title: "Any* Embedding Model Can Become a Late Interaction Model... If You Give It a Chance! - Qdrant"
---

- [Articles](https://qdrant.tech/articles/)
- Any\* Embedding Model Can Become a Late Interaction Model... If You Give It a Chance!

[Back to Machine Learning](https://qdrant.tech/articles/machine-learning/)

# Any\* Embedding Model Can Become a Late Interaction Model... If You Give It a Chance!

Kacper Łukawski

·

August 14, 2024

![Any* Embedding Model Can Become a Late Interaction Model... If You Give It a Chance!](https://qdrant.tech/articles_data/late-interaction-models/preview/title.jpg)

\\* At least any open-source model, since you need access to its internals.

## [Anchor](https://qdrant.tech/articles/late-interaction-models/\#you-can-adapt-dense-embedding-models-for-late-interaction) You Can Adapt Dense Embedding Models for Late Interaction

Qdrant 1.10 introduced support for multi-vector representations, with late interaction being a prominent example of this model. In essence, both documents and queries are represented by multiple vectors, and identifying the most relevant documents involves calculating a score based on the similarity between the corresponding query and document embeddings. If you’re not familiar with this paradigm, our updated [Hybrid Search](https://qdrant.tech/articles/hybrid-search/) article explains how multi-vector representations can enhance retrieval quality.

**Figure 1:** We can visualize late interaction between corresponding document-query embedding pairs.

![Late interaction model](https://qdrant.tech/articles_data/late-interaction-models/late-interaction.png)

There are many specialized late interaction models, such as [ColBERT](https://qdrant.tech/documentation/fastembed/fastembed-colbert/), but **it appears that regular dense embedding models can also be effectively utilized in this manner**.

> In this study, we will demonstrate that standard dense embedding models, traditionally used for single-vector representations, can be effectively adapted for late interaction scenarios using output token embeddings as multi-vector representations.

By testing out retrieval with Qdrant’s multi-vector feature, we will show that these models can rival or surpass specialized late interaction models in retrieval performance, while offering lower complexity and greater efficiency. This work redefines the potential of dense models in advanced search pipelines, presenting a new method for optimizing retrieval systems.

## [Anchor](https://qdrant.tech/articles/late-interaction-models/\#understanding-embedding-models) Understanding Embedding Models

The inner workings of embedding models might be surprising to some. The model doesn’t operate directly on the input text; instead, it requires a tokenization step to convert the text into a sequence of token identifiers. Each token identifier is then passed through an embedding layer, which transforms it into a dense vector. Essentially, the embedding layer acts as a lookup table that maps token identifiers to dense vectors. These vectors are then fed into the transformer model as input.

**Figure 2:** The tokenization step, which takes place before vectors are added to the transformer model.

![Input token embeddings](https://qdrant.tech/articles_data/late-interaction-models/input-embeddings.png)

The input token embeddings are context-free and are learned during the model’s training process. This means that each token always receives the same embedding, regardless of its position in the text. At this stage, the token embeddings are unaware of the context in which they appear. It is the transformer model’s role to contextualize these embeddings.

Much has been discussed about the role of attention in transformer models, but in essence, this mechanism is responsible for capturing cross-token relationships. Each transformer module takes a sequence of token embeddings as input and produces a sequence of output token embeddings. Both sequences are of the same length, with each token embedding being enriched by information from the other token embeddings at the current step.

**Figure 3:** The mechanism that produces a sequence of output token embeddings.

![Output token embeddings](https://qdrant.tech/articles_data/late-interaction-models/output-embeddings.png)

**Figure 4:** The final step performed by the embedding model is pooling the output token embeddings to generate a single vector representation of the input text.

![Pooling](https://qdrant.tech/articles_data/late-interaction-models/pooling.png)

There are several pooling strategies, but regardless of which one a model uses, the output is always a single vector representation, which inevitably loses some information about the input. It’s akin to giving someone detailed, step-by-step directions to the nearest grocery store versus simply pointing in the general direction. While the vague direction might suffice in some cases, the detailed instructions are more likely to lead to the desired outcome.

## [Anchor](https://qdrant.tech/articles/late-interaction-models/\#using-output-token-embeddings-for-multi-vector-representations) Using Output Token Embeddings for Multi-Vector Representations

We often overlook the output token embeddings, but the fact is—they also serve as multi-vector representations of the input text. So, why not explore their use in a multi-vector retrieval model, similar to late interaction models?

### [Anchor](https://qdrant.tech/articles/late-interaction-models/\#experimental-findings) Experimental Findings

We conducted several experiments to determine whether output token embeddings could be effectively used in place of traditional late interaction models. The results are quite promising.

| Dataset | Model | Experiment | NDCG@10 |
| --- | --- | --- | --- |
| SciFact | `prithivida/Splade_PP_en_v1` | sparse vectors | 0.70928 |
| `colbert-ir/colbertv2.0` | late interaction model | 0.69579 |
| `all-MiniLM-L6-v2` | single dense vector representation | 0.64508 |
| output token embeddings | 0.70724 |
| `BAAI/bge-small-en` | single dense vector representation | 0.68213 |
| output token embeddings | 0.73696 |
|  |
| NFCorpus | `prithivida/Splade_PP_en_v1` | sparse vectors | 0.34166 |
| `colbert-ir/colbertv2.0` | late interaction model | 0.35036 |
| `all-MiniLM-L6-v2` | single dense vector representation | 0.31594 |
| output token embeddings | 0.35779 |
| `BAAI/bge-small-en` | single dense vector representation | 0.29696 |
| output token embeddings | 0.37502 |
|  |
| ArguAna | `prithivida/Splade_PP_en_v1` | sparse vectors | 0.47271 |
| `colbert-ir/colbertv2.0` | late interaction model | 0.44534 |
| `all-MiniLM-L6-v2` | single dense vector representation | 0.50167 |
| output token embeddings | 0.45997 |
| `BAAI/bge-small-en` | single dense vector representation | 0.58857 |
| output token embeddings | 0.57648 |

The [source code for these experiments is open-source](https://github.com/kacperlukawski/beir-qdrant/blob/main/examples/retrieval/search/evaluate_all_exact.py) and utilizes [`beir-qdrant`](https://github.com/kacperlukawski/beir-qdrant), an integration of Qdrant with the [BeIR library](https://github.com/beir-cellar/beir). While this package is not officially maintained by the Qdrant team, it may prove useful for those interested in experimenting with various Qdrant configurations to see how they impact retrieval quality. All experiments were conducted using Qdrant in exact search mode, ensuring the results are not influenced by approximate search.

Even the simple `all-MiniLM-L6-v2` model can be applied in a late interaction model fashion, resulting in a positive impact on retrieval quality. However, the best results were achieved with the `BAAI/bge-small-en` model, which outperformed both sparse and late interaction models.

It’s important to note that ColBERT has not been trained on BeIR datasets, making its performance fully out of domain. Nevertheless, the `all-MiniLM-L6-v2` [training dataset](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2#training-data) also lacks any BeIR data, yet it still performs remarkably well.

## [Anchor](https://qdrant.tech/articles/late-interaction-models/\#comparative-analysis-of-dense-vs-late-interaction-models) Comparative Analysis of Dense vs. Late Interaction Models

The retrieval quality speaks for itself, but there are other important factors to consider.

The traditional dense embedding models we tested are less complex than late interaction or sparse models. With fewer parameters, these models are expected to be faster during inference and more cost-effective to maintain. Below is a comparison of the models used in the experiments:

| Model | Number of parameters |
| --- | --- |
| `prithivida/Splade_PP_en_v1` | 109,514,298 |
| `colbert-ir/colbertv2.0` | 109,580,544 |
| `BAAI/bge-small-en` | 33,360,000 |
| `all-MiniLM-L6-v2` | 22,713,216 |

One argument against using output token embeddings is the increased storage requirements compared to ColBERT-like models. For instance, the `all-MiniLM-L6-v2` model produces 384-dimensional output token embeddings, which is three times more than the 128-dimensional embeddings generated by ColBERT-like models. This increase not only leads to higher memory usage but also impacts the computational cost of retrieval, as calculating distances takes more time. Mitigating this issue through vector compression would make a lot of sense.

## [Anchor](https://qdrant.tech/articles/late-interaction-models/\#exploring-quantization-for-multi-vector-representations) Exploring Quantization for Multi-Vector Representations

Binary quantization is generally more effective for high-dimensional vectors, making the `all-MiniLM-L6-v2` model, with its relatively low-dimensional outputs, less ideal for this approach. However, scalar quantization appeared to be a viable alternative. The table below summarizes the impact of quantization on retrieval quality.

| Dataset | Model | Experiment | NDCG@10 |
| --- | --- | --- | --- |
| SciFact | `all-MiniLM-L6-v2` | output token embeddings | 0.70724 |
| output token embeddings (uint8) | 0.70297 |
|  |
| NFCorpus | `all-MiniLM-L6-v2` | output token embeddings | 0.35779 |
| output token embeddings (uint8) | 0.35572 |

It’s important to note that quantization doesn’t always preserve retrieval quality at the same level, but in this case, scalar quantization appears to have minimal impact on retrieval performance. The effect is negligible, while the memory savings are substantial.

We managed to maintain the original quality while using four times less memory. Additionally, a quantized vector requires 384 bytes, compared to ColBERT’s 512 bytes. This results in a 25% reduction in memory usage, with retrieval quality remaining nearly unchanged.

## [Anchor](https://qdrant.tech/articles/late-interaction-models/\#practical-application-enhancing-retrieval-with-dense-models) Practical Application: Enhancing Retrieval with Dense Models

If you’re using one of the sentence transformer models, the output token embeddings are calculated by default. While a single vector representation is more efficient in terms of storage and computation, there’s no need to discard the output token embeddings. According to our experiments, these embeddings can significantly enhance retrieval quality. You can store both the single vector and the output token embeddings in Qdrant, using the single vector for the initial retrieval step and then reranking the results with the output token embeddings.

**Figure 5:** A single model pipeline that relies solely on the output token embeddings for reranking.

![Single model reranking](https://qdrant.tech/articles_data/late-interaction-models/single-model-reranking.png)

To demonstrate this concept, we implemented a simple reranking pipeline in Qdrant. This pipeline uses a dense embedding model for the initial oversampled retrieval and then relies solely on the output token embeddings for the reranking step.

### [Anchor](https://qdrant.tech/articles/late-interaction-models/\#single-model-retrieval-and-reranking-benchmarks) Single Model Retrieval and Reranking Benchmarks

Our tests focused on using the same model for both retrieval and reranking. The reported metric is NDCG@10. In all tests, we applied an oversampling factor of 5x, meaning the retrieval step returned 50 results, which were then narrowed down to 10 during the reranking step. Below are the results for some of the BeIR datasets:

| Dataset | `all-miniLM-L6-v2` | `BAAI/bge-small-en` |
| --- | --- | --- |
| dense embeddings only | dense + reranking | dense embeddings only | dense + reranking |
| --- | --- | --- | --- |
| SciFact | 0.64508 | 0.70293 | 0.68213 | 0.73053 |
| NFCorpus | 0.31594 | 0.34297 | 0.29696 | 0.35996 |
| ArguAna | 0.50167 | 0.45378 | 0.58857 | 0.57302 |
| Touche-2020 | 0.16904 | 0.19693 | 0.13055 | 0.19821 |
| TREC-COVID | 0.47246 | 0.6379 | 0.45788 | 0.53539 |
| FiQA-2018 | 0.36867 | 0.41587 | 0.31091 | 0.39067 |

The source code for the benchmark is publicly available, and [you can find it in the repository of the `beir-qdrant` package](https://github.com/kacperlukawski/beir-qdrant/blob/main/examples/retrieval/search/evaluate_reranking.py).

Overall, adding a reranking step using the same model typically improves retrieval quality. However, the quality of various late interaction models is [often reported based on their reranking performance when BM25 is used for the initial retrieval](https://huggingface.co/mixedbread-ai/mxbai-colbert-large-v1#1-reranking-performance). This experiment aimed to demonstrate how a single model can be effectively used for both retrieval and reranking, and the results are quite promising.

Now, let’s explore how to implement this using the new Query API introduced in Qdrant 1.10.

## [Anchor](https://qdrant.tech/articles/late-interaction-models/\#setting-up-qdrant-for-late-interaction) Setting Up Qdrant for Late Interaction

The new Query API in Qdrant 1.10 enables the construction of even more complex retrieval pipelines. We can use the single vector created after pooling for the initial retrieval step and then rerank the results using the output token embeddings.

Assuming the collection is named `my-collection` and is configured to store two named vectors: `dense-vector` and `output-token-embeddings`, here’s how such a collection could be created in Qdrant:

```python
from qdrant_client import QdrantClient, models

client = QdrantClient("http://localhost:6333")

client.create_collection(
    collection_name="my-collection",
    vectors_config={
        "dense-vector": models.VectorParams(
            size=384,
            distance=models.Distance.COSINE,
        ),
        "output-token-embeddings": models.VectorParams(
            size=384,
            distance=models.Distance.COSINE,
            multivector_config=models.MultiVectorConfig(
                comparator=models.MultiVectorComparator.MAX_SIM
            ),
        ),
    }
)

```

Both vectors are of the same size since they are produced by the same `all-MiniLM-L6-v2` model.

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

```

Now, instead of using the search API with just a single dense vector, we can create a reranking pipeline. First, we retrieve 50 results using the dense vector, and then we rerank them using the output token embeddings to obtain the top 10 results.

```python
query = "What else can be done with just all-MiniLM-L6-v2 model?"

client.query_points(
    collection_name="my-collection",
    prefetch=[\
        # Prefetch the dense embeddings of the top-50 documents\
        models.Prefetch(\
            query=model.encode(query).tolist(),\
            using="dense-vector",\
            limit=50,\
        )\
    ],
    # Rerank the top-50 documents retrieved by the dense embedding model
    # and return just the top-10. Please note we call the same model, but
    # we ask for the token embeddings by setting the output_value parameter.
    query=model.encode(query, output_value="token_embeddings").tolist(),
    using="output-token-embeddings",
    limit=10,
)

```

## [Anchor](https://qdrant.tech/articles/late-interaction-models/\#try-the-experiment-yourself) Try the Experiment Yourself

In a real-world scenario, you might take it a step further by first calculating the token embeddings and then performing pooling to obtain the single vector representation. This approach allows you to complete everything in a single pass.

The simplest way to start experimenting with building complex reranking pipelines in Qdrant is by using the forever-free cluster on [Qdrant Cloud](https://cloud.qdrant.io/?ajs_anonymous_id=32dd7203-471e-4298-8b65-cc21cb5d0670) and reading [Qdrant’s documentation](https://qdrant.tech/documentation/).

The [source code for these experiments is open-source](https://github.com/kacperlukawski/beir-qdrant/blob/main/examples/retrieval/search/evaluate_all_exact.py) and uses [`beir-qdrant`](https://github.com/kacperlukawski/beir-qdrant), an integration of Qdrant with the [BeIR library](https://github.com/beir-cellar/beir).

## [Anchor](https://qdrant.tech/articles/late-interaction-models/\#future-directions-and-research-opportunities) Future Directions and Research Opportunities

The initial experiments using output token embeddings in the retrieval process have yielded promising results. However, we plan to conduct further benchmarks to validate these findings and explore the incorporation of sparse methods for the initial retrieval. Additionally, we aim to investigate the impact of quantization on multi-vector representations and its effects on retrieval quality. Finally, we will assess retrieval speed, a crucial factor for many applications.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/late-interaction-models.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/late-interaction-models.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574426441&cv=11&fst=1748574426441&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Flate-interaction-models%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Any*%20Embedding%20Model%20Can%20Become%20a%20Late%20Interaction%20Model...%20If%20You%20Give%20It%20a%20Chance!%20-%20Qdrant&npa=0&pscdl=noapi&auid=427077316.1748574426&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574426386&cv=11&fst=1748574426386&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Flate-interaction-models%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Any*%20Embedding%20Model%20Can%20Become%20a%20Late%20Interaction%20Model...%20If%20You%20Give%20It%20a%20Chance!%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=427077316.1748574426&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=24b6b70d-f4cb-4dbe-9a7c-d8a0096c3136&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=07c9aea0-37ff-4351-ba95-f6192f7543a5&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Flate-interaction-models%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=24b6b70d-f4cb-4dbe-9a7c-d8a0096c3136&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=07c9aea0-37ff-4351-ba95-f6192f7543a5&tw_document_href=https%3A%2F%2Fqdrant.tech%2Farticles%2Flate-interaction-models%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574427654&cv=11&fst=1748574427654&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Farticles%2Flate-interaction-models%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Any*%20Embedding%20Model%20Can%20Become%20a%20Late%20Interaction%20Model...%20If%20You%20Give%20It%20a%20Chance!%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=427077316.1748574426&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)