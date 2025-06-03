---
url: "https://qdrant.tech/documentation/frameworks/sycamore/"
title: "Sycamore - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Frameworks](https://qdrant.tech/documentation/frameworks/)
- Sycamore

## [Anchor](https://qdrant.tech/documentation/frameworks/sycamore/\#sycamore) Sycamore

[Sycamore](https://sycamore.readthedocs.io/en/stable/) is an LLM-powered data preparation, processing, and analytics system for complex, unstructured documents like PDFs, HTML, presentations, and more. With Aryn, you can prepare data for GenAI and RAG applications, power high-quality document processing workflows, and run analytics on large document collections with natural language.

You can use the Qdrant connector to write into and read documents from Qdrant collections.

## [Anchor](https://qdrant.tech/documentation/frameworks/sycamore/\#writing-to-qdrant) Writing to Qdrant

To write a Docset to a Qdrant collection in Sycamore, use the `docset.write.qdrant(....)` function. The Qdrant writer accepts the following arguments:

- `client_params`: Parameters that are passed to the Qdrant client constructor. See more information in the [Client API Reference](https://python-client.qdrant.tech/qdrant_client.qdrant_client).
- `collection_params`: Parameters that are passed into the `qdrant_client.QdrantClient.create_collection` method. See more information in the [Client API Reference](https://python-client.qdrant.tech/_modules/qdrant_client/qdrant_client#QdrantClient.create_collection).
- `vector_name`: The name of the vector in the Qdrant collection. Defaults to `None`.
- `execute`: Execute the pipeline and write to Qdrant on adding this operator. If `False`, will return a `DocSet` with this write in the plan. Defaults to `True`.
- `kwargs`: Keyword arguments to pass to the underlying execution engine.

```python
ds.write.qdrant(
    {
        "url": "http://localhost:6333",
        "timeout": 50,
    },
    {
        "collection_name": "{collection_name}",
        "vectors_config": {
            "size": 384,
            "distance": "Cosine",
        },
    },
)

```

## [Anchor](https://qdrant.tech/documentation/frameworks/sycamore/\#reading-from-qdrant) Reading from Qdrant

To read a Docset from a Qdrant collection in Sycamore, use the `docset.read.qdrant(....)` function. The Qdrant reader accepts the following arguments:

- `client_params`: Parameters that are passed to the Qdrant client constructor. See more information in the [Client API Reference](https://python-client.qdrant.tech/qdrant_client.qdrant_client).
- `query_params`: Parameters that are passed into the `qdrant_client.QdrantClient.query_points` method. See more information in the [Client API Reference](https://python-client.qdrant.tech/_modules/qdrant_client/qdrant_client#QdrantClient.query_points).
- `kwargs`: Keyword arguments to pass to the underlying execution engine.

```python
docs = ctx.read.qdrant(
    {
        "url": "https://xyz-example.eu-central.aws.cloud.qdrant.io:6333",
        "api_key": "<paste-your-api-key-here>",
    },
    {"collection_name": "{collection_name}", "limit": 100, "using": "{optional_vector_name}"},
).take_all()

```

## [Anchor](https://qdrant.tech/documentation/frameworks/sycamore/\#-further-reading) 📚 Further Reading

- [Sycamore Reference](https://sycamore.readthedocs.io/en/stable/)
- [Sycamore](https://github.com/aryn-ai/sycamore/tree/main/examples)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/sycamore.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/frameworks/sycamore.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=6ebba06c-1951-4cfd-ae52-efc855e824fb&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=59dcb37f-ff8a-42bc-a835-50057ced139c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsycamore%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574593763&cv=11&fst=1748574593763&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsycamore%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Sycamore%20-%20Qdrant&npa=0&pscdl=noapi&auid=995708534.1748574593&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574593753&cv=11&fst=1748574593753&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55t0h2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsycamore%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Sycamore%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=995708534.1748574593&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574593811&cv=11&fst=1748574593811&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55t0h2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102510904~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsycamore%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Sycamore%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=995708534.1748574593&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=6ebba06c-1951-4cfd-ae52-efc855e824fb&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=59dcb37f-ff8a-42bc-a835-50057ced139c&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fframeworks%2Fsycamore%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)