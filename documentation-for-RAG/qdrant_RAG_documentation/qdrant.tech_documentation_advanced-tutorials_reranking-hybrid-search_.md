---
url: "https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/"
title: "Reranking in Hybrid Search - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Advanced tutorials](https://qdrant.tech/documentation/advanced-tutorials/)
- Reranking in Hybrid Search

# [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#reranking-hybrid-search-results-with-qdrant-vector-database) Reranking Hybrid Search Results with Qdrant Vector Database

Hybrid search combines dense and sparse retrieval to deliver precise and comprehensive results. By adding reranking with ColBERT, you can further refine search outputs for maximum relevance.

In this guide, we’ll show you how to implement hybrid search with reranking in Qdrant, leveraging dense, sparse, and late interaction embeddings to create an efficient, high-accuracy search system. Let’s get started!

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#overview) Overview

Let’s start by breaking down the architecture:

![image3.png](https://qdrant.tech/documentation/examples/reranking-hybrid-search/image3.png)

Processing Dense, Sparse, and Late Interaction Embeddings in Vector Databases (VDB)

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#ingestion-stage) Ingestion Stage

Here’s how we’re going to set up the advanced hybrid search. The process is similar to what we did earlier but with a few powerful additions:

1. **Documents**: Just like before, we start with the raw input—our set of documents that need to be indexed for search.
2. **Dense Embeddings**: We’ll generate dense embeddings for each document, just like in the basic search. These embeddings capture the deeper, semantic meanings behind the text.
3. **Sparse Embeddings**: This is where it gets interesting. Alongside dense embeddings, we’ll create sparse embeddings using more traditional, keyword-based methods. Specifically, we’ll use BM25, a probabilistic retrieval model. BM25 ranks documents based on how relevant their terms are to a given query, taking into account how often terms appear, document length, and how common the term is across all documents. It’s perfect for keyword-heavy searches.
4. **Late Interaction Embeddings**: Now, we add the magic of ColBERT. ColBERT uses a two-stage approach. First, it generates contextualized embeddings for both queries and documents using BERT, and then it performs late interaction—matching those embeddings efficiently using a dot product to fine-tune relevance. This step allows for deeper, contextual understanding, making sure you get the most precise results.
5. **Vector Database**: All of these embeddings—dense, sparse, and late interaction—are stored in a vector database like Qdrant. This allows you to efficiently search, retrieve, and rerank your documents based on multiple layers of relevance.

![image2.png](https://qdrant.tech/documentation/examples/reranking-hybrid-search/image2.png)

Query Retrieval and Reranking Process in Search Systems

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#retrieval-stage) Retrieval Stage

Now, let’s talk about how we’re going to pull the best results once the user submits a query:

1. **User’s Query**: The user enters a query, and that query is transformed into multiple types of embeddings. We’re talking about representations that capture both the deeper meaning (dense) and specific keywords (sparse).
2. **Embeddings**: The query gets converted into various embeddings—some for understanding the semantics (dense embeddings) and others for focusing on keyword matches (sparse embeddings).
3. **Hybrid Search**: Our hybrid search uses both dense and sparse embeddings to find the most relevant documents. The dense embeddings ensure we capture the overall meaning of the query, while sparse embeddings make sure we don’t miss out on those key, important terms.
4. **Rerank**: Once we’ve got a set of documents, the final step is reranking. This is where late interaction embeddings come into play, giving you results that are not only relevant but tuned to your query by prioritizing the documents that truly meet the user’s intent.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#implementation) Implementation

Let’s see it in action in this section.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#additional-setup) Additional Setup

This time around, we’re using FastEmbed—a lightweight Python library designed for generating embeddings, and it supports popular text models right out of the box. First things first, you’ll need to install it:

```python
pip install fastembed

```

* * *

Here are the models we’ll be pulling from FastEmbed:

```python
from fastembed import TextEmbedding, LateInteractionTextEmbedding, SparseTextEmbedding

```

* * *

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#ingestion) Ingestion

As before, we’ll convert our documents into embeddings, but thanks to FastEmbed, the process is even more straightforward because all the models you need are conveniently available in one location.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#embeddings) Embeddings

First, let’s load the models we need:

```python
dense_embedding_model = TextEmbedding("sentence-transformers/all-MiniLM-L6-v2")
bm25_embedding_model = SparseTextEmbedding("Qdrant/bm25")
late_interaction_embedding_model = LateInteractionTextEmbedding("colbert-ir/colbertv2.0")

```

* * *

Now, let’s convert our documents into embeddings:

```python
dense_embeddings = list(dense_embedding_model.embed(doc for doc in documents))
bm25_embeddings = list(bm25_embedding_model.embed(doc for doc in documents))
late_interaction_embeddings = list(late_interaction_embedding_model.embed(doc for doc in documents))

```

* * *

Since we’re dealing with multiple types of embeddings (dense, sparse, and late interaction), we’ll need to store them in a collection that supports a multi-vector setup. The previous collection we created won’t work here, so we’ll create a new one designed specifically for handling these different types of embeddings.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#create-collection) Create Collection

Now, we’re setting up a new collection in Qdrant for our hybrid search with the right configurations to handle all the different vector types we’re working with.

Here’s how you do it:

```python
from qdrant_client.models import Distance, VectorParams, models

client.create_collection(
    "hybrid-search",
    vectors_config={
        "all-MiniLM-L6-v2": models.VectorParams(
            size=len(dense_embeddings[0]),
            distance=models.Distance.COSINE,
        ),
        "colbertv2.0": models.VectorParams(
            size=len(late_interaction_embeddings[0][0]),
            distance=models.Distance.COSINE,
            multivector_config=models.MultiVectorConfig(
                comparator=models.MultiVectorComparator.MAX_SIM,
            )
        ),
    },
    sparse_vectors_config={
        "bm25": models.SparseVectorParams(modifier=models.Modifier.IDF
        )
    }
)

```

* * *

What’s happening here? We’re creating a collection called “hybrid-search”, and we’re configuring it to handle:

- **Dense embeddings** from the model all-MiniLM-L6-v2 using cosine distance for comparisons.
- **Late interaction embeddings** from colbertv2.0, also using cosine distance, but with a multivector configuration to use the maximum similarity comparator.
- **Sparse embeddings** from BM25 for keyword-based searches. They use dot\_product for similarity calculation.

This setup ensures that all the different types of vectors are stored and compared correctly for your hybrid search.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#upsert-data) Upsert Data

Next, we need to insert the documents along with their multiple embeddings into the **hybrid-search** collection:

```python
from qdrant_client.models import PointStruct
points = []
for idx, (dense_embedding, bm25_embedding, late_interaction_embedding, doc) in enumerate(zip(dense_embeddings, bm25_embeddings, late_interaction_embeddings, documents)):

    point = PointStruct(
        id=idx,
        vector={
            "all-MiniLM-L6-v2": dense_embedding,
            "bm25": bm25_embedding.as_object(),
            "colbertv2.0": late_interaction_embedding,
        },
        payload={"document": doc}
    )
    points.append(point)

operation_info = client.upsert(
    collection_name="hybrid-search",
    points=points
)

```

Upload with implicit embeddings computation

```python
from qdrant_client.models import PointStruct
points = []

for idx, doc in enumerate(documents):
    point = PointStruct(
        id=idx,
        vector={
            "all-MiniLM-L6-v2": models.Document(text=doc, model="sentence-transformers/all-MiniLM-L6-v2"),
            "bm25": models.Document(text=doc, model="Qdrant/bm25"),
            "colbertv2.0": models.Document(text=doc, model="colbert-ir/colbertv2.0"),
        },
        payload={"document": doc}
    )
    points.append(point)

operation_info = client.upsert(
    collection_name="hybrid-search",
    points=points
)

```

* * *

This code pulls everything together by creating a list of **PointStruct** objects, each containing the embeddings and corresponding documents.

For each document, it adds:

- **Dense embeddings** for the deep, semantic meaning.
- **BM25 embeddings** for powerful keyword-based search.
- **ColBERT embeddings** for precise contextual interactions.

Once that’s done, the points are uploaded into our **“hybrid-search”** collection using the upsert method, ensuring everything’s in place.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#retrieval) Retrieval

For retrieval, it’s time to convert the user’s query into the required embeddings. Here’s how you can do it:

```python
dense_vectors = next(dense_embedding_model.query_embed(query))
sparse_vectors = next(bm25_embedding_model.query_embed(query))
late_vectors = next(late_interaction_embedding_model.query_embed(query))

```

* * *

The real magic of hybrid search lies in the **prefetch** parameter. This lets you run multiple sub-queries in one go, combining the power of dense and sparse embeddings. Here’s how to set it up, after which we execute the hybrid search:

```python
prefetch = [\
        models.Prefetch(\
            query=dense_vectors,\
            using="all-MiniLM-L6-v2",\
            limit=20,\
        ),\
        models.Prefetch(\
            query=models.SparseVector(**sparse_vectors.as_object()),\
            using="bm25",\
            limit=20,\
        ),\
    ]

```

* * *

This code kicks off a hybrid search by running two sub-queries:

- One using dense embeddings from “all-MiniLM-L6-v2” to capture the semantic meaning of the query.
- The other using sparse embeddings from BM25 for strong keyword matching.

Each sub-query is limited to 20 results. These sub-queries are bundled together using the prefetch parameter, allowing them to run in parallel.

### [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#rerank) Rerank

Now that we’ve got our initial hybrid search results, it’s time to rerank them using late interaction embeddings for maximum precision. Here’s how you can do it:

```python
results = client.query_points(
         "hybrid-search",
        prefetch=prefetch,
        query=late_vectors,
        using="colbertv2.0",
        with_payload=True,
        limit=10,
)

```

Query points with implicit embeddings computation

```python
prefetch = [\
        models.Prefetch(\
            query=models.Document(text=query, model="sentence-transformers/all-MiniLM-L6-v2"),\
            using="all-MiniLM-L6-v2",\
            limit=20,\
        ),\
        models.Prefetch(\
            query=models.Document(text=query, model="Qdrant/bm25"),\
            using="bm25",\
            limit=20,\
        ),\
    ]
results = client.query_points(
         "hybrid-search",
        prefetch=prefetch,
        query=models.Document(text=query, model="colbert-ir/colbertv2.0"),
        using="colbertv2.0",
        with_payload=True,
        limit=10,
)

```

* * *

Let’s look at how the positions change after applying reranking. Notice how some documents shift in rank based on their relevance according to the late interaction embeddings.

|  | **Document** | **First Query Rank** | **Second Query Rank** | **Rank Change** |
| --- | --- | --- | --- | --- |
|  | In machine learning, feature scaling is the process of normalizing the range of independent variables or features. The goal is to ensure that all features contribute equally to the model, especially in algorithms like SVM or k-nearest neighbors where distance calculations matter. | 1 | 1 | No Change |
|  | Feature scaling is commonly used in data preprocessing to ensure that features are on the same scale. This is particularly important for gradient descent-based algorithms where features with larger scales could disproportionately impact the cost function. | 2 | 6 | Moved Down |
|  | Unsupervised learning algorithms, such as clustering methods, may benefit from feature scaling, which ensures that features with larger numerical ranges don’t dominate the learning process. | 3 | 4 | Moved Down |
|  | Data preprocessing steps, including feature scaling, can significantly impact the performance of machine learning models, making it a crucial part of the modeling pipeline. | 5 | 2 | Moved Up |

Great! We’ve now explored how reranking works and successfully implemented it.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#best-practices-in-reranking) Best Practices in Reranking

Reranking can dramatically improve the relevance of search results, especially when combined with hybrid search. Here are some best practices to keep in mind:

- **Implement Hybrid Reranking**: Blend keyword-based (sparse) and vector-based (dense) search results for a more comprehensive ranking system.
- **Continuous Testing and Monitoring**: Regularly evaluate your reranking models to avoid overfitting and make timely adjustments to maintain performance.
- **Balance Relevance and Latency**: Reranking can be computationally expensive, so aim for a balance between relevance and speed. Therefore, the first step is to retrieve the relevant documents and then use reranking on it.

## [Anchor](https://qdrant.tech/documentation/advanced-tutorials/reranking-hybrid-search/\#conclusion) Conclusion

Reranking is a powerful tool that boosts the relevance of search results, especially when combined with hybrid search methods. While it can add some latency due to its complexity, applying it to a smaller, pre-filtered subset of results ensures both speed and relevance.

Qdrant offers an easy-to-use API to get started with your own search engine, so if you’re ready to dive in, sign up for free at [Qdrant Cloud](https://qdrant.tech/) and start building

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/reranking-hybrid-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/advanced-tutorials/reranking-hybrid-search.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573861741&cv=11&fst=1748573861741&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Freranking-hybrid-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Reranking%20in%20Hybrid%20Search%20-%20Qdrant&npa=0&pscdl=noapi&auid=1635745258.1748573861&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573861699&cv=11&fst=1748573861699&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Freranking-hybrid-search%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Reranking%20in%20Hybrid%20Search%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1635745258.1748573861&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0b0b4287-b95b-4a5d-ab96-fcc0fa3d7f1d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3ab085fa-5fb6-457a-aee1-e674cacc0574&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Freranking-hybrid-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573862268&cv=11&fst=1748573862268&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Freranking-hybrid-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Reranking%20in%20Hybrid%20Search%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1635745258.1748573861&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0b0b4287-b95b-4a5d-ab96-fcc0fa3d7f1d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=3ab085fa-5fb6-457a-aee1-e674cacc0574&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fadvanced-tutorials%2Freranking-hybrid-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)