---
url: "https://qdrant.tech/documentation/embeddings/gemini/"
title: "Gemini - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Gemini

| Time: 10 min | Level: Beginner | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/qdrant/examples/blob/gemini-getting-started/gemini-getting-started/gemini-getting-started.ipynb) |
| --- | --- | --- |

# [Anchor](https://qdrant.tech/documentation/embeddings/gemini/\#gemini) Gemini

Qdrant is compatible with Gemini Embedding Model API and its official Python SDK that can be installed as any other package:

Gemini is a new family of Google PaLM models, released in December 2023. The new embedding models succeed the previous Gecko Embedding Model.

In the latest models, an additional parameter, `task_type`, can be passed to the API call. This parameter serves to designate the intended purpose for the embeddings utilized.

The Embedding Model API supports various task types, outlined as follows:

1. `retrieval_query`: query in a search/retrieval setting
2. `retrieval_document`: document from the corpus being searched
3. `semantic_similarity`: semantic text similarity
4. `classification`: embeddings to be used for text classification
5. `clustering`: the generated embeddings will be used for clustering
6. `task_type_unspecified`: Unset value, which will default to one of the other values.

If you’re building a semantic search application, such as RAG, you should use `task_type="retrieval_document"` for the indexed documents and `task_type="retrieval_query"` for the search queries.

The following example shows how to do this with Qdrant:

## [Anchor](https://qdrant.tech/documentation/embeddings/gemini/\#setup) Setup

```bash
pip install google-generativeai

```

Let’s see how to use the Embedding Model API to embed a document for retrieval.

The following example shows how to embed a document with the `models/embedding-001` with the `retrieval_document` task type:

## [Anchor](https://qdrant.tech/documentation/embeddings/gemini/\#embedding-a-document) Embedding a document

```python
import google.generativeai as gemini_client
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

collection_name = "example_collection"

GEMINI_API_KEY = "YOUR GEMINI API KEY"  # add your key here

client = QdrantClient(url="http://localhost:6333")
gemini_client.configure(api_key=GEMINI_API_KEY)
texts = [\
    "Qdrant is a vector database that is compatible with Gemini.",\
    "Gemini is a new family of Google PaLM models, released in December 2023.",\
]

results = [\
    gemini_client.embed_content(\
        model="models/embedding-001",\
        content=sentence,\
        task_type="retrieval_document",\
        title="Qdrant x Gemini",\
    )\
    for sentence in texts\
]

```

## [Anchor](https://qdrant.tech/documentation/embeddings/gemini/\#creating-qdrant-points-and-indexing-documents-with-qdrant) Creating Qdrant Points and Indexing documents with Qdrant

### [Anchor](https://qdrant.tech/documentation/embeddings/gemini/\#creating-qdrant-points) Creating Qdrant Points

```python
points = [\
    PointStruct(\
        id=idx,\
        vector=response['embedding'],\
        payload={"text": text},\
    )\
    for idx, (response, text) in enumerate(zip(results, texts))\
]

```

### [Anchor](https://qdrant.tech/documentation/embeddings/gemini/\#create-collection) Create Collection

```python
client.create_collection(collection_name, vectors_config=
    VectorParams(
        size=768,
        distance=Distance.COSINE,
    )
)

```

### [Anchor](https://qdrant.tech/documentation/embeddings/gemini/\#add-these-into-the-collection) Add these into the collection

```python
client.upsert(collection_name, points)

```

## [Anchor](https://qdrant.tech/documentation/embeddings/gemini/\#searching-for-documents-with-qdrant) Searching for documents with Qdrant

Once the documents are indexed, you can search for the most relevant documents using the same model with the `retrieval_query` task type:

```python
client.search(
    collection_name=collection_name,
    query_vector=gemini_client.embed_content(
        model="models/embedding-001",
        content="Is Qdrant compatible with Gemini?",
        task_type="retrieval_query",
    )["embedding"],
)

```

## [Anchor](https://qdrant.tech/documentation/embeddings/gemini/\#using-gemini-embedding-models-with-binary-quantization) Using Gemini Embedding Models with Binary Quantization

You can use Gemini Embedding Models with [Binary Quantization](https://qdrant.tech/articles/binary-quantization/) \- a technique that allows you to reduce the size of the embeddings by 32 times without losing the quality of the search results too much.

In this table, you can see the results of the search with the `models/embedding-001` model with Binary Quantization in comparison with the original model:

At an oversampling of 3 and a limit of 100, we’ve a 95% recall against the exact nearest neighbors with rescore enabled.

| Oversampling |  | 1 | 1 | 2 | 2 | 3 | 3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | **Rescore** | False | True | False | True | False | True |
| **Limit** |  |  |  |  |  |  |  |
| 10 |  | 0.523333 | 0.831111 | 0.523333 | 0.915556 | 0.523333 | 0.950000 |
| 20 |  | 0.510000 | 0.836667 | 0.510000 | 0.912222 | 0.510000 | 0.937778 |
| 50 |  | 0.489111 | 0.841556 | 0.489111 | 0.913333 | 0.488444 | 0.947111 |
| 100 |  | 0.485778 | 0.846556 | 0.485556 | 0.929000 | 0.486000 | **0.956333** |

That’s it! You can now use Gemini Embedding Models with Qdrant!

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/gemini.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/gemini.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573600800&cv=11&fst=1748573600800&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fgemini%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Gemini%20-%20Qdrant&npa=0&pscdl=noapi&auid=1325320209.1748573601&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573600767&cv=11&fst=1748573600767&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fgemini%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Gemini%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1325320209.1748573601&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=79f825f8-e365-4699-bc10-0c261166242d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=cbede886-2df8-4471-94df-b2d1c3b87ae4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fgemini%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=79f825f8-e365-4699-bc10-0c261166242d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=cbede886-2df8-4471-94df-b2d1c3b87ae4&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fgemini%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573601863&cv=11&fst=1748573601863&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fgemini%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Gemini%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1325320209.1748573601&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)