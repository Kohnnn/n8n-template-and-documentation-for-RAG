---
url: "https://qdrant.tech/documentation/frameworks/canopy/"
title: "Pinecone Canopy - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Pinecone Canopy

# [Anchor](https://qdrant.tech/documentation/frameworks/canopy/\#pinecone-canopy) Pinecone Canopy

[Canopy](https://github.com/pinecone-io/canopy) is an open-source framework and context engine to build chat assistants at scale.

Qdrant is supported as a knowledge base within Canopy for context retrieval and augmented generation.

## [Anchor](https://qdrant.tech/documentation/frameworks/canopy/\#usage) Usage

Install the SDK with the Qdrant extra as described in the [Canopy README](https://github.com/pinecone-io/canopy?tab=readme-ov-file#extras).

```bash
pip install canopy-sdk[qdrant]

```

### [Anchor](https://qdrant.tech/documentation/frameworks/canopy/\#creating-a-knowledge-base) Creating a knowledge base

```python
from canopy.knowledge_base import QdrantKnowledgeBase

kb = QdrantKnowledgeBase(collection_name="<YOUR_COLLECTION_NAME>")

```

To create a new Qdrant collection and connect it to the knowledge base, use the `create_canopy_collection` method:

```python
kb.create_canopy_collection()

```

You can always verify the connection to the collection with the `verify_index_connection` method:

```python
kb.verify_index_connection()

```

Learn more about customizing the knowledge base and its inner components [in the Canopy library](https://github.com/pinecone-io/canopy/blob/main/docs/library.md#understanding-knowledgebase-workings).

### [Anchor](https://qdrant.tech/documentation/frameworks/canopy/\#adding-data-to-the-knowledge-base) Adding data to the knowledge base

To insert data into the knowledge base, you can create a list of documents and use the `upsert` method:

```python
from canopy.models.data_models import Document

documents = [\
    Document(\
        id="1",\
        text="U2 are an Irish rock band from Dublin, formed in 1976.",\
        source="https://en.wikipedia.org/wiki/U2",\
    ),\
    Document(\
        id="2",\
        text="Arctic Monkeys are an English rock band formed in Sheffield in 2002.",\
        source="https://en.wikipedia.org/wiki/Arctic_Monkeys",\
        metadata={"my-key": "my-value"},\
    ),\
]

kb.upsert(documents)

```

### [Anchor](https://qdrant.tech/documentation/frameworks/canopy/\#querying-the-knowledge-base) Querying the knowledge base

You can query the knowledge base with the `query` method to find the most similar documents to a given text:

```python
from canopy.models.data_models import Query

kb.query(
    [\
        Query(text="Arctic Monkeys music genre"),\
        Query(\
            text="U2 music genre",\
            top_k=10,\
            metadata_filter={"key": "my-key", "match": {"value": "my-value"}},\
        ),\
    ]
)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/canopy/\#further-reading) Further Reading

- [Introduction to Canopy](https://www.pinecone.io/blog/canopy-rag-framework/)
- [Canopy library reference](https://github.com/pinecone-io/canopy/blob/main/docs/library.md)
- [Source Code](https://github.com/pinecone-io/canopy/tree/main/src/canopy/knowledge_base/qdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/canopy.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/canopy.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573661685&cv=11&fst=1748573661685&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcanopy%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Pinecone%20Canopy%20-%20Qdrant&npa=0&pscdl=noapi&auid=509970502.1748573662&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573661640&cv=11&fst=1748573661640&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~103308615&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcanopy%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Pinecone%20Canopy%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=509970502.1748573662&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c26ef5d0-be41-4041-847c-1bc817db1f1d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f39b0ed5-4e03-4d31-88d0-90b92fb61c60&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcanopy%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c26ef5d0-be41-4041-847c-1bc817db1f1d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f39b0ed5-4e03-4d31-88d0-90b92fb61c60&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcanopy%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573662694&cv=11&fst=1748573662694&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcanopy%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Pinecone%20Canopy%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=509970502.1748573662&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)