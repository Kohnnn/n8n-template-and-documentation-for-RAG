---
url: "https://qdrant.tech/documentation/data-management/confluent/"
title: "Confluent Kafka - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Data management](https://qdrant.tech/documentation/data-management/)
- Confluent Kafka

![Confluent Logo](https://qdrant.tech/documentation/frameworks/confluent/confluent-logo.png)

Built by the original creators of Apache Kafka®, [Confluent Cloud](https://www.confluent.io/confluent-cloud/?utm_campaign=tm.pmm_cd.cwc_partner_Qdrant_generic&utm_source=Qdrant&utm_medium=partnerref) is a cloud-native and complete data streaming platform available on AWS, Azure, and Google Cloud. The platform includes a fully managed, elastically scaling Kafka engine, 120+ connectors, serverless Apache Flink®, enterprise-grade security controls, and a robust governance suite.

With our [Qdrant-Kafka Sink Connector](https://github.com/qdrant/qdrant-kafka), Qdrant is part of the [Connect with Confluent](https://www.confluent.io/partners/connect/) technology partner program. It brings fully managed data streams directly to organizations from Confluent Cloud, making it easier for organizations to stream any data to Qdrant with a fully managed Apache Kafka service.

## [Anchor](https://qdrant.tech/documentation/data-management/confluent/\#usage) Usage

### [Anchor](https://qdrant.tech/documentation/data-management/confluent/\#pre-requisites) Pre-requisites

- A Confluent Cloud account. You can begin with a [free trial](https://www.confluent.io/confluent-cloud/tryfree/?utm_campaign=tm.pmm_cd.cwc_partner_qdrant_tryfree&utm_source=qdrant&utm_medium=partnerref) with credits for the first 30 days.
- Qdrant instance to connect to. You can get a free cloud instance at [cloud.qdrant.io](https://cloud.qdrant.io/?ajs_anonymous_id=cd78b68c-29d0-4383-a09c-c71bcb7c1e04).

### [Anchor](https://qdrant.tech/documentation/data-management/confluent/\#installation) Installation

1. Download the latest connector zip file from [Confluent Hub](https://www.confluent.io/hub/qdrant/qdrant-kafka).

2. Configure an environment and cluster on Confluent and create a topic to produce messages for.

3. Navigate to the `Connectors` section of the Confluent cluster and click `Add Plugin`. Upload the zip file with the following info.


![Qdrant Connector Install](https://qdrant.tech/documentation/frameworks/confluent/install.png)

4. Once installed, navigate to the connector and set the following configuration values.

![Qdrant Connector Config](https://qdrant.tech/documentation/frameworks/confluent/config.png)

Replace the placeholder values with your credentials.

5. Add the Qdrant instance host to the allowed networking endpoints.

![Qdrant Connector Endpoint](https://qdrant.tech/documentation/frameworks/confluent/endpoint.png)

7. Start the connector.

## [Anchor](https://qdrant.tech/documentation/data-management/confluent/\#producing-messages) Producing Messages

You can now produce messages for the configured topic, and they’ll be written into the configured Qdrant instance.

![Qdrant Connector Message](https://qdrant.tech/documentation/frameworks/confluent/message.png)

## [Anchor](https://qdrant.tech/documentation/data-management/confluent/\#message-formats) Message Formats

The connector supports messages in the following formats.

_Click each to expand._

**Unnamed/Default vector**

Reference: [Creating a collection with a default vector](https://qdrant.tech/documentation/concepts/collections/#create-a-collection).

```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vector": [\
        0.1,\
        0.2,\
        0.3,\
        0.4,\
        0.5,\
        0.6,\
        0.7,\
        0.8\
    ],
    "payload": {
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
        "url": "https://kafka.apache.org/"
    }
}

```

**Named multiple vectors**

Reference: [Creating a collection with multiple vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-multiple-vectors).

```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vector": {
        "some-dense": [\
            0.1,\
            0.2,\
            0.3,\
            0.4,\
            0.5,\
            0.6,\
            0.7,\
            0.8\
        ],
        "some-other-dense": [\
            0.1,\
            0.2,\
            0.3,\
            0.4,\
            0.5,\
            0.6,\
            0.7,\
            0.8\
        ]
    },
    "payload": {
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
        "url": "https://kafka.apache.org/"
    }
}

```

**Sparse vectors**

Reference: [Creating a collection with sparse vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-sparse-vectors).

```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vector": {
        "some-sparse": {
            "indices": [\
                0,\
                1,\
                2,\
                3,\
                4,\
                5,\
                6,\
                7,\
                8,\
                9\
            ],
            "values": [\
                0.1,\
                0.2,\
                0.3,\
                0.4,\
                0.5,\
                0.6,\
                0.7,\
                0.8,\
                0.9,\
                1.0\
            ]
        }
    },
    "payload": {
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
        "url": "https://kafka.apache.org/"
    }
}

```

**Multi-vectors**

Reference:

- [Multi-vectors](https://qdrant.tech/documentation/concepts/vectors/#multivectors)

```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vector": {
        "some-multi": [\
            [\
                0.1,\
                0.2,\
                0.3,\
                0.4,\
                0.5,\
                0.6,\
                0.7,\
                0.8,\
                0.9,\
                1.0\
            ],\
            [\
                1.0,\
                0.9,\
                0.8,\
                0.5,\
                0.4,\
                0.8,\
                0.6,\
                0.4,\
                0.2,\
                0.1\
            ]\
        ]
    },
    "payload": {
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
        "url": "https://kafka.apache.org/"
    }
}

```

**Combination of named dense and sparse vectors**

Reference:

- [Creating a collection with multiple vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-multiple-vectors).

- [Creating a collection with sparse vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-sparse-vectors).


```json
{
    "collection_name": "{collection_name}",
    "id": "a10435b5-2a58-427a-a3a0-a5d845b147b7",
    "vector": {
        "some-other-dense": [\
            0.1,\
            0.2,\
            0.3,\
            0.4,\
            0.5,\
            0.6,\
            0.7,\
            0.8\
        ],
        "some-sparse": {
            "indices": [\
                0,\
                1,\
                2,\
                3,\
                4,\
                5,\
                6,\
                7,\
                8,\
                9\
            ],
            "values": [\
                0.1,\
                0.2,\
                0.3,\
                0.4,\
                0.5,\
                0.6,\
                0.7,\
                0.8,\
                0.9,\
                1.0\
            ]
        }
    },
    "payload": {
        "name": "kafka",
        "description": "Kafka is a distributed streaming platform",
        "url": "https://kafka.apache.org/"
    }
}

```

## [Anchor](https://qdrant.tech/documentation/data-management/confluent/\#further-reading) Further Reading

- [Kafka Connect Docs](https://docs.confluent.io/platform/current/connect/index.html)
- [Confluent Connectors Docs](https://docs.confluent.io/cloud/current/connectors/bring-your-connector/custom-connector-qs.html)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/confluent.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/confluent.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=a7a8766e-1e7e-4fff-b751-4037be8f22f2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6e9c5791-0dfc-4bc6-8796-2bc501f60e04&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fconfluent%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575137285&cv=11&fst=1748575137285&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fconfluent%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Confluent%20Kafka%20-%20Qdrant&npa=0&pscdl=noapi&auid=27268362.1748575137&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575137268&cv=11&fst=1748575137268&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fconfluent%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Confluent%20Kafka%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=27268362.1748575137&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748575137355&cv=11&fst=1748575137355&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fconfluent%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Confluent%20Kafka%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=27268362.1748575137&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=a7a8766e-1e7e-4fff-b751-4037be8f22f2&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=6e9c5791-0dfc-4bc6-8796-2bc501f60e04&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fconfluent%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)