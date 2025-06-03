---
url: "https://qdrant.tech/documentation/data-management/airflow/"
title: "Apache Airflow - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Data management](https://qdrant.tech/documentation/data-management/)
- Apache Airflow

# [Anchor](https://qdrant.tech/documentation/data-management/airflow/\#apache-airflow) Apache Airflow

[Apache Airflow](https://airflow.apache.org/) is an open-source platform for authoring, scheduling and monitoring data and computing workflows. Airflow uses Python to create workflows that can be easily scheduled and monitored.

Qdrant is available as a [provider](https://airflow.apache.org/docs/apache-airflow-providers-qdrant/stable/index.html) in Airflow to interface with the database.

## [Anchor](https://qdrant.tech/documentation/data-management/airflow/\#prerequisites) Prerequisites

Before configuring Airflow, you need:

1. A Qdrant instance to connect to. You can set one up in our [installation guide](https://qdrant.tech/documentation/guides/installation/).

2. A running Airflow instance. You can use their [Quick Start Guide](https://airflow.apache.org/docs/apache-airflow/stable/start.html).


## [Anchor](https://qdrant.tech/documentation/data-management/airflow/\#installation) Installation

You can install the Qdrant provider by running `pip install apache-airflow-providers-qdrant` in your Airflow shell.

**NOTE**: You’ll have to restart your Airflow session for the provider to be available.

## [Anchor](https://qdrant.tech/documentation/data-management/airflow/\#setting-up-a-connection) Setting up a connection

Open the `Admin-> Connections` section of the Airflow UI. Click the `Create` link to create a new [Qdrant connection](https://airflow.apache.org/docs/apache-airflow-providers-qdrant/stable/connections.html).

![Qdrant connection](https://qdrant.tech/documentation/frameworks/airflow/connection.png)

You can also set up a connection using [environment variables](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#environment-variables-connections) or an [external secret backend](https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/secrets-backend/index.html).

## [Anchor](https://qdrant.tech/documentation/data-management/airflow/\#qdrant-hook) Qdrant hook

An Airflow hook is an abstraction of a specific API that allows Airflow to interact with an external system.

```python
from airflow.providers.qdrant.hooks.qdrant import QdrantHook

hook = QdrantHook(conn_id="qdrant_connection")

hook.verify_connection()

```

A [`qdrant_client#QdrantClient`](https://pypi.org/project/qdrant-client/) instance is available via `@property conn` of the `QdrantHook` instance for use within your Airflow workflows.

```python
from qdrant_client import models

hook.conn.count("<COLLECTION_NAME>")

hook.conn.upsert(
    "<COLLECTION_NAME>",
    points=[\
        models.PointStruct(id=32, vector=[0.32, 0.12, 0.123], payload={"color": "red"})\
    ],
)

```

## [Anchor](https://qdrant.tech/documentation/data-management/airflow/\#qdrant-ingest-operator) Qdrant Ingest Operator

The Qdrant provider also provides a convenience operator for uploading data to a Qdrant collection that internally uses the Qdrant hook.

```python
from airflow.providers.qdrant.operators.qdrant import QdrantIngestOperator

vectors = [\
    [0.11, 0.22, 0.33, 0.44],\
    [0.55, 0.66, 0.77, 0.88],\
    [0.88, 0.11, 0.12, 0.13],\
]
ids = [32, 21, "b626f6a9-b14d-4af9-b7c3-43d8deb719a6"]
payload = [{"meta": "data"}, {"meta": "data_2"}, {"meta": "data_3", "extra": "data"}]

QdrantIngestOperator(
    conn_id="qdrant_connection",
    task_id="qdrant_ingest",
    collection_name="<COLLECTION_NAME>",
    vectors=vectors,
    ids=ids,
    payload=payload,
)

```

## [Anchor](https://qdrant.tech/documentation/data-management/airflow/\#reference) Reference

- 📦 [Provider package PyPI](https://pypi.org/project/apache-airflow-providers-qdrant/)
- 📚 [Provider docs](https://airflow.apache.org/docs/apache-airflow-providers-qdrant/stable/index.html)
- 📄 [Source Code](https://github.com/apache/airflow/tree/main/providers/qdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/airflow.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/airflow.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573956709&cv=11&fst=1748573956709&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairflow%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Apache%20Airflow%20-%20Qdrant&npa=0&pscdl=noapi&auid=539826182.1748573957&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573956665&cv=11&fst=1748573956665&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairflow%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Apache%20Airflow%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=539826182.1748573957&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=f6cb47f4-eefd-4127-948a-0aca851b890d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f20899c0-6a92-4fd2-8cb6-e310351e7fc1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairflow%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=f6cb47f4-eefd-4127-948a-0aca851b890d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f20899c0-6a92-4fd2-8cb6-e310351e7fc1&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairflow%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573958357&cv=11&fst=1748573958357&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fairflow%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Apache%20Airflow%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=539826182.1748573957&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)