---
url: "https://qdrant.tech/documentation/cloud/create-cluster/"
title: "Create a Cluster - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud](https://qdrant.tech/documentation/cloud/)
- Create a Cluster

# [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#creating-a-qdrant-cloud-cluster) Creating a Qdrant Cloud Cluster

Qdrant Cloud offers two types of clusters: **Free** and **Standard**.

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#free-clusters) Free Clusters

Free tier clusters are perfect for prototyping and testing. You don’t need a credit card to join.

A free tier cluster only includes 1 single node with the following resources:

| Resource | Value |
| --- | --- |
| RAM | 1 GB |
| vCPU | 0.5 |
| Disk space | 4 GB |
| Nodes | 1 |

This configuration supports serving about 1 M vectors of 768 dimensions. To calculate your needs, refer to our documentation on [Capacity Planning](https://qdrant.tech/documentation/guides/capacity-planning/).

The choice of cloud providers and regions is limited.

It includes:

- Standard Support
- Basic monitoring
- Basic log access
- Basic alerting
- Version upgrades with downtime
- Only manual snapshots and restores via API
- No dedicated resources

If unused, free tier clusters are automatically suspended after 1 week, and deleted after 4 weeks of inactivity if not reactivated.

You can always upgrade to a standard cluster with more resources and features.

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#standard-clusters) Standard Clusters

On top of the Free cluster features, Standard clusters offer:

- Response time and uptime SLAs
- Dedicated resources
- Backup and disaster recovery
- Multi-node clusters for high availability
- Horizontal and vertical scaling
- Monitoring and log management
- Zero-downtime upgrades for multi-node clusters with replication

You have a broad choice of regions on AWS, Azure and Google Cloud.

For payment information see [**Pricing and Payments**](https://qdrant.tech/documentation/cloud/pricing-payments/).

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#create-a-cluster) Create a Cluster

![Create Cluster Page](https://qdrant.tech/documentation/cloud/create-cluster.png)

This page shows you how to use the Qdrant Cloud Console to create a custom Qdrant Cloud cluster.

> **Prerequisite:** Please make sure you have provided billing information before creating a custom cluster.

01. Start in the **Clusters** section of the [Cloud Dashboard](https://cloud.qdrant.io/?ajs_anonymous_id=dfa44255-2ed7-4465-b202-8c934f5d1619).

02. Select **Clusters** and then click **\+ Create**.

03. In the **Create a cluster** screen select **Free** or **Standard**
    Most of the remaining configuration options are only available for standard clusters.

04. Select a provider. Currently, you can deploy to:

    - Amazon Web Services (AWS)
    - Google Cloud Platform (GCP)
    - Microsoft Azure
    - Your own [Hybrid Cloud](https://qdrant.tech/documentation/hybrid-cloud/) Infrastructure
05. Choose your data center region or Hybrid Cloud environment.

06. Configure RAM for each node.


    > For more information, see our [Capacity Planning](https://qdrant.tech/documentation/guides/capacity-planning/) guidance.

07. Choose the number of vCPUs per node. If you add more
    RAM, the menu provides different options for vCPUs.

08. Select the number of nodes you want the cluster to be deployed on.


    > Each node is automatically attached with a disk, that has enough space to store data with Qdrant’s default collection configuration.

09. Select additional disk space for your deployment.


    > Depending on your collection configuration, you may need more disk space per RAM. For example, if you configure `on_disk: true` and only use RAM for caching.

10. Review your cluster configuration and pricing.

11. When you’re ready, select **Create**. It takes some time to provision your cluster.


Once provisioned, you can access your cluster on ports 443 and 6333 (REST) and 6334 (gRPC).

![Cluster configured in the UI](https://qdrant.tech/documentation/cloud/cluster-detail.png)

You should now see the new cluster in the **Clusters** menu.

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#deleting-a-cluster) Deleting a Cluster

You can delete a Qdrant database cluster from the cluster’s detail page.

![Delete Cluster](https://qdrant.tech/documentation/cloud/delete-cluster.png)

## [Anchor](https://qdrant.tech/documentation/cloud/create-cluster/\#next-steps) Next Steps

You will need to connect to your new Qdrant Cloud cluster. Follow [**Authentication**](https://qdrant.tech/documentation/cloud/authentication/) to create one or more API keys.

You can also scale your cluster both horizontally and vertically. Read more in [**Cluster Scaling**](https://qdrant.tech/documentation/cloud/cluster-scaling/).

If a new Qdrant version becomes available, you can upgrade your cluster. See [**Cluster Upgrades**](https://qdrant.tech/documentation/cloud/cluster-upgrades/).

For more information on creating and restoring backups of a cluster, see [**Backups**](https://qdrant.tech/documentation/cloud/backups/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/create-cluster.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/create-cluster.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574847382&cv=11&fst=1748574847382&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcreate-cluster%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Create%20a%20Cluster%20-%20Qdrant&npa=0&pscdl=noapi&auid=147247600.1748574847&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574847368&cv=11&fst=1748574847368&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcreate-cluster%2F&_ng=1&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Create%20a%20Cluster%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=147247600.1748574847&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0e296815-4d10-449e-b621-65946477ad40&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=2433fcfa-b7ca-4d03-a237-4cd36b28c8ee&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcreate-cluster%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=0e296815-4d10-449e-b621-65946477ad40&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=2433fcfa-b7ca-4d03-a237-4cd36b28c8ee&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcreate-cluster%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748574848550&cv=11&fst=1748574848550&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcreate-cluster%2F&_ng=1&hn=www.googleadservices.com&frm=0&tiba=Create%20a%20Cluster%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=147247600.1748574847&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)