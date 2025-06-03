---
url: "https://qdrant.tech/documentation/frameworks/neo4j-graphrag/"
title: "Neo4j GraphRAG - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Neo4j GraphRAG

# [Anchor](https://qdrant.tech/documentation/frameworks/neo4j-graphrag/\#neo4j-graphrag) Neo4j GraphRAG

[Neo4j GraphRAG](https://neo4j.com/docs/neo4j-graphrag-python/current/) is a Python package to build graph retrieval augmented generation (GraphRAG) applications using Neo4j and Python. As a first-party library, it offers a robust, feature-rich, and high-performance solution, with the added assurance of long-term support and maintenance directly from Neo4j. It offers a Qdrant retriever natively to search for vectors stored in a Qdrant collection.

## [Anchor](https://qdrant.tech/documentation/frameworks/neo4j-graphrag/\#installation) Installation

```bash
pip install neo4j-graphrag[qdrant]

```

## [Anchor](https://qdrant.tech/documentation/frameworks/neo4j-graphrag/\#usage) Usage

A vector query with Neo4j and Qdrant could look like:

```python
from neo4j import GraphDatabase
from neo4j_graphrag.retrievers import QdrantNeo4jRetriever
from qdrant_client import QdrantClient
from examples.embedding_biology import EMBEDDING_BIOLOGY

NEO4J_URL = "neo4j://localhost:7687"
NEO4J_AUTH = ("neo4j", "password")

with GraphDatabase.driver(NEO4J_URL, auth=NEO4J_AUTH) as neo4j_driver:
    retriever = QdrantNeo4jRetriever(
        driver=neo4j_driver,
        client=QdrantClient(url="http://localhost:6333"),
        collection_name="{collection_name}",
        id_property_external="neo4j_id",
        id_property_neo4j="id",
    )

retriever.search(query_vector=[0.5523, 0.523, 0.132, 0.523, ...], top_k=5)

```

Alternatively, you can use any [Langchain embeddings providers](https://python.langchain.com/docs/integrations/text_embedding/), to vectorize text queries automatically.

```python
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from neo4j import GraphDatabase
from neo4j_graphrag.retrievers import QdrantNeo4jRetriever
from qdrant_client import QdrantClient

NEO4J_URL = "neo4j://localhost:7687"
NEO4J_AUTH = ("neo4j", "password")

with GraphDatabase.driver(NEO4J_URL, auth=NEO4J_AUTH) as neo4j_driver:
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    retriever = QdrantNeo4jRetriever(
        driver=neo4j_driver,
        client=QdrantClient(url="http://localhost:6333"),
        collection_name="{collection_name}",
        id_property_external="neo4j_id",
        id_property_neo4j="id",
        embedder=embedder,
    )

retriever.search(query_text="my user query", top_k=10)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/neo4j-graphrag/\#further-reading) Further Reading

- [Neo4j GraphRAG Reference](https://neo4j.com/docs/neo4j-graphrag-python/current/index.html)
- [Qdrant Retriever Reference](https://neo4j.com/docs/neo4j-graphrag-python/current/user_guide_rag.html#qdrant-neo4j-retriever-user-guide)
- [Source](https://github.com/neo4j/neo4j-graphrag-python/tree/main/src/neo4j_graphrag/retrievers/external/qdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/neo4j-graphrag.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/neo4j-graphrag.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575394567&cv=11&fst=1748575394567&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308615&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fneo4j-graphrag%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Neo4j%20GraphRAG%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=349149188.1748575395&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575394662&cv=11&fst=1748575394662&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fneo4j-graphrag%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Neo4j%20GraphRAG%20-%20Qdrant&npa=0&pscdl=noapi&auid=349149188.1748575395&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)

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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e6e69d1e-fafa-4719-9ffd-22b243276623&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0f282787-4ecc-4fec-8139-a2c38ba8bd1a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fneo4j-graphrag%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=e6e69d1e-fafa-4719-9ffd-22b243276623&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=0f282787-4ecc-4fec-8139-a2c38ba8bd1a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fneo4j-graphrag%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575395397&cv=11&fst=1748575395397&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2h1v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fneo4j-graphrag%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Neo4j%20GraphRAG%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=349149188.1748575395&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)