---
url: "https://qdrant.tech/documentation/cloud/cluster-access/"
title: "Cluster Access - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud](https://qdrant.tech/documentation/cloud/)
- Cluster Access

# [Anchor](https://qdrant.tech/documentation/cloud/cluster-access/\#accessing-qdrant-cloud-clusters) Accessing Qdrant Cloud Clusters

Once you [created](https://qdrant.tech/documentation/cloud/create-cluster/) a cluster, and set up an [API key](https://qdrant.tech/documentation/cloud/authentication/), you can access your cluster through the integrated Cluster UI, the REST API and the GRPC API.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-access/\#cluster-ui) Cluster UI

There is the convenient link on the cluster detail page in the Qdrant Cloud Console to access the [Cluster UI](https://qdrant.tech/documentation/web-ui/).

![Cluster Cluster UI](https://qdrant.tech/documentation/cloud/cloud-db-dashboard.png)

The Overview tab also contains direct links to explore Qdrant tutorials and sample datasets.

![Cluster Cluster UI Tutorials](https://qdrant.tech/documentation/cloud/cloud-db-deeplinks.png)

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-access/\#api) API

The REST API is exposed on your cluster endpoint at port `6333`. The GRPC API is exposed on your cluster endpoint at port `6334`. When accessing the cluster endpoint, traffic is automatically load balanced across all healthy Qdrant nodes in the cluster. For all operations, but the few mentioned at [Node specific endpoints](https://qdrant.tech/documentation/cloud/cluster-access/#node-specific-endpoints), you should use the cluster endpoint. It does not matter which node in the cluster you land on. All nodes can handle all search and write requests.

![Cluster cluster endpoint](https://qdrant.tech/documentation/cloud/cloud-endpoint.png)

Have a look at the [API reference](https://qdrant.tech/documentation/interfaces/#api-reference) and the official [client libraries](https://qdrant.tech/documentation/interfaces/#client-libraries) for more information on how to interact with the Qdrant Cloud API.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-access/\#node-specific-endpoints) Node Specific Endpoints

Next to the cluster endpoint which loadbalances requests across all healthy Qdrant nodes, each node in the cluster has its own endpoint as well. This is mainly usefull for monitoring or manual shard management purpuses.

You can finde the node specific endpoints on the cluster detail page in the Qdrant Cloud Console.

![Cluster node endpoints](https://qdrant.tech/documentation/cloud/cloud-node-endpoints.png)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-access.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-access.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574765591&cv=11&fst=1748574765591&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075~103308613&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-access%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Cluster%20Access%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=62971504.1748574765&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574765715&cv=11&fst=1748574765715&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-access%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Cluster%20Access%20-%20Qdrant&npa=0&pscdl=noapi&auid=62971504.1748574765&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d4c7aa5b-2d82-486b-9576-ed42afc5323d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=095c9f4a-7658-470c-9c38-3c0140bd3c13&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-access%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=d4c7aa5b-2d82-486b-9576-ed42afc5323d&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=095c9f4a-7658-470c-9c38-3c0140bd3c13&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-access%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574766509&cv=11&fst=1748574766509&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~102015666~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-access%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Cluster%20Access%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=62971504.1748574765&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)