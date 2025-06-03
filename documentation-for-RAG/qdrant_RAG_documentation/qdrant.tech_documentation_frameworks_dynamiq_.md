---
url: "https://qdrant.tech/documentation/frameworks/dynamiq/"
title: "Dynamiq - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Dynamiq

# [Anchor](https://qdrant.tech/documentation/frameworks/dynamiq/\#dynamiq) Dynamiq

Dynamiq is your all-in-one Gen AI framework, designed to streamline the development of AI-powered applications. Dynamiq specializes in orchestrating retrieval-augmented generation (RAG) and large language model (LLM) agents.

Qdrant is a vector database available in Dynamiq, capable of serving multiple roles. It can be used for writing and retrieving documents, acting as memory for agent interactions, and functioning as a retrieval tool that agents can call when needed.

## [Anchor](https://qdrant.tech/documentation/frameworks/dynamiq/\#installing) Installing

First, ensure you have the `dynamiq` library installed:

```bash
$ pip install dynamiq

```

## [Anchor](https://qdrant.tech/documentation/frameworks/dynamiq/\#retriever-node) Retriever node

The QdrantDocumentRetriever node enables efficient retrieval of relevant documents based on vector similarity search.

```python
from dynamiq.nodes.retrievers import QdrantDocumentRetriever
from dynamiq import Workflow

# Define a retriever node to fetch most relevant documents
retriever_node = QdrantDocumentRetriever(
    index_name="default",
    top_k=5,  # Optional: Maximum number of documents to retrieve
    filters={...}  # Optional: Additional filtering conditions
)

# Create a workflow and add the retriever node
wf = Workflow()
wf.flow.add_nodes(retriever_node)

# Execute retrieval
result = wf.run(input_data={
  'embedding': query_embedding  # Provide an embedded query for similarity search
})

```

## [Anchor](https://qdrant.tech/documentation/frameworks/dynamiq/\#writer-node) Writer node

The QdrantDocumentWriter node allows storing documents in the Qdrant vector database.

```python
from dynamiq.nodes.writers import QdrantDocumentWriter

# Define a writer node to store documents in Qdrant
writer_node = QdrantDocumentWriter(
    index_name="default",
    create_if_not_exist=True
)

# Create a workflow and add the writer node
wf = Workflow()
wf.flow.add_nodes(writer_node)

# Execute writing
result = wf.run(input_data={
  'documents': embedded_documents  # Provide embedded documents for storage
})

```

# [Anchor](https://qdrant.tech/documentation/frameworks/dynamiq/\#additional-tutorials) Additional Tutorials

Discover additional examples and use cases of Qdrant with Dynamiq:

- [Using Qdrant with Dynamiq – A Hands-on Tutorial](https://colab.research.google.com/drive/1rlZJW4lOM36b7ZxK-dVJv5dE2xrgwxU_?usp=sharing)
- [End-to-End Application with Qdrant and Dynamiq](https://colab.research.google.com/drive/1RaR25BCj_D5wzQ70ejUQyKzdCM6DUXMF?usp=sharing)

## [Anchor](https://qdrant.tech/documentation/frameworks/dynamiq/\#for-more-details-please-refer-to) For more details, please refer to:

- [Dynamiq Documentation](https://docs.getdynamiq.ai/)
- [Dynamiq GitHub](https://github.com/dynamiq-ai/dynamiq)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/dynamiq.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/dynamiq.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575095781&cv=11&fst=1748575095781&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdynamiq%2F&hn=www.googleadservices.com&frm=0&tiba=Dynamiq%20-%20Qdrant&npa=0&pscdl=noapi&auid=1204470726.1748575096&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575095734&cv=11&fst=1748575095734&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdynamiq%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Dynamiq%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1204470726.1748575096&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=eb393403-ee61-4b30-8343-b1e6d15a2b24&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=446ab5cc-8400-450a-9948-6dfb9a8ad29f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdynamiq%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=eb393403-ee61-4b30-8343-b1e6d15a2b24&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=446ab5cc-8400-450a-9948-6dfb9a8ad29f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdynamiq%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575097075&cv=11&fst=1748575097075&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fdynamiq%2F&hn=www.googleadservices.com&frm=0&tiba=Dynamiq%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1204470726.1748575096&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)