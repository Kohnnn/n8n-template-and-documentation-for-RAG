---
url: "https://qdrant.tech/documentation/data-management/fluvio/"
title: "InfinyOn Fluvio - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Data management](https://qdrant.tech/documentation/data-management/)
- InfinyOn Fluvio

![Fluvio Logo](https://qdrant.tech/documentation/data-management/fluvio/fluvio-logo.png)

[InfinyOn Fluvio](https://www.fluvio.io/) is an open-source platform written in Rust for high speed, real-time data processing. It is cloud native, designed to work with any infrastructure type, from bare metal hardware to containerized platforms.

## [Anchor](https://qdrant.tech/documentation/data-management/fluvio/\#usage-with-qdrant) Usage with Qdrant

With the [Qdrant Fluvio Connector](https://github.com/qdrant/qdrant-fluvio), you can stream records from Fluvio topics to Qdrant collections, leveraging Fluvio’s delivery guarantees and high-throughput.

### [Anchor](https://qdrant.tech/documentation/data-management/fluvio/\#pre-requisites) Pre-requisites

- A Fluvio installation. You can refer to the [Fluvio Quickstart](https://www.fluvio.io/docs/fluvio/quickstart/) for instructions.
- Qdrant server to connect to. You can set up a [local instance](https://qdrant.tech/documentation/quickstart/) or a free cloud instance at [cloud.qdrant.io](https://cloud.qdrant.io/?ajs_anonymous_id=5e43a7df-8f3b-4d00-aa10-a686df855409).

### [Anchor](https://qdrant.tech/documentation/data-management/fluvio/\#downloading-the-connector) Downloading the connector

Run the following commands after [setting up Fluvio](https://www.fluvio.io/docs/fluvio/quickstart).

```console
cdk hub download qdrant/qdrant-sink@0.1.0

```

### [Anchor](https://qdrant.tech/documentation/data-management/fluvio/\#example-config) Example Config

> _config.yaml_

```yaml
apiVersion: 0.1.0
meta:
  version: 0.1.0
  name: my-qdrant-connector
  type: qdrant-sink
  topic: topic-name
  secrets:
    - name: QDRANT_API_KEY

qdrant:
  url: https://xyz-example.eu-central.aws.cloud.qdrant.io:6334
  api_key: "${{ secrets.QDRANT_API_KEY }}"

```

> _secrets.txt_

```text
QDRANT_API_KEY=<SOME_API_KEY>

```

### [Anchor](https://qdrant.tech/documentation/data-management/fluvio/\#running) Running

```console
cdk deploy start --ipkg qdrant-qdrant-sink-0.1.0.ipkg -c config.yaml --secrets secrets.txt

```

### [Anchor](https://qdrant.tech/documentation/data-management/fluvio/\#produce-messages) Produce Messages

You can now run the following to generate messages to be written into Qdrant.

```console
fluvio produce topic-name

```

### [Anchor](https://qdrant.tech/documentation/data-management/fluvio/\#message-formats) Message Formats

This sink connector supports messages with dense/sparse/multi vectors.

_Click each to expand._

**Unnamed/Default vector**

Reference: [Creating a collection with a default vector](https://qdrant.tech/documentation/concepts/collections/#create-a-collection).

```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vectors": [\
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
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "https://www.fluvio.io/"
    }
}

```

**Named multiple vectors**

Reference: [Creating a collection with multiple vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-multiple-vectors).

```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vectors": {
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
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "https://www.fluvio.io/"
    }
}

```

**Sparse vectors**

Reference: [Creating a collection with sparse vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-sparse-vectors).

```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vectors": {
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
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "https://www.fluvio.io/"
    }
}

```

**Multi-vector**

```json
{
    "collection_name": "{collection_name}",
    "id": 1,
    "vectors": {
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
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "https://www.fluvio.io/"
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
    "vectors": {
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
        "name": "fluvio",
        "description": "Solution for distributed stream processing",
        "url": "https://www.fluvio.io/"
    }
}

```

### [Anchor](https://qdrant.tech/documentation/data-management/fluvio/\#further-reading) Further Reading

- [Fluvio Quickstart](https://www.fluvio.io/docs/fluvio/quickstart)
- [Fluvio Tutorials](https://www.fluvio.io/docs/fluvio/tutorials/)
- [Connector Source](https://github.com/qdrant/qdrant-fluvio)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/fluvio.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/fluvio.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574044256&cv=11&fst=1748574044256&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Ffluvio%2F&hn=www.googleadservices.com&frm=0&tiba=InfinyOn%20Fluvio%20-%20Qdrant&npa=0&pscdl=noapi&auid=1479410114.1748574044&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574044227&cv=11&fst=1748574044227&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Ffluvio%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=InfinyOn%20Fluvio%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1479410114.1748574044&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=72391837-62c4-47cd-952b-19e9072397f7&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9597688e-0434-4e5b-9d4f-6bcfa7aace9d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Ffluvio%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=72391837-62c4-47cd-952b-19e9072397f7&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9597688e-0434-4e5b-9d4f-6bcfa7aace9d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Ffluvio%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574045373&cv=11&fst=1748574045373&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Ffluvio%2F&hn=www.googleadservices.com&frm=0&tiba=InfinyOn%20Fluvio%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1479410114.1748574044&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)