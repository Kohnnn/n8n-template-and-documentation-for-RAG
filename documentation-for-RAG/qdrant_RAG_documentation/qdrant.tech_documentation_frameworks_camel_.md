---
url: "https://qdrant.tech/documentation/frameworks/camel/"
title: "CamelAI - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- CamelAI

# [Anchor](https://qdrant.tech/documentation/frameworks/camel/\#camel) Camel

[Camel](https://www.camel-ai.org/) is a Python framework to build and use LLM-based agents for real-world task solving.

Qdrant is available as a storage mechanism in Camel for ingesting and retrieving semantically similar data.

## [Anchor](https://qdrant.tech/documentation/frameworks/camel/\#usage-with-qdrant) Usage With Qdrant

- Install Camel with the `vector-databases` extra.

```bash
pip install "camel[vector-databases]"

```

- Configure the `QdrantStorage` class.

```python
from camel.storages import QdrantStorage, VectorDBQuery, VectorRecord
from camel.types import VectorDistance

qdrant_storage = QdrantStorage(
    url_and_api_key=(
        "https://xyz-example.eu-central.aws.cloud.qdrant.io:6333",
        "<provide-your-own-key>",
    ),
    collection_name="{collection_name}",
    distance=VectorDistance.COSINE,
    vector_dim=384,
)

```

The `QdrantStorage` class implements methods to read and write to a Qdrant instance. An instance of this class can now be passed to retrievers for interfacing with your Qdrant collections.

```python
qdrant_storage.add([VectorRecord(\
            vector=[-0.1, 0.1, ...],\
            payload={'key1': 'value1'},\
        ),\
        VectorRecord(\
            vector=[-0.1, 0.1, ...],\
            payload={'key2': 'value2'},\
        ),])

query_results = qdrant_storage.query(VectorDBQuery(query_vector=[0.1, 0.2, ...], top_k=10))
for result in query_results:
    print(result.record.payload, result.similarity)

qdrant_storage.clear()

```

- Use the `QdrantStorage` in Camel’s Vector Retriever.

```python
from camel.embeddings import OpenAIEmbedding
from camel.retrievers import VectorRetriever

# Initialize the VectorRetriever with an embedding model
vr = VectorRetriever(embedding_model=OpenAIEmbedding())

content_input_path = "<URL-TO-SOME-RESOURCE>"

vr.process(content_input_path, qdrant_storage)

# Execute the query and retrieve results
results = vr.query("<SOME_USER_QUERY>", vector_storage)

```

- Camel also provides an Auto Retriever implementation that handles both embedding and storing data and executing queries.

```python
from camel.retrievers import AutoRetriever
from camel.types import StorageType

ar = AutoRetriever(
    url_and_api_key=(
        "https://xyz-example.eu-central.aws.cloud.qdrant.io:6333",
        "<provide-your-own-key>",
    ),
    storage_type=StorageType.QDRANT,
)

retrieved_info = ar.run_vector_retriever(
    contents=["<URL-TO-SOME-RESOURCE>"],
    query=""<SOME_USER_QUERY>"",
    return_detailed_info=True,
)

print(retrieved_info)

```

You can refer to the Camel [documentation](https://docs.camel-ai.org/) for more information about the retrieval mechansims.

## [Anchor](https://qdrant.tech/documentation/frameworks/camel/\#end-to-end-examples) End-To-End Examples

- [Camel RAG Cookbook](https://docs.camel-ai.org/cookbooks/agents_with_rag.html)
- [Customer Service Discord Bot with Agentic RAG](https://docs.camel-ai.org/cookbooks/customer_service_Discord_bot_with_agentic_RAG.html)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/camel.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/camel.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574542330&cv=11&fst=1748574542330&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcamel%2F&hn=www.googleadservices.com&frm=0&tiba=CamelAI%20-%20Qdrant&npa=0&pscdl=noapi&auid=2065559082.1748574542&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574542298&cv=11&fst=1748574542298&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247~103308614&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcamel%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=CamelAI%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2065559082.1748574542&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c93f0cb1-e969-4328-9297-2722a20dba17&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6ccaf909-18cc-4700-acb2-4a0913856546&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcamel%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=c93f0cb1-e969-4328-9297-2722a20dba17&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6ccaf909-18cc-4700-acb2-4a0913856546&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcamel%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574543477&cv=11&fst=1748574543477&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104573694&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fcamel%2F&hn=www.googleadservices.com&frm=0&tiba=CamelAI%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2065559082.1748574542&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)