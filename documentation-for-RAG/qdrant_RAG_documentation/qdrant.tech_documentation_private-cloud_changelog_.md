---
url: "https://qdrant.tech/documentation/private-cloud/changelog/"
title: "Changelog - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Private cloud](https://qdrant.tech/documentation/private-cloud/)
- Changelog

# [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#changelog) Changelog

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#170-2025-05-14) 1.7.0 (2025-05-14)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.16.3 |
| operator version | 2.4.2 |
| qdrant-cluster-manager version | v0.3.5 |

- Add optional automatic shard balancing
- Set strict mode by default for new clusters to only allow queries with payload filters on fields that are indexed

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#164-2025-04-17) 1.6.4 (2025-04-17)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.15.5 |
| operator version | 2.3.4 |
| qdrant-cluster-manager version | v0.3.4 |

- Fix bug in operator Helm chart that caused role binding generation to fail when using `watch.namespaces`

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#163-2025-03-28) 1.6.3 (2025-03-28)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.15.0 |
| operator version | 2.3.3 |
| qdrant-cluster-manager version | v0.3.4 |

- Performance and stability improvements for collection re-sharding

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#162-2025-03-21) 1.6.2 (2025-03-21)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.15.0 |
| operator version | 2.3.2 |
| qdrant-cluster-manager version | v0.3.3 |

- Allow disabling NetworkPolicy management in Qdrant Cluster operator

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#161-2025-03-14) 1.6.1 (2025-03-14)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.14.2 |
| operator version | 2.3.2 |
| qdrant-cluster-manager version | v0.3.3 |

- Add support for GPU instances
- Experimental support for automatic shard balancing

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#151-2025-03-04) 1.5.1 (2025-03-04)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.12.0 |
| operator version | 2.1.26 |
| qdrant-cluster-manager version | v0.3.2 |

- Fix scaling down clusters that have TLS with self-signed certificates configured
- Various performance improvements and stability fixes

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#150-2025-02-21) 1.5.0 (2025-02-21)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.12.0 |
| operator version | 2.1.26 |
| qdrant-cluster-manager version | v0.3.0 |

- Added support for P2P TLS configuration
- Faster node removal on scale down
- Various performance improvements and stability fixes

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#140-2025-01-23) 1.4.0 (2025-01-23)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.8.0 |
| operator version | 2.1.26 |
| qdrant-cluster-manager version | v0.3.0 |

- Support deleting peers on horizontal scale down, even if they are already offline
- Support removing partially deleted peers

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#130-2025-01-17) 1.3.0 (2025-01-17)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.8.0 |
| operator version | 2.1.21 |
| qdrant-cluster-manager version | v0.2.10 |

- Support for re-sharding with Qdrant >= 1.13.0

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#120-2025-01-16) 1.2.0 (2025-01-16)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.8.0 |
| operator version | 2.1.20 |
| qdrant-cluster-manager version | v0.2.9 |

- Performance and stability improvements

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#110-2024-12-03) 1.1.0 (2024-12-03)

\| qdrant-kubernetes-api version \| v1.6.4 \|
\| operator version \| 2.1.10 \|
\| qdrant-cluster-manager version \| v0.2.6 \|

- Activate cluster-manager for automatic shard replication

## [Anchor](https://qdrant.tech/documentation/private-cloud/changelog/\#100-2024-11-11) 1.0.0 (2024-11-11)

|  |  |
| --- | --- |
| qdrant-kubernetes-api version | v1.2.7 |
| operator version | 0.1.3 |
| qdrant-cluster-manager version | v0.2.4 |

- Initial release

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/changelog.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/changelog.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574908539&cv=11&fst=1748574908539&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fchangelog%2F&hn=www.googleadservices.com&frm=0&tiba=Changelog%20-%20Qdrant&npa=0&pscdl=noapi&auid=973247203.1748574908&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574908501&cv=11&fst=1748574908501&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fchangelog%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Changelog%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=973247203.1748574908&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d5574683-bf2d-4d3f-bb39-76437344ce11&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9df01a3b-2271-4146-8e13-76a1c3ebad8d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fchangelog%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d5574683-bf2d-4d3f-bb39-76437344ce11&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=9df01a3b-2271-4146-8e13-76a1c3ebad8d&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fchangelog%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574909368&cv=11&fst=1748574909368&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612245~104612247&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fprivate-cloud%2Fchangelog%2F&hn=www.googleadservices.com&frm=0&tiba=Changelog%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=973247203.1748574908&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)