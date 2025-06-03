---
url: "https://qdrant.tech/documentation/interfaces/"
title: "API & SDKs - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- API & SDKs

# [Anchor](https://qdrant.tech/documentation/interfaces/\#interfaces) Interfaces

Qdrant supports these “official” clients.

> **Note:** If you are using a language that is not listed here, you can use the REST API directly or generate a client for your language
> using [OpenAPI](https://github.com/qdrant/qdrant/blob/master/docs/redoc/master/openapi.json)
> or [protobuf](https://github.com/qdrant/qdrant/tree/master/lib/api/src/grpc/proto) definitions.

## [Anchor](https://qdrant.tech/documentation/interfaces/\#client-libraries) Client Libraries

|  | Client Repository | Installation | Version |
| --- | --- | --- | --- |
| [![python](https://qdrant.tech/docs/misc/python.webp)](https://python-client.qdrant.tech/) | **[Python](https://github.com/qdrant/qdrant-client)** \+ **[(Client Docs)](https://python-client.qdrant.tech/)** | `pip install qdrant-client[fastembed]` | [Latest Release](https://github.com/qdrant/qdrant-client/releases) |
| ![typescript](https://qdrant.tech/docs/misc/ts.webp) | **[JavaScript / Typescript](https://github.com/qdrant/qdrant-js)** | `npm install @qdrant/js-client-rest` | [Latest Release](https://github.com/qdrant/qdrant-js/releases) |
| ![rust](https://qdrant.tech/docs/misc/rust.png) | **[Rust](https://github.com/qdrant/rust-client)** | `cargo add qdrant-client` | [Latest Release](https://github.com/qdrant/rust-client/releases) |
| ![golang](https://qdrant.tech/docs/misc/go.webp) | **[Go](https://github.com/qdrant/go-client)** | `go get github.com/qdrant/go-client` | [Latest Release](https://github.com/qdrant/go-client/releases) |
| ![.net](https://qdrant.tech/docs/misc/dotnet.webp) | **[.NET](https://github.com/qdrant/qdrant-dotnet)** | `dotnet add package Qdrant.Client` | [Latest Release](https://github.com/qdrant/qdrant-dotnet/releases) |
| ![java](https://qdrant.tech/docs/misc/java.webp) | **[Java](https://github.com/qdrant/java-client)** | [Available on Maven Central](https://central.sonatype.com/artifact/io.qdrant/client) | [Latest Release](https://github.com/qdrant/java-client/releases) |

## [Anchor](https://qdrant.tech/documentation/interfaces/\#api-reference) API Reference

All interaction with Qdrant takes place via the REST API. We recommend using REST API if you are using Qdrant for the first time or if you are working on a prototype.

| API | Documentation |
| --- | --- |
| REST API | [OpenAPI Specification](https://api.qdrant.tech/api-reference) |
| gRPC API | [gRPC Documentation](https://github.com/qdrant/qdrant/blob/master/docs/grpc/docs.md) |

### [Anchor](https://qdrant.tech/documentation/interfaces/\#grpc-interface) gRPC Interface

The gRPC methods follow the same principles as REST. For each REST endpoint, there is a corresponding gRPC method.

As per the [configuration file](https://github.com/qdrant/qdrant/blob/master/config/config.yaml), the gRPC interface is available on the specified port.

```yaml
service:
  grpc_port: 6334

```

Running the service inside of Docker will look like this:

```bash
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant

```

**When to use gRPC:** The choice between gRPC and the REST API is a trade-off between convenience and speed. gRPC is a binary protocol and can be more challenging to debug. We recommend using gRPC if you are already familiar with Qdrant and are trying to optimize the performance of your application.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/interfaces.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/interfaces.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574344921&cv=11&fst=1748574344921&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Finterfaces%2F&hn=www.googleadservices.com&frm=0&tiba=API%20%26%20SDKs%20-%20Qdrant&npa=0&pscdl=noapi&auid=668004208.1748574345&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574344876&cv=11&fst=1748574344876&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Finterfaces%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=API%20%26%20SDKs%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=668004208.1748574345&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=691a70c8-246a-4d98-ba1b-5ec95c30fe8a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9e731488-e846-4371-ab17-704839a0049a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Finterfaces%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=691a70c8-246a-4d98-ba1b-5ec95c30fe8a&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9e731488-e846-4371-ab17-704839a0049a&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Finterfaces%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574345820&cv=11&fst=1748574345820&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Finterfaces%2F&hn=www.googleadservices.com&frm=0&tiba=API%20%26%20SDKs%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=668004208.1748574345&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)