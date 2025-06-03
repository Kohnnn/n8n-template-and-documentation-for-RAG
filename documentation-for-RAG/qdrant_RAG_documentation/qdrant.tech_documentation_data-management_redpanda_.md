---
url: "https://qdrant.tech/documentation/data-management/redpanda/"
title: "Redpanda Connect - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Data management](https://qdrant.tech/documentation/data-management/)
- Redpanda Connect

![Redpanda Cover](https://qdrant.tech/documentation/data-management/redpanda/redpanda-cover.png)

[Redpanda Connect](https://www.redpanda.com/connect) is a declarative data-agnostic streaming service designed for efficient, stateless processing steps. It offers transaction-based resiliency with back pressure, ensuring at-least-once delivery when connecting to at-least-once sources with sinks, without the need to persist messages during transit.

Connect pipelines are configured using a YAML file, which organizes components hierarchically. Each section represents a different component type, such as inputs, processors and outputs, and these can have nested child components and [dynamic values](https://docs.redpanda.com/redpanda-connect/configuration/interpolation/).

The [Qdrant Output](https://docs.redpanda.com/redpanda-connect/components/outputs/qdrant/) component enables streaming vector data into Qdrant collections in your RedPanda pipelines.

## [Anchor](https://qdrant.tech/documentation/data-management/redpanda/\#example) Example

An example configuration of the output once the inputs and processors are set, would look like:

```yaml
input:
    # https://docs.redpanda.com/redpanda-connect/components/inputs/about/

pipeline:
  processors:
    # https://docs.redpanda.com/redpanda-connect/components/processors/about/

output:
  label: "qdrant-output"
  qdrant:
    max_in_flight: 64
    batching:
      count: 8
    grpc_host: xyz-example.eu-central.aws.cloud.qdrant.io:6334
    api_token: "<provide-your-own-key>"
    tls:
      enabled: true
    #   skip_cert_verify: false
    #   enable_renegotiation: false
    #   root_cas: ""
    #   root_cas_file: ""
    #   client_certs: []
    collection_name: "<collection_name>"
    id: root = uuid_v4()
    vector_mapping: 'root = {"some_dense": this.vector, "some_sparse": {"indices": [23,325,532],"values": [0.352,0.532,0.532]}}'
    payload_mapping: 'root = {"field": this.value, "field_2": 987}'

```

## [Anchor](https://qdrant.tech/documentation/data-management/redpanda/\#further-reading) Further Reading

- [Getting started with Connect](https://docs.redpanda.com/redpanda-connect/guides/getting_started/)
- [Qdrant Output Reference](https://docs.redpanda.com/redpanda-connect/components/outputs/qdrant/)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/redpanda.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/data-management/redpanda.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574256914&cv=11&fst=1748574256914&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fredpanda%2F&hn=www.googleadservices.com&frm=0&tiba=Redpanda%20Connect%20-%20Qdrant&npa=0&pscdl=noapi&auid=1584296724.1748574257&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574256880&cv=11&fst=1748574256880&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244~103308615&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fredpanda%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Redpanda%20Connect%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1584296724.1748574257&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1f4730a3-a15f-49d6-b4df-4622a8ba271b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=92595304-a35d-4f60-bf61-3692b2d6a1b7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fredpanda%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=1f4730a3-a15f-49d6-b4df-4622a8ba271b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=92595304-a35d-4f60-bf61-3692b2d6a1b7&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fredpanda%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574257879&cv=11&fst=1748574257879&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~104612242~104612244&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fdata-management%2Fredpanda%2F&hn=www.googleadservices.com&frm=0&tiba=Redpanda%20Connect%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1584296724.1748574257&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)