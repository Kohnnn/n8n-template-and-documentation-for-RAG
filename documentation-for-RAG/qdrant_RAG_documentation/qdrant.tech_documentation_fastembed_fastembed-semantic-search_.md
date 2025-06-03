---
url: "https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/"
title: "FastEmbed & Qdrant - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Fastembed](https://qdrant.tech/documentation/fastembed/)
- FastEmbed & Qdrant

# [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/\#using-fastembed-with-qdrant-for-vector-search) Using FastEmbed with Qdrant for Vector Search

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/\#install-qdrant-client-and-fastembed) Install Qdrant Client and FastEmbed

```python
pip install "qdrant-client[fastembed]>=1.14.2"

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/\#initialize-the-client) Initialize the client

Qdrant Client has a simple in-memory mode that lets you try semantic search locally.

```python
from qdrant_client import QdrantClient, models

client = QdrantClient(":memory:")  # Qdrant is running from RAM.

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/\#add-data) Add data

Now you can add two sample documents, their associated metadata, and a point `id` for each.

```python
docs = [\
    "Qdrant has a LangChain integration for chatbots.",\
    "Qdrant has a LlamaIndex integration for agents.",\
]
metadata = [\
    {"source": "langchain-docs"},\
    {"source": "llamaindex-docs"},\
]
ids = [42, 2]

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/\#create-a-collection) Create a collection

Qdrant stores vectors and associated metadata in collections.
Collection requires vector parameters to be set during creation.
In this tutorial, we’ll be using `BAAI/bge-small-en` to compute embeddings.

```python
model_name = "BAAI/bge-small-en"
client.create_collection(
    collection_name="test_collection",
    vectors_config=models.VectorParams(
        size=client.get_embedding_size(model_name),
        distance=models.Distance.COSINE
    ),  # size and distance are model dependent
)

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/\#upsert-documents-to-the-collection) Upsert documents to the collection

Qdrant client can do inference implicitly within its methods via FastEmbed integration.
It requires wrapping your data in models, like `models.Document` (or `models.Image` if you’re working with images)

```python
metadata_with_docs = [\
    {"document": doc, "source": meta["source"]} for doc, meta in zip(docs, metadata)\
]
client.upload_collection(
    collection_name="test_collection",
    vectors=[models.Document(text=doc, model=model_name) for doc in docs],
    payload=metadata_with_docs,
    ids=ids,
)

```

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-semantic-search/\#run-vector-search) Run vector search

Here, you will ask a dummy question that will allow you to retrieve a semantically relevant result.

```python
search_result = client.query_points(
    collection_name="test_collection",
    query=models.Document(
        text="Which integration is best for agents?",
        model=model_name
    )
).points
print(search_result)

```

The semantic search engine will retrieve the most similar result in order of relevance. In this case, the second statement about LlamaIndex is more relevant.

```python
[\
    ScoredPoint(\
        id=2,\
        score=0.87491801319731,\
        payload={\
            "document": "Qdrant has a LlamaIndex integration for agents.",\
            "source": "llamaindex-docs",\
        },\
        ...\
    ),\
    ScoredPoint(\
        id=42,\
        score=0.8351846627714035,\
        payload={\
            "document": "Qdrant has a LangChain integration for chatbots.",\
            "source": "langchain-docs",\
        },\
        ...\
    ),\
]

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/fastembed/fastembed-semantic-search.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/fastembed/fastembed-semantic-search.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573636192&cv=11&fst=1748573636192&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104611959~104611961&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-semantic-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=FastEmbed%20%26%20Qdrant%20-%20Qdrant&npa=0&pscdl=noapi&auid=822572258.1748573636&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573636145&cv=11&fst=1748573636145&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104611959~104611961&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-semantic-search%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=FastEmbed%20%26%20Qdrant%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=822572258.1748573636&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=265610a3-7769-41ee-9d5e-3c8f60a564ce&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=209b243b-2ebf-4d96-b895-0c7b07c1f24e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-semantic-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=265610a3-7769-41ee-9d5e-3c8f60a564ce&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=209b243b-2ebf-4d96-b895-0c7b07c1f24e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-semantic-search%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573637024&cv=11&fst=1748573637024&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104611959~104611961&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Ffastembed%2Ffastembed-semantic-search%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=FastEmbed%20%26%20Qdrant%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=822572258.1748573636&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)