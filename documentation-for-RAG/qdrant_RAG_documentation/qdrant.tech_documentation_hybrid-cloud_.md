---
url: "https://qdrant.tech/documentation/hybrid-cloud/"
title: "Hybrid Cloud - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- Hybrid Cloud

# [Anchor](https://qdrant.tech/documentation/hybrid-cloud/\#qdrant-hybrid-cloud) Qdrant Hybrid Cloud

Seamlessly deploy and manage your vector database across diverse environments, ensuring performance, security, and cost efficiency for AI-driven applications.

[Qdrant Hybrid Cloud](https://qdrant.tech/hybrid-cloud/) integrates Kubernetes clusters from any setting - cloud, on-premises, or edge - into a unified, enterprise-grade managed service.

You can use [Qdrant Cloud’s UI](https://qdrant.tech/documentation/cloud/create-cluster/) to create and manage your database clusters, while they still remain within your infrastructure. **All Qdrant databases will operate solely within your network, using your storage and compute resources. All user data will stay securely within your environment and won’t be accessible by the Qdrant Cloud platform, or anyone else outside your organization.**

Qdrant Hybrid Cloud ensures data privacy, deployment flexibility, low latency, and delivers cost savings, elevating standards for vector search and AI applications.

**How it works:** Qdrant Hybrid Cloud relies on Kubernetes and works with any standard compliant Kubernetes distribution. When you onboard a Kubernetes cluster as a Hybrid Cloud Environment, you can deploy the Qdrant Kubernetes Operator and Cloud Agent into this cluster. These will manage Qdrant databases within your Kubernetes cluster and establish an outgoing connection to Qdrant Cloud to transport telemetry and receive management instructions. You can then benefit from the same cloud management features and transport telemetry that is available with any managed Qdrant Cloud cluster.

**Setup instructions:** To begin using Qdrant Hybrid Cloud, [read our installation guide](https://qdrant.tech/documentation/hybrid-cloud/hybrid-cloud-setup/).

## [Anchor](https://qdrant.tech/documentation/hybrid-cloud/\#hybrid-cloud-architecture) Hybrid Cloud architecture

The Hybrid Cloud onboarding will install a Kubernetes Operator and Cloud Agent into your Kubernetes cluster.

The Cloud Agent will establish an outgoing connection to `cloud.qdrant.io` on port `443` to transport telemetry and receive management instructions. It will also interact with the Kubernetes API through a ServiceAccount to create, read, update and delete the necessary Qdrant CRs (Custom Resources) based on the configuration setup in the Qdrant Cloud Console.

The Qdrant Kubernetes Operator will manage the Qdrant databases within your Kubernetes cluster. Based on the Qdrant CRs, it will interact with the Kubernetes API through a ServiceAccount to create and manage the necessary resources to deploy and run Qdrant databases, such as Pods, Services, ConfigMaps, and Secrets.

Both component’s access is limited to the Kubernetes namespace that you chose during the onboarding process.

The Cloud Agent only sends telemetry data and status information to the Qdrant Cloud platform. It does not send any user data or sensitive information. The telemetry data includes:

- The health status and resource (CPU, memory, disk and network) usage of the Qdrant databases and Qdrant control plane components.
- Information about the Qdrant databases, such as the number, name and configuration of collections, the number of vectors, the number of queries, and the number of indexing operations.
- Telemetry and notification data from the Qdrant databases.
- Kubernetes operations and scheduling events reported for the Qdrant databases and Qdrant control plane components.

After the initial onboarding, the lifecycle of these components will be controlled by the Qdrant Cloud platform via the built-in Helm controller.

You don’t need to expose your Kubernetes Cluster to the Qdrant Cloud platform, you don’t need to open any ports for incoming traffic, and you don’t need to provide any Kubernetes or cloud provider credentials to the Qdrant Cloud platform.

![hybrid-cloud-architecture](https://qdrant.tech/blog/hybrid-cloud/hybrid-cloud-architecture.png)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/hybrid-cloud/_index.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/hybrid-cloud/_index.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574266361&cv=11&fst=1748574266361&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2F&hn=www.googleadservices.com&frm=0&tiba=Hybrid%20Cloud%20-%20Qdrant&npa=0&pscdl=noapi&auid=2045799469.1748574266&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574266347&cv=11&fst=1748574266347&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Hybrid%20Cloud%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=2045799469.1748574266&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=6908d0fe-9d87-4608-bf5a-385d4ae9a26b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d8aaad02-1990-4970-ab9a-036d420f6e57&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=6908d0fe-9d87-4608-bf5a-385d4ae9a26b&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=d8aaad02-1990-4970-ab9a-036d420f6e57&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574267333&cv=11&fst=1748574267333&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075~104612242~104612244&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fhybrid-cloud%2F&hn=www.googleadservices.com&frm=0&tiba=Hybrid%20Cloud%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=2045799469.1748574266&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)