---
url: "https://qdrant.tech/documentation/embeddings/mistral/"
title: "Mistral - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Mistral

| Time: 10 min | Level: Beginner | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/qdrant/examples/blob/mistral-getting-started/mistral-embed-getting-started/mistral_qdrant_getting_started.ipynb) |
| --- | --- | --- |

# [Anchor](https://qdrant.tech/documentation/embeddings/mistral/\#mistral) Mistral

Qdrant is compatible with the new released Mistral Embed and its official Python SDK that can be installed as any other package:

## [Anchor](https://qdrant.tech/documentation/embeddings/mistral/\#setup) Setup

### [Anchor](https://qdrant.tech/documentation/embeddings/mistral/\#install-the-client) Install the client

```bash
pip install mistralai

```

And then we set this up:

```python
from mistralai.client import MistralClient
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

collection_name = "example_collection"

MISTRAL_API_KEY = "your_mistral_api_key"
client = QdrantClient(":memory:")
mistral_client = MistralClient(api_key=MISTRAL_API_KEY)
texts = [\
    "Qdrant is the best vector search engine!",\
    "Loved by Enterprises and everyone building for low latency, high performance, and scale.",\
]

```

Let’s see how to use the Embedding Model API to embed a document for retrieval.

The following example shows how to embed a document with the `models/embedding-001` with the `retrieval_document` task type:

## [Anchor](https://qdrant.tech/documentation/embeddings/mistral/\#embedding-a-document) Embedding a document

```python
result = mistral_client.embeddings(
    model="mistral-embed",
    input=texts,
)

```

The returned result has a data field with a key: `embedding`. The value of this key is a list of floats representing the embedding of the document.

### [Anchor](https://qdrant.tech/documentation/embeddings/mistral/\#converting-this-into-qdrant-points) Converting this into Qdrant Points

```python
points = [\
    PointStruct(\
        id=idx,\
        vector=response.embedding,\
        payload={"text": text},\
    )\
    for idx, (response, text) in enumerate(zip(result.data, texts))\
]

```

## [Anchor](https://qdrant.tech/documentation/embeddings/mistral/\#create-a-collection-and-insert-the-documents) Create a collection and Insert the documents

```python
client.create_collection(collection_name, vectors_config=VectorParams(
        size=1024,
        distance=Distance.COSINE,
    )
)
client.upsert(collection_name, points)

```

## [Anchor](https://qdrant.tech/documentation/embeddings/mistral/\#searching-for-documents-with-qdrant) Searching for documents with Qdrant

Once the documents are indexed, you can search for the most relevant documents using the same model with the `retrieval_query` task type:

```python
client.search(
    collection_name=collection_name,
    query_vector=mistral_client.embeddings(
        model="mistral-embed", input=["What is the best to use for vector search scaling?"]
    ).data[0].embedding,
)

```

## [Anchor](https://qdrant.tech/documentation/embeddings/mistral/\#using-mistral-embedding-models-with-binary-quantization) Using Mistral Embedding Models with Binary Quantization

You can use Mistral Embedding Models with [Binary Quantization](https://qdrant.tech/articles/binary-quantization/) \- a technique that allows you to reduce the size of the embeddings by 32 times without losing the quality of the search results too much.

At an oversampling of 3 and a limit of 100, we’ve a 95% recall against the exact nearest neighbors with rescore enabled.

| Oversampling |  | 1 | 1 | 2 | 2 | 3 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | **Rescore** | False | True | False | True | False | True |
| **Limit** |  |  |  |  |  |  |  |
| 10 |  | 0.53444 | 0.857778 | 0.534444 | 0.918889 | 0.533333 | 0.941111 |
| 20 |  | 0.508333 | 0.837778 | 0.508333 | 0.903889 | 0.508333 | 0.927778 |
| 50 |  | 0.492222 | 0.834444 | 0.492222 | 0.903556 | 0.492889 | 0.940889 |
| 100 |  | 0.499111 | 0.845444 | 0.498556 | 0.918333 | 0.497667 | **0.944556** |

That’s it! You can now use Mistral Embedding Models with Qdrant!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/mistral.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/mistral.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574493386&cv=11&fst=1748574493386&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmistral%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Mistral%20-%20Qdrant&npa=0&pscdl=noapi&auid=69009005.1748574493&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574493358&cv=11&fst=1748574493358&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmistral%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Mistral%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=69009005.1748574493&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=23f4d5b2-75fd-401b-922a-f6e386a93592&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5dbef757-0102-4f8a-b0cd-705df7fe880c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmistral%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=23f4d5b2-75fd-401b-922a-f6e386a93592&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=5dbef757-0102-4f8a-b0cd-705df7fe880c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmistral%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574494528&cv=11&fst=1748574494528&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fmistral%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Mistral%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=69009005.1748574493&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)