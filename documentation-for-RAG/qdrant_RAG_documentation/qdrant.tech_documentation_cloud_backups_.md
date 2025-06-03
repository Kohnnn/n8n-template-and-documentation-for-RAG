---
url: "https://qdrant.tech/documentation/cloud/backups/"
title: "Backup Clusters - Qdrant"
---

- [Documentation](https://qdrant.tech/documentation/)
- [Cloud](https://qdrant.tech/documentation/cloud/)
- Backup Clusters

# [Anchor](https://qdrant.tech/documentation/cloud/backups/\#backing-up-qdrant-cloud-clusters) Backing up Qdrant Cloud Clusters

Qdrant organizes cloud instances as clusters. On occasion, you may need to
restore your cluster because of application or system failure.

You may already have a source of truth for your data in a regular database. If you
have a problem, you could reindex the data into your Qdrant vector search cluster.
However, this process can take time. For high availability critical projects we
recommend replication. It guarantees the proper cluster functionality as long as
at least one replica is running.

For other use-cases such as disaster recovery, you can set up automatic or
self-service backups.

## [Anchor](https://qdrant.tech/documentation/cloud/backups/\#prerequisites) Prerequisites

You can back up your Qdrant clusters though the Qdrant Cloud
Dashboard at [https://cloud.qdrant.io](https://cloud.qdrant.io/). This section assumes that you’ve already
set up your cluster, as described in the following sections:

- [Create a cluster](https://qdrant.tech/documentation/cloud/create-cluster/)
- Set up [Authentication](https://qdrant.tech/documentation/cloud/authentication/)
- Configure one or more [Collections](https://qdrant.tech/documentation/concepts/collections/)

## [Anchor](https://qdrant.tech/documentation/cloud/backups/\#automatic-backups) Automatic Backups

You can set up automatic backups of your clusters with our Cloud UI. With the
procedures listed in this page, you can set up
snapshots on a daily/weekly/monthly basis. You can keep as many snapshots as you
need. You can restore a cluster from the snapshot of your choice.

> Note: When you restore a snapshot, consider the following:
>
> - The affected cluster is not available while a snapshot is being restored.
> - If you changed the cluster setup after the copy was created, the cluster
>   resets to the previous configuration.
> - The previous configuration includes:
>   - CPU
>   - Memory
>   - Node count
>   - Qdrant version

### [Anchor](https://qdrant.tech/documentation/cloud/backups/\#configure-a-backup) Configure a Backup

After you have taken the prerequisite steps, you can configure a backup with the
[Qdrant Cloud Dashboard](https://cloud.qdrant.io/). To do so, take these steps:

1. On the **Cluster Detail Page** and select the **Backups** tab.
2. Now you can set up a backup schedule.
The **Days of Retention** is the number of days after a backup snapshot is
deleted.
3. Alternatively, you can select **Backup now** to take an immediate snapshot.

![Configure a cluster backup](https://qdrant.tech/documentation/cloud/backup-schedule.png)

### [Anchor](https://qdrant.tech/documentation/cloud/backups/\#restore-a-backup) Restore a Backup

If you have a backup, it appears in the list of **Available Backups**. You can
choose to restore or delete the backups of your choice.

![Restore or delete a cluster backup](https://qdrant.tech/documentation/cloud/restore-delete.png)

## [Anchor](https://qdrant.tech/documentation/cloud/backups/\#backups-with-a-snapshot) Backups With a Snapshot

Qdrant also offers a snapshot API which allows you to create a snapshot
of a specific collection or your entire cluster. For more information, see our
[snapshot documentation](https://qdrant.tech/documentation/concepts/snapshots/).

Here is how you can take a snapshot and recover a collection:

1. Take a snapshot:
   - For a single node cluster, call the snapshot endpoint on the exposed URL.
   - For a multi node cluster call a snapshot on each node of the collection.
     Specifically, prepend `node-{num}-` to your cluster URL.
     Then call the [snapshot endpoint](https://qdrant.tech/documentation/concepts/snapshots/#create-snapshot) on the individual hosts. Start with node 0.
   - In the response, you’ll see the name of the snapshot.
2. Delete and recreate the collection.
3. Recover the snapshot:
   - Call the [recover endpoint](https://qdrant.tech/documentation/concepts/snapshots/#recover-in-cluster-deployment). Set a location which points to the snapshot file ( `file:///qdrant/snapshots/{collection_name}/{snapshot_file_name}`) for each host.

## [Anchor](https://qdrant.tech/documentation/cloud/backups/\#backup-considerations) Backup Considerations

Backups are incremental for AWS and GCP clusters. For example, if you have two backups, backup number 2
contains only the data that changed since backup number 1. This reduces the
total cost of your backups.

For Azure clusters, backups are based on total disk usage. The cost is calculated
as half of the disk usage when the backup was taken.

You can create multiple backup schedules.

When you restore a snapshot, any changes made after the date of the snapshot
are lost.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/backups.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/backups.md)
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

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573601528&cv=11&fst=1748573601528&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fbackups%2F&hn=www.googleadservices.com&frm=0&tiba=Backup%20Clusters%20-%20Qdrant&npa=0&pscdl=noapi&auid=1885481950.1748573601&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573601495&cv=11&fst=1748573601495&fmt=3&bg=ffffff&guid=ON&async=1&gcl_ctr=1&gtm=45be55s2v9117590405z8898302740za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fbackups%2F&label=_FJrCMev-7EDEND_w7so&hn=www.googleadservices.com&frm=0&tiba=Backup%20Clusters%20-%20Qdrant&value=0&bttype=purchase&npa=0&pscdl=noapi&auid=1885481950.1748573601&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&ec_mode=a&fledge=1&capi=1&_tu=Cg&em=tv.1&ct_cookie_present=0)![](https://t.co/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=f103cf91-f5cb-42aa-af30-8cfbd4df7930&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=52dd6e90-0440-4874-b095-74d2f01d4ae9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fbackups%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=America%2FAdak%26en-US%2Cen%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=f103cf91-f5cb-42aa-af30-8cfbd4df7930&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=52dd6e90-0440-4874-b095-74d2f01d4ae9&tw_document_href=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fbackups%2F&tw_iframe_status=0&txn_id=o81g6&type=javascript&version=2.3.33)

[iframe](https://td.doubleclick.net/td/rul/10862264272?random=1748573602592&cv=11&fst=1748573602592&fmt=3&bg=ffffff&guid=ON&async=1&gtm=45be55s2v9117590405za200zb898302740&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103130498~103130500~103200004~103233427~103252644~103252646~103351869~103351871~104481633~104481635~104559073~104559075&ptag_exp=101509157~103116026~103130498~103130500~103200004~103211513~103233427~103252644~103252646~103351866~103351868~104481633~104481635~104559073~104559075&u_w=1280&u_h=1024&url=https%3A%2F%2Fqdrant.tech%2Fdocumentation%2Fcloud%2Fbackups%2F&hn=www.googleadservices.com&frm=0&tiba=Backup%20Clusters%20-%20Qdrant&did=dZTQ1Zm&gdid=dZTQ1Zm&npa=0&pscdl=noapi&auid=1885481950.1748573601&uaa=x86&uab=64&uafvl=Google%2520Chrome%3B137.0.7151.55%7CChromium%3B137.0.7151.55%7CNot%252FA)Brand%3B24.0.0.0&uamb=0&uam=&uap=Linux%20x86_64&uapv=6.6.72&uaw=0&fledge=1&data=event%3Dgtag.config)