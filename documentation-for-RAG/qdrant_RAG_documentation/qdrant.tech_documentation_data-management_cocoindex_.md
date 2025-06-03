---
url: "https://qdrant.tech/documentation/data-management/cocoindex/"
title: "CocoIndex - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Data management](https://qdrant.tech/documentation/data-management/)
- CocoIndex

# [Anchor](https://qdrant.tech/documentation/data-management/cocoindex/\#cocoindex) CocoIndex

[CocoIndex](https://cocoindex.com/) is a high performance ETL framework to transform data for AI, with real-time incremental processing.

Qdrant is available as a native built-in vector database to store and retrieve embeddings.

Install CocoIndex:

```bash
pip install -U cocoindex

```

Install Postgres with [Docker Compose](https://docs.docker.com/compose/install/):

```bash
docker compose -f <(curl -L https://raw.githubusercontent.com/cocoindex-io/cocoindex/refs/heads/main/dev/postgres.yaml) up -d

```

CocoIndex is a stateful ETL framework and only processes data that has changed. It uses Postgres as a metadata store to track the state of the data.

```python
import cocoindex

doc_embeddings.export(
    "doc_embeddings",
    cocoindex.storages.Qdrant(
        collection_name="cocoindex",
        grpc_url="https://xyz-example.cloud-region.cloud-provider.cloud.qdrant.io:6334/",
        api_key="<your-api-key-here>",
    ),
    primary_key_fields=["id_field"],
    setup_by_user=True,
)

```

The spec takes the following fields:

- `collection_name` (type: str, required): The name of the collection to export the data to.
- `grpc_url` (type: str, optional): The gRPC URL of the Qdrant instance. Defaults to http://localhost:6334/.
- `api_key` (type: str, optional). API key to authenticate requests with.

Before exporting, you must create a collection with a vector name that matches the vector field name in CocoIndex, and set `setup_by_user=True` during export.

## [Anchor](https://qdrant.tech/documentation/data-management/cocoindex/\#further-reading) Further Reading

- [CocoIndex Documentation](https://cocoindex.io/docs/ops/storages#qdrant)
- [Example Code to build text embeddings with Qdrant](https://github.com/cocoindex-io/cocoindex/tree/main/examples/text_embedding_qdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/cocoindex.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/cocoindex.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573692289&cv=11&fst=1748573692289&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fcocoindex%2F&hn=www.googleadservices.com&frm=0&tiba=CocoIndex%20-%20Qdrant&npa=0&pscdl=noapi&auid=1054113207.1748573692&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573692264&cv=11&fst=1748573692264&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fcocoindex%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=CocoIndex%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1054113207.1748573692&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0f35c494-b04b-487d-9f42-ce2f50fd34b0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c1b878cb-f4f7-4907-92f1-00b27545599e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fcocoindex%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0f35c494-b04b-487d-9f42-ce2f50fd34b0&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=c1b878cb-f4f7-4907-92f1-00b27545599e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fcocoindex%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573693368&cv=11&fst=1748573693368&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fcocoindex%2F&hn=www.googleadservices.com&frm=0&tiba=CocoIndex%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1054113207.1748573692&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)