---
url: "https://qdrant.tech/documentation/observability/datadog/"
title: "Datadog - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Observability](https://qdrant.tech/documentation/observability/)
- Datadog

![Datadog Cover](https://qdrant.tech/documentation/observability/datadog/datadog-cover.jpg)

[Datadog](https://www.datadoghq.com/) is a cloud-based monitoring and analytics platform that offers real-time monitoring of servers, databases, and numerous other tools and services. It provides visibility into the performance of applications and enables businesses to detect issues before they affect users.

You can install the [Qdrant integration](https://docs.datadoghq.com/integrations/qdrant/) to get real-time metrics to monitor your Qdrant deployment within Datadog including:

- The performance of REST and gRPC interfaces with metrics such as total requests, total failures, and time to serve to identify potential bottlenecks and mitigate them.

- Information about the readiness of the cluster, and deployment (total peers, pending operations, etc.) to gain insights into your Qdrant deployment.


### [Anchor](https://qdrant.tech/documentation/observability/datadog/\#usage) Usage

- With the [Datadog Agent installed](https://docs.datadoghq.com/agent/basic_agent_usage), run the following command to add the Qdrant integration:

```shell
datadog-agent integration install -t qdrant==1.0.0

```

- Edit the `conf.d/qdrant.d/conf.yaml` file in your [Agent’s configuration directory](https://docs.datadoghq.com/agent/guide/agent-configuration-files/#agent-configuration-directory) to start collecting your [Qdrant metrics](https://qdrant.tech/documentation/guides/monitoring/).

Most importantly, set the `openmetrics_endpoint` value to the `/metrics` endpoint of your Qdrant instance.

```yaml
instances:
    ## @param openmetrics_endpoint - string - optional
    ## The URL exposing metrics in the OpenMetrics format.
  - openmetrics_endpoint: http://localhost:6333/metrics

```

If the Qdrant instance requires authentication, you can specify the token by configuring [`extra_headers`](https://github.com/DataDog/integrations-core/blob/26f9ae7660f042c43f5d771f0c937ff805cf442c/openmetrics/datadog_checks/openmetrics/data/conf.yaml.example#L553C1-L558C35).

```yaml
# @param extra_headers - mapping - optional
# Additional headers to send with every request.
extra_headers:
   api-key: <QDRANT_API_KEY>

```

- Restart the Datadog agent.

- You can now head over to the Datadog dashboard to view the [metrics](https://docs.datadoghq.com/integrations/qdrant/#data-collected) emitted by the Qdrant check.


## [Anchor](https://qdrant.tech/documentation/observability/datadog/\#further-reading) Further Reading

- [Getting started with Datadog](https://docs.datadoghq.com/getting_started/)
- [Qdrant integration source](https://github.com/DataDog/integrations-extras/tree/master/qdrant)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/observability/datadog.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/observability/datadog.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574655834&cv=11&fst=1748574655834&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fdatadog%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Datadog%20-%20Qdrant&npa=0&pscdl=noapi&auid=173314197.1748574656&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574655770&cv=11&fst=1748574655770&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fdatadog%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Datadog%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=173314197.1748574656&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0c6007b9-a7c4-4379-a46c-1e0fb5e4678f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1542b552-4500-4bbb-850b-f1ae63b9f9e2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fdatadog%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0c6007b9-a7c4-4379-a46c-1e0fb5e4678f&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=1542b552-4500-4bbb-850b-f1ae63b9f9e2&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fdatadog%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574656777&cv=11&fst=1748574656777&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fdatadog%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Datadog%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=173314197.1748574656&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)