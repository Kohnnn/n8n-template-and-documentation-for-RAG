---
url: "https://qdrant.tech/documentation/cloud/cluster-scaling/"
title: "Scale Clusters - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud](https://qdrant.tech/documentation/cloud/)
- Scale Clusters

# [Anchor](https://qdrant.tech/documentation/cloud/cluster-scaling/\#scaling-qdrant-cloud-clusters) Scaling Qdrant Cloud Clusters

The amount of data is always growing and at some point you might need to upgrade or downgrade the capacity of your cluster.

![Cluster Scaling](https://qdrant.tech/documentation/cloud/cluster-scaling.png)

There are different options for how it can be done.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-scaling/\#vertical-scaling) Vertical Scaling

Vertical scaling is the process of increasing the capacity of a cluster by adding or removing CPU, storage and memory resources on each database node.

You can start with a minimal cluster configuration of 2GB of RAM and resize it up to 64GB of RAM (or even more if desired) over the time step by step with the growing amount of data in your application. If your cluster consists of several nodes each node will need to be scaled to the same size. Please note that vertical cluster scaling will require a short downtime period to restart your cluster. In order to avoid a downtime you can make use of data replication, which can be configured on the collection level. Vertical scaling can be initiated on the cluster detail page via the button “scale”.

If you want to scale your cluster down, the new, smaller memory size must be still sufficient to store all the data in the cluster. Otherwise, the database cluster could run out of memory and crash. Therefore, the new memory size must be at least as large as the current memory usage of the database cluster including a bit of buffer. Qdrant Cloud will automatically prevent you from scaling down the Qdrant database cluster with a too small memory size.

Note, that it is not possible to scale down the disk space of the cluster due to technical limitations of the underlying cloud providers.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-scaling/\#horizontal-scaling) Horizontal Scaling

Vertical scaling can be an effective way to improve the performance of a cluster and extend the capacity, but it has some limitations. The main disadvantage of vertical scaling is that there are limits to how much a cluster can be expanded. At some point, adding more resources to a cluster can become impractical or cost-prohibitive.

In such cases, horizontal scaling may be a more effective solution.

Horizontal scaling, also known as horizontal expansion, is the process of increasing the capacity of a cluster by adding more nodes and distributing the load and data among them. The horizontal scaling at Qdrant starts on the collection level. You have to choose the number of shards you want to distribute your collection around while creating the collection. Please refer to the [sharding documentation](https://qdrant.tech/documentation/guides/distributed_deployment/#sharding) section for details.

After that, you can configure, or change the amount of Qdrant database nodes within a cluster during cluster creation, or on the cluster detail page via “Scale” button.

Important: The number of shards means the maximum amount of nodes you can add to your cluster. In the beginning, all the shards can reside on one node. With the growing amount of data you can add nodes to your cluster and move shards to the dedicated nodes using the [cluster setup API](https://qdrant.tech/documentation/guides/distributed_deployment/#cluster-scaling).

When scaling down horizontally, the cloud platform will automatically ensure that any shards that are present on the nodes to be deleted, are moved to the remaining nodes.

We will be glad to consult you on an optimal strategy for scaling.

[Let us know](https://qdrant.tech/documentation/support/) your needs and decide together on a proper solution.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-scaling/\#resharding) Resharding

_Available as of Qdrant v1.13.0_

When creating a collection, it has a specific number of shards. The ideal number of shards might change as your cluster evolves.

Resharding allows you to change the number of shards in your existing collections, both up and down, without having to recreate the collection from scratch.

Resharding is a transparent process, meaning that the collection is still available while resharding is going on without having downtime. This allows you to scale from one node to any number of nodes and back, keeping your data perfectly distributed without compromise.

To increase the number of shards (reshard up), use the [Update collection cluster setup API](https://api.qdrant.tech/master/api-reference/distributed/update-collection-cluster) to initiate the resharding process:

```http
POST /collections/{collection_name}/cluster
{
    "start_resharding": {
        "direction": "up",
        "shard_key": null
    }
}

```

To decrease the number of shards (reshard down), you may specify the `"down"` direction.

The current status of resharding is listed in the [collection cluster info](https://api.qdrant.tech/v-1-12-x/api-reference/distributed/collection-cluster-info) which can be fetched with:

```http
GET /collections/{collection_name}/cluster

```

We always recommend to run an ongoing resharding operation till the end. But, if at any point the resharding operation needs to be aborted, you can use:

```http
POST /collections/{collection_name}/cluster
{
    "abort_resharding": {}
}

```

A few things to be aware of with regards to resharding:

- during resharding, performance of your cluster may be slightly reduced
- during resharding, reported point counts will not be accurate
- resharding may be a long running operation on huge collections
- you can only run one resharding operation per collection at a time

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-scaling.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-scaling.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7d10e393-d999-4f81-9775-0435535a8d42&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=16934986-c5d7-46b9-a110-9adeaae9585f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-scaling%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573611108&cv=11&fst=1748573611108&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-scaling%2F&hn=www.googleadservices.com&frm=0&tiba=Scale%20Clusters%20-%20Qdrant&npa=0&pscdl=noapi&auid=375414315.1748573611&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573611066&cv=11&fst=1748573611066&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-scaling%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Scale%20Clusters%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=375414315.1748573611&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573611195&cv=11&fst=1748573611195&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-scaling%2F&hn=www.googleadservices.com&frm=0&tiba=Scale%20Clusters%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=375414315.1748573611&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=7d10e393-d999-4f81-9775-0435535a8d42&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=16934986-c5d7-46b9-a110-9adeaae9585f&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-scaling%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)