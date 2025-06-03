---
url: "https://qdrant.tech/documentation/embeddings/cohere/"
title: "Cohere - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Embeddings](https://qdrant.tech/documentation/embeddings/)
- Cohere

# [Anchor](https://qdrant.tech/documentation/embeddings/cohere/\#cohere) Cohere

Qdrant is compatible with Cohere [co.embed API](https://docs.cohere.ai/reference/embed) and its official Python SDK that
might be installed as any other package:

```bash
pip install cohere

```

The embeddings returned by co.embed API might be used directly in the Qdrant client’s calls:

```python
import cohere
import qdrant_client
from qdrant_client.models import Batch

cohere_client = cohere.Client("<< your_api_key >>")
qdrant_client = qdrant_client.QdrantClient()
qdrant_client.upsert(
    collection_name="MyCollection",
    points=Batch(
        ids=[1],
        vectors=cohere_client.embed(
            model="large",
            texts=["The best vector database"],
        ).embeddings,
    ),
)

```

If you are interested in seeing an end-to-end project created with co.embed API and Qdrant, please check out the
“ [Question Answering as a Service with Cohere and Qdrant](https://qdrant.tech/articles/qa-with-cohere-and-qdrant/)” article.

## [Anchor](https://qdrant.tech/documentation/embeddings/cohere/\#embed-v3) Embed v3

Embed v3 is a new family of Cohere models, released in November 2023. The new models require passing an additional
parameter to the API call: `input_type`. It determines the type of task you want to use the embeddings for.

- `input_type="search_document"` \- for documents to store in Qdrant
- `input_type="search_query"` \- for search queries to find the most relevant documents
- `input_type="classification"` \- for classification tasks
- `input_type="clustering"` \- for text clustering

While implementing semantic search applications, such as RAG, you should use `input_type="search_document"` for the
indexed documents and `input_type="search_query"` for the search queries. The following example shows how to index
documents with the Embed v3 model:

```python
import cohere
import qdrant_client
from qdrant_client.models import Batch

cohere_client = cohere.Client("<< your_api_key >>")
client = qdrant_client.QdrantClient()
client.upsert(
    collection_name="MyCollection",
    points=Batch(
        ids=[1],
        vectors=cohere_client.embed(
            model="embed-english-v3.0",  # New Embed v3 model
            input_type="search_document",  # Input type for documents
            texts=["Qdrant is the a vector database written in Rust"],
        ).embeddings,
    ),
)

```

Once the documents are indexed, you can search for the most relevant documents using the Embed v3 model:

```python
client.query_points(
    collection_name="MyCollection",
    query=cohere_client.embed(
        model="embed-english-v3.0",  # New Embed v3 model
        input_type="search_query",  # Input type for search queries
        texts=["The best vector database"],
    ).embeddings[0],
)

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/cohere.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/embeddings/cohere.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573813010&cv=11&fst=1748573813010&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fcohere%2F&hn=www.googleadservices.com&frm=0&tiba=Cohere%20-%20Qdrant&npa=0&pscdl=noapi&auid=884380810.1748573813&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573812986&cv=11&fst=1748573812986&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fcohere%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Cohere%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=884380810.1748573813&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4f051239-cfd5-46f9-9888-7c32abea0d11&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=889c4d01-a351-4ac2-aac5-1c1ea6275125&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fcohere%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=4f051239-cfd5-46f9-9888-7c32abea0d11&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=889c4d01-a351-4ac2-aac5-1c1ea6275125&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fcohere%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573814084&cv=11&fst=1748573814084&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fembeddings%2Fcohere%2F&hn=www.googleadservices.com&frm=0&tiba=Cohere%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=884380810.1748573813&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)