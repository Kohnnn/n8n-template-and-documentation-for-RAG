---
url: "https://qdrant.tech/documentation/observability/openlit/"
title: "OpenLIT - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Observability](https://qdrant.tech/documentation/observability/)
- OpenLIT

# [Anchor](https://qdrant.tech/documentation/observability/openlit/\#openlit) OpenLIT

[OpenLIT](https://github.com/openlit/openlit) is an OpenTelemetry-native LLM Application Observability tool and includes OpenTelemetry auto-instrumentation to monitor Qdrant and provide insights to improve database operations and application performance.

This page assumes you’re using `qdrant-client` version 1.7.3 or above.

## [Anchor](https://qdrant.tech/documentation/observability/openlit/\#usage) Usage

### [Anchor](https://qdrant.tech/documentation/observability/openlit/\#step-1-install-openlit) Step 1: Install OpenLIT

Open your command line or terminal and run:

```bash
pip install openlit

```

### [Anchor](https://qdrant.tech/documentation/observability/openlit/\#step-2-initialize-openlit-in-your-application) Step 2: Initialize OpenLIT in your Application

Integrating OpenLIT into LLM applications is straightforward with just **two lines of code**:

```python
import openlit

openlit.init()

```

OpenLIT directs the trace to your console by default. To forward telemetry data to an HTTP OTLP endpoint, configure the `otlp_endpoint` parameter or the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable.

For OpenTelemetry backends requiring authentication, use the `otlp_headers` parameter or the `OTEL_EXPORTER_OTLP_HEADERS` environment variable with the required values.

## [Anchor](https://qdrant.tech/documentation/observability/openlit/\#further-reading) Further Reading

With the LLM Observability data now being collected by OpenLIT, the next step is to visualize and analyze this data to get insights Qdrant’s performance, behavior, and identify areas of improvement.

To begin exploring your LLM Application’s performance data within the OpenLIT UI, please see the [Quickstart Guide](https://docs.openlit.io/latest/quickstart).

If you want to integrate and send the generated metrics and traces to your existing observability tools like Promethues+Jaeger, Grafana or more, refer to the [Official Documentation for OpenLIT Connections](https://docs.openlit.io/latest/connections/intro) for detailed instructions.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/observability/openlit.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/observability/openlit.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574664457&cv=11&fst=1748574664457&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fopenlit%2F&hn=www.googleadservices.com&frm=0&tiba=OpenLIT%20-%20Qdrant&npa=0&pscdl=noapi&auid=1537168749.1748574664&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574664435&cv=11&fst=1748574664435&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fopenlit%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=OpenLIT%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1537168749.1748574664&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=74de1b3d-fcf4-49c8-9778-f6844c48ec4d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a0d21b5c-d5e6-4615-87d6-8fae8537aeed&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fopenlit%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=74de1b3d-fcf4-49c8-9778-f6844c48ec4d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=a0d21b5c-d5e6-4615-87d6-8fae8537aeed&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fopenlit%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574665663&cv=11&fst=1748574665663&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104573694&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fobservability%2Fopenlit%2F&hn=www.googleadservices.com&frm=0&tiba=OpenLIT%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1537168749.1748574664&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)