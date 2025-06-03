---
url: "https://qdrant.tech/documentation/embeddings/openai/"
title: "OpenAI - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- OpenAI

# [Anchor](https://qdrant.tech/documentation/embeddings/openai/\#openai) OpenAI

Qdrant supports working with [OpenAI embeddings](https://platform.openai.com/docs/guides/embeddings/embeddings).

There is an official OpenAI Python package that simplifies obtaining them, and it can be installed with pip:

```bash
pip install openai

```

### [Anchor](https://qdrant.tech/documentation/embeddings/openai/\#setting-up-the-openai-and-qdrant-clients) Setting up the OpenAI and Qdrant clients

```python
import openai
import qdrant_client

openai_client = openai.Client(
    api_key="<YOUR_API_KEY>"
)

client = qdrant_client.QdrantClient(":memory:")

texts = [\
    "Qdrant is the best vector search engine!",\
    "Loved by Enterprises and everyone building for low latency, high performance, and scale.",\
]

```

The following example shows how to embed a document with the `text-embedding-3-small` model that generates sentence embeddings of size 1536. You can find the list of all supported models [here](https://platform.openai.com/docs/models/embeddings).

### [Anchor](https://qdrant.tech/documentation/embeddings/openai/\#embedding-a-document) Embedding a document

```python
embedding_model = "text-embedding-3-small"

result = openai_client.embeddings.create(input=texts, model=embedding_model)

```

### [Anchor](https://qdrant.tech/documentation/embeddings/openai/\#converting-the-model-outputs-to-qdrant-points) Converting the model outputs to Qdrant points

```python
from qdrant_client.models import PointStruct

points = [\
    PointStruct(\
        id=idx,\
        vector=data.embedding,\
        payload={"text": text},\
    )\
    for idx, (data, text) in enumerate(zip(result.data, texts))\
]

```

### [Anchor](https://qdrant.tech/documentation/embeddings/openai/\#creating-a-collection-to-insert-the-documents) Creating a collection to insert the documents

```python
from qdrant_client.models import VectorParams, Distance

collection_name = "example_collection"

client.create_collection(
    collection_name,
    vectors_config=VectorParams(
        size=1536,
        distance=Distance.COSINE,
    ),
)
client.upsert(collection_name, points)

```

## [Anchor](https://qdrant.tech/documentation/embeddings/openai/\#searching-for-documents-with-qdrant) Searching for documents with Qdrant

Once the documents are indexed, you can search for the most relevant documents using the same model.

```python
client.search(
    collection_name=collection_name,
    query_vector=openai_client.embeddings.create(
        input=["What is the best to use for vector search scaling?"],
        model=embedding_model,
    )
    .data[0]
    .embedding,
)

```

## [Anchor](https://qdrant.tech/documentation/embeddings/openai/\#using-openai-embedding-models-with-qdrants-binary-quantization) Using OpenAI Embedding Models with Qdrant’s Binary Quantization

You can use OpenAI embedding Models with [Binary Quantization](https://qdrant.tech/articles/binary-quantization/) \- a technique that allows you to reduce the size of the embeddings by 32 times without losing the quality of the search results too much.

| Method | Dimensionality | Test Dataset | Recall | Oversampling |
| --- | --- | --- | --- | --- |
| OpenAI text-embedding-3-large | 3072 | [DBpedia 1M](https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-large-3072-1M) | 0.9966 | 3x |
| OpenAI text-embedding-3-small | 1536 | [DBpedia 100K](https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-small-1536-100K) | 0.9847 | 3x |
| OpenAI text-embedding-3-large | 1536 | [DBpedia 1M](https://huggingface.co/datasets/Qdrant/dbpedia-entities-openai3-text-embedding-3-large-1536-1M) | 0.9826 | 3x |
| OpenAI text-embedding-ada-002 | 1536 | [DbPedia 1M](https://huggingface.co/datasets/KShivendu/dbpedia-entities-openai-1M) | 0.98 | 4x |

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/openai.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/openai.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ada49d93-9e26-4978-93f6-24f6c3712de0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ee3af354-1ba6-4146-b763-6c1e3cb7a589&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fopenai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575418098&cv=11&fst=1748575418098&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fopenai%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=OpenAI%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=45845121.1748575418&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575418143&cv=11&fst=1748575418143&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fopenai%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=OpenAI%20-%20Qdrant&npa=0&pscdl=noapi&auid=45845121.1748575418&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575418290&cv=11&fst=1748575418290&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fopenai%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=OpenAI%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=45845121.1748575418&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ada49d93-9e26-4978-93f6-24f6c3712de0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ee3af354-1ba6-4146-b763-6c1e3cb7a589&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fopenai%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)