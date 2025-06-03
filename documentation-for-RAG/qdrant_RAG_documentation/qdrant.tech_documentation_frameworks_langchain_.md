---
url: "https://qdrant.tech/documentation/frameworks/langchain/"
title: "Langchain - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Langchain

# [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#langchain) Langchain

Langchain is a library that makes developing Large Language Model-based applications much easier. It unifies the interfaces
to different libraries, including major embedding providers and Qdrant. Using Langchain, you can focus on the business value instead of writing the boilerplate.

Langchain distributes the Qdrant integration as a partner package.

It might be installed with pip:

```bash
pip install langchain-qdrant

```

The integration supports searching for relevant documents usin dense/sparse and hybrid retrieval.

Qdrant acts as a vector index that may store the embeddings with the documents used to generate them. There are various ways to use it, but calling `QdrantVectorStore.from_texts` or `QdrantVectorStore.from_documents` is probably the most straightforward way to get started:

```python
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

doc_store = QdrantVectorStore.from_texts(
    texts, embeddings, url="<qdrant-url>", api_key="<qdrant-api-key>", collection_name="texts"
)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#using-an-existing-collection) Using an existing collection

To get an instance of `langchain_qdrant.QdrantVectorStore` without loading any new documents or texts, you can use the `QdrantVectorStore.from_existing_collection()` method.

```python
doc_store = QdrantVectorStore.from_existing_collection(
    embeddings=embeddings,
    collection_name="my_documents",
    url="<qdrant-url>",
    api_key="<qdrant-api-key>",
)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#local-mode) Local mode

Python client allows you to run the same code in local mode without running the Qdrant server. That’s great for testing things
out and debugging or if you plan to store just a small amount of vectors. The embeddings might be fully kept in memory or
persisted on disk.

### [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#in-memory) In-memory

For some testing scenarios and quick experiments, you may prefer to keep all the data in memory only, so it gets lost when the
client is destroyed - usually at the end of your script/notebook.

```python
qdrant = QdrantVectorStore.from_documents(
    docs,
    embeddings,
    location=":memory:",  # Local mode with in-memory storage only
    collection_name="my_documents",
)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#on-disk-storage) On-disk storage

Local mode, without using the Qdrant server, may also store your vectors on disk so they’re persisted between runs.

```python
qdrant = Qdrant.from_documents(
    docs,
    embeddings,
    path="/tmp/local_qdrant",
    collection_name="my_documents",
)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#on-premise-server-deployment) On-premise server deployment

No matter if you choose to launch QdrantVectorStore locally with [a Docker container](https://qdrant.tech/documentation/guides/installation/), or
select a Kubernetes deployment with [the official Helm chart](https://github.com/qdrant/qdrant-helm), the way you’re
going to connect to such an instance will be identical. You’ll need to provide a URL pointing to the service.

```python
url = "<---qdrant url here --->"
qdrant = QdrantVectorStore.from_documents(
    docs,
    embeddings,
    url,
    prefer_grpc=True,
    collection_name="my_documents",
)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#similarity-search) Similarity search

`QdrantVectorStore` supports 3 modes for similarity searches. They can be configured using the `retrieval_mode` parameter when setting up the class.

- Dense Vector Search(Default)
- Sparse Vector Search
- Hybrid Search

### [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#dense-vector-search) Dense Vector Search

To search with only dense vectors,

- The `retrieval_mode` parameter should be set to `RetrievalMode.DENSE`(default).
- A [dense embeddings](https://python.langchain.com/v0.2/docs/integrations/text_embedding/) value should be provided for the `embedding` parameter.

```py
from langchain_qdrant import RetrievalMode

qdrant = QdrantVectorStore.from_documents(
    docs,
    embedding=embeddings,
    location=":memory:",
    collection_name="my_documents",
    retrieval_mode=RetrievalMode.DENSE,
)

query = "What did the president say about Ketanji Brown Jackson"
found_docs = qdrant.similarity_search(query)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#sparse-vector-search) Sparse Vector Search

To search with only sparse vectors,

- The `retrieval_mode` parameter should be set to `RetrievalMode.SPARSE`.
- An implementation of the [SparseEmbeddings interface](https://github.com/langchain-ai/langchain/blob/master/libs/partners/qdrant/langchain_qdrant/sparse_embeddings.py) using any sparse embeddings provider has to be provided as value to the `sparse_embedding` parameter.

The `langchain-qdrant` package provides a [FastEmbed](https://github.com/qdrant/fastembed) based implementation out of the box.

To use it, install the [FastEmbed package](https://github.com/qdrant/fastembed#-installation).

```python
from langchain_qdrant import FastEmbedSparse, RetrievalMode

sparse_embeddings = FastEmbedSparse(model_name="Qdrant/BM25")

qdrant = QdrantVectorStore.from_documents(
    docs,
    sparse_embedding=sparse_embeddings,
    location=":memory:",
    collection_name="my_documents",
    retrieval_mode=RetrievalMode.SPARSE,
)

query = "What did the president say about Ketanji Brown Jackson"
found_docs = qdrant.similarity_search(query)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#hybrid-vector-search) Hybrid Vector Search

To perform a hybrid search using dense and sparse vectors with score fusion,

- The `retrieval_mode` parameter should be set to `RetrievalMode.HYBRID`.
- A [dense embeddings](https://python.langchain.com/v0.2/docs/integrations/text_embedding/) value should be provided for the `embedding` parameter.
- An implementation of the [SparseEmbeddings interface](https://github.com/langchain-ai/langchain/blob/master/libs/partners/qdrant/langchain_qdrant/sparse_embeddings.py) using any sparse embeddings provider has to be provided as value to the `sparse_embedding` parameter.

```python
from langchain_qdrant import FastEmbedSparse, RetrievalMode

sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

qdrant = QdrantVectorStore.from_documents(
    docs,
    embedding=embeddings,
    sparse_embedding=sparse_embeddings,
    location=":memory:",
    collection_name="my_documents",
    retrieval_mode=RetrievalMode.HYBRID,
)

query = "What did the president say about Ketanji Brown Jackson"
found_docs = qdrant.similarity_search(query)

```

Note that if you’ve added documents with HYBRID mode, you can switch to any retrieval mode when searching. Since both the dense and sparse vectors are available in the collection.

## [Anchor](https://qdrant.tech/documentation/frameworks/langchain/\#next-steps) Next steps

If you’d like to know more about running Qdrant in a Langchain-based application, please read our article
[Question Answering with Langchain and Qdrant without boilerplate](https://qdrant.tech/articles/langchain-integration/). Some more information
might also be found in the [Langchain documentation](https://python.langchain.com/docs/integrations/vectorstores/qdrant).

- [Source Code](https://github.com/langchain-ai/langchain/tree/master/libs%2Fpartners%2Fqdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/langchain.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/langchain.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574416550&cv=11&fst=1748574416550&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain%2F&hn=www.googleadservices.com&frm=0&tiba=Langchain%20-%20Qdrant&npa=0&pscdl=noapi&auid=1644573058.1748574416&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574416523&cv=11&fst=1748574416523&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Langchain%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1644573058.1748574416&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1943c507-dafd-4bad-9aaa-35b07a726c00&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a6dfb698-882f-4fb3-89b0-6e2d46827f84&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1943c507-dafd-4bad-9aaa-35b07a726c00&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a6dfb698-882f-4fb3-89b0-6e2d46827f84&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574417574&cv=11&fst=1748574417574&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Flangchain%2F&hn=www.googleadservices.com&frm=0&tiba=Langchain%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1644573058.1748574416&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)