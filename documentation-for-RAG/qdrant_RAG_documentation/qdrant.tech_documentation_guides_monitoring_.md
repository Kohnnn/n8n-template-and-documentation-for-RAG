---
url: "https://qdrant.tech/documentation/guides/monitoring/"
title: "Monitoring & Telemetry - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Guides](https://qdrant.tech/documentation/guides/)
- Monitoring & Telemetry

# [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#monitoring--telemetry) Monitoring & Telemetry

Qdrant exposes its metrics in [Prometheus](https://prometheus.io/docs/instrumenting/exposition_formats/#text-based-format)/ [OpenMetrics](https://github.com/OpenObservability/OpenMetrics) format, so you can integrate them easily
with the compatible tools and monitor Qdrant with your own monitoring system. You can
use the `/metrics` endpoint and configure it as a scrape target.

Metrics endpoint: [http://localhost:6333/metrics](http://localhost:6333/metrics)

The integration with Qdrant is easy to
[configure](https://prometheus.io/docs/prometheus/latest/getting_started/#configure-prometheus-to-monitor-the-sample-targets)
with Prometheus and Grafana.

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#monitoring-multi-node-clusters) Monitoring multi-node clusters

When scraping metrics from multi-node Qdrant clusters, it is important to scrape from
each node individually instead of using a load-balanced URL. Otherwise, your metrics will appear inconsistent after each scrape.

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#monitoring-in-qdrant-cloud) Monitoring in Qdrant Cloud

Qdrant Cloud offers additional metrics and telemetry that are not available in the open-source version. For more information, see [Qdrant Cloud Monitoring](https://qdrant.tech/documentation/cloud/cluster-monitoring/).

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#exposed-metrics) Exposed metrics

There are two endpoints avaliable:

- `/metrics` is the direct endpoint of the underlying Qdrant database node.

- `/sys_metrics` is a Qdrant cloud-only endpoint that provides additional operational and infrastructure metrics about your cluster, like CPU, memory and disk utilisation, collection metrics and load balancer telemetry. For more information, see [Qdrant Cloud Monitoring](https://qdrant.tech/documentation/cloud/cluster-monitoring/).


### [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#node-metrics-metrics) Node metrics `/metrics`

Each Qdrant server will expose the following metrics.

| Name | Type | Meaning |
| --- | --- | --- |
| app\_info | gauge | Information about Qdrant server |
| app\_status\_recovery\_mode | gauge | If Qdrant is currently started in recovery mode |
| collections\_total | gauge | Number of collections |
| collections\_vector\_total | gauge | Total number of vectors in all collections |
| collections\_full\_total | gauge | Number of full collections |
| collections\_aggregated\_total | gauge | Number of aggregated collections |
| rest\_responses\_total | counter | Total number of responses through REST API |
| rest\_responses\_fail\_total | counter | Total number of failed responses through REST API |
| rest\_responses\_avg\_duration\_seconds | gauge | Average response duration in REST API |
| rest\_responses\_min\_duration\_seconds | gauge | Minimum response duration in REST API |
| rest\_responses\_max\_duration\_seconds | gauge | Maximum response duration in REST API |
| grpc\_responses\_total | counter | Total number of responses through gRPC API |
| grpc\_responses\_fail\_total | counter | Total number of failed responses through REST API |
| grpc\_responses\_avg\_duration\_seconds | gauge | Average response duration in gRPC API |
| grpc\_responses\_min\_duration\_seconds | gauge | Minimum response duration in gRPC API |
| grpc\_responses\_max\_duration\_seconds | gauge | Maximum response duration in gRPC API |
| cluster\_enabled | gauge | Whether the cluster support is enabled. 1 - YES |
| memory\_active\_bytes | gauge | Total number of bytes in active pages allocated by the application. [Reference](https://jemalloc.net/jemalloc.3.html#stats.active) |
| memory\_allocated\_bytes | gauge | Total number of bytes allocated by the application. [Reference](https://jemalloc.net/jemalloc.3.html#stats.allocated) |
| memory\_metadata\_bytes | gauge | Total number of bytes dedicated to allocator metadata. [Reference](https://jemalloc.net/jemalloc.3.html#stats.metadata) |
| memory\_resident\_bytes | gauge | Maximum number of bytes in physically resident data pages mapped. [Reference](https://jemalloc.net/jemalloc.3.html#stats.resident) |
| memory\_retained\_bytes | gauge | Total number of bytes in virtual memory mappings. [Reference](https://jemalloc.net/jemalloc.3.html#stats.retained) |
| collection\_hardware\_metric\_cpu | gauge | CPU measurements of a collection |

**Cluster-related metrics**

There are also some metrics which are exposed in distributed mode only.

| Name | Type | Meaning |
| --- | --- | --- |
| cluster\_peers\_total | gauge | Total number of cluster peers |
| cluster\_term | counter | Current cluster term |
| cluster\_commit | counter | Index of last committed (finalized) operation cluster peer is aware of |
| cluster\_pending\_operations\_total | gauge | Total number of pending operations for cluster peer |
| cluster\_voter | gauge | Whether the cluster peer is a voter or learner. 1 - VOTER |

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#telemetry-endpoint) Telemetry endpoint

Qdrant also provides a `/telemetry` endpoint, which provides information about the current state of the database, including the number of vectors, shards, and other useful information. You can find a full documentation of this endpoint in the [API reference](https://api.qdrant.tech/api-reference/service/telemetry).

## [Anchor](https://qdrant.tech/documentation/guides/monitoring/\#kubernetes-health-endpoints) Kubernetes health endpoints

_Available as of v1.5.0_

Qdrant exposes three endpoints, namely
[`/healthz`](http://localhost:6333/healthz),
[`/livez`](http://localhost:6333/livez) and
[`/readyz`](http://localhost:6333/readyz), to indicate the current status of the
Qdrant server.

These currently provide the most basic status response, returning HTTP 200 if
Qdrant is started and ready to be used.

Regardless of whether an [API key](https://qdrant.tech/documentation/guides/security/#authentication) is configured,
the endpoints are always accessible.

You can read more about Kubernetes health endpoints
[here](https://kubernetes.io/docs/reference/using-api/health-checks/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/monitoring.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/guides/monitoring.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573868521&cv=11&fst=1748573868521&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fmonitoring%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Monitoring%20%26%20Telemetry%20-%20Qdrant&npa=0&pscdl=noapi&auid=1334184856.1748573868&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573868467&cv=11&fst=1748573868467&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~102938614~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fmonitoring%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Monitoring%20%26%20Telemetry%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1334184856.1748573868&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d4489f8d-957b-41be-b5b9-042a6ed46f5f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4c7c099f-db27-47cd-82b3-a54f1e3af8f3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fmonitoring%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d4489f8d-957b-41be-b5b9-042a6ed46f5f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=4c7c099f-db27-47cd-82b3-a54f1e3af8f3&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fguides%2Fmonitoring%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)