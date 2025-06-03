---
url: "https://qdrant.tech/documentation/cloud/cluster-monitoring/"
title: "Monitor Clusters - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud](https://qdrant.tech/documentation/cloud/)
- Monitor Clusters

# [Anchor](https://qdrant.tech/documentation/cloud/cluster-monitoring/\#monitoring-qdrant-cloud-clusters) Monitoring Qdrant Cloud Clusters

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-monitoring/\#telemetry) Telemetry

![Cluster Metrics](https://qdrant.tech/documentation/cloud/cluster-metrics.png)

Qdrant Cloud provides you with a set of metrics to monitor the health of your database cluster. You can access these metrics in the Qdrant Cloud Console in the **Metrics** and **Request** sections of the cluster details page.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-monitoring/\#logs) Logs

![Cluster Logs](https://qdrant.tech/documentation/cloud/cluster-logs.png)

Logs of the database cluster are available in the Qdrant Cloud Console in the **Logs** section of the cluster details page.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-monitoring/\#alerts) Alerts

You will receive automatic alerts via email before your cluster reaches the currently configured memory or storage limits, including recommendations for scaling your cluster.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-monitoring/\#qdrant-database-metrics-and-telemetry) Qdrant Database Metrics and Telemetry

You can also directly access the metrics and telemetry that the Qdrant database nodes provide.

To scrape metrics from a Qdrant cluster running in Qdrant Cloud, an [API key](https://qdrant.tech/documentation/cloud/authentication/) is required to access `/metrics` and `/sys_metrics`. Qdrant Cloud also supports supplying the API key as a [Bearer token](https://www.rfc-editor.org/rfc/rfc6750.html), which may be required by some providers.

### [Anchor](https://qdrant.tech/documentation/cloud/cluster-monitoring/\#qdrant-node-metrics) Qdrant Node Metrics

Metrics in a Prometheus compatible format are available at the `/metrics` endpoint of each Qdrant database node. When scraping, you should use the [node specific URLs](https://qdrant.tech/documentation/cloud/cluster-access/#node-specific-endpoints) to ensure that you are scraping metrics from all nodes in each cluster. For more information see [Qdrant monitoring](https://qdrant.tech/documentation/guides/monitoring/).

You can also access the `/telemetry` [endpoint](https://api.qdrant.tech/api-reference/service/telemetry) of your database. This endpoint is available on the cluster endpoint and provides information about the current state of the database, including the number of vectors, shards, and other useful information.

For more information, see [Qdrant monitoring](https://qdrant.tech/documentation/guides/monitoring/).

### [Anchor](https://qdrant.tech/documentation/cloud/cluster-monitoring/\#cluster-system-metrics) Cluster System Metrics

Cluster system metrics is a cloud-only endpoint that not only shares all the information about the database from `/metrics` but also provides additional operational data from our infrastructure about your cluster, including information from our load balancers, ingresses, and cluster workloads themselves.

Metrics in a Prometheus-compatible format are available at the `/sys_metrics` cluster endpoint. Database API Keys are used to authenticate access to cluster system metrics. `/sys_metrics` only need to be queried once per cluster on the main load-balanced cluster endpoint. You don’t need to scrape each cluster node individually, instead it will always provide metrics about all nodes.

## [Anchor](https://qdrant.tech/documentation/cloud/cluster-monitoring/\#grafana-dashboard) Grafana Dashboard

If you scrape your Qdrant Cluster system metrics into your own monitoring system, and your are using Grafana, you can use our [Grafana dashboard](https://github.com/qdrant/qdrant-cloud-grafana-dashboard) to visualize these metrics.

![Grafa dashboard](https://qdrant.tech/documentation/cloud/cloud-grafana-dashboard.png)

Qdrant's Full Observability with Monitoring - YouTube

Qdrant - Vector Database & Search Engine

7.91K subscribers

[Qdrant's Full Observability with Monitoring](https://www.youtube.com/watch?v=pKPP-tL5_6w)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=pKPP-tL5_6w&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F&embeds_referring_origin=https%3A%2F%2Fqdrant.tech)

0:00

0:00 / 2:31
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=pKPP-tL5_6w "Watch on YouTube")

### [Anchor](https://qdrant.tech/documentation/cloud/cluster-monitoring/\#cluster-system-mtrics-sys_metrics) Cluster System Mtrics `/sys_metrics`

In Qdrant Cloud, each Qdrant cluster will expose the following metrics. This endpoint is not available when running Qdrant open-source.

**List of metrics**

| Name | Type | Meaning |
| --- | --- | --- |
| app\_info | gauge | Information about the Qdrant server |
| app\_status\_recovery\_mode | gauge | If Qdrant is currently started in recovery mode |
| cluster\_commit |  |  |
| cluster\_enabled |  | Indicates wether multi-node clustering is enabled |
| cluster\_peers\_total | counter | Total number of cluster peers |
| cluster\_pending\_operations\_total | counter | Total number of pending operations in the cluster |
| cluster\_term |  |  |
| cluster\_voter |  |  |
| collection\_hardware\_metric\_cpu |  |  |
| collection\_hardware\_metric\_io\_read |  |  |
| collection\_hardware\_metric\_io\_write |  |  |
| collections\_total | counter | Number of collections |
| collections\_vector\_total | counter | Total number of vectors in all collections |
| container\_cpu\_cfs\_periods\_total |  |  |
| container\_cpu\_cfs\_throttled\_periods\_total | counter | Indicating that your CPU demand was higher than what your instance offers |
| container\_cpu\_usage\_seconds\_total | counter | Total CPU usage in seconds |
| container\_file\_descriptors |  |  |
| container\_fs\_reads\_bytes\_total | counter | Total number of bytes read by the container file system (disk) |
| container\_fs\_reads\_total | counter | Total number of read operations on the container file system (disk) |
| container\_fs\_writes\_bytes\_total | counter | Total number of bytes written by the container file system (disk) |
| container\_fs\_writes\_total | counter | Total number of write operations on the container file system (disk) |
| container\_memory\_cache | gauge | Memory used for cache in the container |
| container\_memory\_mapped\_file | gauge | Memory used for memory-mapped files in the container |
| container\_memory\_rss | gauge | Resident Set Size (RSS) - Memory used by the container excluding swap space used for caching |
| container\_memory\_working\_set\_bytes | gauge | Total memory used by the container, including both anonymous and file-backed memory |
| container\_network\_receive\_bytes\_total | counter | Total bytes received over the container’s network interface |
| container\_network\_receive\_errors\_total |  |  |
| container\_network\_receive\_packets\_dropped\_total |  |  |
| container\_network\_receive\_packets\_total |  |  |
| container\_network\_transmit\_bytes\_total | counter | Total bytes transmitted over the container’s network interface |
| container\_network\_transmit\_errors\_total |  |  |
| container\_network\_transmit\_packets\_dropped\_total |  |  |
| container\_network\_transmit\_packets\_total |  |  |
| kube\_persistentvolumeclaim\_info |  |  |
| kube\_pod\_container\_info |  |  |
| kube\_pod\_container\_resource\_limits | gauge | Response contains limits for CPU and memory of DB. |
| kube\_pod\_container\_resource\_requests | gauge | Response contains requests for CPU and memory of DB. |
| kube\_pod\_container\_status\_last\_terminated\_exitcode |  |  |
| kube\_pod\_container\_status\_last\_terminated\_reason |  |  |
| kube\_pod\_container\_status\_last\_terminated\_timestamp |  |  |
| kube\_pod\_container\_status\_ready |  |  |
| kube\_pod\_container\_status\_restarts\_total |  |  |
| kube\_pod\_container\_status\_running |  |  |
| kube\_pod\_container\_status\_terminated |  |  |
| kube\_pod\_container\_status\_terminated\_reason |  |  |
| kube\_pod\_created |  |  |
| kube\_pod\_info |  |  |
| kube\_pod\_start\_time |  |  |
| kube\_pod\_status\_container\_ready\_time |  |  |
| kube\_pod\_status\_initialized\_time |  |  |
| kube\_pod\_status\_phase | gauge | Pod status in terms of different phases (Failed/Running/Succeeded/Unknown) |
| kube\_pod\_status\_ready | gauge | Pod readiness state (unknown/false/true) |
| kube\_pod\_status\_ready\_time |  |  |
| kube\_pod\_status\_reason |  |  |
| kubelet\_volume\_stats\_capacity\_bytes | gauge | Amount of disk available |
| kubelet\_volume\_stats\_inodes | gauge | Amount of inodes available |
| kubelet\_volume\_stats\_inodes\_used | gauge | Amount of inodes used |
| kubelet\_volume\_stats\_used\_bytes | gauge | Amount of disk used |
| memory\_active\_bytes |  |  |
| memory\_allocated\_bytes |  |  |
| memory\_metadata\_bytes |  |  |
| memory\_resident\_bytes |  |  |
| memory\_retained\_bytes |  |  |
| qdrant\_cluster\_state |  |  |
| qdrant\_collection\_commit |  |  |
| qdrant\_collection\_config\_hnsw\_full\_ef\_construct |  |  |
| qdrant\_collection\_config\_hnsw\_full\_scan\_threshold |  |  |
| qdrant\_collection\_config\_hnsw\_m |  |  |
| qdrant\_collection\_config\_hnsw\_max\_indexing\_threads |  |  |
| qdrant\_collection\_config\_hnsw\_on\_disk |  |  |
| qdrant\_collection\_config\_hnsw\_payload\_m |  |  |
| qdrant\_collection\_config\_optimizer\_default\_segment\_number |  |  |
| qdrant\_collection\_config\_optimizer\_deleted\_threshold |  |  |
| qdrant\_collection\_config\_optimizer\_flush\_interval\_sec |  |  |
| qdrant\_collection\_config\_optimizer\_indexing\_threshold |  |  |
| qdrant\_collection\_config\_optimizer\_max\_optimization\_threads |  |  |
| qdrant\_collection\_config\_optimizer\_max\_segment\_size |  |  |
| qdrant\_collection\_config\_optimizer\_memmap\_threshold |  |  |
| qdrant\_collection\_config\_optimizer\_vacuum\_min\_vector\_number |  |  |
| qdrant\_collection\_config\_params\_always\_ram |  |  |
| qdrant\_collection\_config\_params\_on\_disk\_payload |  |  |
| qdrant\_collection\_config\_params\_product\_compression |  |  |
| qdrant\_collection\_config\_params\_read\_fanout\_factor |  |  |
| qdrant\_collection\_config\_params\_replication\_factor |  |  |
| qdrant\_collection\_config\_params\_scalar\_quantile |  |  |
| qdrant\_collection\_config\_params\_scalar\_type |  |  |
| qdrant\_collection\_config\_params\_shard\_number |  |  |
| qdrant\_collection\_config\_params\_vector\_size |  |  |
| qdrant\_collection\_config\_params\_write\_consistency\_factor |  |  |
| qdrant\_collection\_config\_quantization\_always\_ram |  |  |
| qdrant\_collection\_config\_quantization\_product\_compression |  |  |
| qdrant\_collection\_config\_quantization\_scalar\_quantile |  |  |
| qdrant\_collection\_config\_quantization\_scalar\_type |  |  |
| qdrant\_collection\_config\_wal\_capacity\_mb |  |  |
| qdrant\_collection\_config\_wal\_segments\_ahead |  |  |
| qdrant\_collection\_consensus\_thread\_status |  |  |
| qdrant\_collection\_is\_voter |  |  |
| qdrant\_collection\_number\_of\_collections | counter | Total number of collections in Qdrant |
| qdrant\_collection\_number\_of\_grpc\_requests | counter | Total number of gRPC requests on a collection |
| qdrant\_collection\_number\_of\_rest\_requests | counter | Total number of REST requests on a collection |
| qdrant\_collection\_pending\_operations | counter | Total number of pending operations on a collection |
| qdrant\_collection\_role |  |  |
| qdrant\_collection\_shard\_segment\_num\_indexed\_vectors |  |  |
| qdrant\_collection\_shard\_segment\_num\_points |  |  |
| qdrant\_collection\_shard\_segment\_num\_vectors |  |  |
| qdrant\_collection\_shard\_segment\_type |  |  |
| qdrant\_collection\_term |  |  |
| qdrant\_collection\_transfer |  |  |
| qdrant\_operator\_cluster\_info\_total |  |  |
| qdrant\_operator\_cluster\_phase | gauge | Information about the status of Qdrant clusters |
| qdrant\_operator\_cluster\_pod\_up\_to\_date |  |  |
| qdrant\_operator\_cluster\_restore\_info\_total |  |  |
| qdrant\_operator\_cluster\_restore\_phase |  |  |
| qdrant\_operator\_cluster\_scheduled\_snapshot\_info\_total |  |  |
| qdrant\_operator\_cluster\_scheduled\_snapshot\_phase |  |  |
| qdrant\_operator\_cluster\_snapshot\_duration\_sconds |  |  |
| qdrant\_operator\_cluster\_snapshot\_phase | gauge | Information about the status of Qdrant cluster backups |
| qdrant\_operator\_cluster\_status\_nodes |  |  |
| qdrant\_operator\_cluster\_status\_nodes\_ready |  |  |
| qdrant\_node\_rssanon\_bytes | gauge | Allocated memory without memory-mapped files. This is the hard metric on memory which will lead to an OOM if it goes over the limit |
| rest\_responses\_avg\_duration\_seconds |  |  |
| rest\_responses\_duration\_seconds\_bucket |  |  |
| rest\_responses\_duration\_seconds\_count |  |  |
| rest\_responses\_duration\_seconds\_sum |  |  |
| rest\_responses\_fail\_total |  |  |
| rest\_responses\_max\_duration\_seconds |  |  |
| rest\_responses\_min\_duration\_seconds |  |  |
| rest\_responses\_total |  |  |
| traefik\_service\_open\_connections |  |  |
| traefik\_service\_request\_duration\_seconds\_bucket |  |  |
| traefik\_service\_request\_duration\_seconds\_count |  |  |
| traefik\_service\_request\_duration\_seconds\_sum | gauge | Response contains list of metrics for each Traefik service. |
| traefik\_service\_requests\_bytes\_total |  |  |
| traefik\_service\_requests\_total | counter | Response contains list of metrics for each Traefik service. |
| traefik\_service\_responses\_bytes\_total |  |  |

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-monitoring.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/cluster-monitoring.md)
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

![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=12059ad1-a7b9-49d2-8700-b2d68091fc6e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ced57745-a01f-4be8-99ca-9dafb218cc6e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-monitoring%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=12059ad1-a7b9-49d2-8700-b2d68091fc6e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=ced57745-a01f-4be8-99ca-9dafb218cc6e&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fcluster-monitoring%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)